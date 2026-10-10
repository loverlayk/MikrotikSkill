# monitor

> RouterOS command reference for /ip/traffic-flow/monitor.

-----------

## ip/traffic-flow/monitor 
**Type:** Command
Show the current flow-cache counters (live-updating output; stops after `duration`).

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="finished-flows" typ="num">Number of flows that expired and were exported</ArgTableRow>
<ArgTableRow arg="active-flows" typ="num">Number of flows in the cache right now</ArgTableRow>
<ArgTableRow arg="unmanaged-packets" typ="num">Packets that did not fit into any tracked flow</ArgTableRow>
<ArgTableRow arg="unmanaged-bytes" typ="num">Bytes of the unmanaged packets</ArgTableRow>
</ArgTable>
