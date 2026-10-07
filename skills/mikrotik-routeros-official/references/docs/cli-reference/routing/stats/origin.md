# origin

> RouterOS directory reference for /routing/stats/origin.

-----------

## routing/stats/origin 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="Y" typ="synthetic">synthetic</ArgTableRow>
<ArgTableRow arg="Z" typ="terminal">terminal</ArgTableRow>
<ArgTableRow arg="X" typ="stopping">stopping</ArgTableRow>
<ArgTableRow arg="A" typ="abandoned">abandoned</ArgTableRow>
<ArgTableRow arg="H" typ="hold">hold</ArgTableRow>
<ArgTableRow arg="U" typ="attrs-updated">attrs-updated</ArgTableRow>
<ArgTableRow arg="M" typ="attrs-merge">attrs-merge</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="string"></ArgTableRow>
<ArgTableRow arg="instance-id" typ="num"></ArgTableRow>
<ArgTableRow arg="dealer-id" typ="num"></ArgTableRow>
<ArgTableRow arg="publisher-idx" typ="num"></ArgTableRow>
<ArgTableRow arg="route-type" typ="string"></ArgTableRow>
<ArgTableRow arg="pid" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="route-count" typ="multi { route-count: num
 }"></ArgTableRow>
<ArgTableRow arg="in-policy" typ="num"></ArgTableRow>
<ArgTableRow arg="update.in-policy" typ="num"></ArgTableRow>
<ArgTableRow arg="total-route-count" typ="num"></ArgTableRow>
</ArgTable>
