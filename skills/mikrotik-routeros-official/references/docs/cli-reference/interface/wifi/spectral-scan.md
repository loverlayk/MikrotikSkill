# spectral-scan

> RouterOS command reference for /interface/wifi/spectral-scan.

-----------

## interface/wifi/spectral-scan 
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="resolution" typ="enum (312khz | 625khz | 1.25mhz | 2.5mhz | 5mhz | 10mhz | 20mhz | 40mhz | 80mhz) { 312khz:312, 625khz:625, 1.25mhz:1250, 2.5mhz:2500, 5mhz:5000, 10mhz:10000, 20mhz:20000, 40mhz:40000, 80mhz:80000 }"></ArgTableRow>
<ArgTableRow arg="data" typ="enum (min | max | avg) { min:0, max:1, avg:2 }"></ArgTableRow>
<ArgTableRow arg="range" typ="composite { start: num [2400000 .. 7000000]
, end: num [2400000 .. 7000000]
 }"></ArgTableRow>
<ArgTableRow arg="peak-mode" typ="enum (disabled | avg | max) { disabled:0, avg:1, max:2 }"></ArgTableRow>
<ArgTableRow arg="peak-hold-duration" typ="num"></ArgTableRow>
<ArgTableRow arg="show-interference" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="freq" typ="num"></ArgTableRow>
<ArgTableRow arg="magn" typ="num"></ArgTableRow>
<ArgTableRow arg="peak" typ="num"></ArgTableRow>
<ArgTableRow arg="graph" typ="meter"></ArgTableRow>
<ArgTableRow arg="interference" typ="composite { type: enum (mwo | cw | wifi | cordless24 | cordless5 | bluetooth | fhss |  ) { mwo:0, cw:1, wifi:2, cordless24:3, cordless5:4, bluetooth:5, fhss:6,  :7 }
, rssi: num
 }"></ArgTableRow>
</ArgTable>
