# decode-ad

> RouterOS command reference for /iot/bluetooth/decode-ad.

-----------

## iot/bluetooth/decode-ad 
**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="data" typ="string"></ArgTableRow>
<ArgTableRow arg="key" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (unknown | mikrotik | ibeacon | eddystone-uid | eddystone-url | eddystone-tlm | eddystone-eid) { unknown:0, mikrotik:1, ibeacon:2, eddystone-uid:3, eddystone-url:4, eddystone-tlm:5, eddystone-eid:6 }"></ArgTableRow>
<ArgTableRow arg="version" typ="num"></ArgTableRow>
<ArgTableRow arg="encrypted" typ="bool"></ArgTableRow>
<ArgTableRow arg="acc-x" typ="num"></ArgTableRow>
<ArgTableRow arg="acc-y" typ="num"></ArgTableRow>
<ArgTableRow arg="acc-z" typ="num"></ArgTableRow>
<ArgTableRow arg="temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="uptime" typ="num"></ArgTableRow>
<ArgTableRow arg="flags" typ="multi { array-id, flags: enum (reed-switch | tilt | free-fall | impact-x | impact-y | impact-z) { reed-switch:0, tilt:1, free-fall:2, impact-x:3, impact-y:4, impact-z:5 }
 }"></ArgTableRow>
<ArgTableRow arg="battery" typ="num"></ArgTableRow>
<ArgTableRow arg="uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="major" typ="num"></ArgTableRow>
<ArgTableRow arg="minor" typ="num"></ArgTableRow>
<ArgTableRow arg="rssi-at-1m" typ="num"></ArgTableRow>
<ArgTableRow arg="namespace" typ="string"></ArgTableRow>
<ArgTableRow arg="instance" typ="string"></ArgTableRow>
<ArgTableRow arg="battery-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="packet-count" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-power" typ="num"></ArgTableRow>
<ArgTableRow arg="eid" typ="string"></ArgTableRow>
</ArgTable>
