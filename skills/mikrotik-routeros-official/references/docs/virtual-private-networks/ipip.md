# IPIP

> IPIP (IP-in-IP) is a tunneling protocol in RouterOS for secure point-to-point connections over IP networks, supporting IPv4 encapsulation and interoperability with other platforms. It offers basic configuration...

# IPIP

IPIP (IP-in-IP) is a simple tunneling protocol defined in RFC 2003 that encapsulates IP packets within another IP header to transport traffic between two endpoints. In RouterOS, IPIP can be used to create point-to-point tunnels between routers across intermediate IP networks.

An IPIP tunnel interface is represented as a virtual interface in the interface list and can be configured similarly to other logical interfaces. The protocol is supported by various networking platforms, including RouterOS, Linux, and Cisco devices, enabling interoperability between different vendors.

IPIP is commonly used to connect remote networks over public or private IP infrastructure without requiring direct Layer 2 connectivity. The protocol supports encapsulation of IPv4 traffic and is often used as a lightweight tunneling mechanism where encryption is not required.

Typical use cases for IPIP include tunneling private networks over the internet, establishing routed links between remote sites, and providing an alternative to source routing in network designs. Because IPIP does not provide encryption, authentication, or traffic integrity protection, it is commonly combined with IPsec when secure transport is required.

IPIP is configured in [`/interface/ipip`](../cli-reference/interface/ipip.md) and [`/interface/ipipv6`](../cli-reference/interface/ipipv6.md) menus.

## Example

This example adds an IPIP tunnel between routers R1 and R2:

![](./img/ipip-01.webp)

First, configure IPIP interfaces and add IP addresses to them.
  
The configuration for router **R1** is as follows:

```ros
[admin@MikroTik] /interface/ipip> add
local-address: 10.0.0.1
remote-address: 22.63.11.6
[admin@MikroTik] /interface/ipip> print
Flags: X - disabled, R - running
# NAME MTU LOCAL-ADDRESS REMOTE-ADDRESS
0 X ipip1 1480 10.0.0.1 22.63.11.6

[admin@MikroTik] /interface/ipip> en 0
[admin@MikroTik] /interface/ipip> /ip/address/add address=1.1.1.1/24 interface=ipip1
```

The configuration for router **R2**:

```ros
[admin@MikroTik] /interface/ipip> add local-address=22.63.11.6 remote-address=10.
0.0.1
[admin@MikroTik] /interface/ipip> print
Flags: X - disabled, R - running
# NAME MTU LOCAL-ADDRESS REMOTE-ADDRESS
0 X ipip1 1480 22.63.11.6 10.0.0.1

[admin@MikroTik] /interface/ipip> enable 0
[admin@MikroTik] /interface/ipip> /ip/address/add address=1.1.1.2/24 interface=ipip1
```

Now both routers can ping each other:

```ros
[admin@MikroTik] /interface/ipip> /ping 1.1.1.2
1.1.1.2 64 byte ping: ttl=64 time=24 ms
1.1.1.2 64 byte ping: ttl=64 time=19 ms
1.1.1.2 64 byte ping: ttl=64 time=20 ms
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 19/21.0/24 ms
[admin@MikroTik] /interface/ipip>
```
