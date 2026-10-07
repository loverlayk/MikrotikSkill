# interfaces

> Interface assignments for the NAT-PMP service: the interface that connects to the Internet (external) and the interfaces the NAT-PMP clients are connected to (internal). The list accepts only one external interface...

-----------

## ip/nat-pmp/interfaces 
**Type:** Directory

Interface assignments for the NAT-PMP service: the interface that connects to the Internet (`external`) and the interfaces the NAT-PMP clients are connected to (`internal`). The list accepts only one external interface (`only one external interface can be added to the list`). See the [NAT-PMP guide page](../../../firewall-and-quality-of-service/nat-pmp).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled. The interface is not used by NAT-PMP. New entries are created enabled.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Name of the interface. On an `internal` interface, the service listens for client requests and sends external address announcements on the multicast group 224.0.0.1, UDP port 5350.</ArgTableRow>
<ArgTableRow arg="type" typ="enum (external | internal)" mandatory="1">
NAT-PMP interface role:
- `external` - the interface facing the Internet. Only one external interface is allowed.
- `internal` - the local interface the NAT-PMP clients are connected to.
</ArgTableRow>
<ArgTableRow arg="forced-ip" typ="super { forced-ip: ipAddr
 }">Report this address to clients as the router's external address instead of the interface address, for example when the external interface has several addresses.</ArgTableRow>
</ArgTable>
