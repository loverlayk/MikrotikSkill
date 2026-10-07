# joineui

> RouterOS directory reference for /iot/lora/joineui.

-----------

## iot/lora/joineui 
**Package:** iot
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="logging" typ="bool"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (whitelist | blacklist) { whitelist:1, blacklist:2 }"></ArgTableRow>
<ArgTableRow arg="joineuis" typ="object { range: composite { min: string
, max: string
 }
 }"></ArgTableRow>
</ArgTable>
