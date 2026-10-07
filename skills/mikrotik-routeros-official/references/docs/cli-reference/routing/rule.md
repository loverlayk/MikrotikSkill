# rule

> RouterOS directory reference for /routing/rule.

-----------

## routing/rule 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="src-address" typ="address (flags=64iv/)" unset="1">Source address to match.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="address (flags=64iv/)" unset="1">Destination address to match.</ArgTableRow>
<ArgTableRow arg="routing-mark" typ="enum" unset="1">Match a specific routing mark.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" unset="1">Incoming interface to match.</ArgTableRow>
<ArgTableRow arg="action" typ="enum (lookup | lookup-only-in-table | unreachable | drop | mangle)">
Action to take on the matching packet:
- drop - silently drop the packet.
- lookup - perform a lookup in routing tables.
- lookup-only-in-table - perform lookup only in the specified routing table (see the `table` parameter).
- unreachable - generate an ICMP unreachable message and send it to the source.
- mangle - perform actions by firewall mangle rules.
</ArgTableRow>
<ArgTableRow arg="table" typ="enum (local) { local:4095 }">Name of the routing table to use for lookup.</ArgTableRow>
<ArgTableRow arg="min-prefix" typ="num" unset="1">Hide routes from the routing table with the specified prefix length from packets processed by this routing rule. This is equivalent to the Linux IP rule `suppress_prefixlength`. For example, set the value to 0 to suppress the default route in the routing decision.</ArgTableRow>
<ArgTableRow arg="vrf" typ="switch"></ArgTableRow>
<ArgTableRow arg="realm" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="chain" typ="enum" unset="1">Name of the chain used by routing decision rules. By default, `user` is used when the chain is not specified. If the chain name matches a built-in routing decision name, user-created rules are added after that decision. For example, if `chain=mangle`, user-created rules in this chain are located immediately after the `mangle` decision.</ArgTableRow>
</ArgTable>
