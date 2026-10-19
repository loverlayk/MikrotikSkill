# start

> RouterOS command reference for /tool/traffic-generator/start.

-----------

## tool/traffic-generator/start 
**Type:** Command
Starts the traffic generator in the background. All parameters override the values configured in the stream and the packet template (like in the quick command).

<ArgTable c1="Argument" c2="Type" c3="Description">
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
