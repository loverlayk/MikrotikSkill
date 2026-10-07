# tree

> RouterOS directory reference for /queue/tree.

-----------

## queue/tree 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="parent" typ="enum (global) { global:0xfffff4 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="packet-mark" typ="multi { array-id, packet-mark: enum
 }"></ArgTableRow>
<ArgTableRow arg="limit-at" typ="num"></ArgTableRow>
<ArgTableRow arg="queue" typ="enum"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="max-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="burst-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="burst-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="burst-time" typ="time"></ArgTableRow>
<ArgTableRow arg="bucket-size" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="packets" typ="num"></ArgTableRow>
<ArgTableRow arg="dropped" typ="num"></ArgTableRow>
<ArgTableRow arg="rate" typ="num"></ArgTableRow>
<ArgTableRow arg="packet-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="queued-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="queued-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="pcq-queues" typ="num"></ArgTableRow>
</ArgTable>
