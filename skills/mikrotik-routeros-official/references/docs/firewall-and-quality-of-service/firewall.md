# Firewall

> Overview of the RouterOS firewall: the filter, NAT, mangle and RAW tables, their predefined chains, how the rules of a chain are processed, and how to group rules in your own chains.

# Firewall

![A local network behind a router with a firewall: authorized access to and from the internet passes, unauthorized access from the internet is stopped](img/firewall-01.webp)

The firewall manages the data flow to the router, from the router and through the router. It filters packets with and without regard to their connection: [connection tracking](../connection-tracking) gives the firewall the state of each connection. Together with network address translation (NAT), it prevents unauthorized access to the networks behind the router and to the router itself, and it can filter outgoing traffic.

Whenever networks are joined, someone from outside can try to break into your network, to steal, change or destroy data. A firewall prevents or reduces the security risks of connecting to other networks.

The RouterOS firewall can classify traffic by:

- Source MAC address.
- IP addresses, as networks or address lists, and address types (broadcast, local, multicast, unicast).
- Port or port range.
- IP protocol.
- Protocol options: ICMP type and code, TCP flags, IP options and MSS.
- The interface that the packet arrived on or leaves through.
- Packet marks and connection marks.
- The DSCP field.
- Packet content, including Layer 7 protocol detection.
- The rate at which packets arrive, and their sequence.
- Packet size.
- The time when the packet arrives.

## Firewall tables

The firewall has four tables. Each is a menu in `/ip/firewall` for IPv4 and in `/ipv6/firewall` for IPv6:

- [Filter](./filter) accepts or drops packets according to your policies.
- [RAW](./raw) drops packets or excludes them from connection tracking before connection tracking processes them, which saves resources.
- [Mangle](./mangle) marks packets, connections and routing decisions, sets priorities and changes fields of the IP header.
- [NAT](./nat) translates addresses, redirects connections and forwards ports.

[Address lists](./address-lists) hold groups of addresses that the rules of all tables can match. [Common Firewall Matchers and Actions](./common-firewall-matchers-and-actions) describes what the tables have in common: the rule counters and the order of the matchers.

## Chains

The rules of each table are grouped in chains. Each table has predefined chains, which process the packets at fixed points of the [packet flow](../packet-flow-in-routeros):

- **raw**: `prerouting`, `output`.
- **filter**: `input`, `forward`, `output`.
- **mangle**: `prerouting`, `input`, `forward`, `output`, `postrouting`.
- **nat**: `srcnat`, `dstnat`, `input`, `output`.

The router takes the rules of a chain in the order in which they are listed, from top to bottom. When a packet matches a rule, the router applies the action of the rule and processes no more rules of the chain. The exceptions are the `passthrough` action and other actions that do not end the processing, such as `fasttrack-connection` in the filter table and some [mangle](./mangle) actions: after them, the router continues with the next rule. A packet that matches no rule of a chain is accepted.

### Chains of your own

You can add chains of your own and send packets to them with `action=jump`. A chain is created when you add its first rule. This lets you match a common condition once and put the detailed rules into a separate chain.

In this example, rules for the public address of an office, 198.51.100.7, are grouped in the chain `office`. The jump rule matches the source address and the interface, and the rules of the chain match only the ports, without repeating them:

```ros
/ip/firewall/filter
add chain=input action=jump jump-target=office \
    src-address=198.51.100.7 in-interface-list=WAN \
    comment="Rules for the office address" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=office action=accept protocol=tcp dst-port=22 \
    comment="SSH from the office"
add chain=office action=accept protocol=tcp dst-port=8291 \
    comment="WinBox from the office"
```

A packet that matches no rule of the `office` chain returns to the `input` chain and continues with the rule after the jump rule. In the default firewall, that is the rule that drops what does not come from the local network.

```ros
/ip/firewall/filter/print stats where chain=office or jump-target=office
```

```text
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN   ACTION  BYTES  PACKETS
;;; Rules for the office address
0 input   jump      300        5
;;; SSH from the office
1 office  accept     60        1
;;; WinBox from the office
2 office  accept     60        1
```
