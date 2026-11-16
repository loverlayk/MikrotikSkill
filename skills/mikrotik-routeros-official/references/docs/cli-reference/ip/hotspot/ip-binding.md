# ip-binding

> The /ip/hotspot/ip-binding menu sets how the HotSpot treats single devices: let them through without login, block them, or translate their address. See the HotSpot guide.

-----------

## ip/hotspot/ip-binding 
**Type:** Directory

The `/ip/hotspot/ip-binding` menu sets how the HotSpot treats single devices: let them through without login, block them, or translate their address. See the [HotSpot](../../../authentication-authorization-accounting/hotspot-captive-portal) guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The binding is disabled.</ArgTableRow>
<ArgTableRow arg="P" typ="bypassed">The binding has `type=bypassed`.</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">The binding has `type=blocked`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the device.</ArgTableRow>
<ArgTableRow arg="address" typ="ipRange">IP address or address range of the devices.</ArgTableRow>
<ArgTableRow arg="to-address" typ="ipAddr">IP address to which the address of the device is translated.</ArgTableRow>
<ArgTableRow arg="server" typ="enum (all) { all:0 }">HotSpot server to which the binding applies. Default: `all`.</ArgTableRow>
<ArgTableRow arg="type" typ="enum (regular | bypassed | blocked) { regular:0, bypassed:1, blocked:2 }">
What the HotSpot does with the device:
- `regular` - the device logs in as usual; its address is translated to `to-address`
- `bypassed` - the device has network access without login
- `blocked` - the packets of the device are dropped
</ArgTableRow>
</ArgTable>
