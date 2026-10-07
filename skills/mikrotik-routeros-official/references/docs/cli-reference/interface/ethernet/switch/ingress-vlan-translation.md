# ingress-vlan-translation

> The Ingress VLAN Translation table allows for up to 15 entries for each port. One or multiple fields can be selected from the packet header for lookup in the Ingress VLAN Translation table. The S-VLAN or C-VLAN or...

-----------

## interface/ethernet/switch/ingress-vlan-translation 
**Syscap:** musicswitch
**Type:** Directory

The Ingress VLAN Translation table allows for up to 15 entries for each port. One or multiple fields can be selected from the packet header for lookup in the Ingress VLAN Translation table. The S-VLAN or C-VLAN or both configured in the first matched entry are assigned to the packet.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="protocol" typ="alt { protocol-name: enum (length | llc-bpdu) { length:1, llc-bpdu:0x4242 }
, protocol-number: num [ .. 65535]
 }">Matching Ethernet protocol. (only for Ingress VLAN Translation)</ArgTableRow>
<ArgTableRow arg="sa-learning" typ="bool">Enables or disables source MAC learning after VLAN translation. (only for Ingress VLAN Translation)</ArgTableRow>
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
 }">The new customer VLAN ID replaces the matching customer VLAN ID. If set to 4095 and ingress VLAN translation is used, then traffic is dropped.</ArgTableRow>
<ArgTableRow arg="pcp-propagation" typ="bool">
Enables or disables PCP propagation.
- If the port type is Edge, the customer PCP is copied from the service PCP.
- If the port type is Network, the service PCP is copied from the customer PCP.
</ArgTableRow>
<ArgTableRow arg="swap-vids" typ="enum (no | assign-cvid-to-svid) { no:0, assign-cvid-to-svid:0 }"></ArgTableRow>
</ArgTable>
Below is a table of traffic that triggers a rule that has a certain VLAN format set; note that traffic that is tagged with VLAN ID 0 is a special case that is also taken into account.

| Property | Description |
| :-- | :-- |
| **any** | Accepts:Untagged trafficTagged trafficTagged traffic with priority setVLAN 0 trafficVLAN 0 traffic with priority set |
| **priority-tagged-or-tagged** | Accepts:Tagged trafficTagged traffic with priority setVLAN 0 trafficVLAN 0 traffic with priority set |
| **tagged** | Accepts:Tagged trafficTagged traffic with priority set |
| **untagged-or-tagged** | Accepts:Untagged trafficTagged trafficTagged traffic with priority set |

:::danger
If `VLAN-format` is set to `any`, then `customer-vid``/``service-vid` set to `0` will trigger the switch rule with VLAN 0 traffic. In this case, the switch rule will be looking for untagged traffic or traffic with a VLAN 0 tag, and only `untagged-or-tagged` will filter out VLAN 0 traffic.
:::
