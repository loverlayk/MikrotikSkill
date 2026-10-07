# qos-group

> The global QoS group table is used for VLAN-based, Protocol-based, and MAC-based QoS group assignment configuration.

-----------

## interface/ethernet/switch/qos-group 
**Syscap:** musicswitch
**Type:** Directory

The global QoS group table is used for VLAN-based, Protocol-based, and MAC-based QoS group assignment configuration.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the QoS group.</ArgTableRow>
<ArgTableRow arg="pcp" typ="num">The new value of PCP for the QoS group.</ArgTableRow>
<ArgTableRow arg="dei" typ="num">The new value of DEI for the QoS group.</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">The new value of DSCP for the QoS group.</ArgTableRow>
<ArgTableRow arg="priority" typ="num">Internal priority is of local significance for classifying traffic to different egress queues on a port (1 is highest, 15 is lowest).</ArgTableRow>
<ArgTableRow arg="drop-precedence" typ="enum (green | yellow | red | drop)">Drop precedence is an internal QoS attribute used for packet enqueuing or dropping.</ArgTableRow>
</ArgTable>
