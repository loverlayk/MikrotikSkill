# monitor-traffic

> RouterOS command reference for /interface/monitor-traffic.

-----------

## interface/monitor-traffic 
**Type:** Command
Real-time per-interface throughput (rates per second). Multiple interfaces print side-by-side columns; the table refreshes continuously. Use `duration` to bound it.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="multi { array-id, interface: iface_enum { aggregate:0 }
 }">Interfaces to watch (or `aggregate` for the combined view)</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Interface name</ArgTableRow>
<ArgTableRow arg="rx-packets-per-second" typ="num">Received packets per second</ArgTableRow>
<ArgTableRow arg="rx-bits-per-second" typ="num">Received bits per second</ArgTableRow>
<ArgTableRow arg="fp-rx-packets-per-second" typ="num">Fast Path received packets per second</ArgTableRow>
<ArgTableRow arg="fp-rx-bits-per-second" typ="num">Fast Path received bits per second</ArgTableRow>
<ArgTableRow arg="rx-drops-per-second" typ="num">Receive drops per second</ArgTableRow>
<ArgTableRow arg="rx-errors-per-second" typ="num">Receive errors per second</ArgTableRow>
<ArgTableRow arg="tx-packets-per-second" typ="num">Transmitted packets per second</ArgTableRow>
<ArgTableRow arg="tx-bits-per-second" typ="num">Transmitted bits per second</ArgTableRow>
<ArgTableRow arg="fp-tx-packets-per-second" typ="num">Fast Path transmitted packets per second</ArgTableRow>
<ArgTableRow arg="fp-tx-bits-per-second" typ="num">Fast Path transmitted bits per second</ArgTableRow>
<ArgTableRow arg="tx-drops-per-second" typ="num">Transmit drops per second</ArgTableRow>
<ArgTableRow arg="tx-queue-drops-per-second" typ="num">Interface queue drops per second</ArgTableRow>
<ArgTableRow arg="tx-errors-per-second" typ="num">Transmit errors per second</ArgTableRow>
</ArgTable>
