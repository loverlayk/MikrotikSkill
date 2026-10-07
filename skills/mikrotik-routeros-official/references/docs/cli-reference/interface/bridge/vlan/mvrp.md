# mvrp

> RouterOS directory reference for /interface/bridge/vlan/mvrp.

-----------

## interface/bridge/vlan/mvrp 
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="bridge" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="port" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="registrar-state" typ="enum (IN | LV | MT) { IN:1, LV:2, MT:3 }"></ArgTableRow>
<ArgTableRow arg="applicant-state" typ="enum (Very anxious Observer | Very anxious Passive | Very anxious New | Anxious New | Anxious Active | Quiet Active | Leaving Active | Anxious Observer | Quiet Observer | Anxious Passive | Quiet Passive | Leaving Observer) { Very anxious Observer:1, Very anxious Passive:2, Very anxious New:3, Anxious New:4, Anxious Active:5, Quiet Active:6, Leaving Active:7, Anxious Observer:8, Quiet Observer:9, Anxious Passive:10, Quiet Passive:11, Leaving Observer:12 }"></ArgTableRow>
<ArgTableRow arg="last-event" typ="enum (New | JoinIn | In | JoinEmpty | Empty | Leave) { New:0, JoinIn:1, In:2, JoinEmpty:3, Empty:4, Leave:5 }"></ArgTableRow>
</ArgTable>
