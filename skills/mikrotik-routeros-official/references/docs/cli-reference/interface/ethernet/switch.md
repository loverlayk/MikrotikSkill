# switch

> Global parameters for CRS1xx and 2xx series switches.

-----------

## interface/ethernet/switch 
**Conditions:** !smips
**Syscap:** musicswitch
**Type:** Settings Directory

Global parameters for CRS1xx and 2xx series switches.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the switch.</ArgTableRow>
<ArgTableRow arg="bridge-type" typ="enum (customer-vid-used-as-lookup-vid | service-vid-used-as-lookup-vid) { customer-vid-used-as-lookup-vid:0, service-vid-used-as-lookup-vid:1 }">Defines which VLAN tag is used as Lookup-VID. Lookup-VID serves as the VLAN key for all VLAN-based lookups.</ArgTableRow>
<ArgTableRow arg="drop-if-no-vlan-assignment-on-ports" typ="multi { array-id }">Ports which drop frames if no MAC-based, Protocol-based VLAN assignment or Ingress VLAN Translation is applied.</ArgTableRow>
<ArgTableRow arg="drop-if-invalid-or-src-port-not-member-of-vlan-on-ports" typ="multi { array-id, port: enum
 }">Ports that drop invalid and other port VLAN ID frames.</ArgTableRow>
<ArgTableRow arg="unknown-vlan-lookup-mode" typ="enum (ivl | svl)">
Lookup and learning mode for packets with an invalid VLAN.
 - `ivl` - use Independent VLAN Learning,
 - `svl` - use Shared VLAN Learning.
</ArgTableRow>
<ArgTableRow arg="forward-unknown-vlan" typ="bool">Whether to allow forwarding VLANs that are not members of the VLAN table.</ArgTableRow>
<ArgTableRow arg="use-svid-in-one2one-vlan-lookup" typ="bool">Whether to use service VLAN ID for 1:1 VLAN switching lookup.</ArgTableRow>
<ArgTableRow arg="use-cvid-in-one2one-vlan-lookup" typ="bool">Whether to use customer VLAN ID for 1:1 VLAN switching lookup.</ArgTableRow>
<ArgTableRow arg="mac-level-isolation" typ="bool">Globally enables or disables MAC level isolation. Once enabled, the switch will check the source and destination MAC address entries and their `isolation-profile` from the unicast forwarding table. By default, the switch will learn MAC addresses and place them into a `promiscuous` isolation profile. Other isolation profiles can be used when creating static unicast entries. If the source or destination MAC address is located on a `promiscuous` isolation profile, the packet is forwarded. If both source and destination MAC addresses are located on the same `community1` or `community2` isolation profile, the packet is forwarded. The packet is dropped when the source and destination MAC address isolation profile is `isolated`, or when the source and destination MAC address isolation profiles are from different communities (e.g. source MAC address is `community1` and destination MAC address is `community2`). When MAC level isolation is globally disabled, the isolation is bypassed.</ArgTableRow>
<ArgTableRow arg="multicast-lookup-mode" typ="enum (dst-mac-and-vid-always | dst-ip-and-vid-for-ipv4) { dst-mac-and-vid-always:0, dst-ip-and-vid-for-ipv4:1 }">
Lookup mode for IPv4 multicast bridging.
- `dst-mac-and-vid-always` - for all packet types the lookup key is the destination MAC and VLAN ID.
- `dst-ip-and-vid-for-ipv4` - for IPv4 packets the lookup key is the destination IP and VLAN ID.
</ArgTableRow>
<ArgTableRow arg="override-existing-when-ufdb-full" typ="bool">Enable or disable overriding an existing entry which has the lowest aging value when UFDB is full.</ArgTableRow>
<ArgTableRow arg="unicast-fdb-timeout" typ="time">Timeout for Unicast FDB entries.</ArgTableRow>
<ArgTableRow arg="ingress-mirror0" typ="composite { port-or-trunk: alt { port: enum (none) { none:0xffffffff }
, trunk: enum
 }
