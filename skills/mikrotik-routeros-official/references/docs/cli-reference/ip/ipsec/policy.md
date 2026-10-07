# policy

> All packets are IPIP encapsulated in tunnel mode, and their new IP header's src-address and dst-address are set to sa-src-address and sa-dst-address values of this policy. If you do not use tunnel mode (i.e., you use...

-----------

## ip/ipsec/policy 
**Type:** Directory

:::info
Policy order is important. It works similarly to firewall filters where policies are executed from top to bottom (priority parameter is removed).

All packets are IPIP encapsulated in tunnel mode, and their new IP header's src-address and dst-address are set to sa-src-address and sa-dst-address values of this policy. If you do not use tunnel mode (i.e., you use transport mode), then only packets whose source and destination addresses are the same as sa-src-address and sa-dst-address can be processed by this policy. Transport mode can only work with packets that originate at and are destined for IPsec peers (hosts that established security associations). To encrypt traffic between networks (or a network and a host) you have to use tunnel mode.
:::

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="T" typ="template">Whether the item is a template to assign for dynamic peers.</ArgTableRow>
<ArgTableRow arg="B" typ="backup">Whether the item is included in the backup.</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">Whether the item is disabled.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">Whether the item was created dynamically.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">Whether this policy is invalid - the possible cause is a duplicate policy with the same src-address and dst-address.</ArgTableRow>
<ArgTableRow arg="A" typ="active">Whether the item is currently active.</ArgTableRow>
<ArgTableRow arg="*" typ="default">Whether the item is the default.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="peer" typ="multi { array-id, peer: enum
 }">Name of the peer on which the policy applies.c</ArgTableRow>
<ArgTableRow arg="tunnel" typ="bool">Whether to use tunnel mode.</ArgTableRow>
<ArgTableRow arg="group" typ="enum">Policy group name.</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { prefix6: ip6Prefix
, prefix4: ipPrefix
 }">Source address or network to be matched in packets. Applicable when tunnel mode (`tunnel=yes`) or template (`template=yes`) is used.</ArgTableRow>
<ArgTableRow arg="src-port" typ="num">Source port.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="alt { prefix6: ip6Prefix
, prefix4: ipPrefix
 }">Destination address or network to be matched in packets. Applicable when tunnel mode (`tunnel=yes`) or template (`template=yes`) is used.</ArgTableRow>
<ArgTableRow arg="dst-port" typ="num">Destination port.</ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (all) { all:255 }">IP protocol number or name.</ArgTableRow>
<ArgTableRow arg="action" typ="enum (encrypt | discard | none) { encrypt:2, discard:0, none:1 }">
Action to take for matching traffic.
- `none` - pass the packet unchanged.
- `discard` - drop the packet.
- `encrypt` - apply transformations specified in this policy and its SA.
</ArgTableRow>
<ArgTableRow arg="level" typ="enum (require | use | unique) { require:2, use:1, unique:3 }">
Specifies what to do if some of the SAs for this policy cannot be found:
- `use` - skip this transform, do not drop the packet, and do not acquire SA from IKE daemon;
- `require` - drop the packet and acquire SA;
- `unique` - drop the packet and acquire a unique SA that is only used with this particular policy. It is used in setups where multiple clients can sit behind one public IP address (clients behind NAT).
</ArgTableRow>
<ArgTableRow arg="ipsec-protocols" typ="enum (ah | esp) { ah:1, esp:2 }">Specifies what combination of Authentication Header and Encapsulating Security Payload protocols you want to apply to matched traffic.</ArgTableRow>
<ArgTableRow arg="sa-src-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">endpoint address</ArgTableRow>
<ArgTableRow arg="sa-dst-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">endpoint address</ArgTableRow>
<ArgTableRow arg="proposal" typ="enum">Proposal template name.</ArgTableRow>
<ArgTableRow arg="template" typ="bool">Whether this policy is a template.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="active-interface" typ="iface_enum">The interface through which the SA is established.</ArgTableRow>
<ArgTableRow arg="ph2-count" typ="num">Number of phase 2 exchanges.</ArgTableRow>
<ArgTableRow arg="ph2-state" typ="enum (spawning | starting | ready-to-send | getspi-sent | getspi-done | msg1-sent | ready-to-establish | commiting | adding-sa | established | expired | no-phase2) { spawning:0, starting:1, ready-to-send:2, getspi-sent:3, getspi-done:4, msg1-sent:5, ready-to-establish:6, commiting:7, adding-sa:8, established:9, expired:10, no-phase2:11 }">Current phase 2 state.</ArgTableRow>
</ArgTable>
