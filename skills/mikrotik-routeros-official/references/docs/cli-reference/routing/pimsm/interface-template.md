# interface-template

> The interface template menu defines which interfaces will participate in PIM and what per-interface configuration will be used.

-----------

## routing/pimsm/interface-template 
**Conditions:** !smips
**Type:** Directory

The interface template menu defines which interfaces will participate in PIM and what per-interface configuration will be used.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum" mandatory="1">Name of the PIM instance this interface template belongs to.</ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { interface: iface_enum
 }" unset="1">List of interfaces that will participate in PIM.</ArgTableRow>
<ArgTableRow arg="hello-period" typ="time">Periodic interval for Hello messages.</ArgTableRow>
<ArgTableRow arg="hello-delay" typ="time">Randomized interval for the initial Hello message on interface startup or detecting a new neighbor.</ArgTableRow>
<ArgTableRow arg="priority" typ="num">The Designated Router (DR) priority. A single Designated Router is elected on each network. The priority is used only if all neighbors have advertised a priority option. The numerically largest priority is preferred. In case of a tie or if priority is not used - the numerically largest IP address is preferred.</ArgTableRow>
<ArgTableRow arg="join-prune-period" typ="time"></ArgTableRow>
<ArgTableRow arg="propagation-delay" typ="time">Sets the value for a prune pending timer. It is used by upstream routers to figure out how long they should wait for a Join override message before pruning an interface that has join suppression enabled.</ArgTableRow>
<ArgTableRow arg="override-interval" typ="time">Sets the maximum time period over which to randomize when scheduling a delayed override Join message on a network that has join suppression enabled.</ArgTableRow>
<ArgTableRow arg="join-tracking-support" typ="bool">Sets the value of a Tracking (T) bit in the LAN Prune Delay option in the Hello message. When enabled, a router advertises its willingness to disable Join suppression. It is possible for upstream routers to explicitly track the join membership of individual downstream routers if Join suppression is disabled. Unless all PIM routers on a link negotiate this capability, explicit tracking and the disabling of the Join suppression mechanism are not possible.</ArgTableRow>
<ArgTableRow arg="source-addresses" typ="object { address: address (flags=46)
 }" unset="1"></ArgTableRow>
</ArgTable>
