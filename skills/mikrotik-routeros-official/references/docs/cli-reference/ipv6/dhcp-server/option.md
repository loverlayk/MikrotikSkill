# option

> Additional options the DHCPv6 server can send, assigned with dhcp-option to a server or a binding, or grouped in option sets. For details, see DHCPv6 Server.

-----------

## ipv6/dhcp-server/option 
**Type:** Directory

Additional options the DHCPv6 server can send, assigned with `dhcp-option` to a server or a binding, or grouped in option sets. For details, see [DHCPv6 Server](../../../../network-management/dhcp/dhcpv6-server).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the option, used where options are assigned.</ArgTableRow>
<ArgTableRow arg="code" typ="num" mandatory="1">DHCPv6 option code, for example 23 for DNS servers.</ArgTableRow>
<ArgTableRow arg="value" typ="string">Value of the option, in the same syntax as DHCP server option values. An IPv6 address in quotes is sent as 16 bytes, for example `'2001:db8::53'`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="raw-value" typ="string">The option value as it is sent, in hex.</ArgTableRow>
</ArgTable>
