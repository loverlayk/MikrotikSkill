# Certificates

> Certificates in MikroTik RouterOS: create a certificate authority and sign certificates on the router, use them for services, export and import them, trust other authorities, request certificates, check revocation...

# Certificates

RouterOS keeps certificates and their private keys in the `/certificate` menu. Services such as WebFig over HTTPS, the API, VPN servers and clients, CAPsMAN, RADIUS and Fetch refer to a certificate by its name, and verify the certificates of other devices against the authorities this menu trusts.

The page covers these tasks:

- Create a certificate authority (CA) on the router and sign server and client certificates.
- Assign a certificate to a service.
- Export certificates for other devices, and import certificates and keys.
- Trust the certificate authority of another device.
- Request a certificate from an authority outside the router.
- Revoke certificates and check certificate revocation lists (CRL).
- Enrol certificates automatically with the Simple Certificate Enrollment Protocol (SCEP).
- Get a public certificate with the Automatic Certificate Management Environment (ACME) client.

The examples use two devices. The router `192.168.88.1` is the certificate authority and the HTTPS server with the name `router.example.com`. A second RouterOS device in the same network is the client.

## Create a certificate authority and sign certificates

A certificate starts as a template. The `add` command creates the template with the subject and the key settings, and the `sign` command generates the key and turns the template into a certificate with the same name. A template signed without the `ca` parameter becomes a self-signed certificate. With `ca`, the named authority signs it.

Set `key-usage` in every template. A template without it gets all the default usages, which include the right to sign other certificates. An authority has `key-cert-sign` and `crl-sign`, a server certificate has `tls-server`, and a client certificate has `tls-client`.

Clients compare the name or address they connect to with the `subject-alt-name` of the server certificate. List every DNS name and IP address the server is reached by.

Create the authority, a certificate for the HTTPS server of the router, and a certificate for one client:

```ros
/certificate
add name=ca common-name="Example Root CA" days-valid=3650 \
    key-usage=key-cert-sign,crl-sign
sign ca ca-crl-host=192.168.88.1
add name=router common-name=router.example.com \
    subject-alt-name=DNS:router.example.com,IP:192.168.88.1 \
    key-usage=digital-signature,key-encipherment,tls-server
sign router ca=ca
add name=client1 common-name=client1 key-usage=tls-client
sign client1 ca=ca
```

The `ca-crl-host` parameter makes the authority publish a certificate revocation list. The router serves the list over HTTP at this address, and every certificate the authority signs carries the link to it. The `www` service of the router serves the list on TCP port 80: keep the service enabled and reachable for the devices that check the list.

Check the result:

```ros
[admin@MikroTik] > /certificate/print where name~"ca|router|client1"
Flags: K - PRIVATE-KEY; L - CRL; A - AUTHORITY; I - ISSUED; T - TRUSTED
Columns: NAME, TRUST-STORE, COMMON-NAME, SUBJECT-ALT-NAME
#       NAME     TRUST-STORE  COMMON-NAME         SUBJECT-ALT-NAME
1 KLA T ca       all          Example Root CA
2 K  I  router   all          router.example.com  DNS:router.example.com
                                                  IP:192.168.88.1
3 K  I  client1  all          client1
```

The authority has the flags `K` (the private key is on the router), `L` (it publishes a revocation list), `A` (authority) and `T` (trusted). RouterOS trusts a self-signed authority it created. The signed certificates have the flag `I` (issued) and are not trusted as authorities.

A template without `key-size` and `days-valid` gets a 2048-bit RSA key and is valid for 365 days. For an elliptic curve key, set `key-size` to a curve name, for example `key-size=prime256v1`.

:::warning
When you remove the authority certificate, RouterOS also removes all certificates it issued.
:::

## Assign a certificate to a service

Services take the certificate by name. Enable the HTTPS service of the router with the server certificate:

```ros
/ip/service
set www-ssl certificate=router disabled=no
```

Check that the service has the certificate:

```ros
[admin@MikroTik] > /ip/service/print where name=www-ssl
Columns: NAME, PORT, PROTO, CERTIFICATE, VRF, MAX-SESSIONS
# NAME     PORT  PROTO  CERTIFICATE  VRF   MAX-SESSIONS
0 www-ssl   443  tcp    router       main            20
```

