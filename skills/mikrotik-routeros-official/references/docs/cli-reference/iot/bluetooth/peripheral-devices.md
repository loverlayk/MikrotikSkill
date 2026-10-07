# peripheral-devices

> RouterOS directory reference for /iot/bluetooth/peripheral-devices.

-----------

## iot/bluetooth/peripheral-devices 
**Package:** iot
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address-type" typ="enum (public | random) { public:0, random:1 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr" mandatory="1"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="persist" typ="bool"></ArgTableRow>
<ArgTableRow arg="mtik-key" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="rssi" typ="num"></ArgTableRow>
<ArgTableRow arg="last-data" typ="string">Advertisement data in hex format</ArgTableRow>
<ArgTableRow arg="last-seen" typ="date"></ArgTableRow>
<ArgTableRow arg="beacon-types" typ="multi { array-id, beacon-types: enum (unknown | mikrotik | ibeacon | eddystone-uid | eddystone-url | eddystone-tlm | eddystone-eid) { unknown:0, mikrotik:1, ibeacon:2, eddystone-uid:3, eddystone-url:4, eddystone-tlm:5, eddystone-eid:6 }
 }"></ArgTableRow>
<ArgTableRow arg="mtik-version" typ="num"></ArgTableRow>
<ArgTableRow arg="mtik-encrypted" typ="bool"></ArgTableRow>
<ArgTableRow arg="mtik-acc-x" typ="num"></ArgTableRow>
<ArgTableRow arg="mtik-acc-y" typ="num"></ArgTableRow>
<ArgTableRow arg="mtik-acc-z" typ="num"></ArgTableRow>
<ArgTableRow arg="mtik-temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="mtik-battery" typ="num"></ArgTableRow>
<ArgTableRow arg="mtik-uptime" typ="num"></ArgTableRow>
<ArgTableRow arg="mtik-flags" typ="multi { array-id, flags: enum (reed-switch | tilt | free-fall | impact-x | impact-y | impact-z) { reed-switch:0, tilt:1, free-fall:2, impact-x:3, impact-y:4, impact-z:5 }
 }"></ArgTableRow>
<ArgTableRow arg="ibeacon-uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="ibeacon-major" typ="num"></ArgTableRow>
<ArgTableRow arg="ibeacon-minor" typ="num"></ArgTableRow>
<ArgTableRow arg="ibeacon-rssi-at-1m" typ="num"></ArgTableRow>
<ArgTableRow arg="eddy-rssi-at-1m" typ="num"></ArgTableRow>
<ArgTableRow arg="eddy-namespace" typ="string"></ArgTableRow>
<ArgTableRow arg="eddy-instance" typ="string"></ArgTableRow>
<ArgTableRow arg="eddy-version" typ="num"></ArgTableRow>
<ArgTableRow arg="eddy-battery-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="eddy-temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="eddy-packet-count" typ="num"></ArgTableRow>
<ArgTableRow arg="eddy-uptime" typ="num"></ArgTableRow>
<ArgTableRow arg="eddy-tx-power" typ="num"></ArgTableRow>
<ArgTableRow arg="eddy-eid" typ="string"></ArgTableRow>
</ArgTable>
