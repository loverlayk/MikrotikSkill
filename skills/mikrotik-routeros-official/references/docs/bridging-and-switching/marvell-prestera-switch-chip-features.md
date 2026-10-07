# Marvell Prestera switch chip features

> MikroTik devices with Marvell Prestera switch chip offer high-performance Layer 2 and Layer 3 features including advanced forwarding, routing offloading, VLAN support, QoS, mirroring, and PTP synchronization for...

# Marvell Prestera switch chip features

---

Some MikroTik devices use high-performance and feature-rich Marvell Prestera Ethernet switches. These devices can be designed into various Ethernet applications including unmanaged switch, Layer 2 managed switch, carrier switch, inter-VLAN router, and wired unified packet processor.

:::warning
This article applies only to MikroTik devices with Marvell Prestera switch, not to [CRS1xx/CRS2xx series switches](./user-guides/crs1xx-2xx-series-switches-examples).
:::

### Features

<WideTable>

| Features | Description |
| :-- | :-- |
| **Forwarding** | Configurable ports for switching or routingFull non-blocking wire-speed switchingLarge Unicast FDB for Layer 2 unicast forwardingForwarding Databases work based on IVLJumbo frame supportIGMP/MLD Snooping supportDHCP Snooping support with custom Option 82 (Circuit ID, Remote ID)DHCPv6 Snooping support with custom Option 18 (Interface ID) and Option 37 (Remote ID)RA Guard support |
| **Routing** | Layer 3 Hardware Offloading:IPv4, IPv6 Unicast RoutingSupported on Ethernet, Bridge, Bonding, and VLAN interfacesECMPBlackholesOffloaded Fasttrack connections <sup>1</sup>Offloaded NAT for Fasttrack connections <sup>1</sup>Hardware-offloaded VRF <sup>1</sup>Multiple MTU profiles**Important:** 1. Applies only to [certain switch models](./l3-hardware-offloading.md#l3hw-device-support)  |
| **Spanning Tree Protocol** | STPRSTPMSTPEdge port, BPDU Guard, Root Guard |
| **Mirroring** | Various types of mirroring:Port based mirroringVLAN based mirroringMAC based mirroringRemote Switch Port Analyzer (RSPAN) |
| **VLAN** | Fully compatible with IEEE802.1Q and IEEE802.1ad VLAN4k active VLANsFlexible VLAN assignment:Port based VLANProtocol based VLANMAC based VLANVLAN filteringIngress VLAN translationMultiple VLAN Registration protocol (MVRP) |
| **Bonding** | Supports 802.3ad (LACP), balance-xor and active-backup modesUp to 8 member ports per bonding interfaceHardware automatic failover and load balancingMLAG |
| **Quality of Service (QoS)** | Eight output queues per portDSCP and 802.1p PCP mappingPort based Layer2 and Layer3 trust settingsPort and Queue based egress rate limiterPolicy based QoS via ACL rulesStrict Priority (SP) and Shaped Deficit Weighted Round Robin (SDWRR) queuingEnhanced Transmission Selection (ETS) schedulingWeighted Random Early Detection (WRED) <sup>1</sup>Explicit Congestion Notification (ECN) <sup>1</sup>Priority-based Flow Control (PFC) <sup>1</sup>Resource allocation control (queue, shared-pool and multicast based) with extensive monitoring capabilitiesCompatible with Dante environmentsCompatible with RDMA over Converged Ethernet (RoCE) environment <sup>1</sup>Ingress traffic limiting (port based or via ACL rules)Traffic storm control**Important:** 1. Applies only to [certain switch models](./quality-of-service.md#qos-device-support)  |
| **Port isolation** | Applicable for Private VLAN implementation |
| **Access Control List** | Ingress ACL tablesClassification based on ports, L2, L3, L4 protocol header fieldsACL actions include filtering, forwarding and modifying of the protocol header fields |
| **PTP** | Two-step Ordinary Clock and Boundary Clock.Hardware timestamping, ensuring clock synchronization in the nanosecond(ns) range.IPv4 and Layer 2 (L2) multicast transport modes.End-to-End (E2E) and Peer-to-Peer (P2P) delay mechanisms.IEEE 1588-2008 (PTPv2).Profile Support for:802.1AS: Timing and synchronization for Audio Video Bridging (AVB) and Time-Sensitive Networking (TSN).AES67: High-performance audio-over-IP interoperability.G.8275.1: Frequency and phase synchronization in PTP-aware networks.SMPTE: Audio/video synchronization in professional broadcast environments.**Important:** PTP support is hardware-dependent, please refer to the list of [supported devices.](../system-information-and-utilities/precision-time-protocol.md#supported-devices)  |

:::info
For L3 hardware offloading feature support and hardware limits, please refer to [Feature Support](./l3-hardware-offloading.md#l3hw-device-support) user manuals.
:::

:::note
For QoS hardware offloading feature support and hardware limits, please refer to the [Quality of Service (QoS)](./quality-of-service.md) user manuals.
:::

</WideTable>

### Models

This table clarifies the main differences between Cloud Router Switch models and CCR routers.

<WideTable>

|  |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **Model** | **Switch Chip** | **CPU** | **Size of RAM** | **Ethernet** | **[PoE out](../hardware/poe-out.mdx)** | **ACL rules** | **Unicast FDB entries** | **Jumbo Frame (Bytes)** |
| **CRS318-1Fi-15Fr-2S-OUT (netPower 15FR)** | Marvell-98DX224S | ARM 2-core 800MHz | 256 MB | 16x 10/100M Ethernet  2x 1G SFP | 1x passive | 128 | up to 16K | 10218 |
| **CRS318-16P-2S+OUT (netPower 16P)** | Marvell-98DX226S | ARM 2-core 800MHz | 256 MB | 16x 10/100/1000M Ethernet  2x 10G SFP+ | 16x 802.3af/at | 128 | up to 16K | 10218 |
| **CRS310-1G-5S-4S+ (netFiber 9/IN)** | Marvell-98DX226S | ARM 2-core 800MHz | 256 MB | 1x 10/100/1000M Ethernet  5x 1G SFP  4x 10G SFP+ |  | 128 | up to 16K | 10218 |
| **CRS310-8G+2S+IN** | Marvell-98DX226S | ARM 2-core 800MHz | 256 MB | 8x 2.5G Ethernet  2x 10G SFP+ |  | 128 | up to 16K | 10218 |
| **CRS320-8P-8B-4S+RM** | Marvell-98DX226S | ARM 2-core 800MHz | 256 MB | 16x 10/100/1000M Ethernet  4x 10G SFP+ | 8x 802.3af/at  8x 802.3bt | 128 | up to 16K | 10218 |
| **CRS304-4XG-IN** | Marvell-98DX2528 | ARM64 2-core 1200MHz | 512 MB | 4x 1/2.5/5/10G Ethernet |  | 128 | up to 16K | 10218 |
| **CRS326-24G-2S+ (RM/IN)** | Marvell-98DX3236 | ARM 2-core 800MHz | 512 MB | 24x 10/100/1000M Ethernet  2x 10G SFP+ |  | 128 | up to 16K | 10218 |
| **CRS328-24P-4S+RM** | Marvell-98DX3236 | ARM 1-core 800MHz | 512 MB | 24x 10/100/1000M Ethernet  4x 10G SFP+ | 24x 802.3af/at | 128 | up to 16K | 10218 |
| **CRS328-4C-20S-4S+RM** | Marvell-98DX3236 | ARM 2-core 800MHz | 512 MB | 20x 1G SFP  4x 1G combo  4x 10G SFP+ |  | 128 | up to 16K | 10218 |
| **CRS305-1G-4S+IN** | Marvell-98DX3236 | ARM 2-core 800MHz | 512 MB | 1x 10/100/1000M Ethernet  4x 10G SFP+ |  | 128 | up to 16K | 10218 |
| **CRS305-1G-4S+OUT (FiberBox Plus)** | Marvell-98DX226S | ARM 2-core 800MHz | 256 MB | 1x 10/100/1000M Ethernet  4x 10G SFP+ |  | 128 | up to 16K | 10218 |
| **CRS309-1G-8S+IN** | Marvell-98DX8208 | ARM 2-core 800MHz | 512 MB | 1x 10/100/1000M Ethernet  8x 10G SFP+ |  | 1024 | up to 32K | 10218 |
| **CRS317-1G-16S+RM** | Marvell-98DX8216 | ARM 2-core 800MHz | 1 GB | 1x 10/100/1000M Ethernet  16x 10G SFP+ |  | 1024 | up to 128K | 10218 |
| **CRS312-4C+8XG-RM** | Marvell-98DX8212 | MIPSBE 1-core 650MHz | 64 MB | 4x 10G combo  8x 1/2.5/5/10G Ethernet |  | 512 | up to 32K | 10218 |
| **CRS326-24S+2Q+RM** | Marvell-98DX8332 | MIPSBE 1-core 650MHz | 128 MB | 24x 10G SFP+  2x 40G QSFP+ |  | 256 | up to 32K | 10218 |
| **CRS326-4C+20G+2Q+RM** | Marvell-98DX8332 | MIPSBE 1-core 650MHz | 128 MB | 4x 2.5G Ethernet/10G SFP+ combo  20x 2.5G Ethernet  2x 40G QSFP+ |  | 256 | up to 32K | 10218 |
| **CRS354-48G-4S+2Q+RM** | Marvell-98DX3257 | MIPSBE 1-core 650MHz | 128 MB | 48x 10/100/1000M Ethernet  4x 10G SFP+  2x 40G QSFP+ |  | 170 | up to 32K | 10218 |
| **CRS354-48P-4S+2Q+RM** | Marvell-98DX3257 | MIPSBE 1-core 650MHz | 128 MB | 48x 10/100/1000M Ethernet  4x 10G SFP+  2x 40G QSFP+ | 48x 802.3af/at | 170 | up to 32K | 10218 |
| **CRS418-8P-8G-2S+RM**  **CRS418-8P-8G-2S+5axQ2axQ-RM** | Marvell-98DX226S | ARM64 4-core 2208MHz | 1 GB | 16x 10/100/1000M Ethernet  2x 10G SFP+ | 8x 802.3af/at | 128 | up to 16K | 10218 |
| **CRS504-4XQ (IN/OUT)** | Marvell-98DX4310 | MIPSBE 1-core 650MHz | 64 MB | 4x 100G QSFP28 |  | 1024 | up to 128K | 10218 |
| **CRS510-8XS-2XQ-IN** | Marvell-98DX4310 | MIPSBE 1-core 650MHz | 128 MB | 8x 25G SFP28  2x 100G QSFP28 |  | 1024 | up to 128K | 10218 |
| **CRS518-16XS-2XQ-RM** | Marvell-98DX8525 | MIPSBE 1-core 650MHz | 64 MB | 16x 25G SFP28  2x 100G QSFP28 |  | 1024 | up to 128K | 10218 |
| **CRS520-4XS-16XQ-RM** | Marvell-98CX8410 | ARM64 4-core 2000MHz | 4 GB | 4x 25G SFP28  16x 100G QSFP28 |  | 682 | up to 256K | 9570 |
| **CRS812-8DS-2DQ-2DDQ-RM** | Marvell-98DX7335 | ARM64 4-core 2000MHz | 4 GB | 8x 50G SFP56  2x 200G QSFP56  2x 400G QSFP56-DD |  | 1365 | up to 128K | 9570 |
| **CRS804-4DDQ-hRM** | Marvell-98DX7335 | ARM64 4-core 2000MHz | 4 GB | 4x 400G QSFP56-DD |  | 1365 | up to 128K | 9570 |
| **CCR2116-12G-4S+** | Marvell-98DX3255 | ARM64 16-core 2000MHz | 16 GB | 12x 10/100/1000M Ethernet  4x 10G SFP+ |  | 512 | up to 32K | 9570 |
| **CCR2216-1G-12XS-2XQ** | Marvell-98DX8525 | ARM64 16-core 2000MHz | 16 GB | 12x 25G SFP28  2x 100G QSFP28 |  | 1024 | up to 128K | 9570 |
| **RDS2216-2XG-4S+4XS-2XQ** | Marvell-98DX4310 | ARM64 16-core 2000MHz | 32 GB | 2x 1/2.5/5/10G Ethernet  4x 10G SFP+  4x 25G SFP28  2x 100G QSFP28 |  | 1024 | up to 128K | 9570 |

</WideTable>

### Abbreviations

- FDB - Forwarding Database.
- MDB - Multicast Database.
- SVL - Shared VLAN Learning.
- IVL - Independent VLAN Learning.
- PVID - Port VLAN ID.
- ACL - Access Control List.
- CVID - Customer VLAN ID.
- SVID - Service VLAN ID.

## Port switching

---

In order to set up port switching, check the [Bridge Hardware Offloading](index.md#bridge-hardware-offloading) page.

:::danger
Currently, it is possible to create only one bridge with hardware offloading. Use the `hw=yes/no` parameter to select which bridge will use hardware offloading.
:::

:::warning
Bridge STP/RSTP/MSTP, IGMP Snooping, and VLAN filtering settings don't affect hardware offloading. Since RouterOS v6.42, Bonding interfaces are also hardware offloaded.
:::

## VLAN

---

Since RouterOS version 6.41, a bridge provides VLAN aware Layer2 forwarding and VLAN tag modifications within the bridge. This set of features makes bridge operation more like a traditional Ethernet switch and allows overcoming Spanning Tree compatibility issues compared to the configuration when tunnel-like VLAN interfaces are bridged. Bridge VLAN Filtering configuration is highly recommended to comply with STP (802.1D), RSTP (802.1w) standards, and it is mandatory to enable MSTP (802.1s) support in RouterOS.

### VLAN Filtering

Detailed architectural concepts and configuration steps are covered in the main [Bridge VLAN Filtering](index.md#bridge-vlan-filtering) section.

#### Supported VLAN Implementations

Depending on your network design, you can implement several hardware-offloaded VLAN topologies:

- **Port-Based VLAN:** See the step-by-step configuration guide in the [Bridge VLAN Filtering](index.md#bridge-vlan-filtering) section.
- **Protocol-Based VLAN:** Configured via the switch rule table to map specific network protocols.
- **MAC-Based VLAN:** Maps specific source MAC addresses to a designated VLAN ID.

---

### MAC-Based VLAN Configuration

:::warning Hardware & Forwarding Restrictions

- **Rule Capacity:** This functionality utilizes the hardware Switch Rule table. Refer to the [Switch Chip Model Capacity Table](./marvell-prestera-switch-chip-features.md#models) to verify how many rules your specific device supports.
- **CPU Forwarding Limitation:** MAC-based VLANs apply strictly to traffic switched between hardware ports. If a packet is routed or forwarded to the CPU, the bridge port's default `pvid` is enforced instead of the `new-vlan-id` action defined in your ACL rules.
- **DHCP Conflict:** MAC-based VLAN matching will fail to process DHCP packets if `dhcp-snooping=yes` is enabled on the bridge.
:::

#### Configuration Example

Enable switching on ports by creating a bridge with enabled hw-offloading:

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
```

Add VLANs in the Bridge VLAN table and specify ports:

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 untagged=ether7 vlan-ids=200,300,400
```

Add Switch rules which assign VLAN id based on MAC address:

```ros
/interface/ethernet/switch/rule
add switch=switch1 ports=ether7 src-mac-address=A4:12:6D:77:94:43/FF:FF:FF:FF:FF:FF new-vlan-id=200
add switch=switch1 ports=ether7 src-mac-address=84:37:62:DF:04:20/FF:FF:FF:FF:FF:FF new-vlan-id=300
add switch=switch1 ports=ether7 src-mac-address=E7:16:34:A1:CD:18/FF:FF:FF:FF:FF:FF new-vlan-id=400
```

#### Protocol Based VLAN

:::warning

- The Switch Rule table is used for Protocol Based VLAN functionality, see [this table](./marvell-prestera-switch-chip-features.md#models) on how many rules each device supports.
- Protocol-based VLANs will only work properly between switch ports and not between switch ports and CPU. When a packet is being forwarded to the CPU, the `pvid` property for the bridge port will always be used instead of `new-vlan-id` from ACL rules.
- Protocol-based VLANs will not work for DHCP packets when DHCP snooping is enabled.

:::

Enable switching on ports by creating a bridge with enabled hw-offloading:

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

Add VLANs in the Bridge VLAN table and specify ports:

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 untagged=ether6 vlan-ids=200
add bridge=bridge1 tagged=ether2 untagged=ether7 vlan-ids=300
add bridge=bridge1 tagged=ether2 untagged=ether8 vlan-ids=400
```

Add Switch rules which assign VLAN ID based on MAC protocol:

```ros
/interface/ethernet/switch/rule
add mac-protocol=ip new-vlan-id=200 ports=ether6 switch=switch1
add mac-protocol=ipx new-vlan-id=300 ports=ether7 switch=switch1
add mac-protocol=0x80F3 new-vlan-id=400 ports=ether8 switch=switch1
```

#### VLAN Tunneling (Q-in-Q)

Since RouterOS v6.43, it is possible to use a provider bridge (IEEE 802.1ad) and Tag Stacking VLAN filtering, and hardware offloading at the same time. The configuration is described in the [Bridge VLAN Tunneling (Q-in-Q)](vlan.md#q-in-q) section.

:::danger
Devices with the switch chip Marvell-98DX3257 (e.g. CRS354 series) do not support VLAN filtering on 1Gbps Ethernet interfaces for other VLAN types (`0x88a8` and `0x9100`).
:::

### Ingress VLAN translation

It is possible to translate a certain VLAN ID to a different VLAN ID using ACL rules on an ingress port. In this example we create two ACL rules, allowing bidirectional communication. This can be done by doing the following.

Create a new bridge and add ports to it with hardware offloading:

```ros
/interface/bridge
add name=bridge1 vlan-filtering=no
/interface/bridge/port
add interface=ether1 bridge=bridge1 hw=yes
add interface=ether2 bridge=bridge1 hw=yes
```

Add ACL rules to translate a VLAN ID in each direction:

```ros
/interface/ethernet/switch/rule
add new-dst-ports=ether2 new-vlan-id=20 ports=ether1 switch=switch1 vlan-id=10
add new-dst-ports=ether1 new-vlan-id=10 ports=ether2 switch=switch1 vlan-id=20
```

Add both VLAN IDs to the bridge VLAN table:

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 vlan-ids=10
add bridge=bridge1 tagged=ether2 vlan-ids=20
```

Enable bridge VLAN filtering:

```ros
/interface/bridge/set bridge1 vlan-filtering=yes
```

:::warning
Bidirectional communication is limited only between two switch ports. Translating VLAN ID between more ports can cause traffic flooding or incorrect forwarding between the same VLAN ports.

**Caution:** By enabling `vlan-filtering` you will be filtering out traffic destined to the CPU. Before enabling VLAN filtering you should make sure that you set up a [Management port](index.md#management-access-configuration).
:::

## (R/M)STP

---

MikroTik devices with a Marvell Prestera switch are capable of running STP, RSTP, and MSTP on a hardware level. For more detailed information, you should check out the [Spanning Tree Protocol](./user-guides/spanning-tree-protocol.md) manual page and for relevant configuration/monitoring options see the [Bridging and Switching](./) page.

## Bonding

---

MikroTik devices with Marvell Prestera switch support hardware offloading with bonding interfaces. Only `802.3ad` (LACP), `balance-xor` (static LAG) and `active-backup` bonding modes are hardware offloaded; other bonding modes will use the CPU's resources. You can find more information about the bonding interfaces in the [Bonding Interface](../high-availability-solutions/bonding.md) section.

To create a hardware offloaded bonding interface, you must create a bonding interface with a supported bonding mode:

```ros
/interface/bonding
add mode=802.3ad name=bond1 slaves=ether1,ether2
```

This interface can be added to a bridge alongside other interfaces:

```ros
/interface/bridge
add name=bridge
/interface/bridge/port
add bridge=bridge interface=bond1 hw=yes
add bridge=bridge interface=ether3 hw=yes
add bridge=bridge interface=ether4 hw=yes
```

:::warning
Do not add interfaces to a bridge that are already in a bond, RouterOS will not allow you to add an interface to a bridge that is already a slave port for bonding.
:::

Make sure that the bonding interface is hardware offloaded by checking the "H" flag:

```text
/interface/bridge/port/print 
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE                                 BRIDGE                                 HW
 0   H bond1                                     bridge                                 yes
 1   H ether3                                    bridge                                 yes
 2   H ether4                                    bridge                                 yes
```

:::warning
With HW-offloaded bonding interfaces, the built-in switch chip will always use Layer2+Layer3+Layer4 for a transmit hash policy; changing the transmit hash policy manually will have no effect.
:::

### Configuration example - VLANs with bonds

This section will show how to configure multiple switches to use bonding interfaces and port-based VLANs, and it will also show a working example with a DHCP-Server, inter-VLAN routing, management IP, and invalid VLAN filtering configuration.

For this network topology, we will be using two CRS326-24G-2S+, one CRS317-1G-16S+, and one CCR1072-1G-8S+.

![CRS3xx VLANs with Bonds](./img/marvell-prestera-switch-chip-features-01.webp)

In this setup, SwitchA and SwitchC will tag all traffic from ports ether1-ether8 to VLAN ID 10, ether9-ether16 to VLAN ID 20, and ether17-ether24 to VLAN ID 30. Management will only be possible if a user is connecting with tagged traffic with VLAN ID 99 from ether1 on SwitchA or SwitchB. Connecting to all devices will also be possible from the router using tagged traffic with VLAN ID 99. The SFP+ ports in this setup are going to be used as VLAN trunk ports while being in a bond to create a LAG interface.

#### Configure bonding

Bonding interfaces are used when a larger amount of bandwidth is required. This is done by creating a link aggregation group, which also provides hardware automatic failover and load balancing for switches. By adding two 10Gbps interfaces to bonding, you can increase the theoretical bandwidth limit to 20Gbps. Make sure that all bonded interfaces are linked to the same speed rates.

:::info
When using the hardware-offloaded bridge, the switch aggregates traffic using the built-in switch chip without using CPU resources.
:::

To create a 20Gbps bonding interface from sfp-sfpplus1 and sfp-sfpplus2 between SwitchA and SwitchB and between SwitchC and SwitchB, use these commands on **SwitchA** and **SwitchC**:

```ros
/interface/bonding
add mode=802.3ad name=bond_1-2 slaves=sfp-sfpplus1,sfp-sfpplus2
```

To create a 40Gbps bonding interface between SwitchB and the Router and a 20Gbps bonding interface between SwitchA and SwitchC, use these commands on **SwitchB**:

```ros
/interface/bonding
add mode=802.3ad name=bond_1-2 slaves=sfp-sfpplus1,sfp-sfpplus2
add mode=802.3ad name=bond_3-4 slaves=sfp-sfpplus3,sfp-sfpplus4
add mode=802.3ad name=bond_5-6-7-8 slaves=sfp-sfpplus5,sfp-sfpplus6,sfp-sfpplus7,sfp-sfpplus8
```

In our case the Router needs a software-based bonding interface. Use these commands on the **Router**:

```ros
/interface/bonding
add mode=802.3ad name=bond_1-2-3-4 slaves=sfp-sfpplus1,sfp-sfpplus2,sfp-sfpplus3,sfp-sfpplus4
```

:::info
Interface bonding does not create an interface with a larger link speed. Interface bonding creates a virtual interface that can load balance traffic over multiple interfaces. More details can be found on the [LAG interfaces and load balancing](./user-guides/layer2-misconfiguration.md#lag-interfaces-and-load-balancing) page.
:::

#### Configure port switching

All switches in this setup require that all used ports are switched together. For bonding, you should add the bonding interface as a bridge port, instead of individual bonding ports. Use these commands on **SwitchA** and **SwitchC**:

```ros
/interface/bridge
add name=bridge vlan-filtering=no
/interface/bridge/port
add bridge=bridge interface=ether1 pvid=10
add bridge=bridge interface=ether2 pvid=10
add bridge=bridge interface=ether3 pvid=10
add bridge=bridge interface=ether4 pvid=10
add bridge=bridge interface=ether5 pvid=10
add bridge=bridge interface=ether6 pvid=10
add bridge=bridge interface=ether7 pvid=10
add bridge=bridge interface=ether8 pvid=10
add bridge=bridge interface=ether9 pvid=20
add bridge=bridge interface=ether10 pvid=20
add bridge=bridge interface=ether11 pvid=20
add bridge=bridge interface=ether12 pvid=20
add bridge=bridge interface=ether13 pvid=20
add bridge=bridge interface=ether14 pvid=20
add bridge=bridge interface=ether15 pvid=20
add bridge=bridge interface=ether16 pvid=20
add bridge=bridge interface=ether17 pvid=30
add bridge=bridge interface=ether18 pvid=30
add bridge=bridge interface=ether19 pvid=30
add bridge=bridge interface=ether20 pvid=30
add bridge=bridge interface=ether21 pvid=30
add bridge=bridge interface=ether22 pvid=30
add bridge=bridge interface=ether23 pvid=30
add bridge=bridge interface=ether24 pvid=30
add bridge=bridge interface=bond_1-2
```

Add all bonding interfaces to a single bridge on SwitchB by using these commands on **SwitchB**:

```ros
/interface/bridge
add name=bridge vlan-filtering=no
/interface/bridge/port
add bridge=bridge interface=bond_1-2
add bridge=bridge interface=bond_3-4
add bridge=bridge interface=bond_5-6-7-8
```

#### Configure management IP

It is very useful to create a management interface and assign an IP address to it to preserve access to the switch. This is also very useful when updating your switches since such traffic to the switch will be blocked when enabling invalid VLAN filtering.

Create a routable VLAN interface on **SwitchA**, **SwitchB,** and **SwitchC**:

```ros
/interface/vlan
add interface=bridge name=MGMT vlan-id=99
```

The Router needs a routable VLAN interface to be created on the bonding interface. Use these commands to create a VLAN interface on the **Router**:

```ros
/interface/vlan
add interface=bond_1-2-3-4 name=MGMT vlan-id=99
```

For this guide, we are going to use these addresses for each device:

| Device | Address |
| :-- | :-- |
| Router | 192.168.99.1 |
| SwitchA | 192.168.99.2 |
| SwitchB | 192.168.99.3 |
| SwitchC | 192.168.99.4 |

Add an IP address for each switch device on the VLAN interface (change X to the appropriate number):

```ros
/ip/address
add address=192.168.99.X/24 interface=MGMT
```

Do not forget to add the default gateway and specify a DNS server on the switch devices:

```ros
/ip/route
add gateway=192.168.99.1
/ip/dns
set servers=192.168.99.1
```

Add the IP address on the **Router**:

```ros
/ip/address
add address=192.168.99.1/24 interface=MGMT
```

#### Configure invalid VLAN filtering

Since most ports on SwitchA and SwitchC are going to be access ports, you can set all ports to accept only certain types of packets, in this case, we will want SwitchA and SwitchC to only accept untagged packets. Use these commands on **SwitchA** and **SwitchC**:

```ros
/interface/bridge/port
set [ find ] frame-types=admit-only-untagged-and-priority-tagged
```

There is an exception for frame types on SwitchA and SwitchC. In this setup, access to the management is required from ether1 and bonding interfaces. They require that tagged traffic can be forwarded. Use these commands on **SwitchA** and **SwitchC**:

```ros
/interface/bridge/port
set [find where interface=ether1] frame-types=admit-all
set [find where interface=bond_1-2] frame-types=admit-only-vlan-tagged
```

On SwitchB only tagged packets should be forwarded, use these commands on **SwitchB**:

```ros
/interface/bridge/port
set [ find ] frame-types=admit-only-vlan-tagged
```

An optional step is to set `frame-types=admit-only-vlan-tagged` on the bridge interface to disable the default untagged VLAN 1 (`pvid=1`). We are using the tagged VLAN on the bridge for management access, so there is no need to accept untagged traffic on the bridge. Use these commands on **SwitchA**, **SwitchB** and **SwitchC**:

```ros
/interface/bridge/set [find name=bridge] frame-types=admit-only-vlan-tagged
```

It is required to set up a bridge VLAN table. In this network setup, we need to allow VLAN 10 on ether1-ether8, VLAN 20 on ether9-ether16, VLAN 30 on ether17-ether24, VLAN 10,20,30,99 on bond\_1-2, and a special case for ether1 to allow forwarding of VLAN 99 on SwitchA and SwitchC. Use these commands on **SwitchA** and **SwitchC**:

```ros
/interface/bridge/vlan
add bridge=bridge tagged=bond_1-2 vlan-ids=10
add bridge=bridge tagged=bond_1-2 vlan-ids=20
add bridge=bridge tagged=bond_1-2 vlan-ids=30
add bridge=bridge tagged=bridge,bond_1-2,ether1 vlan-ids=99
```

:::warning
Bridge ports with `frame-types` set to `admit-all` or `admit-only-untagged-and-priority-tagged` will be automatically added as untagged ports for the `pvid` VLAN.
:::

Similarly, it is required to set up a bridge VLAN table for SwitchB. Use these commands on **SwitchB**:

```ros
/interface/bridge/vlan
add bridge=bridge tagged=bond_1-2,bond_3-4,bond_5-6-7-8 vlan-ids=10,20,30
add bridge=bridge tagged=bond_1-2,bond_3-4,bond_5-6-7-8,bridge vlan-ids=99
```

When everything is configured, VLAN filtering can be enabled. Use these commands on **SwitchA**, **SwitchB,** and **SwitchC**:

```ros
/interface/bridge
set bridge vlan-filtering=yes
```

:::danger
Double-check if port-based VLANs are set up properly. If a mistake is made, you might lose access to the switch, and connectivity can only be regained by resetting the configuration or by using the serial console.
:::

:::note
VLAN filtering is described in greater detail in the [Bridge VLAN Filtering](index.md#bridge-vlan-filtering) section.
:::

#### Configure InterVLAN routing

To create InterVLAN routing, the VLAN interface for each customer VLAN ID must be created on the router and must have an IP address assigned to it. The VLAN interface must be created on the bonding interface created previously.

Use these commands on the **Router**:

```ros
/interface/vlan
add interface=bond_1-2-3-4 name=VLAN10 vlan-id=10
add interface=bond_1-2-3-4 name=VLAN20 vlan-id=20
add interface=bond_1-2-3-4 name=VLAN30 vlan-id=30
/ip/address
add address=192.168.10.1/24 interface=VLAN10
add address=192.168.20.1/24 interface=VLAN20
add address=192.168.30.1/24 interface=VLAN30
```

:::info
These commands are required for a DHCP Server setup. If inter-VLAN routing is not desired but a DHCP Server on a single router is required, use [Firewall Filter](../firewall-and-quality-of-service/firewall/filter.md) rules to block communication between different subnets.
:::

:::note
Since RouterOS v7, it is possible to route traffic using L3 HW offloading on supported hardware. See more details in the [L3 Hardware Offloading](./l3-hardware-offloading.md) section.
:::

#### Configure DHCP server

To get the DHCP-Server working for each VLAN ID, the server must be set up on the previously created VLAN interfaces (one server for each VLAN ID). Preferably, each VLAN ID should have its own subnet and its own IP pool. A DNS Server could be specified as the router's IP address for a particular VLAN ID, or a global DNS Server could be used, but this address must be reachable.

To set up the DHCP-Server, use these commands on the **Router**:

```ros
/ip/pool
add name=VLAN10_POOL ranges=192.168.10.100-192.168.10.200
add name=VLAN20_POOL ranges=192.168.20.100-192.168.20.200
add name=VLAN30_POOL ranges=192.168.30.100-192.168.30.200
/ip/dhcp-server
add address-pool=VLAN10_POOL disabled=no interface=VLAN10 name=VLAN10_DHCP
add address-pool=VLAN20_POOL disabled=no interface=VLAN20 name=VLAN20_DHCP
add address-pool=VLAN30_POOL disabled=no interface=VLAN30 name=VLAN30_DHCP
/ip/dhcp-server/network
add address=192.168.10.0/24 dns-server=192.168.10.1 gateway=192.168.10.1
add address=192.168.20.0/24 dns-server=192.168.20.1 gateway=192.168.20.1
add address=192.168.30.0/24 dns-server=192.168.30.1 gateway=192.168.30.1
```

In case the router's DNS Server is being used, don't forget to allow remote requests and make sure DNS Servers are configured on the router. Use these commands on the **Router**:

```ros
/ip/dns
set allow-remote-requests=yes servers=8.8.8.8
```

:::danger
Make sure to secure your local DNS Server with Firewall from the outside when using `allow-remote-requests` set to `yes` since your DNS Server can be used for DDoS attacks if it is accessible from the Internet by anyone.
:::

Don't forget to create NAT, assuming that sfp-sfpplus8 is used as a WAN port, use these commands on the **Router**:

```ros
/ip/firewall/nat
add action=masquerade chain=srcnat out-interface=sfp-sfpplus8
```

#### Configure jumbo frames

One can increase the total throughput in such a setup by enabling jumbo frames. This reduces the packet overhead by increasing the Maximum Transmission Unit (MTU). If a device in your network does not support jumbo frames, then it will not benefit from a larger MTU. Usually, the whole network does not support jumbo frames, but you can still benefit when sending data between devices that support jumbo frames, including all switches in the path.

In this case, if clients behind SwitchA and the client behind SwitchC support jumbo frames, then enabling jumbo frames will be beneficial. Before enabling jumbo frames, determine the MAX-L2MTU by using this command:

```ros
[admin@SwitchA] > interface print 
Flags: R - RUNNING
Columns: NAME, TYPE, ACTUAL-MTU, L2MTU, MAX-L2MTU, MAC-ADDRESS
 #   NAME           TYPE   ACTUAL-MTU  L2MTU  MAX-L2MTU  MAC-ADDRESS      
 1 R sfp-sfpplus1   ether        1500   1584      10218  64:D1:54:FF:E3:7F

```

:::info
More information can be found in the [MTU manual](../hardware/mtu-in-routeros.md) page.
:::

When MAX-L2MTU is determined, choose the MTU size depending on the traffic on your network, and use this command on **SwitchA**, **SwitchB,** and **SwitchC**:

```ros
/interface/ethernet
set [ find ] l2mtu=10218 mtu=10218
```

:::info
Don't forget to change the MTU on your client devices too, otherwise, the above-mentioned settings will not have any effect.
:::

## Multi-chassis Link Aggregation Group

---

MLAG (Multi-chassis Link Aggregation Group) implementation in RouterOS allows configuring LACP bonds on two separate devices, while the client device believes it is connected to the same machine. This provides a physical redundancy in case of switch failure. MikroTik devices with a Marvell Prestera switch can be configured with hardware offloaded MLAG. Read [here](../high-availability-solutions/multi-chassis-link-aggregation-group.md) for more information.

## L3 Hardware Offloading

---

Layer3 hardware offloading (otherwise known as IP switching or HW routing) will allow offloading some of the router features onto the switch chip. This allows reaching wire speeds when routing packets, which simply would not be possible with the CPU.

Offloaded feature set depends on the used chipset. Read [here](./l3-hardware-offloading.md) for more info.

## Port isolation

---

Since RouterOS v6.43 it is possible to create a Private VLAN setup, an example can be found in the [Switch chip port isolation](./switch-chip-features.md#port-isolation) manual page. Hardware offloaded bonding interfaces are not included in the switch port-isolation menu, but it is still possible to configure port-isolation individually on each secondary interface of the bonding.

:::warning
Port isolation can be used with vlan-filtering bridge and it is possible to isolate ports that are members of the same VLAN. The isolation works per-port; it is not possible to isolate ports per-VLAN.
:::

## IGMP/MLD Snooping

---

MikroTik devices with Marvell Prestera switch are capable of using IGMP/MLD Snooping on a hardware level. To see more detailed information, you should check out the [IGMP/MLD snooping](./user-guides/bridge-igmp-mld-snooping.md) manual page.

## DHCP Snooping and DHCP Option 82

---

MikroTik devices with a Marvell Prestera switch are capable of using DHCP Snooping with custom Option 82 (Circuit ID, Remote ID) on a hardware level. The switch will create a dynamic ACL rule to capture the DHCP packets and redirect them to the main CPU for further processing. To see more detailed information, please visit the [DHCP Snooping and DHCP Option 82](index.md#dhcp-snooping-and-dhcp-option-82) manual page.

:::info
Starting from RouterOS v7.17, DHCP snooping is supported with hardware offloading bonding interfaces.
:::

## DHCPv6 Snooping and DHCP Option 18, Option 37

---

MikroTik devices with Marvell Prestera switch are capable of using DHCPv6 Snooping with custom Option 18 (Interface ID) and Option 37 (Remote ID) on a hardware level since RouterOS v7.23. The switch will create a dynamic ACL rule to capture the DHCPv6 packets and redirect them to the main CPU for further processing. To see more detailed information, please visit the [DHCPv6 Snooping / DHCPv6 Shield](./#dhcpv6-snooping--dhcpv6-shield) manual page.

## RA Guard

---

MikroTik devices with a Marvell Prestera switch are capable of using RA Guard on a hardware level since RouterOS v7.22. The switch will create a dynamic ACL rule to capture the relevant IPv6 packets and redirect them to the main CPU for further processing. To see more detailed information, please visit the [RA Guard](./#ra-guard) manual page.

## Mirroring

---

Mirroring is a function that allows a network switch to duplicate all the data passing through it and send a copy to another specified port, known as the `mirror-target`. This feature is useful for setting up a tap device, which allows for analyzing network traffic using a separate device. You can set up mirroring in a simple way by designating source ports (see `mirror-egress` and `mirror-ingress` in `/interface/ethernet/switch/port`), or you can configure more advanced mirroring based on different criteria (see `mirror` in `/interface/ethernet/switch/rule`).

It is important to note that the `mirror-target` port must be on the same switch. You can check the device block diagram or navigate to the `/interface/ethernet` menu to identify which interfaces are connected where. When setting up the configuration, it is not mandatory to add the `mirror-target` interface to the same hardware offloaded bridge where the source ports are set up. The `mirror-target` port can be a standalone interface (not configured as a bridge port), or it can be within a bridge setup. When using the `mirror-target` with a bridge, note that data and mirrored traffic may both travel on the same LAN. In such cases, consider employing RSPAN (Remote Switch Port Analyzer), where mirrored traffic is encapsulated into a separate VLAN before being transmitted over the network.

Additionally, you can set the `mirror-target` port to a special value "cpu", which means that the copied packets will be sent to the switch chip's CPU port.

### Configuration examples

---

#### Port Based Mirroring

Starting from RouterOS version 7.15, it is possible to configure multiple source ports and selectively choose whether to mirror incoming traffic, outgoing traffic, or both. In this example, both incoming and outgoing traffic from the **ether2** interface will be copied and sent to the **ether3** interface for monitoring or analysis.

```ros
# Since RouterOS v7.15
/interface/ethernet/switch/port
set ether2 mirror-egress=yes mirror-ingress=yes
/interface/ethernet/switch
set switch1 mirror-target=ether3

# Older RouterOS:
/interface/ethernet/switch
set switch1 mirror-source=ether2 mirror-target=ether3
```

#### VLAN Based Mirroring

Using ACL rules, it is possible to mirror packets from multiple interfaces using the `ports` setting. Additionally, you can specify more detailed criteria such as VLAN ID, MAC/IP address or TCP/UDP port. Only **ingress** packets are mirrored to the `mirror-target` interface. This example will mirror incoming VLAN 11 traffic from the **ether2** interface, and send copies to the **ether3** interface. To use an ACL rule with a `vlan-id` matcher, you need to have [bridge vlan-filtering](index.md#bridge-vlan-filtering) enabled.

```ros
/interface/bridge
set bridge1 vlan-filtering=yes
/interface/ethernet/switch
set switch1 mirror-target=ether3
/interface/ethernet/switch/rule
add mirror=yes ports=ether1 switch=switch1 vlan-id=11
```

#### MAC Based Mirroring

This example will mirror incoming traffic with 64:D1:54:D9:27:E6 MAC destination or source address from the **ether1** interface, and send copies to the **ether3** interface.

```ros
/interface/ethernet/switch
set switch1 mirror-target=ether3
/interface/ethernet/switch/rule
add mirror=yes ports=ether1 switch=switch1 dst-mac-address=64:D1:54:D9:27:E6/FF:FF:FF:FF:FF:FF
add mirror=yes ports=ether1 switch=switch1 src-mac-address=64:D1:54:D9:27:E6/FF:FF:FF:FF:FF:FF
```

#### IP Based Mirroring

This example will mirror incoming traffic with IP destination or source address 192.168.88.0/24 from the **ether1** interface, and send copies to the **ether3** interface.

```ros
/interface/ethernet/switch
set switch1 mirror-target=ether3 mirror-source=none
/interface/ethernet/switch/rule
add mirror=yes ports=ether1 switch=switch1 src-address=192.168.88.0/24
add mirror=yes ports=ether1 switch=switch1 dst-address=192.168.88.0/24
```

There are other options as well, check the [ACL section](./marvell-prestera-switch-chip-features.md#switch-rules-acl) to find out all possible parameters that can be used to match packets.

#### Remote Switch Port Analyzer

This example will mirror incoming and outgoing traffic from the **ether2** interface, copies will be encapsulated in 802.1Q VLAN using the 999 as VLAN ID, and packets will be sent to the **ether3** interface. If the original traffic is already VLAN tagged, RSPAN will add another layer of VLAN tagging as an outer tag. This results in the mirrored traffic being tagged twice. If the `mirror-target` port is included in a vlan-filtering bridge, it is not required to make the interface a tagged VLAN member under the `/interface/bridge/vlan` menu for the RSPAN.

```ros
/interface/ethernet/switch/port
set ether2 mirror-egress=yes mirror-ingress=yes
/interface/ethernet/switch
set switch1 mirror-target=ether3 rspan=yes rspan-egress-vlan-id=999 rspan-ingress-vlan-id=999
```

### Property Reference

**Sub-menu:** `/interface/ethernet/switch`

| Property | Description |
| :-- | :-- |
| **mirror-target** (*cpu \| name \| none*; Default: **none**) | Selects a single mirroring target port. Packets from `mirror-egress` and `mirror-ingress` (`/interface/ethernet/switch/port`) and mirror (`/interface/ethernet/switch/rule`) will be sent to the selected port. |
| **rspan** (*no \| yes*; Default: **no**) | Enables the Remote Switch Port Analyzer (RSPAN) feature on `mirror-target`. Traffic marked for ingress or egress mirroring is carried over a specified remote analyzer VLAN - `rspan-egress-vlan-id` and `rspan-ingress-vlan-id`. |
| **rspan-egress-vlan-id** (*integer: 1..4095*; Default: **1**) | Selects the VLAN ID for marked egress traffic. Only applies when `rspan` is enabled. |
| **rspan-ingress-vlan-id** (*integer: 1..4095*; Default: **1**) | Selects the VLAN ID for marked ingress traffic. Only applies when `rspan` is enabled. |

**Sub-menu:** `/interface/ethernet/switch/port`

| Property | Description |
| :-- | :-- |
| **mirror-egress** (*no \| yes*; Default: **no**) | Whether to send an egress packet copy to the `mirror-target` port. |
| **mirror-ingress** (*no \| yes*; Default: **no**) | Whether to send an ingress packet copy to the `mirror-target` port. |

**Sub-menu:** `/interface/ethernet/switch/rule`

| Property | Description |
| :-- | :-- |
| **mirror** (*no \| yes*; Default: **no**) | Whether to send a packet copy to `mirror-target` port. |

## Traffic Shaping

---

It is possible to limit ingress traffic that matches certain parameters with ACL rules and it is possible to limit ingress/egress traffic per port basis. The policer is used for ingress traffic, the shaper is used for egress traffic. The ingress policer controls the received traffic with packet drops. Everything that exceeds the defined limit will get dropped. This can affect the TCP congestion control mechanism on end hosts and achieved bandwidth can actually be less than defined. The egress shaper tries to queue packets that exceed the limit instead of dropping them. Eventually, it will also drop packets when the output queue gets full; however, it should allow utilizing the defined throughput better.

### Port-based traffic police and shaper

```ros
/interface/ethernet/switch/port
set ether1 ingress-rate=10M egress-rate=5M
```

### MAC-based traffic policer

```ros
/interface/ethernet/switch/rule
add ports=ether1 switch=switch1 src-mac-address=64:D1:54:D9:27:E6/FF:FF:FF:FF:FF:FF rate=10M
```

### VLAN-based traffic policer

```ros
/interface/bridge
set bridge1 vlan-filtering=yes
/interface/ethernet/switch/rule
add ports=ether1 switch=switch1 vlan-id=11 rate=10M
```

:::danger
By enabling `vlan-filtering` you will be filtering out traffic destined to the CPU. Before enabling VLAN filtering you should make sure that you set up a [Management port](index.md#management-access-configuration).
:::

### Protocol-based traffic policer

```ros
/interface/ethernet/switch/rule
add ports=ether1 switch=switch1 mac-protocol=ipx rate=10M
```

There are other options as well, check the [ACL section](./marvell-prestera-switch-chip-features.md#switch-rules-acl) to find out all possible parameters that can be used to match packets.

:::warning
The Switch Rule table is used for QoS functionality. See [this table](./marvell-prestera-switch-chip-features.md#models) on how many rules each device supports.
:::

:::danger
Due to hardware limitations, the `egress-rate` and `storm-rate` settings do not work correctly on 10Gbps switch ports when they are linked at 10/100Mbps, 1/2.5/5Gbps. This applies to 98DX224S, 98DX226S, 98DX2528, 98DX3236 switch chips.
:::

## Traffic Storm Control

---

Since RouterOS v6.42 it is possible to enable traffic storm control. A traffic storm can emerge when certain frames are continuously flooded on the network. Storm control settings are generally configured on non-uplink ports to restrict incoming storm traffic on those specific ports. This helps safeguard the entire switch and its connected ports by minimizing the impact of traffic storms across the network.

For example, if a network loop has been created and no loop avoidance mechanisms are used (e.g. [Spanning Tree Protocol](./user-guides/spanning-tree-protocol.md)), broadcast or multicast frames can quickly overwhelm the network, causing degraded network performance or even complete network breakdown. Using MikroTik devices with a Marvell Prestera switch, it is possible to limit broadcast, unknown multicast and unknown unicast traffic. Unknown unicast traffic is considered when a switch does not contain a host entry for the destined MAC address. Unknown multicast traffic is considered when a switch does not contain a multicast group entry in the `/interface/bridge/mdb` menu. Storm control settings should be applied to ingress ports; the egress traffic will be limited.

![Traffic Storm](./img/marvell-prestera-switch-chip-features-02.webp)

:::warning
The storm control parameter is specified as a percentage (%) of the link speed. If your link speed is 1Gbps, then specifying `storm-rate` as `10` will allow only 100Mbps of broadcast, unknown multicast and/or unknown unicast traffic to be forwarded.
:::

**Sub-menu:** `/interface/ethernet/switch/port`

| Property | Description |
| :-- | :-- |
| **limit-broadcasts** (*yes \| no*; Default: **yes**) | Limit broadcast traffic on a switch port. |
| **limit-unknown-multicasts** (*yes \| no*; Default: **no**) | Limit unknown multicast traffic on a switch port. |
| **limit-unknown-unicasts** (*yes \| no*; Default: **no**) | Limit unknown unicast traffic on a switch port. |
| **storm-rate** (*integer 0..100*; Default: **100**) | Amount of broadcast, unknown multicast and/or unknown unicast traffic is limited to a percentage of the link speed. |

:::danger
Devices with 98DX224S, 98DX226S, 98DX2528, 98DX3236 switch chip cannot distinguish unknown multicast traffic from all multicast traffic. For example, CRS326-24G-2S+ will limit all multicast traffic when `limit-unknown-multicasts` and `storm-rate` are used. For other devices, for example, CRS317-1G-16S+, the `limit-unknown-multicasts` parameter will limit only unknown multicast traffic (addresses that are not present in `/interface/bridge/mdb).`
:::

For example, to limit 1% (10Mbps) of broadcast and unknown unicast traffic on ether1 (1Gbps), use the following commands:

```ros
/interface/ethernet/switch/port
set ether1 storm-rate=1 limit-broadcasts=yes limit-unknown-unicasts=yes
```

:::warning
Due to hardware limitations, the `egress-rate` and `storm-rate` settings do not work correctly on 10Gbps switch ports when they are linked at 10/100Mbps, 1/2.5/5Gbps. This applies to 98DX224S, 98DX226S, 98DX2528, 98DX3236 switch chips.
:::

## MPLS hardware offloading

---

Since RouterOS v6.41 it is possible to offload certain MPLS functions to the switch chip. The switch must be a (P)rovider router in a PE-P-PE setup in order to achieve hardware offloading. A setup example can be found in the [LDP example setup](../user-guides/routing-and-networking-protocols/mpls/ldp.md#example-setup). The hardware offloading will only take place when LDP interfaces are configured as physical switch interfaces (e.g. Ethernet, SFP, SFP+).

:::warning
Currently only `CRS317-1G-16S+` and `CRS309-1G-8S+` using RouterOS v6.41 and newer are capable of hardware offloading certain MPLS functions. `CRS317-1G-16S+` and `CRS309-1G-8S+` built-in switch chips are not capable of popping MPLS labels from packets, in a PE-P-PE setup you either have to use explicit null or disable TTL propagation in the MPLS network to achieve hardware offloading.

**Caution:** The MPLS hardware offloading has been removed since RouterOS v7.
:::

## Switch Rules (ACL)

---

An Access Control List contains ingress policy engines and egress policy engines. See [this table](./marvell-prestera-switch-chip-features.md#models) on how many rules each device supports. It is an advanced tool for wire-speed packet filtering, forwarding and modifying based on Layer2, Layer3 and Layer4 protocol header field conditions.

ACL rules are checked for each received packet until a match has been found. If there are multiple rules that can match, then only the first rule will be triggered. A rule without any action parameters is a rule to accept the packet.

Enabling features such as IGMP snooping, DHCP snooping, RoMON, PTP, or loop-protect can automatically create dynamic ACL rules. These rules should be considered when adding new ACL entries. Use the `place-before` property when creating a new rule, or the `move` command to adjust the ACL rule order.

:::warning
It is not required to set `mac-protocol` to a certain IP version when using L3 or L4 matchers, however, it is recommended to set the `mac-protocol=ip` or `mac-protocol=ipv6`  when filtering any IP packets.
:::

:::danger
Then switch ACL rules are modified (e.g. added, removed, disabled, enabled, or moved), the existing switch rules will be inactive for a short time. This can cause some packet leakage during the ACL rule modifications.
:::

**Sub-menu:** `/interface/ethernet/switch/rule`

| Property | Description |
| :-- | :-- |
| **copy-to-cpu** (*no \| yes*; Default: **no**) | Clones the matching packet and sends it to the CPU. |
| **disabled** (*yes \| no*; Default: **no**) | Enables or disables the ACL entry. |
| **dscp** (*0..63*) | Matching the DSCP field of the packet (only applies to IPv4 packets). |
| **dst-address** (*IP address/Mask*) | Matching destination IPv4 address and mask. If `mac-protocol=arp` is specified, matches the destination IP in ARP packets. Without `mac-protocol`, matches only IPv4 packets. |
| **dst-address6** (*IPv6 address/Mask*) | Matching destination IPv6 address and mask. |
| **dst-mac-address** (*MAC address/Mask*) | Matching destination MAC address and mask. |
| **dst-port** (*0..65535*) | Matching destination protocol port number (applies to IPv4 and IPv6 packets if `mac-protocol` is not specified). |
| **flow-label** (*0..1048575*) | Matching IPv6 flow label. |
| **mac-protocol** (*802.2 \| arp \| capsman \| dot1x \| homeplug-av \| ip \| ipv6 \| ipx \| lacp \| lldp \| loop-protect \| macsec \| mpls-multicast \| mpls-unicast \| mvrp \| packing-compr \| packing-simple \| pppoe \| pppoe-discovery \| rarp \| romon \| service-vlan \| vlan \| or 0..65535 \| or 0x0000-0xffff*) | Matching a particular MAC protocol specified by protocol name or number |
| **mirror** (*no \| yes*) | Clones the matching packet and sends it to the mirror-target port. |
| **new-dst-ports** (*ports \| bond \| all*) | Changes the destination port to the specified value: If the setting is left empty (e.g. <code>new-dst-ports=""</code>), the packet will be dropped;If a port or  hardware-offloaded bonding interface is specified, the packet will be redirected to that port. Only a single port or bond interface is supported;if you use the <code>all</code> argument, packet will be allowed to pass through to the egress processing without being dropped;If this parameter is not used, the packet will be accepted as is. |
| **new-vlan-id** (*0..4095*) | Changes the VLAN ID to the specified value. Requires `vlan-filtering=yes`. |
| **new-vlan-priority** (*0..7*) | Changes the VLAN priority (priority code point). Requires `vlan-filtering=yes`. |
| **new-vrf** (*vrf name*) | Assigns ingress traffic to a specified VRF. Requires [hardware-offloaded VRF](./l3-hardware-offloading.md#l3hw-feature-support) support on the switch chip. On VRF-unaware switches (98DX3xxx and 98DX2xxx series), setting `new-vrf` to anything other than `main` will be treated as `redirect-to-cpu=yes`. |
| **ports** (*ports \| bond*) | Matching switch interfaces where the rule will apply to incoming traffic. Multiple ports and [hardware-offloaded bonding](./marvell-prestera-switch-chip-features.md#bonding) interfaces can be selected. Note that the `switch1-cpu` port cannot be selected. If `ports` property is left empty, the rule will apply to all switch interfaces. |
| **protocol** (*dccp \| ddp \| egp \| encap \| etherip \| ggp \| gre \| hmp \| icmp \| icmpv6 \| idpr-cmtp \| igmp \| ipencap \| ipip \| ipsec-ah \| ipsec-esp \| ipv6 \| ipv6-frag \| ipv6-nonxt \| ipv6-opts \| ipv6-route \| iso-tp4 \| l2tp \| ospf \| pim \| pup \| rdp \| rspf \| rsvp \| sctp \| st \| tcp \| udp \| udp-lite \| vmtp \| vrrp \| xns-idp \| xtp \| or 0..255*) | Matching a particular IP protocol specified by protocol name or number. Only applies to IPv4 packets if `mac-protocol` is not specified. To match certain IPv6 protocols, use the `mac-protocol=ipv6` setting. |
| **rate** (*0..4294967295*) | Sets ingress traffic limitation (bits per second) for matched traffic. |
| **redirect-to-cpu** (*no \| yes*) | Changes the destination port of a matching packet to the CPU. |
| **src-address** (*IP address/Mask*) | Matching source IPv4 address and mask. If `mac-protocol=arp` is specified, matches the source IP in ARP packets. Without `mac-protocol`, matches only IPv4 packets. |
| **src-address6** (*IPv6 address/Mask*) | Matching source IPv6 address and mask. |
| **src-mac-address** (*MAC address/Mask*) | Matching source MAC address and mask. |
| **src-port** (*0..65535*) | Matching source protocol port number (applies to IPv4 and IPv6 packets if `mac-protocol` is not specified). |
| **switch** (*switch group*) | Matching switch group on which the rule will apply. |
| **traffic-class** (*0..255*) | Matching IPv6 traffic class. |
| **vlan-id** (*0..4095*) | Matching VLAN ID. Requires `vlan-filtering=yes`. |
| **vlan-header** (*not-present \| present*) | Matching VLAN header, whether the VLAN header is present or not. Requires `vlan-filtering=yes`. |
| **vlan-priority** (*0..7*) | Matching VLAN priority (priority code point). |

### Action parameters

- copy-to-cpu
- redirect-to-cpu
- mirror
- new-dst-ports (can be used to drop packets)
- new-vlan-id
- new-vlan-priority
- new-vrf
- rate

### Layer2 condition parameters

- dst-mac-address
- mac-protocol
- src-mac-address
- vlan-id
- vlan-header
- vlan-priority

### Layer3 condition parameters

- dscp
- protocol
- IPv4 conditions:
  - dst-address
  - src-address
- IPv6 conditions:
  - dst-address6
  - flow-label
  - src-address6
  - traffic-class

### Layer4 condition parameters

- dst-port
- src-port

:::warning
For VLAN-related matchers or VLAN-related action parameters to work, you need to enable `vlan-filtering` on the bridge interface and make sure that hardware offloading is enabled on those ports, otherwise, these parameters will not have any effect.
:::
:::warning
When bridge interface `ether-type` is set to `0x8100`, then VLAN-related ACL rules are relevant to frames tagged using regular/customer VLAN (TPID 0x8100); this includes `vlan-id` and `new-vlan-id`. When bridge interface `ether-type` is set to `0x88a8`, then ACL rules are relevant to frames tagged with 802.1ad service tag (TPID 0x88a8).
:::

### Rule counters

Each ACL rule counts the number of packets and bytes it has matched. These counters allow verifying whether a rule is working as expected and how much traffic it handles.

Counters are not displayed by the default `print` command, use `print stats` in the `/interface/ethernet/switch/rule` menu to display them:

```ros
[admin@MikroTik] > /interface/ethernet/switch/rule/print stats
Columns: SWITCH, COPY-TO-CPU, REDIRECT-TO-CPU, BYTES, PACKETS
# SWITCH   COPY-TO-CPU  REDIRECT-TO-CPU  BYTES  PACKETS
;;; count incoming ICMP
0 switch1  yes          no               68716      366
;;; drop ICMP to 192.168.99.1
1 switch1  no           no                   0        0
```

In this example, the first rule has matched 366 packets (68716 bytes), while the second rule has not matched any traffic yet.

Use the `reset-counters` command to clear the counters of selected rules, or `reset-counters [find]` to clear the counters of all rules at once:

```ros
[admin@MikroTik] > /interface/ethernet/switch/rule/reset-counters 0
```

## Port Security

---

It is possible to limit allowed MAC addresses on a single switch port. For example, to allow the 64:D1:54:81:EF:8E MAC address on a switch port, start by switching multiple ports together. In this example, 64:D1:54:81:EF:8E is going to be located behind **ether1**.

Create an ACL rule to allow the given MAC address and drop all other traffic on **ether1** (for ingress traffic):

```ros
/interface/ethernet/switch/rule
add ports=ether1 src-mac-address=64:D1:54:81:EF:8E/FF:FF:FF:FF:FF:FF switch=switch1
add new-dst-ports="" ports=ether1 switch=switch1
```

Egress traffic can still contain information that should not reach devices with unknown MAC addresses.  
Assuming the ports are switched, disable MAC learning and disable unknown unicast flooding on **ether1**:

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1 hw=yes learn=no unknown-unicast-flood=no
add bridge=bridge1 interface=ether2 hw=yes
```

With MAC learning disabled, you need to add a static host entry for 64:D1:54:81:EF:8E (for egress traffic):

```ros
/interface/bridge/host
add bridge=bridge1 interface=ether1 mac-address=64:D1:54:81:EF:8E
```

:::warning
Broadcast and multicast traffic will still be sent out from **ether1**. You can use the `broadcast-flood` and `unknown-multicast-flood` parameters to prevent it. Note that some solutions might depend on these settings, such as streaming protocols and DHCP.
:::

## Dual Boot

---

The “dual boot” feature allows you to choose which operating system you prefer to use on CRS3xx series switches, RouterOS or SwOS. The Device operating system could be changed using:

- Command-line (`/system/routerboard/settings/set boot-os=swos`)
- Winbox
- Webfig
- Serial Console

More details about SwOS are described here: [SwOS manual](https://help.mikrotik.com/docs/display/SWOS/SwOS).

:::warning
To check if a model supports booting into SwOS, refer to the [SwOS Model table](https://help.mikrotik.com/docs/spaces/SWOS/pages/76415036/CRS3xx+and+CSS3xx+series+Manual#CRS3xxandCSS3xxseriesManual-Models) and the product page under Specifications "Operating System".
:::

## Configuring SwOS using RouterOS

---

Since RouterOS 6.43 it is possible to load, save and reset SwOS configuration, as well as upgrade SwOS and set an IP address for the CRS3xx series switches by using RouterOS:

- Save configuration with `/system/swos/save-config`.

:::warning
The configuration will be saved on the same device with `swos.config` as a filename. Make sure you download the file from your device since the configuration file will be removed after a reboot.
:::

- Load configuration with `/system/swos/load-config`.
- Change password with `/system/swos/password`.
- Reset configuration with `/system/swos/reset-config`.
- Upgrade SwOS from RouterOS using `/system/swos/upgrade`.

:::warning
The upgrade command will automatically install the latest available SwOS primary backup version, make sure that your device has access to the Internet in order for the upgrade process to work properly. When the device is booted into SwOS, the version number will include the letter "p", indicating a primary backup version. You can then install the latest available SwOS secondary main version from the SwOS "Upgrade" menu.
:::

:::warning
Starting from RouterOS version 7.17, device-mode restricts SwOS/RouterOS transition for dual-boot; in order to enable: `/system/device-mode/update` routerboard=yes
:::

| Property | Description |
| :-- | :-- |
| **address-acquisition-mode** (*dhcp-only \| dhcp-with-fallback \| static*; Default: **dhcp-with-fallback**) | Changes address acquisition method: dhcp-only - uses only a DHCP client to acquire an address  dhcp-with-fallback - for the first 10 seconds, it will try to acquire an address using a DHCP client. If the request is unsuccessful, then the address falls back to static as defined by the static-ip-address property  static - the address is set as defined by the static-ip-address property |
| **allow-from** (*IP/Mask*; Default: **0.0.0.0/0**) | IP address or a network from which the switch is accessible. By default, the switch is accessible by any IP address. |
| **allow-from-ports** (*name*; Default: ) | List of switch ports from which the device is accessible. By default, all ports are allowed to access the switch |
| **allow-from-vlan** (*integer: 0..4094*; Default: **0**) | VLAN ID from which the device is accessible. By default, all VLANs are allowed |
| **identity** (*name*; Default: **Mikrotik**) | Name of the switch (used for the Mikrotik Neighbor Discovery protocol) |
| **static-ip-address** (*IP*; Default: **192.168.88.1**) | IP address of the switch in case the address-acquisition-mode is either set to dhcp-with-fallback or static. By setting a static IP address, the address acquisition process does not change, which is DHCP with fallback by default. This means that the configured static IP address will become active only when there are going to be no DHCP servers in the same broadcast domain |

## See also

[Basic VLAN switching](./user-guides/basic-vlan-switching.md)

[Bridge Hardware Offloading](index.md#bridge-hardware-offloading)

[L3HW Route Hardware Offloading](./l3-hardware-offloading.md)

[Quality of Service](./quality-of-service.md)

[Spanning Tree Protocol](./user-guides/spanning-tree-protocol.md)

[MTU on RouterBOARD](../hardware/mtu-in-routeros.md)

[Layer2 misconfiguration](./user-guides/layer2-misconfiguration.md)

[Bridge VLAN Table](./user-guides/bridge-vlan-table.md)

[Bridge IGMP/MLD snooping](./user-guides/bridge-igmp-mld-snooping.md)

[Multi-chassis Link Aggregation Group](../high-availability-solutions/multi-chassis-link-aggregation-group.md)
