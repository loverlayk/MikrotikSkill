# MACVLAN

> MACVLAN allows creating multiple virtual network interfaces with unique MAC addresses on a physical interface, enabling efficient IP address management and distinct PPPoE connections. It operates at the MAC level...

# MACVLAN

The MACVLAN provides a means to create multiple virtual network interfaces, each with its own unique Media Access Control (MAC) address, attached to a physical network interface. This technology is utilized to address specific network requirements, such as obtaining multiple IP addresses or establishing distinct PPPoE client connections from a single physical Ethernet interface while using different MAC addresses. Unlike traditional [VLAN](./vlan.md) (Virtual LAN) interfaces, which rely on Ethernet frames tagged with VLAN identifiers, MACVLAN operates at the MAC address level, making it a versatile and efficient solution for specific networking scenarios.

:::info
A MACVLAN interface can only receive broadcast packets, packets addressed to its own MAC address, and a limited number of multicast addresses. If the physical interface has a VLAN configured, the MACVLAN interface cannot receive packets from that VLAN.

For bridging and more complex Layer2 solutions involving VLANs, a dedicated switch should be used instead.
:::

## Basic Configuration Example

Picture a scenario where the ether1 interface connects to your ISP, and your router needs to lease two IP addresses, each with a distinct MAC address. Traditionally, this would require the use of two physical Ethernet interfaces and an additional switch. However, a more efficient solution is to create a virtual MACVLAN interface.

To create a MACVLAN interface, select the needed Ethernet interface. A MAC address will be automatically assigned if not manually specified:

```ros
/interface/macvlan
add interface=ether1 name=macvlan1

/interface/macvlan/print
Flags: R - RUNNING
Columns: NAME, MTU, INTERFACE, MAC-ADDRESS, MODE
#   NAME       MTU  INTERFACE  MAC-ADDRESS        MODE  
0 R macvlan1  1500  ether1     76:81:BF:68:69:83  bridge
```

Now, a DHCP client can be created on the ether1 and macvlan1 interfaces:

```ros
/ip/dhcp-client
add interface=ether1
add interface=macvlan1
```

## Property Reference

**Sub-menu:** `/interface/macvlan`

Configuration settings for the MACVLAN interface.

| Property | Description |
| :-- | :-- |
| **arp** (*disabled \| enabled \| local-proxy-arp \| proxy-arp \| reply-only*; Default: **enabled**) | Address Resolution Protocol setting<code>disabled</code> - the interface will not use ARP<code>enabled</code> - the interface will use ARP<code>local-proxy-arp</code> -  the router performs proxy ARP on the interface and sends replies to the same interface<code>proxy-arp</code> - the router performs proxy ARP on the interface and sends replies to other interfaces<code>reply-only</code> - the interface will only reply to requests originating from matching IP address/MAC address combinations, which are entered as static entries in the IP/ARP table. No dynamic entries will be automatically stored in the IP/ARP table. Therefore, for communications to be successful, a valid static entry must already exist. |
| **arp-timeout** (*auto \| integer*; Default: **auto**) | Sets how long the ARP record is kept in the ARP table after no packets are received from IP. Value `auto` equals the value of `arp-timeout` in `/ip/settings/`, default is 30s. |
| **comment** (*string*; Default: ) | Short description of the interface. |
| **disabled** (*yes \| no*; Default: **no**) | Changes whether the interface is disabled. |
| **interface** (*name*; Default: ) | The name of the underlying interface on which the MACVLAN will operate. MACVLAN interfaces can be created on any interface that has a MAC address. **Warning:** Adding a VLAN interface on top of a MACVLAN interface is not supported.Adding MACVLAN on an interface which is already bridged or bonded is not supported. |
| **loop-protect** (*on \| off \| default*; Default: **default**) | Enables or disables loop protect on the interface, the **default** works as turned off. |
| **loop-protect-disable-time** (*time interval \| 0*; Default: **5m**) | Sets how long the selected interface is disabled when a loop is detected. **0** - forever. |
| **loop-protect-send-interval** (*time interval*; Default: **5s**) | Sets how often loop protect packets are sent on the selected interface. |
| **mac-address** (*MAC*; Default: ) | Static MAC address of the interface. A randomly generated MAC address will be assigned when not specified. |
| **mode** (*private \| bridge*; Default: **bridge**) | Sets MACVLAN interface mode: <code>private</code> - does not allow communication between MACVLAN instances on the same parent interface.<code>bridge</code> - allows communication between MACVLAN instances on the same parent interface. |
| **mtu** (*integer*; Default: **1500**) | Sets Layer 3 Maximum Transmission Unit. For the MACVLAN interface, it cannot be higher than the parent **interface**. |
| **name** (*string*; Default: ) | Interface name. |
