# shaper

> Traffic shaping restricts the rate and burst size of the flow which is transmitted out from the interface. The shaper is implemented by a token bucket. If the packet exceeds the maximum rate or the burst size, which...

-----------

## interface/ethernet/switch/shaper 
**Syscap:** musicswitch
**Type:** Directory

Traffic shaping restricts the rate and burst size of the flow which is transmitted out from the interface. The shaper is implemented by a token bucket. If the packet exceeds the maximum rate or the burst size, which means not enough tokens for the packet, the packet is stored in the buffer until there are enough tokens to transmit it.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="port" typ="enum" mandatory="1">Physical port for traffic shaper.</ArgTableRow>
<ArgTableRow arg="target" typ="enum (queue0 | queue1 | queue2 | queue3 | queue4 | queue5 | queue6 | queue7 | wrr-group0 | wrr-group1 | port) { queue0:0, queue1:1, queue2:2, queue3:3, queue4:4, queue5:5, queue6:6, queue7:7, wrr-group0:8, wrr-group1:9, port:10 }">
Three levels of shapers are supported on each port (including CPU port).
- `port` - entry applies to the port of the switch-chip.
- `wrr-group0` or `wrr-group1` - entry applies to one of the 2 Weighted Round Robin queue groups on the port.
- `queue0`-`queue7` - entry applies to one of the 8 queues on the port.
</ArgTableRow>
<ArgTableRow arg="meter-unit" typ="enum (bit | packet) { bit:0, packet:1 }">Measuring units for traffic shaper rate.</ArgTableRow>
<ArgTableRow arg="rate" typ="num">Maximum data rate limit.</ArgTableRow>
<ArgTableRow arg="burst" typ="num">Maximum data rate which can be transmitted while the burst is allowed.</ArgTableRow>
</ArgTable>
