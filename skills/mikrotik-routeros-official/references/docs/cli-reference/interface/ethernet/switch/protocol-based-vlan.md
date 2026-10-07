# protocol-based-vlan

> The Protocol Based VLAN table is used to assign VID and QoS attributes to related protocol packets per port.

-----------

## interface/ethernet/switch/protocol-based-vlan 
**Syscap:** musicswitch
**Type:** Directory

The Protocol Based VLAN table is used to assign VID and QoS attributes to related protocol packets per port.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="frame-type" typ="enum (ethernet | rfc-1042 | llc) { ethernet:0, rfc-1042:1, llc:2 }">Encapsulation type of the matching frames.</ArgTableRow>
<ArgTableRow arg="protocol" typ="alt { protocol: enum ()
, protocol-number: num [ .. 65535]
 }">Matching protocol for Protocol-based VLAN rule.</ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id }" mandatory="1">Matching switch ports for Protocol-based VLAN rule.</ArgTableRow>
<ArgTableRow arg="set-service-vid-for" typ="enum (none | untagged-or-priority-tagged | tagged | all) { none:0, untagged-or-priority-tagged:1, tagged:2, all:3 }">Service VLAN ID assignment command for different packet types.</ArgTableRow>
<ArgTableRow arg="new-service-vid" typ="num">The new service VLAN ID replaces the original service VLAN ID for the specified protocol.</ArgTableRow>
<ArgTableRow arg="set-customer-vid-for" typ="enum (none | untagged-or-priority-tagged | tagged | all) { none:0, untagged-or-priority-tagged:1, tagged:2, all:3 }">Customer VLAN ID assignment command for different packet types.</ArgTableRow>
<ArgTableRow arg="new-customer-vid" typ="num">The new customer VLAN ID replaces the original customer VLAN ID for the specified protocol. If set to 4095, then traffic is dropped.</ArgTableRow>
<ArgTableRow arg="set-qos-for" typ="enum (none | untagged-or-priority-tagged | tagged | all) { none:0, untagged-or-priority-tagged:1, tagged:2, all:3 }">Frame type for which QoS assignment command applies.</ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none) { none:0xffffffff }">Defined QoS group from the QoS group menu.</ArgTableRow>
</ArgTable>
