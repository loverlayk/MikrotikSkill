# port

> RouterOS directory reference for /interface/ethernet/switch/port.

-----------

## interface/ethernet/switch/port 
**Syscap:** musicswitch
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ingress-customer-tpid-override" typ="num">Ingress customer TPID override allows accepting specific frames with a custom customer tag TPID. The default value is for the tag of 802.1Q frames.</ArgTableRow>
<ArgTableRow arg="egress-customer-tpid-override" typ="num">Egress customer TPID override allows custom identification for egress frames with a customer tag. The default value is for the tag of 802.1Q frames.</ArgTableRow>
<ArgTableRow arg="ingress-service-tpid-override" typ="num">Ingress service TPID override allows accepting specific frames with a custom service tag TPID. The default value is for the service tag of 802.1AD frames.</ArgTableRow>
<ArgTableRow arg="egress-service-tpid-override" typ="num">Egress service TPID override allows custom identification for egress frames with a service tag. The default value is for the service tag of 802.1AD frames.</ArgTableRow>
<ArgTableRow arg="drop-secure-static-mac-move" typ="bool">Prevents MAC relearning of static entries until UFDB timeout if the MAC is already learned on another port.</ArgTableRow>
<ArgTableRow arg="drop-dynamic-mac-move" typ="bool">Prevents MAC relearning until UFDB timeout if the MAC is already learned on another port.</ArgTableRow>
<ArgTableRow arg="learn-limit" typ="num">Enable or disable MAC address learning and set the MAC limit on the port. MAC learning limit is disabled by default.</ArgTableRow>
<ArgTableRow arg="allow-unicast-loopback" typ="bool">Unicast loopback on port. When enabled, it permits sending back when the source port and destination port are the same for known unicast packets.</ArgTableRow>
<ArgTableRow arg="allow-multicast-loopback" typ="bool">Multicast loopback on port. When enabled, it permits sending back when the source port and destination port are the same for registered multicast or broadcast packets.</ArgTableRow>
<ArgTableRow arg="action-on-static-station-move" typ="enum (forward | redirect-to-cpu | copy-to-cpu | drop) { forward:0, redirect-to-cpu:1, copy-to-cpu:2, drop:3 }">Action for packets when UFDB already contains a static entry with such a MAC but with a different port.</ArgTableRow>
<ArgTableRow arg="drop-when-ufdb-entry-src-drop" typ="bool">Enable or disable dropping packets when UFDB entry has action src-drop.</ArgTableRow>
<ArgTableRow arg="isolation-leakage-profile-override" typ="num">
Custom port profile for port isolation/leakage configurations.
- Port-level isolation profile 0. Uplink port - allows the port to communicate with all ports in the device.
- Port-level isolation profile 1. Isolated port - allows the port to communicate only with uplink ports.
- Port-level isolation profile 2 - 31. Community port - allows communication among the same community ports and uplink ports.
</ArgTableRow>
<ArgTableRow arg="vlan-type" typ="enum (edge-port | network-port) { edge-port:0, network-port:1 }">Port VLAN type specifies whether VLAN ID is used in UFDB learning. The network port learns VLAN ID in UFDB, edge port does not - VLAN 0. It can be observed only in IVL learning mode.</ArgTableRow>
<ArgTableRow arg="allow-fdb-based-vlan-translate" typ="bool">Enable or disable MAC-based VLAN translation on the port.</ArgTableRow>
<ArgTableRow arg="allow-mac-based-service-vlan-assignment-for" typ="enum (none | untagged-and-priority-tagged-frame-only | tagged-frame-only | all) { none:0, untagged-and-priority-tagged-frame-only:1, tagged-frame-only:2, all:3 }">Frame type for which MAC-based service VLAN translation applies.</ArgTableRow>
<ArgTableRow arg="allow-mac-based-customer-vlan-assignment-for" typ="enum (none | untagged-and-priority-tagged-frame-only | tagged-frame-only | all) { none:0, untagged-and-priority-tagged-frame-only:1, tagged-frame-only:2, all:3 }">Frame type for which MAC-based customer VLAN translation applies.</ArgTableRow>
<ArgTableRow arg="filter-untagged-frame" typ="bool">Whether to filter untagged frames on the port.</ArgTableRow>
<ArgTableRow arg="filter-priority-tagged-frame" typ="bool">Whether to filter tagged frames with priority on the port.</ArgTableRow>
<ArgTableRow arg="filter-tagged-frame" typ="bool">Whether to filter tagged frames on the port.</ArgTableRow>
<ArgTableRow arg="egress-vlan-tag-table-lookup-key" typ="enum (egress-vid | according-to-bridge-type) { egress-vid:0, according-to-bridge-type:1 }">
Egress VLAN table (VLAN Tagging) lookup:
- `egress-vid` - lookup VLAN ID is `CVID` when an Edge port is configured, `SVID` when a Network port.
- `according-to-bridge-type` - lookup VLAN ID is `CVID` when a customer VLAN bridge is configured, `SVID` when a service VLAN bridge.
</ArgTableRow>
<ArgTableRow arg="egress-vlan-mode" typ="enum (untagged | tagged | unmodified) { untagged:0, tagged:1, unmodified:2 }">Egress VLAN tagging action on the port.</ArgTableRow>
<ArgTableRow arg="ingress-mirror-to" typ="enum (none | mirror0 | mirror1) { none:0xffffffff, mirror0:0, mirror1:1 }">Analyzer port for port-based ingress mirroring.</ArgTableRow>
<ArgTableRow arg="ingress-mirroring-according-to-vlan" typ="bool"></ArgTableRow>
<ArgTableRow arg="egress-mirror-to" typ="enum (none | mirror0 | mirror1) { none:0xffffffff, mirror0:0, mirror1:1 }">Analyzer port for port-based egress mirroring.</ArgTableRow>
<ArgTableRow arg="qos-scheme-precedence" typ="multi { array-id, qos-type: enum (pcp-based | vlan-based | protocol-based | da-based | sa-based | dscp-based | ingress-acl-based) { pcp-based:0, vlan-based:1, protocol-based:2, da-based:3, sa-based:4, dscp-based:5, ingress-acl-based:6 }
 }">Specifies applied QoS assignment schemes on the ingress of the port.</ArgTableRow>
