# Certificates

> This page documents the Certificate management menu in MikroTik RouterOS, covering certificate template creation, configuration properties such as key size and usage, and certificate management including ACME client...

# Certificates

## Overview

**Sub-menu:** `/certificate`

The general menu is used to manage certificates, add templates, issue certificates, and manage CRL and SCEP Clients.

### Certificate Template

Certificate templates are used to prepare a desired certificate for signing.

The Certificate template is deleted right after a certificate is signed or a certificate request command is executed

```ros
/certificate
add name=CA-Template common-name=CAtemp key-usage=key-cert-sign,crl-sign
add name=Server common-name=server
add name=Client common-name=client
```

To print out certificates:

```ros
[admin@4k11] /certificate> print detail 
Flags: K - private-key; L - crl; C - smart-card-key; A - authority; I - issued, R - revoked; E - expired; T - trusted 
 0         name="CA-Template" key-type=rsa common-name="CAtemp" key-size=2048 subject-alt-name="" days-valid=365 key-usage=key-cert-sign,crl-sign 

 1         name="Server" key-type=rsa common-name="server" key-size=2048 subject-alt-name="" days-valid=365 
           key-usage=digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client 

 2         name="Client" key-type=rsa common-name="client" key-size=2048 subject-alt-name="" days-valid=365 
           key-usage=digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client 
```

#### Certificate template properties

During the certificate template creation process, it is possible to define and configure multiple parameters to meet specific requirements.

| Property | Description |
| :-- | :-- |
| **common-name** (*string*) | Certificate common name |
| **copy-from**(*name*) | Certificate name from which to copy general settings |
| **country** (*string*) | Certificate issuer country |
| **days-valid** (*days* Default: **365**) | Days certificate will be valid after signing |
| **digest-algorithm** (*md5 \| sha1 \| sha256 \| sha384 \| sha512* Default: **sha256**) | Hash algorithm used to sign the certificate. |
| **key-size** (*1024* \| *1536* \| *2048* \| *4096* \| *8192* \| *prime256v1* \| *secp384r1* \| *secp521r1* Default: **2048**) | Certificate public key size |
| **key-usage** (*code-sign* \| *crl-sign* \| *decipher-only* \| *dvcs* \| *encipher-only* \| *key-cert-sign* \| *ocsp-sign* \| *tls-client* \| *content-commitment* \| *data-encipherment* \| *digital-signature* \| *email-protect* \| *key-agreement* \| *key-encipherment* \| *timestamp* \| *tls-server* Default: **digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client)** | Certificate usage |
| **locality** (*string*) | Certificate issuer locality |
| **name** (*string*) | Certificate name |
| **organization** (*string*) | Certificate issuer organization |
| **state** (*string*) | Certificate issuer state |
| **subject-alt-name** (*DNS: \| IP: \| email:*) | Certificate subject alternative name |
| **trusted** (*no \| yes*) | Whether to trust certificate. If *yes,*certificate will be used for host certificate verification. |
| **trust-store**(*all* \| *capsman* \| *dns* \| *email* \| *ipsec* \| *mqtt* \| *openflow* \| *radius* \| *sstp* \| *userman* \| *www* \| *api* \| *container* \| *dot1x* \| *fetch* \| *lora* \| *netwatch* \| *ovpn* \| *tr069* \| *wpa-eap* \| *wiliot* \| *logging* Default: **all**) | Specify the service which can use a specific certificate for certificate verification or trust-chain creation (www, sstp). |
| **unit** (*string*) | Certificate issuer organizational unit |

### Certificate properties

For a signed certificate, most properties are read-only, with the exception of *name, trusted*, and *trust-store*.

