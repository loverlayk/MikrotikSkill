# IPIP

> IPIP (IP-in-IP) tunnels carry IPv4 packets inside IPv4 or IPv6 packets between two routers. The page covers encapsulation, a routed-site example, keepalive, MTU and fragmentation, firewall matching, IPsec protection...

# IPIP

IPIP (IP-in-IP) places an IPv4 packet inside another IP header and sends it between two tunnel
endpoints. Use it for a routed link between two networks over a plain IP path, for example a
site-to-site connection that does not need Layer 2 or encryption. The tunnel carries IPv4 only and
adds 20 bytes of overhead over an IPv4 path, or 40 bytes over an IPv6 path.

An IPIP interface is a virtual interface: assign it an address and create routes through it, as with a
physical link. IPIP has no encryption, authentication or integrity protection. Protect the tunnel
with IPsec, or use it only on a trusted path. For a tunnel that also carries IPv6, use
[GRE](./gre); to extend a Layer 2 segment, use [EoIP](./eoip); for an encrypted tunnel without IPsec,
use [WireGuard](./wireguard).

RouterOS has two IPIP menus:

- [`/interface/ipip`](../cli-reference/interface/ipip) carries IPv4 inside IPv4.
- [`/interface/ipipv6`](../cli-reference/interface/ipipv6) carries IPv4 inside IPv6.

Both menus share most properties; `/interface/ipip` has `allow-fast-path` and `/interface/ipipv6`
does not. Before you begin, make sure `local-address` is an address already assigned to the router,
each router has a route to the other router's endpoint address that does not use the tunnel, and the
path passes the tunnel packets. The interface name is local and does not have to match on the other
router.

## How the tunnel works

The sending router takes an IPv4 packet from the tunnel interface, puts it after a new outer IPv4
header and sends the result to the remote endpoint. The outer header uses IP protocol 4. The
receiving router removes the outer header and delivers the original packet, so the tunneled packet
keeps its addresses and DSCP value.

For `/interface/ipipv6`, the outer header is IPv6 and its next header is 4 (IPIP). The inner packet
is still IPv4.

RouterOS does not negotiate the tunnel: both endpoints must be configured, with each router's
`local-address` set to the address that the other router reaches as `remote-address`. The tunnel
then carries packets in both directions; the routes for the LANs are configured separately.

The interface shows the `R` (running) flag when the tunnel is up. Keepalive decides when the
flag is removed: with keepalive enabled, the router sends a probe to the remote endpoint and keeps
the flag only while the peer answers. Without keepalive, the router does not remove the flag when
the peer stops answering.

The outer header takes space from the path MTU. With the default `mtu=auto`, the router sets
`actual-mtu` to the MTU of the underlying interface minus 20 bytes (IPv4) or 40 bytes (IPv6): 1480
and 1460 on a 1500-byte path. A fixed `mtu` overrides this value.

By default `dscp=inherit` copies the DSCP value of the tunneled packet to the outer header. Set
`dscp` to a number to mark the outer packets with that value instead, for example `dscp=46` for
traffic that the network should prioritize.

## Connect two sites with an IPIP tunnel

The example connects R1 (LAN 192.168.10.0/24) and R2 (LAN 192.168.20.0/24) over an IPv4 path. The
routers reach each other at 192.0.2.1 and 192.0.2.2 on a direct link, and their LAN addresses are
192.168.10.1 and 192.168.20.1. The example assumes those addresses are already configured; replace
them with your own, and make sure the two LAN subnets differ. The tunnel uses the subnet
10.10.10.0/30, which gives one address to each end.

On routers with the default firewall, accept protocol 4 from the peer before the tunnel can come up
(see the firewall section below).

On R1:

```ros
/interface/ipip/add name=ipip1 local-address=192.0.2.1 \
    remote-address=192.0.2.2
/ip/address/add address=10.10.10.1/30 interface=ipip1
/ip/route/add dst-address=192.168.20.0/24 gateway=10.10.10.2
```

On R2:

```ros
/interface/ipip/add name=ipip1 local-address=192.0.2.2 \
    remote-address=192.0.2.1
/ip/address/add address=10.10.10.2/30 interface=ipip1
/ip/route/add dst-address=192.168.10.0/24 gateway=10.10.10.1
```

