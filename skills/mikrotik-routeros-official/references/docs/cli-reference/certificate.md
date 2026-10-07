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
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="trust-store" typ="alt { all: enum (all)
, component: ubit (ipsec, wpa-eap, capsman, fetch, sstp, ovpn, mqtt, email, netwatch, radius, container, userman, lora, wiliot, openflow, tr069, dot1x, dns, www, api, reverse-proxy, logging)
 }"></ArgTableRow>
<ArgTableRow arg="digest-algorithm" typ="enum (md5 | sha1 | sha256 | sha384 | sha512)"></ArgTableRow>
<ArgTableRow arg="trusted" typ="bool"></ArgTableRow>
<ArgTableRow arg="common-name" typ="string"></ArgTableRow>
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
 }"></ArgTableRow>
<ArgTableRow arg="key-size" typ="enum (prime256v1 | secp384r1 | secp521r1 | 1024 | 1536 | 2048 | 4096 | 8192) { 1024:1024, 1536:1536, 2048:2048, 4096:4096, 8192:8192 }"></ArgTableRow>
<ArgTableRow arg="key-usage" typ="ubit (digital-signature, content-commitment, key-encipherment, data-encipherment, key-agreement, key-cert-sign, crl-sign, encipher-only, decipher-only, tls-server, tls-client, code-sign, email-protect, timestamp, ocsp-sign, dvcs)"></ArgTableRow>
<ArgTableRow arg="days-valid" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="ca-crl-host" typ="string"></ArgTableRow>
<ArgTableRow arg="ca" typ="enum"></ArgTableRow>
<ArgTableRow arg="scep-url" typ="string"></ArgTableRow>
<ArgTableRow arg="fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="req-fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="expires-after" typ="time"></ArgTableRow>
<ArgTableRow arg="challenge-password" typ="string"></ArgTableRow>
<ArgTableRow arg="domain-names" typ="string"></ArgTableRow>
<ArgTableRow arg="directory-url" typ="string"></ArgTableRow>
<ArgTableRow arg="acme-status" typ="string"></ArgTableRow>
<ArgTableRow arg="revoked" typ="date"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="issuer" typ="multi { array-id, issuer: string
 }"></ArgTableRow>
<ArgTableRow arg="key-type" typ="enum (rsa | dsa | ec)"></ArgTableRow>
<ArgTableRow arg="invalid-before" typ="date"></ArgTableRow>
<ArgTableRow arg="invalid-after" typ="date"></ArgTableRow>
<ArgTableRow arg="serial-number" typ="string"></ArgTableRow>
<ArgTableRow arg="akid" typ="string"></ArgTableRow>
<ArgTableRow arg="skid" typ="string"></ArgTableRow>
</ArgTable>
