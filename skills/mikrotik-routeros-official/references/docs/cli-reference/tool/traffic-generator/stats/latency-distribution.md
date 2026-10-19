# latency-distribution

> RouterOS directory reference for /tool/traffic-generator/stats/latency-distribution.

-----------

## tool/traffic-generator/stats/latency-distribution 
**Type:** Directory
Shows how many received packets fall into each latency range, per stream or per measurement sequence. See the [Traffic Generator](../../../../diagnostics-monitoring-and-troubleshooting/traffic-generator) guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="stream-id" typ="num">Filter the output to one stream ID.</ArgTableRow>
<ArgTableRow arg="port" typ="enum">Filter the output to one port.</ArgTableRow>
<ArgTableRow arg="seq" typ="range">Filter the output to one measurement sequence number.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="latency" typ="string">Latency range of this bucket, for example 0-15.5us.</ArgTableRow>
<ArgTableRow arg="count" typ="num">Number of packets received in this latency range.</ArgTableRow>
<ArgTableRow arg="share" typ="num">Share of received packets falling into this latency range, in percent.</ArgTableRow>
<ArgTableRow arg="graph" typ="meter">Graphical representation of the share.</ArgTableRow>
</ArgTable>
