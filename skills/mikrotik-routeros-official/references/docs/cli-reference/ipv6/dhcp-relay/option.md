# option

> Options a DHCPv6 relay can add to the Relay-Forward messages it sends. A relay adds the options listed in its dhcp-options property. For details, see DHCP Relay.

-----------

## ipv6/dhcp-relay/option 
**Type:** Directory

Options a DHCPv6 relay can add to the Relay-Forward messages it sends. A relay adds the options listed in its `dhcp-options` property. For details, see [DHCP Relay](../../../network-management/dhcp/relay).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">Predefined option.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the option, used in the `dhcp-options` property of the relay.</ArgTableRow>
<ArgTableRow arg="code" typ="num" mandatory="1">DHCPv6 option code.</ArgTableRow>
<ArgTableRow arg="value" typ="string">Value of the option, in the same syntax as DHCP server option values. The predefined `client_mac` option (code 79) uses `0x0001$(CLIENT_MAC)`, the link-layer type Ethernet followed by the MAC address of the client.</ArgTableRow>
<ArgTableRow arg="only-if-mac-available" typ="bool">Whether to add the option only when the message came directly from a client (not from another relay) and the client's MAC address is known.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="raw-value" typ="string">The option value as it is sent, in hex.</ArgTableRow>
</ArgTable>
