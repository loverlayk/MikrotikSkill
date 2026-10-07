# Quality of Service

> This documentation introduces Quality of Service (QoS) features in MikroTik RouterOS for devices with Marvell Prestera switch chips, detailing QoS prioritization, traffic shaping, and congestion management. It covers...

# Quality of Service

This document describes **Quality of Service (QoS)** implementation in RouterOS for devices equipped with **[Marvell Prestera switch chips](./marvell-prestera-switch-chip-features.md)**.

QoS is a collection of features in network switches that allows network administrators to prioritize traffic and allocate network resources to ensure that critical data flows smoothly with low latency.

The primary function of QoS in a network switch is to manage traffic in a way that meets the specific requirements of different types of network applications. For example, voice and video data require low latency and minimal packet loss to ensure high-quality communication, while file transfers and other data applications can tolerate higher levels of latency and packet loss.

QoS works by identifying the type of traffic flowing through the switch and assigning it a priority level based on its requirements. The switch then uses this information to modify packet headers and prioritize traffic flow, ensuring that higher-priority traffic receives preferential treatment over lower-priority traffic.

RouterOS v7.15 or later is required to support all QoS features:

1. **QoS Marking.** QoS profile matching by ingress packet header, then egress header modification according to the assigned QoS profile.
2. **QoS Enforcement.** Avoid or resolve congestion based on the assigned QoS profile and traffic shaping.
3. **QoS Policy.** Assign QoS profiles via ACL rules.
4. Active Queue Management: **WRED** (Weighted Random Early Detection), **ECN** notification and processing, **PFC** (Priority-based Flow Control).
5. Traffic shaping.

### QoS Changes in RouterOS v7.23

RouterOS v7.23 introduces significant changes to Quality of Service (QoS) offloading. These changes simplify the configuration process and add support for "lossless" traffic classes. Although hardware resources are finite, active queue management using ECN and/or PFC can prevent packet loss when all connected devices support these features and are properly configured. Previous RouterOS versions already supported ECN and PFC, but v7.23 streamlines how you set them up.

:::info
Not all devices support lossless traffic. Check the QoS Device Support table.
:::

#### Configuration Change Summary

- QoS Settings: most changes were set to "auto" by default, allowing RouterOS to pick the best known settings for the setup.
- QoS Settings: added `lossless-traffic-class` and `lossless-buffers`, allowing explicit specification of lossless traffic and the reservation of queue resources for it. The user can leave those fields as "auto" as well.
- QoS Monitor: displays the shared pool usage for lossy and lossless separately.
- Tx Queue: removed shared pool index. RouterOS automatically selects the shared pool based on the traffic type (lossy or lossless).
- QoS Profile: added automapping to the specified PCP and DSCP values (enabled by default). For example, adding a QoS profile with DSCP=46 automatically applies the profile to traffic received from trusted ports.

## QoS Terminology

This section defines the key terms and abbreviations used throughout this documentation:

