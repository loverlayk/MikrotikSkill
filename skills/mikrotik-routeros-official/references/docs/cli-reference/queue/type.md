# type

> RouterOS directory reference for /queue/type.

-----------

## queue/type 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="kind" typ="enum (bfifo | pfifo | red | sfq | pcq | mq-pfifo | none | codel | fq-codel | cake) { bfifo:1, pfifo:2, red:3, sfq:4, pcq:5, mq-pfifo:6, none:7, codel:8, fq-codel:9, cake:10 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="bfifo-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="pfifo-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="red-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="red-min-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="red-max-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="red-burst" typ="num"></ArgTableRow>
<ArgTableRow arg="red-avg-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="sfq-perturb" typ="num"></ArgTableRow>
<ArgTableRow arg="sfq-allot" typ="num"></ArgTableRow>
<ArgTableRow arg="pcq-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="pcq-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="pcq-classifier" typ="ubit (src-address, dst-address, src-port, dst-port)"></ArgTableRow>
<ArgTableRow arg="pcq-total-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="pcq-burst-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="pcq-burst-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="pcq-burst-time" typ="time"></ArgTableRow>
<ArgTableRow arg="pcq-src-address-mask" typ="num"></ArgTableRow>
<ArgTableRow arg="pcq-dst-address-mask" typ="num"></ArgTableRow>
<ArgTableRow arg="pcq-src-address6-mask" typ="num"></ArgTableRow>
<ArgTableRow arg="pcq-dst-address6-mask" typ="num"></ArgTableRow>
<ArgTableRow arg="mq-pfifo-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="codel-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="codel-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="codel-target" typ="time"></ArgTableRow>
<ArgTableRow arg="codel-ecn" typ="bool"></ArgTableRow>
<ArgTableRow arg="codel-ce-threshold" typ="time"></ArgTableRow>
<ArgTableRow arg="fq-codel-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="fq-codel-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="fq-codel-target" typ="time"></ArgTableRow>
<ArgTableRow arg="fq-codel-ecn" typ="bool"></ArgTableRow>
<ArgTableRow arg="fq-codel-ce-threshold" typ="time"></ArgTableRow>
<ArgTableRow arg="fq-codel-flows" typ="num"></ArgTableRow>
<ArgTableRow arg="fq-codel-memlimit" typ="num"></ArgTableRow>
<ArgTableRow arg="fq-codel-quantum" typ="num"></ArgTableRow>
<ArgTableRow arg="cake-bandwidth" typ="num"></ArgTableRow>
<ArgTableRow arg="cake-autorate-ingress" typ="bool"></ArgTableRow>
<ArgTableRow arg="cake-overhead" typ="num"></ArgTableRow>
<ArgTableRow arg="cake-mpu" typ="num"></ArgTableRow>
<ArgTableRow arg="cake-atm" typ="enum (none | atm | ptm) { none:0, atm:1, ptm:2 }"></ArgTableRow>
<ArgTableRow arg="cake-overhead-scheme" typ="multi { cake-overhead-scheme: enum (raw | conservative | ipoa-vcmux | ipoa-llcsnap | bridged-vcmux | bridged-llcsnap | pppoa-vcmux | pppoa-llc | pppoe-vcmux | pppoe-llcsnap | pppoe-ptm | bridged-ptm | via-ethernet | ethernet | ether-vlan | docsis) { raw:1, conservative:2, ipoa-vcmux:3, ipoa-llcsnap:4, bridged-vcmux:5, bridged-llcsnap:6, pppoa-vcmux:7, pppoa-llc:8, pppoe-vcmux:9, pppoe-llcsnap:10, pppoe-ptm:11, bridged-ptm:12, via-ethernet:13, ethernet:14, ether-vlan:15, docsis:16 }
 }"></ArgTableRow>
<ArgTableRow arg="cake-rtt" typ="time"></ArgTableRow>
<ArgTableRow arg="cake-rtt-scheme" typ="enum (none | datacentre | lan | metro | regional | internet | oceanic | satellite | interplanetary) { none:0, datacentre:1, lan:2, metro:3, regional:4, internet:5, oceanic:6, satellite:7, interplanetary:8 }"></ArgTableRow>
<ArgTableRow arg="cake-diffserv" typ="enum (diffserv3 | diffserv4 | diffserv8 | besteffort | precedence) { diffserv3:0, diffserv4:1, diffserv8:2, besteffort:3, precedence:4 }"></ArgTableRow>
<ArgTableRow arg="cake-flowmode" typ="enum (flowblind | srchost | dsthost | hosts | flows | dual-srchost | dual-dsthost | triple-isolate) { flowblind:0, srchost:1, dsthost:2, hosts:3, flows:4, dual-srchost:5, dual-dsthost:6, triple-isolate:7 }"></ArgTableRow>
<ArgTableRow arg="cake-nat" typ="bool"></ArgTableRow>
<ArgTableRow arg="cake-wash" typ="bool"></ArgTableRow>
<ArgTableRow arg="cake-ack-filter" typ="enum (none | filter | aggressive) { none:0, filter:1, aggressive:2 }"></ArgTableRow>
<ArgTableRow arg="cake-memlimit" typ="num"></ArgTableRow>
</ArgTable>
