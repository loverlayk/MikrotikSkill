# Precision Time Protocol

> MikroTik RouterOS documentation introduces Precision Time Protocol (PTP) for sub-microsecond clock synchronization across networks, supporting IEEE 1588-2008 with hardware timestamping and multiple profile options...

# Precision Time Protocol

The Precision Time Protocol (PTP), developed by the Institute of Electrical and Electronics Engineers (IEEE), is a protocol used to synchronize clocks across a local area network. It is essential in industries and applications where precise timing is critical, such as telecommunications, finance, and industrial automation. PTP typically ensures time accuracy in the sub-microsecond range, but nanosecond-level accuracy is also achievable when hardware requirements are met. MikroTik’s implementation of PTP supports IEEE 1588-2008 (PTPv2) and includes hardware timestamping capabilities that ensure synchronization within the nanosecond range. For additional details on MikroTik’s PTP features, please refer to the list below.

- Two-step Ordinary Clock and Boundary Clock.
- Hardware timestamping, ensuring clock synchronization in nanosecond(ns) range.
- IPv4 and Layer 2 (L2) multicast transport modes.
- End-to-End (E2E) and Peer-to-Peer (P2P) delay mechanisms.
- IEEE 1588-2008 (PTPv2).
- Profile Support for:
  - 802.1AS: Timing and synchronization for Audio Video Bridging (AVB) and Time-Sensitive Networking (TSN), based on IEEE 802.1AS-2020.
  - AES67: High-performance audio-over-IP interoperability.
  - G.8275.1: Frequency and phase synchronization in PTP-aware networks.
  - SMPTE: Audio/video synchronization in professional broadcast environments.

