# monitor

> Command is used to monitor the bonding interface and bonding ports.

-----------

## interface/bonding/monitor 
**Type:** Command

Command is used to monitor the bonding interface and bonding ports.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mode" typ="enum (balance-rr | active-backup | balance-xor | broadcast | 802.3ad | balance-tlb | balance-alb) { balance-rr:0, active-backup:1, balance-xor:2, broadcast:3, 802.3ad:4, balance-tlb:5, balance-alb:6 }">Used bonding mode.</ArgTableRow>
<ArgTableRow arg="active-ports" typ="multi { array-id, port: iface_enum
 }">Shows the active bonding ports.</ArgTableRow>
<ArgTableRow arg="inactive-ports" typ="multi { array-id, port: iface_enum
 }">Shows the inactive bonding ports (e.g. a disabled or backup interface).</ArgTableRow>
<ArgTableRow arg="lacp-system-id" typ="macAddr">Shows the local LACP system ID.</ArgTableRow>
<ArgTableRow arg="lacp-system-priority" typ="num">Shows the local LACP priority.</ArgTableRow>
<ArgTableRow arg="lacp-partner-system-id" typ="macAddr">Shows the partner LACP system ID.</ArgTableRow>
</ArgTable>
