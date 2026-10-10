# Precision Time Protocol

> Precision Time Protocol (PTP, IEEE 1588-2008) clock synchronization on RouterOS: supported hardware, profiles (802.1AS, AES67, G.8275.1, SMPTE 2059), ports, hardware timestamping and synchronization monitoring.

# Precision Time Protocol

The Precision Time Protocol (PTP, IEEE 1588-2008, also known as PTPv2) synchronizes clocks across a local network, which matters in telecommunications, broadcast, audio production and industrial automation. MikroTik's implementation features:

- Two-step Ordinary Clock and Boundary Clock.
- Hardware timestamping, which brings clock synchronization into the nanosecond range.
- IPv4 and Layer 2 multicast transport modes.
- End-to-End (E2E) and Peer-to-Peer (P2P) delay mechanisms.
- Profiles: 802.1AS (AVB/TSN, per IEEE 802.1AS-2020), AES67 (audio over IP), G.8275.1 (telecom frequency and phase synchronization) and SMPTE 2059 (professional broadcast).

:::info
PTP support is hardware dependent; see [supported devices](#supported-devices). Devices not listed there do not have the `/system/ptp` menu at all. The MGMT (management) port is not supported for PTP on any device; "all ports" refers to all data interfaces, excluding the MGMT port.
:::

## Configure PTP

Configuration has two steps: create a PTP profile in [`/system/ptp`](../cli-reference/system/ptp), then assign the ports that participate in it in [`/system/ptp/port`](../cli-reference/system/ptp/port).

Create a profile instance (this example uses the 802.1AS profile):

```ros
/system/ptp/add name=ptp1 profile=802.1as
```

PTP only syncs when all clocks in the chain run the same profile, so make the profile (and with it the domain, transport and delay mode) match your grandmaster and the rest of the PTP network.

Profile parameters left at `auto` take the values their profile defines (for example 802.1AS sets `priority1=246`, `priority2=248`, transport on layer 2 and P2P delay measurement — the per-profile presets are listed in the CLI reference rows). Change them manually only when the chosen standard allows it; G.8275.1, 802.1AS, SMPTE 2059 and AES67 each define their own required values.

```ros
[admin@MikroTik] > /system/ptp/print
 Flags: I - inactive, X - disabled
 0   name="ptp1" priority1=auto priority2=auto delay-mode=auto transport=auto profile=802.1as domain=auto
```

Then assign the ports of the profile. Here sfp28-12 is connected to the grandmaster clock, while sfp28-1 and sfp28-2 connect to an ordinary clock (slave):

```ros
/system/ptp/port/add interface=sfp28-1 ptp=ptp1
/system/ptp/port/add interface=sfp28-2 ptp=ptp1
/system/ptp/port/add interface=sfp28-12 ptp=ptp1
```

A port can also have its role pinned instead of letting the best master clock algorithm decide: with `role=bmca` the algorithm chooses master or slave, on a known topology you can pin a port directly with `role=master` or `role=slave`. `ptp-mode` in [`/system/ptp`](../cli-reference/system/ptp) selects between ordinary-clock and transparent-clock behaviour.

### PTP on VLAN ports

When PTP ports are also part of VLANs on your boundary clock device, you must add a bridge interface as an untagged port in the [bridge VLAN table](../bridging-and-switching/user-guides/bridge-vlan-table.md) for every entry that includes a PTP port. Continuing the example with sfp28-1 in VLAN 10 and sfp28-2 in VLAN 20:

```ros
/interface/bridge/add name=bridge1
/interface/bridge/port/add bridge=bridge1 interface=sfp28-1 pvid=10
/interface/bridge/port/add bridge=bridge1 interface=sfp28-2 pvid=20
/interface/bridge/vlan/add bridge=bridge1 vlan-ids=10 \
    untagged=bridge1,sfp28-1
/interface/bridge/vlan/add bridge=bridge1 vlan-ids=20 \
    untagged=bridge1,sfp28-2
```

This is necessary because the bridge interface functions as a bridge port towards the CPU. Therefore, it must be included in the VLAN table along with the PTP ports, so packets can be correctly received from the physical port and forwarded to the CPU through the bridge.

If PTP instead arrives tagged over a trunk port, set the tag directly on the PTP port with `vlan-id` in [`/system/ptp/port`](../cli-reference/system/ptp/port).

:::note
This applies to the IPv4 and L2-forwardable (01-1B-19-00-00-00) transport modes. The only exception is L2-non-forwardable (01-80-C2-00-00-0E), where the bridge does not have to be included in the bridge VLAN table.

To check the default (auto) transport mode values for each profile, refer to the [`transport`](../cli-reference/system/ptp) description in the CLI reference.
:::

### PTP with IGMP snooping

If IGMP snooping is enabled on your bridge and VLANs are configured as shown above, manually add static Multicast Database (MDB) entries for each VLAN containing PTP ports that use **IPv4** (224.0.1.129) as their transport mode. This ensures proper forwarding of PTP multicast traffic:

```ros
/interface/bridge/mdb/add group=224.0.1.129 bridge=bridge1 \
    ports=bridge1 vid=10
/interface/bridge/mdb/add group=224.0.1.129 bridge=bridge1 \
    ports=bridge1 vid=20
```

Static MDB entries in a PTP setup are only required when IGMP snooping is enabled alongside VLANs.

## Monitor synchronization

Check whether the ports are up and running first:

```ros
/system/ptp/status/print
```

The `state`, `delay` and `as-capable` columns show where a port is stuck before synchronization settles.

Then monitor the profile instance (by number or name) with [`/system/ptp/monitor`](../cli-reference/system/ptp/monitor):

```ros
/system/ptp/monitor ptp1
```

An example of a synchronized clock:

```text
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

The values to watch: `i-am-gm`/`gm-clock-id` say who is the grandmaster, the `offset` is the time error against the master clock, `freq-drift` the long-term clock frequency correction, and `slave-port-delay` the measured one-way path delay of the slave port.

## Supported devices

- **CRS326-24G-2S+:** Supported only on Gigabit Ethernet ports.
- **CRS328-24P-4S+:** Supported only on Gigabit Ethernet ports.
- **CRS317-1G-16S+:** Supported on all ports.
- **CRS326-24S+2Q+:** Supported on SFP+ and QSFP+ interfaces.
- **CRS312-4C+8XG:** Supported on all ports.
- **CRS318-16P-2S+:** Supported only on Gigabit Ethernet ports.
- **CRS318-1Fi-15Fr-2S:** Supported only on 100M Ethernet ports.
- **CCR2116-12G-4S+:** Supported on all ports.
- **CCR2216-1G-12XS-2XQ:** Supported on all ports.
- **CRS518-16XS-2XQ:** Supported on all ports.
- **CRS504-4XQ:** Supported on all ports.
- **CRS510-8XS-2XQ:** Supported on all ports.
- **CRS520-4XS-16XQ:** Supported on all ports.
- **CRS320-8P-8B-4S+RM:** Supported only on Gigabit Ethernet ports.
- **CRS326-4C+20G+2Q+:** Supported on all ports.
- **RDS2216-2XG-4S+4XS-2XQ:** Supported on all ports.

:::info
Devices not listed in this section do not support Precision Time Protocol.
:::

## Technical details

Profiles preset the parameters whose values you left at `auto`:

| Profile | priority1 | priority2 | domain | transport | delay-mode |
| :-- | :-- | :-- | :-- | :-- | :-- |
| default | 128 | 128 | 0 | ipv4 | e2e |
| 802.1AS | 246 | 248 | 0 | l2-non-forwardable | p2p |
| AES67 | 128 | 128 | 0 | ipv4 | e2e |
| G.8275.1 | 128 | 128 | 24 | l2-non-forwardable | e2e |
| SMPTE 2059 | 128 | 128 | 127 | ipv4 | e2e |

- IPv4 transport multicasts PTP primary messages to 224.0.1.129 and peer delay messages to 224.0.0.107.
- L2-forwardable uses the multicast MAC 01-1B-19-00-00-00, which PTP-unaware bridges forward; L2-non-forwardable uses 01-80-C2-00-00-0E, which compliant bridges cannot forward, so PTP communication stays on the local link.
- Domains separate independent PTP instances on one network; allowed ranges differ per profile (0-127 for most profiles, 24-43 for G.8275.1).

For all parameters, see the [`/system/ptp`](../cli-reference/system/ptp), [`/system/ptp/port`](../cli-reference/system/ptp/port), [`/system/ptp/status`](../cli-reference/system/ptp/status) and [`/system/ptp/monitor`](../cli-reference/system/ptp/monitor) CLI reference pages.
