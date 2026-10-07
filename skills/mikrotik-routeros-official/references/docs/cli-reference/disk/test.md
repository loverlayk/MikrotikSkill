# test

> RouterOS command reference for /disk/test.

-----------

## disk/test 
**Conditions:** !smips
**Type:** Command

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="N" typ="initializing">The test is initializing (preparing, clearing the caches) and has not started reading or writing yet.</ArgTableRow>
<ArgTableRow arg="R" typ="running">The test is running.</ArgTableRow>
<ArgTableRow arg="F" typ="failed">The test failed.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="disk" typ="multi { array-id, disk: enum
 }">Disk or partition to test.</ArgTableRow>
<ArgTableRow arg="block-size" typ="num">Size of one read or write block. Default: 64 KiB.</ArgTableRow>
<ArgTableRow arg="thread-count" typ="num">Number of parallel test threads. Default: 1.</ArgTableRow>
<ArgTableRow arg="direction" typ="enum (read | write)">
What the test does with the data.
- `read` (default) - Read the disk; does not change its content.
- `write` - Write to the disk; destroys all data on it.
</ArgTableRow>
<ArgTableRow arg="type" typ="enum (device | filesystem)">Test target: `device` reads or writes the raw block device, `filesystem` goes through the mounted file system. Default: device.</ArgTableRow>
<ArgTableRow arg="pattern" typ="enum (sequential | random)">
Access pattern.
- `sequential` (default) - Read or write consecutive blocks.
- `random` - Read or write blocks at random positions.
</ArgTableRow>
<ArgTableRow arg="entries-to-show" typ="num">How many of the most recent result rows to keep and show.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="seq" typ="enum (TOT) { TOT:0xffffffff }">Sequence number of the result row; the `TOT` row aggregates all threads.</ArgTableRow>
<ArgTableRow arg="rate" typ="num">Current throughput of this row.</ArgTableRow>
<ArgTableRow arg="iops" typ="num">Input/output operations per second.</ArgTableRow>
<ArgTableRow arg="bytes" typ="num">Bytes transferred for this row so far.</ArgTableRow>
<ArgTableRow arg="disk" typ="enum (TOT) { TOT:0xffffffff }">The tested disk.</ArgTableRow>
<ArgTableRow arg="thread" typ="enum (TOT) { TOT:0xffffffff }">Thread this row belongs to; `TOT` aggregates all threads.</ArgTableRow>
<ArgTableRow arg="type" typ="enum (device | filesystem)">Test type as given when the test was started.</ArgTableRow>
<ArgTableRow arg="pattern" typ="enum (sequential | random)">Access pattern as given when the test was started.</ArgTableRow>
<ArgTableRow arg="dir" typ="enum (read | write)">Direction (`read` or `write`) as given when the test was started.</ArgTableRow>
<ArgTableRow arg="bsize" typ="num">Block size as given when the test was started.</ArgTableRow>
<ArgTableRow arg="state" typ="string">State of a running test, for example `clear caches` while it prepares and `run` while it works.</ArgTableRow>
</ArgTable>
