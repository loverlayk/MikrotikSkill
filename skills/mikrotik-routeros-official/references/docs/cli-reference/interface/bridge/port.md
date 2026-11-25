# port

> RouterOS directory reference for /interface/bridge/port.

-----------

## interface/bridge/port 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offload">hw-offload</ArgTableRow>
<ArgTableRow arg="Y" typ="managed">managed</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="alt { interface: iface_enum
, interface-list: enum
 }" mandatory="1">Interface or interface list to add to the bridge.</ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" mandatory="1">The bridge interface the port is grouped into.</ArgTableRow>
<ArgTableRow arg="priority" typ="enum (0x00 | 0x10 | 0x20 | 0x30 | 0x40 | 0x50 | 0x60 | 0x70 | 0x80 | 0x90 | 0xa0 | 0xb0 | 0xc0 | 0xd0 | 0xe0 | 0xf0) { 0x00:0x00, 0x10:0x10, 0x20:0x20, 0x30:0x30, 0x40:0x40, 0x50:0x50, 0x60:0x60, 0x70:0x70, 0x80:0x80, 0x90:0x90, 0xa0:0xa0, 0xb0:0xb0, 0xc0:0xc0, 0xd0:0xd0, 0xe0:0xe0, 0xf0:0xf0 }">
Port priority used by STP to determine the root port, and by MSTP to determine the root port between regions. Must be set in steps of 16 (0x10).

Default: 0x80.
</ArgTableRow>
<ArgTableRow arg="path-cost" typ="num">
Path cost to the interface, used by STP and RSTP to determine the best path, and by MSTP to determine the best path between regions. If not set, the bridge determines the cost automatically from the interface speed and the `port-cost-mode` setting. Clear a manual value with `!path-cost`:

```ros
/interface/bridge/port/set [find interface=sfp28-1] !path-cost
```

Use [port monitor](./monitor) to observe the applied path cost. This property has no effect when `protocol-mode` is set to `none`.
</ArgTableRow>
<ArgTableRow arg="internal-path-cost" typ="num">
Path cost to the interface for MSTI0 inside a region. If not set, the bridge determines the cost automatically from the interface speed and the `port-cost-mode` setting. Clear a manual value with `!internal-path-cost`:

```ros
/interface/bridge/port/set [find interface=sfp28-1] !internal-path-cost
```

Use [port monitor](./monitor) to observe the applied internal path cost. This property only has an effect when `protocol-mode` is set to `mstp`.
</ArgTableRow>
<ArgTableRow arg="edge" typ="enum (auto | yes | no | yes-discover | no-discover) { auto:0, yes:1, no:2, yes-discover:3, no-discover:4 }">
Whether the port is an edge port, and whether it can automatically discover that it is one. Edge ports connect to a LAN with no other bridges, so they skip the learning and listening states and move straight to forwarding.

This property has no effect when `protocol-mode` is set to `none`.

- `auto` (default) - same as `no-discover`, and additionally treats a Wireless interface with bridge mode disabled as an edge port without discovery
- `yes` - edge port without discovery, transitions directly to forwarding
- `yes-discover` - edge port with discovery, transitions directly to forwarding
- `no` - non-edge port without discovery, takes part in learning and listening and waits for BPDU agreement, so it can stay non-forwarding indefinitely if no BPDU arrives
- `no-discover` - non-edge port with discovery, can become an edge port if no BPDU is received
</ArgTableRow>
<ArgTableRow arg="point-to-point" typ="enum (auto | yes | no) { auto:0, yes:1, no:2 }">
Whether the port connects to a single other bridge over a point-to-point link, which skips the check that waits for BPDUs from other devices and speeds up (R/M)STP convergence. Set to `no` only where several devices can be reached through the link, such as a hub or a wireless medium. With a full-duplex Ethernet link, `auto` enables point-to-point operation.

Default: auto. This property has no effect when `protocol-mode` is set to `none`.
</ArgTableRow>
<ArgTableRow arg="learn" typ="enum (auto | yes | no) { auto:0, yes:2, no:1 }">
MAC learning behavior on the port.

Default: auto.

- `yes` - enables MAC learning
- `no` - disables MAC learning
- `auto` - uses the Wireless registration table instead of MAC learning when the port is a Wireless interface in `ap-bridge`, `bridge` or `wds-slave` mode with bridge mode disabled
</ArgTableRow>
<ArgTableRow arg="horizon" typ="num">
Split horizon group. Ports in the same group do not forward traffic to each other, which prevents bridging loops. Split horizon is a software feature and disables hardware offloading on the port.

