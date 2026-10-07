# VPLS

> The VPLS page introduces MikroTik RouterOS's Virtual Private LAN Service (VPLS) interface, detailing its use as a transparent ethernet tunnel with LDP or MP-BGP protocols. It covers VPLS features like pseudowire...

# VPLS

The Virtual Private LAN Service (VPLS) interface can be considered a tunnel interface just like the [EoIP](../../../../virtual-private-networks/eoip.md) interface, to achieve transparent ethernet segment forwarding between customer sites.

Negotiation of VPLS tunnels can be done by LDP protocol or MP-BGP - both endpoints of the tunnel exchange labels they are going to use for the tunnel.

Data forwarding in the tunnel happens by imposing 2 labels on packets: tunnel label and transport label - a label that ensures traffic delivery to the other endpoint of the tunnel.

MikroTik RouterOS implements the following VPLS features:

- VPLS LDP signaling (RFC 4762).
- Cisco style static VPLS pseudowires (RFC 4447 FEC type 0x80).
- VPLS pseudowire fragmentation and reassembly (RFC 4623).
- VPLS MP-BGP based autodiscovery and signaling (RFC 4761).
- Cisco VPLS BGP-based auto-discovery (draft-ietf-l2vpn-signaling-08).
- Support for multiple import/export route-target extended communities for BGP based VPLS (both RFC 4761 and draft-ietf-l2vpn-signaling-08).

## VPLS Prerequisites

For VPLS to be able to transport MPLS packets, one of the label distribution protocols should be already running on the backbone; it can be LDP, RSVP-TE, or static bindings.

Before moving forward, familiarize yourself with the [prerequisites required for LDP](../ldp.md#prerequisites-for-mpls) and prerequisites for RSVP-TE.

If BGP should be used as a VPLS discovery and signaling protocol, the backbone should be running iBGP preferably with route reflector/s.

## Example Setup

Let's consider that we already have a working LDP setup from the [LDP configuration example](../ldp.md#example-setup).

Routers R1, R3, and R4 are connected to Customer A sites, and routers R1 and R3 are connected to Customer B sites. Customers require transparent L2 connectivity between the sites.
