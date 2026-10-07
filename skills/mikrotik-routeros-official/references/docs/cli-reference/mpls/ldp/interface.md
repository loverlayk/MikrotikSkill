# interface

> RouterOS directory reference for /mpls/ldp/interface.

-----------

## mpls/ldp/interface 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="enum ()" mandatory="1">Name of the interface or interface list where LDP will be listening.</ArgTableRow>
<ArgTableRow arg="hello-interval" typ="time" unset="1">The interval between hello packets that the router sends out on the specified interface/s. The default value is 5s.</ArgTableRow>
<ArgTableRow arg="hold-time" typ="time" unset="1">Specifies the interval after which a neighbor discovered on the interface is declared as not reachable. The default value is 15s.</ArgTableRow>
<ArgTableRow arg="transport-addresses" typ="multi { array-id, transport-address: address (flags=46)
 }" unset="1">Used transport addresses if they differ from LDP Instance settings.</ArgTableRow>
<ArgTableRow arg="accept-dynamic-neighbors" typ="bool" unset="1">Defines whether to discover neighbors dynamically or use only statically configured in LDP neighbors menu.</ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6)" unset="1">Determines interface address family. Only AFIs that are configured as supported by the instance are taken into account. If the value is not explicitly specified then it is considered to be equal to the instance-supported AFIs.</ArgTableRow>
</ArgTable>
