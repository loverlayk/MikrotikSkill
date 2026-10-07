# ingress-port-policer

> RouterOS directory reference for /interface/ethernet/switch/ingress-port-policer.

-----------

## interface/ethernet/switch/ingress-port-policer 
**Syscap:** musicswitch
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="port" typ="enum" mandatory="1">Physical port or trunk for the ingress port policer entry.</ArgTableRow>
<ArgTableRow arg="rate" typ="num" mandatory="1">Maximum data rate limit.</ArgTableRow>
<ArgTableRow arg="burst" typ="num">Maximum data rate which can be transmitted while the burst is allowed.</ArgTableRow>
<ArgTableRow arg="meter-unit" typ="enum (bit | packet) { bit:0, packet:1 }">Measuring units for traffic ingress port policer rate.</ArgTableRow>
<ArgTableRow arg="meter-len" typ="enum (layer-1 | layer-2 | layer-3) { layer-1:0, layer-2:1, layer-3:2 }">
Packet classification which sets the packet byte length for metering.
- `layer-1` - includes the entire layer-2 frame + FCS + inter-packet gap + preamble.
- `layer-2` - includes the layer-2 frame + FCS.
- `layer-3` - includes only the layer-3 + ethernet padding without the layer-2 header and FCS.
</ArgTableRow>
<ArgTableRow arg="yellow-action" typ="enum (drop | forward | remark) { drop:0, forward:1, remark:2 }">Performed action for exceeded traffic.</ArgTableRow>
<ArgTableRow arg="new-dei-for-yellow" typ="alt { spcial-dei: enum (remap) { remap:0xffffffff }
, dei: num [ .. 1]
 }">Remarked DEI for exceeded traffic if yellow-action is remark.</ArgTableRow>
<ArgTableRow arg="new-pcp-for-yellow" typ="alt { special-pcp: enum (remap) { remap:0xffffffff }
, pcp: num [ .. 7]
 }">Remarked PCP for exceeded traffic if yellow-action is remark.</ArgTableRow>
<ArgTableRow arg="new-dscp-for-yellow" typ="alt { special-dscp: enum (remap) { remap:0xffffffff }
, dscp: num [ .. 63]
 }">Remarked DSCP for exceeded traffic if yellow-action is remark.</ArgTableRow>
<ArgTableRow arg="packet-types" typ="ubit (arp-or-nd, tcp-control, broadcast, unregistered-multicast, registered-multicast, unknown-unicast, known-unicast)">Matching packet types for which the ingress port policer entry is valid.</ArgTableRow>
</ArgTable>