| Property | Description |
| :-- | :-- |
| **acme-status** *(string)* | ACME client status |
| **common-name** (*string*) | Certificate common name |
| **copy-from**(*name*) | Certificate name from which to copy general settings |
| **country** (*string*) | Certificate issuer country |
| **days-valid** (*days*) | Days certificate will be valid after signing |
| **digest-algorithm** (*md5 \| sha1 \| sha256 \| sha384 \| sha512*) | Hash algorithm used to sign the certificate |
| **directory-url** *(string)* | ACME client directory URL |
| **domain-names** *(string)* | ACME client used domain names |
| **key-size** (*1024* \| *1536* \| *2048* \| *4096* \| *8192* \| *prime256v1* \| *secp384r1* \| *secp521r1*) | Certificate public key size |
| **key-usage** (*code-sign* \| *crl-sign* \| *decipher-only* \| *dvcs* \| *encipher-only* \| *key-cert-sign* \| *ocsp-sign* \| *tls-client* \| *content-commitment* \| *data-encipherment* \| *digital-signature* \| *email-protect* \| *key-agreement* \| *key-encipherment* \| *timestamp* \| *tls-server*) | Certificate usage |
| **locality** (*string*) | Certificate issuer locality |
| **organization** (*string*) | Certificate issuer organization |
| **revoked** *(date)* | Certificate revoke time (only for certificates that are signed and revoked in a specific device) |
| **state** (*string*) | Certificate issuer state |
| **subject-alt-name** (*DNS \| IP \| email*) | Certificate subject alternative name |
| **trusted** (*no \| yes*) | Whether to trust the certificate. If *yes*, certificate will be used for host certificate verification. |
| **trust-store**(*all* \| *capsman* \| *dns* \| *email* \| *ipsec* \| *mqtt* \| *openflow* \| *radius* \| *sstp* \| *userman* \| *www* \| *api* \| *container* \| *dot1x* \| *fetch* \| *lora* \| *netwatch* \| *ovpn* \| *tr069* \| *wpa-eap* \| *wiliot* \| *logging*) | Specify service which can use a specific certificate for certificate verification or trust-chain creation (www, sstp). |
| **unit** (*string*) | Certificate issuer organizational unit |
| **serial-number** (*string*) | Certificate serial number |
| **fingerprint** (*string*) | Certificate fingerprint |
| **akid** (*string*) | Certificate authority ID |
| **skid** (*string*) | Certificate subject ID |
| **issuer** (*string*) | Certificate Authority |
| **invalid-before** *(date)* | Date and time before which the certificate is not yet valid (validity start date). |
| **invalid-after** *(date)* | Date and time after which the certificate is no longer valid (expiration date). |
| **expires-after** *(time)* | Time left before expiration |
| **key-type** (*string*) | Private key type |
| **ca** *(string)* | CA certificate name (shown only for certificates that are signed in a specific device) |

:::warning
If the CA certificate is removed, all issued certificates in the chain are also removed.
:::

### Sign Certificate

Certificates should be signed. In the following example, we will sign certificates and add a CRL URL for the server certificate:

```ros
/certificate 
sign CA-Template 
sign Client      
sign Server ca-crl-host=192.168.88.1 name=ServerCA

```

Let's check if the certificates are signed:

```ros
[admin@MikroTik] /certificate> print
Flags: K - private-key; L - crl; A - authority; T - trusted
Columns: NAME, COMMON-name, FINGERPRINT
#        NAME         COMMON  FINGERPRINT                                                     
0  K AT  CA-Template  CAtemp  0c7aaa7607a4dde1bbf33deaae6be7bac9fe4064ba47d64e8a73dcefad6cfc38
1  K AT  Client       client  b3ff25ecb166ea41e15733a7493003f3ea66310c10390c33e98fe32364c3659f
2  KLAT  ServerCA     server  152b88c9d81f4b765a59e2302e01efd1fbf11ceeed6e59f4974e87787a5bb980

```

