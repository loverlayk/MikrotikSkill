# traffic-flow

> RouterOS settings reference for /ip/traffic-flow.

-----------

## ip/traffic-flow 
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, interface-or-list: alt { interface: iface_enum { local:0, all:0xFFFFFFFF }
, interface-list: enum
 }
 }"></ArgTableRow>
<ArgTableRow arg="cache-entries" typ="enum (1k | 2k | 4k | 8k | 16k | 32k | 64k | 128k | 256k | 512k | 1M | 2M | 4M | 8M | 16M | 32M) { 1k:0x400, 2k:0x800, 4k:0x1000, 8k:0x2000, 16k:0x4000, 32k:0x8000, 64k:0x10000, 128k:0x20000, 256k:0x40000, 512k:0x80000, 1M:0x100000, 2M:0x200000, 4M:0x400000, 8M:0x800000, 16M:0x1000000, 32M:0x2000000 }"></ArgTableRow>
<ArgTableRow arg="active-flow-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="inactive-flow-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="packet-sampling" typ="bool"></ArgTableRow>
<ArgTableRow arg="sampling-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="sampling-space" typ="num"></ArgTableRow>
</ArgTable>
