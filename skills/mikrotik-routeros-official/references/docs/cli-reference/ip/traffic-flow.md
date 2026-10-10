# traffic-flow

> RouterOS settings reference for /ip/traffic-flow.

-----------

## ip/traffic-flow 
**Type:** Settings Directory
Traffic-Flow (NetFlow/IPFIX-compatible) configuration. Turn it on with `enabled=yes` and add export destinations under [`target`](target). Flows pass only through the CPU path of the router, so HW-offloaded traffic cannot be exported. See the [Traffic Flow](../../../diagnostics-monitoring-and-troubleshooting/traffic-flow) guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool">Enable or disable the Traffic-Flow service</ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, interface-or-list: alt { interface: iface_enum { local:0, all:0xFFFFFFFF }
, interface-list: enum
 }
 }">Comma-separated interface names (or `all`) whose forwarded traffic is accounted</ArgTableRow>
<ArgTableRow arg="cache-entries" typ="enum (1k | 2k | 4k | 8k | 16k | 32k | 64k | 128k | 256k | 512k | 1M | 2M | 4M | 8M | 16M | 32M) { 1k:0x400, 2k:0x800, 4k:0x1000, 8k:0x2000, 16k:0x4000, 32k:0x8000, 64k:0x10000, 128k:0x20000, 256k:0x40000, 512k:0x80000, 1M:0x100000, 2M:0x200000, 4M:0x400000, 8M:0x800000, 16M:0x1000000, 32M:0x2000000 }">Number of flow records held in memory at once (the default value depends on the device memory: 256k on larger boards, down to 4k on the smallest)</ArgTableRow>
<ArgTableRow arg="active-flow-timeout" typ="time">Maximum lifetime of a flow, even when packets keep matching it; the flow is expired and exported after this time. Default: 30m</ArgTableRow>
<ArgTableRow arg="inactive-flow-timeout" typ="time">A flow that sees no packet for this long is expired and exported; the next packet starts a new flow. If the timeout is too small, it can create many flows and overflow the buffer. Default: 15s</ArgTableRow>
<ArgTableRow arg="packet-sampling" typ="bool">Enable packet sampling: packets are accounted only per `sampling-interval` and `sampling-space`</ArgTableRow>
<ArgTableRow arg="sampling-interval" typ="num">Number of consecutive packets that are sampled in each sampling cycle</ArgTableRow>
<ArgTableRow arg="sampling-space" typ="num">Number of consecutive packets that are omitted in each sampling cycle</ArgTableRow>
</ArgTable>
