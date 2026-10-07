# show

> RouterOS command reference for /system/dashboard/show.

-----------

## system/dashboard/show 
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="model" typ="string"></ArgTableRow>
<ArgTableRow arg="board-name" typ="string"></ArgTableRow>
<ArgTableRow arg="identity" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="cpu-usage" typ="num"></ArgTableRow>
<ArgTableRow arg="memory-usage" typ="composite { used: num
, total: num
 }"></ArgTableRow>
<ArgTableRow arg="hdd-usage" typ="composite { used: num
, total: num
 }"></ArgTableRow>
<ArgTableRow arg="ether" typ="super { running: num
, [enabled] /num
, [total] /num
 }"></ArgTableRow>
<ArgTableRow arg="wifi" typ="super { running: num
, [enabled] /num
, [total] /num
 }"></ArgTableRow>
<ArgTableRow arg="total-bw" typ="super { tx: num
, [rx] /num
 }"></ArgTableRow>
<ArgTableRow arg="uplink-bw" typ="super { tx: num
, [rx] /num
 }"></ArgTableRow>
<ArgTableRow arg="ether-bw" typ="super { tx: num
, [rx] /num
 }"></ArgTableRow>
<ArgTableRow arg="wifi-bw" typ="super { tx: num
, [rx] /num
 }"></ArgTableRow>
<ArgTableRow arg="lte-bw" typ="super { tx: num
, [rx] /num
 }"></ArgTableRow>
</ArgTable>
