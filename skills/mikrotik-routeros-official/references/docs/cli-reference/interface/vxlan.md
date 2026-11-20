# vxlan

> Create and configure Virtual eXtensible Local Area Network (VXLAN) interfaces for Layer 2 overlays over routed IPv4 or IPv6 underlays. Interfaces can carry a comment. See the VXLAN guide for forwarding, configuration...

-----------

## interface/vxlan 
**Type:** Directory

Create and configure Virtual eXtensible Local Area Network (VXLAN) interfaces for Layer 2 overlays over routed IPv4 or IPv6 underlays. Interfaces can carry a `comment`. See the [VXLAN guide](../../../bridging-and-switching/vxlan) for forwarding, configuration examples, and hardware offload.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether the VXLAN interface is disabled. New interfaces are enabled by default.</ArgTableRow>
<ArgTableRow arg="R" typ="running">Whether the VXLAN interface is running.</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">Whether the VXLAN interface is hardware-offloaded on a supported device.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the VXLAN interface. Default: `vxlan1`.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Maximum transmission unit of the VXLAN interface. VXLAN adds 50 bytes of overhead over IPv4 and 70 bytes over IPv6; each inner 802.1Q tag adds another 4 bytes. Ensure that encapsulated Ethernet frames fit the underlay MTU, or reduce the frame or VXLAN MTU to prevent fragmentation and packet loss. Default: `1500`.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">Static MAC address of the VXLAN interface. If unset, RouterOS assigns a randomly generated address that persists when the interface is disabled and re-enabled. Default: automatically generated.</ArgTableRow>
<ArgTableRow arg="vni" typ="num" mandatory="1">VXLAN Network Identifier (VNI) of the overlay segment. VNI values must be unique across VXLAN interfaces on the router. Range: `1..16777215`.</ArgTableRow>
<ArgTableRow arg="group" typ="alt { address: ipAddr
, ipv6-address: ip6Addr
 }">Multicast group address used to forward broadcast, unknown-unicast, and multicast (BUM) traffic between VTEPs. This property requires `interface`. Setting `group` updates `vteps-ip-version` to the group address family. The underlay must provide multicast connectivity between VTEPs. A multicast underlay disables hardware offload on devices that support VXLAN offload. Default: unset.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">Interface used for multicast forwarding. This property requires `group`. A multicast underlay disables hardware offload on devices that support VXLAN offload. Default: unset.</ArgTableRow>