, packet-format: [ enum (unmodified | analyzer-configured) { unmodified:0, analyzer-configured:1 }]
 }">
The first ingress mirroring analyzer port or trunk and mirroring format.
 - `analyzer-configured` - packet is the same as the packet to the destination, VLAN format is modified based on the VLAN configurations of the analyzer port.
 - `unmodified` - traffic is mirrored without any change to the original incoming packet format, but the service VLAN tag is stripped in the edge port.
</ArgTableRow>
<ArgTableRow arg="ingress-mirror1" typ="composite { port-or-trunk: alt { port: enum (none) { none:0xffffffff }
, trunk: enum
 }
, packet-format: [ enum (unmodified | analyzer-configured) { unmodified:0, analyzer-configured:1 }]
 }">
The second ingress mirroring analyzer port or trunk and mirroring format.
 - `analyzer-configured` - packet is the same as the packet to the destination, VLAN format is modified based on the VLAN configurations of the analyzer port.
 - `unmodified` - traffic is mirrored without any change to the original incoming packet format, but the service VLAN tag is stripped in the edge port.
</ArgTableRow>
<ArgTableRow arg="ingress-mirror-ratio" typ="enum (1/1 | 1/2 | 1/4 | 1/8 | 1/16 | 1/32 | 1/64 | 1/128 | 1/256 | 1/512 | 1/1024 | 1/2048 | 1/4096 | 1/8192 | 1/16384 | 1/32768)">The proportion of ingress mirrored packets compared to all packets.</ArgTableRow>
<ArgTableRow arg="egress-mirror0" typ="composite { port-or-trunk: alt { port: enum (none) { none:0xffffffff }
, trunk: enum
 }
, packet-format: [ enum (modified | analyzer-configured | original) { modified:0, analyzer-configured:1, original:2 }]
 }">
The first egress mirroring analyzer port or trunk and mirroring format.
 - `analyzer-configured` - packet is the same as the packet to the destination, VLAN format is modified based on the VLAN configurations of the analyzer port.
 - `modified` - packet is the same as the packet to the destination, VLAN format is modified based on the VLAN configurations of the egress port.
 - `original` - traffic is mirrored without any change to the original incoming packet format, but the service VLAN tag is stripped in the edge port.
</ArgTableRow>
<ArgTableRow arg="egress-mirror1" typ="composite { port-or-trunk: alt { port: enum (none) { none:0xffffffff }
, trunk: enum
 }
, packet-format: [ enum (modified | analyzer-configured | original) { modified:0, analyzer-configured:1, original:2 }]
 }">
The second egress mirroring analyzer port or trunk and mirroring format.
 - `analyzer-configured` - packet is the same as the packet to the destination, VLAN format is modified based on the VLAN configurations of the analyzer port.
 - `modified` - packet is the same as the packet to the destination, VLAN format is modified based on the VLAN configurations of the egress port.
 - `original` - traffic is mirrored without any change to the original incoming packet format, but the service VLAN tag is stripped in the edge port.
