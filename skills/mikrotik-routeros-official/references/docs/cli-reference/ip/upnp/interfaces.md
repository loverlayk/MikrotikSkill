# interfaces

> Interface assignments for the UPnP service: which interface connects to the Internet (external) and which interfaces the local UPnP clients are connected to (internal). Each external interface gets its own...

-----------

## ip/upnp/interfaces 
**Type:** Directory

Interface assignments for the UPnP service: which interface connects to the Internet (`external`) and which interfaces the local UPnP clients are connected to (`internal`). Each external interface gets its own WANConnectionDevice service, so several external interfaces can be active at the same time. See the [UPnP guide page](../../../firewall-and-quality-of-service/upnp).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled. The interface is not used by UPnP. New entries are created enabled.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Name of the interface. On an `internal` interface the control service listens on TCP port 2828 of its addresses and SSDP announcements are sent out of it.</ArgTableRow>
<ArgTableRow arg="type" typ="enum (external | internal) { external:1, internal:2 }" mandatory="1">
UPnP interface role:
- `external` - the interface facing the Internet. Dynamic dst-nat rules for client port mappings are created with this interface as `in-interface` and its address as `dst-address`.
- `internal` - the local interface the UPnP clients are connected to.
</ArgTableRow>
<ArgTableRow arg="forced-ip" typ="super { forced-ip: ipAddr
 }">Use this address as the external IP address of the interface: it is reported to clients in `GetExternalIPAddress` responses and used as `dst-address` in the dynamic dst-nat rules. Set when the external interface has several addresses. When not set, the primary address of the interface is used.</ArgTableRow>
</ArgTable>
