# esi

> RouterOS directory reference for /routing/bgp/evpn/esi.

-----------

## routing/bgp/evpn/esi 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="esi" typ="object { esi-value: super { byte0: string
, [byte1] :string
, [byte2] :string
, [byte3] :string
, [byte4] :string
, [byte5] :string
, [byte6] :string
, [byte7] :string
, [byte8] :string
, [byte9] :string
 }
 }"></ArgTableRow>
<ArgTableRow arg="bond" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="peers" typ="multi { peer: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="bds" typ="multi { array-id, array-id, array-id, bd: super { [vlan] vlan-num
, [vxlan] /iface_enum
, [role] /enum (non-df | df)
 }
 }"></ArgTableRow>
</ArgTable>
