# dhcp-relay

> The DHCPv6 relay forwards DHCPv6 messages from clients on its interface to DHCPv6 servers, wrapped in Relay-Forward messages, and delivers the servers' Relay-Reply messages back to the clients. For an overview, see...

-----------

## ipv6/dhcp-relay 
**Type:** Directory

The DHCPv6 relay forwards DHCPv6 messages from clients on its interface to DHCPv6 servers, wrapped in Relay-Forward messages, and delivers the servers' Relay-Reply messages back to the clients. For an overview, see [DHCP Relay](../../../network-management/dhcp/relay).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The relay is disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The relay configuration is invalid.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the relay.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Interface on which the relay listens for messages from clients.</ArgTableRow>
<ArgTableRow arg="dhcp-server" typ="object { server: alt { interface-address: composite { address6: ip6Addr
, interface: iface_enum
 }
, address6: ip6Addr
 }
 }" mandatory="1">DHCPv6 servers to forward Relay-Forward messages to. A link-local address is given with its interface, for example `fe80::1%ether1`.</ArgTableRow>
<ArgTableRow arg="dhcp-options" typ="multi { array-id, option: enum
 }">Options (`/ipv6/dhcp-relay/option`) added to Relay-Forward messages. The Interface-ID option (18) is always added. Default: client_mac, the client link-layer address (option 79).</ArgTableRow>
<ArgTableRow arg="link-address" typ="ip6Addr">Address sent in the link-address field of Relay-Forward messages, which a server can use to identify the client's link. With `::`, no address is sent. Default: ::.</ArgTableRow>
<ArgTableRow arg="delay-threshold" typ="alt { const: enum (none) { none:0 }
, time: time
 }">Minimum value of the elapsed-time field a message must have to be forwarded. With `none`, all messages are forwarded. Default: none.</ArgTableRow>
<ArgTableRow arg="store-relayed-bindings" typ="bool">Whether to keep the bindings found in the servers' replies and add routes to them through the client, so traffic to delegated prefixes behind the relay is routed. The bindings are listed in `/ipv6/dhcp-relay/routes`. Default: no.</ArgTableRow>
</ArgTable>
