# macvlan

> MACVLAN interfaces add virtual interfaces with their own MAC addresses on a parent interface. Several MACVLAN interfaces can share one parent.

-----------

## interface/macvlan 
**Type:** Directory

[MACVLAN](../../bridging-and-switching/macvlan.md) interfaces add virtual interfaces with their own MAC addresses on a parent interface. Several MACVLAN interfaces can share one parent.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="R" typ="running">Whether the interface is running.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Interface name.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the interface. When not set, RouterOS generates an address and stores it in the configuration, so it stays the same after a reboot.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Layer 3 maximum transmission unit. Default: `1500`. The value cannot be higher than the parent interface's MTU; if the parent's MTU is lower, set `mtu` when creating the interface.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">Parent interface. Any interface with a MAC address can be used, including an Ethernet, VLAN or bond interface. An active bridge port cannot be used: creation fails with `failed to create device` and the log reports a busy parent.</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (private | bridge) { private:1, bridge:4 }">Controls communication between MACVLAN interfaces on the same parent. `bridge`: the interfaces can communicate (default). `private`: they cannot; with either interface set to `private`, communication between them stops.</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }">[Address Resolution Protocol](../../getting-started/networking-fundamentals/index.md#arp-and-tying-it-all-together) mode. `disabled`: the interface does not use ARP. `enabled`: it uses ARP (default). `proxy-arp`: the router answers ARP requests on behalf of other interfaces. `local-proxy-arp`: it answers on the same interface. `reply-only`: the interface replies only for static entries in the IP/ARP table and does not learn dynamic entries.</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }">How long an ARP record is kept after no packets are received from the address. `auto` uses the value from `/ip/settings`, which is 30s by default. Default: `auto`.</ArgTableRow>
<ArgTableRow arg="arp-accept" typ="bool">Whether to accept gratuitous ARP (GARP) frames from devices that are not already in the ARP table. `no`: new entries are not created; `yes`: new entries are created. Default: `no`.</ArgTableRow>
<ArgTableRow arg="loop-protect" typ="enum (default | off | on) { default:0, off:1, on:2 }">Enables loop protection on the interface. `default` works as turned off. Default: `default`.</ArgTableRow>
<ArgTableRow arg="loop-protect-send-interval" typ="time">How often loop protect packets are sent on the interface. Default: `5s`.</ArgTableRow>
<ArgTableRow arg="loop-protect-disable-time" typ="time">How long the interface is disabled when a loop is detected. `0` disables it forever. Default: `5m`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="l2mtu" typ="num">[Layer2 maximum transmission unit](../../hardware/mtu-in-routeros.md).</ArgTableRow>
<ArgTableRow arg="loop-protect-status" typ="enum (off | on | disabled) { off:1, on:2, disabled:3 }">Current loop protect state: `off`, `on`, or `disabled`.</ArgTableRow>
</ArgTable>
