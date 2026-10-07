# L3 Hardware Offloading

> L3 Hardware Offloading enables routing at wire speed by offloading CPU-intensive tasks to the switch chip. This page details how to configure L3HW for entire switches, individual ports, and global settings like IPv6...

# L3 Hardware Offloading

**Layer 3 Hardware Offloading** (**L3HW**, otherwise known as IP switching or HW routing) allows offloading some router features onto the switch chip. This allows reaching wire speeds when routing packets, which would simply not be possible with the CPU.

## Switch Configuration

To enable Layer 3 Hardware Offloading, set `l3-hw-offloading=yes` for the switch:

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

### Switch Port Configuration

Layer 3 Hardware Offloading can be configured for each physical switch port. For example:

```ros
/interface/ethernet/switch/port/set sfp-sfpplus1 l3-hw-offloading=yes
```

Note that l3hw settings for switch and ports are different:

- Setting `l3-hw-offloading``=no` for the switch completely disables offloading - all packets will be routed by the CPU.
- However, setting `l3-hw-offloading``=no` for a switch port only disables hardware routing from/to this particular port. Moreover, the port can still participate in Fasttrack connection offloading.

To enable full hardware routing, enable l3hw on all switch ports:

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
/interface/ethernet/switch/port/set [find] l3-hw-offloading=yes
```

To make all packets go through the CPU first, and offload only the Fasttrack connections, disable l3hw on all ports but keep it enabled on the switch chip itself:

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
/interface/ethernet/switch/port/set [find] l3-hw-offloading=no
```

:::info
**Packets are routed by hardware when both the ingress and egress ports have `l3-hw-offloading=yes`.**

If both ingress and egress ports have `l3-hw-offloading=no`, packets will go through the CPU/Firewall while offloading only the Fasttrack connections.

It is possible to direct packets to go through the CPU/Firewall by setting `l3-hw-offloading=no` on just the egress port. However, setting `l3-hw-offloading=no` only the ingress port may cause unpredictable behavior, for example, packets might still be routed by hardware and completely bypass the CPU/firewall.
:::

The next example enables hardware routing on all ports but the upstream port (sfp-sfpplus16). Packets going to/from sfp-sfpplus16 will enter the CPU and, therefore, be subject to Firewall/NAT processing.

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
/interface/ethernet/switch/port/set [find] l3-hw-offloading=yes
/interface/ethernet/switch/port/set sfp-sfpplus16 l3-hw-offloading=no
```

:::warning
The existing connections may be unaffected by the `l3-hw-offloading` setting change.
:::

### L3HW Settings

Settings menu [`/interface/ethernet/switch/l3hw-settings`](../cli-reference/interface/ethernet/switch/l3hw-settings/l3hw-settings.md) can be used to tweak L3HW behavior according to setup needs.

### Interface Lists

It is impossible to use interface lists directly to control `l3-hw-offloading` because an interface list may contain virtual interfaces (such as VLAN) while the `l3-hw-offloading` setting must be applied to physical switch ports only. For example, if there are two VLAN interfaces (vlan20 and vlan30) running on the same switch port (trunk port), it is impossible to enable hardware routing on vlan20 but keep it disabled on vlan30.

However, an interface list may be used as a port selector. The following example demonstrates how to enable hardware routing on LAN ports (ports that belong to the "LAN" interface list) and disable it on WAN ports:

```ros
:foreach i in=[/interface/list/member/find where list=LAN] do={
    /interface/ethernet/switch/port/set [/interface/list/member/get $i interface] l3-hw-offloading=yes
}

