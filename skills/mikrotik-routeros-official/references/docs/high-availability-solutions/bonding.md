# Bonding

> Bonding in RouterOS: join several Ethernet-like interfaces into one link for more capacity and failover, monitor the links with MII or ARP, choose a mode (LACP, balance-xor, balance-rr, active-backup and others) and...

# Bonding

Bonding joins several Ethernet-like interfaces into one virtual interface. The traffic is spread over the links, and when a link fails the others carry it.

:::warning
A bonding interface does not have a larger link speed. It balances traffic over its links, so one connection is not faster than one link in most modes. See [LAG interfaces and load balancing](../bridging-and-switching/user-guides/layer2-misconfiguration).
:::

## Join two links between two routers

The interfaces of a bond must not have IP addresses of their own. Add a bonding interface with the two interfaces as `slaves`, and an address on it. On Router1:

```ros
/interface/bonding/add name=bond1 slaves=ether1,ether2
/ip/address/add address=172.16.0.1/24 interface=bond1
```

On Router2:

```ros
/interface/bonding/add name=bond1 slaves=ether1,ether2
/ip/address/add address=172.16.0.2/24 interface=bond1
```

The bond needs a few seconds before it passes traffic. Then test it with `/ping 172.16.0.2` on Router1. `/interface/bonding/monitor bond1` shows the mode and the links in `active-ports` and `inactive-ports`.

Without `mode`, the bond uses `balance-rr`. To connect to a switch with LACP, use `mode=802.3ad`.

## Monitor the links

The bond must know when a link fails, or it keeps sending packets to the failed link and they are lost. There are two checks, and a bond uses one of them (`link-monitoring=none` turns both off).

### MII monitoring

`link-monitoring=mii` is the default. It looks at the state of the local interface: when the interface has no link, the bond stops using it (`mii-interval`, 100 ms by default).

If the driver of an interface does not report the link state, the link always looks up. A failure that MII monitoring sees is found almost at once, sooner than with ARP monitoring.

MII monitoring cannot see whether the link really passes traffic. If the link stays up while the path is broken, for example through a media converter, a switch or a tunnel, MII monitoring does not notice the failure.

### ARP monitoring

`link-monitoring=arp` sends ARP requests to one or more addresses through each link, and uses the answers as the sign that the link works. It sees failures that MII monitoring does not. On Router1:

```ros
/interface/bonding/set [find name=bond1] link-monitoring=arp \
    arp-ip-targets=172.16.0.2
```

On Router2:

```ros
/interface/bonding/set [find name=bond1] link-monitoring=arp \
    arp-ip-targets=172.16.0.1
```

When a link fails, a few packets can be lost until the check notices it. The failed link is then in `inactive-ports` of `/interface/bonding/monitor bond1`.

- `arp-interval` is 100 ms by default.
- Give several addresses in `arp-ip-targets` where you can. With one target, a failure of the target looks like a failure of all links.
- The answers are not checked: any packet that arrives on the interface marks it as active.
- With `balance-rr` or `balance-xor` through a switch, the switch must spread the packets evenly over the links. If all ARP answers arrive on one link, the other links look failed.
- ARP monitoring works without an IP address on the device.
- The ARP requests of the bond have no VLAN tag, also when the address of the target network is on a VLAN interface.

## Bonding modes

### 802.3ad

IEEE 802.3ad is the standard for link aggregation, also known as LACP (Link Aggregation Control Protocol). The two devices agree on the links of the group automatically, so the switch needs little configuration. The standard requires that frames arrive in order, so connections do not get packets out of order. All links of the group must have the same speed and duplex.

```ros
/interface/bonding/add name=bond1 slaves=ether1,ether2 mode=802.3ad
```

The device at the other end, usually a switch, must run LACP on the same links. Check the bond with `monitor`: when LACP works, all ports are in `active-ports` and `lacp-partner-system-id` shows the other device. If the other end does not run LACP, there is no `lacp-partner-system-id`, only one port is active, and the link can lose traffic.

