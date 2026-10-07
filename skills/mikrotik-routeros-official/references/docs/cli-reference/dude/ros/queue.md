# queue

> RouterOS directory reference for /dude/ros/queue.

-----------

## dude/ros/queue 
**Package:** dude
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="target" typ="object { target: alt { target-address: alt { ip-address: ipPrefix
, ipv6-address: ip6Prefix
 }
, target-interface: enum
 }
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="dst" typ="alt { ip-address: ipPrefix
, ipv6-address: ip6Prefix
, interface: enum
 }"></ArgTableRow>
<ArgTableRow arg="parent" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="packet-marks" typ="multi { array-id, packet-mark: string
 }"></ArgTableRow>
<ArgTableRow arg="priority" typ="composite { upload-priority: num [1 .. 8]
, download-priority: num [1 .. 8]
 }"></ArgTableRow>
<ArgTableRow arg="queue" typ="composite { upload-queue: enum
, download-queue: enum
 }"></ArgTableRow>
<ArgTableRow arg="limit-at" typ="composite { upload-limit-at: num
, download-limit-at: num
 }"></ArgTableRow>
<ArgTableRow arg="max-limit" typ="composite { upload-max-limit: num
, download-max-limit: num
 }"></ArgTableRow>
<ArgTableRow arg="burst-limit" typ="composite { upload-burst-limit: num
, download-burst-limit: num
 }"></ArgTableRow>
<ArgTableRow arg="burst-threshold" typ="composite { upload-threshold: num
, download-threshold: num
 }"></ArgTableRow>
<ArgTableRow arg="burst-time" typ="composite { upload-burst-time: time
, download-burst-time: time
 }"></ArgTableRow>
<ArgTableRow arg="bucket-size" typ="composite { upload-bucket-size: num [ .. 10000]
, download-bucket-size: num [ .. 10000]
 }"></ArgTableRow>
<ArgTableRow arg="total-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="total-queue" typ="enum"></ArgTableRow>
<ArgTableRow arg="total-limit-at" typ="num"></ArgTableRow>
<ArgTableRow arg="total-max-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="total-burst-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="total-burst-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="total-burst-time" typ="time"></ArgTableRow>
<ArgTableRow arg="total-bucket-size" typ="num"></ArgTableRow>
<ArgTableRow arg="time" typ="super { start: time
, [end] -time
, [day] ,ubit (sun, mon, tue, wed, thu, fri, sat)
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="bytes" typ="composite { upload: num
, download: num
 }"></ArgTableRow>
<ArgTableRow arg="total-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="packets" typ="composite { upload: num
, download: num
 }"></ArgTableRow>
<ArgTableRow arg="total-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="dropped" typ="composite { upload: num
, download: num
 }"></ArgTableRow>
<ArgTableRow arg="total-dropped" typ="num"></ArgTableRow>
<ArgTableRow arg="rate" typ="composite { upload: num
, download: num
 }"></ArgTableRow>
<ArgTableRow arg="total-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="packet-rate" typ="composite { upload: num
, download: num
 }"></ArgTableRow>
<ArgTableRow arg="total-packet-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="queued-packets" typ="composite { upload: num
, download: num
 }"></ArgTableRow>
<ArgTableRow arg="total-queued-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="queued-bytes" typ="composite { upload: num
, download: num
 }"></ArgTableRow>
<ArgTableRow arg="total-queued-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="pcq-queues" typ="composite { upload: num
, download: num
 }"></ArgTableRow>
<ArgTableRow arg="total-pcq-queues" typ="num"></ArgTableRow>
</ArgTable>
