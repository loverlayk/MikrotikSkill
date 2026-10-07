# packet

> RouterOS directory reference for /interface/wireless/sniffer/packet.

-----------

## interface/wireless/sniffer/packet 
**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="E" typ="crc-error"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="time" typ="num"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="channel" typ="string"></ArgTableRow>
<ArgTableRow arg="signal-at-rate" typ="composite { strength: num
, rate: string
 }"></ArgTableRow>
<ArgTableRow arg="dst" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="src" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (assoc-req | assoc-resp | reassoc-req | reassoc-resp | probe-req | probe-resp | beacon | atim | disassoc | auth | deauth | ps-poll | rts | cts | ack | cf-end | cf-endack | data | d-cfack | d-cfpoll | d-cfackpoll | data-null | nd-cfack | nd-cfpoll | nd-cfackpoll) { assoc-req:0x00, assoc-resp:0x01, reassoc-req:0x02, reassoc-resp:0x03, probe-req:0x04, probe-resp:0x05, beacon:0x08, atim:0x09, disassoc:0x0a, auth:0x0b, deauth:0x0c, ps-poll:0x1a, rts:0x1b, cts:0x1c, ack:0x1d, cf-end:0x1e, cf-endack:0x1f, data:0x20, d-cfack:0x21, d-cfpoll:0x22, d-cfackpoll:0x23, data-null:0x24, nd-cfack:0x25, nd-cfpoll:0x26, nd-cfackpoll:0x27 }"></ArgTableRow>
</ArgTable>