:foreach i in=[/interface/list/member/find where list=WAN] do={
    /interface/ethernet/switch/port/set [/interface/list/member/get $i interface] l3-hw-offloading=no
}
```

Please take into account that since interface lists are not directly used in hardware routing control, **modifying the interface list also does not automatically reflect in l3hw changes**. For instance, adding a switch port to the "LAN" interface list does not automatically enable `l3-hw-offloading` on it. The user has to rerun the above script to apply the changes.

### MTU

The hardware supports up to 8 MTU profiles, meaning that the user can set up to 8 different MTU values for interfaces: the default 1500 + seven custom ones.

:::tip
It is recommended to disable `l3-hw-offloading` while changing the MTU/L2MTU values on the interfaces.
:::

**MTU Change Example**

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=no
/interface/set sfp-sfpplus1 mtu=9000 l2mtu=9022
/interface/set sfp-sfpplus2 mtu=9000 l2mtu=9022
/interface/set sfp-sfpplus3 mtu=10000 l2mtu=10022
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

### Layer 2 Dependency

Layer 3 hardware processing lies on top of Layer 2 hardware processing. Therefore, L3HW offloading requires L2HW offloading on the underlying interfaces. The latter is enabled by default, but there are some exceptions. For example, MikroTik devices with Marvell Prestera switch support only one hardware bridge. If there are multiple bridges, others are processed by the CPU and are not subject to L3HW.

Another example is ACL rules. If a rule redirects traffic to the CPU for software processing, then hardware routing (L3HW) is not triggered:

#### ACL rule to disable hardware processing on a specific port

```ros
/interface/ethernet/switch/rule/add switch=switch1 ports=ether1 redirect-to-cpu=yes
```

:::tip
It is recommended to turn off L3HW offloading during L2 configuration.
:::

To make sure that Layer 3 is in sync with Layer 2 on both the software and hardware sides, we recommend disabling L3HW while configuring Layer 2 features. The recommendation applies to the following configuration:

- Adding/removing/enabling/disabling bridges.
- Adding/removing switch ports to/from the bridge.
- Bonding switch ports / removing bonds.
- Changing VLAN settings.
- Changing MTU/L2MTU on switch ports.
- Changing ethernet (MAC) addresses.

In short, disable `l3-hw-offloading` while making changes under `/interface/bridge/` and `/interface/vlan/`:

#### Layer 2 Configuration Template

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=no

/interface/bridge
# put bridge configuration changes here

/interface/vlan
# define/change VLAN interfaces
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

### MAC telnet

There is a limitation for MAC telnet when L3HW offloading is enabled on **98DX8xxx**, **98DX4xxx,** or **98DX325x** switch chips. Packets from MAC Telnet are dropped and do not reach the CPU, thus access to the device will fail.

If MAC telnet is desired in combination with L3HW, a certain ACL rule can be created to force these packets to the CPU.

For example, if MAC telnet access on sfp-sfpplus1 and sfp-sfpplus2 is needed, you will need to add this ACL rule. It is possible to select even more interfaces with the `ports` setting.

```ros
/interface/ethernet/switch/rule
add dst-port=20561 ports=sfp-sfpplus1,sfp-sfpplus2 protocol=udp redirect-to-cpu=yes switch=switch1
```

### Inter-VLAN Routing

Since L3HW depends on L2HW, and L2HW is the one that does VLAN processing, Inter-VLAN *hardware* routing typically requires a hardware bridge underneath. Even if a particular VLAN has only one tagged port member, the port must be a bridge member, and the VLAN interface must be assigned to the bridge.

Devices with Marvell 98DX7xxx series switch chips are an exception — they also support hardware routing between VLAN interfaces created directly on Ethernet switch ports, without a bridge:

`/interface/vlan/add interface=ether2 name=vlan20 vlan-id=20`

On all other L3HW devices, do not assign a VLAN interface directly to a switch port — such an interface does not get offloaded and its traffic is routed by the CPU. Assign the VLAN interface to the bridge instead. This way, VLAN configuration gets offloaded to the hardware, and, with L3HW enabled, the traffic is subject to inter-VLAN hardware routing.

#### VLAN Configuration Example

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=no
/interface/bridge/port/add bridge=bridge interface=ether2
/interface/bridge/vlan/add bridge=bridge tagged=bridge,ether2 vlan-ids=20
/interface/vlan/add interface=bridge name=vlan20 vlan-id=20
/ip/address/add address=192.0.2.1/24 interface=vlan20
/interface/bridge/set bridge vlan-filtering=yes
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

:::info
For Inter-VLAN routing, the bridge interface must be a tagged member of every routable `/interface/bridge/vlan/` entry.
:::

### Per-VLAN offloading

It is possible to configure L3HW offloading per individual VLAN interface using the `l3-hw-offloading=yes|no` setting in the `/interface/vlan` menu. This provides finer control over which VLANs (and their related routes) are offloaded to the switch chip, and which are processed by the CPU. It is no longer necessary to disable L3HW on a switch port in order to disable L3HW routing for specific VLANs.

VLAN interface gets offloaded (receives the H flag) only when ALL the following conditions are met:

- VLAN interface has `l3-hw-offloading=yes`.
- VLAN interface is created on a hardware-offloaded, vlan-filtering bridge, or, on 98DX7xxx switches, directly on an Ethernet switch port.
- All involved switch ports have l3-hw-offloading=yes — all member ports of the VLAN for the bridge case, or the parent port for a VLAN interface created directly on a switch port.

For inter-VLAN routing, both ingress and egress VLANs must be hw-offloaded, otherwise, packets are sent to the CPU.

:::info
If a switch port carries multiple VLANs with different L3HW settings, keep the port's `l3-hw-offloading=yes`.
:::

### L3HW MAC Address Range Limitation (DX2000/DX3000 series only)

Marvell Prestera DX2000 and DX3000 switch chips have a hardware limitation that allows configuring only the last (least significant) octet of the MAC address for each interface. The other five (most significant) octets are configured globally and, therefore, must be equal for all interfaces (switch ports, bridge, VLANs). In other words, the MAC addresses must be in the format "**XX:XX:XX:XX:XX:??**", where:

- "**XX:XX:XX:XX:XX**" part is common for all interfaces.
- "**??**" is a variable part.

**This requirement applies only to Layer 3 (routing).** Layer 2 (bridging) does not use the switch's ethernet addresses. Moreover, it does not apply to bridge ports because they use the bridge's MAC address.

The requirement for common five octets applies to:

- Standalone switch ports (not bridge members) with hardware routing enabled (`l3-hw-offloading=yes`).
- Bridge itself.
- VLAN interfaces (those that use the bridge's MAC address by default).

## Route Configuration

---

### Suppressing HW Offload

By default, all the routes are hardware candidate routes. To further fine-tune which traffic to offload, there is an option for each route to disable/enable **`suppress-hw-offload`**.

For example, if we know that the majority of traffic flows to the network where servers are located, we can enable offloading only to that specific destination:

```ros
/ip/route/set [find where static && dst-address!="192.168.3.0/24"] suppress-hw-offload=yes
```

Now only the route to 192.168.3.0/24 has H-flag, indicating that it will be the only one eligible to be selected for HW offloading:

```ros
[admin@MikroTik] > /ip/route/print where static
Flags: A - ACTIVE; s - STATIC, y - COPY; H - HW-OFFLOADED
Columns: DST-ADDRESS, GATEWAY, DISTANCE
#     DST-ADDRESS       GATEWAY         D
0 As  0.0.0.0/0         172.16.2.1      1
1 As  10.0.0.0/8        10.155.121.254  1
2 AsH 192.168.3.0/24    172.16.2.1      1
```

:::danger
H-flag does not indicate that the route is actually HW offloaded; it indicates only that the route can be selected to be HW offloaded.
:::

### Routing Filters

For dynamic routing protocols like OSPF and BGP, it is possible to suppress HW offloading using [routing filters](../user-guides/routing-and-networking-protocols/route-selection-and-filtering.md). For example, to suppress HW offloading on all OSPF instance routes, use the "**`suppress-hw-offload yes`**" property:

```ros
/routing/ospf/instance
set [find name=instance1] in-filter-chain=ospf-input
/routing/filter/rule
add chain="ospf-input" rule="set suppress-hw-offload yes; accept"
```

### Offloading Fasttrack Connections

Firewall filter rules have the **`hw-offload`** option for Fasttrack, allowing fine-tuning connection offloading. Since the hardware memory for Fasttrack connections is very limited, we can choose what type of connections to offload and, therefore, benefit from near-the-wire-speed traffic. The next example offloads only TCP connections while UDP packets are routed via the CPU and do not occupy HW memory:

```ros
/ip/firewall/filter
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=yes protocol=tcp
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=no
add action=accept chain=forward connection-state=established,related
```

### Stateless Hardware Firewall

While connection tracking and stateful firewalling can be performed only by the CPU, the hardware can perform stateless firewalling via [switch rules (ACL)](./marvell-prestera-switch-chip-features.md#switch-rules-acl). The next example prevents (on a hardware level) accessing a MySQL server from ether1, and redirects packets from ether2 and ether3 to the CPU/Firewall:

```ros
/interface/ethernet/switch/rule
add switch=switch1 dst-address=10.0.1.2/32 dst-port=3306 ports=ether1 new-dst-ports=""
add switch=switch1 dst-address=10.0.1.2/32 dst-port=3306 ports=ether2,ether3 redirect-to-cpu=yes
```

### Switch Rules (ACL) vs. Fasttrack HW Offloading

Some firewall rules may be implemented via both [switch rules (ACL)](./marvell-prestera-switch-chip-features.md#switch-rules-acl) and CPU [Firewall Filter](../firewall-and-quality-of-service/firewall/filter.md) + Fasttrack HW Offloading. Both options grant near-the-wire-speed performance. So the question is which one to use?

First, [not all devices support Fasttrack HW Offloading](./l3-hardware-offloading.md#l3hw-device-support), and without HW offloading, Firewall Filter uses only software routing, which is dramatically slower than its hardware counterpart. Second, even if Fasttrack HW Offloading is an option, a rule of thumb is:

:::tip
Always use Switch Rules (ACL), if possible.
:::

Switch rules share the hardware memory with Fasttrack connections. However, hardware resources are allocated for each Fasttrack connection while a single ACL rule can match multiple connections. For example, if you have a guest WiFi network connected to sfp-sfpplus1 VLAN 10 and you don't want it to access your internal network, simply create an ACL rule:

```ros
/interface/ethernet/switch/rule
add switch=switch1 ports=sfp-sfpplus1 vlan-id=10 dst-address=10.0.0.0/8 new-dst-ports=""
```

The matched packets will be dropped on the hardware level. It is much better than letting *all* guest packets go to the CPU for Firewall filtering.

Of course, ACL rules cannot match everything. For instance, ACL rules cannot filter connection states: accept established, drop others. That is where Fasttrack HW Offloading gets into action - redirect the packets to the CPU by default for firewall filtering, then offload the established Fasttrack connections. However, disabling `l3-hw-offloading` for the entire switch or port is not the only option.

:::info
Define ACL rules with `redirect-to-cpu=yes` instead of setting `l3-hw-offloading=no` on the switch port for narrowing down the traffic that goes to the CPU.
:::

### Hardware-Offloaded VRF

Hardware-offloaded VRF is supported on [98DX8xxx, 98DX4xxx, 98DX325x, 98CX8410](#ccr2xxx-crs3xx-crs5xx-switch-98dx8xxx-and-98dx4xxx-series) and [98DX7xxx](#crs8xx-switch-98dx7xxx-series) switch chips. It is not supported on [98DX3xxx and 98DX2xxx](#crs3xx-switch-98dx3xxx-and-98dx2xxx-series) series.

If routes are in a VRF and the egress interface is L3HW-capable the switch chip will route the packet. You can associate any L3HW-capable interface (Ethernet, bonding, bridge, VLAN) with a VRF. Always associate the master interface with the VRF, not an interface marked with the `S` (slave) flag, such as a bridge or bonding port. Fasttrack, NAT, and VXLAN offloading are limited to the `main` routing table only.

VRFs are configured under `/ip/vrf`. For more details, see the [VRF](../user-guides/routing-and-networking-protocols/vrf) manual.

98DX8208, 98DX8212, 98DX8332, 98DX3257, 98DX3255 support up to 512 VRF tables. All other supported switch chips support up to 1024.

#### VRF Assignment via ACL

L3HW supports assigning VRF to ingress traffic using ACL switch rules. The `new-vrf` option in `/interface/ethernet/switch/rule` allows directing matched packets into a specific VRF table.

On VRF-unaware switches (98DX3xxx and 98DX2xxx series), setting `new-vrf` to anything other than `main` will result in `redirect-to-cpu=yes`.

For more details on ACL rules, see [Switch Rules (ACL)](./marvell-prestera-switch-chip-features.md#switch-rules-acl).

## Configuration Examples

---

### Inter-VLAN Routing with Upstream Port Behind Firewall/NAT

This example demonstrates how to benefit from near-to-wire-speed inter-VLAN routing while keeping Firewall and NAT running on the upstream port. Moreover, Fasttrack connections to the upstream port get offloaded to hardware as well, boosting the traffic speed close to wire-level. Inter-VLAN traffic is fully routed by the hardware, not entering the CPU/Firewall, and, therefore, not occupying the hardware memory of Fasttrack connections.

We use the **CRS317-1G-16S+** model with the following setup:

- sfp1-sfp4 - bridged ports, VLAN ID 20, untagged.
- sfp5-sfp8 - bridged ports, VLAN ID 30, untagged.
- sfp16 - the upstream port.
- ether1 - management port.

Set up interface lists for easy access:

### Interface Lists

```ros
/interface/list
add name=LAN
add name=WAN
add name=MGMT 

