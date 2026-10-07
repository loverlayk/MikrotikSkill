# show

> RouterOS command reference for /interface/wifi/dashboard/show.

-----------

## interface/wifi/dashboard/show 
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="multi { array-id, interface: iface_enum
 }" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="ifaces" typ="num"></ArgTableRow>
<ArgTableRow arg="aps-total" typ="num"></ArgTableRow>
<ArgTableRow arg="aps-run" typ="num"></ArgTableRow>
<ArgTableRow arg="slaveaps-total" typ="num"></ArgTableRow>
<ArgTableRow arg="aps-2g" typ="num"></ArgTableRow>
<ArgTableRow arg="aps-5g" typ="num"></ArgTableRow>
<ArgTableRow arg="aps-6g" typ="num"></ArgTableRow>
<ArgTableRow arg="aps-be" typ="num"></ArgTableRow>
<ArgTableRow arg="aps-ax" typ="num"></ArgTableRow>
<ArgTableRow arg="aps-ac" typ="num"></ArgTableRow>
<ArgTableRow arg="aps-n" typ="num"></ArgTableRow>
<ArgTableRow arg="aps-ofdm" typ="num"></ArgTableRow>
<ArgTableRow arg="stas-total" typ="num"></ArgTableRow>
<ArgTableRow arg="stas-2ghz" typ="num"></ArgTableRow>
<ArgTableRow arg="stas-5ghz" typ="num"></ArgTableRow>
<ArgTableRow arg="stas-6ghz" typ="num"></ArgTableRow>
<ArgTableRow arg="stas-open" typ="num"></ArgTableRow>
<ArgTableRow arg="stas-wpa" typ="num"></ArgTableRow>
<ArgTableRow arg="stas-wpa2" typ="num"></ArgTableRow>
<ArgTableRow arg="stas-wpa3" typ="num"></ArgTableRow>
<ArgTableRow arg="stas-eap" typ="num"></ArgTableRow>
<ArgTableRow arg="stas-ft" typ="num"></ArgTableRow>
<ArgTableRow arg="stas-be" typ="num"></ArgTableRow>
<ArgTableRow arg="stas-ax" typ="num"></ArgTableRow>
<ArgTableRow arg="stas-ac" typ="num"></ArgTableRow>
<ArgTableRow arg="stas-n" typ="num"></ArgTableRow>
<ArgTableRow arg="stas-ofdm" typ="num"></ArgTableRow>
<ArgTableRow arg="bw-total-down" typ="num"></ArgTableRow>
<ArgTableRow arg="bw-total-up" typ="num"></ArgTableRow>
<ArgTableRow arg="ap-freqs" typ="multi { array-id, array-id, array-id, range: super { start: num
, [end] -num
, [value] :num
 }
 }"></ArgTableRow>
<ArgTableRow arg="sta-freqs" typ="multi { array-id, array-id, array-id, range: super { start: num
, [end] -num
, [value] :num
 }
 }"></ArgTableRow>
</ArgTable>
