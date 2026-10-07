# setup

> Starts the setup wizard that automates networking, storage, and registry configuration for the App system.

-----------

## app/setup 
**Syscap:** app
**Package:** container
**Type:** Command

Starts the setup wizard that automates networking, storage, and registry configuration for the App system.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="disk" typ="enum (none)">Selected storage disk for application installation</ArgTableRow>
<ArgTableRow arg="lan-bridge" typ="iface_enum { none }">Selected LAN bridge interface for container networking</ArgTableRow>
<ArgTableRow arg="router-ip-alt" typ="alt { router-ip-enum: enum
, router-ip: ipAddr
 }">Manual IP address override for the RouterOS device</ArgTableRow>
</ArgTable>
