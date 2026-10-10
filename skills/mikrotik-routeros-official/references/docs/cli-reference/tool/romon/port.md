# port

> Ports that participate in the RoMON network.

-----------

## tool/romon/port 
**Type:** Directory

Ports that participate in the [RoMON network](../../../management-tools/romon#choose-ports).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum { all }" mandatory="1">Interface that participates in RoMON; either a single interface or the built-in wildcard `all`. Master interfaces such as bridges are not accepted — name the physical ports. The preconfigured `all` entry cannot be added a second time, removed, enabled or disabled; only its `cost`, `forbid` and `secrets` can be changed.</ArgTableRow>
<ArgTableRow arg="forbid" typ="bool">Whether the matched interface is allowed or forbidden to participate in the RoMON network.</ArgTableRow>
<ArgTableRow arg="cost" typ="num">The port's cost. All specific port entries have higher priority than the wildcard entry with `interface=all`.</ArgTableRow>
<ArgTableRow arg="secrets" typ="multi { array-id, name: string
 }">List of individual port secrets used for RoMON message hashing.</ArgTableRow>
</ArgTable>
