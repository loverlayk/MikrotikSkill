# cap

> RouterOS settings reference for /interface/wireless/cap.

-----------

## interface/wireless/cap 
**Package:** wireless-rep
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (request | none) { request:0 }"></ArgTableRow>
<ArgTableRow arg="lock-to-caps-man" typ="bool"></ArgTableRow>
<ArgTableRow arg="discovery-interfaces" typ="multi { array-id, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="caps-man-addresses" typ="multi { array-id, address: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="caps-man-names" typ="multi { array-id, name: string
 }"></ArgTableRow>
<ArgTableRow arg="caps-man-certificate-common-names" typ="multi { array-id, common-name: string
 }"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum { none:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="static-virtual" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="requested-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="locked-caps-man-common-name" typ="string"></ArgTableRow>
</ArgTable>
