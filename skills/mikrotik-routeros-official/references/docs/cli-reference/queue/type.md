# type

> Queue types: named sets of settings for a queuing algorithm. Simple queues, queue trees and interface queues use them. See the Queue types guide.

-----------

## queue/type 
**Type:** Directory

Queue types: named sets of settings for a queuing algorithm. Simple queues, queue trees and interface queues use them. See the [Queue types](../../firewall-and-quality-of-service/queues/queue-types) guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">Default queue type. Its settings can be changed, but it cannot be removed.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the queue type.</ArgTableRow>
<ArgTableRow arg="kind" typ="enum (bfifo | pfifo | red | sfq | pcq | mq-pfifo | none | codel | fq-codel | cake) { bfifo:1, pfifo:2, red:3, sfq:4, pcq:5, mq-pfifo:6, none:7, codel:8, fq-codel:9, cake:10 }" mandatory="1">Queuing algorithm of the type. `none` means no software queue. See [Queue types](../../firewall-and-quality-of-service/queues/queue-types) for a description of each kind.</ArgTableRow>
<ArgTableRow arg="bfifo-limit" typ="num">Queue size in bytes. Default: `15000`.</ArgTableRow>
<ArgTableRow arg="pfifo-limit" typ="num">Queue size in packets. Default: `50`.</ArgTableRow>
<ArgTableRow arg="red-limit" typ="num">Hard limit of the queue, in packets. Default: `60`.</ArgTableRow>
<ArgTableRow arg="red-min-threshold" typ="num">Average queue size, in packets, at which RED starts to drop packets at random. Default: `10`.</ArgTableRow>
<ArgTableRow arg="red-max-threshold" typ="num">Average queue size, in packets, at which RED drops every new packet. Default: `50`.</ArgTableRow>
<ArgTableRow arg="red-burst" typ="num">Number of packets that RED accepts in a burst before the average queue size follows. Default: `20`.</ArgTableRow>
<ArgTableRow arg="red-avg-packet" typ="num">Average packet size in bytes that RED uses to calculate the average queue size. Default: `1000`.</ArgTableRow>
<ArgTableRow arg="sfq-perturb" typ="num">Time in seconds after which SFQ changes how it sorts packets into flows. Default: `5`.</ArgTableRow>
<ArgTableRow arg="sfq-allot" typ="num">Number of bytes that a flow sends in one turn. Default: `1514`.</ArgTableRow>
<ArgTableRow arg="pcq-rate" typ="num">Rate limit of each sub-stream, in bits per second. `0` means no limit for a sub-stream: every active sub-stream sends the same number of packets. Default: `0`.</ArgTableRow>
<ArgTableRow arg="pcq-limit" typ="num">Queue size of one sub-stream, in KiB. Default: `50KiB`.</ArgTableRow>
<ArgTableRow arg="pcq-classifier" typ="ubit (src-address, dst-address, src-port, dst-port)">What one sub-stream is. Select one or several values. Default: empty, all traffic is one sub-stream.</ArgTableRow>
<ArgTableRow arg="pcq-total-limit" typ="num">Queue size of all sub-streams together, in KiB. Default: `2000KiB`.</ArgTableRow>
<ArgTableRow arg="pcq-burst-rate" typ="num">Rate that a sub-stream can reach while burst is allowed. See [Queue Burst](../../firewall-and-quality-of-service/queues/queue-burst). Default: `0`.</ArgTableRow>
<ArgTableRow arg="pcq-burst-threshold" typ="num">Average rate of a sub-stream up to which burst is allowed. Default: `0`.</ArgTableRow>
<ArgTableRow arg="pcq-burst-time" typ="time">Time over which the average rate of a sub-stream is calculated. Default: `10s`.</ArgTableRow>
<ArgTableRow arg="pcq-src-address-mask" typ="num">Prefix length of the IPv4 network that is one sub-stream when the classifier has `src-address`. Default: `32`.</ArgTableRow>
<ArgTableRow arg="pcq-dst-address-mask" typ="num">Prefix length of the IPv4 network that is one sub-stream when the classifier has `dst-address`. Default: `32`.</ArgTableRow>
<ArgTableRow arg="pcq-src-address6-mask" typ="num">Prefix length of the IPv6 network that is one sub-stream when the classifier has `src-address`. Default: `128`.</ArgTableRow>
<ArgTableRow arg="pcq-dst-address6-mask" typ="num">Prefix length of the IPv6 network that is one sub-stream when the classifier has `dst-address`. Default: `128`.</ArgTableRow>
<ArgTableRow arg="mq-pfifo-limit" typ="num">Size of each queue in packets. Default: `50`.</ArgTableRow>
<ArgTableRow arg="codel-limit" typ="num">Hard limit of the queue, in packets. Default: `1000`.</ArgTableRow>
<ArgTableRow arg="codel-interval" typ="time">Time over which CoDel checks the waiting time of packets. Set it to about the round-trip time of the connections. Default: `100ms`.</ArgTableRow>
<ArgTableRow arg="codel-target" typ="time">Waiting time of packets that the queue accepts. Default: `5ms`.</ArgTableRow>
<ArgTableRow arg="codel-ecn" typ="bool">Whether CoDel marks packets of ECN-capable connections instead of dropping them. Default: `no`.</ArgTableRow>
<ArgTableRow arg="codel-ce-threshold" typ="time">Waiting time from which CoDel marks packets of ECN-capable connections. Default: not set.</ArgTableRow>
<ArgTableRow arg="fq-codel-limit" typ="num">Hard limit of all flow queues together, in packets. Default: `10240`.</ArgTableRow>
<ArgTableRow arg="fq-codel-interval" typ="time">Time over which CoDel checks the waiting time of packets. Set it to about the round-trip time of the connections. Default: `100ms`.</ArgTableRow>
<ArgTableRow arg="fq-codel-target" typ="time">Waiting time of packets that the queue accepts. Default: `5ms`.</ArgTableRow>
<ArgTableRow arg="fq-codel-ecn" typ="bool">Whether FQ-CoDel marks packets of ECN-capable connections instead of dropping them. Default: `yes`.</ArgTableRow>
<ArgTableRow arg="fq-codel-ce-threshold" typ="time">Waiting time from which FQ-CoDel marks packets of ECN-capable connections. Default: not set.</ArgTableRow>
<ArgTableRow arg="fq-codel-flows" typ="num">Number of flow queues into which FQ-CoDel sorts packets. Default: `1024`.</ArgTableRow>
<ArgTableRow arg="fq-codel-memlimit" typ="num">Memory limit for the packets in all flow queues together. Default: `32.0MiB`.</ArgTableRow>
<ArgTableRow arg="fq-codel-quantum" typ="num">Number of bytes that a flow sends in one turn. Default: `1514`.</ArgTableRow>
<ArgTableRow arg="cake-bandwidth" typ="num">Rate of the shaper that is built into CAKE. `0` means no shaping by CAKE: use it when HTB sets the rate. Default: `0`. See [CAKE](../../firewall-and-quality-of-service/queues/queue-types/cake).</ArgTableRow>
<ArgTableRow arg="cake-autorate-ingress" typ="bool">Whether CAKE estimates the link capacity from the arriving packets and adjusts its shaper. Default: not set.</ArgTableRow>
<ArgTableRow arg="cake-overhead" typ="num">Bytes that CAKE adds to the size of each packet for the overhead of the link, from `-64` to `256`. Default: `0`.</ArgTableRow>
<ArgTableRow arg="cake-mpu" typ="num">Smallest packet size on the link, in bytes, from `0` to `256`. Smaller packets are counted with this size. Default: not set.</ArgTableRow>
<ArgTableRow arg="cake-atm" typ="enum (none | atm | ptm) { none:0, atm:1, ptm:2 }">Framing compensation: `atm` for ATM cells, `ptm` for PTM encoding, `none`. Default: not set.</ArgTableRow>
<ArgTableRow arg="cake-overhead-scheme" typ="multi { cake-overhead-scheme: enum (raw | conservative | ipoa-vcmux | ipoa-llcsnap | bridged-vcmux | bridged-llcsnap | pppoa-vcmux | pppoa-llc | pppoe-vcmux | pppoe-llcsnap | pppoe-ptm | bridged-ptm | via-ethernet | ethernet | ether-vlan | docsis) { raw:1, conservative:2, ipoa-vcmux:3, ipoa-llcsnap:4, bridged-vcmux:5, bridged-llcsnap:6, pppoa-vcmux:7, pppoa-llc:8, pppoe-vcmux:9, pppoe-llcsnap:10, pppoe-ptm:11, bridged-ptm:12, via-ethernet:13, ethernet:14, ether-vlan:15, docsis:16 }
 }">Preset for `cake-overhead`, `cake-mpu` and `cake-atm` that matches a link technology. Default: empty. See [CAKE](../../firewall-and-quality-of-service/queues/queue-types/cake).</ArgTableRow>
