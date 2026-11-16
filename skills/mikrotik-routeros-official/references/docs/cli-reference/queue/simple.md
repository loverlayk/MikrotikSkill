# simple

> Simple queues: rate limits for the upload and download of a target address, network or interface. See the Simple queue guide.

-----------

## queue/simple 
**Type:** Directory

Simple queues: rate limits for the upload and download of a target address, network or interface. See the [Simple queue](../../../firewall-and-quality-of-service/queues/simple-queue) guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The queue is disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The queue is not in use, for example outside its `time` range or when its queue type does not exist.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">The queue was created by another RouterOS service, not by the user.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the queue.</ArgTableRow>
<ArgTableRow arg="target" typ="object { target: alt { target-interface: iface_enum
, target-address: alt { ip-address: ipPrefix
, ipv6-address: ip6Prefix
 }
 }
 }" mandatory="1">Addresses, networks or interfaces whose traffic the queue limits. Upload is the traffic that the target sends, download is the traffic that it receives. A simple queue must match a packet either by source or by destination: if both ends of a connection are inside the target, all its packets count as download.</ArgTableRow>
<ArgTableRow arg="dst" typ="alt { ip-address: ipPrefix
, ipv6-address: ip6Prefix
, interface: iface_enum
 }">Destination address, network or interface. The queue takes only the traffic between the target and this destination.</ArgTableRow>
<ArgTableRow arg="parent" typ="enum (none) { none:0 }">Parent simple queue, or `none`. Child queues share the rate of their parent. Default: `none`.</ArgTableRow>
<ArgTableRow arg="packet-marks" typ="multi { array-id, packet-mark: enum
 }">Packet marks that the queue takes. Empty means that the queue does not check packet marks. Default: empty.</ArgTableRow>
<ArgTableRow arg="priority" typ="composite { upload-priority: num [1 .. 8]
, download-priority: num [1 .. 8]
 }">Priority of a child queue for upload and download, from `1` (highest) to `8` (lowest). Default: `8/8`.</ArgTableRow>
<ArgTableRow arg="queue" typ="composite { upload-queue: enum
, download-queue: enum
 }">Queue type for upload and download. Default: `default-small/default-small`.</ArgTableRow>
<ArgTableRow arg="limit-at" typ="composite { upload-limit-at: num
, download-limit-at: num
 }">Rate that the queue gets when the queues of the same parent together ask for more than the parent allows. See [HTB](../../../firewall-and-quality-of-service/queues/htb-hierarchical-token-bucket). Default: `0`. The value is in bits per second; the suffixes `k` and `M` are accepted.</ArgTableRow>
<ArgTableRow arg="max-limit" typ="composite { upload-max-limit: num
, download-max-limit: num
 }">Highest rate that the queue allows. `0` means no limit. Default: `0`. The value is in bits per second; the suffixes `k` and `M` are accepted.</ArgTableRow>
<ArgTableRow arg="burst-limit" typ="composite { upload-burst-limit: num
, download-burst-limit: num
 }">Highest rate that the queue allows while burst is active. See [Queue Burst](../../../firewall-and-quality-of-service/queues/queue-burst). Default: `0`. The value is in bits per second; the suffixes `k` and `M` are accepted.</ArgTableRow>
<ArgTableRow arg="burst-threshold" typ="composite { upload-threshold: num
, download-threshold: num
 }">Average rate up to which burst is allowed. Default: `0`. The value is in bits per second; the suffixes `k` and `M` are accepted.</ArgTableRow>
<ArgTableRow arg="burst-time" typ="composite { upload-burst-time: time
, download-burst-time: time
 }">Time over which the average rate for burst is calculated. Default: `0s`.</ArgTableRow>
