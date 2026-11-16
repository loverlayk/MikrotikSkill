# ip

> The /ip/hotspot/walled-garden/ip menu lists the packets that devices can send before login, by address, protocol, and port. Each rule is added to the firewall as dynamic rules. See the HotSpot guide.

-----------

## ip/hotspot/walled-garden/ip 
**Type:** Directory

The `/ip/hotspot/walled-garden/ip` menu lists the packets that devices can send before login, by address, protocol, and port. Each rule is added to the firewall as dynamic rules. See the [HotSpot](../../../../authentication-authorization-accounting/hotspot-captive-portal) guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The rule is disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The rule is invalid.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="server" typ="super { !
, server: enum
 }">HotSpot server to which the rule applies.</ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, range: ipRange
 }">IP address of the client.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, range: ipRange
 }">Destination IP address.</ArgTableRow>
<ArgTableRow arg="dst-host" typ="string">Destination host name. The router adds a dynamic rule with the address that the name resolves to.</ArgTableRow>
<ArgTableRow arg="protocol" typ="super { !
, protocol: enum ()
 }">IP protocol.</ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }">Destination port or port range.</ArgTableRow>
<ArgTableRow arg="src-address-list" typ="super { !
, address-list: enum
 }">Firewall address list with the client addresses.</ArgTableRow>
<ArgTableRow arg="dst-address-list" typ="super { !
, address-list: enum
 }">Firewall address list with the destination addresses.</ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | drop | reject) { accept:0, drop:10, reject:11 }">`accept` - the packet passes without login. `drop` - the packet is dropped. `reject` - the packet is dropped and an ICMP message is sent to the client.</ArgTableRow>
</ArgTable>
