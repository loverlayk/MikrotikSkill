# routes

> Bindings found in the servers' replies by DHCPv6 relays with store-relayed-bindings=yes. The relay adds a route to each delegated prefix through the client. For details, see DHCP Relay.

-----------

## ipv6/dhcp-relay/routes 
**Type:** Directory

Bindings found in the servers' replies by DHCPv6 relays with `store-relayed-bindings=yes`. The relay adds a route to each delegated prefix through the client. For details, see [DHCP Relay](../../../network-management/dhcp/relay).

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="relay" typ="enum">DHCPv6 relay that saw the binding.</ArgTableRow>
<ArgTableRow arg="prefix" typ="ip6Prefix">Delegated prefix or assigned address.</ArgTableRow>
<ArgTableRow arg="peer-address" typ="ip6Addr">Address of the client, usually its link-local address, used as the gateway of the route.</ArgTableRow>
<ArgTableRow arg="life-time" typ="time">Lifetime of the binding.</ArgTableRow>
<ArgTableRow arg="last-seen" typ="time">Time since the relay last saw the binding in a reply.</ArgTableRow>
</ArgTable>
