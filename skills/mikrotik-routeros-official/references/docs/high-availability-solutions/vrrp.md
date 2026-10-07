# VRRP

> This page describes the Virtual Router Redundancy Protocol (VRRP) in MikroTik RouterOS, explaining how it provides router redundancy through IPv4/IPv6 multicast communication and prioritized election among routers....

# VRRP

## Summary

This chapter describes the Virtual Router Redundancy Protocol (VRRP) support in RouterOS.

Mostly on larger LANs, dynamic routing protocols (OSPF or RIP) are used; however, there are a number of factors that may make it undesirable to use dynamic routing protocols. One alternative is to use static routing, but if the statically configured first hop fails, then the host will not be able to communicate with other hosts.

In IPv6 networks, hosts learn about routers by receiving Router Advertisements used by the Neighbor Discovery (ND) protocol. ND already has a built-in mechanism to determine unreachable routers. However, it can take up to 38 seconds to detect an unreachable router. It is possible to change parameters and make detection faster, but it will increase the overhead of ND traffic especially if there are a lot of hosts. VRRP allows the detection of unreachable routers within 3 seconds without additional traffic overhead.

Virtual Router Redundancy Protocol (VRRP) provides a solution by combining a number of routers into a logical group called *Virtual Router* (VR). VRRP implementation in RouterOS is based on VRRPv2 RFC 3768 and VRRPv3 RFC 5798.

It is recommended to use the same version of RouterOS for all devices with the same VRID used to implement VRRP.

:::warning
According to the RFC authentication is deprecated for VRRP v3.

:::

## Protocol Overview

![](./img/vrrp-01.webp)

The purpose of VRRP is to communicate with all VRRP routers associated with the Virtual Router ID and support router redundancy through a prioritized election process among them.

All messaging is done by IPv4 or IPv6 multicast packets using protocol 112 (VRRP). The destination address of an IPv4 packet is *224.0.0.18* and for IPv6 it is *FF02:0:0:0:0:0:0:12*. The source address of the packet is always the primary IP address of an interface from which the packet is being sent. In IPv6 networks, the source address is the link-local address of an interface.

These packets are always sent with TTL=255 and are not forwarded by the router. If for any reason the router receives a packet with a lower TTL, the packet is discarded.

Each VR node has a single assigned MAC address. This MAC address is used as a source for all periodic messages sent by Master.

Virtual Router is defined by VRID and a mapped set of IPv4 or IPv6 addresses. The master router is said to be the **owner** of the mapped IPv4/IPv6 addresses. There are no limits to using the same VRID for IPv4 and IPv6; however, these will be two different Virtual Routers.

Only the Master router is sending periodic Advertisement messages to minimize the traffic. A backup will try to preempt the Master only if it has the higher priority and preemption is not prohibited.

:::tip
All VRRP routers belonging to the same VR must be configured with the same advertisement interval. If the interval does not match, the router will discard the received advertisement packet.

:::

## Virtual Router (VR)

A Virtual Router (VR) consists of one Owner router and one or more backup routers belonging to the same network.

VR includes:

- VRID is configured on each VRRP router.
- The same virtual IP is configured on each router.
- Owner and Backup are configured on each router. On a given VR there can be only one Owner.

### Virtual MAC address

VRRP automatically assigns a MAC address to the VRRP interface based on the standard MAC prefix for VRRP packets and the VRID number. The first five octets are 00:00:5E:00:01 and the last octet is the configured VRID. For example, if Virtual Router's VRID is 49, then the virtual MAC address will be *00:00:5E:00:01:31*.

:::warning
Virtual MAC addresses cannot be manually set or edited.

:::

### Owner

An Owner router for a VR is the default Master router and operates as the Owner for all subnets included in the VR. Priority on an owner router must be the highest value (255) and the virtual IP is the same as the real IP (owns the virtual IP address).

:::warning
RouterOS cannot be configured as Owner. The Pure virtual IP configuration is the only valid configuration unless a non-RouterOS device is set as the owner.

:::

### Master

A master router in a VR operates as the physical gateway for the network for which it is configured. The selection of the Master is controlled by priority value. The Master state describes the behavior of the Master router. In the example network, **R1** is the Master router. When R1 is no longer available R2 becomes master.

