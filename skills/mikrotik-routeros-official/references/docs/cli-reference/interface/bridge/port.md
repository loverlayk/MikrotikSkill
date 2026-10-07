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
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="priority" typ="enum (0x00 | 0x10 | 0x20 | 0x30 | 0x40 | 0x50 | 0x60 | 0x70 | 0x80 | 0x90 | 0xa0 | 0xb0 | 0xc0 | 0xd0 | 0xe0 | 0xf0) { 0x00:0x00, 0x10:0x10, 0x20:0x20, 0x30:0x30, 0x40:0x40, 0x50:0x50, 0x60:0x60, 0x70:0x70, 0x80:0x80, 0x90:0x90, 0xa0:0xa0, 0xb0:0xb0, 0xc0:0xc0, 0xd0:0xd0, 0xe0:0xe0, 0xf0:0xf0 }"></ArgTableRow>
<ArgTableRow arg="path-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="internal-path-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="edge" typ="enum (auto | yes | no | yes-discover | no-discover) { auto:0, yes:1, no:2, yes-discover:3, no-discover:4 }"></ArgTableRow>
<ArgTableRow arg="point-to-point" typ="enum (auto | yes | no) { auto:0, yes:1, no:2 }"></ArgTableRow>
<ArgTableRow arg="learn" typ="enum (auto | yes | no) { auto:0, yes:2, no:1 }"></ArgTableRow>
<ArgTableRow arg="horizon" typ="num"></ArgTableRow>
<ArgTableRow arg="hw" typ="bool"></ArgTableRow>
<ArgTableRow arg="auto-isolate" typ="bool"></ArgTableRow>
<ArgTableRow arg="restricted-role" typ="bool"></ArgTableRow>
<ArgTableRow arg="restricted-tcn" typ="bool"></ArgTableRow>
<ArgTableRow arg="pvid" typ="num"></ArgTableRow>
<ArgTableRow arg="frame-types" typ="enum (admit-all | admit-only-vlan-tagged | admit-only-untagged-and-priority-tagged) { admit-all:0, admit-only-vlan-tagged:1, admit-only-untagged-and-priority-tagged:2 }"></ArgTableRow>
<ArgTableRow arg="ingress-filtering" typ="bool"></ArgTableRow>
<ArgTableRow arg="unknown-unicast-flood" typ="bool"></ArgTableRow>
<ArgTableRow arg="unknown-multicast-flood" typ="bool"></ArgTableRow>
<ArgTableRow arg="broadcast-flood" typ="bool"></ArgTableRow>
<ArgTableRow arg="tag-stacking" typ="bool"></ArgTableRow>
<ArgTableRow arg="bpdu-guard" typ="bool"></ArgTableRow>
<ArgTableRow arg="trusted" typ="bool"></ArgTableRow>
<ArgTableRow arg="trusted-ra" typ="bool"></ArgTableRow>
<ArgTableRow arg="trusted-dhcpv6" typ="bool"></ArgTableRow>
<ArgTableRow arg="trusted-arp" typ="bool"></ArgTableRow>
<ArgTableRow arg="mvrp-registrar-state" typ="enum (normal | fixed)"></ArgTableRow>
<ArgTableRow arg="mvrp-applicant-state" typ="enum (normal-participant | non-participant)"></ArgTableRow>
<ArgTableRow arg="multicast-router" typ="enum (disabled | temporary-query | permanent) { disabled:0, temporary-query:1, permanent:2 }"></ArgTableRow>
<ArgTableRow arg="fast-leave" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="parent" typ="enum"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (inactive | in-bridge | in-bridge | disabled)"></ArgTableRow>
<ArgTableRow arg="port-id" typ="composite { priority: num
, number: num
 }"></ArgTableRow>
<ArgTableRow arg="role" typ="enum (disabled-port | root-port | designated-port | alternate-port | backup-port) { disabled-port:0, root-port:1, designated-port:2, alternate-port:3, backup-port:4 }"></ArgTableRow>
<ArgTableRow arg="edge-port" typ="bool"></ArgTableRow>
<ArgTableRow arg="edge-port-discovery" typ="bool"></ArgTableRow>
<ArgTableRow arg="point-to-point-port" typ="bool"></ArgTableRow>
<ArgTableRow arg="external-fdb-status" typ="bool"></ArgTableRow>
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
<ArgTableRow arg="designated-port-id" typ="composite { priority: num
, number: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-bpdu" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bpdu" typ="num"></ArgTableRow>
<ArgTableRow arg="discard-transitions" typ="num"></ArgTableRow>
<ArgTableRow arg="forward-transitions" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-tc" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-tc" typ="num"></ArgTableRow>
<ArgTableRow arg="topology-changes" typ="num"></ArgTableRow>
<ArgTableRow arg="last-topology-change" typ="time"></ArgTableRow>
<ArgTableRow arg="multicast-router" typ="bool"></ArgTableRow>
<ArgTableRow arg="hw-offload-group" typ="enum"></ArgTableRow>
<ArgTableRow arg="declared-vlan-ids" typ="multi { vlan-range: range
 }"></ArgTableRow>
<ArgTableRow arg="registered-vlan-ids" typ="multi { vlan-range: range
 }"></ArgTableRow>
<ArgTableRow arg="hw-offload" typ="bool"></ArgTableRow>
<ArgTableRow arg="debug-info" typ="string"></ArgTableRow>
</ArgTable>
