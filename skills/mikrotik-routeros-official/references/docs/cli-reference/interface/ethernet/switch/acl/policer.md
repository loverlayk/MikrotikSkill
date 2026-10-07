# policer

> RouterOS directory reference for /interface/ethernet/switch/acl/policer.

-----------

## interface/ethernet/switch/acl/policer 
**Syscap:** musicswitch
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the Policer used in ACL.</ArgTableRow>
<ArgTableRow arg="yellow-rate" typ="num" mandatory="1">Maximum data rate limit for packets with yellow drop precedence.</ArgTableRow>
<ArgTableRow arg="yellow-burst" typ="num">Maximum data rate which can be transmitted while the burst is allowed for packets with yellow drop precedence.</ArgTableRow>
<ArgTableRow arg="red-rate" typ="num">Maximum data rate limit for packets with red drop precedence.</ArgTableRow>
<ArgTableRow arg="red-burst" typ="num">Maximum data rate which can be transmitted while the burst is allowed for packets with red drop precedence.</ArgTableRow>
<ArgTableRow arg="meter-unit" typ="enum (bit | packet) { bit:0, packet:1 }">Measuring units for ACL traffic rate.</ArgTableRow>
<ArgTableRow arg="meter-len" typ="enum (layer-1 | layer-2 | layer-3) { layer-1:0, layer-2:1, layer-3:2 }">
Packet classification which sets the packet byte length for metering.
- `layer-1` - includes entire layer-2 frame + FCS + inter-packet gap + preamble.
- `layer-2` - includes layer-2 frame + FCS.
- `layer-3` - includes only layer-3 + ethernet padding without layer-2 header and FCS.
</ArgTableRow>
<ArgTableRow arg="color-awareness" typ="bool">
`yes` - makes the policer take into account pre-colored drop precedence.
`no` - ignores drop precedence.
</ArgTableRow>
<ArgTableRow arg="bucket-coupling" typ="bool"></ArgTableRow>
<ArgTableRow arg="yellow-action" typ="enum (drop | forward | remark) { drop:0, forward:1, remark:2 }">Performed action for exceeded traffic with yellow drop precedence.</ArgTableRow>
<ArgTableRow arg="new-dei-for-yellow" typ="alt { spcial-dei: enum (remap) { remap:0xffffffff }
, dei: num [ .. 1]
 }">New DEI for yellow drop precedence packets.</ArgTableRow>
<ArgTableRow arg="new-pcp-for-yellow" typ="alt { special-pcp: enum (remap) { remap:0xffffffff }
, pcp: num [ .. 7]
 }">New PCP for yellow drop precedence packets.</ArgTableRow>
<ArgTableRow arg="new-dscp-for-yellow" typ="alt { special-dscp: enum (remap) { remap:0xffffffff }
, dscp: num [ .. 63]
 }">New DSCP for yellow drop precedence packets.</ArgTableRow>
<ArgTableRow arg="red-action" typ="enum (drop | forward | remark) { drop:0, forward:1, remark:2 }">Performed action for exceeded traffic with red drop precedence.</ArgTableRow>
<ArgTableRow arg="new-dei-for-red" typ="alt { spcial-dei: enum (remap) { remap:0xffffffff }
, dei: num [ .. 1]
 }">New DEI for red drop precedence packets.</ArgTableRow>
<ArgTableRow arg="new-pcp-for-red" typ="alt { special-pcp: enum (remap) { remap:0xffffffff }
, pcp: num [ .. 7]
 }">New PCP for red drop precedence packets.</ArgTableRow>
<ArgTableRow arg="new-dscp-for-red" typ="alt { special-dscp: enum (remap) { remap:0xffffffff }
, dscp: num [ .. 63]
 }">New DSCP for red drop precedence packets.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="green-counter" typ="num"></ArgTableRow>
<ArgTableRow arg="yellow-counter" typ="num"></ArgTableRow>
<ArgTableRow arg="red-counter" typ="num"></ArgTableRow>
</ArgTable>
