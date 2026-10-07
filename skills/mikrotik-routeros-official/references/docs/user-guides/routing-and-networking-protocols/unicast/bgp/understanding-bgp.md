# Understanding BGP

> Overview of BGP protocol basics.

# Understanding BGP

The **Border Gateway Protocol** (**BGP**) is an exterior gateway protocol (**EGP**). It lets you set up an inter-domain dynamic routing system. The system automatically updates routing tables on BGP routers when network topology changes.

BGP is an inter-autonomous-system routing protocol based on the **path-vector** algorithm. It exchanges routing information across the Internet and is the only protocol designed to operate at Internet scale and handle multiple connections to unrelated routing domains.

BGP is designed to allow administrators to implement sophisticated routing policies. It does not exchange information about network topology but rather reachability information. As such, BGP is better suited to **inter-AS** environments and special cases like informational feeds. If you need to enable dynamic routing in your network, use OSPF instead.

:::info
BGP is not supported on SMIPS devices (hAP lite, hAP lite TC, and hAP mini).
:::

## Terminology

- **AS** - An Autonomous System is a set of routers under a single technical administration with common set of metrics.
- **ASN** - Autonomous System Number is a unique identifier for an Autonomous System. ASNs can be private or public. Public ASNs are unique globally and are assigned by regulatory organizations such as RIPE.
- **AS Path** - Sequence of autonomous systems the route traverses.
- **Path Attributes** - Contain additional information about the AS path and are used in routing policy.
- **Routing policy** - A set of rules to control the redistribution of routing information and to choose the best path among multiple available paths.
- **NLRI** - Network Layer Reachability Information is what is exchanged between BGP peers and represents how to reach prefixes.
- **IGP** - an Interior Gateway Protocol such as OSPF or ISIS.
- **EGP** - an Exterior Gateway Protocol such as BGP.
- **RR** - A route reflector is a BGP router that reflects routing information between **iBGP** speakers, eliminating the need for full mesh connectivity.
- **Route server** - A BGP router that does not participate in traffic forwarding. Routes are typically not even installed in the FIB.
- **Loopback address** - A /32 (IPv4) or /128 (IPv6) address configured on a dummy bridge interface that can act as a loopback.

There are two types of BGP connections:

- **iBGP** - An "internal" link connecting peers from the same AS.
- **eBGP** - An "external" link connecting peers belonging to two different AS-es.

## Protocol basics

BGP routers exchange reachability information by means of a transport protocol; in the case of BGP, that protocol is TCP (port 179). Upon forming a TCP connection, these routers exchange **OPEN** messages to negotiate and confirm supported capabilities.

After agreeing on capabilities to use, the session is considered to be **established** and peers can start to exchange NLRIs via **UPDATE** messages. These messages indicate the sequence of AS‑es (AS Path) the route should take to reach the destination network (NLRI prefix).

The peers initially exchange their full routing tables and after the initial exchange, incremental updates are sent as the routing tables change. Thus, BGP does not require a periodic refresh of the entire BGP routing table.

BGP maintains the routing table version number which must be the same between any two given peers for the duration of the connection.

**KEEPALIVE** messages are sent periodically to ensure the connection is up and running. If the messages are not received within the **Hold Time** interval, the connection closes.

To respond to errors or special conditions, **NOTIFICATION** messages can be generated and sent to the remote peer; this message type also indicates whether the connection should close immediately.

An AS might have multiple BGP speakers and provide transit service to other AS‑es. This implies that BGP speakers must maintain a consistent view of routing within the AS. A consistent view of routes exterior to the AS is provided by having all BGP routers within the AS establish direct **iBGP** connections with each other (full mesh) or by utilizing a **route reflector** setup.

Using a set of administrative policies (routing policies), BGP speakers within the AS come to an agreement about which entry or exit point to use for a particular destination. This information is communicated to the interior routers of the AS using the interior routing protocol (**IGP**), for example, OSPF, RIP, or static routing. In certain setups, iBGP can take the IGP protocol role as well.

