# egress-vlan-translation

> RouterOS directory reference for /interface/ethernet/switch/egress-vlan-translation.

-----------

## interface/ethernet/switch/egress-vlan-translation 
**Syscap:** musicswitch
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ports" typ="multi { array-id }" mandatory="1">Matching switch ports for VLAN translation rule.</ArgTableRow>
<ArgTableRow arg="service-vlan-format" typ="enum (untagged-or-tagged | priority-tagged-or-tagged | tagged | any) { untagged-or-tagged:0, priority-tagged-or-tagged:1, tagged:2, any:3 }">Type of frames with service tag for which VLAN translation rule is valid.</ArgTableRow>
<ArgTableRow arg="service-vid" typ="num">Matching VLAN ID of the service tag.</ArgTableRow>
<ArgTableRow arg="service-pcp" typ="num">Matching PCP of the service tag.</ArgTableRow>
<ArgTableRow arg="service-dei" typ="num">Matching DEI of the service tag.</ArgTableRow>
<ArgTableRow arg="customer-vlan-format" typ="enum (untagged-or-tagged | priority-tagged-or-tagged | tagged | any) { untagged-or-tagged:0, priority-tagged-or-tagged:1, tagged:2, any:3 }">Type of frames with customer tag for which VLAN translation rule is valid.</ArgTableRow>
<ArgTableRow arg="customer-vid" typ="num">Matching the VLAN ID of the customer tag.</ArgTableRow>
<ArgTableRow arg="customer-pcp" typ="num">Matching PCP of the customer tag.</ArgTableRow>
<ArgTableRow arg="customer-dei" typ="num">Matching DEI of the customer tag.</ArgTableRow>
<ArgTableRow arg="new-service-vid" typ="alt { special-vid: enum (customer-vid) { customer-vid:4096 }
, vid: num [ .. 4095]
 }">The new service VLAN ID replaces the matching service VLAN ID.</ArgTableRow>
<ArgTableRow arg="new-customer-vid" typ="alt { special-vid: enum (service-vid) { service-vid:4096 }
, vid: num [ .. 4095]
 }">The new customer VLAN ID replaces the matching customer VLAN ID.</ArgTableRow>
<ArgTableRow arg="pcp-propagation" typ="bool">
Enables or disables PCP propagation.
- If the port type is Edge, the customer PCP is copied from the service PCP.
- If the port type is Network, the service PCP is copied from the customer PCP.
</ArgTableRow>
<ArgTableRow arg="swap-vids" typ="enum (no | assign-cvid-to-svid) { no:0, assign-cvid-to-svid:0 }"></ArgTableRow>
</ArgTable>