<ArgTableRow arg="default-customer-pcp" typ="num">Default customer PCP of the port.</ArgTableRow>
<ArgTableRow arg="default-service-pcp" typ="num">Default service PCP of the port.</ArgTableRow>
<ArgTableRow arg="pcp-propagation-for-initial-pcp" typ="bool">
Enables or disables PCP propagation for initial PCP assignment on ingress.
- If the port `vlan-type` is an Edge port, the service PCP is copied from the customer PCP.
- If the port `vlan-type` is a Network port, the customer PCP is copied from the service PCP.
</ArgTableRow>
<ArgTableRow arg="egress-pcp-propagation" typ="bool">Enables or disables egress PCP propagation. If the port `vlan-type` is an Edge port, the service PCP is copied from the customer PCP. If the port `vlan-type` is a Network port, the customer PCP is copied from the service PCP.</ArgTableRow>
<ArgTableRow arg="dscp-based-qos-dscp-to-dscp-mapping" typ="bool">Enables or disables DSCP to internal DSCP mapping on the port.</ArgTableRow>
<ArgTableRow arg="pcp-or-dscp-based-qos-change-dei" typ="bool">Enables or disables PCP or DSCP based DEI change on the port.</ArgTableRow>
<ArgTableRow arg="pcp-or-dscp-based-qos-change-pcp" typ="bool">Enables or disables PCP or DSCP based PCP change on the port.</ArgTableRow>
<ArgTableRow arg="pcp-or-dscp-based-qos-change-dscp" typ="bool">Enables or disables PCP or DSCP based DSCP change on the port.</ArgTableRow>
<ArgTableRow arg="pcp-based-qos-drop-precedence-mapping" typ="object { range-and-drop-precedence: composite { pcp-dei-range: range [ .. 15]
, drop-precedence: enum (green | yellow | red | drop)
 }
 }">The new value of drop precedence for the PCP/DEI to drop precedence (drop | green | red | yellow) mapping. Multiple mappings are allowed separated by a comma e.g. "0-7:yellow,8-15:red".</ArgTableRow>
