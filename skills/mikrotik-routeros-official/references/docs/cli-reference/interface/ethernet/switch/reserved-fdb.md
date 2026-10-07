# reserved-fdb

> Cloud Router Switch supports 256 RFDB entries. Each RFDB entry can store either a Layer2 unicast or multicast MAC address with specific commands.

-----------

## interface/ethernet/switch/reserved-fdb 
**Syscap:** musicswitch
**Type:** Directory

Cloud Router Switch supports 256 RFDB entries. Each RFDB entry can store either a Layer2 unicast or multicast MAC address with specific commands.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr" mandatory="1">Matching MAC address for Reserved FDB entry.</ArgTableRow>
<ArgTableRow arg="action" typ="enum (forward | redirect-to-cpu | copy-to-cpu | drop) { forward:0, redirect-to-cpu:1, copy-to-cpu:2, drop:3 }">
Action for RFDB entry.
- `copy-to-cpu` - packets are copied to the CPU when their destination MAC matches the entry.
- `drop` - packets are dropped when their destination MAC matches the entry.
- `forward` - packets are forwarded when their destination MAC matches the entry.
- `redirect-to-cpu` - packets are redirected to the CPU when their destination MAC matches the entry.
</ArgTableRow>
<ArgTableRow arg="bypass-ingress-vlan-filter" typ="bool">Allows bypassing VLAN filtering for matching packets.</ArgTableRow>
<ArgTableRow arg="bypass-ingress-port-policing" typ="bool">Allows bypassing Ingress Port Policer for matching packets.</ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none) { none:0xffffffff }">Defined QoS group from QoS group menu.</ArgTableRow>
</ArgTable>
