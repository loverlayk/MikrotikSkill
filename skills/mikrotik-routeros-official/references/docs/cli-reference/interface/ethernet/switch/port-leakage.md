# port-leakage

> Port leakage allows bypassing egress VLAN filtering on the port. A leaky port is allowed to access other ports for various applications such as security, network control, and management. Note: When both isolation and...

-----------

## interface/ethernet/switch/port-leakage 
**Syscap:** musicswitch
**Type:** Directory

Port leakage allows bypassing egress VLAN filtering on the port. A leaky port is allowed to access other ports for various applications such as security, network control, and management. Note: When both isolation and leakage are applied to the same port, the port is isolated.

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
