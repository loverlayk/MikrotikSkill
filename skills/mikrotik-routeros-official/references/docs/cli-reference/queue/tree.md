# tree

> Queue tree: rate limits for traffic in one direction, selected by packet mark, on an interface or globally. See the Queue tree guide.

-----------

## queue/tree 
**Type:** Directory

Queue tree: rate limits for traffic in one direction, selected by packet mark, on an interface or globally. See the [Queue tree](../../../firewall-and-quality-of-service/queues/queue-tree) guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The queue is disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The queue is invalid and not in use.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the queue.</ArgTableRow>
<ArgTableRow arg="parent" typ="enum (global) { global:0xfffff4 }" mandatory="1">Where the queue is attached: an interface, `global`, or another queue tree entry.</ArgTableRow>
<ArgTableRow arg="packet-mark" typ="multi { array-id, packet-mark: enum
 }">Packet mark that the queue takes. `no-mark` takes the packets that have no packet mark. Leave it empty on a queue that has child queues. Default: empty.</ArgTableRow>
<ArgTableRow arg="limit-at" typ="num">Rate that the queue gets when the queues of the same parent together ask for more than the parent allows. See [HTB](../../../firewall-and-quality-of-service/queues/htb-hierarchical-token-bucket). Default: `0`. The value is in bits per second; the suffixes `k` and `M` are accepted.</ArgTableRow>
<ArgTableRow arg="queue" typ="enum">Queue type. Default: `default-small`.</ArgTableRow>
<ArgTableRow arg="priority" typ="num">Priority of a child queue, from `1` (highest) to `8` (lowest). Default: `8`.</ArgTableRow>
<ArgTableRow arg="max-limit" typ="num">Highest rate that the queue allows. `0` means no limit. Default: `0`. The value is in bits per second; the suffixes `k` and `M` are accepted.</ArgTableRow>
<ArgTableRow arg="burst-limit" typ="num">Highest rate that the queue allows while burst is active. See [Queue Burst](../../../firewall-and-quality-of-service/queues/queue-burst). Default: `0`. The value is in bits per second; the suffixes `k` and `M` are accepted.</ArgTableRow>
<ArgTableRow arg="burst-threshold" typ="num">Average rate up to which burst is allowed. Default: `0`. The value is in bits per second; the suffixes `k` and `M` are accepted.</ArgTableRow>
<ArgTableRow arg="burst-time" typ="time">Time over which the average rate for burst is calculated. Default: `0s`.</ArgTableRow>
<ArgTableRow arg="bucket-size" typ="num">Size of the HTB token bucket as a multiple of `max-limit`. See [HTB](../../../firewall-and-quality-of-service/queues/htb-hierarchical-token-bucket). Default: `0.1`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="bytes" typ="num">Number of bytes that passed the queue.</ArgTableRow>
<ArgTableRow arg="packets" typ="num">Number of packets that passed the queue.</ArgTableRow>
<ArgTableRow arg="dropped" typ="num">Number of packets that the queue dropped.</ArgTableRow>
<ArgTableRow arg="rate" typ="num">Average rate of the traffic that passes the queue, in bits per second.</ArgTableRow>
<ArgTableRow arg="packet-rate" typ="num">Average rate of the traffic that passes the queue, in packets per second.</ArgTableRow>
<ArgTableRow arg="queued-packets" typ="num">Number of packets that wait in the queue.</ArgTableRow>
<ArgTableRow arg="queued-bytes" typ="num">Number of bytes that wait in the queue.</ArgTableRow>
<ArgTableRow arg="pcq-queues" typ="num">Number of PCQ sub-streams, when the queue type is a PCQ type.</ArgTableRow>
</ArgTable>