The static route sends the other site's LAN through the tunnel. Each router needs its own route;
configuring one router does not make the return path work.

Check the interface and the tunnel address:

```ros
/interface/ipip/print
Flags: R - RUNNING
Columns: NAME, MTU, ACTUAL-MTU, LOCAL-ADDRESS, REMOTE-ADDRESS, KEEPALIVE, 
         DSCP
#   NAME   MTU   ACTUAL-MTU  LOCAL-ADDRESS  REMOTE-ADDRESS  KEEPALIVE  DSCP   
0 R ipip1  auto        1480  192.0.2.1      192.0.2.2       10s,10     inherit
```

The `R` flag appears after the remote endpoint answers a keepalive probe; with the default `10s,10`,
allow up to 10 seconds. Test the tunnel and the route:

```ros
/ping 10.10.10.2 count=3
  SEQ HOST                                     SIZE TTL TIME       STATUS      
    0 10.10.10.2                                 56  64 351us     
    1 10.10.10.2                                 56  64 257us     
    2 10.10.10.2                                 56  64 299us     
    sent=3 received=3 packet-loss=0% min-rtt=257us avg-rtt=302us 
   max-rtt=351us

/ping 192.168.20.1 count=3
  SEQ HOST                                     SIZE TTL TIME       STATUS      
    0 192.168.20.1                               56  64 198us     
    1 192.168.20.1                               56  64 304us     
    2 192.168.20.1                               56  64 311us     
    sent=3 received=3 packet-loss=0% min-rtt=198us avg-rtt=271us 
   max-rtt=311us
```

The first ping reaches R2's tunnel address, the second one reaches R2's LAN address through the
tunnel. Test from a host on each LAN too, because a ping from the router does not exercise
forwarding.

## Keepalive

Keepalive is on by default (`10s,10`): the router probes the remote endpoint every 10 seconds and
removes the `R` flag after 10 unanswered probes, so about 100 seconds after the peer stops
answering. Shorten it for faster failover, for example `keepalive=1s,2` detects a dead peer in
about two seconds. The interval must be at least 1 second and the retry count at least 1.

With keepalive enabled, the remote end must answer RouterOS keepalive probes. A Linux `ipip` tunnel
does not answer them. The tunnel then never reaches the `R` flag, even though the peer is reachable,
and no traffic passes. Disable keepalive on the RouterOS side in that case:

```ros
/interface/ipip/unset ipip1 keepalive
```

For `/interface/ipipv6`, use the same command on that menu. Without keepalive, the `R` flag stays
set when the peer stops answering, so the tunnel cannot detect a dead peer on its own. Use it when
the peer does not support RouterOS keepalive.

## MTU and fragmentation

`actual-mtu` is the largest inner packet that the tunnel accepts. With `mtu=auto`, it follows the MTU
of the underlying interface: when that interface's MTU is smaller, `actual-mtu` drops by the same
amount. Auto does not track a smaller MTU on the path beyond the router. If the path MTU is lower,
or you want a fixed value, set `mtu` explicitly:

```ros
/interface/ipip/set ipip1 mtu=1400
```

Packets larger than the tunnel MTU are fragmented on the outer packet when the outer header allows
fragmentation. To keep TCP connections working across the tunnel, `clamp-tcp-mss` (enabled by
default) lowers the MSS in received TCP SYN packets to fit the tunnel; UDP and ICMP traffic needs a
smaller `mtu` instead.

The `dont-fragment` property controls the DF bit in the outer header: `no` (the default) clears it,
so the outer packet can be fragmented; `inherit` copies the DF flag from the tunneled packet and
drops an inner packet whose DF bit is set when it exceeds the tunnel MTU.

## Filter tunnel traffic

The firewall protocol name `ipip` in RouterOS means IP protocol 94. An IPIP tunnel itself uses IP
protocol 4, which the firewall names `ipencap`. Use `protocol=ipencap` in firewall rules; a rule with
`protocol=ipip` never matches an IPIP tunnel.

