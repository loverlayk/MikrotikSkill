# bonding

> Bonding is used in High Availability Solutions.

-----------

## interface/bonding 
**Type:** Directory

[Bonding](../../../high-availability-solutions/bonding.md) is used in High Availability Solutions.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled.</ArgTableRow>
<ArgTableRow arg="R" typ="running">running.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the bonding interface.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Maximum Transmit Unit in bytes. Must be smaller or equal to the smallest L2MTU value of a bonding slave.</ArgTableRow>
<ArgTableRow arg="forced-mac-address" typ="macAddr">By default, the bonding interface will use the MAC address of the first selected slave interface. This property allows to configure static MAC address for the bond interface (all zeros, broadcast or multicast addresses will not apply). RouterOS will automatically change the MAC address for slave interfaces and it will be visible in [`/interface/ethernet`](../ethernet/ethernet.md) configuration export</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }">[Address Resolution Protocol](../../../getting-started/networking-fundamentals/index.md#arp-and-tying-it-all-together) mode.</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }">How long the ARP record is kept in the ARP table after no packets are received from IP. Value auto equals the value of arp-timeout in IP/Settings, default is 30s.</ArgTableRow>
<ArgTableRow arg="slaves" typ="multi { array-id, slave: iface_enum
 }">At least two ethernet-like interfaces separated by a comma, which will be used for bonding.</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (balance-rr | active-backup | balance-xor | broadcast | 802.3ad | balance-tlb | balance-alb) { balance-rr:0, active-backup:1, balance-xor:2, broadcast:3, 802.3ad:4, balance-tlb:5, balance-alb:6 }">
Specifies one of the bonding policies.
- `802.3ad` - LACP, IEEE 802.3ad dynamic link aggregation. In this mode, the interfaces are aggregated in a group where each slave shares the same speed. It provides fault tolerance and load balancing. Slave selection for outgoing traffic is done according to the `transmit-hash-policy`.
- `active-backup` - provides link backup, only one slave active at a time.
- `balance-alb` - adaptive load balancing, both outgoing and incoming traffic balanced. The device driver should have support for changing its MAC address.
- `balance-rr` - round-robin load balancing. Slaves in a bonding interface will transmit and receive data in sequential order. It provides load balancing and fault tolerance.
- `balance-tlb` - outgoing traffic distributed according to current load. Incoming traffic is not balanced and is received by the current slave. If receiving slave fails, then another slave takes the MAC address of the failed slave.
- `balance-xor` - static LAG, transmit based on `transmit-hash-policy`. This mode provides load balancing and fault tolerance.
- `broadcast` - broadcasts the same data on all interfaces. This provides fault tolerance but slows down traffic throughput on some slow machines.

MikroTik devices with Marvell Prestera switch and 88E6393X, 88E6191X, 88E6190 switch chips support bridge hardware offloading with bonding interfaces.  
Only `802.3ad` (LACP), `balance-xor` (static LAG) and `active-backup` bonding modes are hardware offloaded, other bonding modes will use the CPU's resources.
</ArgTableRow>
<ArgTableRow arg="primary" typ="iface_enum { none:0 }">Controls the primary interface between active slave ports, works only for `active-backup`, `balance-tlb` and `balance-alb` modes. For `active-backup` mode, it controls which running interface is supposed to send and receive the traffic. For `balance-tlb` mode, it controls which running interface is supposed to receive all the traffic, but for `balance-alb` mode, it controls which interface is supposed to receive the unbalanced traffic (the non-IPv4 traffic). When none of the interfaces are selected as primary, device will automatically select the interface that is configured as the first one.</ArgTableRow>
<ArgTableRow arg="link-monitoring" typ="enum (none | arp | mii) { none:0, arp:1, mii:2 }">
Method to use for monitoring the link. Some bonding modes require specific link monitoring to work properly.
- `arp` - uses ARP to determine whether the remote interface is reachable.
- `mii` - uses Media Independent Interface to determine link status. Link status determination relies on the device driver.
- `none` - no link monitoring.
</ArgTableRow>
<ArgTableRow arg="arp-interval" typ="time">Time in milliseconds defines how often to monitor ARP requests.</ArgTableRow>
<ArgTableRow arg="arp-ip-targets" typ="multi { array-id, arp-target: ipAddr
 }">IP target address which will be monitored if link-monitoring is set to arp. Multiple IP addresses can be specified, separated by a comma.</ArgTableRow>
