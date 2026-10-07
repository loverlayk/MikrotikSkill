# profile

> QoS profiles determine priority field values (PCP, DSCP) for the forwarded/routed packets. Congestion avoidance/resolution is based on QoS profiles. Each packet gets a QoS profile assigned based on the ingress switch...

-----------

## interface/ethernet/switch/qos/profile 
**Syscap:** rbswitch and crs_prestera
**Type:** Directory

QoS profiles determine priority field values (PCP, DSCP) for the forwarded/routed packets. Congestion avoidance/resolution is based on QoS profiles. Each packet gets a QoS profile assigned based on the ingress switch port QoS settings (see `/in/eth/sw/port`).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">The user-defined name of the QoS profile.</ArgTableRow>
<ArgTableRow arg="pcp" typ="num">VLAN priority value (IEEE 802.1q PCP - Priority Code Point). Used only if the egress packets assigned to the QoS profile are VLAN-tagged (have the 802.1q header). The value can be further altered via the QoS Egress Map.</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">IPv4/IPv6 DSCP field value for the egress packets assigned to the QoS profile.</ArgTableRow>
<ArgTableRow arg="traffic-class" typ="num">The traffic class determines the packet priority and the egress queue. The queue number is usually the same as the traffic class (packets with tc0 go into queue0, tc1 - queue1, ... tc7 - queue7). TC0 always selects the lowest priority.</ArgTableRow>
<ArgTableRow arg="automap" typ="bool">Automatically maps packets with matching PCP or DSCP values to this QoS profile. Only applies to **trusted** ports.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>
