# script

> RouterOS directory reference for /system/script.

-----------

## system/script 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="owner" typ="string"></ArgTableRow>
<ArgTableRow arg="policy" typ="multi { array-id, policy: enum
 }"></ArgTableRow>
<ArgTableRow arg="dont-require-permissions" typ="bool"></ArgTableRow>
<ArgTableRow arg="source" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="last-started" typ="date"></ArgTableRow>
<ArgTableRow arg="run-count" typ="num"></ArgTableRow>
</ArgTable>
