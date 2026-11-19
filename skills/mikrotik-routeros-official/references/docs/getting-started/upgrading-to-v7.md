# Upgrading to v7

> Upgrade a router from RouterOS v6 to v7: what to prepare, how to run the upgrade, what the one-time configuration conversion does with BGP, OSPF, MPLS, routing filters, PIM-SM and User Manager, and what to check...

# Upgrading to v7

Upgrading from RouterOS v6 to v7 works the same way as an upgrade within v6: the router installs the new packages and reboots. During the first boot on v7, RouterOS converts the v6 configuration to the v7 format. Most routers need no further steps and work right after the reboot.

Routing is the part that changed most between the two major releases. Read the sections about BGP, OSPF, MPLS and routing filters before you upgrade a router that runs them, and check the result after the upgrade. PIM-SM configuration is not converted, and the User Manager database is migrated with a separate command.

## Prerequisites

- If the router runs an older release, upgrade it to the latest long-term or stable v6 release first. The [Upgrade](./installation-and-upgrade/upgrade) page describes the procedure.
- Use hardware with at least 64 MB of RAM. Do not run v7 on devices with less memory. `/system resource print` shows the memory as `total-memory`, and the architecture as `architecture-name`.
- Save a backup and a configuration export, and copy both files from the router to your computer:

  ```ros
  /system backup save name=before-v7 password=StrongPassword
  /export file=before-v7
  ```

  Replace `StrongPassword` with your own password. The backup is the file to load if you later want to convert the v6 configuration again. The export is a readable copy to compare with the converted configuration.
- Plan access to the router that does not depend on the routing protocols, for example a directly connected management network. A routing session that does not come up after the upgrade can leave a remote router unreachable.

## Packages

RouterOS v7 has one `routeros` package that contains most of the features that were separate packages in v6. Some features are extra packages in v7, and the router has the feature only when the package is installed:

- `user-manager` for User Manager.
- `wireless` for the `/interface/wireless` and `/caps-man` menus. The router keeps the configuration of these menus only when the package is installed.

When you upgrade with package files, upload these packages together with the `routeros` package.

The [Packages](./installation-and-upgrade/packages) page lists all extra packages.

The v6 `multicast` package has no v7 counterpart: multicast routing is part of the `routeros` package. With the `multicast` package installed, the `install` command of Check for updates can stop and report that the v7 package is missing. Upgrade with package files in that case. RouterOS v7 has no `lcd` and `kvm` packages.

## Upgrade the router

### Upgrade with Check for updates

On v6, select the `upgrade` channel, which offers the next major release, and install the offered version:

```ros
/system package update set channel=upgrade
/system package update check-for-updates
/system package update install
```

The router downloads the v7 version of the installed packages, for example `user-manager`, and reboots.

The `upgrade` channel can offer an intermediate v7 release instead of the latest one. After the router boots on v7, check for updates again in the channel that you want to follow, and install the latest release. Commands on v7 are written with slashes between the menu levels:

```ros
/system/package/update/set channel=stable
/system/package/update/check-for-updates
/system/package/update/install
```

### Upgrade with package files

