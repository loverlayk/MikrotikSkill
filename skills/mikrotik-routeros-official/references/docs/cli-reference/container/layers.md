# layers

> RouterOS directory reference for /container/layers.

-----------

## container/layers 
**Package:** container
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="layer-dir" typ="string"></ArgTableRow>
<ArgTableRow arg="size" typ="alt { size: num
, size-state: enum (unavailable | pending | done)
 }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (layer | root-dir)"></ArgTableRow>
<ArgTableRow arg="containers" typ="multi { container: enum
 }"></ArgTableRow>
</ArgTable>
