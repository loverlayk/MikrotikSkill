# keymat-provider

> RouterOS directory reference for /system/keymat-provider.

-----------

## system/keymat-provider 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (qkd | hkdf)"></ArgTableRow>
<ArgTableRow arg="key-size" typ="num">in bits</ArgTableRow>
<ArgTableRow arg="qkd-address" typ="string">KME device address</ArgTableRow>
<ArgTableRow arg="qkd-kme-id" typ="string">should match the KME ID in the received TLS certificate</ArgTableRow>
<ArgTableRow arg="qkd-certificate" typ="enum (none)">this also specifies your SAE ID</ArgTableRow>
<ArgTableRow arg="qkd-peer-sae-id" typ="string">peer (master or slave) SAE ID</ArgTableRow>
<ArgTableRow arg="qkd-cache-size" typ="num">number of unused keys to keep in cache</ArgTableRow>
<ArgTableRow arg="hkdf-secret" typ="string"></ArgTableRow>
<ArgTableRow arg="hkdf-hash" typ="enum (sha256 | sha512)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="qkd-cache-state" typ="num">number of current unused keys in cache</ArgTableRow>
<ArgTableRow arg="qkd-total-keys-received" typ="num">total number of received keys</ArgTableRow>
</ArgTable>
