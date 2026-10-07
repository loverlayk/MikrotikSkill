# IS-IS

> IS-IS is an Interior Gateway Protocol used for distributing IP routing information within a single Autonomous System, operating as a link-state protocol that exchanges topology data between neighbors. It supports...

# IS-IS

The IS-IS (Intermediate System - Intermediate System) protocol is an Interior Gateway Protocol (IGP) used to distribute IP routing information throughout a single Autonomous System.

It was originally developed as a routing protocol for CLNP but was later extended to include IP routing when IP became popular. An extended version is sometimes referred to as Integrated IS-IS.

IS-IS belongs to the link-state protocol family, which exchanges topology information between nearest neighbors and floods it throughout the AS. The main advantage is that complete knowledge of the network topology allows the router to choose the best path to the destination. It can also serve traffic engineering purposes.

Neighbors periodically exchange **Hello** packets, form adjacencies, and select the Designated IS (DIS) based on the negotiation. Hello packets are sent individually for **Level-1** and **Level-2**.

## Standards and Technologies

- [RFC 1195](https://datatracker.ietf.org/doc/html/rfc1195) Use of OSI IS-IS for Routing in TCP/IP and Dual Environments
- [RFC 5302](https://datatracker.ietf.org/doc/html/rfc5302) Domain-Wide Prefix Distribution with Two-Level IS-IS
- [RFC 5303](https://datatracker.ietf.org/doc/html/rfc5303) Three-Way Handshake for IS-IS Point-to-Point Adjacencies
- [RFC 5305](https://datatracker.ietf.org/doc/html/rfc5305) IS-IS Extensions for Traffic Engineering (only wide metric support)
- [RFC 5308](https://datatracker.ietf.org/doc/html/rfc5308) Routing IPv6 with IS-IS

## IS-IS Terminology

- **IS** - Intermediate System is a router capable of forwarding traffic between distantly located hosts.
- **LSP** - Link State PDU contains information on the router local state (usable interfaces, reachable neighbors, and the cost of the interfaces). See [`/routing/isis/lsp`](../../../cli-reference/routing/isis/lsp.md).
- **SPF** - Shortest-path-first algorithm.
- **DIS** - Designated Intermediate System. DIS ensures that all routers in the network maintain a synchronized database. Separate DISs are elected for L1 and L2 routing. Election of the DIS is based on the highest interface priority.
- **Level-1 (L1) routing** - Controls distribution of routing information within an IS-IS area. L1 routing is based on system ID.
- **Level-2 (L2) routing** - Controls distribution of routing information between IS-IS areas. L2 routing is based on area ID.
- **IS-IS Adjacency** - Link between IS-IS neighbors (see [`/routing/isis/neighbor`](../../../cli-reference/routing/isis/neighbor.md)). The type of adjacency formed depends on the parameters exchanged in the IS-IS Hello packets. Each of the adjacent routers runs the DIS election process to determine whether it is eligible to be an L1 or L2 DIS on the broadcast network.
- **NSAP** - Network Service Access Point address to identify the router.
- **NET** - Network Entity Title. NSAP address with the last byte always set to zero.

## Protocol Basics

The IS-IS protocol is TLV (Type/Length/Value) based, which makes it easy to extend. It uses the OSI addressing principle, and the NSAP address is assigned per node, not per interface.

The NSAP address is split into three parts:

```
+-----+------+-----------+----+
| AFI | Area | System-ID | NS |
+-----+------+-----------+----+
```

- **AFI** - The first leftmost byte defines the meaning of the NSAP address. The IS-IS [`afi`](../../../cli-reference/routing/isis/instance.md#afi) parameter controls which address family the instance handles.
- **Area ID** - 2 octets.
- Most IS-IS implementations use a 6-octet **System-ID**.
- **NS** (N-selector) - One byte and is always set to zero by IS-IS.

The address is written as a hexadecimal string with two-byte portions separated by a dot, with a few exceptions.
For example, the NET address `49222211112222aded00` is written as `49.2222.1111.2222.aded.00`:

- The leftmost dot separates AFI (2 characters).
- Followed by Area ID (4 characters).
- Followed by System ID, which is split into 3 sets of 4 characters.
- The rightmost dot must be between the System ID and the N-selector.

RouterOS splits the NET address into two configuration options. The first 3 bytes (AFI and Area) are configured with the [`areas`](../../../cli-reference/routing/isis/instance.md#areas) parameter, the next 6 bytes are the System ID and are configured with the [`system-id`](../../../cli-reference/routing/isis/instance.md#system-id) parameter, and the last NS byte is not explicitly configured anywhere. It is always assumed to be zero.

Some other vendor implementations can require the AFI byte to be set to a specific value, for example, `0x47` indicating a classic ISO NSAP address.
Also, `0x49` can be used as private address space, similar to IPv4 private address ranges (10.0.0.0/8 etc.).

## Basic Configuration Example

Basic configuration requires creating an instance (under [`/routing/isis/instance`](../../../cli-reference/routing/isis/instance.md)) with the area ID and system ID set, and enabling IS-IS on an interface via [`/routing/isis/interface-template`](../../../cli-reference/routing/isis/interface-template.md).

For example, an IS-IS setup between three routers, one Cisco and two RouterOS.

**R1:**

```ros
/routing/isis/instance
add afi=ip areas=49.2222 disabled=no name=isis-instance-1 system-id=90ab.cdef.0001
/routing/isis/interface-template
add instance=isis-instance-1 interfaces=ether1 levels=l1,l2

[] /routing/isis/neighbor> print 
 0 instance=isis-instance-1 interface=ether1 level-type=l2 snpa=08:00:27:22:B4:A2 srcid="1111.2222.aded" state=up 

 1 instance=isis-instance-1 interface=ether1 level-type=l2 snpa=D4:CA:6D:78:2F:2E srcid="1111.2222.cded" state=up 

 2 instance=isis-instance-1 interface=ether1 level-type=l1 snpa=08:00:27:22:B4:A2 srcid="1111.2222.aded" state=up 

 3 instance=isis-instance-1 interface=ether1 level-type=l1 snpa=D4:CA:6D:78:2F:2E srcid="1111.2222.cded" state=up 

[] /routing/route> print where is-is
Flags: A - ACTIVE; i - IS-IS
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
   DST-ADDRESS        GATEWAY                AFI  DISTANCE  SCOPE  TARGET-SCOPE  IMMEDIATE-GW         
 i 0.0.0.0/0          10.155.101.214%ether1  ip4       115     20            10  10.155.101.214%ether1
 i 10.155.101.0/24    10.155.101.216%ether1  ip4       115     20            10  10.155.101.216%ether1
Ai 10.255.255.162/32  10.155.101.216%ether1  ip4       115     20            10  10.155.101.216%ether1

```

**R2:**

```ros
/routing/isis/instance
add afi=ip areas=49.2222 disabled=no l1.originate-default=always l2.originate-default=always name=isis-instance-1 \
    system-id=1111.2222.cded
/routing/isis/interface-template
add instance=isis-instance-1 interfaces=sfp12 levels=l1,l2
add instance=isis-instance-1 interfaces=lo levels=l2

[] /routing/isis/neighbor> print 
 0 instance=isis-instance-1 interface=sfp12 level-type=l1 snpa=08:00:27:22:B4:A2 srcid="1111.2222.aded" state=up 

 1 instance=isis-instance-1 interface=sfp12 level-type=l1 snpa=C4:AD:34:43:EA:5C srcid="90ab.cdef.0001" state=up 

 2 instance=isis-instance-1 interface=sfp12 level-type=l2 snpa=08:00:27:22:B4:A2 srcid="1111.2222.aded" state=up 

 3 instance=isis-instance-1 interface=sfp12 level-type=l2 snpa=C4:AD:34:43:EA:5C srcid="90ab.cdef.0001" state=up 

```

**R3 Cisco:**

```ros
interface Loopback0
 ip address 10.255.255.162 255.255.255.255
 ip router isis 
!
interface GigabitEthernet1
 ip address dhcp
 ip router isis 
 negotiation auto
!
router isis
 net 49.2222.1111.2222.aded.00
!

# show isis neighbors 

Tag null:
System Id      Type Interface   IP Address      State Holdtime Circuit Id
90AB.CDEF.0001 L1   Gi1         10.155.101.183  UP    27       1111.2222.CDED.01  
90AB.CDEF.0001 L2   Gi1         10.155.101.183  UP    27       1111.2222.CDED.01  
1111.2222.CDED L1   Gi1         10.155.101.214  UP    9        1111.2222.CDED.01  
1111.2222.CDED L2   Gi1         10.155.101.214  UP    9        1111.2222.CDED.01 

# show ip route

i*L1  0.0.0.0/0 [115/11] via 10.155.101.214, 4w5d, GigabitEthernet1
      10.0.0.0/8 is variably subnetted, 5 subnets, 2 masks
C        10.155.101.0/24 is directly connected, GigabitEthernet1
L        10.155.101.216/32 is directly connected, GigabitEthernet1
i L2     10.155.255.214/32 [115/10] via 10.155.101.183, 2w3d, GigabitEthernet1

```

## Troubleshooting

### IS-IS does not work and prints the warning message "invalid 3way tlv"

This warning indicates that the remote neighbor most likely does not comply with the 3-way handshake for point-to-point networks from RFC 5303. For example, on Cisco you must enable "isis three-way-handshake ietf" on the interface to have the 15-byte TLV.