1. Download the `routeros` package for the architecture of your router, and each extra package that you need, in the same version, from the [download page](https://mikrotik.com/download).
2. Upload the files to the root of the router's file list.
3. Reboot the router:

   ```ros
   /system reboot
   ```

The [Upgrade](./installation-and-upgrade/upgrade) page describes both methods in detail.

## Check the router after the upgrade

Check that every package you need is installed, and read the log for errors:

```ros
/system/package/print
/log/print where topics~"error|critical"
```

On a router that runs routing protocols, check the sessions, the filter rules and the routes:

```ros
/routing/bgp/session/print
/routing/ospf/neighbor/print
/mpls/ldp/neighbor/print
/routing/filter/rule/print where disabled
/routing/route/print where filtered
```

- An established BGP session has the `E` flag.
- An OSPF neighbor that is fully adjacent shows `state="Full"`.
- The third command lists the LDP neighbors. A working session has the `O` (operational) flag.
- The fourth command lists the disabled filter rules. The section about routing filters explains when the upgrade disables rules.
- The last command lists the routes that a filter rejected. Check that each of them is a route that you want to reject.

## What the upgrade converts

| Feature | Result of the upgrade |
| :-- | :-- |
| Interfaces | Converted. |
| Bridge and switching | Converted. |
| Wireless | Converted. Requires the `wireless` package. |
| CAPsMAN | Converted. Requires the `wireless` package. |
| Tunnels and PPP | Converted. |
| IP addresses, DHCP, DNS | Converted. |
| IPv6 | Converted. |
| Firewall, NAT and mangle | Converted. |
| Queues | Converted. |
| HotSpot | Converted. |
| Static routes, routing marks and routing rules | Converted. A routing mark becomes a routing table in `/routing/table`. |
| BGP | Converted to the new menu structure. Check the result. |
| OSPF | Converted to the new menu structure. Check the result. |
| MPLS | Converted. Check the result. |
| Routing filters | Converted to the new rule syntax. Check the result. |
| IGMP proxy | Converted. |
| PIM-SM | Not converted. Configure it again. |
| User Manager | Not converted. Migrate the database with a command. |
| Tools, scripts and scheduler | Converted. |

## The conversion runs only once

:::warning
The routing protocol configuration is converted only once, during the first boot on v7. If you downgrade the router to v6, change the configuration there and upgrade again, the router does not convert the changed configuration: it starts with the v7 configuration that it had before the downgrade.
:::

To convert a v6 configuration again, save a backup on v6 that contains the configuration, upgrade the router, and load the backup on v7 with the `force-v6-to-v7-configuration-upgrade=yes` option of [`/system/backup/load`](../cli-reference/system/backup/load):

```ros
/system/backup/load name=before-v7 password=StrongPassword \
    force-v6-to-v7-configuration-upgrade=yes
```

The router asks for confirmation, restores the v6 configuration, reboots and converts it. The loaded configuration replaces everything that you configured on v7 after the upgrade. Without such a backup, make the change in the v7 configuration instead. The [Backup](./configuration-management/backup) page describes how backups are saved and restored.

## BGP

The BGP configuration has a new structure. The v6 `instance` and `peer` menus are replaced with these menus:

- [`/routing/bgp/instance`](../cli-reference/routing/bgp/instance) holds the AS number and the router ID of a BGP instance.
- [`/routing/bgp/connection`](../cli-reference/routing/bgp/connection) defines a peer: where to connect or listen, and which instance the peer belongs to.
- [`/routing/bgp/template`](../cli-reference/routing/bgp/template) holds BGP protocol options that several connections can share. A template is also used for dynamic peers. Most options are similar to the v6 ones. The options that apply to received or sent routes are grouped under `input.` and `output.`, which shows in which direction an option works.
- [`/routing/bgp/session`](../cli-reference/routing/bgp/session) shows the state of all connected and disconnected peers.

A connection requires `instance` and `local.role`. The peer role is mandatory: for a basic setup, use `ebgp` or `ibgp`. Set `remote.address` to the address of the peer.

```ros
/routing/bgp/instance
add name=bgp1 as=65001 router-id=10.0.0.1
/routing/bgp/connection
add name=peer1 instance=bgp1 local.role=ebgp \
    remote.address=10.255.0.2 remote.as=65002
```

The `connect` and `listen` options set whether the router opens the connection to the peer, waits for the peer to connect, or does both. For a multihop peer, set `local.address` too.

The upgrade converts the v6 configuration as follows:

- Each v6 peer becomes a connection with the same name. The role is set from the v6 peer: `ebgp` or `ibgp`, and `ibgp-rr` for a peer with `route-reflect=yes`.
- `in-filter` and `out-filter` become `input.filter` and `output.filter-chain`.
- `update-source` becomes `local.address`.
- The v6 `/routing bgp network` menu does not exist in v7. In v7, you add the networks to an address list in `/ip/firewall/address-list` and set the name of the list in the `output.network` option. The upgrade puts the v6 networks into the `bgp-networks` list. The router advertises a network only when a matching IGP route exists.

After the upgrade, check that each connection refers to an instance with the right AS number and router ID, and that the sessions are established:

```ros
/routing/bgp/instance/print
/routing/bgp/connection/print
/routing/bgp/session/print
```

The [`/routing/stats`](../cli-reference/routing/stats/process) menu shows debugging information about all routing processes, for example their memory use.

The [BGP](../user-guides/routing-and-networking-protocols/unicast/bgp) page describes the configuration in detail.

## OSPF

OSPFv2 and OSPFv3 are configured in one menu, [`/routing/ospf`](../cli-reference/routing/ospf/instance). A new v7 router has no default instance and no default area: to start OSPF, create an instance, add an area to it, and add an interface template.

```ros
/routing/ospf/instance
add name=ospf-v2 version=2 router-id=10.0.0.1
/routing/ospf/area
add name=backbone-v2 area-id=0.0.0.0 instance=ospf-v2
/routing/ospf/interface-template
add area=backbone-v2 networks=10.255.0.0/30
```

RouterOS v7 matches interfaces against the entries of [`/routing/ospf/interface-template`](../cli-reference/routing/ospf/interface-template) and runs OSPF on each matched interface with the settings of the template. The [`interface`](../cli-reference/routing/ospf/interface) and [`neighbor`](../cli-reference/routing/ospf/neighbor) menus show the matched interfaces and the discovered neighbors for monitoring.

The upgrade converts the v6 configuration as follows:

- The v6 `default` instance becomes the `default-v2` instance, and the OSPFv3 instance becomes `default-v3`.
- Each area gets the suffix of its instance: the v6 `backbone` area becomes `backbone-v2` for OSPFv2 and `backbone-v3` for OSPFv3.
- The v6 `network` and `interface` entries become interface templates. Interface settings such as the network type, cost and authentication are kept.
- The `in-filter` and `out-filter` chains become `in-filter-chain` and `out-filter-chain` of the instance.

The [OSPF](../user-guides/routing-and-networking-protocols/unicast/ospf) page describes the configuration in detail.

## MPLS

Upgrade MPLS setups with caution, and save a backup before the upgrade.

The upgrade converts the LDP settings to an entry in [`/mpls/ldp`](../cli-reference/mpls/ldp) with the same LSR ID and transport address, and keeps the LDP interfaces, the accept and advertise filters, and the VPLS interfaces.

LDP needs a route to the transport address of each neighbor. If the routes come from a routing protocol, the LDP sessions come up only after that protocol works: check OSPF and the routing filters first, then `/mpls/ldp/neighbor/print`.

The [MPLS](../user-guides/routing-and-networking-protocols/mpls) page describes the configuration in detail.

## Routing filters

Routing filters use a script-like syntax in v7. A rule in [`/routing/filter/rule`](../cli-reference/routing/filter/rule) can have the form "if .. then": it sets route attributes or applies an action when the condition matches.

```ros
/routing/filter/rule
add chain=bgp-in rule="if (dst in 10.0.0.0/8) { accept; }"
```

Rules of one chain are processed from the top, like firewall rules. A rule without an action changes the route and passes it to the next rule, so several `set` statements can be written one per line. The order of `set` statements matters, and one statement per rule shows from top to bottom what is applied:

```ros
/routing/filter/rule
add chain=bgp-set rule="set bgp-local-pref 150;"
add chain=bgp-set rule="set distance 77;"
add chain=bgp-set rule="if (dst in 10.0.0.0/8) { accept; }"
```

The upgrade converts each v6 filter rule to one v7 rule in the same chain, and keeps the comment. Check these points after the upgrade:

- A v6 option that v7 does not support is left out of the converted rule. The router adds a note to the comment of the rule that starts with `upgrade-notes:` and names the option, for example `'set-routing-mark to-isp2' not supported`, and disables all rules of that chain. While its rules are disabled, the chain accepts no routes. Review the chain, replace the unsupported option, and enable the rules.
- A route that no rule of the chain accepts is rejected. In v6, a route that matched no rule was accepted. Make sure that each chain ends with the action that you expect for the remaining routes.

The [Route Selection and Filtering](../user-guides/routing-and-networking-protocols/route-selection-and-filtering) page describes the rule syntax, and [Moving from ROSv6 to ROSv7](../user-guides/routing-and-networking-protocols/moving-from-rosv6-to-rosv7#routing-filters) has more examples of converted rules.

## PIM-SM

The upgrade does not preserve the PIM configuration. Multicast routing is configured in the [`/routing/pimsm`](../cli-reference/routing/pimsm) menu, and the separate `multicast` package is not required. Configure PIM-SM again after the upgrade as described on the [PIM-SM](../user-guides/routing-and-networking-protocols/multicast/pim-sm) page.

## User Manager

RouterOS v7 has a new implementation of [User Manager](../authentication-authorization-accounting/user-manager). It is configured in WinBox and in the console; the web interface for administrators is not available.

The upgrade does not convert the User Manager configuration: a direct migration is not possible. The v6 database stays in its folder on the router, and the v7 User Manager starts with an empty database. The `database` menu shows the folder of the v6 database when it finds one:

```ros
/user-manager/database/print
```

```text
               db-path: /user-manager5
  found-legacy-db-path: user-manager  
               db-size: 148.6KiB      
       free-disk-space: 27.6MiB       
```

To migrate the v6 database, run [`/user-manager/database/migrate-legacy-db`](../cli-reference/user-manager/database/migrate-legacy-db) with the path of that folder:

```ros
/user-manager/database/migrate-legacy-db database-path=user-manager
```

The command migrates users, profiles, limitations, the links between them, and routers. When the v7 database already contains data, the command stops with an error. Add `overwrite=yes` to delete the data of the v7 database and migrate again.

Check the migrated entries, for example the limits of each limitation, before you enable User Manager. Alternatively, configure User Manager from scratch. The system [backup](./configuration-management/backup) does not contain the User Manager database.

## New features in v7

RouterOS v7 has a new kernel. Routing no longer uses a route cache, and some tasks use more CPU and RAM than on v6.

- New NTP client and server implementation.
- Individual packages are merged: only the `routeros` package and a few extra packages remain.
- New command line style with slashes between menu levels, for example `/ip/address/print`. Commands in the v6 style are still accepted.
- Let's Encrypt certificates.
- REST API.
- UEFI boot mode on x86.
- CHR FastPath support for the vmxnet3 and virtio-net drivers.
- CAKE and FQ-CoDel queue types.
- IPv6 NAT.
- Layer 3 hardware offloading, QoS and MLAG on devices with Marvell Prestera switch chips.
- MBIM driver with basic support for all modems that have an MBIM mode.
- VRRP grouping, and connection tracking synchronization between VRRP nodes.
- Virtual eXtensible Local Area Network (VXLAN).
- L2TPv3.
- OpenVPN over UDP.
- WireGuard.
- Hardware offloaded VLAN filtering on RTL8367 (RB4011, RB1100AHx4) and MT7621 (hEX, hEX S, RBM33G) switch chips.
- ZeroTier on ARM and ARM64 devices.
- CPU frequency scaling on x86 devices.