Other services refer to certificates in the same way. For browser access to the router, see [WebFig](../management-tools/webfig#enable-https).

## Export certificates

Other devices need the certificate of the authority to verify the router, and a client needs its own certificate with the private key. Export the authority certificate without its key, and the client certificate with its key in a PKCS12 file:

```ros
/certificate
export-certificate ca file-name=example-ca
export-certificate client1 type=pkcs12 file-name=client1 \
    export-passphrase=Use-a-long-passphrase
```

The files appear in the file list:

```ros
[admin@MikroTik] > /file/print where name~"example-ca|client1"
Columns: NAME, TYPE, SIZE, LAST-MODIFIED
# NAME            TYPE       SIZE  LAST-MODIFIED
1 client1.p12     .p12 file  3316  2026-11-16 09:09:18
2 example-ca.crt  .crt file  1155  2026-11-16 09:09:18
```

- Without `export-passphrase`, the command exports only the certificate, as a PEM file with the `.crt` extension. The private key stays on the router.
- With `export-passphrase` and the default `type=pem`, the command also writes the private key to a `.key` file, encrypted with the passphrase.
- With `type=pkcs12`, the command writes one `.p12` file with the certificate, its private key and the certificate of the authority, encrypted with the passphrase (AES-256).
- Without `file-name`, the files are named `cert_export_<certificate name>`.

The `export-certificate` command requires the `sensitive` user policy. Download the files with one of the methods in [Files](../system-information-and-utilities/files), and delete them from the router afterwards.

## Trust a certificate authority

A device verifies a certificate only when it trusts the authority that signed it. On the second device, a download from the router with certificate checking fails with `no trusted CA certificate found` until the authority is imported.

Upload `example-ca.crt` to the second device and import it:

```ros
/certificate

     certificates-imported: 1
     private-keys-imported: 0
            files-imported: 0
       decryption-failures: 0
  keys-with-no-certificate: 0
```

The import deletes the file. The certificate is in the store with the `T` (trusted) flag:

```ros
[admin@MikroTik] > /certificate/print where name=example-ca
Flags: L - CRL; T - TRUSTED
Columns: NAME, TRUST-STORE, COMMON-NAME
#    NAME        TRUST-STORE  COMMON-NAME
0 LT example-ca  all          Example Root CA
```

The device has to resolve the name of the router. When no DNS server knows the name, add a static entry:

```ros
/ip/dns/static
add name=router.example.com address=192.168.88.1
```

Check that the device now verifies the router. The download succeeds only when the authority is trusted and the name in the URL is in the certificate:

```ros
/tool/fetch url=https://router.example.com/ output=none \
    check-certificate=yes
```

```text
  status: connecting

      status: finished
        code: 200
  downloaded: 1KiB
       total: 1KiB
    duration: 1s
```

A URL with a name that is not in the certificate fails with `name verification failed`.

### Limit the trust to some services

An imported certificate is trusted by all services. The `trust-store` property limits it to the listed services, and `trusted=no` removes the trust. Let only the `fetch` and `www` services use the authority:

```ros
/certificate
set example-ca trust-store=fetch,www
```

```ros
[admin@MikroTik] > /certificate/print where name=example-ca
Flags: L - CRL; T - TRUSTED
Columns: NAME, TRUST-STORE, COMMON-NAME
#    NAME        TRUST-STORE  COMMON-NAME
0 LT example-ca  fetch        Example Root CA
                 www
```

A service that is not in the list rejects certificates signed by this authority.

When you import a certificate that is not an authority, add `trusted=no` to the `import` command.

### Paste a certificate

A certificate in PEM format can be pasted into the command line instead of uploaded as a file. Put the whole text, with its line breaks, in quotes after `pem=`:

```ros
/certificate
add name=example-ca pem="-----BEGIN CERTIFICATE-----
MIIDKTCCAhGgAwIBAgIIYSWvMzKnLtQwDQYJKoZIhvcNAQELBQAwGjEYMBYGA1UE
...
+Aw0thQcxQIt2pwFk4LLhEQODijRmWjMPrjujInd9bMmzVJoBDeTZtCV39zv
-----END CERTIFICATE-----"
```

The example shows only the first and the last line of the certificate, with `...` for the lines between them. Paste your own certificate with all its lines. Without the line breaks the command fails with `bad PEM data`.

## Import a certificate with its private key

A PKCS12 file holds a certificate, its key and the authority. Upload `client1.p12` to the device and import it with the passphrase it was exported with:

```ros
/certificate

    passphrase=Use-a-long-passphrase trusted=no
     certificates-imported: 1
     private-keys-imported: 1
            files-imported: 1
       decryption-failures: 0
  keys-with-no-certificate: 0
```

The certificate has the `K` flag, so the device can use it to identify itself:

```ros
[admin@MikroTik] > /certificate/print where name~"client1|example"
Flags: K - PRIVATE-KEY; L - CRL; T - TRUSTED
Columns: NAME, TRUST-STORE, COMMON-NAME
#     NAME        TRUST-STORE  COMMON-NAME
1  LT example-ca  all          Example Root CA
2 K   client1     all          client1
```

For a certificate and a key in separate PEM files, import the certificate first and the key file second. The key is added to the certificate it belongs to. An encrypted key needs the `passphrase` parameter.

The `pem=` parameter accepts keys too, and one string can hold a certificate followed by its key. The `/certificate/import` command accepts an encrypted key together with `passphrase`. The `/certificate/add` command accepts only an unencrypted key.

To keep an imported private key on the device, add `no-key-export=yes` to the `import` command. An export of this certificate with a passphrase then fails with `Private key export is disallowed for this entry!`.

## Request a certificate from another authority

When the authority is outside the device, the device creates the key and a certificate request, and the authority signs the request. The private key stays with the device.

Create a template and the request on the device that needs the certificate:

```ros
/certificate
add name=office common-name=office.example.com \
    subject-alt-name=DNS:office.example.com \
    key-usage=digital-signature,key-encipherment,tls-server
create-certificate-request template=office \
    key-passphrase=Use-a-long-passphrase
```

The command writes two files: the request and the private key, encrypted with `key-passphrase`:

```ros
[admin@MikroTik] > /file/print where name~"certificate-request"
Columns: NAME, TYPE, SIZE, LAST-MODIFIED
# NAME                         TYPE       SIZE  LAST-MODIFIED
0 certificate-request_key.pem  .pem file  1834  2026-11-16 09:11:20
1 certificate-request.pem      .pem file  1017  2026-11-16 09:11:20
```

Send `certificate-request.pem` to the authority. Keep the key file on the device.

When the authority is a RouterOS router, upload the request to it, here as `office.csr`, and sign it:

```ros
/certificate
sign-certificate-request file-name=office.csr ca=ca
```

The new certificate gets the common name of the request as its name:

```ros
[admin@MikroTik] > /certificate/print where name~"office"
Flags: I - ISSUED
Columns: NAME, TRUST-STORE, COMMON-NAME, SUBJECT-ALT-NAME
#   NAME                TRUST-STORE  COMMON-NAME         SUBJECT-ALT-NAME
1 I office.example.com  all          office.example.com  DNS:office.example.com
```

Export it:

```ros
/certificate
export-certificate office.example.com file-name=office
```

Back on the requesting device, upload the signed certificate, here `office.crt`. Import the certificate, then the key file, and remove the template:

```ros
/certificate

    passphrase=Use-a-long-passphrase
remove office
```

The certificate has its private key:

```ros
[admin@MikroTik] > /certificate/print where name~"office"
Flags: K - PRIVATE-KEY
Columns: NAME, TRUST-STORE, COMMON-NAME, SUBJECT-ALT-NAME
#   NAME         TRUST-STORE  COMMON-NAME         SUBJECT-ALT-NAME
0 K office-cert  all          office.example.com  DNS:office.example.com
```

## Revoke a certificate and check revocation

An authority with `ca-crl-host` lists the certificates it has revoked. Other devices use the list only when revocation checking is on.

On the client, turn the checking on and download the lists:

```ros
/certificate/settings
set crl-use=yes crl-download=yes
/certificate/crl
download
```

RouterOS adds the list of an authority dynamically when the imported authority certificate contains a link to it. With `crl-use=yes`, a connection fails with `crl not found` as long as the list of the authority is not downloaded. The `crl-download` setting lets the device download and update the lists by itself, and the `download` command fetches them immediately.

On the authority, revoke the certificate:

```ros
/certificate
issued-revoke router
```

The certificate now has the `R` (revoked) flag:

```ros
[admin@MikroTik] > /certificate/print where name=router
Flags: K - PRIVATE-KEY; R - REVOKED
Columns: NAME, TRUST-STORE, COMMON-NAME, SUBJECT-ALT-NAME
#    NAME    TRUST-STORE  COMMON-NAME         SUBJECT-ALT-NAME
0 KR router  all          router.example.com  DNS:router.example.com
                                              IP:192.168.88.1
```

On the client, download the updated list. The `REVOKED` column shows how many certificates the list contains:

```ros
/certificate/crl
download
```

```ros
[admin@MikroTik] > /certificate/crl/print
Flags: D - DYNAMIC
Columns: CERT, TRUST-STORE, LAST-UPDATE, NUM, REVOKED
#   CERT        TRUST-STORE  LAST-UPDATE          NUM  REVOKED
0 D example-ca  all          2026-11-16 14:07:24    1        1
```

Check that the client now refuses the revoked certificate:

```ros
/tool/fetch url=https://router.example.com/ output=none \
    check-certificate=yes
```

```text
  status: connecting

      status: failed
  downloaded: 0KiB

failure: SSL: ssl: cert is revoked by crl - "CN=router.example.com" (6) (/tool/fetch; line 1)
```

The HTTPS service of the authority still uses the revoked certificate. Sign a new certificate and give it to the service:

```ros
/certificate
add name=router2 common-name=router.example.com \
    subject-alt-name=DNS:router.example.com,IP:192.168.88.1 \
    key-usage=digital-signature,key-encipherment,tls-server
sign router2 ca=ca
/ip/service
set www-ssl certificate=router2
```

The client accepts the new certificate:

```ros
[admin@MikroTik] > /tool/fetch url=https://router.example.com/ output=none \
    check-certificate=yes
  status: connecting

      status: finished
        code: 200
  downloaded: 1KiB
       total: 1KiB
    duration: 1s
```

A certificate issued by an authority that publishes a revocation list cannot be removed from the authority, only revoked.

## Enrol certificates with SCEP

With the Simple Certificate Enrollment Protocol (SCEP), a device creates its key, sends the request to the authority over HTTP and receives the signed certificate without file transfers. A RouterOS router can be the SCEP server and the SCEP client.

On the authority, add a SCEP server for the authority certificate:

```ros
/certificate/scep-server
add ca-cert=ca path=/scep/example days-valid=365
```

Clients reach the server at `http://192.168.88.1/scep/example`. The SCEP server also uses the `www` service on TCP port 80. If the service is disabled, the certificate on the client shows the `requesting-ca-capabilities-failed` status.

Generate a one-time password for the device you enrol. A request with a valid password is signed without confirmation:

```ros
[admin@MikroTik] > /certificate/scep-server/otp/generate minutes-valid=30
  password: a0209edb24f942297d5e
```

On the client, create a template and enrol it with the password:

```ros
/certificate
add name=branch common-name=branch.example.com \
    key-usage=digital-signature,key-encipherment,tls-client
add-scep template=branch challenge-password=a0209edb24f942297d5e \
    scep-url=http://192.168.88.1/scep/example
```

Check that the client has the certificate with its key:

```ros
[admin@MikroTik] > /certificate/print where name=branch
Flags: K - PRIVATE-KEY; T - TRUSTED
Columns: NAME, TRUST-STORE, COMMON-NAME
#    NAME    TRUST-STORE  COMMON-NAME
0 KT branch  all          branch.example.com
```

On the authority, the request is listed as authorized:

```ros
[admin@MikroTik] > /certificate/scep-server/requests/print
Columns: AUTHORITY, STATUS, COMMON-NAME, CREATED
#  AUTHORITY  STATUS      COMMON-NAME         CREATED
0  ca         authorized  branch.example.com  2026-11-16 09:12:37
```

A request without a password stays in the `pending` status. Approve it on the authority with `/certificate/scep-server/requests/grant`. The client collects the certificate the next time it asks the server.

## ACME client

The ACME client gets a certificate from a public certificate authority and renews it automatically. Browsers and other devices trust such a certificate without importing anything.

### Let's Encrypt certificate

The `add-acme` command requests the certificate. Without `directory-url`, the client uses Let's Encrypt.

For the [IP Cloud](../network-management/cloud/#ddns) name of the router, the client proves the ownership of the name through DNS, so no port has to be open from the internet. Enable the IP Cloud DDNS service first, then request the certificate:

```ros
/certificate
add-acme name=cloud-name domain-names=[/ip/cloud/get dns-name]
```

The certificate appears in `/certificate` with the flags `K` and `a` (ACME managed). Check its status. When the certificate is issued, the status shows the time of the next renewal:

```ros
[admin@MikroTik] > :put [/certificate/get cloud-name acme-status]
next update at 2027.01.27-07:09:16
```

The command also accepts the wildcard of the IP Cloud name, `*.<name>.sn.mynetname.net`. The certificate is then valid for every name under the IP Cloud name.

The client renews the certificate when 80 % of its validity time has passed. To renew it immediately, use `/certificate/acme-renew cloud-name`.

### Certificate for your own domain name

For a name that is not an IP Cloud name, the authority validates the name over HTTP. Three conditions have to be met:

- The name resolves to the public address of the router.
- The `www` service is enabled on TCP port 80.
- TCP port 80 of the router is reachable from the internet.

Request the certificate:

```ros
/certificate
add-acme name=public-name domain-names=router.example.com
```

Check the status in the same way as for the IP Cloud name. When the validation fails, the entry stays in `/certificate` with the error as its comment, for example `http-01 challenge validation failed`. Remove the entry, correct the cause and run `add-acme` again.

:::warning
An open TCP port 80 also makes the WebFig login page of the router reachable from the internet. When the IP Cloud name is enough, use it: it needs no open port.
:::

## Built-in trust store authorities

RouterOS contains a list of public root certificate authorities. Services use the list to verify public servers without importing a certificate, for example [Fetch](../system-information-and-utilities/fetch) with `check-certificate=yes` or [DNS over HTTPS](../network-management/dns).

The authorities are listed in `/certificate/builtin`.

### Settings

The `builtin-trust-store` setting in `/certificate/settings` selects the services that use the list:

- `default` - the services in the read-only `current-defaults` setting: `fetch`, `mqtt`, `email`, `netwatch`, `container`, `lora`, `wiliot`, `dns`, `www` and `reverse-proxy`.
- A list of services, for example `fetch,dns` - only these services.
- `untrusted` - no service. Every authority then has to be imported.

### List of built-in CAs

The following list of built-in CAs is available on all architectures except SMIPS.

| Organization | Common Name | Subject ID |
| :-- | :-- | :-- |
| Amazon | Amazon Root CA 1 | `8418CC8534ECBC0C94942E08599CC7B2104E0A08` |
| DigiCert Inc | DigiCert Assured ID Root CA | `45EBA2AFF492CB82312D518BA7A7219DF36DC80F` |
| DigiCert Inc | DigiCert Assured ID Root G2 | `CEC34AB99955F2B8DB60BFA97EBD56B59736A7D6` |
| DigiCert Inc | DigiCert Assured ID Root G3 | `CBD0BDA9E1980551A14D37A28379CE8D1D2AE484` |
| DigiCert Inc | DigiCert Global Root CA | `03DE503556D14CBB66F0A3E21B1BC397B23DD155` |
| DigiCert Inc | DigiCert Global Root G2 | `4E2254201895E6E36EE60FFAFAB912ED06178F39` |
| DigiCert Inc | DigiCert Global Root G3 | `B3DB48A4F9A1C5D8AE3641CC1163696229BC4BC6` |
| DigiCert Inc | DigiCert High Assurance EV Root CA | `B13EC36903F8BF4701D498261A0802EF63642BC3` |
| DigiCert, Inc. | DigiCert TLS ECC P384 Root G5 | `C151455059AB3EE72C5AFA2022120780887C116A` |
| DigiCert, Inc. | DigiCert TLS RSA4096 Root G5 | `51331CED3640AF17D325CD6968F2AF4E233EB341` |
| DigiCert Inc | DigiCert Trusted Root G4 | `ECD7E382D2715D644CDF2E673FE7BA98AE1C0F4F` |
| GlobalSign | GlobalSign | `3DE629489BEA07CA21444A26DE6EDED283D09F59` |
| GlobalSign nv-sa | GlobalSign Root CA | `607B661A450D97CA89502F7D04CD34A8FFFCFD4B` |
| GlobalSign | GlobalSign | `8FF04B7FA82E4524AE4D50FA639A8BDEE2DD1BBC` |
| GlobalSign | GlobalSign | `AE6C05A39313E2A2E7E2D71CD6C7F07FC86753A0` |
| GlobalSign nv-sa | GlobalSign Root E46 | `310A908FB6C69DD2444B80B5A2E61FB1124F1B95` |
| GlobalSign nv-sa | GlobalSign Root R46 | `035CAB738187A8CCB0A6D594E2369649FF05992C` |
| GoDaddy.com, Inc. | Go Daddy Root Certificate Authority - G2 | `3A9A8507106728B6EFF6BD05416E20C194DA0FDE` |
| SSL Corporation | SSL.com Root Certification Authority ECC | `82D1857330E73504D38E0292FBE5A4D1C421E8CD` |
| Sectigo Limited | Sectigo Public Server Authentication Root E46 | `D122DA4C59F14B5F2638AA9DD6EEEB0DC3FBA961` |
| Sectigo Limited | Sectigo Public Server Authentication Root R46 | `5673586495F9921AB0122A046279A14015882149` |
| The USERTRUST Network | USERTrust ECC Certification Authority | `3AE10986D4CF19C29676744976DCE035C663639A` |
| The USERTRUST Network | USERTrust RSA Certification Authority | `5379BF5AAA2B4ACF5480E1D89BC09DF2B20366CB` |
| Internet Security Research Group | ISRG Root X1 | `79B459E67BB6E5E40173800888C81A58F6E99B6E` |
| Internet Security Research Group | ISRG Root X2 | `7C4296AEDE4B483BFA92F89E8CCF6D8BA9723795` |
| ISRG | Root YE | `A3C8265A8EA14CD03563FC9B23C83AAE56F34F56` |
| ISRG | Root YR | `DEE75B60D0226D40287D3F0D01FEA4B552B45194` |

### SMIPS built-in CAs

SMIPS devices have a reduced built-in CA trust store:

| Organization | Common Name | Subject ID |
| :-- | :-- | :-- |
| DigiCert Inc | DigiCert Global Root G2 | `4E2254201895E6E36EE60FFAFAB912ED06178F39` |
| Internet Security Research Group | ISRG Root X1 | `79B459E67BB6E5E40173800888C81A58F6E99B6E` |
| Internet Security Research Group | ISRG Root X2 | `7C4296AEDE4B483BFA92F89E8CCF6D8BA9723795` |
| ISRG | Root YE | `A3C8265A8EA14CD03563FC9B23C83AAE56F34F56` |
| ISRG | Root YR | `DEE75B60D0226D40287D3F0D01FEA4B552B45194` |

## Technical details

- The `sign` command keeps the name of the template.
- An imported certificate is trusted unless the `import` command has `trusted=no`.
- The `import` command reports how many certificates and private keys it imported.
- A certificate with a weak RSA public exponent (7 or lower) continues to work. It is marked with the comment `key uses insecure RSA public exponent!` in `/certificate/print`. Replace such a certificate with one that has a stronger key.
- Certificate checks compare the validity dates with the clock of the device. Set the clock, for example with the [NTP client](../system-information-and-utilities/ntp), before you rely on them.

For all properties and commands, see [`/certificate`](../cli-reference/certificate/), [`/certificate/settings`](../cli-reference/certificate/settings), [`/certificate/crl`](../cli-reference/certificate/crl/), [`/certificate/builtin`](../cli-reference/certificate/builtin) and [`/certificate/scep-server`](../cli-reference/certificate/scep-server/) in the CLI reference.
