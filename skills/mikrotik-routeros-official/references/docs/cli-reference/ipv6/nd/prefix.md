# prefix

> Prefix information sent in router advertisement (RA) messages used for stateless address autoconfiguration (RFC 4862). By default, autoconfiguration applies only to hosts and not routers.

-----------

## ipv6/nd/prefix 
**Type:** Directory

Prefix information sent in router advertisement (RA) messages used for stateless address autoconfiguration ([RFC 4862](https://tools.ietf.org/html/rfc4862)). By default, autoconfiguration applies only to hosts and not routers.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="prefix" typ="alt { none: enum (none) { none:0 }
, prefix: ip6Prefix
 }">Prefix used for stateless address autoconfiguration. If the option "none" is selected, RouterOS advertises only options and does not include a specific prefix.</ArgTableRow>
<ArgTableRow arg="6to4-interface" typ="iface_enum { none:0xffffffff }">If set, RouterOS combines this prefix with the interface IPv4 address to produce a valid 6to4 prefix. RouterOS replaces the first 16 bits with 2002 and the next 32 bits with the interface's configured IPv4 address. It advertises the remaining 80 bits, including the SLA ID, as configured.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Interface on which stateless autoconfiguration runs.</ArgTableRow>
<ArgTableRow arg="on-link" typ="bool">When set, indicates that RouterOS can treat this prefix as on-link. When not set, RA messages do not make any statement about the prefix's on-link or off-link status. The prefix might still be used for address configuration while some addresses in the prefix remain off-link.</ArgTableRow>
<ArgTableRow arg="autonomous" typ="bool">When set, indicates that RouterOS can use this prefix for autonomous address configuration. Otherwise, RouterOS ignores the prefix information.</ArgTableRow>
<ArgTableRow arg="dhcp6-pd-preferred" typ="bool">Indicates that clients should use DHCPv6 Prefix Delegation according to [RFC 9762](https://datatracker.ietf.org/doc/rfc9762/).</ArgTableRow>
<ArgTableRow arg="valid-lifetime" typ="alt { special: enum (infinity) { infinity:0xffffffff }
, value: time
, ticking: time
 }">Length of time after the packet is sent that an address remains valid. The valid lifetime must be greater than or equal to the preferred lifetime. [`Read more >>`](../../../../getting-started/networking-fundamentals/ipv6-neighbor-discovery.md#address-states)</ArgTableRow>
<ArgTableRow arg="preferred-lifetime" typ="alt { special: enum (infinity) { infinity:0xffffffff }
, value: time
, ticking: time
 }">Time after the packet is sent when the generated address becomes deprecated. A deprecated address is used only for existing connections and remains usable until the valid lifetime expires. [`Read more >>`](../../../../getting-started/networking-fundamentals/ipv6-neighbor-discovery.md#address-states)</ArgTableRow>
</ArgTable>
