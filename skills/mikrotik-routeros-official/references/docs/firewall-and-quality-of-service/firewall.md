# Firewall

> MikroTik RouterOS firewall provides stateful and stateless packet filtering, NAT, and advanced traffic classification to secure network data flow and prevent unauthorized access. It includes filter/raw, mangle, and...

# Firewall

![Firewall fundamentals](img/firewall-01.webp)

The firewall implements stateful (by utilizing connection tracking) and stateless packet filtering and thereby provides security functions that are used to manage data flow to, from, and through the router. Along with the Network Address Translation (NAT), it serves as a tool for preventing unauthorized access to directly attached networks and the router itself as well as a filter for outgoing traffic.

Network firewalls keep outside threats away from sensitive data available inside the network. Whenever different networks are joined together, there is always a threat that someone from outside of your network will break into your LAN. Such break-ins may result in private data being stolen and distributed, valuable data being altered or destroyed, or entire hard drives being erased. Firewalls are used as a means of preventing or minimizing the security risks inherent in connecting to other networks. A properly configured firewall plays a key role in efficient and secure network infrastructure deployment.

MikroTik RouterOS has a very powerful firewall implementation with features including:

- Stateless packet inspection.
- Stateful packet inspection.
- Layer-7 protocol detection.
- Peer-to-peer protocols filtering.
- Traffic classification by:
  - Source MAC address.
  - IP addresses (network or list) and address types (broadcast, local, multicast, unicast).
  - Port or port range.
  - IP protocols.
  - Protocol options (ICMP type and code fields, TCP flags, IP options and MSS).
  - Interface the packet arrived from or left through.
  - Internal flow and connection marks.
  - DSCP byte.
  - Packet content.
  - Rate at which packets arrive and sequence numbers.
  - Packet size.
  - Packet arrival time.

and much more!

Firewall is split into three major modules:

- **filter/raw** - Used to deny traffic based on configured policies. Filtering in RAW tables allows saving resources if connection tracking is not required.
- **mangle** - Used to mark certain connections, packets, streams, set priorities and do other tasks.
- **nat** - Used to set up address translation rules, redirects and port forwarding.

## Chains

Firewall filtering rules are grouped together in chains. It allows a packet to be matched against one common criterion in one chain, and then passed over to another chain for processing against some other common criteria.

For example, a packet should be matched against the IP address:port pair. Of course, it could be achieved by adding as many rules with IP address:port match as required to the forward chain, but a better way could be to add one rule that matches traffic from a particular IP address. Then, rules that perform matching against separate ports can be added to the "**mychain**" chain without specifying the IP addresses.

```ros
/ip/firewall/filter 
add chain=mychain protocol=tcp dst-port=22 action=accept
add chain=mychain protocol=tcp dst-port=23 action=accept

add action=jump chain=input src-address=1.1.1.2/32 jump-target="mychain"
```

When processing a chain, rules are taken from the chain in the order they are listed, from top to bottom. If a packet matches the criteria of the rule, then the specified action is performed on it, and no more rules are processed in that chain (the exception is the **passthrough** action and some [Mangle](./mangle.md) actions).

If a packet has not matched any rule within the chain, then it is accepted.

Each firewall module has its own pre-defined chains:

- **raw**:
  - prerouting
  - output
- **filter**:
  - input
  - forward
  - output
- **mangle**:
  - prerouting
  - input
  - forward
  - output
  - postrouting
- **nat**:
  - srcnat
  - dstnat
  - input
  - output

More detailed packet processing in RouterOS is described in the [Packet Flow in the RouterOS](../packet-flow-in-routeros.md) diagram.