On a router with the default firewall, the input chain drops packets that do not come from the LAN,
including tunnel packets addressed to the router. Accept them from the remote endpoint before that
rule:

```ros
/ip/firewall/filter/add chain=input action=accept protocol=ipencap \
    src-address=192.0.2.2 \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

Use the remote endpoint address in `src-address` and create a rule for each peer. If the router does
not have that default rule, add the accept rule at the top of the input chain instead.

With `allow-fast-path=yes` (the default), packets of an established flow can bypass the firewall,
so the rule counters do not show every packet. Set `allow-fast-path=no` on the tunnel if every
packet must pass the firewall; see
[Packet flow in RouterOS](../firewall-and-quality-of-service/packet-flow-in-routeros).

## Protect the tunnel with IPsec

Set the same `ipsec-secret` on both ends to encrypt the tunnel. RouterOS adds a dynamic IPsec peer
and a transport-mode policy for the tunnel packets; keepalive packets are protected too.

On `/interface/ipip`, set `allow-fast-path=no` first. RouterOS does not support FastPath together
with IPsec, and setting the secret while FastPath is enabled fails with
`cannot enable fastpath together with ipsec yet`:

```ros
/interface/ipip/set ipip1 allow-fast-path=no
/interface/ipip/set ipip1 ipsec-secret=change-this-secret
```

`/interface/ipipv6` has no `allow-fast-path` property, so set `ipsec-secret` directly there. Run the
commands on R1 and R2, with the same secret. Check that the peer is established:

```ros
/ip/ipsec/active-peers/print
Flags: R - RESPONDER
Columns: STATE, UPTIME, PH2-TOTAL, REMOTE-ADDRESS
#    STATE        UPTIME  PH2-TOTAL  REMOTE-ADDRESS
;;; ipip1
0    established  14s             2  192.0.2.2     
;;; ipip1
1 R  established  8s                 192.0.2.2     
```

Both ends have the secret, so each router lists two sessions: the one it started and the one it
answered, marked `R - RESPONDER`. An `established` state with a non-zero `PH2-TOTAL` shows that the
tunnel is encrypted.

IPsec adds its own overhead to the outer packet, so `actual-mtu` becomes smaller: 1438 bytes on a
1500-byte path with the default proposal in this example. Adjust `mtu` or the MSS if connections
through the tunnel stall on large packets.

To remove the encryption and the dynamic IPsec entries, unset the secret on both ends:

```ros
/interface/ipip/unset ipip1 ipsec-secret
```

For `/interface/ipipv6`, unset the secret on that menu instead.

## IPv4 over IPv6

`/interface/ipipv6` carries IPv4 over an IPv6 path, for example an IPv4 site-to-site link across an
IPv6-only provider. Use the IPv6 addresses of the two endpoints; the inner configuration is IPv4.
The example puts the endpoints on a direct link with global addresses; in practice use the addresses
your provider assigns.

On R1:

```ros
/interface/ipipv6/add name=ipipv6-1 local-address=2001:db8:0:5::1 \
    remote-address=2001:db8:0:5::2
/ip/address/add address=10.20.20.1/30 interface=ipipv6-1
```

On R2, swap the endpoint addresses and the tunnel address:

```ros
/interface/ipipv6/add name=ipipv6-1 local-address=2001:db8:0:5::2 \
    remote-address=2001:db8:0:5::1
/ip/address/add address=10.20.20.2/30 interface=ipipv6-1
```

```ros
/interface/ipipv6/print
Flags: R - RUNNING
Columns: NAME, MTU, ACTUAL-MTU, LOCAL-ADDRESS, REMOTE-ADDRESS, KEEPALIVE, 
         DSCP
#   NAME      MTU   ACTU  LOCAL-ADDRESS    REMOTE-ADDRESS   KEEPALIVE  DSCP   
0 R ipipv6-1  auto  1460  2001:db8:0:5::1  2001:db8:0:5::2  10s,10     inherit

/ping 10.20.20.2 count=3
  SEQ HOST                                     SIZE TTL TIME       STATUS      
    0 10.20.20.2                                 56  64 380us     
    1 10.20.20.2                                 56  64 402us     
    2 10.20.20.2                                 56  64 382us     
    sent=3 received=3 packet-loss=0% min-rtt=380us avg-rtt=388us 
   max-rtt=402us
