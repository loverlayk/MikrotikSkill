# channel

> RouterOS directory reference for /interface/wifi/channel.

-----------

## interface/wifi/channel 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="frequency" typ="object" unset="1"></ArgTableRow>
<ArgTableRow arg="secondary-frequency" typ="multi { array-id, secondary-frequency: alt { secondary-frequency-disable: enum (disabled)
, secondary-frequency-num: num
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (60ghz-ad | 5ghz-a | 5ghz-n | 5ghz-ac | 5ghz-ax | 5ghz-be | 2ghz-g | 2ghz-n | 2ghz-ax | 2ghz-be | s1ghz-ah | 6ghz-ax | 6ghz-be)" unset="1"></ArgTableRow>
<ArgTableRow arg="width" typ="enum (20mhz | 20/40mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz | 20/40/80+80mhz | 20/40/80/160mhz | 20/40/80/160/320mhz | 1mhz | 1/2mhz | 1/2/4mhz | 1/2/4/8mhz | 2160mhz)" unset="1"></ArgTableRow>
<ArgTableRow arg="skip-dfs-channels" typ="enum (disabled | all | 10min-cac)" unset="1"></ArgTableRow>
<ArgTableRow arg="deprioritize-unii-3-4" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="reselect-interval" typ="super { reselect-interval-min: time [1 .. 60*60*24*300]
, [reselect-interval-max] ..time [1 .. 60*60*24*300]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="reselect-time" typ="super { reselect-time-min: date
, [reselect-time-max] ..date
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="preamble-puncturing" typ="alt { preamble-puncturing: enum (yes | no) { yes:-1, no:0 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="afc" typ="bool" unset="1"></ArgTableRow>
</ArgTable>
