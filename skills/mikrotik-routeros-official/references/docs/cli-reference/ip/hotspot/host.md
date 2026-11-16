# host

> The /ip/hotspot/host menu lists the devices that the HotSpot servers see, logged in or not.

-----------

## ip/hotspot/host 
**Type:** Directory

The `/ip/hotspot/host` menu lists the devices that the HotSpot servers see, logged in or not.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="S" typ="static">Static host.</ArgTableRow>
<ArgTableRow arg="H" typ="DHCP">The host got its address from the DHCP server.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">Dynamic host.</ArgTableRow>
<ArgTableRow arg="A" typ="authorized">The host is logged in.</ArgTableRow>
<ArgTableRow arg="P" typ="bypassed">The host is bypassed by an IP binding.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the device.</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr">IP address that the device uses.</ArgTableRow>
<ArgTableRow arg="to-address" typ="ipAddr">IP address to which the HotSpot translates the address of the device. It can be the same as `address`.</ArgTableRow>
<ArgTableRow arg="server" typ="enum">HotSpot server to which the device is connected.</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">Time since the host was added.</ArgTableRow>
<ArgTableRow arg="idle-time" typ="time">Time since the last traffic from the host.</ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="time">Idle timeout that applies to the host.</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="time">Keepalive timeout that applies to the host.</ArgTableRow>
<ArgTableRow arg="host-dead-time" typ="time">Time for which the host has been unreachable.</ArgTableRow>
<ArgTableRow arg="bridge-port" typ="iface_enum">Bridge port through which the device is connected, when the HotSpot runs on a bridge.</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num">VLAN ID with which the packets of the device arrive.</ArgTableRow>
<ArgTableRow arg="http-proxy" typ="composite { address: ipAddr
, port: num
 }">Proxy server that the browser of the device is set to use.</ArgTableRow>
<ArgTableRow arg="bytes-in" typ="num">Bytes received from the host.</ArgTableRow>
<ArgTableRow arg="bytes-out" typ="num">Bytes sent to the host.</ArgTableRow>
<ArgTableRow arg="packets-in" typ="num">Packets received from the host.</ArgTableRow>
<ArgTableRow arg="packets-out" typ="num">Packets sent to the host.</ArgTableRow>
<ArgTableRow arg="found-by" typ="string">Packet that created the entry, for example `UDP :48767 -> 192.168.88.1:53`.</ArgTableRow>
</ArgTable>