```

`actual-mtu` is 1460 on a 1500-byte IPv6 path: the 40-byte IPv6 header is larger than the 20-byte
IPv4 header. Keepalive, DSCP and MTU work as for `/interface/ipip`; IPsec works without the
`allow-fast-path` step. Create routes for the LANs as in the IPv4 example.

## Troubleshooting

### The tunnel has no `R` flag

- **Disabled interface.** A disabled interface shows the `X` flag in `/interface/ipip/print`. Enable
  it and allow up to one keepalive interval (10 seconds with the default) for the flag to appear.
- **Keepalive and the peer.** The endpoint can be reachable but not answer RouterOS keepalive
  probes, as a Linux `ipip` tunnel does. Disable keepalive with
  `/interface/ipip/unset <name> keepalive` and ping the remote tunnel address: the flag no longer
  proves the path, so the ping does.
- **Endpoint addresses.** Each router must reach the other's `remote-address` through a route that
  does not use the tunnel itself, and `local-address` must be an address assigned to the router.
  Test the path with `/ping <remote-address> src-address=<local-address>`.
- **Firewall.** The input chain must accept `protocol=ipencap` from the remote endpoint. A rule
  written as `protocol=ipip` matches protocol 94 and does not help.
- **Both ends.** The remote router must have a tunnel with the local and remote addresses reversed.
  With keepalive enabled, a tunnel with only one end configured never gets the flag.

### The tunnel is running but traffic does not pass

- **Return route.** Create a route on the remote router for the local LAN. A ping that works in one
  direction and fails in the other usually misses this route.
- **Tunnel addresses.** The addresses at the two ends of the tunnel must be in the same subnet and
  must not overlap with a LAN.
- **NAT or firewall on the path.** The outer packets are ordinary IP packets from the endpoint
  addresses; a NAT rule or firewall on the path that blocks protocol 4 stops the tunnel.
- **IPsec mismatch.** Both ends need the same `ipsec-secret`; with a secret on one end only, ping
  over the tunnel fails in both directions.

### Large packets fail

Reduce `mtu` on both ends to the largest inner packet that passes. For TCP, `clamp-tcp-mss=yes`
negotiates a smaller MSS; UDP and ICMP traffic needs the smaller `mtu`. A ping with
`size=1492 do-not-fragment` fails on a 1500-byte path because the packet exceeds the 1480-byte
tunnel MTU. With IPsec, use a smaller value still, because the IPsec header and trailer add to the
outer packet.

### Setting the IPsec secret fails

On `/interface/ipip`, setting the secret fails while FastPath is enabled. Set `allow-fast-path=no`
first; the error message is `cannot enable fastpath together with ipsec yet`.

## Technical details

An IPIP packet is an outer IPv4 header with protocol 4 followed by the unchanged inner IPv4 packet.
The header adds 20 bytes, so the tunnel MTU is 20 bytes below the path MTU: a packet at the tunnel
MTU (1480 bytes on a 1500-byte path) fills the path exactly. `/interface/ipipv6` uses an outer IPv6
header with next header 4 and adds 40 bytes.

A keepalive probe is an outer packet with an empty payload: for `/interface/ipip`, an IPv4 packet
with protocol 4 and an inner IPv4 header without data (40-byte outer packet); for
`/interface/ipipv6`, an IPv6 packet with next header 41 instead of the next header 4 used for data.
The probe travels from the local endpoint to the remote endpoint, and the running flag remains while
replies arrive.

IPIP is stateless: there is no session establishment, and the running flag is the only state. The
tunnel does not fragment the inner packet: packets above the tunnel MTU rely on outer fragmentation
or on the sender reducing its packet size.

The IPv4 encapsulation is defined in [RFC 2003](https://www.rfc-editor.org/rfc/rfc2003). The menus
and every property are described in the [`/interface/ipip`](../cli-reference/interface/ipip) and
[`/interface/ipipv6`](../cli-reference/interface/ipipv6) CLI references.
