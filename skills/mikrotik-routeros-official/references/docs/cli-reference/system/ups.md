# ups

> RouterOS directory reference for /system/ups.

-----------

## system/ups 
**Package:** ups
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="port" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="offline-time" typ="time"></ArgTableRow>
<ArgTableRow arg="min-runtime" typ="alt { never: enum (never) { never:0xffffffff }
, min-runtime: time
 }"></ArgTableRow>
<ArgTableRow arg="alarm-setting" typ="enum (immediate | delayed | low-battery | none) { immediate:0, delayed:1, low-battery:2, none:3 }"></ArgTableRow>
<ArgTableRow arg="check-capabilities" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="model" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="serial" typ="string"></ArgTableRow>
<ArgTableRow arg="manufacture-date" typ="string"></ArgTableRow>
<ArgTableRow arg="load" typ="num"></ArgTableRow>
<ArgTableRow arg="on-line" typ="bool"></ArgTableRow>
<ArgTableRow arg="nominal-battery-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="offline-after" typ="time"></ArgTableRow>
</ArgTable>
