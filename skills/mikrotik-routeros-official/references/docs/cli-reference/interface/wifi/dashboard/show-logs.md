# show-logs

> RouterOS command reference for /interface/wifi/dashboard/show-logs.

-----------

## interface/wifi/dashboard/show-logs 
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="multi { array-id, interface: iface_enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr" unset="1"></ArgTableRow>
<ArgTableRow arg="bssid" typ="macAddr" unset="1"></ArgTableRow>
<ArgTableRow arg="time" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="time-start" typ="date" unset="1"></ArgTableRow>
<ArgTableRow arg="time-end" typ="date" unset="1"></ArgTableRow>
<ArgTableRow arg="event" typ="enum (connected | disconnected | failed)" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="time" typ="date"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="event" typ="enum (connected | disconnected | failed)"></ArgTableRow>
<ArgTableRow arg="bssid" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="signal" typ="num"></ArgTableRow>
<ArgTableRow arg="auth-type" typ="enum (wpa2-eap | wpa2-psk | ft-eap | ft-wpa2-psk | wpa3-eap | wpa2-psk-sha2 | wpa3-psk | wpa3-psk-gd | ft-wpa3-psk | ft-wpa3-psk-gd | wpa3-eap-192 | ft-wpa3-eap-192 | owe | wpa-eap | wpa-psk | dpp)"></ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="reason" typ="string"></ArgTableRow>
</ArgTable>