<ArgTableRow arg="port" typ="num">UDP port on which the VTEP listens and the destination port for packets sent to remote VTEPs. It does not fix the outer UDP source port. VXLAN interfaces that share a UDP port must use the same `checksum` setting and `vtep-vrf`. Range: `1..65535`. Default: `4789`.</ArgTableRow>
<ArgTableRow arg="local-address" typ="address (flags=46)">Local source address for outer VXLAN packets. If unset, RouterOS selects an address from the underlay egress interface. Setting this property updates `vteps-ip-version` to the local address family. Default: unset.</ArgTableRow>
<ArgTableRow arg="dont-fragment" typ="enum (disabled | enabled | auto | inherit) { disabled:0, enabled:1, auto:2, inherit:2 }">
Controls fragmentation and the Don't Fragment (DF) flag of outer packets.
- `disabled` - Clear DF in the outer IPv4 header and allow fragmentation when the encapsulated packet exceeds the outgoing interface MTU. Also allow fragmentation over an IPv6 underlay. Disables hardware offload on devices that support VXLAN offload.
- `enabled` - Set DF in the outer IPv4 header and drop packets that exceed the outgoing interface MTU. Also prevent fragmentation over an IPv6 underlay.
- `auto` (default) - Operate as `enabled` for hardware-offloaded VXLAN on supported devices, and as `inherit` without hardware offload.
- `inherit` - Copy the inner IPv4 DF flag to the outer IPv4 header. For non-IP inner packets, leave outer DF clear and allow fragmentation. For inner IPv6 packets, set outer DF. Drop an oversized packet when DF applies. With an IPv6 underlay, operate as `disabled`.
Default: `auto`.
</ArgTableRow>
<ArgTableRow arg="vtep-vrf" typ="enum">Routing table in which local VTEPs listen and originate underlay connections. Multicast `group` and `interface` settings do not support a VRF underlay. The same UDP `port` cannot be used in multiple routing tables. VXLAN-VRF offload is supported on CPSS switch chips; do not infer hardware support on other chips from this software property. Default: `main`.</ArgTableRow>
<ArgTableRow arg="vteps-ip-version" typ="enum (ipv4 | ipv6) { ipv4:1, ipv6:2 }">
Address family for local and remote VTEPs:
- `ipv4` (default) - Use an IPv4 underlay.
- `ipv6` - Use an IPv6 underlay. IPv6 disables hardware offload on devices that support VXLAN offload.
A VXLAN interface uses one address family at a time; configured remote VTEP entries of the opposite family are ignored. Setting `local-address` or multicast `group` updates this property to the corresponding address family.
Default: `ipv4`.
</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">Whether to allow Fast Path processing. Fragmented and flooded VXLAN packets are redirected through slow path. Fast Path is disabled for a VXLAN interface that uses a VRF. Default: `yes`.</ArgTableRow>
<ArgTableRow arg="max-fdb-size" typ="num">Maximum number of MAC addresses that the VXLAN forwarding database (FDB) can store. Range: `1..65535`. Default: `4096`.</ArgTableRow>
<ArgTableRow arg="ttl" typ="num">Time to live for outgoing outer IPv4 packets and hop limit for outer IPv6 packets. `auto` uses 64 for unicast underlays and 1 for multicast underlays. Increase the value when the multicast underlay crosses routers. Range: `0..255`. Default: `auto`.</ArgTableRow>
<ArgTableRow arg="learning" typ="bool">
Whether to learn inner source MAC addresses and remote VTEP addresses from received packets:
- `yes` (default) - Populate the VXLAN forwarding database dynamically.
- `no` - Suppress VXLAN FDB learning. When `bridge` is set, the dynamic bridge port also gets `learn=no`.
Default: `yes`.
</ArgTableRow>
<ArgTableRow arg="checksum" typ="bool">
UDP checksum handling for transmitted outer VXLAN packets:
- `no` (default) - Set the outer UDP checksum to zero. Also accept IPv6 VXLAN packets with a zero UDP checksum.
- `yes` - Calculate a valid UDP checksum for transmitted outer packets.
VXLAN interfaces that share a UDP port must use the same checksum setting. On devices that support VXLAN hardware offload, offloaded packets use a zero UDP checksum regardless of this setting.
Default: `no`.
</ArgTableRow>
<ArgTableRow arg="rem-csum" typ="enum (none | rx | tx | both) { none:0, rx:1, tx:2, both:3 }">
Remote Checksum Offload (RCO) mode. RCO elides the inner checksum of an encapsulated datagram so that the outer checksum can be offloaded by the network driver. RCO changes the encapsulation protocol, so the receiver must also support it.
- `none` (default) - Disable RCO.
- `rx` - Enable RCO for received packets.
- `tx` - Enable RCO for transmitted packets.
- `both` - Enable RCO for received and transmitted packets.
RCO is described in the Internet-Drafts `draft-herbert-vxlan-rco-00` and `draft-herbert-remotecsumoffload-00`. On devices that support VXLAN hardware offload, this setting is ignored for offloaded packets and RCO is disabled.
Default: `none`.
</ArgTableRow>
<ArgTableRow arg="hw" typ="bool">Whether to allow hardware offload on devices that support VXLAN offload. Set to `no` to disable offload for this interface. Default: `yes`.</ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum">Name of the bridge to which RouterOS adds the VXLAN interface as a dynamic port. Bridge VLAN entries configure tagged and untagged VLAN membership. Default: unset.</ArgTableRow>
<ArgTableRow arg="bridge-pvid" typ="num">Port VLAN ID assigned to the dynamic bridge port created by `bridge`. This property has an effect only when the bridge has `vlan-filtering=yes`; bridge VLAN entries control tagged and untagged membership. Range: `1..4094`. Default: `1`.</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }">
Address Resolution Protocol (ARP) mode:
- `disabled` - Do not use ARP on the interface.
- `enabled` (default) - Use ARP on the interface.
- `proxy-arp` - Answer ARP requests on behalf of other interfaces.
- `reply-only` - Reply only to requests that match static entries in `/ip/arp`, and do not create dynamic ARP entries. Communication requires a matching static entry.
- `local-proxy-arp` - Answer ARP requests on the same interface on behalf of other addresses.
Default: `enabled`.
</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }">How long an ARP entry is kept after no packets are received from the address. `auto` uses the `arp-timeout` value from `/ip/settings`, which is 30s by default. Default: `auto`.</ArgTableRow>
<ArgTableRow arg="arp-accept" typ="bool">Whether to accept gratuitous ARP replies and create new ARP entries for addresses not already present in `/ip/arp`. Default: `no`.</ArgTableRow>
<ArgTableRow arg="loop-protect" typ="enum (default | off | on) { default:0, off:1, on:2 }">
Loop protection mode on the interface:
- `default` (default) - Operate as `off`.
- `off` - Disable loop protection.
- `on` - Enable loop protection.
Default: `default`.
</ArgTableRow>
<ArgTableRow arg="loop-protect-send-interval" typ="time">How often loop protect packets are sent on the interface. Default: `5s`.</ArgTableRow>
<ArgTableRow arg="loop-protect-disable-time" typ="time">How long the interface is disabled when a loop is detected. `0` disables it forever. Default: `5m`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="l2mtu" typ="num">Read-only Layer 2 maximum transmission unit. Without an associated multicast `interface`, the value is `65535`. When the associated interface exposes its own L2MTU, VXLAN subtracts 50 bytes for an IPv4 underlay or 70 bytes for IPv6. Reduce `mtu` if it does not fit the associated interface.</ArgTableRow>
<ArgTableRow arg="loop-protect-status" typ="enum (off | on | disabled) { off:1, on:2, disabled:3 }">
Current loop protection state:
- `off` - Loop protection is disabled.
- `on` - Loop protection is enabled, and the interface sends and listens for loop protect packets.
- `disabled` - Loop protection is enabled, and the interface disabled itself after receiving a loop protect packet to prevent a loop.
</ArgTableRow>
</ArgTable>
