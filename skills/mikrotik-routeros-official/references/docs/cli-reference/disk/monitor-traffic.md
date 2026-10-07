# monitor-traffic

> RouterOS command reference for /disk/monitor-traffic.

-----------

## disk/monitor-traffic 
**Conditions:** !smips
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="io-ops" typ="num">Total number of I/O operations since the last `reset-counters`.</ArgTableRow>
<ArgTableRow arg="io-errors" typ="num">Total number of I/O errors.</ArgTableRow>
<ArgTableRow arg="slot" typ="string">The disk that is being monitored.</ArgTableRow>
<ArgTableRow arg="read-ops" typ="num">Total number of read operations.</ArgTableRow>
<ArgTableRow arg="read-ops-per-second" typ="num">Read operations per second.</ArgTableRow>
<ArgTableRow arg="read-bytes" typ="num">Total bytes read.</ArgTableRow>
<ArgTableRow arg="read-rate" typ="num">Current read speed.</ArgTableRow>
<ArgTableRow arg="read-merges" typ="num">Total number of merged read operations (adjacent requests the driver combined).</ArgTableRow>
<ArgTableRow arg="read-time" typ="time">Total time spent reading.</ArgTableRow>
<ArgTableRow arg="write-ops" typ="num">Total number of write operations.</ArgTableRow>
<ArgTableRow arg="write-ops-per-second" typ="num">Write operations per second.</ArgTableRow>
<ArgTableRow arg="write-bytes" typ="num">Total bytes written.</ArgTableRow>
<ArgTableRow arg="write-rate" typ="num">Current write speed.</ArgTableRow>
<ArgTableRow arg="write-merges" typ="num">Total number of merged write operations.</ArgTableRow>
<ArgTableRow arg="write-time" typ="time">Total time spent writing.</ArgTableRow>
<ArgTableRow arg="in-flight-ops" typ="num">Operations currently queued on the disk.</ArgTableRow>
<ArgTableRow arg="active-time" typ="time">Total time the disk was busy with requests.</ArgTableRow>
<ArgTableRow arg="wait-time" typ="time">Total time requests waited in the queue before being processed.</ArgTableRow>
<ArgTableRow arg="discard-ops" typ="num">Total number of discard (TRIM) operations.</ArgTableRow>
<ArgTableRow arg="discard-bytes" typ="num">Total bytes discarded.</ArgTableRow>
<ArgTableRow arg="discard-merges" typ="num">Total number of merged discard operations.</ArgTableRow>
<ArgTableRow arg="discard-time" typ="time">Total time spent discarding.</ArgTableRow>
<ArgTableRow arg="flush-ops" typ="num">Total number of flush operations.</ArgTableRow>
<ArgTableRow arg="flush-time" typ="time">Total time spent flushing.</ArgTableRow>
</ArgTable>
