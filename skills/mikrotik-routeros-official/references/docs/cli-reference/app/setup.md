# setup

> Starts the interactive setup wizard. It selects the app disk, the LAN bridge, and the router IP address used for app URLs and port forwarding.

-----------

## app/setup 
**Syscap:** app
**Package:** container
**Type:** Command

Starts the interactive setup wizard. It selects the app disk, the LAN bridge, and the router IP address used for app URLs and port forwarding.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="disk" typ="enum (none)">Selected storage disk for application installation</ArgTableRow>
<ArgTableRow arg="lan-bridge" typ="iface_enum { none }">Selected LAN bridge interface for container networking</ArgTableRow>
<ArgTableRow arg="router-ip-alt" typ="alt { router-ip-enum: enum
, router-ip: ipAddr
 }">Manual IP address override for the RouterOS device</ArgTableRow>
</ArgTable>
