# provisioning

> RouterOS directory reference for /interface/wifi/provisioning.

-----------

## interface/wifi/provisioning 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="radio-mac" typ="macAddr" unset="1"></ArgTableRow>
<ArgTableRow arg="identity-regexp" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="common-name-regexp" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="address-ranges" typ="object { address-range: super { address-range-start: address (flags=46)
, [address-range-end] -address (flags=46)
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="supported-bands" typ="multi { array-id, supported-band: enum ()
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="supported-hw-caps" typ="multi { array-id, supported-hw-cap: enum ()
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (none | create-enabled | create-disabled | create-dynamic-enabled | use-network-config)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="master-configuration" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="slave-configurations" typ="multi { array-id, slave-configuration: enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="multi-link-mode" typ="enum (auto | disabled | master | all)" unset="1"></ArgTableRow>
<ArgTableRow arg="name-format" typ="string"></ArgTableRow>
<ArgTableRow arg="slave-name-format" typ="string"></ArgTableRow>
</ArgTable>
