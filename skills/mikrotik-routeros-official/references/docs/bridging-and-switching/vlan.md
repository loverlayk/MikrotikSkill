# VLAN

> This page introduces VLAN functionality in MikroTik RouterOS, explaining how to create and manage Virtual LANs using IEEE 802.1Q standards for efficient network segmentation, with details on VLAN interfaces,...

# VLAN

**Sub-menu:** `/interface/vlan`

**Standards:** `IEEE 802.1Q, IEEE 802.1ad`

Virtual Local Area Network (VLAN) is a Layer 2 method that allows multiple Virtual LANs on a single physical interface (ethernet, wireless, etc.), giving the ability to segregate LANs efficiently.

You can use MikroTik RouterOS (as well as Cisco IOS, Linux, and other router systems) to mark these packets as well as to accept and route marked ones.

As VLAN works on OSI Layer 2, it can be used just like any other network interface without any restrictions. VLAN successfully passes through regular Ethernet bridges.

You can also transport VLANs over wireless links and put multiple VLAN interfaces on a single wireless interface. Note that as VLAN is not a full tunnel protocol (i.e., it does not have additional fields to transport MAC addresses of the sender and the recipient), the same limitation applies to bridging over VLAN as to bridging plain wireless interfaces. In other words, while wireless clients may participate in VLANs put on wireless interfaces, it is not possible to have a VLAN put on a wireless interface in station mode bridged with any other interface.

## 802.1Q

The most commonly used protocol for Virtual LANs (VLANs) is IEEE 802.1Q. It is a standardized encapsulation protocol that defines how to insert a four-byte VLAN identifier into the Ethernet header.

Each VLAN is treated as a separate subnet. It means that by default, a host in a specific VLAN cannot communicate with a host that is a member of another VLAN, although they are connected to the same switch. So if you want inter-VLAN communication, you need a router. RouterOS supports up to 4094 VLAN interfaces, each with a unique VLAN ID, per interface. VLAN priorities may also be used and manipulated.

When the VLAN extends over more than one switch, the inter-switch link has to become a 'trunk', where packets are tagged to indicate which VLAN they belong to. A trunk carries the traffic of multiple VLANs; it is like a point-to-point link that carries tagged packets between switches or between a switch and a router.

:::info
The IEEE 802.1Q standard has reserved VLAN IDs with special use cases; the following VLAN IDs should not be used in generic VLAN setups: 0, 1, 4095
:::

## Q-in-Q

Original 802.1Q allows only one VLAN header; Q-in-Q, on the other hand, allows two or more VLAN headers. In RouterOS, Q-in-Q can be configured by adding one VLAN interface over another. Example:

```ros
/interface/vlan
add name=vlan1 vlan-id=11 interface=ether1
add name=vlan2 vlan-id=12 interface=vlan1
```

If any packet is sent over the 'vlan2' interface, two VLAN tags will be added to the Ethernet header - '11' and '12'.

## Properties

**Sub-menu:** `/interface/vlan`

