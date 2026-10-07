# sniffer

> RouterOS settings reference for /interface/wireless/sniffer.

-----------

## interface/wireless/sniffer 
**Package:** wireless-rep
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="multiple-channels" typ="bool"></ArgTableRow>
<ArgTableRow arg="channel-time" typ="time"></ArgTableRow>
<ArgTableRow arg="only-headers" typ="bool"></ArgTableRow>
<ArgTableRow arg="receive-errors" typ="bool"></ArgTableRow>
<ArgTableRow arg="memory-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="file-name" typ="string"></ArgTableRow>
<ArgTableRow arg="file-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="streaming-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="streaming-server" typ="super { ip: ipAddr
, [port] [ :num [1 .. 65535]]
 }"></ArgTableRow>
<ArgTableRow arg="streaming-max-rate" typ="num"></ArgTableRow>
</ArgTable>