Default: none.
</ArgTableRow>
<ArgTableRow arg="hw" typ="bool">
Allows enabling or disabling [hardware offloading](../../../../bridging-and-switching/#bridge-hardware-offloading) on interfaces capable of it. Ignored for software interfaces such as [EoIP](../../../../virtual-private-networks/eoip/) or [VLAN](../../../../bridging-and-switching/vlan/). Some bridge and port settings disable offloading automatically, see the `H` flag in `print`.

Default: yes.
</ArgTableRow>
<ArgTableRow arg="auto-isolate" typ="bool">
When enabled, prevents the port from moving from discarding to forwarding until a BPDU is received from the neighboring bridge. Use it to keep a segment isolated until the bridge on the other side is confirmed.

Default: no. This property only has an effect when `protocol-mode` is set to `rstp` or `mstp` and `edge` is set to `no`.
</ArgTableRow>
<ArgTableRow arg="restricted-role" typ="bool">
When enabled, prevents the port from becoming the root port of the CIST or of any MSTI, so it stays an alternate port while it receives superior BPDUs and returns to forwarding once it stops receiving them. Equivalent to root guard.

Default: no. This property only has an effect when `protocol-mode` is set to `stp`, `rstp` or `mstp`.
</ArgTableRow>
<ArgTableRow arg="restricted-tcn" typ="bool">
When enabled, prevents the port from propagating received topology change notifications to other ports, and from generating one for changes it causes itself. Use it to keep a neighboring bridge from flushing MAC addresses in the local network.

Default: no. This property only has an effect when `protocol-mode` is set to `stp`, `rstp` or `mstp`.
</ArgTableRow>
<ArgTableRow arg="pvid" typ="num">
Port VLAN ID. Assigns untagged ingress traffic to this VLAN.

Default: 1. This property only has an effect when `vlan-filtering` is set to `yes`.
</ArgTableRow>
<ArgTableRow arg="frame-types" typ="enum (admit-all | admit-only-vlan-tagged | admit-only-untagged-and-priority-tagged) { admit-all:0, admit-only-vlan-tagged:1, admit-only-untagged-and-priority-tagged:2 }">
Allowed ingress frame types on the port.

Default: admit-all. This property only has an effect when `vlan-filtering` is set to `yes`.
</ArgTableRow>
<ArgTableRow arg="ingress-filtering" typ="bool">
Checks that the ingress port is a member of the received VLAN ID in the bridge VLAN table, and drops frames in VLANs the port is not a member of. Combine it with `frame-types` to select tagged or untagged ingress traffic.

Default: yes. This property only has an effect when `vlan-filtering` is set to `yes`.
</ArgTableRow>
<ArgTableRow arg="unknown-unicast-flood" typ="bool">
Whether the bridge floods unknown unicast traffic to this port. Only controls egress traffic. Traffic is unknown unicast until the destination MAC address is learned in the bridge host table, so static host entries avoid drops on the first packets.

Default: yes.
</ArgTableRow>
<ArgTableRow arg="unknown-multicast-flood" typ="bool">
Whether the bridge floods unknown multicast traffic to this port. Only controls egress traffic, and the setting covers all multicast, including non-IP, IPv4, IPv6 and the link-local ranges such as `224.0.0.0/24` and `ff02::1`. With `igmp-snooping` enabled and a querier detected, only multicast present in the MDB table is sent to the port.

Default: yes.
</ArgTableRow>
<ArgTableRow arg="broadcast-flood" typ="bool">
Whether the bridge floods broadcast traffic to this port. Only controls egress traffic. Broadcast traffic uses `FF:FF:FF:FF:FF:FF` as the destination MAC address and carries protocols such as DHCP, ARP, NDP and BOOTP (Netinstall). The setting does not limit flooding to the CPU.

Default: yes.
</ArgTableRow>
<ArgTableRow arg="tag-stacking" typ="bool">
Treats all ingress frames as untagged. Every frame is tagged with an additional VLAN tag using the port `pvid` and the bridge `ether-type`, whether or not it already carries a tag.

Default: no. This property only has an effect when `vlan-filtering` is set to `yes`.
</ArgTableRow>
<ArgTableRow arg="bpdu-guard" typ="bool">
Puts the port into a disabled role when it receives a BPDU, and keeps it there until it is manually disabled and enabled again. Use it to protect the bridge from BPDU-related attacks.

Default: no. This property has no effect when `protocol-mode` is set to `none`.
</ArgTableRow>
<ArgTableRow arg="trusted" typ="bool">
Allows DHCP packets towards the DHCP server through this port, and stops DHCP server messages received on it from being dropped. Mainly used to prevent unauthorized DHCP servers from providing malicious information to users.

Default: no. This property only has an effect when `dhcp-snooping` is set to `yes`.
</ArgTableRow>
<ArgTableRow arg="trusted-ra" typ="bool">
Permits IPv6 Router Advertisement messages through the port. Set it to `yes` for ports connected to legitimate routers, leave it `no` to block unauthorized sources.

Default: no. This property only has an effect when `ra-guard` is set to `yes`.
</ArgTableRow>
<ArgTableRow arg="trusted-dhcpv6" typ="bool">
Allows forwarding DHCPv6 packets towards the DHCPv6 server through this port. Mainly used to prevent unauthorized DHCPv6 servers from providing malicious information to users.

Default: no. This property only has an effect when `dhcpv6-snooping` is set to `yes`.
</ArgTableRow>
<ArgTableRow arg="trusted-arp" typ="bool">
Forwards ARP packets received on this port without validating them against the DHCP snooping binding database. When disabled, ARP packets whose sender MAC and IP do not match a binding entry are dropped.

Default: no. This property only has an effect when `arp-inspection` is set to `yes`.
</ArgTableRow>
<ArgTableRow arg="trusted-ipsg" typ="bool">
Forwards IPv4 packets received on this port without validating them against the DHCP snooping binding database. Use it to exempt a single access port from IP Source Guard without also allowing DHCP server messages from that port.

Default: no. This property only has an effect when `ip-source-guard` is set to `yes` and the port is set to `trusted=no`.
</ArgTableRow>
<ArgTableRow arg="mvrp-registrar-state" typ="enum (normal | fixed)">
MVRP registrar behavior of the port.

Default: normal.

- `fixed` - ignores all MRP messages and stays registered (IN) in every configured VLAN
- `normal` - processes MRP messages according to the standard
</ArgTableRow>
<ArgTableRow arg="mvrp-applicant-state" typ="enum (normal-participant | non-participant)">
MVRP applicant behavior of the port.

Default: normal-participant.

- `non-participant` - the port sends no MRP messages
- `normal-participant` - the port takes part in MRP exchanges normally
</ArgTableRow>
<ArgTableRow arg="multicast-router" typ="enum (disabled | temporary-query | permanent) { disabled:0, temporary-query:1, permanent:2 }">
Whether the port is treated as a multicast router port, where unregistered multicast streams and IGMP/MLD membership reports are sent. Use it to steer membership reports to selected ports for multicast routing or proxying.

Default: temporary-query. This property only has an effect when `igmp-snooping` is set to `yes`.

- `disabled` - the port is not treated as a multicast router, nothing is sent to it regardless of what is connected
- `permanent` - the port is always treated as a multicast router, unregistered multicast and membership reports are sent to it regardless of what is connected
- `temporary-query` - the multicast router state is detected automatically from IGMP/MLD queries
</ArgTableRow>
<ArgTableRow arg="fast-leave" typ="bool">
Stops forwarding multicast traffic to the port as soon as an IGMP/MLD leave message is received, without first checking whether other clients still need the group.

Default: no. This property only has an effect when `igmp-snooping` is set to `yes`.
</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="parent" typ="enum">Name of the interface list the port was expanded from. The field is present only on dynamic ports created from an `interface-list` entry, and it is absent for ports added by interface name.</ArgTableRow>
<ArgTableRow arg="status" typ="enum (inactive | in-bridge | in-bridge | disabled)">
Current port state.

- `in-bridge` - the port is enabled and in the bridge
- `inactive` - the port is disabled or not running
- `disabled` - the port is administratively disabled
</ArgTableRow>
<ArgTableRow arg="port-id" typ="composite { priority: num
, number: num
 }">Port identifier used by STP, shown as `priority.number`. The priority is the high byte of the port priority and the number is the port index.</ArgTableRow>