<ArgTableRow arg="bucket-size" typ="composite { upload-bucket-size: num [ .. 10000]
, download-bucket-size: num [ .. 10000]
 }">Size of the HTB token bucket as a multiple of `max-limit`. See [HTB](../../../firewall-and-quality-of-service/queues/htb-hierarchical-token-bucket). Default: `0.1`.</ArgTableRow>
<ArgTableRow arg="total-priority" typ="num">Priority for the limit of upload and download together. Default: not set.</ArgTableRow>
<ArgTableRow arg="total-queue" typ="enum">Queue type for the limit of upload and download together. Default: not set.</ArgTableRow>
<ArgTableRow arg="total-limit-at" typ="num">`limit-at` for upload and download together. Default: not set.</ArgTableRow>
<ArgTableRow arg="total-max-limit" typ="num">Highest rate for upload and download together. Default: not set.</ArgTableRow>
<ArgTableRow arg="total-burst-limit" typ="num">`burst-limit` for upload and download together. Default: not set.</ArgTableRow>
<ArgTableRow arg="total-burst-threshold" typ="num">`burst-threshold` for upload and download together. Default: not set.</ArgTableRow>
<ArgTableRow arg="total-burst-time" typ="time">`burst-time` for upload and download together. Default: not set.</ArgTableRow>
<ArgTableRow arg="total-bucket-size" typ="num">`bucket-size` for upload and download together. Default: not set.</ArgTableRow>
<ArgTableRow arg="time" typ="super { !
, start: time
, [end] -time
, [day] ,ubit (sun, mon, tue, wed, thu, fri, sat)
 }">Time range and days in which the queue is active. Outside this time the queue has the `I` flag and limits no traffic. Default: not set, always active.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="bytes" typ="composite { upload: num
, download: num
 }">Number of bytes that passed the queue.</ArgTableRow>
<ArgTableRow arg="total-bytes" typ="num">Number of bytes counted by the limit of upload and download together.</ArgTableRow>
<ArgTableRow arg="packets" typ="composite { upload: num
, download: num
 }">Number of packets that passed the queue.</ArgTableRow>
<ArgTableRow arg="total-packets" typ="num">Number of packets counted by the limit of upload and download together.</ArgTableRow>
<ArgTableRow arg="dropped" typ="composite { upload: num
, download: num
 }">Number of packets that the queue dropped.</ArgTableRow>
<ArgTableRow arg="total-dropped" typ="num">Number of packets dropped by the limit of upload and download together.</ArgTableRow>
<ArgTableRow arg="rate" typ="composite { upload: num
, download: num
 }">Average rate of the traffic that passes the queue, in bits per second, for upload and download.</ArgTableRow>
<ArgTableRow arg="total-rate" typ="num">Average rate counted by the limit of upload and download together, in bits per second.</ArgTableRow>
<ArgTableRow arg="packet-rate" typ="composite { upload: num
, download: num
 }">Average rate of the traffic that passes the queue, in packets per second.</ArgTableRow>
<ArgTableRow arg="total-packet-rate" typ="num">Average rate counted by the limit of upload and download together, in packets per second.</ArgTableRow>
<ArgTableRow arg="queued-packets" typ="composite { upload: num
, download: num
 }">Number of packets that wait in the queue.</ArgTableRow>
<ArgTableRow arg="total-queued-packets" typ="num">Number of packets that wait in the queue for upload and download together.</ArgTableRow>
<ArgTableRow arg="queued-bytes" typ="composite { upload: num
, download: num
 }">Number of bytes that wait in the queue.</ArgTableRow>
<ArgTableRow arg="total-queued-bytes" typ="num">Number of bytes that wait in the queue for upload and download together.</ArgTableRow>
<ArgTableRow arg="pcq-queues" typ="composite { upload: num
, download: num
 }">Number of PCQ sub-streams, when the queue type is a PCQ type.</ArgTableRow>
<ArgTableRow arg="total-pcq-queues" typ="num">Number of PCQ sub-streams of the queue for upload and download together.</ArgTableRow>
</ArgTable>
