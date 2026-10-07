# provisioning

> RouterOS directory reference for /caps-man/provisioning.

-----------

## caps-man/provisioning 
**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="radio-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="hw-supported-modes" typ="multi { array-id, hw-supported-mode: enum (a | a-turbo | an | ac | b | g | g-turbo | gn) { a:1, a-turbo:2, an:3, ac:5, b:0x11, g:0x12, g-turbo:0x13, gn:0x14 }
 }"></ArgTableRow>
<ArgTableRow arg="identity-regexp" typ="string"></ArgTableRow>
<ArgTableRow arg="common-name-regexp" typ="string"></ArgTableRow>
<ArgTableRow arg="ip-address-ranges" typ="multi { ip-address-range: ipRange
 }"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (none | create-enabled | create-disabled | create-dynamic-enabled)"></ArgTableRow>
<ArgTableRow arg="master-configuration" typ="enum"></ArgTableRow>
<ArgTableRow arg="slave-configurations" typ="multi { array-id, slave-configuration: enum
 }"></ArgTableRow>
<ArgTableRow arg="name-format" typ="enum (cap | prefix | identity | prefix-identity)"></ArgTableRow>
<ArgTableRow arg="name-prefix" typ="string"></ArgTableRow>
</ArgTable>