/interface/list/member
add interface=sfp-sfpplus1 list=LAN
add interface=sfp-sfpplus2 list=LAN
add interface=sfp-sfpplus3 list=LAN
add interface=sfp-sfpplus4 list=LAN
add interface=sfp-sfpplus5 list=LAN
add interface=sfp-sfpplus6 list=LAN
add interface=sfp-sfpplus7 list=LAN
add interface=sfp-sfpplus8 list=LAN
add interface=sfp-sfpplus16 list=WAN
add interface=ether1 list=MGMT 
```

### Bridge Setup

```ros
/interface/bridge
add name=bridge vlan-filtering=yes

/interface/bridge/port
add bridge=bridge interface=sfp-sfpplus1 pvid=20
add bridge=bridge interface=sfp-sfpplus2 pvid=20
add bridge=bridge interface=sfp-sfpplus3 pvid=20
add bridge=bridge interface=sfp-sfpplus4 pvid=20
add bridge=bridge interface=sfp-sfpplus5 pvid=30
add bridge=bridge interface=sfp-sfpplus6 pvid=30
add bridge=bridge interface=sfp-sfpplus7 pvid=30
add bridge=bridge interface=sfp-sfpplus8 pvid=30

/interface/bridge/vlan
add bridge=bridge tagged=bridge untagged=sfp-sfpplus1,sfp-sfpplus2,sfp-sfpplus3,sfp-sfpplus4 vlan-ids=20
add bridge=bridge tagged=bridge untagged=sfp-sfpplus5,sfp-sfpplus6,sfp-sfpplus7,sfp-sfpplus8 vlan-ids=30
```

Routing requires dedicated VLAN interfaces. For standard L2 VLAN bridging (without inter-VLAN routing), the next step can be omitted.

#### VLAN Interface Setup for Routing

```ros
/interface/vlan
add interface=bridge name=vlan20 vlan-id=20
add interface=bridge name=vlan30 vlan-id=30