### Backup

VR must contain at least one Backup router. A backup router must be configured with the same virtual IP as the Master for that VR. The default priority for Backup routers is 100. When the current master router is no longer available, a backup router with the highest priority will become a current master. Every time a router with higher priority becomes available it is switched to master. Sometimes this behavior is not necessary. To override it preemption mode should be disabled.

### Virtual Address

![](./img/vrrp-02.webp)

The Virtual IP associated with VR must be identical and set on all VR nodes. All virtual and real addresses should be from the same network.

:::warning
RouterOS can not be configured as Owner. VRRP address and real IP address should not be the same.

:::

If the Master of VR is associated with multiple IP addresses, then Backup routers belonging to the same VR must also be associated with the same set of virtual IP addresses. If the virtual address on the Master is not also on Backup, a misconfiguration exists and VRRP advertisement packets will be discarded.

All Virtual Router members can be configured so that the virtual IP is not the same as the physical IP. Such a virtual address can be called a floating or pure virtual IP address. The advantage of this setup is the flexibility given to the administrator. Since the virtual IP address is not the real address of any one of the participating routers, the administrator can change these physical routers or their addresses without any need to reconfigure the virtual router itself.

In IPv6 networks, the first address is always a link-local address associated with VR. If multiple IPv6 addresses are configured, then they are added to the advertisement packet after the link-local address.

### IPv4 ARP

The Master for a given VR responds to ARP requests with the VR's assigned MAC address. The virtual MAC address is also used as the source MAC address for advertisement packets sent by the Master. To ARP requests for non-virtual IP addresses, the router responds with the system MAC address. Backup routers are not responding to ARP requests for Virtual IPs.

### IPv6 ND

As you may know, in IPv6 networks, the Neighbor Discovery protocol is used instead of ARP. When a router becomes the Master, an unsolicited ND Neighbor Advertisement with the Router Flag is sent for each IPv6 address associated with the virtual router.

## VRRP state machine

![](./img/vrrp-03.webp)

As you can see from the diagram, each VRRP node can be in one of three states:

- Init state
- Backup state
- Master state

### Init state

The purpose of this state is to wait for a Startup event. When this event is received, the following actions are taken:

- If priority is 255:
- \* For IPv4 send advertisement packet and broadcast ARP requests.
- \* For IPv6 send an unsolicited ND Neighbor Advertisement for each IPv6 address associated with the virtual router and set target address to link-local address associated with VR.
- \* Transition to MASTER state.
- Else transition to BACKUP state.

### Backup state

When in the backup state:

- In IPv4 networks, a node is not responding to ARP requests and is not forwarding traffic for the IP associated with the VR.
- In IPv6 networks, a node is not responding to ND Neighbor Solicitation messages and is not sending ND Router Advertisement messages for VR-associated IPv6 addresses.

Routers' main task is to receive advertisement packets and check if the master node is available.

The backup router will transition itself to the master state in two cases:

- If the priority in the advertisement packet is 0.
- When Preemption\_Mode is set to yes and Priority in the ADVERTISEMENT is lower than the local Priority.

After the transition to Master state, the node is:

- In IPv4 broadcasts a gratuitous ARP request.
- In IPv6 sends an unsolicited ND Neighbor Advertisement for every associated IPv6 address.

In other cases, advertisement packets will be discarded. When the shutdown event is received, transition to Init state.

:::warning
Preemption mode is ignored if the Owner router becomes available.

:::

### Master state

When the MASTER state is set, the node functions as a forwarding router for IPv4/IPv6 addresses associated with the VR.

In IPv4 networks, the Master node responds to ARP requests for the IPv4 address associated with the VR. In IPv6 networks, the Master node:

- Responds to the ND Neighbor Solicitation message for the associated IPv6 address.
- Sends ND Router Advertisements for the associated IPv6 addresses.

If the advertisement packet is received by the master node:

- If priority is 0, send advertisement immediately.
- If priority in advertisement packet is greater than node's priority then transition to the backup state.
- If priority in advertisement packet is equal to node's priority and primary IP Address of the sender is greater than the local primary IP Address, then transition to the backup state.
- Ignore advertisement in other cases.

When the shutdown event is received, send the advertisement packet with priority=0 and transition to Init state.

