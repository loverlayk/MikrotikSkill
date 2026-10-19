# quick

> RouterOS command reference for /tool/traffic-generator/quick.

-----------

## tool/traffic-generator/quick 
**Type:** Command
Starts the traffic generator, prints the statistics to the terminal and assembles the latency/jitter report. Parameters override the values configured in the stream and the packet template; if a parameter specifies only one header, the value is multiplied for the other headers.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="entries-to-show" typ="num">How many status lines to print to the terminal.</ArgTableRow>
<ArgTableRow arg="test-id" typ="num">Test session ID (see the general traffic-generator menu).</ArgTableRow>
<ArgTableRow arg="measure-out-of-order" typ="bool">Whether out-of-order received packets are measured and reported for this test.</ArgTableRow>
<ArgTableRow arg="cpu-core" typ="multi { array-id, array-id, cpu-core: range [0 .. 255]
 }">CPU core or range of cores (0-255) the streams are pinned to, for multi-core tests.</ArgTableRow>
<ArgTableRow arg="stream" typ="multi { stream: enum
 }">Names of the streams to start.</ArgTableRow>
<ArgTableRow arg="port" typ="multi { port: enum
 }">Ports to start transmitting from.</ArgTableRow>
<ArgTableRow arg="interface" typ="multi { port: iface_enum
 }">Interfaces to start transmitting from; a port is implied for each.</ArgTableRow>
<ArgTableRow arg="id" typ="multi { id: num [0 .. 255]
 }">Stream IDs to start.</ArgTableRow>
<ArgTableRow arg="packet-size" typ="multi { array-id, array-id, packet-size: range [1 .. 65535]
 }">Override the generated packet size (in bytes); a range generates random sizes.</ArgTableRow>
<ArgTableRow arg="pps" typ="multi { pps: num
 }">Override the packets-per-second rate.</ArgTableRow>
<ArgTableRow arg="mbps" typ="multi { mbps: num
 }">Override the megabits-per-second rate.</ArgTableRow>
<ArgTableRow arg="tx-template" typ="multi { tx-template: enum
 }">Override the packet templates used as the packet content source (up to 16).</ArgTableRow>
<ArgTableRow arg="packet-count" typ="multi { packet-count: num
 }">Override the number of packets to transmit.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="seq" typ="enum (TOT) { TOT:0xffffffff }">Measurement sequence number, or TOT for totals.</ArgTableRow>
<ArgTableRow arg="id" typ="enum (TOT) { TOT:0xffffffff }">Stream ID, or TOT for totals across streams.</ArgTableRow>
<ArgTableRow arg="tx-packet" typ="num">Total packets transmitted.</ArgTableRow>
<ArgTableRow arg="tx-rate" typ="num">Current transmit rate in bps.</ArgTableRow>
<ArgTableRow arg="rx-packet" typ="num">Total packets received.</ArgTableRow>
<ArgTableRow arg="rx-rate" typ="num">Current receive rate in bps.</ArgTableRow>
<ArgTableRow arg="rx-ooo" typ="num">Received packets that were out of order.</ArgTableRow>
<ArgTableRow arg="rx-bad-csum" typ="num">Received packets with a bad checksum.</ArgTableRow>
<ArgTableRow arg="lost-packet" typ="num">Total lost packets (transmitted minus received).</ArgTableRow>
<ArgTableRow arg="lost-rate" typ="num">Current loss rate in bps.</ArgTableRow>
<ArgTableRow arg="lost-ratio" typ="string">Loss as a percentage of transmitted packets.</ArgTableRow>
<ArgTableRow arg="lat-min" typ="string">Minimum measured latency.</ArgTableRow>
<ArgTableRow arg="lat-avg" typ="string">Average measured latency.</ArgTableRow>
<ArgTableRow arg="lat-max" typ="string">Maximum measured latency.</ArgTableRow>
<ArgTableRow arg="jitter" typ="string">Measured latency variation (jitter).</ArgTableRow>
</ArgTable>
