# step

> RouterOS directory reference for /routing/stats/step.

-----------

## routing/stats/step 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="context" typ="string"></ArgTableRow>
<ArgTableRow arg="pid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="order" typ="num"></ArgTableRow>
<ArgTableRow arg="runs" typ="num"></ArgTableRow>
<ArgTableRow arg="targets" typ="num"></ArgTableRow>
<ArgTableRow arg="max-time" typ="time"></ArgTableRow>
<ArgTableRow arg="cur-time" typ="time"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (off | on | once) { off:0, on:1, once:2 }"></ArgTableRow>
<ArgTableRow arg="sched" typ="time"></ArgTableRow>
</ArgTable>
