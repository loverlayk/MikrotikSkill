# builtin

> RouterOS directory reference for /certificate/builtin.

-----------

## certificate/builtin 
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
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
<ArgTableRow arg="issuer" typ="multi { array-id, issuer: string
 }"></ArgTableRow>
<ArgTableRow arg="key-type" typ="enum (rsa | dsa | ec)"></ArgTableRow>
<ArgTableRow arg="invalid-before" typ="date"></ArgTableRow>
<ArgTableRow arg="invalid-after" typ="date"></ArgTableRow>
<ArgTableRow arg="serial-number" typ="string"></ArgTableRow>
<ArgTableRow arg="akid" typ="string"></ArgTableRow>
<ArgTableRow arg="skid" typ="string"></ArgTableRow>
</ArgTable>
