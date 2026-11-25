# monitor

> RouterOS command reference for /interface/bridge/port/monitor.

-----------

## interface/bridge/port/monitor 
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="alt { interface: iface_enum
, interface-list: enum
 }">Interface name or interface list to monitor.</ArgTableRow>
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

In RouterOS the field displays RSTP role names such as `alternate-port` and `backup-port` also when `protocol-mode` is set to `stp`. STP treats all blocked ports alike, so this does not affect operation.

See [STP and RSTP](/docs/bridging-and-switching/user-guides/spanning-tree-protocol#stp-and-rstp) for more details.
</ArgTableRow>
<ArgTableRow arg="edge-port" typ="bool">Whether the port is currently an edge port.</ArgTableRow>
<ArgTableRow arg="edge-port-discovery" typ="bool">Whether the port is set to detect automatically that it is an edge port.</ArgTableRow>
<ArgTableRow arg="point-to-point-port" typ="bool">Whether the link to the neighboring bridge is full-duplex (`yes`) or half-duplex (`no`).</ArgTableRow>
<ArgTableRow arg="external-fdb" typ="bool">Whether the port uses a registration table instead of the forwarding database, for example a Wireless interface with bridge mode disabled.</ArgTableRow>
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
<ArgTableRow arg="designated-internal-cost" typ="num">Designated internal root path cost taken from the port priority vector, for MSTP.</ArgTableRow>
<ArgTableRow arg="designated-port-id" typ="composite { priority: num
, number: num
 }">Designated port identifier taken from the port priority vector, shown as `priority.number`.</ArgTableRow>
<ArgTableRow arg="designated-message-age" typ="num">Message age of the designated port, taken from the port priority vector. It increases as the BPDU passes through bridges and the BPDU is discarded once it exceeds the bridge `max-message-age`.</ArgTableRow>
<ArgTableRow arg="designated-max-age" typ="num">Max age of the designated port, taken from the port priority vector. The BPDU can pass through as many bridges as the `max-message-age` parameter allows.</ArgTableRow>
<ArgTableRow arg="designated-remaining-hops" typ="num">Number of hops the BPDU can still traverse before it reaches its destination, for MSTP.</ArgTableRow>
<ArgTableRow arg="tx-rx-bpdu" typ="composite { tx: num
, rx: num
 }">Number of BPDUs sent and received by the port.</ArgTableRow>
<ArgTableRow arg="discard-transitions" typ="num">Number of times the port entered the discarding state.</ArgTableRow>
<ArgTableRow arg="forward-transitions" typ="num">Number of times the port entered the forwarding state.</ArgTableRow>
<ArgTableRow arg="tx-rx-tc" typ="composite { tx: num
, rx: num
 }">Number of topology change messages sent and received by the port.</ArgTableRow>
<ArgTableRow arg="topology-changes" typ="num">Topology change counter for the port.</ArgTableRow>
<ArgTableRow arg="last-topology-change" typ="time">Time elapsed since the last topology change on the port.</ArgTableRow>
<ArgTableRow arg="host-moves" typ="num">Number of times a host MAC address was moved to this port.</ArgTableRow>
<ArgTableRow arg="multicast-router" typ="bool">Whether a multicast router is detected on the port. Shown only when `igmp-snooping` is enabled.</ArgTableRow>
<ArgTableRow arg="hw-offload-group" typ="enum">Switch chip that offloads the port, for example `switch1`.</ArgTableRow>
<ArgTableRow arg="declared-vlan-ids" typ="multi { vlan-range: range
 }">VLAN IDs the port declares through MVRP.</ArgTableRow>
<ArgTableRow arg="registered-vlan-ids" typ="multi { vlan-range: range
 }">VLAN IDs in which the port is registered through MVRP.</ArgTableRow>
</ArgTable>
