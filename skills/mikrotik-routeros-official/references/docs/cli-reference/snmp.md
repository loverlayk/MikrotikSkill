# snmp

> RouterOS settings reference for /snmp.

-----------

## snmp 
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="contact" typ="string"></ArgTableRow>
<ArgTableRow arg="location" typ="string"></ArgTableRow>
<ArgTableRow arg="engine-id-suffix" typ="string"></ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip: ipAddr
, ip6: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="trap-target" typ="object { ip-addresses: alt { ipv6: ip6Addr
, ip: ipAddr
 }
 }"></ArgTableRow>
<ArgTableRow arg="trap-community" typ="enum"></ArgTableRow>
<ArgTableRow arg="trap-version" typ="enum (1 | 2 | 3) { 1:0, 2:1, 3:3 }"></ArgTableRow>
<ArgTableRow arg="trap-generators" typ="multi { array-id, generator: enum
 }"></ArgTableRow>
<ArgTableRow arg="trap-interfaces" typ="object { interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="engine-id" typ="string"></ArgTableRow>
</ArgTable>