<ArgTableRow arg="cake-rtt" typ="time">Round-trip time that CAKE uses to tune its queue management. Default: `100ms`.</ArgTableRow>
<ArgTableRow arg="cake-rtt-scheme" typ="enum (none | datacentre | lan | metro | regional | internet | oceanic | satellite | interplanetary) { none:0, datacentre:1, lan:2, metro:3, regional:4, internet:5, oceanic:6, satellite:7, interplanetary:8 }">Preset for `cake-rtt`. Default: not set. See [CAKE](../../firewall-and-quality-of-service/queues/queue-types/cake).</ArgTableRow>
<ArgTableRow arg="cake-diffserv" typ="enum (diffserv3 | diffserv4 | diffserv8 | besteffort | precedence) { diffserv3:0, diffserv4:1, diffserv8:2, besteffort:3, precedence:4 }">How CAKE sorts packets into priority classes by their DSCP value. `besteffort` uses one class. Default: `diffserv3`. See [CAKE](../../firewall-and-quality-of-service/queues/queue-types/cake).</ArgTableRow>
<ArgTableRow arg="cake-flowmode" typ="enum (flowblind | srchost | dsthost | hosts | flows | dual-srchost | dual-dsthost | triple-isolate) { flowblind:0, srchost:1, dsthost:2, hosts:3, flows:4, dual-srchost:5, dual-dsthost:6, triple-isolate:7 }">How CAKE separates traffic into queues: by flow, by source or destination host, or by both. Default: `triple-isolate`. See [CAKE](../../firewall-and-quality-of-service/queues/queue-types/cake).</ArgTableRow>
<ArgTableRow arg="cake-nat" typ="bool">Whether CAKE looks up the addresses before NAT, so that it separates the hosts behind a router that translates addresses. Default: `no`.</ArgTableRow>
<ArgTableRow arg="cake-wash" typ="bool">Whether CAKE clears the DSCP value of the packets after it has used it. Default: `no`.</ArgTableRow>
<ArgTableRow arg="cake-ack-filter" typ="enum (none | filter | aggressive) { none:0, filter:1, aggressive:2 }">Whether CAKE removes redundant TCP acknowledgments: `none`, `filter` or `aggressive`. Default: `none`.</ArgTableRow>
<ArgTableRow arg="cake-memlimit" typ="num">Memory limit for the packets that CAKE holds in its queues. Default: not set.</ArgTableRow>
</ArgTable>
