# wifi-logs

> WiFi log monitor for the selected devices.

-----------

## cmr/device/wifi-logs 
**Package:** cmr
**Type:** Command

WiFi log monitor for the selected devices.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="labels" typ="object" unset="1">Select the devices to monitor using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.</ArgTableRow>
<ArgTableRow arg="address" typ="macAddr" unset="1">Filter by client MAC address.</ArgTableRow>
<ArgTableRow arg="bssid" typ="macAddr" unset="1">Filter by BSSID.</ArgTableRow>
<ArgTableRow arg="time" typ="time" unset="1">Filter by time.</ArgTableRow>
<ArgTableRow arg="time-start" typ="date" unset="1">Filter logs from this time.</ArgTableRow>
<ArgTableRow arg="time-end" typ="date" unset="1">Filter logs up to this time.</ArgTableRow>
<ArgTableRow arg="event" typ="enum (connected | disconnected | failed)" unset="1">Filter by event: `connected`, `disconnected`, or `failed`.</ArgTableRow>
</ArgTable>
