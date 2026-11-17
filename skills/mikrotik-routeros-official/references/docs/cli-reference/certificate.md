# certificate

> RouterOS directory reference for /certificate.

-----------

## certificate 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="K" typ="private-key">private-key</ArgTableRow>
<ArgTableRow arg="L" typ="crl">crl</ArgTableRow>
<ArgTableRow arg="C" typ="smart-card-key">smart-card-key</ArgTableRow>
<ArgTableRow arg="A" typ="authority">authority</ArgTableRow>
<ArgTableRow arg="I" typ="issued">issued</ArgTableRow>
<ArgTableRow arg="R" typ="revoked">revoked</ArgTableRow>
<ArgTableRow arg="E" typ="expired">expired</ArgTableRow>
<ArgTableRow arg="T" typ="trusted">trusted</ArgTableRow>
<ArgTableRow arg="a" typ="acme-managed">acme-managed</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="active" typ="switch"></ArgTableRow>
<ArgTableRow arg="inactive" typ="switch"></ArgTableRow>
<ArgTableRow arg="name" typ="string">Name of the certificate or template in the store.</ArgTableRow>
<ArgTableRow arg="pem" typ="string">import certificate or unencrypted private key from a pasted PEM string</ArgTableRow>
<ArgTableRow arg="trust-store" typ="alt { all: enum (all)
, component: ubit (ipsec, wpa-eap, capsman, fetch, sstp, ovpn, mqtt, email, netwatch, radius, container, userman, lora, wiliot, openflow, tr069, dot1x, dns, www, api, reverse-proxy, logging)
 }">Services that use the certificate as a trusted authority. Default: `all`.</ArgTableRow>
<ArgTableRow arg="digest-algorithm" typ="enum (md5 | sha1 | sha256 | sha384 | sha512)">Hash algorithm of the certificate signature. Default: `sha256`.</ArgTableRow>
<ArgTableRow arg="trusted" typ="bool">Whether services trust the certificate as an authority. A self-signed authority created on the router and an imported certificate are trusted by default. A certificate issued by an authority on the router is not.</ArgTableRow>
<ArgTableRow arg="common-name" typ="string">Common name (CN) of the subject.</ArgTableRow>
<ArgTableRow arg="organization" typ="string"></ArgTableRow>
<ArgTableRow arg="unit" typ="string"></ArgTableRow>
<ArgTableRow arg="locality" typ="string"></ArgTableRow>
<ArgTableRow arg="state" typ="string"></ArgTableRow>
<ArgTableRow arg="country" typ="string"></ArgTableRow>
<ArgTableRow arg="subject-alt-name" typ="object { alt-name: composite { type: enum (IP | DNS | email)
, value: alt { ip: alt { ipv6: ip6Addr
, ip: ipAddr
 }
, string: string
 }
 }
 }">Subject alternative names as a list of `DNS:`, `IP:` and `email:` entries, for example `DNS:router.example.com,IP:192.168.88.1`.</ArgTableRow>
<ArgTableRow arg="key-size" typ="enum (prime256v1 | secp384r1 | secp521r1 | 1024 | 1536 | 2048 | 4096 | 8192) { 1024:1024, 1536:1536, 2048:2048, 4096:4096, 8192:8192 }">RSA key size in bits, or the name of an elliptic curve for an EC key. Default: `2048`.</ArgTableRow>
<ArgTableRow arg="key-usage" typ="ubit (digital-signature, content-commitment, key-encipherment, data-encipherment, key-agreement, key-cert-sign, crl-sign, encipher-only, decipher-only, tls-server, tls-client, code-sign, email-protect, timestamp, ocsp-sign, dvcs)">Allowed uses of the key. Default: `digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client`.</ArgTableRow>
<ArgTableRow arg="days-valid" typ="num">Number of days the certificate is valid from the time it is signed. Default: `365`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="ca-crl-host" typ="string">Host where this authority publishes its certificate revocation list.</ArgTableRow>
<ArgTableRow arg="ca" typ="enum">Authority on this router that issued the certificate.</ArgTableRow>
<ArgTableRow arg="scep-url" typ="string">URL of the SCEP server the certificate was enrolled from.</ArgTableRow>
<ArgTableRow arg="fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="req-fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="expires-after" typ="time">Time left until the certificate expires.</ArgTableRow>
<ArgTableRow arg="challenge-password" typ="string"></ArgTableRow>
<ArgTableRow arg="domain-names" typ="string">Domain names of the ACME certificate.</ArgTableRow>
<ArgTableRow arg="directory-url" typ="string">Directory URL of the ACME authority.</ArgTableRow>
<ArgTableRow arg="acme-status" typ="string">State of the ACME client. For an issued certificate, the time of the next renewal.</ArgTableRow>
<ArgTableRow arg="revoked" typ="date">Time when the certificate was revoked.</ArgTableRow>
<ArgTableRow arg="status" typ="string">State of the SCEP client.</ArgTableRow>
<ArgTableRow arg="issuer" typ="multi { array-id, issuer: string
 }">Subject of the authority that issued the certificate.</ArgTableRow>
<ArgTableRow arg="key-type" typ="enum (rsa | dsa | ec)">Type of the key.</ArgTableRow>
<ArgTableRow arg="invalid-before" typ="date">Start of the validity time.</ArgTableRow>
<ArgTableRow arg="invalid-after" typ="date">End of the validity time.</ArgTableRow>
<ArgTableRow arg="serial-number" typ="string">Serial number of the certificate.</ArgTableRow>
<ArgTableRow arg="akid" typ="string">Authority key identifier: the subject key identifier of the issuer.</ArgTableRow>
<ArgTableRow arg="skid" typ="string">Subject key identifier.</ArgTableRow>
</ArgTable>
