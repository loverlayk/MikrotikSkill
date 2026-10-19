# stream

> RouterOS directory reference for /tool/traffic-generator/stream.

-----------

## tool/traffic-generator/stream 
**Type:** Directory
Defines the generated traffic flows: rate, packet size, packet template and CPU core binding. See the [Traffic Generator](../../../diagnostics-monitoring-and-troubleshooting/traffic-generator) guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Descriptive name of the stream.</ArgTableRow>
<ArgTableRow arg="port" typ="enum">Name of the port (from the port menu) the stream transmits through. Usually taken from the packet template; can be overridden here.</ArgTableRow>
<ArgTableRow arg="id" typ="num">Stream ID used to identify the stream in stats and in the start/quick commands. The value TOT is reserved for totals.</ArgTableRow>
<ArgTableRow arg="packet-size" typ="range">L2 size of the generated packets in bytes; a range (for example 64-1518) generates random packet sizes.</ArgTableRow>
<ArgTableRow arg="pps" typ="num">Packets per second the stream tries to generate.</ArgTableRow>
<ArgTableRow arg="mbps" typ="num">Megabits per second the stream tries to generate.</ArgTableRow>
<ArgTableRow arg="packet-count" typ="num">Number of packets to transmit; `unlimited` transmits until the stream is stopped.</ArgTableRow>
<ArgTableRow arg="cpu-core" typ="range">CPU core (0-255) the stream is pinned to, or a range of cores for multi-core streams.</ArgTableRow>
<ArgTableRow arg="tx-template" typ="enum" mandatory="1">Name of the packet template (from packet-template or raw-packet-template) used as the packet content source. Mandatory.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-port" typ="enum">The port this stream transmits on, taken from the packet template.</ArgTableRow>
</ArgTable>