/ip/address
add address=192.168.20.17/24 interface=vlan20 network=192.168.20.0
add address=192.168.30.17/24 interface=vlan30 network=192.168.30.0
```

Configure management and upstream ports, a basic firewall, NAT, and enable hardware offloading of Fasttrack connections:

#### Firewall Setup

```ros
/ip/address
add address=192.168.88.1/24 interface=ether1
add address=10.0.0.17/24 interface=sfp-sfpplus16

/ip/route
add gateway=10.0.0.1

/ip/firewall/filter
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=yes
add action=accept chain=forward connection-state=established,related

/ip/firewall/nat
add action=masquerade chain=srcnat out-interface-list=WAN
```

At this moment, all routing still is performed by the CPU. Enable hardware routing on the switch chip:

#### Enable Layer 3 Hardware Offloading

```ros
# Enable full hardware routing on LAN ports
:foreach i in=[/interface/list/member/find where list=LAN] do={ 
    /interface/ethernet/switch/port/set [/interface/list/member/get $i interface] l3-hw-offloading=yes 
} 

# Disable full hardware routing on WAN or Management ports
:foreach i in=[/interface/list/member/find where list=WAN or list=MGMT] do={ 
    /interface/ethernet/switch/port/set [/interface/list/member/get $i interface] l3-hw-offloading=no 
}

# Activate Layer 3 Hardware Offloading on the switch chip
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

Results:

- Within the same VLAN (e.g., sfp1-sfp4), traffic is forwarded by the hardware on Layer 2 *(L2HW)*.
- Inter-VLAN traffic (e.g. sfp1-sfp5) is routed by the hardware on Layer 3 *(L3HW).*
- Traffic from/to the WAN port gets processed by the CPU/Firewall first. Then Fasttrack connections get offloaded to the hardware *(Hardware-Accelerated L4 Stateful Firewall).* NAT applies both on CPU- and HW-processed packets.
- Traffic to the management port is protected by the Firewall.

## Typical Misconfiguration

---
Below are typical user errors in configuring Layer 3 Hardware Offloading.

### VLAN interface on a switch port or bond

```ros
/interface/vlan
add name=vlan10 vlan-id=10 interface=sfp-sfpplus1
add name=vlan20 vlan-id=20 interface=bond1
```

Due to Layer 2 dependency, on most devices only VLAN interfaces created on a hardware-offloaded, vlan-filtering bridge are capable of L3HW offloading. The correct configuration is:

```ros
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus1 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=bond1 frame-types=admit-only-vlan-tagged
 
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,sfp-sfpplus1 vlan-ids=10
add bridge=bridge1 tagged=bridge1,bond1 vlan-ids=20
 
/interface/vlan
add name=vlan10 vlan-id=10 interface=bridge1
add name=vlan20 vlan-id=20 interface=bridge1
```

