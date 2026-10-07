# profile

> Profiles define a set of parameters used for IKE negotiation during Phase 1. These parameters can be shared with other peer configurations.

-----------

## ip/ipsec/profile 
**Type:** Directory

Profiles define a set of parameters used for IKE negotiation during Phase 1. These parameters can be shared with other peer configurations.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">Whether the item is the default.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Profile name.</ArgTableRow>
<ArgTableRow arg="hash-algorithm" typ="enum (md5 | sha1 | sha256 | sha384 | sha512)">Hash algorithm.</ArgTableRow>
<ArgTableRow arg="prf-algorithm" typ="enum (auto | sha1 | sha256 | sha384 | sha512)">PRF algorithm (IKEv2 only).</ArgTableRow>
<ArgTableRow arg="enc-algorithm" typ="ubit (aes-256, aes-192, aes-128, 3des, des)">Encryption algorithm.</ArgTableRow>
<ArgTableRow arg="dh-group" typ="ubit (x25519, ecp256, ecp384, ecp521, modp6144, modp4096, modp3072, modp2048, modp1536, modp1024, modp768)">Diffie-Hellman group.</ArgTableRow>
<ArgTableRow arg="lifetime" typ="time">Phase 1 lifetime (IKEv1 only).</ArgTableRow>
<ArgTableRow arg="lifebytes" typ="num">Phase 1 lifetime in bytes (IKEv1 only). It is used only as an administrative value which is added to the proposal. Used in cases where the remote peer requires a specific lifebytes value to establish phase 1.</ArgTableRow>
<ArgTableRow arg="proposal-check" typ="enum (obey | strict | claim | exact) { obey:1, strict:2, claim:3, exact:4 }">
Phase 2 lifetime check logic:
- `claim` - take the shortest of proposed and configured lifetimes and notify the initiator about it.
- `exact` - require lifetimes to be the same.
- `obey` - accept whatever is sent by an initiator.
- `strict` - if the proposed lifetime is longer than the default then reject the proposal otherwise accept a proposed lifetime.
</ArgTableRow>
<ArgTableRow arg="nat-traversal" typ="bool">Use Linux NAT-T mechanism to solve IPsec incompatibility with NAT routers between IPsec peers. This can only be used with the ESP protocol (AH is not supported by design, as it signs the complete packet, including the IP header, which is changed by NAT, rendering the AH signature invalid). The method encapsulates IPsec ESP traffic into UDP streams in order to overcome some minor issues that make ESP incompatible with NAT.</ArgTableRow>
<ArgTableRow arg="ppk" typ="enum (no | psk | qkd | psk-ike-initial)">Post-quantum preshared key (IKEv2 only).</ArgTableRow>
<ArgTableRow arg="dpd-interval" typ="alt { special: enum (disable-dpd) { disable-dpd:0 }
, num: time [ .. 3600]
 }">Dead peer detection interval.</ArgTableRow>
<ArgTableRow arg="dpd-maximum-failures" typ="num">Maximum DPD failures before peer is considered dead (IKEv1 only).</ArgTableRow>
</ArgTable>
