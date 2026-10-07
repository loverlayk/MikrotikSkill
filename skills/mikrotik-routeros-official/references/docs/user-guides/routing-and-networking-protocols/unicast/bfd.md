# BFD

> Bidirectional Forwarding Detection (BFD) is a low-latency protocol for detecting faults in network paths, operating independently of routing protocols. It uses UDP encapsulation with configurable ports and supports...

# BFD

**Bidirectional Forwarding Detection** (**BFD**) is a low‑overhead, short‑duration protocol that detects faults in the bidirectional path between two forwarding engines. This includes physical interfaces, sub‑interfaces, data links, and — as far as possible — the forwarding engines themselves, all with very low latency. It operates independently of media, data protocols, and routing protocols.

**BFD** is a hello protocol that checks bidirectional neighbor reachability. It provides sub‑second link failure detection and is not specific to any routing protocol, unlike protocol hello timers.

**Control** data is encapsulated in a **UDP** frame with destination port 3784; port 4784 is used for multihop paths. The source port range is 49152 – 65535.  
**Echo** is encapsulated in a UDP frame with destination port 3785.

Standards and Technologies:

- [RFC 5880 Bidirectional Forwarding Detection (BFD)](https://datatracker.ietf.org/doc/rfc5880/)
- [RFC 5881 BFD for IPv4 and IPv6](https://datatracker.ietf.org/doc/rfc5881/)
- [RFC 5882 Generic Application of BFD](https://datatracker.ietf.org/doc/rfc5882/)
- [RFC 5883 Bidirectional Forwarding Detection (BFD) for Multihop Paths](https://datatracker.ietf.org/doc/rfc5883/)

## Features not yet supported

- Echo mode.
- Enabling BFD for ip route gateways.
- Authentication.

## Configuration

Allowing or forbidding **BFD** sessions can be done from the [`/routing/bfd/configuration`](../../../cli-reference/routing/bfd/configuration.md) menu. For example:

```ros
/routing bfd configuration
add interfaces=sfp12 forbid-bfd=yes
add interfaces=static
```

Configuration entries are order sensitive, which means that in the example above we are forbidding BFD sessions explicitly on the "sfp12" interface (using [`forbid-bfd`](../../../cli-reference/routing/bfd/configuration.md#forbid-bfd)) and allowing on the rest of the interfaces belonging to the "static" interface list.

To be able to filter multi-hop sessions, [`addresses`](../../../cli-reference/routing/bfd/configuration.md#addresses) or [`address-list`](../../../cli-reference/routing/bfd/configuration.md#address-list) properties can be used to match the destination, as well as the appropriate [`vrf`](../../../cli-reference/routing/bfd/configuration.md#vrf), if a session is not running in the "main" VRF.

```ros
/ip firewall address-list
add address=10.155.255.183 list=bgp_allow_bfd
add address=10.155.255.217 list=bgp_allow_bfd

/routing bfd configuration
add addresses=111.111.0.0/16 vrf=vrf1
add address-list=bgp_allow_bfd
```

Anything not explicitly listed in the configuration is forbidden by default.

### BFD with BGP

To enable BFD for [BGP](./bgp/index.md) sessions, set [`use-bfd`](../../../cli-reference/routing/bgp/connection.md#use-bfd) on the required entries in the [`/routing/bgp/connection`](../../../cli-reference/routing/bgp/connection.md) menu.

The BGP session output shows when the associated BFD session is down:

```ros
[admin@dr_02_BGP_MUM] /routing/bgp/session> print 
Flags: E - established 
 0 E ;;; BFD session down
     name="ovpn_test1-1" 
     remote.address=111.111.11.11@vrf1 .as=65530 .id=10.155.101.217 
     .capabilities=mp,rr,as4 .hold-time=infinity .messages=40717 
     .bytes=3436281 .eor="" 
     local.address=111.111.11.12@vrf1 .as=555 .id=111.111.11.12 
     .capabilities=mp,rr,gr,as4 .messages=1 .bytes=19 .eor="" 
     output.procid=20 
     input.procid=20 .filter=bgp-in ebgp 
     hold-time=infinity use-bfd=yes uptime=3s210ms 
     last-started=2023-05-19 09:54:04 prefix-count=3853 
```

### BFD with OSPF

To enable BFD for [OSPF](./ospf/index.md) neighbors, set [`use-bfd`](../../../cli-reference/routing/ospf/interface-template.md#use-bfd) on the required entries in the [`/routing/ospf/interface-template`](../../../cli-reference/routing/ospf/interface-template.md) menu.

## Session Status

View the status of current sessions in the [`/routing/bfd/session`](../../../cli-reference/routing/bfd/session.md) menu:

```ros
[admin@dr_02_BGP_MUM] /routing/bfd/session> print 
Flags: U - up, I - inactive 
 0 I ;;; BFD forbidden for destination address
     multihop=yes remote-address=10.155.101.183 local-address="" desired-tx-interval=0ms required-min-rx=0ms 
     multiplier=0 

 1   multihop=no remote-address=111.111.11.11%ovpn-out1@vrf1 local-address=111.111.11.12@vrf1 state=down 
     state-changes=0 desired-tx-interval=200ms required-min-rx=200ms remote-min-rx=1us multiplier=5 
     packets-rx=0 packets-tx=7674 
```

BFD picks the higher of the local tx interval and the remote minimum rx interval as the desired transmit interval. If the session is not established, the desired minimum tx interval defaults to 1 second.