For certain BGP attributes, handling behavior may change depending on the type of connection; for example, the **LOCAL-PREF** attribute is not advertised to **eBGP** peers.

RouterOS divides configuration and session monitoring into four menus:

- instance menu ([`/routing/bgp/instance`](../../../../cli-reference/routing/bgp/instance.md))
- connection menu ([`/routing/bgp/connection`](../../../../cli-reference/routing/bgp/connection.md))
- sessions menu ([`/routing/bgp/session`](../../../../cli-reference/routing/bgp/session/session.md))
- template menu ([`/routing/bgp/template`](../../../../cli-reference/routing/bgp/template.md))

## Route origin

A BGP router that first advertises a route assigns its origin and writes it in the **ORIGIN** attribute.  
There are three origin types:

- 0 - Router originally learned the route through an **IGP**. RouterOS assigns this value if the route is learned via BGP [`output.network`](../../../../cli-reference/routing/bgp/connection.md#output.network).
- 1 - Router originally learned the route through an **EGP**.
- 2 - Origin is unknown/incomplete. RouterOS assigns this value if route is learned via BGP [`output.redistribute`](../../../../cli-reference/routing/bgp/connection.md#output.redistribute).

## Best-Path Selection

BGP routers can receive multiple copies of the global routing table from multiple providers, but by default BGP can have only one best path. To select the best route, BGP uses the **Best Path Selection Algorithm**.

The route is evaluated by the algorithm only if it is valid. In general, the route is considered valid if:

- The **NEXT_HOP** of the route is valid and reachable
- The **AS_PATH** received from external peers does not contain the local AS
- The route is not rejected by [routing filters](../../../../cli-reference/routing/filter/rule)

For more information read [nexthop selection and validation](./nexthop-selection.md).

The best path algorithm also compares routes received only by a **single BGP instance**. Routes installed by different BGP instances are compared by the general algorithm; i.e., route distances are compared, and the route with a lower distance is preferred.

If all the criteria are met, then the following actions take place:

1. The first path received is automatically considered the 'best path'. Any further received paths are compared to the first received to determine if the new path is better.
2. Prefer the path with the highest **WEIGHT**.
   This parameter is not a part of the BGP standard, it is invented to quickly locally select the best route. A parameter is local to the router (assigned with routing filters in the BGP input) and cannot be advertised. A route without assigned WEIGHT has a default value of 0.
3. Prefer the path with the highest **LOCAL_PREF**.
   This attribute is used only within an AS. A path without the LOCAL_PREF attribute has a value of 100 by default.
4. Prefer the path with the shortest **AS_PATH** (skipped if [`ignore-as-path-len`](../../../../cli-reference/routing/bgp/instance.md#ignore-as-path-len) is set to **yes**).  
   Each **AS_SET** counts as 1, regardless of the set size. The **AS_CONFED_SEQUENCE** and **AS_CONFED_SET** are not included in the **AS_PATH** length.
5. ~~Prefer the path that was locally originated via aggregate or BGP network~~
6. Prefer the path with the lowest [**ORIGIN** type](#route-origin).

   Interior Gateway Protocol (IGP) is lower than Exterior Gateway Protocol (EGP), and EGP is lower than INCOMPLETE.

   In other words, **IGP < EGP < INCOMPLETE**.
7. Prefer the path with the lowest **multi-exit discriminator** (MED).

   The router compares the MED attribute only for paths that have the same neighboring (leftmost) AS. Confederations are not considered when determining the neighboring AS.  
   Paths without an explicit MED value are treated with a MED of 0.
8. Prefer **eBGP** over **iBGP** paths.
9. If `multipath` is enabled, break here and consider paths equal. This will install BGP [ECMP](../../routing-decision.md#multipath-ecmp-routes) routes.
10. Prefer the lowest **IGP metric**.
11. Prefer the route that comes from the BGP router with the lowest [**router ID**](../../../../cli-reference/routing/bgp/instance.md#router-id). If a route carries the **ORIGINATOR_ID** attribute, then the **ORIGINATOR_ID** is used instead of the router ID.
12. Prefer the route with the shortest **route reflection cluster list**. Routes without a cluster list are considered to have a cluster list of length 0.
13. Prefer the path that comes from the lowest neighbor address.

## Multiple instances

There might be a need to run multiple instances of BGP for instance‑dependent features like Layer3 VPN and [EVPN](../evpn.md). RouterOS allows you to add more than one instance in the [`/routing/bgp/instance`](../../../../cli-reference/routing/bgp/instance.md) menu.

Keep in mind that [best path selection](#best-path-selection) does not work on routes from different instances. Also, the default redistribution policy does not redistribute BGP routes received from sessions that do not belong to the same instance. In such cases, set [`output.redistribute`](../../../../cli-reference/routing/bgp/connection.md#output.redistribute)`=bgp` if such redistribution is needed.

## Supported standards

- [RFC 4271](https://tools.ietf.org/html/rfc4271) Border Gateway Protocol 4
- [RFC 4456](https://tools.ietf.org/html/rfc4456) BGP Route Reflection
- [RFC 5065](https://tools.ietf.org/html/rfc5065) Autonomous System Confederations for BGP
- [RFC 1997](https://tools.ietf.org/html/rfc1997) BGP Communities Attribute
- [RFC 8092](https://tools.ietf.org/html/rfc8092) BGP Large Communities
- [RFC 4360](https://tools.ietf.org/html/rfc4360), [5668](https://tools.ietf.org/html/rfc5668) BGP Extended Communities
- [RFC 2385](https://tools.ietf.org/html/rfc2385) TCP MD5 Authentication for BGPv4
- [RFC 5492](https://tools.ietf.org/html/rfc5492) Capabilities Advertisement with BGP-4
- [RFC 2918](https://tools.ietf.org/html/rfc2918) Route Refresh Capability
- [RFC 4760](https://tools.ietf.org/html/rfc4760) Multiprotocol Extensions for BGP-4
- [RFC 2545](https://tools.ietf.org/html/rfc2545) Use of BGP-4 Multiprotocol Extensions for IPv6 Inter-Domain Routing
- [RFC 4893](https://tools.ietf.org/html/rfc4893) BGP Support for Four-octet AS Number Space
- [RFC 4364](https://tools.ietf.org/html/rfc4364) BGP/MPLS IP Virtual Private Networks (VPNs)
- [RFC 4761](https://tools.ietf.org/html/rfc4761) Virtual Private LAN Service (VPLS) Using BGP for Auto-Discovery and Signalling
- draft-ietf-l2vpn-signaling-08 Cisco VPLS BGP-based auto-discovery
- [RFC 6286](https://tools.ietf.org/html/rfc6286) AS-wide Unique BGP Identifier for BGP-4
- [RFC 4273](https://tools.ietf.org/html/rfc4273) SNMP peer table monitoring (OID 1.3.6.1.2.1.15.3.1) (IPv4 only)
- [RFC 6793](https://www.rfc-editor.org/rfc/rfc6793) 4-byte ASN support and Aggregator attribute.
- [RFC 4486](https://datatracker.ietf.org/doc/html/rfc4486) Subcodes for BGP Cease Notification Message
- [RFC 4659](https://datatracker.ietf.org/doc/html/rfc4659) MPLS VPN Extension for IPv6
- [RFC 8950](https://datatracker.ietf.org/doc/html/rfc8950) Advertising IPv4 Network Layer Reachability Information (NLRI) with an IPv6 Next Hop
- [RFC 6811](https://datatracker.ietf.org/doc/html/rfc6811) BGP Prefix Origin Validation
- [RFC 6996](https://www.rfc-editor.org/rfc/rfc6996.html) Autonomous System (AS) Reservation for Private Use
- [RFC 9234](https://datatracker.ietf.org/doc/rfc9234/) Route Leak Prevention and Detection Using Roles in UPDATE and OPEN Messages
- [RFC 5549](https://datatracker.ietf.org/doc/html/rfc5549) Advertising IPv4 Network Layer Reachability Information with an IPv6 Next Hop