<ArgTableRow arg="pcp-based-qos-dscp-mapping" typ="object { range-and-dscp: composite { pcp-dei-range: range [ .. 15]
, dscp: num [ .. 63]
 }
 }">The new value of DSCP for the PCP/DEI to DSCP mapping. Multiple mappings are allowed separated by a comma e.g. "0-7:25,8-15:50".</ArgTableRow>
<ArgTableRow arg="pcp-based-qos-dei-mapping" typ="object { range-and-dei: composite { pcp-dei-range: range [ .. 15]
, dei: num [ .. 1]
 }
 }">The new value of DEI for the PCP/DEI to DEI mapping. Multiple mappings are allowed separated by a comma e.g. "0-7:0,8-15:1".</ArgTableRow>
<ArgTableRow arg="pcp-based-qos-pcp-mapping" typ="object { range-and-pcp: composite { pcp-dei-range: range [ .. 15]
, pcp: num [ .. 7]
 }
 }">The new value of PCP for the PCP/DEI to PCP mapping. Multiple mappings are allowed separated by a comma e.g. "0-7:3,8-15:4".</ArgTableRow>
<ArgTableRow arg="pcp-based-qos-priority-mapping" typ="object { range-and-priority: composite { pcp-dei-range: range [ .. 15]
, priority: num [ .. 15]
 }
 }">The new value of internal priority for the PCP/DEI to priority mapping. Multiple mappings are allowed separated by a comma e.g. "0-7:5,8-15:15".</ArgTableRow>
<ArgTableRow arg="priority-to-queue" typ="object { priority-range-and-queue: composite { priority-range: range [ .. 15]
, queue: num [ .. 7]
 }
 }">Internal priority (0..15) mapping to queue (0..7) per port.</ArgTableRow>
<ArgTableRow arg="per-queue-scheduling" typ="object { scheduling-type-and-weight: composite { scheduling-type: enum (strict-priority | wrr-group0 | wrr-group1) { strict-priority:0, wrr-group0:1, wrr-group1:2 }
, weight: [ num [ .. 255]]
 }
 }">Set port to use either strict or weighted round robin policy for traffic shaping for each queue group.</ArgTableRow>
