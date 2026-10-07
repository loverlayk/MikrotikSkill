# Upgrading to v7

> This page outlines the steps and considerations for upgrading MikroTik RouterOS to version 7, detailing compatibility with features like BGP, OSPF, MPLS, and user manager settings. It highlights mandatory parameters...

# Upgrading to v7

## Introduction

This document describes the recommended steps for upgrading RouterOS to the v7 major release and the possible caveats when doing so.

Upgrading from v6 to v7 works the same way as upgrading within v6 releases. Follow the [Upgrade manual](./installation-and-upgrade/upgrade) for more detailed steps. If you are running RouterOS version 6 or earlier, you should first upgrade to the latest stable or long-term release in v6.

:::info
In most RouterOS setups that run fine with the aforementioned v6 versions, no extra steps are required. Upgrading to v7 automatically converts the configuration and your device functions right away.

:::

:::note
You should not run v7 on hardware that does not have at least 64 MB of RAM.

:::

## Feature list compatibility

As previously stated, nearly all RouterOS systems can use the "Check for updates" functionality and upgrade to v7 in a few clicks, but some features may require extra steps:

| Feature | Status |
| :-- | :-- |
| CAPsMAN | OK |
| Interfaces | OK |
| Wireless | OK |
| Bridge/Switching | OK |
| Tunnels/PPP | OK |
| IPv6 | OK |
| BGP | OK, but attention is required  [\*](#bgp)  |
| OSPF | OK, but attention is required [\*\*](#ospf) |
| MPLS | OK, but attention is required [\*\*\*](#mpls) |
| Routing filters | OK, but attention is required [\*\*\*\*](#routing-filters) |
| PIM-SM | See [notes](#pim-sm) |
| IGMP Proxy | OK |
| Tools | OK |
| Queues | OK |
| Firewall | OK |
| HotSpot | OK |
| Static Routing | OK |
| User Manager | See [notes](#user-manager) |

:::danger
The routing protocol configuration upgrade is triggered only once. This means that if a router was downgraded to v6, the configuration was modified and the router got upgraded back to v7, then the resulting configuration is the one that was present before the downgrade. To re-trigger v6 configuration conversion, load a v6 backup with the [`force-v6-to-v7-configuration-upgrade=yes`](../cli-reference/system/backup/load) option.

:::

## BGP

All known configurations upgrade from 6.x to 7.x successfully. But keep in mind that there is a complete redesign of the configuration. v7 BGP implementation provides [`connection`](../cli-reference/routing/bgp/connection), [`template`](../cli-reference/routing/bgp/template) and [`session`](../cli-reference/routing/bgp/session) menus.

**`Template`** contains all BGP protocol-related configuration options. It can be used as a template for dynamic peers and to apply a similar config to a group of peers. Most of the parameters are similar to the previous implementation except that some are grouped in the output and input sections, making the config more readable and easier to understand whether the option is applied on input or output.

The BGP **`connection`** minimal set of parameters is [`remote.address`](../cli-reference/routing/bgp/connection#remote.address), [`template`](../cli-reference/routing/bgp/template), [`connect`](../cli-reference/routing/bgp/connection#connect), [`listen`](../cli-reference/routing/bgp/connection#listen) and [`local.role`](../cli-reference/routing/bgp/connection#local.role).  
Connect and listen parameters specify whether peers will try to connect and listen to a remote address or just connect or just listen. In setups where a peer uses the multi-hop connection [`local.address`](../cli-reference/routing/bgp/connection) must be configured too. Peer role is now a mandatory parameter. For basic setups, you can just use ibgp, ebgp.

Now you can monitor the status of all connected and disconnected peers from the [`/routing/bgp/session`](../cli-reference/routing/bgp/session) menu.  
Other useful debugging information on all routing processes can be monitored from the [`/routing/stats`](../cli-reference/routing/stats/process) menu.

Networks are added to the firewall address-list and referenced in the BGP **`connection`** configuration.

## OSPF

All known configurations upgrade from 6.x to 7.x successfully.  
OSPFv2 and OSPFv3 are now merged into one single menu [`/routing/ospf`](../cli-reference/routing/ospf/instance). There are no default instances and areas. To start OSPF you need to create an instance and then add an area to the instance.

RouterOS v7 uses templates to match the interface against the template and apply configuration from the matched template. OSPF menus [`interface`](../cli-reference/routing/ospf/interface) and [`neighbor`](../cli-reference/routing/ospf/neighbor) contain read-only entries for status monitoring.

## MPLS

Upgrade MPLS setups with caution, and back up the configuration before the upgrade.

## Routing filters

All supported options are upgraded without any issue, in the case of an unsupported option - an empty entry is created. The routing filter configuration is changed to a script-like configuration.

The rule now can have "if .. then" syntax to set parameters or apply actions based on conditions from the "if" statement.

Multiple rules without action are stacked in a single rule and executed in order like a firewall, because the "set" parameter order is important, and writing one "set" per line allows for an easier understanding from top to bottom on what actions were applied.

More RouterOS v7 routing filter examples are [here](../user-guides/routing-and-networking-protocols/moving-from-rosv6-to-rosv7.md#routing-filters).

## PIM-SM

Upgrading RouterOS to v7 does not preserve PIM-related configuration. After the upgrade, multicast routing configuration is available under the [`/routing/pimsm`](../cli-reference/routing/pimsm) menu and an additional "multicast" package is no longer required. More information is available [here](../user-guides/routing-and-networking-protocols/multicast/pim-sm).

## User Manager

RouterOS v7 provides the new and redesigned implementation of User Manager, configuration is now integrated into RouterOS WinBox and console (WEB admin configuration interface is not available), more information is available [here](../authentication-authorization-accounting/user-manager). Direct migration from the older User Manager is not possible, you can migrate the older database by using [`/user-manager/database/migrate-legacy-db`](../cli-reference/user-manager/database/migrate-legacy-db). However, you may want to start configuration from scratch.

## New features

A New Kernel is implemented in RouterOS v7, which leads to performance changes due to route cache, as well as some tasks may require higher CPU and RAM usage for different processes.

- Completely new NTP client and server implementation.
- Merged individual packages, only bundle and a few extra packages remain *(dropped support for LCD and KVM packages)*.
- New Command Line Interface (CLI) style (RouterOS v6 commands are still supported).
- Support for Let's Encrypt certificate generation.
- Support for REST API.
- Support for UEFI boot mode on x86.
- CHR FastPath support for "vmxnet3" and "virtio-net" drivers.
- Support for "Cake" and "FQ\_Codel" type queues.
- Support for IPv6 NAT.
- Support for Layer 3 hardware acceleration, QoS, and MLAG on MikroTik devices with Marvell Prestera switch.
- Support for MBIM driver with basic functionality support for all modems with MBIM mode.
- Support for VRRP grouping and connection tracking data synchronization between nodes.
- Support for Virtual eXtensible Local Area Network (VXLAN).
- Support for L2TPv3.
- Support for OpenVPN UDP transport protocol.
- Support for WireGuard.
- Support for hardware offloaded VLAN filtering on RTL8367 (RB4011, RB100AHx4) and MT7621 (hEX, hEX S, RBM33G) switches.
- Support for ZeroTier on ARM and ARM64 devices.
- Support for CPU frequency scaling for x86 devices.

## Dropped support

In RouterOS v7, support has been dropped for:

- LCD package
- KVM package
