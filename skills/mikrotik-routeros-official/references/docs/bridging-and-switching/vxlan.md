# VXLAN

> This page documents MikroTik RouterOS's VXLAN implementation, covering its purpose in expanding VLAN IDs, configuration options for VXLAN interfaces and VTEPs, and forwarding table monitoring. It details settings...

# VXLAN

---

Virtual eXtensible Local Area Network (VXLAN) is a tunneling protocol designed to solve the problem of limited VLAN IDs (4096) in IEEE 802.1Q, and it is described by IETF RFC 7348. With VXLAN the size of the identifier is expanded to 24 bits (16777216). It creates a Layer 2 overlay scheme on a Layer 3 network and the protocol runs over UDP. RouterOS VXLAN interface supports IPv4 or IPv6 (since version 7.6), but dual-stack is not supported.

:::info
VXLAN creates a 50-byte overhead for IPv4 and a 70-byte overhead for IPv6. When configuring VXLAN, it is recommended to ensure that the size of the encapsulated Ethernet frame does not exceed the MTU of the underlying network, by configuring the MTU accordingly or by limiting the size of the Ethernet frames.
:::

Only devices within the same VXLAN segment can communicate with each other. Each VXLAN segment is identified through a 24-bit segment ID, termed the VXLAN Network Identifier (VNI). Unlike most tunnels, a VXLAN is a 1-to-N network, not just point-to-point. VXLAN endpoints, which terminate VXLAN tunnels, are known as VXLAN tunnel endpoints (VTEPs). RouterOS only supports statically configured remote VTEPs. When unicast traffic needs to be sent over VXLAN, a device can learn the IP address of the other endpoint dynamically in a manner similar to a learning bridge, and forward traffic only to the necessary VTEP. For traffic that needs to be flooded (broadcast, unknown-unicast, and multicast) to all VTEPs on the same segment, VXLAN can use multicast or unicast with head-end replication to send one replica for every remote VTEP.

## Configuration options

---

This section describes the VXLAN interface and VTEP configuration options.

**Sub-menu:** `/interface/vxlan`

