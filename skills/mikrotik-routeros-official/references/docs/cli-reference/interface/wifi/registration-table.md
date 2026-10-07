# registration-table

> RouterOS directory reference for /interface/wifi/registration-table.

-----------

## interface/wifi/registration-table 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="A" typ="authorized">authorized</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="dhcp-address" typ="address"></ArgTableRow>
<ArgTableRow arg="dhcp-hostname" typ="string"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="last-activity" typ="time"></ArgTableRow>
<ArgTableRow arg="signal" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-per-link" typ="multi { array-id, signal-l: num
 }"></ArgTableRow>
<ArgTableRow arg="auth-type" typ="enum (wpa2-eap | wpa2-psk | ft-eap | ft-wpa2-psk | wpa3-eap | wpa2-psk-sha2 | wpa3-psk | wpa3-psk-gd | ft-wpa3-psk | ft-wpa3-psk-gd | wpa3-eap-192 | ft-wpa3-eap-192 | owe | wpa-eap | wpa-psk | dpp)"></ArgTableRow>
<ArgTableRow arg="mfp" typ="bool"></ArgTableRow>
<ArgTableRow arg="band" typ="multi { array-id, band: enum ()
 }"></ArgTableRow>
<ArgTableRow arg="mld-interfaces" typ="multi { array-id, iface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="mld-link-addresses" typ="multi { array-id, addr: macAddr
 }"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-rate-per-link" typ="multi { array-id, tx-l-rate: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-rate-per-link" typ="multi { array-id, rx-l-rate: num
 }"></ArgTableRow>
<ArgTableRow arg="packets" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-packets-per-link" typ="multi { array-id, tx-l-packets: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-packets-per-link" typ="multi { array-id, rx-l-packets: num
 }"></ArgTableRow>
<ArgTableRow arg="bytes" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-bytes-per-link" typ="multi { array-id, tx-l-bytes: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-bytes-per-link" typ="multi { array-id, rx-l-bytes: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-bits-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bits-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-bits-per-second-per-link" typ="multi { array-id, tx-l-bps: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-bits-per-second-per-link" typ="multi { array-id, rx-l-bps: num
 }"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="eap-identity" typ="string"></ArgTableRow>
<ArgTableRow arg="eap-username" typ="string"></ArgTableRow>
</ArgTable>
