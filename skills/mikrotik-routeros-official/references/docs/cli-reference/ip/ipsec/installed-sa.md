# installed-sa

> This menu provides information about installed security associations including the keys.

-----------

## ip/ipsec/installed-sa 
**Type:** Directory

This menu provides information about installed security associations including the keys.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="S" typ="seen-traffic">Whether traffic has passed through the SA.</ArgTableRow>
<ArgTableRow arg="H" typ="hw-aead">Whether hardware AEAD acceleration is used.</ArgTableRow>
<ArgTableRow arg="A" typ="AH">Whether the SA uses AH protocol.</ArgTableRow>
<ArgTableRow arg="E" typ="ESP">Whether the SA uses ESP protocol.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="spi" typ="num">Security Parameter Index value.</ArgTableRow>
<ArgTableRow arg="state" typ="enum (larval | mature | dying | dead) { larval:0, mature:1, dying:2, dead:3 }">Current SA state.</ArgTableRow>
<ArgTableRow arg="auth-algorithm" typ="enum (none | md5 | sha1 | sha256 | sha512) { none:0, md5:2, sha1:3, sha256:5, sha512:7 }">Authentication algorithm.</ArgTableRow>
<ArgTableRow arg="enc-algorithm" typ="enum (none | des | 3des | null | aes-cbc | aes-ctr | aes-gcm | blowfish | twofish | camellia | chacha20poly1305) { none:0, des:2, 3des:3, null:11, aes-cbc:12, aes-ctr:13, aes-gcm:20, blowfish:7, twofish:253, camellia:22, chacha20poly1305:254 }">Encryption algorithm.</ArgTableRow>
<ArgTableRow arg="enc-key-size" typ="num">Encryption key size in bits.</ArgTableRow>
<ArgTableRow arg="auth-key" typ="string">Authentication key value.</ArgTableRow>
<ArgTableRow arg="enc-key" typ="string">Encryption key value.</ArgTableRow>
<ArgTableRow arg="addtime" typ="date">Time when the SA was added.</ArgTableRow>
<ArgTableRow arg="expires-in" typ="time">Time until the SA expires.</ArgTableRow>
<ArgTableRow arg="add-lifetime" typ="composite { soft: time
, hard: time
 }">
Added lifetime for the SA in the format soft/hard:
- soft - time period after which IKE will try to establish a new SA;
- hard - time period after which the SA is deleted.
</ArgTableRow>
<ArgTableRow arg="current-bytes" typ="num">Number of bytes processed by the SA.</ArgTableRow>
<ArgTableRow arg="current-packets" typ="num">Number of packets processed by the SA.</ArgTableRow>
<ArgTableRow arg="invalid-packets" typ="num">Number of invalid packets.</ArgTableRow>
<ArgTableRow arg="replay" typ="num">Replay window size.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="src-address" typ="super { src-address: alt { ipv6: ip6Addr
, ip: ipAddr
 }
, [port] :num
 }">Source address and port.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { dst-address: alt { ipv6: ip6Addr
, ip: ipAddr
 }
, [port] :num
 }">Destination address and port.</ArgTableRow>
</ArgTable>
