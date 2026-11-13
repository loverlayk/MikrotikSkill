# Packet Flow in RouterOS

> The order in which RouterOS facilities process a packet: bridging, routing, MPLS, the firewall chains, NAT, queues, IPsec, VRF, FastPath and FastTrack, with the packet flow diagrams.

# Packet Flow in RouterOS

A packet passes through several RouterOS facilities on its way through the router: bridging, routing, MPLS, the firewall, queues and others. This page shows the order in which these facilities process a packet. Use it when a configuration combines several facilities, for example packet marks with queues, or NAT with policy routing.

The packet flow diagram has these parts:

- The overall diagram.
- The detailed diagram of bridging, routing and MPLS.
- The facilities in each chain: prerouting, input, forward, output and postrouting.
- The chains that VRF traffic passes.
- The hardware offload and FastPath choices.

## Overall packet flow

![Overall packet flow diagram: physical and logical interfaces, the bridging, MPLS and routing areas, and the local processes of the router](./img/packet-flow-in-routeros-overall.svg#gh-light-mode-only)![Overall packet flow diagram: physical and logical interfaces, the bridging, MPLS and routing areas, and the local processes of the router](./img/packet-flow-in-routeros-overall_dark.svg#gh-dark-mode-only)

The middle of the diagram has four areas: bridging, MPLS, routing, and the processes of the router itself. Each of the first three areas has an input, a forward and an output path. The letters mark the points where a packet enters and leaves an area. The detailed diagram uses the same letters.

The boxes outside the areas:

- **Physical in-interface** - the point where the router receives a packet.
- **Logical in-interface** - the point where a packet enters again after decapsulation, for example a packet that arrived in a tunnel.
- **Local in** - the last point of a packet that is for the router itself.
- **Local out** - the first point of a packet that the router itself sends.
- **Logical out-interface** - the last point of a packet before encapsulation, for example into a tunnel.
- **Interface HTB (Hierarchical Token Bucket)** - the interface queue.
- **Physical out-interface** - the last point of a packet before the router sends it.
- **Switch chip** - a packet that the switch chip forwards in hardware does not reach the CPU and does not pass any other box of the diagram.

A packet that the router routes takes this path:

1. The router receives the packet on the physical in-interface.
2. The in-interface is not a bridge port and the packet has no MPLS label. It is an IP packet, so it enters the routing area at **I**.
3. The packet takes the forward path of the routing area and leaves it at **L**.
4. The packet needs no MPLS label, the out-interface is not a bridge port, and no encapsulation is needed. The packet passes the interface queue and leaves through the physical out-interface.

A packet for the router itself, for example a ping, takes this path:

1. The packet enters the routing area at **I** and takes the input path to **J**.
2. The packet needs no decapsulation, so it goes to local in, and the router processes it.
3. The reply starts at local out. It is an IP packet, so it enters the routing area at **K**.
4. The reply takes the output path, leaves the routing area at **L**, and goes to the physical out-interface.

## Bridging, routing and MPLS

![Detailed diagram of the bridging, routing and MPLS areas with the firewall chains, the bridge chains, the IPsec steps and the MPLS label operations](./img/packet-flow-in-routeros-bridging-routing-mpls.svg#gh-light-mode-only)![Detailed diagram of the bridging, routing and MPLS areas with the firewall chains, the bridge chains, the IPsec steps and the MPLS label operations](./img/packet-flow-in-routeros-bridging-routing-mpls_dark.svg#gh-dark-mode-only)

The grey boxes with double side lines are the chains of the IP firewall. The other boxes:

- **Routing decision** - the router looks for a route to the destination address of the packet. If no route matches, the router discards the packet.
- **MPLS decision** - the router decides what to do with the packet from the MPLS forwarding table.
- **Bridging decision** - the bridge looks for the destination MAC address of the packet in the host table. If it finds the address, it sends the packet to that port. If not, it floods the packet: it sends one copy out of every other bridge port. One copy also reaches the bridge input chain, because the bridge interface itself is one of the destinations. When `vlan-filtering=yes` is set, the bridge drops the packets that the `/interface/bridge/vlan` table does not allow at this stage.
- **Use-ip-firewall** - whether `use-ip-firewall` is enabled in the bridge settings.
- **IPsec policy** - whether the packet matches an IPsec policy.

### Chains

The firewall processes a packet in these chains:

- **Prerouting** - packets that arrive on an interface, before the routing decision. The *raw*, *mangle* and *nat* tables have rules here. The *nat* rules of this point are in `chain=dstnat`.
- **Input** - packets for the router itself. The *mangle*, *filter* and *nat* tables have this chain.
- **Forward** - packets that the router routes. The *mangle* and *filter* tables have this chain.
- **Output** - packets that the router itself sends. The *raw*, *mangle*, *nat* and *filter* tables have this chain.
- **Postrouting** - packets that leave the router, after the routing decision. The *mangle* and *nat* tables have rules here. The *nat* rules of this point are in `chain=srcnat`.

Each chain contains several facilities. The diagram shows their order:

![Diagram of the facilities in the prerouting, routing decision, input, forward, output and postrouting stages, in processing order](./img/packet-flow-in-routeros-chains.svg#gh-light-mode-only)![Diagram of the facilities in the prerouting, routing decision, input, forward, output and postrouting stages, in processing order](./img/packet-flow-in-routeros-chains_dark.svg#gh-dark-mode-only)

- **Hotspot-in** - lets the Hotspot capture traffic that connection tracking would otherwise discard. This way the Hotspot can serve clients whose network settings are wrong.
- **RAW prerouting**, **RAW output** - the [RAW](./firewall/raw) table chains.
- **Connection tracking** - connection tracking processes the packet.
- **Mangle prerouting**, **Mangle input**, **Mangle forward**, **Mangle output**, **Mangle postrouting** - the mangle chains.
- **Dst-NAT** - the `dstnat` chain of the NAT table.
- **Dst-NAT (NAT output)** - the `output` chain of the NAT table. Rules of the `dstnat` chain do not process the packets that the router itself sends; rules of the `output` chain do.
- **Filter input**, **Filter forward**, **Filter output** - the filter chains.
- **Src-NAT** - the `srcnat` chain of the NAT table.
- **Src-NAT (NAT input)** - the `input` chain of the NAT table.
- **Traffic Flow** - the packet is counted for [Traffic Flow](../diagnostics-monitoring-and-troubleshooting/traffic-flow). A packet that the firewall drops in the RAW or filter rules before this point is not counted.
- **HTB global** - the queue tree with `parent=global`.
- **Simple queues** - the simple queues.
- **TTL** - the place where the Time To Live (TTL) of a routed packet is reduced by 1. If the TTL becomes 0, the router discards the packet. The TTL of a bridged packet is not reduced.
- **Routing adjustment** - a new route lookup for a packet that the router itself sends, after a mangle rule of the output chain set a routing mark or a NAT rule of the output chain changed the destination address. The rules of the output chain see the out-interface of the first lookup. The postrouting rules see the new out-interface.
- **Hotspot-out** - undoes the changes of hotspot-in for the packets that go back to the client.

The routing decision goes through the policy rules in the order that `policy-rules` in `/routing/settings` sets. The diagram shows the default order: the routing mark set by mangle rules, the VRF lookup, the VRF unreachable rule, the local table, the routing rules of `/routing/rule`, and the main table.

## Flow of a routed packet

### Forward

A packet that the router routes from one interface to another passes these steps:

1. Prerouting:
   1. Hotspot-in.
   2. RAW prerouting chain.
   3. Connection tracking.
   4. Mangle prerouting chain.
   5. NAT `dstnat` chain.
2. Routing decision.
3. Forward:
   1. The TTL is reduced by 1.
   2. Mangle forward chain.
   3. Filter forward chain.
   4. Traffic Flow.
4. Postrouting:
   1. Mangle postrouting chain.
   2. NAT `srcnat` chain.
   3. Hotspot-out.
   4. Queue tree (HTB global).
   5. Simple queues.
5. The router matches the packet against the IPsec policies.

### Input

A packet for the router itself passes these steps:

1. Prerouting, with the same steps as for a forwarded packet.
2. Routing decision.
3. Input:
   1. Mangle input chain.
   2. Filter input chain.
   3. Traffic Flow.
   4. NAT `input` chain.
   5. Queue tree (HTB global).
   6. Simple queues.
4. The router matches the packet against the IPsec policies.

### Output

A packet that the router itself sends passes these steps:

1. Routing decision.
2. Output:
   1. Bridge decision.
   2. RAW output chain.
   3. Connection tracking.
   4. Mangle output chain.
   5. NAT `output` chain.
   6. Filter output chain.
   7. Traffic Flow.
   8. Routing adjustment.
3. Postrouting, with the same steps as for a forwarded packet.
4. The router matches the packet against the IPsec policies.

## Flow of a bridged packet

This section describes the general bridging process. Some configurations, for example VLAN filtering, horizon, STP, DHCP snooping or IGMP snooping, process some packets differently. See the [bridging manual](../bridging-and-switching/) for details.

The steps refer to the bridging part of the detailed diagram.

### Bridge forward

The bridge forwards a packet from one bridge port to another:

1. The packet enters the bridging area at **A** and passes the bridge NAT `dstnat` chain. Rules of this chain can change the destination MAC address and the priority, and can accept, drop or mark the packet.
2. The bridging decision. A flooded packet (broadcast, multicast or unknown unicast) is copied for every bridge port, and each copy continues in the bridge forward chain.
3. The bridge filter `forward` chain. Rules of this chain can change the priority, and can accept, drop or mark the packet.
4. The bridge NAT `srcnat` chain. Rules of this chain can change the source MAC address and the priority, and can accept, drop or mark the packet.
5. The packet leaves the bridging area at **D**.

:::info
When bridge `vlan-filtering` is enabled, the bridge can add a VLAN header to a received untagged packet at the bridging decision. From that point, the `mac-protocol=vlan` and `vlan-encap` matchers match the packet. This happens if the outgoing port has `frame-types` set to `admit-all` or `admit-only-untagged-and-priority-tagged`.

The bridge can remove the VLAN header of a tagged packet at the bridging decision. From that point, the `mac-protocol=vlan` and `vlan-encap` matchers do not match the packet. This happens if the VLAN ID of the packet matches the untagged VLAN membership of the outgoing port.
:::

### Bridge input

A packet goes to the bridge interface itself, for example to a DHCP server on the bridge, or to be routed:

1. The packet enters at **A** and passes the bridge NAT `dstnat` chain.
2. The bridging decision. A packet whose destination MAC address is the MAC address of the bridge goes to the bridge input chain. A flooded packet also reaches the bridge input chain.
3. The bridge filter `input` chain.
4. The packet leaves the bridging area at **B**.

### Bridge output

A packet from the router leaves through one or more bridge ports, for example a reply of a DHCP server on the bridge:

1. The packet enters the bridging area at **C**.
2. The bridging decision. A flooded packet is copied for every bridge port.
3. The bridge filter `output` chain.
4. The bridge NAT `srcnat` chain.
5. The packet leaves the bridging area at **D**.

### Forward with the IP firewall enabled

With `use-ip-firewall` enabled in the bridge settings, bridged packets also pass the IP firewall chains. This makes it possible to use the IP firewall and simple queues on bridged traffic. The extra processing uses more CPU.

A bridged packet passes these steps:

1. Bridge NAT `dstnat` chain.
2. Prerouting.
3. Bridging decision.
4. Bridge filter `forward` chain.
5. Forward.
6. Bridge NAT `srcnat` chain.
7. Postrouting.

Two more cases apply with `use-ip-firewall` enabled:

- A packet that arrives on a bridge port and is for the router, or is routed, passes prerouting one time, in the bridging area. The routing area does not process prerouting again.
- A packet that the router sends or routes out through a bridge passes postrouting one time, in the routing area. In the bridging area, it passes the bridge output chain and the bridge NAT `srcnat` chain.

## Flow of Hardware Offloaded Packet

On the previous topic, we solely discussed software bridging that requires the main CPU processing to forward packets through the correct bridge port. Most of the MikroTik devices are equipped with dedicated switching hardware, the so-called switch chip or switch ASIC. This allows us to offload some of the bridging functions, like packet forwarding between bridge ports or packet filtering, to this specialized hardware chip without consuming any CPU resources. In RouterOS, we have named this function Bridge Hardware (HW) Offloading. Different MikroTik devices might have different switch chips and each chip has a different set of features available, so make sure to visit this article to get more details - [Bridge Hardware Offloading](../bridging-and-switching/index.md#bridge-hardware-offloading).

![](./img/packet-flow-in-routeros-18.webp)

:::warning
Interface HTB will not work correctly when the out-interface is hardware offloaded and the bridge Fast Path is not active.
:::

![](./img/packet-flow-in-routeros-19.webp)

- **Switching decision** - widely depends on the switch model. This block controls all the switching-related tasks, like host learning, packet forwarding, filtering, VLAN tagging/untagging, etc. Certain switch configurations can alter the packet flow.
- **switch-cpu port** - a special purpose switch port for communication between the main CPU and other switch ports. Note that the switch-cpu port does not show up anywhere on RouterOS except for the switch menu. None of the software-related configurations (e.g. interface-list) can be applied to this port. Packets that reach the CPU are automatically associated with the physical in-interface.

The hardware offloading, however, does not restrict a device to only hardware limited features; rather, it is possible to take advantage of the hardware and software processing at the same time. This does require a profound understanding of how packets travel through the switch chip and when exactly they are passed to the main CPU.

:::info
Switch features found in the `/interface/ethernet/switch` menu and its sub-menus, like ACL rules, mirroring, ingress/egress rate limiters, QoS, and L3HW (except inter-VLAN routing) may not rely on bridge hardware offloading. Therefore, they can **potentially** be applied to interfaces not configured within a hardware-offloaded bridge.
:::

### Switch Forward

We will further discuss a packet flow when bridge hardware offloading is enabled and a packet is forwarded between two switched ports on a single switch chip. This is the most common and also the simplest example:

1. The switch checks whether the in-interface is a hardware offloaded interface.
2. The switch runs a packet through the switch host table to make a forwarding decision. If the switch finds a match for the destination MAC address, the packet is sent out through the physical interface. A packet that ends up being flooded (e.g. broadcast, multicast, unknown unicast traffic) gets multiplied and sent out to every hardware offloaded switch port.

![](./img/packet-flow-in-routeros-20.webp)

### Switch to CPU Input

This process takes place when a packet is received on a physical interface and it is destined for the switch-cpu port for further software processing. There are two paths to the switch-cpu. One is where hardware offloading and switching are not even used (e.g. a standalone interface for routing or a bridged interface but with deliberately disabled HW offloading), so the packet is simply passed further for software processing. Another path is taken when hardware offloading is active on the in-interface. This will cause the packet to pass through the switching decision and there are various reasons why the switch might forward the packet to the switch-cpu port:

- A packet's destination MAC address matches a local MAC address, e.g. when a packet is destined to a local bridge interface.
- A packet might get flooded to all switch ports including the switch-cpu port, e.g. when broadcast, multicast, or unknown unicast traffic is received.
- A switch might have learned that some hosts can only be reached through the CPU (switch-cpu port learning is discussed in the next section), e.g. when a bridge contains HW and non-HW offloaded interfaces, such as wireless, EoIP, and even Ethernet interfaces.
- A packet is intentionally copied to the switch-cpu, e.g. for a packet inspection.
- A packet is triggered by the switch configuration and should be processed in software, e.g. DHCP or IGMP snooping.

See the packet walkthrough when an in-interface is hardware offloaded:

1. The switch checks whether the in-interface is a hardware offloaded interface.
2. Runs a packet through the switch host table to make a forwarding decision. In case any of the above-mentioned points are true, the packet gets forwarded to the switch-cpu port.
3. The packet exits through the switch-cpu port and it will be further processed by the RouterOS packet flow.

![](./img/packet-flow-in-routeros-21.webp)

:::warning
Any received packet that was flooded by the switch chip will not get flooded again by the software bridge to the same HW offloaded switch group. This prevents the formation of duplicate packets.
:::

### CPU Output to Switch

This process takes place when a packet exits the RouterOS software processing and is received on the switch-cpu port. Again, there are two paths the packet can take. One path is where hardware offloading and switching are not even used (e.g. a standalone interface for routing or a bridged interface but with deliberately disabled HW offloading), so the packet is simply sent out through the physical out-interface. Another path is taken when hardware offloading is active on the out-interface. This will cause the packet to pass through the switching decision. Just like any other switch port, the switch will learn the source MAC addresses from packets that are received on the switch-cpu port. This does come in handy when a bridge contains HW and non-HW offloaded interfaces, so the switch can learn which frames should be forwarded to the CPU. See the packet walkthrough when an out-interface is hardware offloaded:

1. A packet that exits the RouterOS software processing is received on the switch-cpu port.
2. The switch checks whether the out-interface is a hardware offloaded interface.
3. The switch runs a packet through the switch host table to make a forwarding decision. If the switch finds a match for the destination MAC address, the packet is sent out through the physical interface. A packet that ends up being flooded (e.g. broadcast, multicast, unknown unicast traffic) gets multiplied and sent out to every hardware offloaded switch port.

![](./img/packet-flow-in-routeros-22.webp)

:::warning
A software bridge that sends a flooded packet through HW offloaded interfaces will only send a single packet copy per HW offloaded switch group rather than per HW offloaded interface. The actual flooding will be done by the switch chip; this prevents the formation of duplicate packets.
:::

## Flow of an MPLS packet

The steps refer to the MPLS part of the detailed diagram:

- **Push label** - the router adds a label to a packet. A packet that the router itself sends passes the output and postrouting chains before the label is added.
- **Switch label** - the router forwards a packet by its label. The IP firewall does not process such a packet: it does not pass the prerouting, forward and postrouting chains.
- **Pop label** - the router removes the label. If the router before the last one removed the label (penultimate hop popping), the last router receives a packet without a label and processes it as an IP packet.

## MPLS IP VPN

In VPNv4 setups a packet arriving at the PE router that needs to be forwarded to the CE router is not a typical "forward".

If incoming label and destination are bound to the VRF Then after MPLS label is popped and:

- The Destination address is local to the router, then the packet is moved to LOCAL\_IN.
- The Destination address is in the CE network, then the packet is moved to LOCAL\_OUT.

:::danger
Forwarded packets from MPLS cloud to the CE network will not show up in forward.
:::

For example, traffic from src:111.15.0.1 to dst:111.13.0.1

```text
[admin@CCR2004_2XS] /mpls/forwarding-table> print 
Flags: L - LDP, P - VPN
Columns: LABEL, VRF, PREFIX, NEXTHOPS
#   LABEL  VRF      PREFIX         NEXTHOPS                                                                                                           
0 P    17  myVrf    111.13.0.0/24  
4 L    20  main     203.0.113.2    { label=impl-null; nh=111.11.0.1; interface=sfp-sfpplus1 }
[admin@CCR2004_2XS] /mpls/forwarding-table>                                                           
...

[admin@CCR2004_2XS] /ip/route> print detail 
Flags: D - dynamic; X - disabled, I - inactive, A - active; c - connect, s - static, r - rip, b - bgp, o - ospf, i - is-is, d - dhcp, v - vpn, m - modem, y - bgp-mpls-vpn; 
H - hw-offloaded; + - ecmp 

   DAc   dst-address=111.11.0.0/24 routing-table=main gateway=sfp-sfpplus1 immediate-gw=sfp-sfpplus1 distance=0 scope=10 suppress-hw-offload=no 
         local-address=111.11.0.2%sfp-sfpplus1 
   DAc   dst-address=203.0.113.1/32 routing-table=main gateway=lo immediate-gw=lo distance=0 scope=10 suppress-hw-offload=no local-address=203.0.113.1%lo 
   DAo   dst-address=203.0.113.2/32 routing-table=main gateway=111.11.0.1%sfp-sfpplus1 immediate-gw=111.11.0.1%sfp-sfpplus1 distance=110 scope=20 target-scope=10 
         suppress-hw-offload=no 
   DAc   dst-address=111.13.0.0/24 routing-table=myVrf gateway=sfp-sfpplus2@myVrf immediate-gw=sfp-sfpplus2 distance=0 scope=10 suppress-hw-offload=no 
         local-address=111.13.0.2%sfp-sfpplus2@myVrf 
   DAy   dst-address=111.15.0.0/24 routing-table=myVrf gateway=203.0.113.2 immediate-gw=111.11.0.1%sfp-sfpplus1 distance=200 scope=40 target-scope=30 suppress-hw-offload=no [admin@CCR2004_2XS] /ip/route>              
```

The packet will be seen in the output and postrouting chains, because now it is a locally originated packet with source MAC address equal to vrfInterface:

```text
08:10:55 firewall,info output: in:(unknown 0) out:sfp-sfpplus2, connection-state:established src-mac f2:b5:e9:17:18:3b, proto ICMP (type 8, code 0), 111.15.0.1->111.13.0.1, len 56
08:10:55 firewall,info postrouting: in:myVrf out:sfp-sfpplus2, connection-state:established src-mac f2:b5:e9:17:18:3b, proto ICMP (type 8, code 0), 111.15.0.1->111.13.0.1, len 56
```

On the other hand, packets routed in the direction CE→PE will be seen in the "forward" as any other routed IP traffic before being sent to the MPLS:

```text
 08:10:55 firewall,info prerouting: in:sfp-sfpplus2 out:(unknown 0), connection-state:established src-mac dc:2c:6e:46:f8:93, proto ICMP (type 0, code 0), 111.13.0.1->111.15.0.1, len 56
 08:10:55 firewall,info forward: in:sfp-sfpplus2 out:sfp-sfpplus1, connection-state:established src-mac dc:2c:6e:46:f8:93, proto ICMP (type 0, code 0), 111.13.0.1->111.15.0.1, len 56
 08:10:55 firewall,info postrouting: in:sfp-sfpplus2 out:sfp-sfpplus1, connection-state:established src-mac dc:2c:6e:46:f8:93, proto ICMP (type 0, code 0), 111.13.0.1->111.15.0.1, len 56
 
```

But there can be an exception. If the destination IP of the reply packet is local to the router and connection tracking is performing NAT translation then connection tracking will "force" the packet to move through the firewall prerouting/forward/postrouting chains.

## Logical interfaces

A tunnel packet passes the firewall two times: as the encapsulated packet and as the packet inside the tunnel.

For example, the router receives a GRE packet that carries a packet for another network:

1. The GRE packet is a packet for the router itself. It passes prerouting and input, and reaches **J**.
2. The packet needs decapsulation. The router removes the GRE header.
3. The inner packet enters at the logical in-interface, with the GRE interface as its in-interface. It passes prerouting, forward and postrouting.

In the other direction, the inner packet passes forward and postrouting with the GRE interface as its out-interface. After encapsulation, the GRE packet passes output and postrouting as a packet that the router itself sends.

A firewall that drops everything else must accept both the tunnel packets and the packets inside the tunnel.

:::info
The VLAN header that a bridge with `vlan-filtering` enabled adds or removes is not related to logical interfaces. See the bridging section of this page.
:::

## IPsec policies

IPsec has no logical interface. The router matches packets against the IPsec policies.

Encryption:

1. The plain packet passes the firewall like any other packet: forward and postrouting, or output and postrouting if the router itself sends it.
2. After postrouting, the router matches the packet against the IPsec policies. If a policy matches, the router encrypts the packet.
3. The encrypted packet passes output and postrouting as a packet that the router itself sends.

Decryption:

1. The encrypted packet is a packet for the router itself. It passes prerouting and input.
2. The router matches the packet against the IPsec policies and decrypts it.
3. The decrypted packet passes prerouting again, and then input or forward.

A firewall that drops everything else must accept both the encrypted and the plain packets. To match the plain packets, use the `ipsec-policy` matcher. For example, `ipsec-policy=in,ipsec` in the forward chain matches the packets that the router decrypted. The prerouting and input chains do not accept `ipsec-policy=out`.

## VRF

![Diagram of the chains that a packet received on a VRF port and a packet sent by the router into a VRF pass, with the in-interface or out-interface of each pass](./img/packet-flow-in-routeros-vrf.svg#gh-light-mode-only)![Diagram of the chains that a packet received on a VRF port and a packet sent by the router into a VRF pass, with the in-interface or out-interface of each pass](./img/packet-flow-in-routeros-vrf_dark.svg#gh-dark-mode-only)

Traffic of an interface that belongs to a VRF passes some chains two times:

- **Received on a VRF port** - the packet passes prerouting with the port as its in-interface: the RAW and mangle prerouting chains and the NAT `dstnat` chain. Then it passes the RAW and mangle prerouting chains again, with the VRF interface as its in-interface. The input and forward chains see the VRF interface as the in-interface.
- **Sent by the router into a VRF** - the packet passes output and postrouting with the VRF interface as its out-interface. Then it passes the RAW, mangle and filter output chains and the mangle postrouting chain again, with the port as its out-interface. The NAT chains process the packet only in the first pass.
- **Routed into a VRF** - the packet passes postrouting one time, with the port as its out-interface.

## Fast Path

From what we learned so far, it is quite obvious that such packet processing takes a lot of CPU resources. To speed things up FastPath was introduced in the first RouterOS v6. What it does is it skips processing in the Linux kernel, basically trading some RouterOS functionality for performance. For FastPath to work, interface driver support and specific configuration conditions are required.

### How Fast Path Works

FastPath is an interface driver extension that allows a driver to talk directly to specific RouterOS facilities and skip all others.

![Diagram of the hardware offload, FastPath and slow path choices between the physical in-interface and the physical out-interface](./img/packet-flow-in-routeros-fast-path.svg#gh-light-mode-only)![Diagram of the hardware offload, FastPath and slow path choices between the physical in-interface and the physical out-interface](./img/packet-flow-in-routeros-fast-path_dark.svg#gh-dark-mode-only)

The packet can be forwarded by a fast path handler only if at least the source interface supports a fast path. For complete fast-forwarding, destination interface support is also required.

Currently, RouterOS has the following FastPath handlers:

- IP traffic processing
- FastTrack
- Traffic Generator
- MPLS
- Bridge

FastPath handler is used if the following conditions are met:

- Firewall rules are not configured.
- Simple queue or queue trees with *parent=global* are not configured.
- Mesh or metarouter interface is not configured.
- Sniffer or torch is not running.
- Connection tracking is not active.
- VRFs are not configured (`/ip/vrf` is empty).
- A hotspot is not used (`/ip/hotspot` has no interfaces).
- IPSec policies are not configured.
- `/tool/mac-scan` is not actively used.
- `/tool/ip-scan` is not actively used.

:::warning
Packets will travel the FastPath way if FastTrack is used no matter whether the above conditions are met.
:::

FastPath caches IPv4 and IPv6 routes by destination address, not by L4 ports or inner headers. Therefore the ECMP `l4` and `l3-inner` policies do not provide per-flow distribution for FastPath-cached traffic.

Traffic Generator automatically uses FastPath if the interface supports this feature.

Currently, MPLS fast-path applies to MPLS switched traffic (frames that enter the router as MPLS and must leave the router as MPLS) and VPLS endpoints that do VPLS encap/decap. Other MPLS ingress and egress will operate as before.

A Bridge handler is used if the following conditions are met:

- There are no bridge Calea, filter, NAT rules.
- *use-ip-firewall* is disabled.
- No mesh, MetaRouter interface configuration.
- sniffer, torch, and traffic generator are not running.
- bridge vlan-filtering is disabled (condition is removed since RouterOS version 7.2).
- bridge dhcp-snooping is disabled.

:::warning
FastPath on the vlan-filtering bridge does NOT support priority-tagged packets (packets with VLAN header but VLAN ID = 0). Those packets are redirected via a slow path.
:::

Interfaces that support FastPath:

| RouterBoard | Interfaces |
| :-- | :-- |
| **RB6xx series** | ether1,2 |
| **RB800** | ether1,2 |
| **RB1100 series** | ether1-11 |
| **All devices** | Ethernet interfaces |
|  | wireless interfaces |
|  | bridge interfaces |
|  | VLAN, VRRP interfaces |
|  | bonding interfaces (RX only) |
|  | PPPoE, L2TP interfaces |
|  | EoIP, GRE, IPIP, VXLAN interfaces. |
|  | VPLS (starting from v7.17) |

EoIP, Gre, IPIP, VXLAN and L2TP interfaces have a per-interface setting *allow-fast-path.* Allowing a fast path on these interfaces has a side effect of bypassing firewall, connection tracking, simple queues, queue tree with parent=global, IPsec, hotspot universal client, vrf assignment for encapsulated packets that go through a fast-path. Also, packet fragments cannot be received in FastPath.

:::info
Whether FastPath is being used can be verified with `/interface/print stats-detail`
:::

The only interface queue that guarantees FastPath is only-hardware-queue. If you need an interface queue other than hardware then the packet will not go fully FastPath, but there is not a big impact on performance, as "interface queue" is the last step in the packet flow.

The packet may go Half-FastPath by switching from FastPath to SlowPath, but not the other way around. So, for example, if the receiving interface has FastPath support, but the out interface does not, then the router will process the packet by FastPath handlers as far as it can and then proceed with SlowPath. If the receiving interface does not support FastPath but the out interface does, the packet will be processed by SlowPath all the way through the router.

![](./img/packet-flow-in-routeros-31.webp)

## FastTrack

Fasttrack can be decoded as Fast Path + Connection Tracking. It allows marking connections as "fast-tracked", marking packets that belong to a fast-tracked connection will be sent the fast-path way. The connection table entry for such a connection now will have a fast-tracked flag.

![](./img/packet-flow-in-routeros-32.webp)

:::warning
FastTrack packets bypass firewall, connection tracking, simple queues, queue tree with parent=global, ip traffic-flow, IPSec, hotspot universal client, VRF assignment, so it is up to the administrator to make sure FastTrack does not interfere with other configuration!
:::

To mark a connection as fast-tracked, a new action was implemented "*fasttrack-connection"* for firewall filter and mangle. Currently, only TCP and UDP connections can be fast-tracked and to maintain connection tracking entries, some random packets will still be sent to a slow path. This must be taken into consideration when designing firewalls with "fasttrack" enabled.

The FastTrack handler also supports source and destination NAT, so special exceptions for NATed connections are not required.

:::danger
Traffic that belongs to a fast-tracked connection travels in FastPath, which means that it will not be visible by other router L3 facilities (firewall, queues, IPsec, VRF assignment, etc). Fasttrack lookups route before routing marks have been set, so it works only with the main routing table.
:::

The easiest way to start using this feature on home routers is to enable "fasttrack" for all *established, related* connections:

```ros
/ip/firewall/filter 
add chain=forward action=fasttrack-connection connection-state=established,related \
  comment="fasttrack established/related"
add chain=forward action=accept connection-state=established,related \
  comment="accept established/related"
```

Notice that the first rule marks established/related connections as fast-tracked, the second rule is still required to accept packets belonging to those connections. The reason for this is that, as was mentioned earlier, some random packets from fast-tracked connections are still sent through the slow pathway and only UDP and TCP are fast-tracked, but we still want to accept packets for other protocols.

![](./img/packet-flow-in-routeros-33.webp)![](./img/packet-flow-in-routeros-34.webp)

After adding the "FastTrack" rule, a special dummy rule appeared at the top of the list. This is not an actual rule, it is for visual information showing that some of the traffic is traveling FastPath and will not reach other firewall rules.

:::warning
FastTrack can process packets only in the main routing table so it is the system administrator's duty to not FastTrack connections that are going through a non-main routing table (thus connections that are processed with mangle action=mark-routing rules). Otherwise packets might be misrouted through the main routing table.
:::

These rules appear as soon as there is at least one fast-tracked connection tracking entry and will disappear after the last fast-tracked connection times out in the connection table.

:::warning
The connection is FastTracked until a connection is closed, timed out or the router is rebooted.
:::

#### Configuration example: excluding specific host, from being Fast-Tracked

```ros
/ip/firewall/filter
add action=accept chain=forward connection-state=established,related src-address=192.168.88.111
add action=accept chain=forward connection-state=established,related dst-address=192.168.88.111
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=no
add action=accept chain=forward connection-state=established,related
```

In this example, we exclude host 192.168.88.111 from being Fast-tracked, by first accepting it with the firewall rule, both for source and destination. The idea is - not allowing the traffic to reach the FastTrack action.

Note: the "exclusion" rules must be placed before fasttrack filters; order is important.

#### Requirements

FastTrack is active if the following conditions are met:

- No mesh, metarouter interface configuration.
- Sniffer, torch, and traffic generator are not running.
- `/tool/mac-scan` is not actively used.
- `/tool/ip-scan` is not actively used.
- FastPath and Route cache are enabled under IP/Settings (route cache condition does not apply to RouterOS v7 or newer).
- Bridge FastPath is enabled if a connection is going over the bridge interface.

## Packet flow for the visually impaired

The following document in DOCX format describes the diagram in a way optimized for visually impaired people. The descriptions are by Apex CoVantage care of Benetech. They are not being updated.

- [Packet flow, optimized document.](https://box.mikrotik.com/f/673207754e4d40638fae/?dl=1)