| Property | Description |
| :-- | :-- |
| **arp** (*disabled \| enabled \| local-proxy-arp \| proxy-arp \| reply-only*; Default: **enabled**) | Address Resolution Protocol setting<code>disabled</code> - the interface will not use ARP<code>enabled</code> - the interface will use ARP<code>local-proxy-arp</code> -  the router performs proxy ARP on the interface and sends replies to the same interface<code>proxy-arp</code> - the router performs proxy ARP on the interface and sends replies to other interfaces<code>reply-only</code> - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the IP/ARP table. No dynamic entries will be automatically stored in the IP/ARP table. Therefore for communications to be successful, a valid static entry must already exist. |
| **arp-timeout** (*auto \| integer*; Default: **auto**) | How long the ARP record is kept in the ARP table after no packets are received from IP. Value `auto` equals the value of `arp-timeout` in IP/Settings, default is 30s. |
| **disabled** (*yes \| no*; Default: **no**) | Changes whether the interface is disabled. |
| **interface** (*name*; Default: ) | Name of the interface on top of which VLAN will work. **Important:** Adding a VLAN interface to a [bridge with vlan-filtering](./#bridge-vlan-filtering) enabled will automatically tag the bridge interface as a member port. A dynamic entry with the comment "added by vlan on bridge" will appear under the `/interface/bridge/vlan` menu.  |
| **l3-hw-offloading** (*yes \| no*; Default: **yes**) | Enables or disables [L3HW](./l3-hardware-offloading.md) on a per-VLAN interface. This setting is only applicable to devices that support L3HW offloading and is available starting from RouterOS v7.21. More details - [Per-VLAN offloading](l3-hardware-offloading.md#per-vlan-offloading). |
| **mvrp** (*yes \| no*; Default: **no**) | Specifies whether this VLAN should declare its attributes through Multiple VLAN Registration Protocol (MVRP) as an applicant. Its main use case is for VLANs that are created on Ethernet interface (such as a "router on a stick" setup) that is connected to a bridge supporting [MVRP](index.md#mvrp). Enabling this option on a VLAN interface that is already part of an MVRP-enabled bridge has no effect, as the bridge manages MVRP in that case. This property only has an effect when `use-service-tag` is disabled. |
| **mtu** (*integer: 68..65535*; Default: **1500**) | Layer3 Maximum transmission unit |
| **name** (*string*; Default: ) | Interface name |
| **use-service-tag** (*yes \| no*; Default: ) | IEEE 802.1ad compatible Service Tag |
| **vlan-id** (*integer: 1..4094*; Default: **1**) | Virtual LAN identifier or tag that is used to distinguish VLANs. Must be equal for all computers that belong to the same VLAN. |

:::info
MTU should be set to 1500 bytes, the same as on Ethernet interfaces. But this may not work with some Ethernet cards that do not support receiving/transmitting full-size Ethernet packets with VLAN header added (1500 bytes data + 4 bytes VLAN header + 14 bytes Ethernet header). In this situation, MTU 1496 can be used, but note that this will cause packet fragmentation if larger packets have to be sent over the interface. At the same time, remember that MTU 1496 may cause problems if path MTU discovery is not working properly between source and destination.
:::

## Setup examples

---

### Video examples

[VLANs pt1](http://youtube.com/watch?v=US2EU6cgHQU), [VLANs pt2](http://youtube.com/watch?v=YMwOrc0LDP8), [VLANs pt3](http://youtube.com/watch?v=7a_z1jAdIME)

### Layer2 VLAN examples

There are multiple possible configurations that you can use, but each configuration type is designed for a special set of devices since some configuration methods will give you the benefits of the built-in switch chip and gain larger throughput. Check the [Basic VLAN switching](./user-guides/basic-vlan-switching.md) guide to see which configuration to use for each type of device to gain maximum possible throughput and compatibility. The guide shows how to set up a very basic VLAN trunk/access port configuration.

There are some other ways to set up VLAN tagging or VLAN switching, but the recommended way is to use [Bridge VLAN Filtering](index.md#bridge-vlan-filtering). Make sure you have not used any [known Layer2 misconfigurations](./user-guides/layer2-misconfiguration.md).

### Layer3 VLAN examples

#### Simple VLAN routing

Let us assume that we have several MikroTik routers connected to a hub. Remember that a hub is an OSI physical layer device (if there is a hub between routers, then from the L3 point of view it is the same as an Ethernet cable connection between them). For simplification, assume that all routers are connected to the hub using the ether1 interface and have been assigned IP addresses as illustrated in the figure below. Then on each of them the VLAN interface is created.

Configuration for R2 and R4 is shown below:

R2:

```ros
[admin@MikroTik] /interface/vlan> add name=VLAN2 vlan-id=2 interface=ether1 disabled=no

[admin@MikroTik] /interface/vlan> print 
Flags: X - disabled, R - running, S - slave 
 #    NAME                  MTU   ARP        VLAN-ID INTERFACE                
0 R  VLAN2                 1500  enabled    2       ether1
```

R4:

```ros
[admin@MikroTik] /interface/vlan> add name=VLAN2 vlan-id=2 interface=ether1 disabled=no

[admin@MikroTik] /interface/vlan> print 
Flags: X - disabled, R - running, S - slave 
 #    NAME                  MTU   ARP        VLAN-ID INTERFACE                
0 R  VLAN2                 1500  enabled    2       ether1
```

The next step is to assign IP addresses to the VLAN interfaces.

R2:

```ros
 [admin@MikroTik] /ip/address> add address=10.10.10.3/24 interface=VLAN2
 [admin@MikroTik] /ip/address> print
 Flags: X - disabled, I - invalid, D - dynamic
   #   ADDRESS            NETWORK         BROADCAST       INTERFACE
   0   10.0.1.4/24        10.0.1.0        10.0.1.255      ether1
   1   10.20.0.1/24       10.20.0.0       10.20.0.255     pc1
   2   10.10.10.3/24      10.10.10.0      10.10.10.255    vlan2

 [admin@MikroTik] /ip/address> 
```

R4:

```ros
 [admin@MikroTik] /ip/address> add address=10.10.10.5/24 interface=VLAN2
 [admin@MikroTik] /ip/address> print
 Flags: X - disabled, I - invalid, D - dynamic
   #   ADDRESS            NETWORK         BROADCAST       INTERFACE
   0   10.0.1.5/24        10.0.1.0        10.0.1.255      ether1
   1   10.30.0.1/24       10.30.0.0       10.30.0.255     pc2
   2   10.10.10.5/24      10.10.10.0      10.10.10.255    vlan2

[admin@MikroTik] /ip/address> 
```

At this point, it should be possible to ping router R4 from router R2 and vice versa:

```ros
 "Ping from R2 to R4:"

 [admin@MikroTik] /ip/address> /ping 10.10.10.5

 10.10.10.5 64 byte ping: ttl=255 time=4 ms

 10.10.10.5 64 byte ping: ttl=255 time=1 ms

 2 packets transmitted, 2 packets received, 0% packet loss

 round-trip min/avg/max = 1/2.5/4 ms

 "From R4 to R2:"
 
 [admin@MikroTik] /ip/address> /ping 10.10.10.3
 10.10.10.3 64 byte ping: ttl=255 time=6 ms
 10.10.10.3 64 byte ping: ttl=255 time=1 ms
 2 packets transmitted, 2 packets received, 0% packet loss
 round-trip min/avg/max = 1/3.5/6 ms 
```

To make sure the VLAN setup is working properly, try to ping R1 from R2. If pings are timing out then VLANs are successfully isolated.

```ros
 "From R2 to R1:"

 [admin@MikroTik] /ip/address> /ping 10.10.10.2
 10.10.10.2 ping timeout
 10.10.10.2 ping timeout
 3 packets transmitted, 0 packets received, 100% packet loss 
```

#### InterVLAN routing

If separate VLANs are implemented on a switch, then a router is required to provide communication between VLANs. A switch works at OSI layer 2, so it uses only the Ethernet header to forward and does not check the IP header. For this reason, we must use the router that is working as a gateway for each VLAN. Without a router, a host is unable to communicate outside of its own VLAN. The routing process between VLANs described above is called inter-VLAN communication.

To illustrate inter-VLAN communication, we will create a trunk that will carry traffic from three VLANs (VLAN2, VLAN3, and VLAN4) across a single link between a Mikrotik router and a manageable switch that supports VLAN trunking.

Each VLAN has its own separate subnet (broadcast domain) as we see in the figure above:

- VLAN 2 – 10.10.20.0/24.
- VLAN 3 – 10.10.30.0/24.
- VLAN 4 – 10.10.40.0/24.

VLAN configuration on most switches is straightforward. We need to define which ports are members of the VLANs and define a 'trunk' port that can carry tagged frames between the switch and the router.

Create VLAN interfaces:

```ros
/interface/vlan
add name=VLAN2 vlan-id=2 interface=ether1 disabled=no
add name=VLAN3 vlan-id=3 interface=ether1 disabled=no
add name=VLAN4 vlan-id=4 interface=ether1 disabled=no
```

Add IP addresses to VLANs:

```ros
/ip/address 
add address=10.10.20.1/24 interface=VLAN2
add address=10.10.30.1/24 interface=VLAN3
add address=10.10.40.1/24 interface=VLAN4
```

#### RouterOS /32 and IP unnumbered addresses

In RouterOS, to create a point-to-point tunnel with addresses you have to use the address with a network mask of '/32' that effectively brings you the same features as some vendors' unnumbered IP address.

There are 2 routers, RouterA and RouterB, where each is part of networks 10.22.0.0/24 and 10.23.0.0/24 respectively, and to connect these routers using VLANs as a carrier with the following configuration:

RouterA:

```ros
 /ip/address/add address=10.22.0.1/24 interface=ether1
 /interface/vlan/add interface=ether2 vlan-id=1 name=vlan1
 /ip/address/add address=10.22.0.1/32 interface=vlan1 network=10.23.0.1
 /ip/route/add gateway=10.23.0.1 dst-address=10.23.0.0/24 
```

RouterB:

```ros
 /ip/address/add address=10.23.0.1/24 interface=ether1
 /interface/vlan/add interface=ether2 vlan-id=1 name=vlan1
 /ip/address/add address=10.23.0.1/32 interface=vlan1 network=10.22.0.1
 /ip/route/add gateway=10.22.0.1 dst-address=10.22.0.0/24 
```
