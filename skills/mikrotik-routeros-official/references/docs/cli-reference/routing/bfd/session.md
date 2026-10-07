# session

> RouterOS directory reference for /routing/bfd/session.

-----------

## routing/bfd/session 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="U" typ="up">up</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="multihop" typ="bool"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="local-address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (admin-down | down | init | up)"></ArgTableRow>
<ArgTableRow arg="state-changes" typ="num"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="desired-tx-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="actual-tx-interval" typ="time">real-time frequency at which the device currently sends BFD control packets.</ArgTableRow>
<ArgTableRow arg="required-min-rx" typ="time"></ArgTableRow>
<ArgTableRow arg="remote-min-rx" typ="time"></ArgTableRow>
<ArgTableRow arg="remote-min-tx" typ="time"></ArgTableRow>
<ArgTableRow arg="multiplier" typ="num"></ArgTableRow>
<ArgTableRow arg="hold-time" typ="time"></ArgTableRow>
<ArgTableRow arg="packets-rx" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-tx" typ="num"></ArgTableRow>
</ArgTable>