- LACP balances the outgoing traffic over the active ports by a hash of the packet headers, and accepts incoming traffic on any active port. `transmit-hash-policy` selects the fields of the hash: the Ethernet addresses, the VLAN tag, and with the layer 3 policies the IP addresses.
- Do not use ARP monitoring with LACP: the other device can send all ARP answers through one port because of its own hash.
- `lacp-rate=1sec` makes the devices exchange LACP packets every second in place of every 30 seconds.
- The `layer-3-and-4` hash policy is not fully compatible with LACP: see the [Linux bonding documentation](https://www.kernel.org/doc/Documentation/networking/bonding.txt).

### balance-xor

This mode balances the outgoing traffic over the active ports by a hash of the packet headers and accepts incoming traffic on any active port. It is like LACP without the protocol. Use it with a static link aggregation group (LAG) on the switch.

### balance-rr

Packets are sent in turn through each link, from the first to the last. This is the only mode that sends the packets of one connection through several links. With several links on both sides, packets often arrive out of order, and TCP then sends segments again. For other protocols such as UDP this is not a problem if the application accepts packets out of order. This mode can join several wireless links, but the links need equal bandwidth: with one slower link, the bond has the bandwidth of the slowest link on each of its links. If a switch connects the links, its ports need a matching configuration, and many switches do not support this mode.

### active-backup

Only one link sends and receives. Another link takes over when the active one fails. `primary` selects the link to use when it works:

```ros
/interface/bonding/add name=bond1 slaves=ether1,ether2 \
    mode=active-backup primary=ether1
```

The MAC address of the bond is seen on the active port only, so switches are not confused. This mode is the best choice for high availability with several switches that are connected to each other.

:::warning
ARP monitoring does not work correctly in this mode when the two routers are connected directly. Use MII monitoring, or put a switch between the routers.
:::

### broadcast

All links send the same data. This gives fault tolerance but no balancing.

### balance-tlb

This mode balances the outgoing traffic for each peer. The links can have different speeds and duplex settings, and the switch needs no configuration. Only MII monitoring works in this mode (ARP monitoring is ignored), and incoming traffic is not balanced: it uses the `primary` link.

In this example `ether1` can carry 10 Mbps and `ether2` 5 Mbps. The first link has more capacity, so it is the primary one:

```ros
/interface/bonding/add mode=balance-tlb slaves=ether1,ether2 \
    primary=ether1
```

![A router connected to a switch with two links, with balance-tlb: outgoing traffic uses both links, incoming traffic uses the primary link](./img/bonding-01.webp)

The router can send to the clients behind the switch with the capacity of both links together (15 Mbps). The clients can send to the router with the capacity of the primary link (10 Mbps).

### balance-alb

This mode is like `balance-tlb`, and it also balances incoming IPv4 traffic. It does this with ARP: the bond changes the source MAC address in the ARP messages that the router sends, so that different peers use the MAC addresses of different links. Only MII monitoring works (ARP monitoring is ignored). The drivers of the interfaces must be able to change the MAC address, and the mode does not work together with `local-proxy-arp`.

![A router connected to a switch with two links, with balance-alb: outgoing and incoming traffic use both links](./img/bonding-02.webp)

## Check the state of a bond

`monitor` shows the active and inactive ports of each bond. For `802.3ad` it also shows the LACP system IDs:

```text
/interface/bonding/monitor [find] 
                      mode: 802.3ad           active-backup
              active-ports: ether4            ether6
                            ether5            
            inactive-ports:                   ether7
            lacp-system-id: CC:2D:E0:11:22:33 
      lacp-system-priority: 65535             
    lacp-partner-system-id: B8:69:F4:44:55:66
```

`monitor-slaves` shows the LACP state of each port of a bond:

```text
/interface/bonding/monitor-slaves bond1
Flags: A - active, P - partner 
 AP port=ether4 key=17 flags="A-GSCD--" partner-sys-id=D4:CA:6D:12:06:65 partner-sys-priority=65535 partner-key=9 partner-flags="A-GSCD--" 

 AP port=ether5 key=17 flags="A-GSCD--" partner-sys-id=D4:CA:6D:12:06:65 partner-sys-priority=65535 partner-key=9 partner-flags="A-GSCD--" 
```

## Hardware offloading

MikroTik devices with a Marvell Prestera switch chip and with the 88E6393X, 88E6191X and 88E6190 switch chips support bridge hardware offloading with bonding interfaces.

- Only the modes `802.3ad`, `balance-xor` and `active-backup` are hardware offloaded. The other modes use the CPU.
- Devices with a Marvell Prestera switch chip always use the layer 2, 3 and 4 fields for the transmit hash. The 88E6393X, 88E6191X and 88E6190 chips use layer 2 only. A change of `transmit-hash-policy` has no effect while hardware offloading is used.

See [Marvell Prestera switch chip features](../bridging-and-switching/marvell-prestera-switch-chip-features), which also has an example of VLANs with bonds.

## Read more

- [`/interface/bonding`](../cli-reference/interface/bonding/)
- [Bonding Examples](user-guides/bonding-examples)
- [Multi-chassis Link Aggregation Group](multi-chassis-link-aggregation-group)
- [Layer 2 misconfiguration](../bridging-and-switching/user-guides/layer2-misconfiguration)