:::warning
If VLAN interfaces are created directly on Ethernet or bonding interfaces on devices that do not support offloading such interfaces (see [Inter-VLAN Routing](#inter-vlan-routing)), packets may be offloaded incorrectly - bypassing CPU processing (such as firewall and NAT) and causing undefined behavior.

If this type of configuration is required, L3HW offloading must be disabled on the related switch ports under the `/interface/ethernet/switch/port` menu by setting `l3-hw-offloading=no`.
:::

### Not adding the bridge interface to /interface/bridge/vlan/

For Inter-VLAN routing, the bridge interface itself needs to be added to the tagged members of the given VLANs. In the next example, Inter-VLAN routing works between VLAN 10 and 11, but packets are NOT routed to VLAN 20.

```ros
/interface/bridge/vlan
add bridge=bridge1 vlan-ids=10 tagged=bridge1,sfp-sfpplus1
add bridge=bridge1 vlan-ids=11 tagged=bridge1 untagged=sfp-sfpplus2,sfp-sfpplus3 
add bridge=bridge1 vlan-ids=20 tagged=sfp-sfpplus1 untagged=sfp-sfpplus4,sfp-sfpplus5
```

The above example does not always mean an error. Sometimes, you may want the device to act as a simple L2 switch in some/all VLANs. Just make sure you set such behavior on purpose, not due to a mistake.

### Creating multiple bridges

The devices support only one hardware bridge. If there are multiple bridges created, only one gets hardware offloading. While for L2 that means software forwarding for other bridges, in the case of L3HW, multiple bridges may lead to undefined behavior.

:::tip
Instead of creating multiple bridges, create one and segregate L2 networks with VLAN filtering.
:::

### Using ports that do not belong to the switch

Some devices have two switch chips or the management port directly connected to the CPU. For example, **CRS312-4C+8XG** has an **ether9** port connected to a separate switch chip. Trying to add this port to a bridge or involve it in the L3HW setup leads to unexpected results. Leave the management port for management!

```ros
[admin@crs312] /interface/ethernet/switch> print
Columns: NAME, TYPE, L3-HW-OFFLOADING
# NAME     TYPE              L3-HW-OFFLOADING
0 switch1  Marvell-98DX8212  yes            
1 switch2  Atheros-8227      no   
           
[admin@crs312] /interface/ethernet/switch> port print
Columns: NAME, SWITCH, L3-HW-OFFLOADING, STORM-RATE
 # NAME         SWITCH   L3-HW-OFFLOADING  STORM-RATE
 0 ether9       switch2                             
 1 ether1       switch1  yes                      100
 2 ether2       switch1  yes                      100
 3 ether3       switch1  yes                      100
 4 ether4       switch1  yes                      100
 5 ether5       switch1  yes                      100
 6 ether6       switch1  yes                      100
 7 ether7       switch1  yes                      100
 8 ether8       switch1  yes                      100
 9 combo1       switch1  yes                      100
10 combo2       switch1  yes                      100
11 combo3       switch1  yes                      100
12 combo4       switch1  yes                      100
13 switch1-cpu  switch1                           100
14 switch2-cpu  switch2
```

### Relying on Fasttrack HW Offloading too much

Since Fasttrack HW Offloading offers near-the-wire-speed performance at zero configuration overhead, users are tempted to use it as the default solution. However, the number of HW Fasttrack connections is very limited, leaving the other traffic for the CPU. Try using the hardware routing as much as possible, reduce the CPU traffic to the minimum via switch ACL rules, and then fine-tune which Fasttrack connections to offload with firewall filter rules.

### Trying to offload slow-path connections

Using certain configurations (e.g. enabling bridge "**use-ip-firewall**" setting, creating bridge nat/filter rules) or running specific features like sniffer or torch can disable RouterOS [FastPath](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path), which will affect the ability to properly FastTrack and HW offload connections. If HW offloaded Fasttrack is required, make sure that there are no settings that disable the FastPath and verify that connections are getting the "H" flag or use the L3HW [monitor](../cli-reference/interface/ethernet/switch/l3hw-settings/monitor.md) command to see the number of HW offloaded connections.

## L3HW Feature Support

- **HW** - The feature is supported and offloaded to the hardware.
- **CPU** - The feature is supported but performed by software (CPU).
- **N/A** - The feature is not available together with L3HW. Layer 3 hardware offloading must be completely disabled (**switch** `l3-hw-offloading=no`) to make this feature work.
- **FW** - The feature requires `l3-hw-offloading=no` for a given **switch port**. On the **switch** level, `l3-hw-offloading=yes`.

| Feature | Support | Comments | Release |
| :-- | :-- | :-- | :-- |
| IPv4 Unicast Routing | **HW** |  | 7.1 |
| IPv6 Unicast Routing | **HW** | `/interface/ethernet/switch/l3hw-settings/set ipv6-hw=yes` | 7.6 |
| IPv4 Multicast Routing | **CPU** |  |  |
| IPv6 Multicast Routing | **CPU** |  |  |
| ECMP | **HW** | Multipath routing | 7.1 |
| Blackholes | **HW** | `/ip/route/add dst-address=10.0.99.0/24 blackhole` | 7.1 |
| `gateway=<interface_name>` | **CPU/HW** | `/ip/route/add dst-address=10.0.0.0/24 gateway=ether1` This works only for directly connected networks. Since HW does not know how to send ARP requests, CPU sends an ARP request and waits for a reply to find out the DST MAC address on the first received packet of the connection that matches a DST IP address. After DST MAC is determined, HW entry is added and all further packets will be processed by the switch chip. | 7.1 |
| Bridge | **HW** | Routing from/to [hardware-offloaded bridge](./#bridge-hardware-offloading) interface. | 7.1 |
| VLAN | **HW** | Routing between VLAN interfaces that are created on hardware-offloaded bridge interface with [vlan-filtering](index.md#bridge-vlan-filtering). On [98DX7xxx](#crs8xx-switch-98dx7xxx-series) switches, also between VLAN interfaces created directly on Ethernet switch ports. `/interface/vlan` | 7.1 |
| Bonding | **HW** | Routing between bonding interfaces. `/interface/bonding` Only `802.3ad` and `balance-xor` bonding modes are hardware offloaded. | 7.1 |
| IPv4 Firewall | **FW** | Users must choose either HW-accelerated routing or firewall. Firewall rules get processed by the CPU. ***Fasttrack*** connections get offloaded to HW. | 7.1 |
| IPv4 NAT | **FW** | NAT rules applied to the offloaded ***Fasttrack*** connections get processed by HW too. | 7.1 |
| MLAG | **N/A** |  |  |
| VRF | **HW** | [Hardware-offloaded VRF](#hardware-offloaded-vrf). |  |
| VRRP | **N/A** |  |  |
| Traffic-Flow | **N/A** | L3HW offloaded traffic is not reported through [Traffic Flow](../diagnostics-monitoring-and-troubleshooting/traffic-flow/index.md). |  |
| VXLAN | **HW** | Support for hardware-offloaded [VXLAN](./vxlan.md) data plane, VXLAN encapsulation and decapsulation. This allows for static one-to-one VLAN-to-VXLAN mappings within a vlan-filtering bridge.  At this point, some known features are not yet implemented.  **Underlay (routing encapsulated VXLAN packets):**  1. VTEPs are not supported over ECMP  2. VTEPs are not supported over bond, bridge, VLAN interfaces (only stand-alone routed Ethernet interfaces are supported)  3. VTEPs are not supported over multicast  4. VXLAN hardware offloading is limited to the `main` routing table. VTEPs cannot operate within VRFs.  5. VTEPs are not supported with IPv6  **Overlay (forwarding between Ethernet and VXLAN):**  1. VLAN tagging over VXLAN is not supported  2. Routing between different VXLAN VNIs is not supported  3. VTEPs are isolated, and there is no mechanism to control "horizon" between them.  4. Bridged VXLAN interfaces do not support IGMP snooping. When snooping is enabled, MDB entries on VXLAN are not offloaded, and multicast traffic gets restricted between Ethernet and VXLAN.  5. Bridged VXLAN interfaces are not supported by MLAG. `/interface/vxlan` | 7.18 |
| MTU | **HW** | The hardware supports up to 8 MTU profiles. | 7.1 |
| QinQ Routing | **CPU** | Stacked routable VLAN interfaces will lose L3HW offloading, while routable VLAN interfaces created directly on the bridge interface can still use HW offloading. |  |
| IPv4 routes with IPv6 nexthops or vice versa | **N/A** |  |  |

Only the devices listed in the table below support L3 HW Offloading.

## L3HW Device Support

Only the devices listed in the table below support L3 HW Offloading.

### CRS3xx: Switch 98DX3xxx and 98DX2xxx Series

The devices below are based on **Marvell **98DX224S, 98DX226S****, **98DX2528,** or **98DX3236** switch chip models.

:::info
The **98DX3255** and **98DX3257** models are exceptions, which have a feature set of the 98DX8xxx rather than the 98DX3xxx series.

**Caution:** Below are some important features that these devices are missing when compared to other switch models:

- Fasttrack and NAT connection offloading
- per-VLAN packet and byte counters
- VXLAN offloading
- hardware-offloaded VRF.

:::

| Switch Chip | Models | IPv4 Route Prefixes <sup>1</sup> | IPv6 Route Prefixes <sup>2</sup> | Nexthops | ECMP paths per prefix <sup>3</sup> |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **98DX3236** | CRS305-1G-4S+IN  CRS326-24G-2S+ (RM/IN)  CRS328-24P-4S+RM  CRS328-4C-20S-4S+RM | 13312 | 3328 | 4K | 8 |
| **98DX226S** | CRS305-1G-4S+OUT (FiberBox Plus)  CRS310-1G-5S-4S+ (netFiber 9/IN)  CRS310-8G+2S+IN  CRS318-16P-2S+OUT (netPower 16P)  CRS320-8P-8B-4S+RM  CRS418-8P-8G-2S+RM  CRS418-8P-8G-2S+5axQ2axQ-RM | 13312 | 3328 | 4K | 8 |
| **98DX224S** | CRS318-1Fi-15Fr-2S-OUT (netPower 15FR) | 13312 | 3328 | 4K | 8 |
| **98DX2528** | CRS304-4XG-IN | 13312 | 3328 | 4K | 8 |

---

<sup>1</sup> Since the total number of routes that can be offloaded is limited, prefixes with higher netmask are preferred to be forwarded by hardware (e.g., /32, /30, /29, etc.). Any other prefixes that do not fit in the HW table will be processed by the CPU. Directly connected hosts are offloaded as /32 (IPv4) or /128 (IPv6) route prefixes. The number of hosts is also limited by max-neighbor-entries in [IP Settings](../cli-reference/ip/settings.md) / [IPv6 Settings](../cli-reference/ipv6/settings.md).  
<sup>2</sup> IPv4 and IPv6 routing tables share the same hardware memory.  
<sup>3</sup> If a route has more paths than the hardware ECMP limit (X), only the first X paths get offloaded.

#### Partial offloading

In the case of **98DX3xxx**, **98DX2xxx** switch chip series, it is quite simple: one RouterOS route entry (/ip/route/) reflects into one HW IPv4 route prefix entry. Connected hosts (/32 routes) also occupy the same table. As long as the total number of routes ("/ip/route/print count-only") + connected host count ("/ip/arp/print count-only where status=reachable or status=stale"), does not exceed **13312 (13k)**, everything gets offloaded. Exceeding the number, routes with *shorter* prefixes stay on the CPU.

### CCR2xxx, CRS3xx, CRS5xx: Switch 98DX8xxx and 98DX4xxx Series

The devices below are based on **Marvell 98DX8xxx**, **98DX4xxx** switch chips, or **98DX325x** model.

<WideTable>

| Switch Chip | Models | IPv4 Routes <sup>1</sup> | IPv4 Hosts <sup>5</sup> | IPv6 Routes <sup>1</sup> | IPv6 Hosts <sup>5</sup> | Nexthops | IPv4 Fasttrack connections <sup>2, 3, 4</sup> | IPv4 NAT entries <sup>2, 4</sup> | IPv4 Fasttrack/NAT, VXLAN offloading Per-VLAN packet/byte counters |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **98DX8208** | CRS309-1G-8S+IN | up to 36K | up to 16K | up to 6K | up to 12K | 8K | 4.5K | 3.9K | + |
| **98DX8212** | CRS312-4C+8XG-RM | up to 36K | up to 16K | up to 6K | up to 12K | 8K | 2.25K | 2.25K | + |
| **98DX8216** | CRS317-1G-16S+RM | up to 240K | up to 64K | up to 40K | up to 48K | 8K | 4.5K | 4K | + |
| **98DX8332** | CRS326-24S+2Q+RM  CRS326-4C+20G+2Q+RM | up to 36K | up to 16K | up to 6K | up to 12K | 8K | 2.25K | 2.25K | + |
| **98DX3257** <sup>6</sup> | CRS354-48G-4S+2Q+RM  CRS354-48P-4S+2Q+RM | up to 36K | up to 16K | up to 6K | up to 12K | 8K | 2.25K | 2.25K | + |
| **98DX4310** | CRS504-4XQ (IN/OUT)  CRS510-8XS-2XQ-IN  RDS2216-2XG-4S+4XS-2XQ | up to 120K | up to 64K | up to 20K | up to 48K | 8K | 4.5K | 4K | + |
| **98CX8410** | CRS520-4XS-16XQ-RM | up to 240K | up to 64K | up to 40K | up to 48K | 8K | 4.5K | 4K | + |
| **98DX3255** <sup>6</sup> | CCR2116-12G-4S+ | up to 36K | up to 16K | up to 6K | up to 12K | 8K | 2.25K | 2.25K | + |
| **98DX8525** | CCR2216-1G-12XS-2XQ  CRS518-16XS-2XQ-RM | up to 120K | up to 64K | up to 20K | up to 48K | 8K | 4.5K | 4K | + |

</WideTable>

<sup>1</sup> Depends on the complexity of the routing table. Whole-byte IP prefixes (/8, /16, /24, etc.) occupy less HW space than others (e.g., /22). When the Routing HW table gets full, only routes with longer subnet prefixes are offloaded (/30, /29, /28, etc.) while the CPU processes the shorter prefixes. Users can fine-tune what routes to offload via routing filters (for dynamic routes) or suppressing hardware offload per switch port, static route or VLAN. IPv4 and IPv6 routing tables share the same hardware memory.  
<sup>2</sup> When the HW limit of Fasttrack or NAT entries is reached, other connections will fall back to the CPU. MikroTik's smart connection offload algorithm ensures that the connections with the most traffic are offloaded to the hardware.  
<sup>3</sup> Fasttrack connections share the same HW memory with ACL rules. Depending on the complexity, one ACL rule may occupy the memory of 3-6 Fasttrack connections.  
<sup>4</sup> If a Fasttrack connection requires Network Address Translation, a hardware NAT entry is created. The hardware supports both SRCNAT and DSTNAT.  
<sup>5</sup> DX4000/DX8000 switch chips store directly connected hosts, IPv4 /32, and IPv6 /128 route entries in the FDB table rather than the routing table. The HW memory is shared between regular FDB L2 entries (MAC), IPv4, and IPv6 addresses. The number of hosts is also limited by max-neighbor-entries in [IP Settings](../cli-reference/ip/settings.md) / [IPv6 Settings](../cli-reference/ipv6/settings.md).  
<sup>6</sup> The switch chip has a feature set of the DX8000 series.

#### Partial offloading

The **98DX8xxx**, **98DX4xxx** have entirely different routing tables. Instead of prefixes, we have to offload route indexes. The entire IPv4 address range (same for IPv6) must be indexed, i.e., 0.0.0.0 - 255.255.255.255. Adding new route entries causes an index rebuild, increasing hardware memory by 0-5 entries depending on the complexity of the routing table. That's why no exact numbers are given. For example, some routing tables containing 240K entries can be fully offloaded to CRS317 HW, while others with 160K entries barely fit. And you will never know until you try.

When indexing the entire IP address range (0.0.0.0 - 255.255.255.255), you can offload as many routes as needed, as long as you also have a default route (0.0.0.0/0) using the same next-hop.

For example, on a CCR2216 router around 950k routes with a /30 prefix are created, all using the same next-hop along with a default route. As a result, all routes were offloaded, while the lpm-usage remained minimal.

```routeros
[admin@MikroTik] > /interface/ethernet/switch/l3hw-settings/advanced/monitor 
        ipv4-routes-total: 942338
           ipv4-routes-hw: 942326
          ipv4-routes-cpu:     11
  ipv4-shortest-hw-prefix:      0
               ipv4-hosts:      1
         route-queue-size:      0
         route-queue-rate:      0
       route-process-rate:      0
              nexthop-cap:   8192
            nexthop-usage:     85
    vxlan-mtu-packet-drop:      0
     fasttrack-ipv4-conns:      0
     fasttrack-queue-size:      0
     fasttrack-queue-rate:      0
   fasttrack-process-rate:      0
   fasttrack-hw-min-speed:      0
   fasttrack-hw-offloaded:      0
    fasttrack-hw-unloaded:      0
                  lpm-cap:  27200
                lpm-usage:     11
             lpm-bank-cap:   1360
           lpm-bank-usage:      1
                                0
                                0
                                0
                                1
                                0
                                0
                                0
                                4
                                0
                                0
                                0
                                5
                                0
                                0
                                0
                                0
                                0
                                0
                                0
                  pbr-cap:   8192
                pbr-usage:      0
             pbr-lpm-bank:      2
                nat-usage:      0
```

However, if there are "gaps" in the address range, such as not using a default route or having multiple next-hops, this consumes HW table. When the routing HW table gets full, only routes with longer subnet prefixes are offloaded (/30, /29, /28, etc.) while the CPU processes the shorter prefixes. Here is what happens when the default route gets disabled or different next-hops are used: only 37k routes with a /30 prefix fit in the HW table. This is the worst-case scenario for the CCR2216.

```routeros
[admin@MikroTik] > /interface/ethernet/switch/l3hw-settings/advanced/monitor 
        ipv4-routes-total: 942337
           ipv4-routes-hw:  37729
          ipv4-routes-cpu: 904608
  ipv4-shortest-hw-prefix:     30
               ipv4-hosts:      1
         route-queue-size:      0
         route-queue-rate:      0
       route-process-rate:      0
              nexthop-cap:   8192
            nexthop-usage:     85
    vxlan-mtu-packet-drop:      0
     fasttrack-ipv4-conns:      0
     fasttrack-queue-size:      0
     fasttrack-queue-rate:      0
   fasttrack-process-rate:      0
   fasttrack-hw-min-speed:      0
   fasttrack-hw-offloaded:      0
    fasttrack-hw-unloaded:      0
                  lpm-cap:  27200
                lpm-usage:  22392
             lpm-bank-cap:   1360
           lpm-bank-usage:   1022
                             1033
                             1027
                             1028
                             1221
                             1033
                             1040
                              678
                             1358
                             1245
                             1254
                             1242
                             1246
                             1249
                             1273
                             1260
                             1101
                             1024
                             1031
                             1027
                  pbr-cap:   8192
                pbr-usage:      0
             pbr-lpm-bank:      2
                nat-usage:      0
```

In many cases, the default behavior "offloading only routes with longer subnet prefixes" is not optimal, especially if the ratio of CPU-handled routes to HW-offloaded routes is too high. When this happens, the chances of a packet being hardware-forwarded drop significantly.

If HW memory is insufficient and partial offloading occurs, a better approach for you as a network administrator would be to offload only the routes that carry the most traffic while keeping less demanding routes on the CPU, and not letting the partial offloading happen.

Fortunately, there are several ways to manage this. There is per-switch-port and static route suppression, and [filtering dynamic routes using a wide range of attributes](../user-guides/routing-and-networking-protocols/route-selection-and-filtering.md). One example is to use as-path to filter most demanding prefixes (Google, Meta), while all other routes get L3HW suppressed.

### CRS8xx: Switch 98DX7xxx Series

The devices below are based on **Marvell 98DX7xxx** switch chip models.

:::danger
The software support for the following features is still in development and not available yet:

- FastTrack and NAT connection offloading
- VXLAN offloading

:::

<WideTable>

| Switch Chip | Models | IPv4 Routes <sup>1</sup> | IPv4 Hosts <sup>2</sup> | IPv6 Routes <sup>1</sup> | IPv6 Hosts <sup>2</sup> | Nexthops | IPv4 Fasttrack connections | IPv4 NAT entries | VXLAN offloading | Per-VLAN packet/byte counters |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **98DX7335** | CRS812-8DS-2DQ-2DDQ-RM | up to 240K | up to 64K | up to 40K | up to 48K | 16K | to be announced | to be announced | to be announced | + |
| **98DX7335** | CRS804-4DDQ-hRM | up to 240K | up to 64K | up to 40K | up to 48K | 16K | to be announced | to be announced | to be announced | + |

</WideTable>

---

<sup>1</sup> Depends on the complexity of the routing table. Whole-byte IP prefixes (/8, /16, /24, etc.) occupy less HW space than others (e.g., /22). When the Routing HW table gets full, only routes with longer subnet prefixes are offloaded (/30, /29, /28, etc.) while the CPU processes the shorter prefixes. Users can fine-tune what routes to offload via routing filters (for dynamic routes) or suppressing hardware offload of static routes. IPv4 and IPv6 routing tables share the same hardware memory.  
<sup>2</sup> 98DX7xxx switch chips store directly connected hosts, IPv4 /32 route entries, and IPv6 /128 route entries in the FDB table rather than the routing table. The HW memory is shared between regular FDB L2 entries (MAC), IPv4 addresses, and IPv6 addresses. The number of hosts is also limited by max-neighbor-entries in [IP Settings](../cli-reference/ip/settings.md) / [IPv6 Settings](../cli-reference/ipv6/settings.md).