### Connection tracking synchronization

Similar to different High availability features, RouterOS v7 supports VRRP connection tracking synchronization.

The VRRP connection tracking synchronization requires that RouterOS [connection tracking](../firewall-and-quality-of-service/connection-tracking.md) is running. By default, connection tracking is working in `auto` mode. If VRRP devices do not contain any firewall rules, you need to manually enable connection tracking:

```ros
/ip/firewall/connection/tracking/set enabled=yes
```

To sync connection tracking entries configure the device as follows:

```ros
/interface/vrrp/set vrrp1 sync-connection-tracking=yes
```

Verify configuration in the logging section:

```ros
16:14:06 vrrp,info vrrp1 now MASTER, master down timer
16:14:06 vrrp,info vrrp1 stop CONNTRACK
16:14:06 vrrp,info vrrp1 starting CONNTRACK MASTER
```

Connection tracking entries are synchronized only from the Master to the Backup device.

When both `sync-connection-tracking` and `preemption-mode` are enabled, and a router with higher VRRP priority becomes online, the connections get synchronized first, and only then the router with higher priority becomes the VRRP master.

:::tip
If multiple VRRP interfaces are configured between two units and `sync-connection-tracking=yes` is required, it must be enabled only on one of the VRRP interfaces, preferably the one designated as the `group-authority`.

:::

Example `connection-tracking-mode` configuration:
```
R1
/interface/vrrp
add connection-tracking-mode=active-active connection-tracking-port=8275 interface=ether1 name=vrrp30 priority=100 sync-connection-tracking=yes vrid=1
add connection-tracking-mode=active-active connection-tracking-port=8276 interface=ether1 name=vrrp40 priority=100 sync-connection-tracking=yes vrid=2

R2
/interface/vrrp
add connection-tracking-mode=active-active connection-tracking-port=8275 interface=ether1 name=vrrp30 priority=55 sync-connection-tracking=yes vrid=1
add connection-tracking-mode=active-active connection-tracking-port=8276 interface=ether1 name=vrrp40 priority=155 sync-connection-tracking=yes vrid=2
```

`group-authority` configuration example:

VRRP instances run on LAN and WAN networks with NAT between them. If one VRRP instance is Master and the other is Backup on the same device, the entire network malfunctions due to NAT failure. Grouping LAN and WAN VRRP interfaces ensures that both are either VRRP Master or Backup. In a VRRP group, VRRP advertisements are sent only by the group authority. In a typical WAN+LAN setup, you should use the LAN network as the group authority to keep VRRP control traffic in the internal network.
```
/interface/vrrp
add name=vrrp-wan interface=sfp-sfpplus1 vrid=1 priority=100
add name=vrrp-lan interface=bridge1 vrid=2 priority=100
set [find] group-authority=vrrp-lan
```

## Configuring VRRP

### IPv4

Setting up a Virtual Router is quite easy, only two actions are required - create a VRRP interface and set Virtual Router's IP address.

For example, add VRRP to ether1 and set VR's address to 192.168.1.1

```ros
/interface/vrrp/add name=vrrp1 interface=ether1
/ip/address/add address=192.168.1.2/24 interface=ether1
/ip/address/add address=192.168.1.1/32 interface=vrrp1
```

Notice that only the 'interface' parameter was specified when adding VRRP. It is the only parameter required to be set manually. Other parameters, if not specified, will be set to their defaults: `vrid=1, priority=100` and `authentication=none`.

:::warning
The address on the VRRP interface must have a /32 netmask if the address configured on VRRP is from the same subnet as on any other interface of the router.

:::

Before VRRP can operate correctly, a correct IP address is required on ether1. In this example, it is 192.168.1.2/24.

### IPv6

To make VRRP work in IPv6 networks, several additional options must be enabled - v3 support is required and the protocol type should be set to IPv6:

```ros
/interface/vrrp/add name=vrrp1 interface=ether1 version=3 v3-protocol=ipv6
```

Now when the VRRP interface is set, we can add a global address and enable ND advertisement:

```ros
/ipv6/address/add address=FEC0:0:0:FFFF::1/64 advertise=yes interface=vrrp1
```

No additional address configuration is required as it is in the IPv4 case. IPv6 uses link-local addresses to communicate between nodes.