:::info
Mikrotik PTP support is hardware-dependent; please refer to the list of [supported devices.](./precision-time-protocol.md#supported-devices)
:::

## General Properties

**Sub-menu:** `/system/ptp`

| Property | Description |
| :-- | :-- |
| **port** | Sub-menu used for adding, removing, or viewing assigned ports. |
| **status** | Sub-menu that shows PTP ports, their state, and delay on slave ports. |
| **comment** (*string*; Default: ) | Short description of the PTP profile. |
| **name** (*string*; Default: ) | Name of the PTP profile. |
| **domain** (Default: **auto**) | Identifier used to separate different PTP instances.  Each PTP profile defines its own allowed domain range and default value:  • 802.1AS    range: 0–127, default: 0 (auto) • AES67        range: 0–127, default: 0 (auto) • G.8275.1   range: 24–43, default: 24 (auto) • SMPTE       range: 0–127, default: 127 (auto) • Default      range: 0–127, default: 0 (auto)  Notes: - "auto" selects the profile’s default domain value. |
| **delay-mode** (*auto \| e2e \| p2p*; Default: **auto**) | auto - selects the delay mode automatically depending on the profile being used.e2e - utilizes the delay request-response mechanism.p2p - utilizes the peer delay mechanism. |
| **priority1** (*integer [0..255]*; auto; Default: **auto**) | Parameter which takes part in the election of a grandmaster clock. |
| **priority2** (*integer [0..255]*; auto; Default: **auto**) | Parameter which takes part in the election of a backup grandmaster clock. |
| **profile**(*802.1as; aes67; g8275.1; smpte; default;* Default: **default**) | Each profile comes with its own predefined auto values for PTP operating parameters and options: 802.1as is an adaptation of PTP for use with Audio Video Bridging and Time-Sensitive Networking. Default(auto) values: priority1=246, priority2=248, transport=l2-non-forwardable, delay-mode=p2p.aes67 profile is for high-performance audio-over-IP interoperability. Default(auto) values: priority1=128, priority2=128, domain=0, transport=ipv4, delay-mode=e2e.g8275.1 profile is for frequency and phase synchronization in a fully PTP-aware network. Default(auto) values: priority1=128, priority2=128, domain=24, transport=l2-non-forwardable, delay-mode=e2e.smpte profile is for the synchronization of audio/video equipment in a professional broadcast environment. Default(auto) values: priority1=128, priority2=128, domain=127, transport=ipv4, delay-mode=e2e.default profile, PTPv2 default configuration, allows for more configuration options than other profiles. Default(auto) values: priority1=128, priority2=128, domain=0, transport=ipv4, delay-mode=e2e. |
| **transport** (*auto; ipv4; l2-forwardable; l2-non-forwardable;* Default: **auto**) | Transport protocol to be used: auto - automatically selects the transport mode based on the PTP profile in use.ipv4 - uses the IPv4 multicast addresses 224.0.1.129 for PTP primary messages and 224.0.0.107 for PTP peer delay messages.l2-forwardable - uses the multicast MAC address <code>01-1B-19-00-00-00</code>, which is being forwarded through PTP-unaware network equipment.l2-non-forwardable - uses the multicast MAC address <code>01-80-C2-00-00-0E</code>, ensuring that PTP messages are not forwarded through PTP-unaware network equipment. |

## Configuration

Configuring Precision Time Protocol (PTP) on MikroTik devices is a straightforward process. The primary steps involve creating a PTP profile and assigning the relevant ports to this profile for PTP operation.

#### Create a PTP Profile

To create a PTP profile, use the following command. In this example, we use the 802.1as profile, but you can select from other available profiles as needed:

```ros
/system/ptp/add name=ptp1 profile=802.1as
```

To verify that the profile has been created successfully, execute:

```routeros
/system/ptp/print
```

The output will display the created profile with its current settings:

```routeros
 Flags: I - inactive, X - disabled 
 0   name="ptp1" priority1=auto priority2=auto delay-mode=auto transport=auto profile=802.1as domain=auto  
```

:::note
By default, parameters for each profile are configured to "auto," which automatically selects the appropriate values based on the profile chosen. Before making manual adjustments, verify that the settings conform to relevant standards (e.g., ITU-T G.8275.1, IEEE 802.1as, SMPTE, AES67).
:::

#### Assign Ports to the PTP Profile

As the final step, assign the ports that will participate in PTP. For example, let's include a few sfp28 interfaces.  SFP28-12 is connected to the grandmaster clock, while SFP28-1 and SFP28-2 are connected to an ordinary clock/slave:

```ros
/system/ptp/port/add interface=sfp28-1 ptp=ptp1
/system/ptp/port/add interface=sfp28-2 ptp=ptp1
/system/ptp/port/add interface=sfp28-12 ptp=ptp1
```

#### PTP on VLAN Ports

When PTP ports are also part of VLANs on your boundary clock device, you must add a bridge interface as an untagged port in the [Bridge VLAN Table](../bridging-and-switching/user-guides/bridge-vlan-table.md) for every entry that includes a PTP port.

This is necessary because the bridge interface functions as a bridge port towards the CPU. Therefore, it must be included in the VLAN table along with the PTP ports ensuring that packets can be correctly received from the physical port and forwarded to the CPU via the bridge. Let's continue with our previous configuration to make this clearer:

```routeros
# Create a new bridge interface
/interface/bridge/add name=bridge1

# Assign the ports that will be part of this bridge
/interface/bridge/port/add bridge=bridge1 interface=sfp28-1 pvid=10
/interface/bridge/port/add bridge=bridge1 interface=sfp28-2 pvid=20

# Create new entries for Bridge VLAN Table
/interface/bridge/vlan/add bridge=bridge1 vlan-ids=10 untagged=bridge1,sfp28-1
/interface/bridge/vlan/add bridge=bridge1 vlan-ids=20 untagged=bridge1,sfp28-2
```

:::note
This applies to the IPv4 and L2-forwardable (01-1B-19-00-00-00) transport modes. The only exception is L2-non-forwardable (01-80-C2-00-00-0E), in which case there is no need to add a bridge interface as an untagged port in the Bridge VLAN Table.

To check the default(auto) transport mode values for each profile, please refer to the ["General Properties](./precision-time-protocol.md#general-properties)" section.
:::

#### PTP with IGMP Snooping

If IGMP snooping is enabled on your bridge and VLANs are configured as shown in the previous example, you must manually add static Multicast Database (MDB) entries for each VLAN containing PTP ports that use **IPv4** (224.0.1.129) as their transport mode. This ensures proper forwarding of PTP multicast traffic.

```routeros
/interface/bridge/mdb/add group=224.0.1.129 bridge=bridge1 ports=bridge1 vid=10
/interface/bridge/mdb/add group=224.0.1.129 bridge=bridge1 ports=bridge1 vid=20
```

:::note
Static MDB entries in PTP setup are only required when IGMP snooping is enabled alongside VLANs.
:::

## Monitoring

To monitor the status and performance of the PTP profile, use the following command:

```ros
/system/ptp/monitor 0
```

The output will provide detailed information about the profile's operational status:

```routeros
name: ptp1
clock-id: 64:D1:54:FF:FE:EB:AD:C7
priority1: 246
priority2: 248
i-am-gm: no
gm-clock-id: 64:D1:54:FF:FE:EB:AE:C3
gm-priority1: 100
gm-priority2: 248
master-clock-id: 64:D1:54:FF:FE:EB:AE:C3
slave-port: ether1
freq-drift: 2690 ppb
offset: 3 ns
hw-offset: -889419842 ns
slave-port-delay: 306 ns
```

This information includes critical details such as the clock IDs, priority values, and timing offsets, which are essential for monitoring the accuracy and synchronization of your PTP setup.

#### Monitor Properties

| Property | Description |
| :-- | :-- |
| **clock-id:** | Local clock identifier, used to uniquely identify the clock within the PTP network. |
| **priority1:** | The priority parameter used in the election of the grandmaster clock. A lower value indicates higher priority. |
| **priority2:** | The priority parameter used in the election of the backup grandmaster clock. A lower value indicates higher priority. |
| **i-am-gm:** yes | no | Indicates if the device is a grandmaster clock (`yes`) or not (`no`). |
| **gm-clock-id:** | Identifier of the grandmaster clock. This is the clock providing the primary time source. |
| **gm-priority1:** | The `priority1` value of the grandmaster clock as seen from the slave device. |
| **gm-priority2:** | The `priority2` value of the grandmaster clock as seen from the slave device. |
| **master-clock-id:** | Identifier of the master clock in the PTP communication path. This may be a grandmaster clock or a boundary clock, depending on the network topology. |
| **slave-port:** | The port on the device that is connected to the master or grandmaster clock. |
| **freq-drift:** | The frequency drift between the master and slave clocks, measured in parts per billion (ppb). This indicates how much the slave clock's frequency deviates from the master clock's frequency. |
| **offset:** | The time difference between the master and slave clocks, measured in nanoseconds (ns). This reflects the synchronization accuracy. |
| **hw-offset:** | Offset difference from the hardware clock. |
| **slave-port-delay:** | The time delay for packets traveling between two devices, measured in nanoseconds (ns). This delay can be influenced by the quality of cables and transceivers used in the network. |
| **name**  | Name of the PTP profile. |

## Supported Devices

- **CRS326-24G-2S+:** Supported only on Gigabit Ethernet ports.
- **CRS328-24P-4S+:** Supported only on Gigabit Ethernet ports.
- **CRS317-1G-16S+:** Supported on all ports.
- **CRS326-24S+2Q+:** Supported on SFP+ and QSFP+ interfaces.
- **CRS312-4C+8XG:** Supported on all ports.
- **CRS318-16P-2S+:** Supported only on Gigabit Ethernet ports.
- **CRS318-1Fi-15Fr-2S:** Supported only on 100M Ethernet ports.

### PTP Support Added in RouterOS Version 7.16 and Later

- **CCR2116-12G-4S+:** Supported on all ports.
- **CCR2216-1G-12XS-2XQ:** Supported on all ports.
- **CRS518-16XS-2XQ:** Supported on all ports.
- **CRS504-4XQ:** Supported on all ports.
- **CRS510-8XS-2XQ:** Supported on all ports.
- **CRS520-4XS-16XQ:** Supported on all ports.

### PTP Support Added in RouterOS Version 7.17 and Later

- **CRS320-8P-8B-4S+RM:** Supported only on Gigabit Ethernet ports.
- **CRS326-4C+20G+2Q+:** Supported on all ports.

### PTP Support Added in RouterOS Version 7.20 and Later

- **RDS2216-2XG-4S+4XS-2XQ:** Supported on all ports.

:::info
Devices not listed in this section do not support Precision Time Protocol.
:::
:::info
The MGMT (management) port is not supported for PTP on any device. "All ports" refers to all data interfaces, excluding the MGMT port.
:::
