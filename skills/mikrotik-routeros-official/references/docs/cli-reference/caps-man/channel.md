# channel

> RouterOS directory reference for /caps-man/channel.

-----------

## caps-man/channel 
**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="frequency" typ="multi { array-id, frequency: num
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="secondary-frequency" typ="multi { array-id, secondary-frequency: alt { secondary-frequency-disable: enum (disabled)
, secondary-frequency-num: num
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="control-channel-width" typ="enum (5mhz | 10mhz | 20mhz | 40mhz-turbo) { 5mhz:5000, 10mhz:10000, 20mhz:20000, 40mhz-turbo:40000 }" unset="1"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)" unset="1"></ArgTableRow>
<ArgTableRow arg="extension-channel" typ="enum (disabled | Ce | eC | Ceee | eCee | eeCe | eeeC | XX | XXXX | Ceeeeeee | eCeeeeee | eeCeeeee | eeeCeeee | eeeeCeee | eeeeeCee | eeeeeeCe | eeeeeeeC | XXXXXXXX)" unset="1"></ArgTableRow>
<ArgTableRow arg="tx-power" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="save-selected" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="reselect-interval" typ="super { reselect-interval-min: time [1 .. 60*60*24*300]
, [reselect-interval-max] ..time [1 .. 60*60*24*300]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="skip-dfs-channels" typ="bool" unset="1"></ArgTableRow>
</ArgTable>