</ArgTableRow>
<ArgTableRow arg="egress-mirror-ratio" typ="enum (1/1 | 1/2 | 1/4 | 1/8 | 1/16 | 1/32 | 1/64 | 1/128 | 1/256 | 1/512 | 1/1024 | 1/2048 | 1/4096 | 1/8192 | 1/16384 | 1/32768)">The proportion of egress mirrored packets compared to all packets.</ArgTableRow>
<ArgTableRow arg="fdb-uses" typ="enum (mirror0 | mirror1) { mirror0:0, mirror1:1 }">Analyzer port used for FDB-based mirroring.</ArgTableRow>
<ArgTableRow arg="vlan-uses" typ="enum (mirror0 | mirror1) { mirror0:0, mirror1:1 }">Analyzer port used for VLAN-based mirroring.</ArgTableRow>
<ArgTableRow arg="mirror-egress-if-ingress-mirrored" typ="bool">When a packet is applied to both ingress and egress mirroring, only ingress mirroring is performed on the packet, if this setting is disabled. If enabled, both mirroring types are applied.</ArgTableRow>
<ArgTableRow arg="mirror-tx-on-mirror-port" typ="bool"></ArgTableRow>
<ArgTableRow arg="mirrored-packet-qos-priority" typ="num">Remarked priority in mirrored packets.</ArgTableRow>
<ArgTableRow arg="mirrored-packet-drop-precedence" typ="enum (green | yellow | red | drop)">Remarked drop precedence in mirrored packets. This QoS attribute is used for mirrored packet enqueuing or dropping.</ArgTableRow>
<ArgTableRow arg="bypass-vlan-ingress-filter-for" typ="ubit (eapol, ripv1, dhcpv4, dhcpv6, igmp, mld, arp, nd, pppoe-discovery)">Protocols that are excluded from Ingress VLAN filtering. These protocols are not dropped if they have an invalid VLAN. (arp, dhcpv4, dhcpv6, eapol, igmp, mld, nd, pppoe-discovery, ripv1).</ArgTableRow>
<ArgTableRow arg="bypass-ingress-port-policing-for" typ="ubit (eapol, ripv1, dhcpv4, dhcpv6, igmp, mld, arp, nd, pppoe-discovery)">Protocols that are excluded from Ingress Port Policing. (arp, dhcpv4, dhcpv6, eapol, igmp, mld, nd, pppoe-discovery, ripv1).</ArgTableRow>
<ArgTableRow arg="bypass-l2-security-check-filter-for" typ="ubit (eapol, ripv1, dhcpv4, dhcpv6, igmp, mld, arp, nd, pppoe-discovery)">Protocols that are excluded from Policy rule security check. (arp, dhcpv4, dhcpv6, eapol, igmp, mld, nd, pppoe-discovery, ripv1).</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (QCA-8513L | QCA-8519 | QCA-8511) { QCA-8513L:9, QCA-8519:11, QCA-8511:12 }"></ArgTableRow>
</ArgTable>

## interface/ethernet/switch 
**Syscap:** rbswitch
**Type:** Directory

