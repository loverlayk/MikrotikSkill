# neighbor

> The neighbor menu shows all detected neighbors that are running PIM and their statuses. This menu contains dynamic and read-only entries.

-----------

## routing/pimsm/neighbor 
**Conditions:** !smips
**Type:** Directory

The neighbor menu shows all detected neighbors that are running PIM and their statuses. This menu contains dynamic and read-only entries.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="designated-router">The neighbor is the elected Designated Router (DR) on the network segment.</ArgTableRow>
<ArgTableRow arg="J" typ="join-tracking">The neighbor supports join tracking. It sets the Tracking (T) bit in the LAN Prune Delay option of its Hello messages.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum">Name of the PIM instance this neighbor is detected on.</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)">Shows the neighbor's IP address and local interface the neighbor is detected on.</ArgTableRow>
<ArgTableRow arg="priority" typ="num">Indicates the neighbor's priority value.</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">Shows the remaining time after the neighbor is removed from the list if no new Hello message is received. The hold time equals neighbor's `hello-period * 3.5`.</ArgTableRow>
<ArgTableRow arg="propagation-delay" typ="time">Indicates the neighbor's value of the propagation delay in the LAN Prune Delay option in the Hello message.</ArgTableRow>
<ArgTableRow arg="override-interval" typ="time">Indicates the neighbor's value of the override interval in the LAN Prune Delay option in the Hello message.</ArgTableRow>
</ArgTable>
