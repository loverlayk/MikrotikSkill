# option

> Options the DHCP client can send to the DHCP server. A client sends the options listed in its dhcp-options property. For details, see DHCP Client.

-----------

## ip/dhcp-client/option 
**Type:** Directory

Options the DHCP client can send to the DHCP server. A client sends the options listed in its `dhcp-options` property. For details, see [DHCP Client](../../../network-management/dhcp/client).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">Predefined option.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the option, used in the `dhcp-options` property of the client.</ArgTableRow>
<ArgTableRow arg="code" typ="alt { number: num [1 .. 254]
, option: enum (hostname | vendor-specific | vendor-class-id | client-id) { hostname:12, vendor-specific:43, vendor-class-id:60, client-id:61 }
 }" mandatory="1">DHCP option code (1-254), or one of the names `hostname` (12), `vendor-specific` (43), `vendor-class-id` (60) or `client-id` (61).</ArgTableRow>
<ArgTableRow arg="value" typ="string">
Value of the option, in the same syntax as DHCP server option values. The value can contain these variables:
- `$(HOSTNAME)` - The router's identity.
- `$(CLIENT_MAC)` - MAC address of the client interface.
- `$(CLIENT_DUID)` - The router's DUID, the same DUID the DHCPv6 client uses.
</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="raw-value" typ="string">The option value as it is sent, in hex.</ArgTableRow>
</ArgTable>