- **QoS** - Quality of Service, a collection of features that allows network administrators to prioritize traffic and allocate network resources.
- **ACL** - Access Control List, a set of switch rules used to filter network traffic based on specified criteria.
- **AQM** - Active Queue Management, a congestion control mechanism that manages traffic flow by dropping or marking packets before queue overflow occurs.
- **DSCP** - Differentiated Services Code Point, a 6-bit field in the IP header used to prioritize network traffic.
- **ECN** - Explicit Congestion Notification, a mechanism that allows routers to signal congestion to endpoints devices without dropping packets.
- **ETS** - Enhanced Transmission Selection, a traffic scheduling method that uses weighted round-robin to allocate bandwidth among multiple queues groups.
- **PCP** - Priority Code Point, a 3-bit field in the VLAN header used to prioritize traffic within a VLAN.
- **PFC** - Priority-based Flow Control (IEEE 802.1Qbb), a flow control mechanism that pauses traffic on specific priority queues to prevent packet loss.
- **RoCE** - RDMA over Converged Ethernet, a protocol that enables remote direct memory access over Ethernet networks.
- **WRED** - Weighted Random Early Detection, a congestion avoidance mechanism that randomly drops packets as a queue approaches capacity.
- **/in/eth/sw/** - A CLI shortcut for `/interface/ethernet/switch/`.

## QoS Enhancements in new generation Marvell Prestera Switch Chips

MikroTik devices with new generation Marvell Prestera switch chips (e.g. CRS8xx series running the [switch-marvell package](../getting-started/installation-and-upgrade/packages.md#extra-packages) offer a new approach in QoS enforcement. Previous models required making a tradeoff between guaranteed and shared Tx queue buffers. By increasing the shared buffer percentage, the device can absorb larger traffic bursts, but at the same time, one congested port can occupy all shared buffers, limiting the QoS capabilities of other ports. Using the new generation switch chips enables the best of both worlds by introducing **Dynamic Buffers**. A switch chip dynamically adjusts port and queue buffer limits based on the current congestion level. If there is no congestion within the device, a single port can absorb a large burst of traffic, preventing packet loss. When the Tx queue size increases across multiple ports, the device reduces per-port and per-queue limits, enforcing fair use of shared resources while ensuring enough buffers for non-congested queues to continue forwarding traffic. The entire process is automated, requiring zero configuration from the user.

Another improvement in the new generation Marvell Prestera switch chips is eliminating the shortage of enqueued packet descriptors for storing control data. The previous generation devices had Packet Cap and Use stats. When a device received a burst of small packets, it could start tail-dropping packets due to hitting Packet Cap, even though it had enough queue buffers to store the payload. The new generation devices ensure there is always enough memory to store control data, leaving the Dynamic Buffer size as the only limiting factor. That's why there are no Packet Cap/Use stats in the new generation devices.

New generation devices require QoS HW Offloading to be enabled at all times (**qos-hw-offloading=yes**). RouterOS ignores user requests to disable it while keeping the field for backward compatibility.

## QoS Device Support

<WideTable>

| Switch Chip | Models | QoS Profiles | QoS Maps | Tx Managers | WRED | ECN | PFC | Lossless Buffers | Dynamic Buffers | Port/Queue Usage Stats |
| :-- | :-- | --: | --: | --: | :-- | :-- | :-- | :-- | :-- | :-- |
| **98DX3236** | CRS305-1G-4S+IN  CRS326-24G-2S+ (RM/IN)  CRS328-24P-4S+RM  CRS328-4C-20S-4S+RM | 128 | 1 | 8 |  |  |  |  |  | Current values |
| **98DX226S** | CRS305-1G-4S+OUT (FiberBox Plus)  CRS310-1G-5S-4S+ (netFiber 9/IN)  CRS310-8G+2S+IN  CRS318-16P-2S+OUT (netPower 16P)  CRS320-8P-8B-4S+RM  CRS418-8P-8G-2S+RM  CRS418-8P-8G-2S+5axQ2axQ-RM | 128 | 1 | 8 |  |  |  |  |  | Current values |
| **98DX224S** | CRS318-1Fi-15Fr-2S-OUT (netPower 15FR) | 128 | 1 | 8 |  |  |  |  |  | Current values |
| **98DX2528** | CRS304-4XG-IN | 128 | 1 | 8 |  |  |  |  |  | Current values |
| **98DX8525** | CCR2216-1G-12XS-2XQ  CRS518-16XS-2XQ-RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | Max fill <sup>1</sup> |
| **98DX4310** | CRS504-4XQ (IN/OUT)  CRS510-8XS-2XQ-IN  RDS2216-2XG-4S+4XS-2XQ | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | Max fill <sup>1</sup> |
| **98DX8208** | CRS309-1G-8S+IN | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | Current values <sup>2</sup> |
| **98DX8212** | CRS312-4C+8XG-RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | Current values <sup>2</sup> |
| **98DX8216** | CRS317-1G-16S+RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | Current values <sup>2</sup> |
| **98DX8332** | CRS326-24S+2Q+RM  CRS326-4C+20G+2Q+RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | Current values <sup>2</sup> |
| **98DX3257** | CRS354-48G-4S+2Q+RM  CRS354-48P-4S+2Q+RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | Current values <sup>2</sup> |
| **98DX3255** | CCR2116-12G-4S+ | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | Current values <sup>2</sup> |
| **98CX8410** | CRS520-4XS-16XQ-RM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ |  | Unavailable <sup>3</sup> |
| **98DX7335** | CRS812-8DS-2DQ-2DDQ-RM  CRS804-4DDQ-hRM | 1024 | 12 | 15 | ✔ | ✔ | ✔ | ✔ | ✔ | Current values + Max fill |

</WideTable>

<sup>**1**</sup> The device gathers max queue fill statistics instead of displaying the current usage values. Use the `reset-counters` command to clear those stats.  
<sup>**2**</sup> Due to hardware limitations, some switch chip models may experience temporary traffic flow disruption while reading or polling QoS port/queue usage data.  
<sup>**3**</sup> Usage data for individual queues on a port is unavailable; only the aggregate total usage for the entire physical port can be accessed.

## Applications and Usage Examples

---

### Basic Configuration Example

This example demonstrates how to configure a single QoS level for VoIP (IP Telephony) on top of the standard Best Effort class. The configuration uses a CRS326-24G-2S+ device with the following setup:

- All ports are bridged and use **[vlan-filtering](index.md#bridge-vlan-filtering)**;
- sfp-sfpplus1 serves as a VLAN trunk connected to another switch;
- ether1 through ether9 are dedicated ports for IP phones;
- ether10 through ether24 are standard ports for host connection.

First, define a QoS profile. This profile specifies the DSCP and PCP values that will be applied to forwarded packets on egress:

```ros
/interface/ethernet/switch/qos/profile
add dscp=46 name=voip pcp=5 traffic-class=5
```

Next, assign the VoIP QoS profile to the dedicated ports for IP phones. This applies the profile to ingress traffic on these ports. All other Ethernet ports will use the default profile (where dscp=0 and pcp=0):

```ros
/interface/ethernet/switch/qos/port
set ether1 profile=voip
set ether2 profile=voip
set ether3 profile=voip
set ether4 profile=voip
set ether5 profile=voip
set ether6 profile=voip
set ether7 profile=voip
set ether8 profile=voip
set ether9 profile=voip
```

The trunk port receives both types of QoS traffic. To differentiate between them, enable trust-l3 and trust-l2:

```ros
/interface/ethernet/switch/qos/port
set sfp-sfpplus1 trust-l3=trust trust-l2=trust
```

> **Note:** If you are running RouterOS version 7.23 or later, the VLAN priority and IP DSCP mapping is created automatically, so this step is not required. If you are using an earlier RouterOS version, you must manually create the VLAN priority and IP DSCP mapping with the QoS profile:

```routeros
/interface/ethernet/switch/qos/map/ip
add dscp=46 profile=voip

/interface/ethernet/switch/qos/map/vlan
add pcp=5 profile=voip
```

Finally, enable QoS hardware offloading for the above settings to take effect:

```ros
/interface/ethernet/switch
set switch1 qos-hw-offloading=yes
```

You can verify the port QoS settings using the `print` command:

```ros
[admin@MikroTik] /interface/ethernet/switch/qos/port/print
Column: NAME, SWITCH, PROFILE, MAP, TRUST-L2, TRUST-L3
 # NAME          SWITCH   PROFILE  MAP      TRUST-L2  TRUST-L3  TX-MANAGER
 0 ether1        switch1  voip     default  ignore    ignore    default
 1 ether2        switch1  voip     default  ignore    ignore    default
 2 ether3        switch1  voip     default  ignore    ignore    default
 3 ether4        switch1  voip     default  ignore    ignore    default
 4 ether5        switch1  voip     default  ignore    ignore    default
 5 ether6        switch1  voip     default  ignore    ignore    default
 6 ether7        switch1  voip     default  ignore    ignore    default
 7 ether8        switch1  voip     default  ignore    ignore    default
 8 ether9        switch1  voip     default  ignore    ignore    default
 9 ether10       switch1  default  default  ignore    ignore    default
10 ether11       switch1  default  default  ignore    ignore    default
11 ether12       switch1  default  default  ignore    ignore    default
12 ether13       switch1  default  default  ignore    ignore    default
13 ether14       switch1  default  default  ignore    ignore    default
14 ether15       switch1  default  default  ignore    ignore    default
15 ether16       switch1  default  default  ignore    ignore    default
16 ether17       switch1  default  default  ignore    ignore    default
17 ether18       switch1  default  default  ignore    ignore    default
18 ether19       switch1  default  default  ignore    ignore    default
19 ether20       switch1  default  default  ignore    ignore    default
20 ether21       switch1  default  default  ignore    ignore    default
21 ether22       switch1  default  default  ignore    ignore    default
22 ether23       switch1  default  default  ignore    ignore    default
23 ether24       switch1  default  default  ignore    ignore    default
24 sfp-sfpplus1  switch1  default  default  trust     ignore    default
25 sfp-sfpplus2  switch1  default  default  ignore    ignore    default
26 switch1-cpu   switch1   
```

With this configuration, incoming packets on port ether1 through ether9 are marked with a Priority Code Point (PCP) value of 5 and a Differentiated Services Code Point (DSCP) value of 46. Incoming packets on port ether10 through ether24 are marked with PCP and DSCP value of 0. When packets are received on the sfp-sfpplus1 port, any packets with a PCP value of 5 retain their PCP value of 5 and DSCP value of 46, while all other packets are marked with PCP and DSCP value of 0.

## Dante

Starting from RouterOS v7.15, all MikroTik QoS-capable devices are compatible with Dante audio networking.

Dante hardware uses the following DSCP/Diffserv priority values for traffic prioritization:

| Dante Priority | Usage | DSCP Label | DSCP Value |
| :-- | :-- | :-- | --: |
| High | Time-critical PTP events | CS7 | 56 |
| Medium | Audio, PTP | EF | 46 |
| None | Other traffic | BE | 0 |

This example assumes the switch is using its default configuration, which includes a default bridge interface with all Ethernet interfaces added as bridge ports. Any of these interfaces can be used for Dante.

First, create QoS profiles to match Dante traffic classes. There is already a pre-existing "default" profile that corresponds to Dante's None priority.

```ros
/interface/ethernet/switch/qos/profile
add name=dante-ptp dscp=56 pcp=7 traffic-class=7
add name=dante-audio dscp=46 pcp=5 traffic-class=5
```

If you are running RouterOS version 7.23 or later, the IP DSCP mapping is created automatically, so this step is not required. If you are using an earlier RouterOS version, create a QoS mapping to match QoS profile based on DSCP values:

```ros
/interface/ethernet/switch/qos/map/ip
add dscp=56 profile=dante-ptp
add dscp=46 profile=dante-audio
```

Configure the hardware queue to enforce QoS on Dante traffic:

```ros
/interface/ethernet/switch/qos/tx-manager/queue
set [find where traffic-class=7] schedule=strict-priority
set [find where traffic-class=5] schedule=strict-priority
```

Dante's High and Medium priority traffic is scheduled in strict priority order. The device transmits time-critical PTP packets until queue7 is empty, then proceeds with audio (queue5). Other traffic is transmitted only when PTP and audio queues are empty.

The next step is to enable trust mode for incoming Layer 3 packets (IP DSCP field):

```ros
/interface/ethernet/switch/qos/port
set [find] trust-l3=keep
```

Finally, enable QoS hardware offloading for the above settings to take effect:

```ros
/interface/ethernet/switch
set switch1 qos-hw-offloading=yes
```

When using Dante in multicast mode, it is beneficial to enable IGMP snooping on the switch. This feature directs traffic only to ports with subscribed devices, preventing unnecessary flooding. Additionally, enabling an IGMP querier (if not already enabled on another device in the same LAN), adjusting query interval, and activating fast-leave can further optimize multicast performance.

```ros
/interface/bridge
set [find name=bridge] igmp-snooping=yes multicast-querier=yes query-interval=60s

/interface/bridge/port
set [find] fast-leave=yes
```

## RDMA over Converged Ethernet (RoCE)

RoCE enables direct memory access to remote storage systems over Ethernet networks without involving the host CPU. This significantly reduces latency and CPU overhead, making RoCE ideal for high-performance computing and data center environments. RoCE also allows a converged network where various services (such as data storage, networking, and multimedia) run over a single Ethernet infrastructure, simplifying network management and reducing the cost and complexity of maintaining separate networks.

RoCE achieves this through the use of **ECN** and **PFC** mechanisms. These features help prevent network congestion and packet loss, ensuring reliable, lossless communication. See the [device feature table](quality-of-service.md#qos-device-support) for compatible switches. While the switch can support a RoCE environment, the end hosts must also be compatible with the RoCE protocol and equipped with RDMA-capable network interface cards (NICs).

There are two main versions of RoCE. RoCEv1 operates as an Ethernet link layer protocol and uses Ethertype 0x8915. RoCEv2 works over standard IP networks, using UDP destination port number 4791. ECN bits in the IP header are marked to signal network congestion, and a Congestion Notification Packet (CNP) is used to acknowledge congestion to the sender. For traffic prioritization, DSCP 26 is used for RoCEv2 traffic, while DSCP 48 is used for CNPs.

The following example can be used for lossless RoCEv2 with PFC and ECN, and it assumes that the switch is using its default configuration, which includes a default bridge interface with all Ethernet interfaces added as bridge ports. The minimal recommended RouterOS version is 7.17.

First, configure additional profiles. Non-RoCE traffic will be assigned to the already existing "default" profile with traffic-class 1, RoCEv2 to traffic-class 3, and CNP to traffic-class 6.

```routeros
/interface/ethernet/switch/qos/profile
add dscp=26 name=roce traffic-class=3
add dscp=48 name=cnp traffic-class=6
```

If you are running RouterOS version 7.23 or later, the IP DSCP mapping is created automatically, so this step is not required. If you are using an earlier RouterOS version, create a QoS mapping to match QoS profiles based on DSCP values.

```routeros
/interface/ethernet/switch/qos/map/ip
add dscp=26 profile=roce
add dscp=48 profile=cnp
```

Configure hardware queue and scheduler. Use ETS (`schedule=high-priority-group`) for traffic-class 1 and traffic-class 3 with 50% bandwidth assignment each (`weight=1`), and strict priority scheduling for traffic-class 6. Additionally, enable ECN (`ecn=yes`) for traffic-class 3 to mark IP packets in the switch that experience congestion.

```routeros
/interface/ethernet/switch/qos/tx-manager/queue
set 1 schedule=high-priority-group weight=1
set 3 schedule=high-priority-group weight=1 ecn=yes
set 6 schedule=strict-priority
```

:::tip
Although using `schedule=low-priority-group` allows you to create separate ETS scheduling and bandwidth allocation for a different set of traffic-classes, it is not recommended to use this setting together with `lldp-dcbx=yes`. The reason is that the ETS Configuration/Recommendation TLVs are designed to handle a single bandwidth allocation across traffic classes, thus `schedule=high-priority-group` should be used instead.
:::

Configure a PFC profile for traffic-class 3 to ensure a lossless environment for RoCEv2 traffic.

```routeros
/interface/ethernet/switch/qos/priority-flow-control
add name=pfc-tc3 rx=yes traffic-class=3 tx=yes
```

Set Layer3 trust mode (`trust-l3=keep`) on switch ports where RoCEv2 traffic is expected. Set PFC (`pfc=pfc-tc3`) and egress rate for queue3 to comply with PFC requirements (`egress-rate-queue3=10.0Gbps`). In this example, 10Gbps SFP+ interfaces is used, and the egress rate can be set to match the physical speed of the interface. Change this property depending on your interface speeds.

```routeros
/interface/ethernet/switch/qos/port
set sfp-sfpplus1 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
set sfp-sfpplus2 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
set sfp-sfpplus3 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
set sfp-sfpplus4 egress-rate-queue3=10.0Gbps pfc=pfc-tc3 trust-l3=keep
```

Enable QoS hardware offloading for the above settings to start working.

```routeros
/interface/ethernet/switch
set switch1 qos-hw-offloading=yes
```

Enable the LLDP Data Center Bridging Capability Exchange Protocol (DCBX) to share QoS settings and capabilities with other neighboring devices.

```routeros
/ip/neighbor/discovery-settings
set lldp-dcbx=yes
```

As an optional step, increase the L2MTU to accommodate larger data packets.

```routeros
/interface/ethernet
set [find switch=switch1] l2mtu=9500
```

## QoS Marking

---

### Understanding Map Ranges

To avoid defining every possible PCP and DSCP mapping individually, RouterOS allows you to specify multiple values or ranges for PCP and DSCP when creating QoS profile mappings.

In this example, PCP values 0 and 2 use the default QoS profile, values 1 and 3-4 use the streaming profile, value 5 uses the voip profile, and values 6-7 use the control profile:

```ros
/interface/ethernet/switch/qos/map/vlan
add pcp=1,3-4 profile=streaming
add pcp=5 profile=voip
add pcp=6-7 profile=control
```

This approach simplifies configuration by grouping related priority values together rather than creating separate mappings rules for each individual value.

### Understanding Port, Profile, and Map relation

Each switch port has Layer2 and Layer3 trust settings that will change how ingress packets are classified into QoS profiles and what PCP and DSCP values will be used. Below are tables that describe all possible options:

| **qos-trust-l2** | **qos-trust-l3** | Behavior |
| :-- | :-- | :-- |
| **ignore** | **ignore** | The port is considered untrusted. Both headers are ignored, and the port's **profile** is forced to all ingress packets. This is the default setting. |
| **ignore** | **trust** | Trust the Layer 3 header. Use the DSCP field from the IP header of ingress packets for QoS profile lookup (see `/in/eth/sw/qos/map/ip`). If the lookup fails (no QoS profiles are mapped to the given DSCP value), the **default** QoS profile is used (not the switch port's QoS profile). The switch port's **profile** field is used only for non-IP traffic. |
| **ignore** | **keep** | Trust the Layer 3 header. Use the DSCP field from the IP header of ingress packets for QoS profile lookup (see `/in/eth/sw/qos/map/ip`). If the lookup fails, the **default** QoS profile is used. The switch port's **profile** field is used only for non-IP traffic. If the forwarded/routed packet is VLAN-tagged, its PCP value is set from the selected QoS profile. However, the original DSCP value of the packet is kept intact. |
| **trust** | **ignore** | Trust the Layer 2 header, but ignore L3. If an ingress packet is VLAN-tagged, use the PCP field from the VLAN header for QoS profile lookup (see `/in/eth/sw/qos/map/vlan`). If the lookup fails (no QoS profiles are mapped to the given PCP value), the **default** QoS profile is used. The switch port's **profile** field is used only for untagged traffic. |
| **trust** | **trust** | Trust both headers, but Layer 3 has higher precedence. In the case of an IP packet, use the DSCP field for QoS profile lookup (see `/in/eth/sw/qos/map/ip`). If the DSCP-to-QoS lookup fails, use the **default** profile. If the packet is not an IP packet but is VLAN-tagged, use the PCP field from the VLAN header for QoS profile lookup (see `/in/eth/sw/qos/map/vlan`).  If the VLAN-to-QoS lookup fails, use the **default** QoS profile. Non-IP untagged packets use the switch port's **profile**. |
| **trust** | **keep** | The same as **trust+trust**, but the original DSCP value is preserved in forwarded/routed packets. |
| **keep** | **ignore** | Trust the Layer 2 header but ignore L3. If an ingress packet is VLAN-tagged, use the PCP field from the VLAN header for QoS profile lookup (see `/in/eth/sw/qos/map/vlan`). If the lookup fails (no QoS profiles are mapped to the given PCP value), the **default** QoS profile is used. The switch port's **profile** field is used only for untagged traffic. If the packet is VLAN-tagged on both ingress and egress, the original PCP value is kept. |
| **keep** | **trust** | Trust both headers, but Layer 3 has higher precedence. In the case of an IP packet, use the DSCP field for QoS profile lookup (see `/in/eth/sw/qos/map/ip`). If the DSCP-to-QoS lookup fails, use the **default** profile. If the packet is not an IP packet but is VLAN-tagged, use the PCP field from the VLAN header for QoS profile lookup (see `/in/eth/sw/qos/map/vlan`).  If the VLAN-to-QoS lookup fails, use the **default** QoS profile. Non-IP untagged packets use the switch port's **profile**. If the packet is VLAN-tagged on both ingress and egress, the original PCP value is kept. The DSCP value in forwarded/routed packets is set from the selected QoS profile. |
| **keep** | **keep** | Trust both headers, but Layer 3 has higher precedence. In the case of an IP packet, use the DSCP field for QoS profile lookup (see `/in/eth/sw/qos/map/ip`). If the DSCP-to-QoS lookup fails, use the **default** profile. If the packet is not an IP packet but is VLAN-tagged, use the PCP field from the VLAN header for QoS profile lookup (see `/in/eth/sw/qos/map/vlan`).  If the VLAN-to-QoS lookup fails, use the **default** QoS profile. Non-IP untagged packets use the switch port's **profile**. Keep both the original PCP and/or DSCP values intact in cases of VLAN-tagged and/or IP packets, respectively. |

<WideTable>

| **Port settings** |  | The selected QoS profile and the source for PCP / DSCP field values in forwarded/routed packets |  |  |  |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **qos-trust-l2** | **qos-trust-l3** | VLAN-Tagged IP |  |  | Untagged IP |  |  | VLAN-Tagged Non-IP |  |  | Untagged Non-IP |  |  |
|  |  | QoS Profile | PCP | DSCP | QoS Profile | PCP <sup>1</sup> | DSCP | QoS Profile | PCP | DSCP | QoS Profile | PCP <sup>1</sup> | DSCP |
| ignore | ignore | profile | profile | profile | profile | profile | profile | profile | profile | - | profile | profile | - |
| ignore | trust | map/ip | map/ip | map/ip | map/ip | map/ip | map/ip | profile | profile | - | profile | profile | - |
| ignore | keep | `/map/ip` | `/map/ip` | original | `/map/ip` | `/map/ip` | original | profile | profile | - | profile | profile | - |
| trust | ignore | map/vlan | map/vlan | map/vlan | profile | profile | profile | map/vlan | map/vlan | - | profile | profile | - |
| trust | trust | `/map/ip` | `/map/ip` | `/map/ip` | `/map/ip` | `/map/ip` | `/map/ip` | `/map/vlan` | `/map/vlan` | - | profile | profile | - |
| trust | keep | `/map/ip` | `/map/ip` | original | `/map/ip` | `/map/ip` | original | `/map/vlan` | `/map/vlan` | - | profile | profile | - |
| keep | ignore | map/vlan | original | map/vlan | profile | profile | profile | map/vlan | original | - | profile | profile | - |
| keep | trust | map/ip | original | map/ip | map/ip | profile | map/ip | map/vlan | original | - | profile | profile | - |
| keep | keep | map/ip | original | original | map/ip | profile | original | map/vlan | original | - | profile | profile | - |

</WideTable>

<sup>**1**</sup> Applies only when ingress traffic is untagged, but the egress interface requires the frames to be VLAN-tagged.

### QoS Marking via Switch Rules (ACL)

Starting from **RouterOS v7.15**, you can assign QoS profiles to network traffic using Switch Rules (ACL). This method allows for flexible traffic classification based on various packet attributes.

The following example assigns a QoS profile based on the source MAC address:

```ros
/interface/ethernet/switch/rule
add new-qos-profile=stream port=ether1,ether2 src-mac-address=00:01:02:00:00:00/FF:FF:FF:00:00:00 switch=switch1
add new-qos-profile=voip port=ether1,ether2 src-mac-address=04:05:06:00:00:00/FF:FF:FF:00:00:00 switch=switch1
```

## QoS Enforcement

### Hardware Queues

Each switch port has eight hardware transmission (Tx) queues (queue0 through queue7). Each queue corresponds to a traffic class (tc0 through tc7) defined by a [QoS profile](../cli-reference/interface/ethernet/switch/qos/profile.md). When a packet enters the switch, it receives a QoS profile assignment, which determines the traffic class and consequently selects the appropriate egress queue for transmission.

Hardware queues have variable sizes configured by the [Transmission Manager](../cli-reference/interface/ethernet/switch/qos/tx-manager/tx-manager.md). Additionally, multiple ports and queues can share resources with each other through a mechanism called *Shared Buffers*. For example, a device with 25 ports has buffer memory sufficient to queue 1200 packets total. If resources are split equally, each port receives 48 exclusive buffers with a maximum of 6 packets per queue (48 divided by 8), which is typically insufficient to absorb even a short traffic burst. However, allocating 50% of buffers for sharing leaves each port with 24 exclusive buffers (3 per queue), while simultaneously allowing a single queue to grow up to 603 buffers (3 exclusive plus 600 shared).

RouterOS enables enabling or disabling the shared pool for each queue individually. This capability helps prevent low-priority traffic from consuming all available hardware memory. Additionally, port buffer limits can restrict a single low-speed port from occupying the entire shared pool. For more details, see [QoS Settings](../cli-reference/interface/ethernet/switch/qos/settings.md) and [Transmission Manager](../cli-reference/interface/ethernet/switch/qos/tx-manager/tx-manager.md).

:::info
The default best-effort traffic class (PCP=0, DSCP=0) is traffic class 1, while the lowest priority traffic (PCP=1) uses traffic class 0.
:::

## Hardware Resources

The switch chip has limited hardware resources (memory). Two main hardware resources are relevant to QoS operations:

- **Packet descriptor** - Contains packet control information such as the target port, header modifications, and other metadata.
- **Data buffer** - Memory chunk that stores the actual packet payload. Buffer size varies depending on the switch chip model; typically 256 bytes.

One packet descriptor may use multiple buffers (depending on the payload size), and buffers may be shared by multiple descriptors in cases of multicast or broadcast traffic. If the hardware does not have enough free descriptors or buffers, the packet gets dropped (tail-drop).

Hardware resources can be limited per destination type (multicast/unicast), per port, and per TX queue. When any of these limits are reached, no additional packets can be enqueued for transmission, and subsequent packets get dropped.

RouterOS abstracts low-level hardware details, allowing resource limits to be configured either in terms of packets or as a percentage of the total amount. RouterOS automatically calculates the required hardware descriptor and buffer count based on the user-specified packet limit and port's MTU. Additionally, RouterOS includes preconfigured hardware resources, eliminating the need for manual configuration in common QoS scenarios.

:::danger
Modifying any hardware resource allocation parameter at runtime causes a temporary device halt during which no packets can be enqueued or transmitted. Temporary packet loss is expected while the device is forwarding traffic.
:::

## Resource Saving (Previous Generation Devices)

:::info
This section applies only to devices that do **not** support **Dynamic Buffers**.
:::

Because hardware resources cannot be reallocated at runtime, RouterOS cannot automatically release queue buffers reserved for inactive ports. These buffers remain unused. However, if you know that a specific port will never be used (for example, it stays physically disconnected), you can manually free the corresponding queue resources by assigning the built-in "offline" tx-manager with minimum resources:

```ros
/interface/ethernet/switch/qos/port
set sfp-sfpplus1 tx-manager=offline
set sfp-sfpplus2 tx-manager=offline
```

:::danger
Do not configure the "offline" tx-manager on the **switch-cpu** port.
:::
:::warning
When configuring the `tx-manager` setting for a QSFP+ or QSFP28 interface, you must apply the same configuration to all four sub-interfaces of that port. For example, if interface qsfp28-1-1 is active and linked at 100Gbps, while sub-interfaces (qsfp28-1-2, qsfp28-1-3, qsfp28-1-4) show a non-running flag, **do not assign the "offline" tx-manager to those non-running sub-interfaces**. Doing so will affect the 100Gbps link as well. However, if none of the four sub-interfaces are running, it is safe to assign the "offline" tx-manager setting.
:::

## Traffic Prioritization

The hardware supports two types of traffic transmission prioritization:

- **Strict Priority** - traffic from higher queues is always transmitted first.
- **Enhanced Transmission Selection (ETS)** - multiple queues participate in packet transmission scheduling at the same time using weighted round-robin.

**Strict Priority** queuing is straightforward. If the highest priority queue (Q7) has packets, those are transmitted first. When Q7 is empty, packets from Q6 get transmitted, and so on. The packets from the lowest priority queue (Q0) are transmitted only if all other queues are empty.

The downside of strict prioritization is increased latency in lower queues while "overprioritizing" higher queues. Suppose the acceptable latency of TC5 is 20ms, TC3 - 50ms. Traffic appearing in Q5 gets immediately transmitted due to the strict priority of the queue, adding extra latency to every packet in the lower queues (Q4..Q0). A packet burst in Q5 (e.g., a start of a voice call) may temporarily "paralyze" Q3, increasing TC3 latencies over the acceptable 50ms (or even causing packet drops due to a full queue) while TC5 packets get transmitted at &lt;1ms (way below the 20ms limit). Slightly sacrificing TC5 latency by transmitting TC3 packets in between would make everybody happy. That is what **ETS** is for.

**Enhanced Transmission Selection (ETS)** schedules traffic for transmission from multiple queues (group members) in a weighted round-robin manner. A queue's weight sets the number of packets transmitted from the queue in each round. For example, if Q2, Q1, and Q0 are the group members, and their weights are 3, 2, and 1, respectively, the scheduler transmits 3 packets from Q2, 2 from Q1, and 1 from Q0. The actual transmission order in each round of the above example is "Q2, Q1, Q0, Q2, Q1, Q2" - for even fairer scheduling.

There are two hardware groups: `low-priority-group` and `high-priority-group`. There is a strict priority ordering between the two groups: the low-priority-group transmits only when *all* queues in the high-priority-group are empty. However, it is possible to use only one group for all queues.

The default (built-in) RouterOS queue setup is listed below. Q3-Q5 share the bandwidth within the high-priority group, where packets are transmitted while Q6 and Q7 are empty. Q0-Q2 are the members of the low-priority-group, where packets are transmitted while Q3-Q7 are empty.

```ros
[admin@MikroTik] /interface/ethernet/switch/qos/tx-manager/queue> print 
Columns: TX-MANAGER, TRAFFIC-CLASS, SCHEDULE, WEIGHT, QUEUE-BUFFERS, USE-SHARED-BUFFERS
#  TX-MANAGER  TRAFFIC-CLASS  SCHEDULE             WEIGHT  QUEUE-BUFFERS  USE-SHARED-BUFFERS
0  default     0              low-priority-group   1       auto           no                
1  default     1              low-priority-group   2       auto           yes                
2  default     2              low-priority-group   3       auto           yes                
3  default     3              high-priority-group  3       auto           yes               
4  default     4              high-priority-group  4       auto           yes               
5  default     5              high-priority-group  5       auto           yes               
6  default     6              strict-priority              auto           yes               
7  default     7              strict-priority              auto           yes 
```

:::tip
It is recommended that all group members are adjacent to each other.
:::

## Active Queue Management (AQM)

### Weighted Random Early Detection (WRED)

WRED is a congestion control mechanism that operates on a per-queue basis. It signals congestion events to end-point devices by dropping packets before queue overflow occurs. WRED relies on rate throttling mechanisms in end-points that respond to packet loss, such as TCP/IP.

WRED uses a randomized packet drop algorithm to anticipate congestion events and respond to them by throttling traffic rates before congestion actually happens. The randomness property of WRED prevents throughput collapse caused by global synchronization of TCP flows.

WRED can be enabled or disabled per queue in each Tx Manager. Disable WRED for lossless traffic classes. There is also no reason to enable WRED on high-speed ports where congestion should not occur in the first place.

The behavior is controlled via the WRED threshold. The WRED threshold defines the maximum number of packets or bytes that can exceed the queue's shared buffer limit (cap). Random packet drops begin when queue usage exceeds its respective capacity:

- `queueX-packet-use > queueX-shared-packet-cap`, or
- `queueX-byte-use > queueX-shared-byte-cap`.

The more the usage exceeds the capacity, the higher the packet drop chance becomes, reaching 100% at `queueX-shared-packet-cap + wred-packet-threshold` (or byte equivalent).

RouterOS automatically selects the actual WRED threshold values based on queue or shared pool capacities. The user can adjust the thresholds via the QoS Settings.

:::danger
WRED requires the respective Tx queue to use shared buffers (**use-shared-buffers=yes**).
:::

Choosing a WRED threshold value involves a tradeoff between congestion anticipation and burst absorption. Setting a higher WRED threshold may lead to earlier traffic rate throttling and, therefore, resolve congestion. However, a high threshold causes packet drops in limited traffic bursts that could be absorbed by the queue buffers and transmitted losslessly if WRED didn't activate.

For example, initiating a remote database connection usually starts with heavier traffic (a "packet burst") during the initialization phase, then the traffic rate drops to a "reasonable" level. Any packet drop during the initialization phase results in a slower database connection due to the need for retransmission. Therefore, lowering the WRED threshold or entirely disabling WRED on such traffic is recommended. The opposite case is video streaming, where early congestion detection helps select a comfortable streaming rate without losing too much bandwidth on retransmission or sacrificing quality level.

:::info
Use Switch Rules (ACL) or other QoS Marking techniques to differentiate traffic and place packets into queues with the desired WRED settings.
:::

The following script applies WRED only to TCP/IP traffic by redirecting it to queue2. UDP and other packets remain in queue1 since their end-points typically cannot respond to early drops. Queue1 and queue2 are scheduled equally without prioritizing one queue over another:

```ros
/interface/ethernet/switch/qos/profile
add name=tcp-wred traffic-class=2 pcp=0 dscp=0

# move TCP traffic to queue2
/interface/ethernet/switch/rule
add new-qos-profile=tcp-wred ports=ether1,ether2,ether3,ether4 protocol=tcp switch=switch1

# set the same scheduling priority (weight) between queue1 and queue2
# apply WRED only to queue2 - TCP traffic
/interface/ethernet/switch/qos/tx-manager/queue/
set [find where traffic-class=1] weight=2 schedule=low-priority-group use-shared-buffers=yes wred=no
set [find where traffic-class=2] weight=2 schedule=low-priority-group use-shared-buffers=yes wred=yes
```

## Explicit Congestion Notification (ECN)

Certain switch chip models support hardware-level ECN marking for IP packets, compliant with RFC 3168. This mechanism operates similarly to WRED but, instead of dropping packets during congestion, it marks them with the CE (Congestion Experienced, binary 11) flag in the ECN field. Only ECN-capable IP packets can receive this mark—those with the ECN field value set to ECT(1) or ECT(0) (binary 01 or 10). Non-ECN-capable transport packets (ECN=00) are never marked. If a packet already carries the CE mark (ECN=11), it retains this designation regardless of whether the device experiences congestion.

Enable ECN marking by setting **ecn=yes** on the desired [Tx Manager Queue](../cli-reference/interface/ethernet/switch/qos/tx-manager/tx-manager.md).

:::danger
The ECN marking mechanism requires the respective Tx queue to use shared buffers (**use-shared-buffers=yes**).
:::

A packet receives the CE mark when **all** of the following conditions are met:

1. The packet is IPv4 or IPv6.
2. The ECN field value in the IP header is either ECT(1) or ECT(0).
3. The egress port's Tx Queue has **ecn=yes** enabled and uses shared buffers (**use-shared-buffers=yes**).
4. Queue usage exceeds the shared buffer capacity: `queueX-packet-use > queueX-shared-packet-cap` or `queueX-byte-use > queueX-shared-byte-cap`.

:::danger
Since enabling ECN (ecn=yes) prevents ECN-capable packet drops, queue usage may exceed WRED thresholds if the traffic sender does not respond to congestion notification in time.
:::

## Priority-based Flow Control (PFC)

Priority-based Flow Control (PFC) enables lossless operation for up to eight traffic classes, ensuring that congestion in one traffic class does not pause traffic in other classes. This allows loss-sensitive traffic types to coexist with loss-tolerant traffic types on the same network.

PFC-capable switch chips comply with IEEE 802.1Qbb PFC standard, meaning they can generate and respond to PFC frames. When congestion occurs on an egress port, the source port transmits a PFC frame for the affected traffic class. The generated PFC frames use timer value 0xFFFF for pause (XOFF) and 0x0 for resume (XON), with the appropriate bit set in the priority enable vector. On the receiving end, the PFC frame pauses the specific priority queues on the destination port for the duration specified in the PFC frame.

In RouterOS, PFC configuration is organized into profiles. Each port can be assigned to a specific PFC profile, which defines the traffic classes to enable PFC on, the pause and resume thresholds for sending XOFF and XON frames respectively, and whether the assigned ports should transmit and/or receive PFC frames.

When congestion occurs on an egress port, PFC is triggered on the ingress port. Shared buffers must be used to associate the amount of ingress traffic with the packets waiting in Tx queues. For each PFC-enabled traffic class, set **use-shared-buffers=yes** on the corresponding Tx queue.

:::info
RouterOS implements a 1:1 mapping between traffic classes and Tx queues. Packets with traffic class 0 are enqueued in queue0, TC1 in queue1, and so on up to TC7 in queue7. Therefore, the terms "traffic class" and "Tx queue" are used interchangeably throughout this documentation.
:::

When selecting pause and resume thresholds, account for the delay in transmitting and processing PFC frames. For example, device A experiences congestion at time T, sends a PFC pause frame to device B, and B processes the frame and stops transmitting at time T+D. During the delta time D, device B continues sending traffic. If device A has configured the pause threshold to 100%, it has no free buffers available, and packets may drop, which is unacceptable for lossless traffic classes. Setting a lower pause threshold, such as 80%, sends a PFC pause frame while still retaining free memory to absorb traffic during the delta time D. The same principle applies to the resume threshold. Setting it to 0% keeps the device idle during the delta time, reducing overall throughput.

PFC receive requires setting the egress rate for all associated queues to calculate pause time, even if it matches the wire speed. For example, if PFC runs on traffic class 3, the assigned ports require the `egress-rate-queue3` setting.

```routeros
/interface/ethernet/switch/qos/priority-flow-control/add name=pfctc3 traffic-class=3 rx=yes
/interface/ethernet/switch/qos/port/set sfp-sfpplus1,sfp-sfpplus2 pfc=pfctc3 egress-rate-queue3=10G
```
