# stream

> RouterOS directory reference for /tool/traffic-generator/stats/stream.

-----------

## tool/traffic-generator/stats/stream 
**Type:** Directory
Statistics of a completed or running test, sorted by stream — the same output as in quick mode. See the [Traffic Generator](../../../../diagnostics-monitoring-and-troubleshooting/traffic-generator) guide.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="seq" typ="enum (TOT) { TOT:0xffffffff }">Measurement sequence number, or TOT for totals.</ArgTableRow>
<ArgTableRow arg="id" typ="enum (TOT) { TOT:0xffffffff }">Stream ID, or TOT for totals across streams.</ArgTableRow>
<ArgTableRow arg="tx-packet" typ="num">Total packets transmitted.</ArgTableRow>
<ArgTableRow arg="tx-byte" typ="num">Total bytes transmitted.</ArgTableRow>
<ArgTableRow arg="tx-rate" typ="num">Current transmit rate in bps.</ArgTableRow>
<ArgTableRow arg="rx-packet" typ="num">Total packets received.</ArgTableRow>
<ArgTableRow arg="rx-byte" typ="num">Total bytes received.</ArgTableRow>
<ArgTableRow arg="rx-rate" typ="num">Current receive rate in bps.</ArgTableRow>
<ArgTableRow arg="rx-ooo" typ="num">Received packets that were out of order.</ArgTableRow>
<ArgTableRow arg="rx-bad-csum" typ="num">Received packets with a bad checksum.</ArgTableRow>
<ArgTableRow arg="lost-packet" typ="num">Total lost packets (transmitted minus received).</ArgTableRow>
<ArgTableRow arg="lost-byte" typ="num">Total lost bytes.</ArgTableRow>
<ArgTableRow arg="lost-rate" typ="num">Current loss rate in bps.</ArgTableRow>
<ArgTableRow arg="lost-ratio" typ="string">Loss as a percentage of transmitted packets.</ArgTableRow>
<ArgTableRow arg="lat-min" typ="string">Minimum measured latency.</ArgTableRow>
<ArgTableRow arg="lat-avg" typ="string">Average measured latency.</ArgTableRow>
<ArgTableRow arg="lat-max" typ="string">Maximum measured latency.</ArgTableRow>
<ArgTableRow arg="jitter" typ="string">Measured latency variation (jitter).</ArgTableRow>
</ArgTable>
