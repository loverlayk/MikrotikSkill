# GRE

> Generic Routing Encapsulation (GRE) is a tunneling protocol for encapsulating various network protocols over IP, implemented as virtual interfaces in RouterOS with optional keepalive and properties like MTU, MSS...

# GRE

Generic Routing Encapsulation (GRE) is a tunneling protocol originally developed by Cisco to encapsulate a wide variety of network layer protocols over an IP network. It creates a virtual point-to-point link between tunnel endpoints, allowing different protocol traffic to be carried across routed infrastructure.

GRE operates as a stateless tunnel, similar in behavior to IPIP and EoIP. Because no session state is maintained between endpoints, traffic continues to be forwarded toward a remote endpoint even if it becomes unreachable. This can result in blackholed traffic until routing reconverges or the tunnel state changes.

In RouterOS, GRE interfaces are implemented as virtual interfaces and can be used in both routed and bridged network designs depending on the required topology.

To improve failure detection, RouterOS includes an optional keepalive mechanism for GRE tunnels. Keepalive monitors the reachability of the remote endpoint and can automatically disable the tunnel interface when the peer stops responding, reducing the risk of traffic being sent into an inactive tunnel.

:::tip
A GRE tunnel adds a 24-byte overhead (4-byte GRE header + 20-byte IP header). A GRE tunnel can forward only IP and IPv6 packets (EtherType 0x0800 and 0x86DD). Do not use the "Check gateway" option "arp" when a GRE tunnel is used as a route gateway.
:::

GRE is configured in [`/interface/gre`](../cli-reference/interface/gre.md) and [`/interface/gre6`](../cli-reference/interface/gre6.md) menus.

## Setup example

The goal of this example is to get Layer 3 connectivity between two remote sites over the internet.

![](./img/gre-01.webp)

The example uses two sites: **Site1** with a local network range 10.1.101.0/24 and **Site2** with a local network range 10.1.202.0/24.

The first step is to create GRE tunnels. A router on site 1:

```ros
/interface/gre/add name=myGre remote-address=192.168.90.1 local-address=192.168.80.1
```

A router on site 2:

```ros
/interface/gre/add name=myGre remote-address=192.168.80.1 local-address=192.168.90.1
```

:::warning
In this example, keepalive is not configured, so the tunnel interface has a **running** flag even if the remote tunnel end is not reachable.
:::

Now, set up tunnel addresses and proper routing. A router on site 1:

```ros
/ip/address/add address=172.16.1.1/30 interface=myGre
/ip/route/add dst-address=10.1.202.0/24 gateway=172.16.1.2
```

A router on site 2:

```ros
/ip/address/add address=172.16.1.2/30 interface=myGre
/ip/route/add dst-address=10.1.101.0/24 gateway=172.16.1.1
```

At this point, both sites have Layer 3 connectivity over the GRE tunnel.
