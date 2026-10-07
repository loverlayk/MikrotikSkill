# neighbor

> List of discovered and statically configured LDP neighbors.

-----------

## mpls/ldp/neighbor 
**Conditions:** !smips
**Type:** Directory

List of discovered and statically configured LDP neighbors.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="O" typ="operational">Indicates whether the peer is operational.</ArgTableRow>
<ArgTableRow arg="C" typ="active-connect">Indicates that active role has been selected and the router is trying to establish the session.</ArgTableRow>
<ArgTableRow arg="W" typ="passive-wait">Indicates whether the peer is in a passive role and currently is waiting for the session to be initialized.</ArgTableRow>
<ArgTableRow arg="T" typ="throttled">Indicates whether session is in throttled state. Session is throttled after initialization failure, max throttle time 120s.</ArgTableRow>
<ArgTableRow arg="t" typ="sending-targeted-hello">Whether targeted hellos are being sent to the neighbor.</ArgTableRow>
<ArgTableRow arg="v" typ="vpls">Whether neighbor is used by LDP signaled VPLS tunnel.</ArgTableRow>
<ArgTableRow arg="p" typ="passive">Indicates whether the peer is in a passive role.</ArgTableRow>
<ArgTableRow arg="d" typ="on-demand">Downstream On Demand label distribution.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="transport" typ="address (flags=46vi)" mandatory="1">Remote transport address.</ArgTableRow>
<ArgTableRow arg="send-targeted" typ="bool" unset="1">Specifies whether to try to send targeted hellos, used for targeted (not directly connected) LDP sessions.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="peer" typ="object { peer-id: composite { id: ipAddr
, namespace: num
 }
 }">LSR-ID and label space of the neighbor.</ArgTableRow>
<ArgTableRow arg="local-transport" typ="address (flags=46)">Selected local transport address.</ArgTableRow>
<ArgTableRow arg="addresses" typ="multi { array-id, address: address (flags=46)
 }">List of discovered addresses on the neighbor.</ArgTableRow>
<ArgTableRow arg="path-vector-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="on-demand" typ="bool">Downstream On Demand label distribution.</ArgTableRow>
<ArgTableRow arg="used-afi" typ="ubit (ip, ipv6)">Used transport AFI.</ArgTableRow>
</ArgTable>