Global parameters for switches with Marwell Prestera chips.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mirror-source" typ="iface_enum { none:0 }" syscap="switch-mirror1">Selects a single mirroring source port. Ingress and egress traffic will be sent to the `mirror-target` port. Note that the `mirror-target` port has to belong to the same switch.</ArgTableRow>
<ArgTableRow arg="mirror-target" typ="iface_enum { none:0, cpu:0xffffffff }" syscap="switch-mirror-prestera">Selects a single mirroring target port. Mirrored packets from [`mirror-egress`](./port/port.md#mirror-egress), [`mirror-ingress`](./port/port.md#mirror-ingress) and [`mirror`](./rule/rule.md#mirror) will be sent to the selected port.</ArgTableRow>
<ArgTableRow arg="mirror-egress-target" typ="enum (none) { none:0 }" syscap="switch-mv88e6xxx">Selects a single mirroring egress target port. Mirrored packets from `mirror-egress` (see the property in the port menu) will be sent to the selected port.</ArgTableRow>
<ArgTableRow arg="rspan" typ="bool" syscap="switch-mirror-prestera">Enables the Remote Switch Port Analyzer (RSPAN) feature on `mirror-target`. Traffic marked for ingress or egress mirroring is carried over a specified remote analyzer VLAN - `rspan-egress-vlan-id` and `rspan-ingress-vlan-id`.</ArgTableRow>
<ArgTableRow arg="rspan-ingress-vlan-id" typ="num" syscap="switch-mirror-prestera">Selects the VLAN ID for marked ingress traffic. Only applies when `rspan` is enabled.</ArgTableRow>
<ArgTableRow arg="rspan-egress-vlan-id" typ="num" syscap="switch-mirror-prestera">Selects the VLAN ID for marked egress traffic. Only applies when `rspan` is enabled.</ArgTableRow>
<ArgTableRow arg="switch-all-ports" typ="bool">Changes the ether1 switch group only on RB450G/RB435G/RB850Gx2 devices. `yes` - ether1 is part of the switch and supports all advanced features including extended statistics. `no` - ether1 is not part of the switch, effectively making it a stand-alone ethernet port, increasing throughput but removing switching capability.</ArgTableRow>
<ArgTableRow arg="cpu-flow-control" typ="bool" syscap="switch-mv88e6xxx">Disables or enables the CPU Flow Control feature. The switch chip ensures the CPU port is not congested by sending out Pause Frames when link capacity is exceeded. Without this feature, packets crucial for routing or management may be dropped.</ArgTableRow>
<ArgTableRow arg="l3-hw-offloading" typ="bool" syscap="crs_prestera">Layer 3 hardware offloading. Allows offloading routing features onto the switch chip to reach wire speeds.</ArgTableRow>
<ArgTableRow arg="qos-hw-offloading" typ="bool" syscap="crs_prestera">Quality of Service hardware offloading. Allows enabling QoS for the given switch chip (if it supports QoS). Turning off the this setting will not completely revert to the previous functionality. It is recommended to reboot the device after disabling it.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (ADMtek | IC-Plus-175C | IC-Plus-178C | IC-Plus-175D | Atheros-8316 | Atheros-7240 | Atheros-8227 | Atheros-8327 | Atheros-8236 | QCA-8513L | Atheros-8327N | QCA-8519 | QCA-8511 | QCA-8337 | MediaTek-MT7621 | Realtek-RTL8367 | Marvell-98DX3236 | Marvell-98DX8216 | Marvell-98DX8208 | Marvell-98DX8332 | Marvell-98DX8212 | Marvell-98DX3257 | IPQ-PPE | Marvell-98DX8525 | Marvell-98PX1012 | Marvell-98DX4310 | Marvell-98DX224S | Marvell-98DX226S | Marvell-88E6393X | Marvell-98DX3255 | Marvell-88E6191X | Marvell-98DX2528 | Marvell-98CX8410 | Marvell-88E6341 | MediaTek-MT7531 | Marvell-88E6190 | Marvell-98DX7335 | Marvell-98DX3510 | Marvell-98DX3550 | MediaTek-MT7531AE | Marvell-98DX1508M | IPQ-9570 | Marvell-98DX3530 | Marvell-98DX4550M | QCA-8386 | EN7523 | Marvell-98DX2521 | Marvell-98DX2556 | Marvell-98DX2588 | Marvell-98DX7335M) { ADMtek:0, IC-Plus-175C:1, IC-Plus-178C:2, IC-Plus-175D:3, Atheros-8316:4, Atheros-7240:5, Atheros-8227:6, Atheros-8327:7, Atheros-8236:8, QCA-8513L:9, Atheros-8327N:10, QCA-8519:11, QCA-8511:12, QCA-8337:13, MediaTek-MT7621:14, Realtek-RTL8367:15, Marvell-98DX3236:16, Marvell-98DX8216:17, Marvell-98DX8208:18, Marvell-98DX8332:19, Marvell-98DX8212:20, Marvell-98DX3257:21, IPQ-PPE:22, Marvell-98DX8525:23, Marvell-98PX1012:24, Marvell-98DX4310:25, Marvell-98DX224S:26, Marvell-98DX226S:27, Marvell-88E6393X:28, Marvell-98DX3255:29, Marvell-88E6191X:30, Marvell-98DX2528:31, Marvell-98CX8410:32, Marvell-88E6341:33, MediaTek-MT7531:34, Marvell-88E6190:35, Marvell-98DX7335:36, Marvell-98DX3510:37, Marvell-98DX3550:38, MediaTek-MT7531AE:39, Marvell-98DX1508M:40, IPQ-9570:41, Marvell-98DX3530:42, Marvell-98DX4550M:43, QCA-8386:44, EN7523:45, Marvell-98DX2521:46, Marvell-98DX2556:47, Marvell-98DX2588:48, Marvell-98DX7335M:49 }"></ArgTableRow>
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
