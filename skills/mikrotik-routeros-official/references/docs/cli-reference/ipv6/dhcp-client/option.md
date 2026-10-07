# option

> Options the DHCPv6 client can send to the DHCPv6 server. A client sends the options listed in its dhcp-options property. For details, see DHCPv6 Client.

-----------

## ipv6/dhcp-client/option 
**Type:** Directory

Options the DHCPv6 client can send to the DHCPv6 server. A client sends the options listed in its `dhcp-options` property. For details, see [DHCPv6 Client](../../../network-management/dhcp/dhcpv6-client).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">Predefined option.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the option, used in the `dhcp-options` property of the client.</ArgTableRow>
<ArgTableRow arg="code" typ="num" mandatory="1">DHCPv6 option code.</ArgTableRow>
<ArgTableRow arg="value" typ="string">Value of the option, in the same syntax as DHCP server option values. The predefined `fqdn` option uses the variables `$(HOSTNAME)` (the router's identity) and `$(HOSTNAME_LEN)` (its length): `0x00$(HOSTNAME_LEN)$(HOSTNAME)`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="raw-value" typ="string">The option value as it is sent, in hex.</ArgTableRow>
</ArgTable>
