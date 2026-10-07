# unicast-fdb

> The unicast forwarding database supports up to 16K MAC entries.

-----------

## interface/ethernet/switch/unicast-fdb 
**Syscap:** musicswitch
**Type:** Directory

The unicast forwarding database supports up to 16K MAC entries.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="A" typ="active"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr" mandatory="1">The action command applies to the packet when the destination MAC or source MAC matches the entry.</ArgTableRow>
<ArgTableRow arg="port" typ="alt { port: enum
, trunk: enum
 }" mandatory="1">Matching port for the Unicast FDB entry.</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num">Unicast FDB lookup/learning VLAN id.</ArgTableRow>
<ArgTableRow arg="action" typ="enum (forward | src-drop | dst-drop | src-and-dst-drop | ingress-port-policing-bypass | src-redirect-to-cpu | dst-redirect-to-cpu | src-and-dst-redirect-to-cpu) { forward:0, src-drop:1, dst-drop:2, src-and-dst-drop:3, ingress-port-policing-bypass:4, src-redirect-to-cpu:5, dst-redirect-to-cpu:6, src-and-dst-redirect-to-cpu:7 }">
Action for UFDB entry.
- `dst-drop` - packets are dropped when their destination MAC matches the entry.
- `dst-redirect-to-cpu` - packets are redirected to the CPU when their destination MAC matches the entry.
- `forward` - packets are forwarded.
- `src-and-dst-drop` - packets are dropped when their source MAC or destination MAC matches the entry.
- `src-and-dst-redirect-to-cpu` - packets are redirected to CPU when their source MAC or destination MAC matches the entry.
- `src-drop` - packets are dropped when their source MAC matches the entry.
- `src-redirect-to-cpu` - packets are redirected to the CPU when their source MAC matches the entry.
</ArgTableRow>
<ArgTableRow arg="mirror" typ="bool">Enables or disables mirroring based on source MAC or destination MAC.</ArgTableRow>
<ArgTableRow arg="isolation-profile" typ="enum (promiscuous | isolated | community1 | community2) { promiscuous:0, isolated:1, community1:2, community2:3 }">MAC level isolation profile.</ArgTableRow>
<ArgTableRow arg="svl" typ="bool">
Unicast FDB learning mode.
- `svl` - Shared VLAN Learning, learning/lookup is based on MAC addresses - not on VLAN IDs.
- `ivl` - Independent VLAN Learning, learning/lookup is based on both MAC addresses and VLAN IDs.
</ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none) { none:0xffffffff }">Defined QoS group from the QoS group menu.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="age" typ="num"></ArgTableRow>
</ArgTable>
