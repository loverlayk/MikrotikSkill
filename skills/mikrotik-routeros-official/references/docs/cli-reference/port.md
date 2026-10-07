# port

> RouterOS directory reference for /port.

-----------

## port 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="baud-rate" typ="enum (auto | 50 | 75 | 110 | 134 | 150 | 200 | 300 | 600 | 1200 | 1800 | 2400 | 4800 | 9600 | 19200 | 38400 | 57600 | 115200 | 230400 | 460800 | 500000 | 576000 | 921600 | 1000000 | 1152000 | 1500000 | 2000000 | 2500000 | 3000000 | 3500000 | 4000000) { auto:0, 50:50, 75:75, 110:110, 134:134, 150:150, 200:200, 300:300, 600:600, 1200:1200, 1800:1800, 2400:2400, 4800:4800, 9600:9600, 19200:19200, 38400:38400, 57600:57600, 115200:115200, 230400:230400, 460800:460800, 500000:500000, 576000:576000, 921600:921600, 1000000:1000000, 1152000:1152000, 1500000:1500000, 2000000:2000000, 2500000:2500000, 3000000:3000000, 3500000:3500000, 4000000:4000000 }"></ArgTableRow>
<ArgTableRow arg="data-bits" typ="enum (7 | 8) { 7:0, 8:1 }"></ArgTableRow>
<ArgTableRow arg="parity" typ="enum (none | odd | even) { none:0, odd:1, even:2 }"></ArgTableRow>
<ArgTableRow arg="stop-bits" typ="enum (1 | 2) { 1:1, 2:2 }"></ArgTableRow>
<ArgTableRow arg="flow-control" typ="enum (xon-xoff | hardware | none) { xon-xoff:0, hardware:1, none:2 }"></ArgTableRow>
<ArgTableRow arg="latency-timer" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="rts" typ="enum (off | on)"></ArgTableRow>
<ArgTableRow arg="dtr" typ="enum (off | on)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="used-by" typ="string"></ArgTableRow>
<ArgTableRow arg="device" typ="string"></ArgTableRow>
<ArgTableRow arg="channels" typ="num"></ArgTableRow>
<ArgTableRow arg="line-state" typ="multi { array-id, line: enum (dtr | rts | cts | dcd | ri | dsr) { dtr:1, rts:2, cts:5, dcd:6, ri:7, dsr:8 }
 }"></ArgTableRow>
</ArgTable>