<ArgTableRow arg="role" typ="enum (disabled-port | root-port | designated-port | alternate-port | backup-port) { disabled-port:0, root-port:1, designated-port:2, alternate-port:3, backup-port:4 }">
Port role assigned by the (R/M)STP algorithm.

- `disabled-port` - the port is disabled or inactive
- `root-port` - the port faces the root bridge and has the lowest cost path to it, one per bridge except on the root bridge itself
- `designated-port` - the port faces away from the root bridge and forwards traffic to downstream devices
- `alternate-port` - the port faces the root bridge but is not forwarding, it is a backup path to the root
- `backup-port` - the port faces away from the root bridge and backs up another designated port on the same segment
</ArgTableRow>
<ArgTableRow arg="edge-port" typ="bool">Whether the port is currently an edge port.</ArgTableRow>
<ArgTableRow arg="edge-port-discovery" typ="bool">Whether the port is set to detect automatically that it is an edge port.</ArgTableRow>
<ArgTableRow arg="point-to-point-port" typ="bool">Whether the link to the neighboring bridge is full-duplex (`yes`) or half-duplex (`no`).</ArgTableRow>
<ArgTableRow arg="external-fdb-status" typ="bool">Whether the port uses a registration table instead of the forwarding database, for example a Wireless interface with bridge mode disabled.</ArgTableRow>
<ArgTableRow arg="sending-rstp" typ="bool">Whether the port sends RSTP or MSTP BPDUs (`yes`) rather than STP BPDUs (`no`). A port switches to STP BPDU type when an RSTP or MSTP port receives an STP BPDU. This does not indicate whether BPDUs are actually sent.</ArgTableRow>
<ArgTableRow arg="learning" typ="bool">Whether the port can learn MAC addresses, which depends on the `learn` setting and the current STP state.</ArgTableRow>
<ArgTableRow arg="forwarding" typ="bool">Whether the port is forwarding, that is, not blocked by (R/M)STP.</ArgTableRow>
<ArgTableRow arg="actual-path-cost" typ="num">Path cost currently applied to the port, either set manually or determined by the bridge from the interface speed and `port-cost-mode`.</ArgTableRow>
<ArgTableRow arg="root-path-cost" typ="num">Total cost of the path from this port to the root bridge.</ArgTableRow>
<ArgTableRow arg="internal-root-path-cost" typ="num">Total internal cost of the path from this port to the regional root bridge, for MSTP.</ArgTableRow>
<ArgTableRow arg="designated-bridge-id" typ="composite { number: num
, address: macAddr
 }">Designated bridge identifier taken from the port priority vector, shown as `priority.MAC address`.</ArgTableRow>
