# device

> Devices of Kid Control. A device is identified by its MAC address. The list also shows, as dynamic entries, the other devices that the router has seen. See Kid Control.

-----------

## ip/kid-control/device 
**Type:** Directory

Devices of Kid Control. A device is identified by its MAC address. The list also shows, as dynamic entries, the other devices that the router has seen. See [Kid Control](../../../../firewall-and-quality-of-service/kid-control).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The device entry is disabled.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">The entry is dynamic: a device that the router has seen and that is not added to a profile.</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">The device is blocked now.</ArgTableRow>
<ArgTableRow arg="L" typ="limited">The device is rate-limited now.</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="all" typ="switch"></ArgTableRow>
<ArgTableRow arg="static" typ="switch"></ArgTableRow>
<ArgTableRow arg="dynamic" typ="switch"></ArgTableRow>
<ArgTableRow arg="name" typ="string">Name of the device.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr" mandatory="1">MAC address of the device. The router takes the IP address of the device from the ARP table.</ArgTableRow>
<ArgTableRow arg="user" typ="enum () { :0xffffffff }" mandatory="1">Profile of `/ip/kid-control` that the device belongs to.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="ip-address" typ="object { server: alt { ip: ipAddr
, ipv6: ip6Addr
 }
 }">IP address of the device, taken from the ARP table.</ArgTableRow>
<ArgTableRow arg="activity" typ="string"></ArgTableRow>
<ArgTableRow arg="rate-down" typ="num">Current download data rate of the device.</ArgTableRow>
<ArgTableRow arg="rate-up" typ="num">Current upload data rate of the device.</ArgTableRow>
<ArgTableRow arg="bytes-down" typ="num">Number of bytes that the device has downloaded since the counters were reset.</ArgTableRow>
<ArgTableRow arg="bytes-up" typ="num">Number of bytes that the device has uploaded since the counters were reset.</ArgTableRow>
<ArgTableRow arg="idle-time" typ="time">Time since the router last saw traffic of the device.</ArgTableRow>
</ArgTable>