| Property | Description |
| :-- | :-- |
| **allow-fast-path** (*yes \| no*; Default: **yes**) | Whether to allow [Fast Path](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path) processing. Fragmented and flooded packets over VXLAN are redirected via a slow path. Fast Path is disabled for VXLAN interface that uses VRF. The setting is available since RouterOS version 7.8. |
| **arp** (*disabled \| enabled \| local-proxy-arp \| proxy-arp \| reply-only*; Default: **enabled**) | Address Resolution Protocol setting<code>disabled</code> - the interface will not use ARP<code>enabled</code> - the interface will use ARP<code>local-proxy-arp</code> -  the router performs proxy ARP on the interface and sends replies to the same interface<code>proxy-arp</code> - the router performs proxy ARP on the interface and sends replies to other interfaces<code>reply-only</code> - the interface will only reply to requests originating from matching IP address/MAC address combinations which are entered as static entries in the IP/ARP table. No dynamic entries will be automatically stored in the IP/ARP table. Therefore for communications to be successful, a valid static entry must already exist. |
| **arp-timeout** (*auto \| integer*; Default: **auto**) | How long the ARP record is kept in the ARP table after no packets are received from IP. Value `auto` equals to the value of `arp-timeout` in IP/Settings, default is the 30s. |
| **bridge** (*name*; Default: ) | Name of the [bridge](../user-guides/routing-and-networking-protocols/unicast/bgp/index.md) interface to which VXLAN interface will be added as a slave port. |
| **bridge-pvid** (*integer 1..4094;* Default: **1**) | Used to assign PVID parameter for dynamically bridge port. This property only has an effect when bridge vlan-filtering is set to yes. |
| **checksum**(*yes \| no*; Default: **no**) | Setting controls whether a UDP checksum is calculated in the transmitted outer VXLAN packets: <code>no</code> – the UDP checksum is set to zero in transmitted outer packets. This also allows receiving VXLAN packets over IPv6 that have a zero UDP checksum.<code>yes</code> - the UDP checksum is calculated in transmitted outer packets. If hardware offloading is used for packet transmission, this setting is ignored, and the behavior defaults to sending packets with a zero UDP checksum. |
| **comment** (*string*; Default: ) | Short description of the interface. |
| **disabled** (*yes \| no*; Default: **no**) | Changes whether the interface is disabled. |
| **dont-fragment**(*auto \| disabled \| enabled \| inherit*; Default: **auto**) | The Don't Fragment (DF) flag controls whether a packet can be broken into smaller packets, called fragments, before being sent over a network. When configuring VXLAN, this setting determines the presence of the DF flag on the outer IPv4 header and can control packet fragmentation if the encapsulated packet exceeds the outgoing interface MTU. This setting has three options: <code>auto</code> - if the device supports VXLAN offloading, the dont-fragment mode will operate as <code>enabled</code>. if VXLAN offloading is not supported, it will use the <code>inherit</code> mode.<code>disabled</code> - the DF flag is not set on the outer IPv4 header, which means that packets can be fragmented if they are too large to be sent over the outgoing interface. This also allows packet fragmentation when VXLAN uses IPv6 underlay. Disables hardware offloading on compatible devices.<code>enabled</code> - the DF flag is always set on the outer IPv4 header, which means that packets will not be fragmented and will be dropped if they exceed the outgoing interface's MTU. This also avoids packet fragmentation when VXLAN uses IPv6 underlay.<code>inherit</code> - The DF flag on the outer IPv4 header is based on the inner IPv4 DF flag. If the inner IPv4 header has the DF flag set, the outer IPv4 header will also have it set. If the packet exceeds the outgoing interface's MTU and DF is set, it will be dropped. If the inner packet is non-IP, the outer IPv4 header will not have the DF flag set and packets can be fragmented. If the inner packet is IPv6, the outer IPv4 header will always set the DF flag and packets cannot be fragmented. Note that when VXLAN uses IPv6 underlay, this setting does not have any effect and is treated the same as <code>disabled</code>. The setting is available since RouterOS version 7.8. |
| **group** (*IPv4 \| IPv6*; Default: ) | When specified, a multicast group address can be used to forward broadcast, unknown-unicast, and multicast traffic between VTEPs. This property requires specifying the `interface` setting. The interface will use IGMP or MLD to join the specified multicast group, make sure to add the necessary PIM and IGMP/MLD configuration. When this property is set, the `vteps-ip-version` automatically gets updated to the used multicast IP version. Disables hardware offloading on compatible devices. |
| **hw** (*yes \| no*; Default: **yes**) | Allows to disable hardware offloading, only applies to devices that support VXLAN offloading. |
| **interface** (*name*; Default: ) | Interface name used for multicast forwarding. This property requires specifying the `group` setting. Disables hardware offloading on compatible devices. |
| **learning**(*yes \| no*; Default: **yes**) | Setting controls whether inner source MAC addresses and remote VTEP IP/IPv6 addresses are learned dynamically from received packets. |
| **local-address** (*IPv4 \| IPv6*; Default: ) | Specifies the local source address for the VXLAN interface. If not set, one IP address of the egress interface will be selected as a source address for VXLAN packets. When the property is set, the `vteps-ip-version` automatically gets updated to the used local IP version. The setting is available since RouterOS version 7.7. |
| **mac-address** (*MAC*; Default: ) | Static MAC address of the interface. A randomly generated MAC address will be assigned when not specified. |
| **max-fdb-size** (*integer: 1*..65535**; Default: **4096**) | Limits the maximum number of MAC addresses that VXLAN can store in the forwarding database (FDB). |
| **mtu** (*integer*; Default: **1500**) | For the maximum transmission unit, the VXLAN interface will set MTU to 1500 by default. The `l2mtu` will be set automatically according to the associated `interface` (subtracting 50 bytes corresponding to the VXLAN header). If no interface is specified, the `l2mtu` value of 65535 is used. The `l2mtu` cannot be changed. |
| **name** (*text*; Default: **vxlan1**) | Name of the interface. |
| **port** (*integer: 1*..65535**; Default: **4789**) | Used UDP port number for listening and sending packets to remote VTEPs. |
| **rem-csum** (*both \| none \| rx \| tx*; Default: **none**) | Changes the Remote Checksum Offload (RCO) settings for VXLAN interface. RCO is a technique for eliding the inner checksum of an encapsulated datagram, allowing the outer checksum to be offloaded by network driver. It does, however, involve a change to the encapsulation protocols, which the receiver must also support. For this reason, it is disabled by default and setting is available to ensure compatibility with systems that rely on this feature.  RCO is detailed in the following Internet-Drafts:  Remote checksum offload for VXLAN, draft-herbert-vxlan-rco-00. Remote checksum offload for encapsulation, draft-herbert-remotecsumoffload-00.  If [hardware offloading](./vxlan.md#hardware-offloaded-vxlan) is used, this setting is ignored, and the behavior defaults to none. |
| **ttl** (*auto \| integer: 0*..255**; Default: **auto**) | Specifies the TTL value to use in outgoing packets. By default, the TTL is set to 64 when using the `auto` option. However, if VXLAN is using a multicast underlay network, the default TTL is set to 1. If the multicast network involves routing, you will need to increase the TTL to a higher value. |
| **vni** (*integer: 1..16777215*; Default: ) | VXLAN Network Identifier (VNI). |
| **vtep-vrf** (*name*; Default: **main**) | Set VRF for the VXLAN interface on which the VTEPs listen and make connections. VRF is not supported when using `interface` and multicast `group` settings. The same UDP `port` cannot be used in multiple routing tables at the same time. When using a VRF that is not set as the "main", hardware offloading is disabled on compatible devices. The setting is available since RouterOS version 7.7. |
| **vteps-ip-version** (*ipv4 \| ipv6*; Default: **ipv4**) | Used IP protocol version for statically configured VTEPs. The RouterOS VXLAN interface does not support dual-stack, any configured remote VTEPs with the opposite IP version will be ignored. When multicast `group` or `local-address` properties are set, the `vteps-ip-version` automatically gets updated to the used IP version. Using IPv6 disables hardware offloading on compatible devices. The setting is available since RouterOS version 7.6. |

**Sub-menu:** `/interface/vxlan/vteps`

| Property | Description |
| :-- | :-- |
| **comment** (*string*; Default: ) | Short description of the configured VTEP. |
| **interface** (*name*; Default: ) | Name of the VXLAN interface. |
| **remote-ip** (*IPv4 \| IPv6*; Default: ) | Defines the VTEP endpoint IPv4 or IPv6 address which is used when the VXLAN interface needs to send BUM (broadcast, unknown-unicast, multicast) traffic. It is not used as access control. |

## Forwarding table

---

Since RouterOS version 7.9, it is possible to monitor the learned MAC addresses from remote VTEPs.

**Sub-menu:** `/interface/vxlan/fdb`

| Property | Description |
| :-- | :-- |
| **interface** (*read-only: *name**) | Name of the VXLAN interface. |
| **mac-address** (*read-only: MAC address*) | MAC address. |
| **remote-ip** (*read-only: IPv4 \| IPv6 address*) | The IPv4 or IPv6 destination address of the remote VTEP. |

```ros
[admin@MikroTik] > /interface/vxlan/fdb/print          
 0 remote-ip=2001::2 mac-address=56:FF:AA:1A:72:33 interface=vxlan1 

 1 remote-ip=2002::2 mac-address=AE:EC:C4:12:8B:B9 interface=vxlan1 

 2 remote-ip=192.168.10.20 mac-address=FE:AF:58:31:A7:B6 interface=vxlan2
```

## Configuration example

---

This configuration example creates a single VXLAN tunnel between two statically configured VTEP endpoints.

First, create VXLAN interfaces on both routers.

```ros
/interface/vxlan
add name=vxlan1 port=4789 vni=10
```

Then configure VTEPs on both routers with respective IPv4 destination addresses. Both devices should have an active route toward the destination address.

```ros
# Router1
/interface/vxlan/vteps
add interface=vxlan1 remote-ip=192.168.10.10

# Router2
/interface/vxlan/vteps
add interface=vxlan1 remote-ip=192.168.20.20
```

The configuration is complete. It is possible to include the VXLAN interface into a bridge with other Ethernet interfaces.

## Hardware offloaded VXLAN

---

Starting from RouterOS version 7.18, initial support for hardware-offloaded VXLAN was introduced. This makes the offloaded VXLAN data plane possible, supporting encapsulation and decapsulation, and allowing for static one-to-one VLAN-to-VXLAN mappings within a vlan-filtering bridge. Refer to the [L3HW Device Support](./l3-hardware-offloading.md#l3hw-device-support) documentation for a list of compatible devices.

At this point, some known features are not yet implemented.

### Underlay (routing encapsulated VXLAN packets)

1. VTEPs are not supported over ECMP.

2. VTEPs are not supported over bond, bridge, VLAN interfaces (only stand-alone routed Ethernet interfaces are supported).

3. VTEPs are not supported over multicast.

4. VTEPs cannot operate within VRFs.

5. VTEPs are not supported with IPv6.

### Overlay (forwarding between Ethernet and VXLAN)

1. Routing between different VXLAN VNIs is not supported.

2. VTEPs are isolated, and there is no mechanism to control "horizon" between them.

3. Bridged VXLAN interfaces do not support IGMP snooping. When snooping is enabled, MDB entries on VXLAN are not offloaded, and multicast traffic gets restricted between Ethernet and VXLAN.

4. Bridged VXLAN interfaces are not supported by MLAG.

### Basic configuration example

In this example, static routing is used to reach remote VTEPs, but dynamic routing protocols like OSPF or BGP could also be used. The upstream interface has a higher MTU to support large packets and VXLAN encapsulation. Below is a network topology overview:

**sfp-sfpplus1** - upstream (underlay) interface  
**sfp-sfpplus3** - bridged port for untagged VLAN 10  
**sfp-sfpplus4** - bridged port for untagged VLAN 20  
**vxlan-10010** - overlay port for untagged VLAN 10  
**vxlan-10020** - overlay port for untagged VLAN 20

```routeros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/ethernet
set [ find default-name=sfp-sfpplus1 ] l2mtu=9500 mtu=9500
/interface/vxlan
add bridge=bridge1 bridge-pvid=10 local-address=192.168.1.1 name=vxlan-10010 vni=10010
add bridge=bridge1 bridge-pvid=20 local-address=192.168.1.1 name=vxlan-10020 vni=10020
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus3 pvid=10
add bridge=bridge1 interface=sfp-sfpplus4 pvid=20
/interface/vxlan/vteps
add interface=vxlan-10010 remote-ip=192.168.1.2
add interface=vxlan-10020 remote-ip=192.168.1.2
/ip/address
add address=192.168.1.1 interface=lo network=192.168.1.1
add address=192.168.10.10/24 interface=sfp-sfpplus1 network=192.168.10.0
/ip/route
add dst-address=192.168.1.2 gateway=192.168.10.20
/interface/ethernet/switch
set 0 l3-hw-offloading=yes
```
