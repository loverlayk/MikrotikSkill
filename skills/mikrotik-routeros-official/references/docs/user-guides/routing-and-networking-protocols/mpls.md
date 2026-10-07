# MPLS

> MPLS is a routing technology that uses labels for faster packet forwarding instead of IP header analysis, with RouterOS supporting MPLS switching, LDP/RSVP-TE protocols, VPLS, and MP-BGP VPNs while excluding certain...

MPLS stands for MultiProtocol Label Switching. Instead of using IP routing, MPLS bases the packet forwarding decision (outgoing interface and next-hop router) on labels attached to a packet, rather than on fields in the IP header (such as destination address) and the routing table. This approach speeds up the forwarding process because the next-hop lookup is simpler than routing lookup (finding the longest matching prefix).

The efficiency of the forwarding process is the main benefit of MPLS. However, keep in mind that MPLS forwarding disables the processing of network layer (for example, IP) headers. Therefore, you cannot apply network layer-based actions like NAT and filtering to MPLS forwarded packets. Apply any network-layer-based actions at the ingress or egress of the MPLS cloud, with ingress being the preferred method. This way, traffic that you intend to drop does not travel through the MPLS backbone.

MPLS operates by distributing labels with the LDP protocol for active routes, and a labeled packet takes the same path as an unlabeled packet would. When a router routes unlabeled packets along a route for which it has received a label from the next hop, it imposes a label on the packet and sends it to the next hop, where MPLS switches it further along the path. When a router receives a packet with a label it has assigned to a particular route, it replaces the packet label with the one received from the next hop of that route and sends the packet to the next hop. A label switched path ensures delivery of data to the MPLS cloud egress point. MPLS applications are based on this concept of label switched paths.

Another way to establish label switching paths is through traffic engineering tunnels (TE tunnels) using the RSVP-TE protocol. Traffic engineering tunnels allow explicitly routed LSPs and constraint-based path selection (where constraints are interface properties and available bandwidth).

Because MPLS introduces complexity and new protocols, and adds different concepts to routed and bridged networks, you should develop an in-depth understanding of MPLS concepts before implementing MPLS in a production network. Some suggested reading material:

- Multiprotocol Label Switching [http://en.wikipedia.org/wiki/Multiprotocol_Label_Switching](http://en.wikipedia.org/wiki/Multiprotocol_Label_Switching)
- RFC3031 Multiprotocol Label Switching Architecture [http://www.ietf.org/rfc/rfc3031.txt](http://www.ietf.org/rfc/rfc3031.txt)
- MPLS Fundamentals by Luc De Ghein [http://www.amazon.com/MPLS-Fundamentals-Luc-Ghein/dp/1587051974](http://www.amazon.com/MPLS-Fundamentals-Luc-Ghein/dp/1587051974)

:::info
This feature is not supported on SMIPS devices (hAP lite, hAP lite TC and hAP mini).
:::

## Supported Features

RouterOS supports the following MPLS-related features:

- MPLS switching with penultimate hop popping support.
- Static local label bindings for IPv4 and IPv6.
- Static remote label bindings for IPv4 and IPv6.
- Label Distribution Protocol ([RFC 3036](https://tools.ietf.org/html/rfc3036), [RFC 5036](https://tools.ietf.org/html/rfc5036), and [RFC 7552](https://tools.ietf.org/html/rfc7552)) for IPv4 and IPv6:
  - Downstream unsolicited label advertisement.
  - Independent label distribution control.
  - Liberal label retention.
  - Targeted session establishment.
  - Optional loop detection.
  - ECMP support.
- Virtual Private LAN Service (VPLS):
  - VPLS LDP signaling ([RFC 4762](https://tools.ietf.org/html/rfc4762)).
  - Cisco-style static VPLS pseudowires ([RFC 4447](https://tools.ietf.org/html/rfc4447) FEC type 0x80).
  - VPLS pseudowire fragmentation and reassembly ([RFC 4623](https://tools.ietf.org/html/rfc4623)).
  - VPLS MP-BGP based autodiscovery and signaling ([RFC 4761](https://tools.ietf.org/html/rfc4761)).
  - Cisco VPLS BGP-based auto-discovery ([draft-ietf-l2vpn-signaling-08](https://tools.ietf.org/html/draft-ietf-l2vpn-signaling-08)).
  - Support for multiple import/export route-target extended communities for BGP-based VPLS (both [RFC 4761](https://tools.ietf.org/html/rfc4761) and [draft-ietf-l2vpn-signaling-08](https://tools.ietf.org/html/draft-ietf-l2vpn-signaling-08)).
- RSVP-TE Tunnels:
  - Tunnel head-end.
  - Explicit paths.
  - OSPF extensions for TE tunnels.
  - CSPF path selection.
  - Forwarding of VPLS and MPLS IP VPN traffic on TE tunnels.
  - Ingress TE tunnel rate limit and automatic reserved bandwidth adjustment. For more information, see [Traffic Eng](./traffic-eng.md).
  - All tunnel bandwidth settings are specified and displayed in bits per second.
- MP-BGP based MPLS IP VPN.
- Per-prefix and per-VRF label distribution policies for MP-BGP based MPLS VPN.
- OSPF extensions for MPLS TE.
- Support for OSPF as a CE-PE protocol.
- Ping and traceroute for a specified VRF.
- Control over network-layer TTL propagation in MPLS.
- RIP as a CE-PE protocol.
- Per-VRF BGP instance redistribution settings.

## MPLS features that RouterOS DOES NOT HAVE yet

- LDP features:
  - Downstream on-demand label advertisement.
  - Ordered label distribution control.
  - Conservative label retention.
- TE features:
  - Fast-reroute.
  - Link/node protection.
- Support for BGP as a label distribution protocol.

<DocCardList />
