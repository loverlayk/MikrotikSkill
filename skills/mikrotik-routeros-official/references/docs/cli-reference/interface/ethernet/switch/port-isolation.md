# port-isolation

> The CRS switches support flexible multi-level isolation features, which can be used for user access control, traffic engineering and advanced security and network management. The isolation features provide an...

-----------

## interface/ethernet/switch/port-isolation 
**Syscap:** musicswitch
**Type:** Directory

The CRS switches support flexible multi-level isolation features, which can be used for user access control, traffic engineering and advanced security and network management. The isolation features provide an organized fabric structure allowing the user to easily program and control the access by port, MAC address, VLAN, protocol, flow, and frame type. The following isolation and leakage features are supported:

- Port-level isolation
- MAC-level isolation
- VLAN-level isolation
- Protocol-level isolation
- Flow-level isolation
- Free combination of the above

Port-level isolation supports different control schemes on the source port and destination port. Each entry can be programmed with access control for either the source port or the destination port.

- When the entry is programmed with source port access control, the entry is.

applied to the ingress packets.

- When the entry is programmed with destination port access control, the entry

is applied to the egress packets.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ports" typ="multi { array-id }">Isolated/leaked ports.</ArgTableRow>
<ArgTableRow arg="type" typ="enum (src | dst) { src:0, dst:1 }">
Lookup type of the isolation/leakage entry:
- src - Entry applies to ingress packets of the ports.
- dst - Entry applies to egress packets of the ports.
</ArgTableRow>
<ArgTableRow arg="forwarding-type" typ="ubit (bridged, routed)">Matching traffic forwarding type on Cloud Router Switch.</ArgTableRow>
<ArgTableRow arg="traffic-type" typ="ubit (unicast, multicast, broadcast)">Matching traffic type.</ArgTableRow>
<ArgTableRow arg="registration-status" typ="ubit (known, unknown)">Registration status for matching packets. Known ones are present in UFDB and MFDB, and unknown ones are not.</ArgTableRow>
<ArgTableRow arg="protocol-type" typ="ubit (arp, nd, dhcpv4, dhcpv6, ripv1)">Included protocols for isolation/leakage.</ArgTableRow>
<ArgTableRow arg="flow-id" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-profile" typ="enum (promiscuous | isolated | community1 | community2) { promiscuous:0, isolated:1, community1:2, community2:3 }">Matching MAC isolation/leakage profile.</ArgTableRow>
<ArgTableRow arg="port-profile" typ="num">Matching Port isolation/leakage profile.</ArgTableRow>
<ArgTableRow arg="vlan-profile" typ="enum (promiscuous | isolated | community1 | community2) { promiscuous:0, isolated:1, community1:2, community2:3 }">Matching VLAN isolation/leakage profile.</ArgTableRow>
</ArgTable>

## interface/ethernet/switch/port-isolation 
**Syscap:** rbswitch
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="forwarding-override" typ="multi { array-id, port: alt { port: enum
, interface-list: enum
 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="switch" typ="enum"></ArgTableRow>
<ArgTableRow arg="current-forwarding-override" typ="multi { array-id, port: enum
 }"></ArgTableRow>
</ArgTable>