<ArgTableRow arg="mii-interval" typ="time">How often to monitor the link for failures (used only if link-monitoring is mii).</ArgTableRow>
<ArgTableRow arg="down-delay" typ="time">If a link failure has been detected, the bonding interface is disabled for a down-delay time. Only has effect when link-monitoring is set to mii.</ArgTableRow>
<ArgTableRow arg="up-delay" typ="time">If a link has been brought up, the bonding interface is disabled for up-delay time. Only has effect when link-monitoring is set to mii.</ArgTableRow>
<ArgTableRow arg="lacp-rate" typ="enum (30secs | 1sec) { 30secs:0, 1sec:1 }">LACP rate specifies how often to exchange LACPDUs between bonding peers. `1sec` - short timeout. `30secs` - long timeout.</ArgTableRow>
<ArgTableRow arg="transmit-hash-policy" typ="enum (layer-2 | layer-3-and-4 | layer-2-and-3 | encap-2-and-3 | encap-3-and-4) { layer-2:0, layer-3-and-4:1, layer-2-and-3:2, encap-2-and-3:3, encap-3-and-4:4 }">
Selects the transmit hash policy for slave selection in balance-xor and 802.3ad modes.
- `layer-2` - Uses XOR of hardware MAC addresses to generate the hash. This algorithm will place all traffic to a particular network peer on the same slave. This algorithm is 802.3ad compliant.
- `layer-2-and-3` - This policy uses a combination of layer2 and layer3 protocol information to generate the hash. Uses XOR of hardware MAC addresses and IP addresses to generate the hash. This algorithm will place all traffic to a particular network peer on the same slave. For non-IP traffic, the formula is the same as for the layer2 transmit hash policy. This policy is intended to provide a more balanced distribution of traffic than layer2 alone, especially in environments where a layer3 gateway device is required to reach most destinations. This algorithm is 802.3ad compliant.
- `layer-3-and-4` - This policy uses upper layer protocol information, when available, to generate the hash. This allows for traffic to a particular network peer to span multiple slaves, although a single connection will not span multiple slaves. For fragmented TCP or UDP packets and all other IP protocol traffic, the source and destination port information is omitted. For non-IP traffic, the formula is the same as for the layer2 transmit hash policy. This algorithm is not fully 802.3ad compliant.
- `encap-2-and-3` - This policy works like the layer-2-and-3 method for distributing traffic, but uses a process to also analyze the encapsulated packet headers. If an encapsulation protocol (like tunneling) is used, it may select the inner headers instead of the outer ones. RouterOS can use this feature when tunnels like 6to4, GRE, GRE6, IPIP, IPIP6, PPPoE, or PPTP are run over a bonding interface.
- `encap-3-and-4` - This policy works like the layer-3-and-4 method for distributing traffic, but uses a process to also analyze the encapsulated packet headers. If an encapsulation protocol (like tunneling) is used, it may select the inner headers instead of the outer ones. RouterOS can use this feature when tunnels like 6to4, GRE, GRE6, IPIP, IPIP6, PPPoE, or PPTP are run over a bonding interface.
</ArgTableRow>
<ArgTableRow arg="min-links" typ="num">How many active slave links needed for bonding to become active.</ArgTableRow>
<ArgTableRow arg="mlag-id" typ="num">Changes [MLAG](../../../high-availability-solutions/multi-chassis-link-aggregation-group.md) ID for bonding interface. The same MLAG ID should be used on both peer devices to successfully create a single MLAG.  The [`mlag-peer-port`](../bridge/bridge.md#mlag-peer-port) should not be configured with the MLAG ID.</ArgTableRow>
<ArgTableRow arg="lacp-user-key" typ="num">Specifies the upper 10 bits of the port key. The lower 6 bits are automatically assigned based on individual port link speed and duplex.</ArgTableRow>
<ArgTableRow arg="lacp-mode" typ="enum (passive | active) { passive:0, active:1 }">
Specifies whether ports actively or passively participates in the LACP.
- `active` - ports actively initiate LACP communication.
- `passive` - ports only respond to LACP messages.
</ArgTableRow>
<ArgTableRow arg="lacp-system-id" typ="macAddr">Specifies the LACP system ID used for LACP negotiations.</ArgTableRow>
<ArgTableRow arg="lacp-system-priority" typ="num">Specifies the LACP system priority used for LACP negotiations.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the bonding interface.</ArgTableRow>
</ArgTable>
