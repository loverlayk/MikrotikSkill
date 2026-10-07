# monitor-slaves

> Command is used to monitor individual bonding ports.

-----------

## interface/bonding/monitor-slaves 
**Type:** Command

Command is used to monitor individual bonding ports.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="A" typ="active">active</ArgTableRow>
<ArgTableRow arg="P" typ="partner">partner</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="bond" typ="iface_enum">Bonding interface to monitor.</ArgTableRow>
<ArgTableRow arg="once" typ="bool">Show the monitor output once instead of continuously.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="port" typ="iface_enum">Used bonding port.</ArgTableRow>
<ArgTableRow arg="key" typ="num">Shows the local LACP aggregation key. The lower 6 bits are automatically assigned based on individual port link speed and duplex. The upper 10 bits can be manually specified using the lacp-user-key setting.</ArgTableRow>
<ArgTableRow arg="flags" typ="string">
Shows the local LACP flags.
- A - activity (link is active).
- T - timeout (link is using short timeout).
- G - aggregation (link can be aggregatable).
- S - synchronization (link is synchronized).
- C - collecting (link is able to collect incoming frames).
- D - distributing (link is able to distribute outgoing frames).
- F - defaulted (link is using defaulted partner information).
- E - expired (link has expired state).
</ArgTableRow>
<ArgTableRow arg="partner-sys-id" typ="macAddr">Shows the partner LACP system ID.</ArgTableRow>
<ArgTableRow arg="partner-sys-priority" typ="num">Shows the partner LACP priority.</ArgTableRow>
<ArgTableRow arg="partner-key" typ="num">Shows the partner LACP aggregation key.</ArgTableRow>
<ArgTableRow arg="partner-flags" typ="string">Shows the partner LACP flags.</ArgTableRow>
</ArgTable>
