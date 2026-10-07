# monitor

> RouterOS command reference for /interface/bridge/port/monitor.

-----------

## interface/bridge/port/monitor 
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="alt { interface: iface_enum
, interface-list: enum
 }"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (inactive | in-bridge | in-bridge | disabled)"></ArgTableRow>
<ArgTableRow arg="port-id" typ="composite { priority: num
, number: num
 }"></ArgTableRow>
<ArgTableRow arg="role" typ="enum (disabled-port | root-port | designated-port | alternate-port | backup-port) { disabled-port:0, root-port:1, designated-port:2, alternate-port:3, backup-port:4 }"></ArgTableRow>
<ArgTableRow arg="edge-port" typ="bool"></ArgTableRow>
<ArgTableRow arg="edge-port-discovery" typ="bool"></ArgTableRow>
<ArgTableRow arg="point-to-point-port" typ="bool"></ArgTableRow>
<ArgTableRow arg="external-fdb" typ="bool"></ArgTableRow>
<ArgTableRow arg="sending-rstp" typ="bool"></ArgTableRow>
<ArgTableRow arg="learning" typ="bool"></ArgTableRow>
<ArgTableRow arg="forwarding" typ="bool"></ArgTableRow>
<ArgTableRow arg="actual-path-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="root-path-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="internal-root-path-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="designated-bridge-id" typ="composite { number: num
, address: macAddr
 }"></ArgTableRow>
<ArgTableRow arg="designated-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="designated-internal-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="designated-port-id" typ="composite { priority: num
, number: num
 }"></ArgTableRow>
<ArgTableRow arg="designated-message-age" typ="num"></ArgTableRow>
<ArgTableRow arg="designated-max-age" typ="num"></ArgTableRow>
<ArgTableRow arg="designated-remaining-hops" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-rx-bpdu" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="discard-transitions" typ="num"></ArgTableRow>
<ArgTableRow arg="forward-transitions" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-rx-tc" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="topology-changes" typ="num"></ArgTableRow>
<ArgTableRow arg="last-topology-change" typ="time"></ArgTableRow>
<ArgTableRow arg="multicast-router" typ="bool"></ArgTableRow>
<ArgTableRow arg="hw-offload-group" typ="enum"></ArgTableRow>
<ArgTableRow arg="declared-vlan-ids" typ="multi { vlan-range: range
 }"></ArgTableRow>
<ArgTableRow arg="registered-vlan-ids" typ="multi { vlan-range: range
 }"></ArgTableRow>
</ArgTable>
