# spectral-scan

> RouterOS command reference for /interface/wireless/spectral-scan.

-----------

## interface/wireless/spectral-scan 
**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="range" typ="alt { range: range [ .. 7000]
, band: enum (2.4ghz | 5ghz | current-channel) { 2.4ghz:1, 5ghz:2, current-channel:3 }
 }"></ArgTableRow>
<ArgTableRow arg="show-interference" typ="bool"></ArgTableRow>
<ArgTableRow arg="samples" typ="num"></ArgTableRow>
<ArgTableRow arg="buckets" typ="num"></ArgTableRow>
<ArgTableRow arg="peak-hold-time" typ="time"></ArgTableRow>
<ArgTableRow arg="save-file-name" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="freq" typ="num"></ArgTableRow>
<ArgTableRow arg="interference" typ="composite { type: enum (none | bluetooth-headset | bluetooth-stereo | cordless-phone | microwave-oven | cwa | video-bridge | wifi) { none:0xffffffff, bluetooth-headset:0, bluetooth-stereo:1, cordless-phone:2, microwave-oven:3, cwa:4, video-bridge:5, wifi:6 }
, rssi: num
 }"></ArgTableRow>
<ArgTableRow arg="dbm" typ="num"></ArgTableRow>
<ArgTableRow arg="graph" typ="meter"></ArgTableRow>
</ArgTable>