<ArgTableRow arg="custom-drop-counter-includes" typ="ubit (device-loopback, fdb-hash-violation, exceeded-port-learn-limitation, dynamic-station-move, static-station-move, ufdb-source-drop, host-source-drop, unknown-host, ingress-vlan-filtered)">Custom include to count dropped packets for switch port custom-drop-packet counter.</ArgTableRow>
<ArgTableRow arg="queue-custom-drop-counter0-includes" typ="ubit (red, yellow, green, queue0, queue1, queue2, queue3, queue4, queue5, queue6, queue7)">Custom include to count dropped packets for switch port tx-queue-custom0-drop-packet and bytes for tx-queue-custom0-drop-byte counter.</ArgTableRow>
<ArgTableRow arg="queue-custom-drop-counter1-includes" typ="ubit (red, yellow, green, queue0, queue1, queue2, queue3, queue4, queue5, queue6, queue7)">Custom include to count dropped packets for switch port tx-queue-custom1-drop-packet and bytes for tx-queue-custom1-drop-byte counter.</ArgTableRow>
<ArgTableRow arg="policy-drop-counter-includes" typ="ubit (ingress-policing, ingress-acl, egress-policing, egress-acl)">Custom include to count dropped packets for switch port policy-drop-packet counter.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="ingress-customer-tpid" typ="num"></ArgTableRow>
<ArgTableRow arg="egress-customer-tpid" typ="num"></ArgTableRow>
<ArgTableRow arg="ingress-service-tpid" typ="num"></ArgTableRow>
<ArgTableRow arg="egress-service-tpid" typ="num"></ArgTableRow>
<ArgTableRow arg="learn" typ="bool"></ArgTableRow>
<ArgTableRow arg="isolation-leakage-profile" typ="num"></ArgTableRow>
<ArgTableRow arg="driver-rx-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="driver-rx-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="driver-tx-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="driver-tx-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-too-short" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-64" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-65-127" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-128-255" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-256-511" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-512-1023" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-1024-1518" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-1519-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-too-long" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-broadcast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-pause" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-multicast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-fcs-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-align-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-fragment" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-overflow" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-control" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-unknown-op" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-length-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-code-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-carrier-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-jabber" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-drop" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-ip-header-checksum-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-tcp-checksum-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-udp-checksum-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-too-short" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-64" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-65-127" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-128-255" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-256-511" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-512-1023" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-1024-1518" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-1519-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-too-long" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-broadcast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-pause" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-multicast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-underrun" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-excessive-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-multiple-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-single-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-excessive-deferred" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-deferred" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-late-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-total-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-pause-honored" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-jabber" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-fcs-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-control" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-fragment" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-carrier-sense-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-64" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-65-127" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-128-255" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-256-511" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-512-1023" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-1024-1518" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-1519-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom0-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom0-drop-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom1-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom1-drop-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="policy-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="custom-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="current-learned" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="not-learned" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-unicast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-unicast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-error-events" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-1024-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-1024-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-1024-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-codewords" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-corrected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-uncorrected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-symbol-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="fc-fec-rx-block" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="fc-fec-block-corrected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="fc-fec-block-uncorrected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue0-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue0-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue1-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue1-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue2-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue2-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue3-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue3-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue4-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue4-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue5-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue5-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue6-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue6-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue7-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue7-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue0-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue0-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue1-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue1-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue2-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue2-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue3-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue3-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue4-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue4-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue5-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue5-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue6-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue6-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue7-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue7-byte" typ="multi { counter: num
 }"></ArgTableRow>
</ArgTable>

