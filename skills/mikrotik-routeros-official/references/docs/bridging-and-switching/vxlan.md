# VXLAN

> Configure VXLAN interfaces and static VTEPs, bridge Layer 2 networks and VLANs over IPv4 or IPv6, check the forwarding database, plan MTU, and understand hardware-offload restrictions.

# VXLAN

Virtual eXtensible Local Area Network (VXLAN) carries Layer 2 frames over a routed IP network. It uses UDP and a 24-bit VXLAN Network Identifier (VNI) to distinguish overlay networks. The larger identifier space addresses the 4096-VLAN limit of IEEE 802.1Q. [RFC 7348](https://www.rfc-editor.org/rfc/rfc7348) defines the protocol.

A VXLAN Tunnel Endpoint (VTEP) encapsulates and decapsulates frames. A VXLAN interface can have multiple remote VTEPs, so it forms a one-to-many overlay rather than a point-to-point link. Configure static remote VTEPs in `/interface/vxlan/vteps`, or use [EVPN](../user-guides/routing-and-networking-protocols/unicast/evpn) to discover VTEPs and distribute MAC reachability through BGP.

RouterOS supports IPv4 and IPv6 underlays. One VXLAN interface uses one underlay address family, not a dual-stack VTEP list. The underlay routing table selects the egress interface and, when `local-address` is unset, its source address. Set `vtep-vrf` to use an underlay in another VRF; the overlay bridge can remain in `main`.

## Connect two Layer 2 networks with static VTEPs

This example extends an Ethernet segment between two routers. Each router has a routed underlay on `ether2` and a separate `bridge1` for the overlay. The configuration preserves the underlay's Layer 3 boundary while allowing hosts connected to the overlay bridges to communicate at Layer 2. VXLAN adds encapsulation overhead and does not provide encryption.

Router1 uses `192.0.2.2` and `10.255.110.2`; Router2 uses `192.0.2.3` and `10.255.110.3`. The underlay addresses are on a connected subnet, so no additional static route is required. In a routed underlay, add routes to the remote VTEP addresses before configuring the tunnel.

**Router1:**

```ros
/interface/bridge/add name=bridge1 protocol-mode=none
/ip/address/add address=192.0.2.2/24 interface=ether2
/ip/address/add address=10.255.110.2/24 interface=bridge1
/interface/vxlan/add name=vxlan110 vni=110 \
    local-address=192.0.2.2 bridge=bridge1
/interface/vxlan/vteps/add interface=vxlan110 \
    remote-ip=192.0.2.3
```

**Router2:**

```ros
/interface/bridge/add name=bridge1 protocol-mode=none
/ip/address/add address=192.0.2.3/24 interface=ether2
/ip/address/add address=10.255.110.3/24 interface=bridge1
/interface/vxlan/add name=vxlan110 vni=110 \
    local-address=192.0.2.3 bridge=bridge1
/interface/vxlan/vteps/add interface=vxlan110 \
    remote-ip=192.0.2.2
```

The `bridge` property adds the VXLAN interface to the bridge as a dynamic port. Add the Ethernet ports that face your Layer 2 hosts to the same bridge. Do not bridge those hosts only to the underlay Ethernet port: traffic between two physical underlay ports does not enter VXLAN.

Both endpoints must use the same VNI and UDP port. The default destination and listening port is 4789. Permit UDP traffic between the VTEP addresses in the underlay firewall.

Ping the remote overlay address to check the tunnel:

```ros
/ping 10.255.110.3 count=3
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS      
    0 10.255.110.3                               56  64 870us     
    1 10.255.110.3                               56  64 391us     
    2 10.255.110.3                               56  64 588us     
    sent=3 received=3 packet-loss=0% min-rtt=391us avg-rtt=616us 
   max-rtt=870us 
```

After traffic passes, `/interface/vxlan/fdb/print` maps the remote MAC address to its VTEP:

```text
Columns: INTERFACE, REMOTE-IP, MAC-ADDRESS
#  INTERFACE  REMOTE-IP  MAC-ADDRESS      
0  vxlan110   192.0.2.3  56:9E:4C:61:01:68
```

## Carry VLANs over VXLAN

A VLAN ID and a VNI are independent identifiers. Bridge VLAN filtering determines which VLANs enter the VXLAN interface. An untagged service commonly uses a one-to-one VLAN-to-VNI mapping. A tagged VXLAN bridge port can carry multiple VLANs over one VNI.

This example continues the preceding topology with untagged VLAN 10 and tagged VLAN 20 in one VNI. Router1 keeps underlay address `192.0.2.2/24` and Router2 keeps `192.0.2.3/24` on `ether2`. Add the following objects without reassigning the underlay addresses.

**Router1:**

```ros
/interface/bridge/add name=bridge-vlan protocol-mode=none \
    pvid=10 vlan-filtering=yes
/ip/address/add address=10.255.70.1/24 interface=bridge-vlan
/interface/vxlan/add name=vxlan10070 vni=10070 \
    local-address=192.0.2.2 bridge=bridge-vlan bridge-pvid=10
/interface/vxlan/vteps/add interface=vxlan10070 \
    remote-ip=192.0.2.3
/interface/vlan/add name=vlan20 interface=bridge-vlan vlan-id=20
/ip/address/add address=10.255.72.1/24 interface=vlan20
/interface/bridge/vlan/add bridge=bridge-vlan vlan-ids=20 \
    tagged=bridge-vlan,vxlan10070
```

**Router2:**

```ros
/interface/bridge/add name=bridge-vlan protocol-mode=none \
    pvid=10 vlan-filtering=yes
/ip/address/add address=10.255.70.3/24 interface=bridge-vlan
/interface/vxlan/add name=vxlan10070 vni=10070 \
    local-address=192.0.2.3 bridge=bridge-vlan bridge-pvid=10
/interface/vxlan/vteps/add interface=vxlan10070 \
    remote-ip=192.0.2.2
/interface/vlan/add name=vlan20 interface=bridge-vlan vlan-id=20
/ip/address/add address=10.255.72.3/24 interface=vlan20
/interface/bridge/vlan/add bridge=bridge-vlan vlan-ids=20 \
    tagged=bridge-vlan,vxlan10070
```

The PVID creates the untagged VLAN 10 membership for the bridge and VXLAN port. The explicit VLAN 20 entry makes the bridge interface and VXLAN port tagged members, allowing the router's local `vlan20` interface and the remote VTEP to exchange tagged frames. See [bridge VLAN configuration](./user-guides/bridge-vlan-table) for physical access and trunk port configuration.

Check both overlay subnets:

```ros
/ping 10.255.70.3
/ping 10.255.72.3
```

## Forward unicast and BUM traffic

The VXLAN forwarding database (FDB) associates inner source MAC addresses with remote VTEP addresses. With `learning=yes`, received packets create these mappings dynamically. Later unicast frames can be sent only to the VTEP that owns the destination MAC. Set `learning=no` to suppress this learning. Static VTEP entries remain available for flooding and are not inbound access-control rules.

Broadcast, unknown-unicast and multicast (BUM) traffic needs replication:

- **Unicast head-end replication** sends one copy to every static remote VTEP. This is the default when no multicast `group` is configured.
- **Multicast underlay** sends BUM traffic to the configured multicast `group`. Set both `group` and `interface`; either property without the other is rejected.

For example, this interface uses multicast group `239.255.10.30` on the underlay interface:

```ros
/interface/vxlan/add name=vxlan10030 vni=10030 \
    local-address=192.0.2.2 group=239.255.10.30 \
    interface=ether2 bridge=bridge1
```

Configure the same VNI, group and UDP port on the other VTEPs, with their own local addresses. Static VTEP entries are not required for multicast flooding. The router joins the group with IGMP or MLD. A routed multicast underlay also requires multicast routing, such as PIM, and sufficient `ttl`. The automatic TTL is 1 for multicast and 64 for unicast underlay packets.

A VXLAN interface does not maintain a separate multicast database for each remote VTEP. When an IGMP-snooping bridge forwards a group to a VXLAN port with multiple static VTEPs, VXLAN can replicate it to all of them. Use separate VXLAN interfaces when you need independent flooding domains.

The configured UDP `port` is the listening and destination port. RouterOS varies the outer source port from inner-packet fields to provide entropy for load balancing. Each VTEP must be able to reach the remote listening port. A NAT between VTEPs must maintain return mappings for the entropy-derived source ports and forward incoming traffic to the VTEP behind NAT; do not assume that the source port is also 4789.

## Check the overlay and troubleshoot failures

Inspect the interface, static VTEPs and learned mappings after sending traffic:

```ros
/interface/vxlan/print detail
/interface/vxlan/vteps/print
/interface/vxlan/fdb/print
/interface/bridge/host/print
```

Work through the path in order:

1. **Check the underlay route.** Ping the remote VTEP address and confirm that the route uses the intended interface and routing table. Permit the configured UDP port and its return traffic through the underlay firewall.
2. **Compare the VNI, UDP port and address family.** Both endpoints need the same VNI and port. Remote VTEPs opposite to the interface's `vteps-ip-version` are ignored. A VNI can be assigned to only one VXLAN interface on a router.
3. **Check the overlay bridge.** The VXLAN interface, not the routed underlay port, belongs in the overlay bridge. For VLAN-filtering bridges, also check PVID and tagged or untagged membership.
4. **Check learning.** An empty FDB is expected with `learning=no` or before traffic arrives. Static VTEP entries can still flood traffic when no FDB mapping exists.
5. **Check packet sizes.** Test progressively smaller inner packets with DF set. Reduce the VXLAN MTU or increase the underlay MTU if large frames disappear.
6. **Capture the underlay.** Compare VNI, UDP ports and inner Ethernet frames at both endpoints. A running interface and configured VTEP do not prove that packets arrive.

Start a UDP port 4789 capture on the underlay interface:

```ros
/tool/sniffer/set filter-interface=ether2 filter-port=4789 \
    file-name=vxlan.pcap
/tool/sniffer/start
```

Generate overlay traffic, then stop the capture with `/tool/sniffer/stop`.

## Plan MTU and fragmentation

The outer IP packet is larger than the inner IP packet:

| Underlay and inner tagging | Added bytes | Largest inner packet on a 1500-byte underlay |
| :-- | --: | --: |
| IPv4, untagged | 50 bytes | 1450 bytes |
| IPv4, one 802.1Q tag | 54 bytes | 1446 bytes |
| IPv6, untagged | 70 bytes | 1430 bytes |
| IPv6, one 802.1Q tag | 74 bytes | 1426 bytes |

Carrying a 1500-byte untagged inner IP packet without fragmentation therefore requires an underlay IP MTU of at least 1550 bytes for IPv4 or 1570 bytes for IPv6. Add another 4 bytes for each 802.1Q tag. Increase the MTU along the entire underlay path, or reduce the VXLAN interface `mtu` to fit the existing path.

Without an associated multicast `interface`, the read-only `l2mtu` is 65535. When the associated interface exposes its own L2MTU, VXLAN subtracts 50 bytes for an IPv4 underlay or 70 bytes for IPv6. Reduce the VXLAN `mtu` if the default 1500 bytes does not fit the associated interface. The L2MTU does not prove that every hop in the underlay supports the required MTU.

The `dont-fragment` property controls outer-packet fragmentation:

- `disabled` clears DF on an IPv4 outer packet and permits fragmentation. It also permits IPv6 outer fragmentation.
- `enabled` sets DF on an IPv4 outer packet and prevents fragmentation. Oversized payloads are dropped instead of being fragmented. IPv6 outer packets are not fragmented either.
- `inherit` copies the inner IPv4 DF decision to the IPv4 outer packet. Non-IP inner traffic has no outer DF flag. Inner IPv6 traffic sets outer IPv4 DF. On an IPv6 underlay, `inherit` permits fragmentation like `disabled`.
- `auto` uses `enabled` on devices with VXLAN hardware offload and `inherit` otherwise.

Prefer an MTU that avoids outer fragmentation. Besides adding processing overhead, fragmentation requires every fragment to reach the remote VTEP before it can decapsulate the inner frame.

## Hardware offloading

Supported switch chips can offload VXLAN encapsulation and decapsulation when `hw=yes`. The `H` flag on VXLAN interfaces and VTEPs indicates hardware-offloaded entries. Consult the [L3HW device support matrix](./l3-hardware-offloading#l3hw-device-support) before designing for offload; a hardware-offloaded bridge port alone does not prove that the complete VXLAN path is offloaded.

The supported underlay is more restricted than software VXLAN:

- Use a standalone routed Ethernet underlay. ECMP and bond, bridge or VLAN underlay interfaces are not supported.
- Multicast underlay and IPv6 VTEP offload are not supported.
- VXLAN-VRF offload is supported on CPSS switch chips. On other switch chips, keep the underlay in `main` unless the device support matrix explicitly lists VXLAN-VRF support. The software `vtep-vrf` property does not imply hardware support.

For the overlay, hardware supports static one-to-one untagged VLAN-to-VNI mappings and tagged VLAN-aware mappings within a VLAN-filtering bridge. The following restrictions apply:

- Routing between different VNIs is not supported.
- VTEPs are isolated, with no configurable horizon between them.
- MDB entries on VXLAN ports are not offloaded for IGMP snooping. Enabling snooping can restrict multicast forwarding between Ethernet and VXLAN.
- Bridged VXLAN interfaces are not supported by MLAG.

### Configure static VLAN-to-VNI mappings

This example uses a loopback VTEP address and a routed underlay. Router1 has loopback `192.0.2.1/32`, underlay `198.51.100.1/30`, and access ports in VLANs 10 and 20. Router2 uses `192.0.2.2/32` and `198.51.100.2/30`. Both endpoints have matching VNIs and access-port VLANs. The underlay MTU accommodates large encapsulated frames and must be supported along the whole path.

```ros
/interface/bridge/add name=bridge1 vlan-filtering=yes
/interface/ethernet/set [find default-name=sfp-sfpplus1] \
    l2mtu=9500 mtu=9500
/interface/vxlan/add name=vxlan-10010 vni=10010 \
    local-address=192.0.2.1 bridge=bridge1 bridge-pvid=10
/interface/vxlan/add name=vxlan-10020 vni=10020 \
    local-address=192.0.2.1 bridge=bridge1 bridge-pvid=20
/interface/bridge/port/add bridge=bridge1 \
    interface=sfp-sfpplus3 pvid=10
/interface/bridge/port/add bridge=bridge1 \
    interface=sfp-sfpplus4 pvid=20
/interface/vxlan/vteps/add interface=vxlan-10010 \
    remote-ip=192.0.2.2
/interface/vxlan/vteps/add interface=vxlan-10020 \
    remote-ip=192.0.2.2
/ip/address/add address=192.0.2.1/32 interface=lo
/ip/address/add address=198.51.100.1/30 \
    interface=sfp-sfpplus1
/ip/route/add dst-address=192.0.2.2/32 gateway=198.51.100.2
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

On Router2, mirror the configuration with local addresses `192.0.2.2` and `198.51.100.2/30`, remote VTEP `192.0.2.2` replaced by `192.0.2.1`, and the route to `192.0.2.1/32` through `198.51.100.1`.

Static routes are shown for brevity. OSPF or BGP can distribute the loopback VTEP addresses when the underlay meets the hardware restrictions.

For all interface, VTEP and FDB properties, see the [VXLAN CLI reference](../cli-reference/interface/vxlan/).
