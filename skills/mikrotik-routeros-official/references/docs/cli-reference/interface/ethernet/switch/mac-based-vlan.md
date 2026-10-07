# mac-based-vlan

> MAC Based VLAN table is used to assign a VLAN based on the source MAC.

-----------

## interface/ethernet/switch/mac-based-vlan 
**Syscap:** musicswitch
**Type:** Directory

MAC Based VLAN table is used to assign a VLAN based on the source MAC.

All CRS1xx/2xx series switches support up to 1024 MAC Based VLAN table entries.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="src-mac-address" typ="macAddr" mandatory="1">Matching source MAC address for MAC based VLAN rule.</ArgTableRow>
<ArgTableRow arg="new-service-vid" typ="num">The new service VLAN ID replaces the original service VLAN ID for matched packets.</ArgTableRow>
<ArgTableRow arg="new-customer-vid" typ="num">The new customer VLAN ID replaces the original service VLAN ID for matched packets. If set to 4095, then traffic is dropped.</ArgTableRow>
</ArgTable>
