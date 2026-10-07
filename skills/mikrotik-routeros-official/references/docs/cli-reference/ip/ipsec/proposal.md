# proposal

> Proposal information that will be sent by IKE daemons to establish SAs for certain policies.

-----------

## ip/ipsec/proposal 
**Type:** Directory

Proposal information that will be sent by IKE daemons to establish SAs for certain policies.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="*" typ="default">Whether the item is the default.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Proposal name.</ArgTableRow>
<ArgTableRow arg="auth-algorithms" typ="ubit (sha512, sha256, sha1, md5, null)">Allowed authentication algorithms. MD5 uses a 128-bit key, SHA1 uses a 160-bit key.</ArgTableRow>
<ArgTableRow arg="enc-algorithms" typ="ubit (chacha20poly1305, aes-256-cbc, aes-256-ctr, aes-256-gcm, camellia-256, aes-192-cbc, aes-192-ctr, aes-192-gcm, camellia-192, aes-128-cbc, aes-128-ctr, aes-128-gcm, camellia-128, 3des, blowfish, twofish, des, null)">Allowed encryption algorithms.</ArgTableRow>
<ArgTableRow arg="lifetime" typ="time">Phase 2 lifetime.</ArgTableRow>
<ArgTableRow arg="pfs-group" typ="enum (none | ecp256 | ecp384 | ecp521 | modp6144 | modp4096 | modp3072 | modp2048 | modp1536 | modp1024 | modp768) { none:0 }">Perfect Forward Secrecy group.</ArgTableRow>
</ArgTable>