## interface/ethernet/switch/port 
**Syscap:** rbswitch
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="running"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="vlan-mode" typ="enum (disabled | fallback | check | secure) { disabled:0, fallback:1, check:2, secure:3 }" syscap="oldswitch">Changes the VLAN lookup mechanism against the VLAN Table for ingress traffic. `disabled` - disables checking against the VLAN Table completely, no traffic is dropped. `fallback` - checks tagged traffic against the VLAN Table, forwards all untagged traffic. `check` - checks tagged traffic, drops all untagged traffic. `secure` - checks tagged traffic, drops all untagged traffic, both ingress and egress ports must be found in the VLAN Table otherwise traffic is dropped.</ArgTableRow>
<ArgTableRow arg="vlan-header" typ="enum (leave-as-is | always-strip | add-if-missing) { leave-as-is:0, always-strip:1, add-if-missing:2 }" syscap="oldswitch">Sets the action performed on the port for egress traffic. `add-if-missing` - adds a VLAN tag using `default-vlan-id` from the ingress port, used for trunk ports. `always-strip` - removes a VLAN tag, used for access ports. `leave-as-is` - does not add or remove a VLAN tag, used for hybrid ports.</ArgTableRow>
<ArgTableRow arg="default-vlan-id" typ="num" syscap="oldswitch">Adds a VLAN tag with the specified VLAN ID on all untagged ingress traffic on a port. Should be used with `vlan-header=always-strip` to configure the port as an access port. For hybrid ports `default-vlan-id` is used to tag untagged traffic. If two ports have the same `default-vlan-id`, the VLAN tag is not added since the switch chip assumes traffic is being forwarded between access ports.</ArgTableRow>
<ArgTableRow arg="mirror-ingress" typ="bool" syscap="switch-mirror-prestera">Whether to send ingress packet copy to the `mirror-target` port.</ArgTableRow>
<ArgTableRow arg="mirror-egress" typ="bool" syscap="switch-mirror-prestera">Whether to send egress packet copy to the `mirror-target` port.</ArgTableRow>
<ArgTableRow arg="mirror-ingress-target" typ="enum (none) { none:0 }" syscap="switch-mv88e6xxx">Selects a single mirroring ingress target port. Mirrored packets from `mirror-ingress` will be sent to the selected port.</ArgTableRow>
<ArgTableRow arg="ingress-rate" typ="num" syscap="oldswitch">Limits the received (ingress) traffic with packet drops. Everything that exceeds the defined limit will be dropped.</ArgTableRow>
<ArgTableRow arg="egress-rate" typ="num" syscap="oldswitch">Limits the transmitted (egress) traffic. The shaper tries to queue packets that exceed the limit instead of dropping them.</ArgTableRow>
<ArgTableRow arg="storm-rate" typ="num" syscap="crs_prestera">Amount of broadcast, unknown multicast and/or unknown unicast traffic limited to a percentage of the link speed.</ArgTableRow>
<ArgTableRow arg="limit-unknown-unicasts" typ="bool" syscap="crs_prestera">Limit unknown unicast traffic on a switch port.</ArgTableRow>
<ArgTableRow arg="limit-unknown-multicasts" typ="bool" syscap="crs_prestera">Limit unknown multicast traffic on a switch port.</ArgTableRow>
<ArgTableRow arg="limit-broadcasts" typ="bool" syscap="crs_prestera">Limit broadcast traffic on a switch port.</ArgTableRow>
<ArgTableRow arg="l3-hw-offloading" typ="bool" syscap="crs_prestera">Layer 3 Hardware Offloading. Hardware routing via this port. Only disables hardware routing from/to this particular port when set to `no`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="switch" typ="enum"></ArgTableRow>
<ArgTableRow arg="driver-rx-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="driver-rx-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="driver-tx-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="driver-tx-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-too-short" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-64" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-65-127" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-128-255" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-256-511" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-512-1023" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-1024-1518" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-1519-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-too-long" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-broadcast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-pause" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-multicast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-fcs-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-align-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-fragment" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-overflow" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-control" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-unknown-op" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-length-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-code-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-carrier-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-jabber" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-drop" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-ip-header-checksum-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-tcp-checksum-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-udp-checksum-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-too-short" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-64" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-65-127" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-128-255" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-256-511" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-512-1023" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-1024-1518" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-1519-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-too-long" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-broadcast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-pause" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-multicast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-underrun" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-excessive-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-multiple-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-single-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-excessive-deferred" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-deferred" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-late-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-total-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-pause-honored" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-jabber" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-fcs-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-control" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-fragment" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-carrier-sense-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-64" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-65-127" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-128-255" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-256-511" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-512-1023" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-1024-1518" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-1519-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom0-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom0-drop-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom1-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom1-drop-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="policy-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="custom-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="current-learned" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="not-learned" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-unicast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-unicast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-error-events" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-1024-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-1024-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-1024-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-codewords" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-corrected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-uncorrected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-symbol-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="fc-fec-rx-block" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="fc-fec-block-corrected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="fc-fec-block-uncorrected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue0-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue0-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue1-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue1-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue2-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue2-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue3-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue3-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue4-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue4-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue5-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue5-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue6-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue6-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue7-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue7-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue0-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue0-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue1-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue1-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue2-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue2-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue3-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue3-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue4-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue4-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue5-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue5-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue6-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue6-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue7-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue7-byte" typ="multi { counter: num
 }"></ArgTableRow>
</ArgTable>
