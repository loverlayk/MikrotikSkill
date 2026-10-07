# wiliot

> RouterOS settings reference for /iot/wiliot.

-----------

## iot/wiliot 
**Package:** iot
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="spoof-gps" typ="bool"></ArgTableRow>
<ArgTableRow arg="lat" typ="num"></ArgTableRow>
<ArgTableRow arg="long" typ="num"></ArgTableRow>
<ArgTableRow arg="server" typ="enum (none)">Used MQTT server</ArgTableRow>
<ArgTableRow arg="scanner" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="advertiser" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="wi-fi" typ="iface_enum { none }"></ArgTableRow>
<ArgTableRow arg="features" typ="ubit (gateway, bridge)">supported Wiliot features</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="gateway-id" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="string"></ArgTableRow>
<ArgTableRow arg="owner" typ="string"></ArgTableRow>
</ArgTable>