For a video example, click [here.](http://youtube.com/watch?v=i2A3YIQKfwY)

:::warning
The time of the key signing process depends on the key size of a specific certificate. With values of 4k and higher, it might take substantial time to sign this specific certificate on less powerful CPU-based devices.
:::

### Export Certificate

It is possible to export client certificates with keys and CA certificates in two formats - PEM or PKCS12.

| Property | Description |
| :-- | :-- |
| **export-passphrase** (*string* Default: **none**) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | Passphrase that will be used for exported certificate private key encryption. |
| **file-name** (*string* Default: **cert\_export\_[certificate name].crt/key/pkcs12**) | Exported certificate file name. |
| **type** (*pem \| pkcs12* Default: **pem**) | Exported certificate type.  In case of PEM, certificate will be exported with CRT extension, if export-passphrase is specified, also an encrypted private KEY file will be exported.  In case of PKCS12, certificate will be exported with P12 extension, if export-passphrase is specified, exported certificate will contain an encrypted private key. The PKCS12 file is encrypted using AES. |

```ros
/certificate 
export-certificate CA-Template 
export-certificate ServerCA export-passphrase=yourpassphrase
export-certificate Client export-passphrase=yourpassphrase
```

Exported certificates are available under the */file* section:

```ros
[admin@MikroTik] > file print
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME                         TYPE        SIZE  CREATION-TIME       
0  skins                        directory         2019-01-19 00:00:04
1  flash                        directory         2019-01-19 01:00:00
2  pub                          directory         2019-01-19 02:42:16
3  cert_export_CA-Template.crt  .crt file   1119  2019-01-19 04:15:21
4  cert_export_ServerCA.crt     .crt file   1229  2019-01-19 04:15:42
5  cert_export_ServerCA.key     .key file   1858  2019-01-19 04:15:42
6  cert_export_Client.crt       .crt file   1164  2019-01-19 04:15:55
7  cert_export_Client.key       .key file   1858  2019-01-19 04:15:55
```

:::warning
Exporting certificates requires "sensitive" user policy.
:::

### Import Certificate

To import certificates, certificates must be uploaded to a device using one of the file upload methods.

Certificates must be imported as a file.

Supported are PEM, DER, CRT, PKCS12 formats. PKCS12 import supports AES and 3DES decryption.

| Property | Description |
| :-- | :-- |
| **name** (*string* Default: **file-name\_number**) | A certificate name that will be shown in the certificate manager |
| **file-name** (*string*) | A file name that will be imported |
| **passphrase** (*string* Default: **none**) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | File passphrase if there is one |
| **trusted** (*yes \| no* Default: yes) | Adds *trusted* flag for the imported certificate |
| **trust-store**(*all* \| *capsman* \| *dns* \| *email* \| *ipsec* \| *mqtt* \| *openflow* \| *radius* \| *sstp* \| *userman* \| *www* \| *api* \| *container* \| *dot1x* \| *fetch* \| *lora* \| *netwatch* \| *ovpn* \| *tr069* \| *wpa-eap* \| *wiliot* \| *logging*  Default: **all**) | Specify the service which can use a specific certificate for certificate verification or trust-chain creation (www, sstp). |

```ros
[admin@MikroTik] > /certificate/import file-name=certificate_file_name name=name_example passphrase=file_passphrase
     certificates-imported: 2
     private-keys-imported: 1
            files-imported: 1
       decryption-failures: 0
  keys-with-no-certificate: 0

[admin@MikroTik] > /certificate/print 
Flags: K - PRIVATE-KEY; T - TRUSTED
Columns: NAME, COMMON-NAME
#    NAME            COMMON-NAME                                                  
0 KT name_example    cert    
1  T name_example_1  ca   
```

### CRL

RouterOS supports Certificate Revocation List (CRL) checking.

By default, CRL is not utilized, and certificates are not verified for revocation status.

Enable `crl-use=yes` in [certificate setting](#settings) to have the system verify every certificate in a chain against its CRL, and set `crl-download=yes` to let RouterOS automatically download and update CRLs.

CRL can be added manually by providing the CRL URL, or dynamically when importing a certificate that contains a CRL Distribution Point.

| Property | Description |
| :-- | :-- |
| **akid** (*string*) | CRL authority ID |
| **cert**(*string*) | Certificate (from certificate store) from which the CRL Distribution Point was added |
| **dynamic** (*flag*) | If CRL is dynamically added |
| **expired** (*flag*) | If CRL is expired |
| **fingerprint** (*string*) | CRL fingerprint |
| **Invalid** (*flag*) | If CRL is invalid (not updated) |
| **last-update** (*date*) | Date and time of last CRL update |
| **next-update** (*date*) | Date and time of next CRL update |
| **num** (*integer*) | CRL number |
| **removed** (*integer*) | Count of revoced certificates |
| **signature** (*string*) | CRL signature |
| **url** (*string*) | CRL URL |
| **num** (*integer*) | CRL number |

### Settings

`/certificate/settings` allows configuring [Certificate Revocation List](#crl) and [built-in trust store](#built-in-trust-store-authorities) settings.

| Property | Description |
| :-- | :-- |
| **builtin-trust-store** (*all* \| *default* \| *capsman* \| *dns* \| *email* \| *ipsec* \| *mqtt* \| *openflow* \| *radius* \| *sstp* \| *userman* \| *www* \| *api* \| *container* \| *dot1x* \| *fetch* \| *lora* \| *netwatch* \| *ovpn* \| *tr069* \| *wpa-eap* \| *wiliot* \| *logging* \| *untrusted* Default: **default**) | Services that can use [built-in trust store authorities](#built-in-trust-store-authorities) for certificate verification.  The current defaults: fetchmqttemailnetwatchcontainerloradnswwwreverse-proxy |
| **crl-download** (*yes \| no* Default: **no**) | Whether to automatically download/update CRL |
| **crl-store** (*ram \| system* Default: **ram**) | Where to store downloaded CRL information  CRL will be automatically renewed every hour for certificates which have "trusted=yes" using http protocol (ldap and ftp are currently unsupported) |
| **crl-use** (*yes \| no* Default: **no**) | Whether to use CRL |

:::warning
If *`/certificate/settings/set crl-use`* is set to *`yes`*, RouterOS will check CRL for each certificate in a certificate chain, therefore, an entire certificate chain should be installed into a device - starting from Root CA, intermediate CAs (if there are such), and certificate that is used for a specific service.
:::

An [example](http://youtube.com/watch?v=q9oMO3_jvBU) on importing a root certificate.

## ACME client

The ACME client automates the acquisition and renewal of multiple TLS certificates via ACME.

To add a new ACME client via CLI, use the command `/certificate/add-acme`.

Existing ACME clients appear in the Certificates view and are marked with the `a` (acme-manage) flag.

Domain names must resolve to the router, and TCP port 80 must be accessible from the WAN (the HTTP-01 challenge is used). For an IP Cloud `<id>.sn.mynetname.net` domain name, the DNS-01 challenge is used instead.

Certificates are automatically renewed when 80% of their validity period has elapsed.

If the certificate is not retrieved during the initial setup, a new ACME client must be added.

### Properties

| Property | Description |
| :-- | :-- |
| **directory-url** (*string*) | ACME directory URL |
| **domain-names** (*string*) | comma-separated list of domain names |
| **eab-hmac-key** (*string*) | HMAC key for ACME External Account Binding |
| **eab-kid** (*string*) | Key identifier |
| **name** (*string*) | ACME client name |

### Manual ACME renewal

To manually trigger ACME certificate renewal:

```ros
/certificate/acme-renew [name]
```

For example:

```ros
/certificate/acme-renew numbers=0
```

### Let's Encrypt certificate

To retrieve a Let's Encrypt certificate with automatic certificate renewal, you must manually provide a domain name with the `domain-names` parameter:

```ros
/certificate/add-acme domain-names=router.example.com
```

To generate a Let's Encrypt certificate for an [IP Cloud](../network-management/cloud/#ddns) name (for example, `example.sn.mynetname.net`), provide the `dns-name` from the `/ip/cloud` menu as the domain name, or read it inline with `[/ip/cloud/get dns-name]`:

```ros
/certificate/add-acme domain-names=[/ip/cloud/get dns-name]
```

:::info
The Let's Encrypt directory is used if `directory-url` is not provided.
:::

## SCEP

SCEP is using the HTTP protocol and base64 encoded GET requests. Most of the requests are without authentication and cipher, however, important ones can be protected if necessary (ciphered or signed using a received public key).

SCEP client in RouterOS will:

- Get CA certificate from CA server or RA (if used).
- User should compare the fingerprint of the CA certificate or if it comes from the right server.
- Generate a self-signed certificate with a temporary key.
- Send a certificate request to the server.
- If the server responds with status x, then the client keeps requesting until the server sends an error or approval.

The SCEP server supports the issuance of one certificate only. RouterOS also supports renew and next-ca options:

- renew - the possibility to renew the old certificate automatically with the same CA.
- next-ca - the possibility to change the current CA certificate to the new one.

The client polls the server for any changes, if the server advertises that the next-ca is available, then the client may request the next CA or wait until the CA almost expires and then request the next-ca.

The RouterOS client by default will try to use POST, AES, and SHA256 if the server advertises that. If the above algorithms are not supported, then the client will try to use 3DES, DES and SHA1, MD5.

:::warning
The SCEP client supports only RSA keys.
:::

SCEP certificates are renewed when 3/4 of their validity time has passed.

## Built-in trust store authorities

RouterOS contains a list of built-in root certificate authorities that specific services can use for host certificate verification.

SMIPS devices have a [reduced built-in CA trust store](#smips-built-in-cas).

The list of services that can use built-in root certificate authorities can be found in the [Settings](#settings) section.

It is possible to use [DoH](../network-management/dns) with certificate validation without the need to manually import the relevant root certificate.

The list of built-in root certificate authorities is accessible in System → Certificates → Built In CA, or at `/certificate/builtin/`.

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
