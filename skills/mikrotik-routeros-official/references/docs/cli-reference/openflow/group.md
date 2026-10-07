# group

> RouterOS directory reference for /openflow/group.

-----------

## openflow/group 
**Package:** openflow
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum">Controller name that installed the group.</ArgTableRow>
<ArgTableRow arg="id" typ="num">Identifier of the group.</ArgTableRow>
<ArgTableRow arg="type" typ="enum (all | select | indirect | ff)">Group type that determines how the action buckets are processed: all, select, indirect, or fast failover.</ArgTableRow>
<ArgTableRow arg="bucket-count" typ="num">Number of action buckets in the group.</ArgTableRow>
<ArgTableRow arg="flow-count" typ="num">Number of flow entries that reference the group.</ArgTableRow>
<ArgTableRow arg="buckets" typ="string">List of action buckets in the group.</ArgTableRow>
<ArgTableRow arg="bytes" typ="num">Number of bytes processed by the group.</ArgTableRow>
<ArgTableRow arg="packets" typ="num">Number of packets processed by the group.</ArgTableRow>
<ArgTableRow arg="duration" typ="time">Time since the group was installed.</ArgTableRow>
<ArgTableRow arg="bucket-stats" typ="string">Per-bucket packet and byte statistics.</ArgTableRow>
</ArgTable>