<ArgTableRow arg="designated-cost" typ="num">Designated root path cost taken from the port priority vector.</ArgTableRow>
<ArgTableRow arg="designated-port-id" typ="composite { priority: num
, number: num
 }">Designated port identifier taken from the port priority vector, shown as `priority.number`.</ArgTableRow>
<ArgTableRow arg="tx-bpdu" typ="num">Number of BPDUs sent by the port.</ArgTableRow>
<ArgTableRow arg="rx-bpdu" typ="num">Number of BPDUs received by the port.</ArgTableRow>
<ArgTableRow arg="discard-transitions" typ="num">Number of times the port entered the discarding state.</ArgTableRow>
<ArgTableRow arg="forward-transitions" typ="num">Number of times the port entered the forwarding state.</ArgTableRow>
<ArgTableRow arg="tx-tc" typ="num">Number of topology change messages sent by the port.</ArgTableRow>
<ArgTableRow arg="rx-tc" typ="num">Number of topology change messages received by the port.</ArgTableRow>
<ArgTableRow arg="topology-changes" typ="num">Topology change counter for the port.</ArgTableRow>
<ArgTableRow arg="last-topology-change" typ="time">Time elapsed since the last topology change on the port.</ArgTableRow>
<ArgTableRow arg="host-moves" typ="num">Number of times a host MAC address was moved to this port.</ArgTableRow>
<ArgTableRow arg="multicast-router" typ="bool">Whether a multicast router is detected on the port. Shown only when `igmp-snooping` is enabled.</ArgTableRow>
<ArgTableRow arg="hw-offload-group" typ="enum">Switch chip that offloads the port, for example `switch1`.</ArgTableRow>
<ArgTableRow arg="declared-vlan-ids" typ="multi { vlan-range: range
 }">VLAN IDs the port declares through MVRP.</ArgTableRow>
<ArgTableRow arg="registered-vlan-ids" typ="multi { vlan-range: range
 }">VLAN IDs in which the port is registered through MVRP.</ArgTableRow>
<ArgTableRow arg="hw-offload" typ="bool">Whether the port is currently offloaded to the switch chip.</ArgTableRow>
<ArgTableRow arg="debug-info" typ="string">Internal debugging information for the port.</ArgTableRow>
</ArgTable>
