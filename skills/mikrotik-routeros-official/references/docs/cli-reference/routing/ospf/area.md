# area

> RouterOS directory reference for /routing/ospf/area.

-----------

## routing/ospf/area 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="T" typ="transit-capable">transit-capable</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">The name of the area</ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1">Name of the OSPF instance this area belongs to.</ArgTableRow>
<ArgTableRow arg="area-id" typ="ipAddr">OSPF area identifier. If the router has networks in more than one area, then an area with `area-id=0.0.0.0` (the backbone) must always be present. The backbone always contains all area border routers. The backbone is responsible for distributing routing information between non-backbone areas. The backbone must be contiguous, i.e. there must be no disconnected segments. However, area border routers do not need to be physically connected to the backbone - connection to it may be simulated using a virtual link.</ArgTableRow>
<ArgTableRow arg="type" typ="enum (default | stub | nssa)">The area type. Read more on the area types in the [OSPF user guides](../../../../user-guides/routing-and-networking-protocols/unicast/ospf/areas-and-virtual-links.md).</ArgTableRow>
<ArgTableRow arg="no-summaries" typ="switch">Flag parameter, if set then the area will not flood summary LSAs in the stub area.</ArgTableRow>
<ArgTableRow arg="default-cost" typ="num" unset="1">Default cost of injected LSAs into the area. If the value is not set, then stub area type-3 default LSA will not be originated.</ArgTableRow>
<ArgTableRow arg="nssa-translator" typ="enum (candidate | no | yes)" unset="1">
The parameter indicates which ABR will be used as a translator from `type-7` to `type-5` LSA. Applicable only if area type is NSSA.
- yes - the router will be always used as a translator.
- no - the router will never be used as a translator.
- candidate - OSPF elects one of the candidate routers to be a translator.
</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="transit-capable" typ="bool"></ArgTableRow>
</ArgTable>
