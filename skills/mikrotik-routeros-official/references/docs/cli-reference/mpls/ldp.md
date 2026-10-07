# ldp

> RouterOS directory reference for /mpls/ldp.

-----------

## mpls/ldp 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="lsr-id" typ="ipAddr" unset="1">Unique label switching router's ID.</ArgTableRow>
<ArgTableRow arg="path-vector-limit" typ="num" unset="1">Max path vector limit used for loop detection. Works in combination with the `loop-detect` property.</ArgTableRow>
<ArgTableRow arg="hop-limit" typ="num" unset="1">Max hop limit used for loop detection. Works in combination with the `loop-detect` property.</ArgTableRow>
<ArgTableRow arg="loop-detect" typ="bool" unset="1">Defines whether to run LSP loop detection. Will not work correctly if not enabled on all LSRs. Should be used only on non-TTL networks such as ATMs.</ArgTableRow>
<ArgTableRow arg="use-explicit-null" typ="bool" unset="1">Whether to distribute explicit-null label bindings.</ArgTableRow>
<ArgTableRow arg="distribute-for-default" typ="bool" unset="1">Defines whether to map label for the default route.</ArgTableRow>
<ArgTableRow arg="transport-addresses" typ="multi { array-id, transport-address: address (flags=46)
 }" unset="1">Specifies LDP session connection origin addresses and also advertises these addresses as transport addresses to LDP neighbors.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">Name of the VRF table this instance will operate on.</ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6)" unset="1">Determines supported address families by the instance.</ArgTableRow>
<ArgTableRow arg="preferred-afi" typ="enum (ip | ipv6)" unset="1">Determines which address family connection is preferred. Value is also set in dual-stack element (if used).</ArgTableRow>
</ArgTable>
