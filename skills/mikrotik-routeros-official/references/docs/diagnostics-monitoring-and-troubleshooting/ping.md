# Ping

> The RouterOS ping tool: check that a host or the internet is reachable, read the status of each reply, find the path MTU, ping from a chosen address, interface or VRF, reach hosts that block ICMP with ARP and ND...

# Ping

Ping checks whether a host answers and how long the answer takes. The router sends Internet Control Message Protocol (ICMP) echo requests (type 8) to the host, and the host answers each one with an echo reply (type 0). The time between a request and its reply is the round-trip time. A request whose reply does not arrive within `interval`, 1 second by default, is reported as a timeout.

Each reply also shows its Time to Live (TTL). Every router that forwards a packet lowers its TTL by one, and a packet whose TTL runs out is dropped. The TTL column shows the TTL of the reply as it arrived, so it tells roughly how many routers the reply crossed: most systems send with TTL 64, 128 or 255, so a reply that arrives with TTL 62 crossed two routers. The router sends its own requests with TTL 255 (IPv4) or hop limit 64 (IPv6).

`/ping` is the short form of `/tool/ping`. To find out where on the path packets stop, use [Traceroute](traceroute).

## Check that a host is reachable

To check the internet connection, ping a public address, then a name:

```ros
/ping 1.1.1.1 count=3
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 1.1.1.1                                    56  60 1ms45us
    1 1.1.1.1                                    56  60 1ms89us
    2 1.1.1.1                                    56  60 1ms163us
    sent=3 received=3 packet-loss=0% min-rtt=1ms45us avg-rtt=1ms99us max-rtt=1ms163us
```

```ros
/ping mikrotik.com count=3
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 159.148.172.205                            56  55 1ms582us
    1 159.148.172.205                            56  55 1ms450us
    2 159.148.172.205                            56  55 1ms513us
    sent=3 received=3 packet-loss=0% min-rtt=1ms450us avg-rtt=1ms515us max-rtt=1ms582us
```

The router resolves the name with its own [DNS](../network-management/dns) settings. When the address answers and the name does not, the connection works and the DNS configuration is at fault. A name that does not resolve fails with `failure: resolve failed`; see [Check and troubleshoot](../network-management/dns#check-and-troubleshoot) on the DNS page. In [WinBox](../management-tools/winbox) 4 and [WebFig](../management-tools/webfig), Tools > Ping sends the name to the router, which also resolves it with its DNS; WinBox 3 resolves the name on the computer it runs on.

Each row is one reply:

- `SEQ` - Number of the request the row answers.
- `HOST` - Address the reply came from: the host, or a router on the path that sent an error.
- `SIZE` - Size of the received packet in bytes.
- `TTL` - TTL of the received packet.
- `TIME` - Round-trip time.
- `STATUS` - Empty for an IPv4 reply and `echo reply` for an IPv6 reply; otherwise what went wrong.

The last line sums up the run: requests sent, replies received, the share of lost requests and the shortest, average and longest round-trip time. Without `count`, ping runs until you stop it with <kbd>Control</kbd>+<kbd>C</kbd>.

## Read the status column

| Status | Meaning |
| :-- | :-- |
| `timeout` | No reply arrived within `interval`. The host is down, it does not answer ping, a firewall on the path drops the request or the reply, or the round-trip time is longer than `interval`. |
| `net unreachable` | The router shown in `HOST` has no route to the destination network, or a firewall rule there rejects the packet with the default `reject` action. |
| `host unreachable` | The router shown in `HOST` reports that it cannot reach the host, or a firewall rule there rejects the packet with `reject-with=icmp-host-unreachable`. |
| `admin prohibited` | A firewall rule on the router shown in `HOST` rejects the packet with `reject-with=icmp-admin-prohibited`. Traceroute shows the same answer as `packet filtered`. |
| `TTL exceeded` | The TTL ran out on the router shown in `HOST`. Usually a routing loop. |
| `fragmentation needed and DF set` | The router shown in `HOST` must forward the packet over a link with a smaller MTU, and the Don't Fragment flag prevents it. |
| `packet too large and cannot be fragmented` | The packet is larger than the MTU of the outgoing interface or than the path MTU the router has learned, and the Don't Fragment flag is set. |
| `no route to host` | The router has no route to the address. For ND ping, the address is not on a directly connected subnet. |
| `echo reply` | An IPv6 echo reply. IPv4 replies leave the status empty. |

A routing loop sends packets back and forth between two routers until their TTL runs out. The first router where it runs out reports it:

```ros
/ping 198.51.100.10 count=2
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 203.0.113.1                                84  64 20ms894us  TTL exceeded
    1 203.0.113.1                                84  64 20ms404us  TTL exceeded
    sent=2 received=0 packet-loss=100%
```

## Find the path MTU

When a link on the path has a smaller maximum transmission unit (MTU) than the links around it, for example a PPPoE connection or a tunnel, small packets pass and large ones are lost: pings work, but web pages load only partly and file transfers stall. To find the largest packet that crosses the path, ping with the Don't Fragment flag. Start with 1500, or 1492 on a PPPoE connection, and lower `size` until replies arrive: the largest size that gets replies is the path MTU.

`size` is the size of the whole IP packet, including the IP header. `size=1500` is a full-size packet on an Ethernet link and matches `ping -l 1472` on Windows and `ping -s 1472` on Linux, which count only the data. For IPv6, the header is 40 bytes, so `size=1500` matches `ping -s 1452`.

```ros
/ping 198.51.100.10 size=1500 do-not-fragment count=2
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 203.0.113.6                               576  63 893us      fragmentation needed and DF set
    1                                                              packet too large and cannot be fragmented
    sent=2 received=0 packet-loss=100%
```

The router at 203.0.113.6 has the link with the smaller MTU and answers the first request with `fragmentation needed and DF set`; `SIZE` 576 is the size of that error message, not the MTU. The message tells the router the MTU of that link, and the router remembers it as the path MTU for this destination for a while: a larger ping then fails immediately with `packet too large and cannot be fragmented`, without leaving the router. The same status appears when `size` is larger than the MTU of the outgoing interface.

```ros
/ping 198.51.100.10 size=1401 do-not-fragment count=1
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0                                                              packet too large and cannot be fragmented
    sent=1 received=0 packet-loss=100%
```

```ros
/ping 198.51.100.10 size=1400 do-not-fragment count=2
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 198.51.100.10                            1400  62 1ms347us
    1 198.51.100.10                            1400  62 1ms41us
    sent=2 received=2 packet-loss=0% min-rtt=1ms41us avg-rtt=1ms194us max-rtt=1ms347us
```

1400 is the largest size that gets replies: the path MTU is 1400 bytes. Without `do-not-fragment`, a larger ping is fragmented and gets replies, so it does not show the MTU problem. When a firewall on the path drops the fragmentation needed messages, pings above the path MTU only time out.

To see which router on the path has the smaller link, run [traceroute with `do-not-fragment`](traceroute#find-the-hop-with-the-smaller-mtu). To keep TCP connections working across such a link, clamp the TCP MSS with a [mangle rule](../firewall-and-quality-of-service/firewall/mangle#change-mss).

## Ping from a specific address, interface or VRF

By default, the router picks the source address as for its other traffic: the `pref-src` of the route when it is set, otherwise the address of the outgoing interface. That is not always the address a test needs. An [IPsec](../virtual-private-networks/ipsec/) site-to-site tunnel, for example, carries only traffic between the two LANs: a ping from the router's WAN address to the remote LAN does not match the IPsec policy and does not enter the tunnel. To test the tunnel, ping from the router's LAN address:

```ros
/ping 192.168.2.10 src-address=192.168.88.1 count=3
```

`interface=` sets the interface the requests leave through. When no route through that interface covers the destination, the router treats the destination as directly connected there and sends ARP requests for it. ARP ping, ND ping to a global address and pings to IPv6 link-local addresses need `interface=`.

`vrf=` sends the ping in a [VRF](../user-guides/routing-and-networking-protocols/vrf):

```ros
/ping 10.0.0.1 vrf=customer1 count=3
```

Only VRFs are accepted. A routing table that exists for policy routing is not a VRF, and the ping is refused with `input does not match any value of vrf`. To test such a table, set `src-address` to an address that a [routing rule](../user-guides/routing-and-networking-protocols/policy-routing) sends to that table: the rules apply to the router's own pings.

## Find a host that does not answer ping

Many hosts drop ICMP echo requests, for example computers with their firewall turned on, so a working host can look like it is down:

```ros
/ping 192.168.88.20 count=2
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 192.168.88.20                                                timeout
    1 192.168.88.20                                                timeout
    sent=2 received=0 packet-loss=100%
```

A host on the same subnet as the router must still answer ARP, or it cannot receive any traffic. With `arp-ping=yes`, the router sends ARP requests instead of ICMP echo requests, and `HOST` shows the MAC address of the host that answered. ARP ping works for IPv4 addresses on a directly connected subnet and needs `interface=`, the interface that has the router's address on that subnet (`bridge` in the default configuration); without it, the ping fails with `interface needs to be specified for arp ping`.

```ros
/ping 192.168.88.20 arp-ping=yes interface=bridge count=2
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 FE:14:80:BE:47:5B                                 386us
    1 FE:14:80:BE:47:5B                                 346us
    sent=2 received=2 packet-loss=0% min-rtt=346us avg-rtt=366us max-rtt=386us
```

To find out which device has that MAC address, look it up in the [DHCP server leases](../network-management/dhcp/server#leases) or on the device's label.

For IPv6, `nd-ping=yes` does the same with Neighbor Discovery: the router sends Neighbor Solicitations (NS) instead of ICMPv6 echo requests and counts a Neighbor Advertisement (NA) as a reply. It confirms that a host is present and that Neighbor Discovery works, even when ICMPv6 echo is filtered or turned off on the host. ND ping works only for addresses on a directly connected IPv6 subnet; an address on another subnet returns a `no route to host` error. A global address needs `interface=`, otherwise the ping fails with `interface needs to be specified for ND ping`; a link-local address carries the interface in its `%interface` suffix:

```ros
/ping fe80::fc14:80ff:febe:475b%ether1 nd-ping=yes count=2
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 fe80::fc14:80ff:febe:475b                         622us
    1 fe80::fc14:80ff:febe:475b                         581us
    sent=2 received=2 packet-loss=0% min-rtt=581us avg-rtt=601us max-rtt=622us
```

```ros
/ping 2001:db8:0:1::2 nd-ping=yes interface=ether1
```

In WinBox, Tools > Ping has an ND Ping checkbox next to ARP Ping, with an interface selector.

## Discover IPv6 hosts on a link

Most IPv6 hosts answer an echo request sent to the all-nodes multicast address `ff02::1`; hosts whose firewall drops such requests do not. Ping it on an interface to list the IPv6 hosts on that link:

```ros
/ping ff02::1%ether1 count=2
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 fe80::fc89:f0ff:fe95:7d86                  56  64 395us      echo reply
    0 fe80::fc14:80ff:febe:475b                  56  64 1ms87us    echo reply
    sent=1 received=2 packet-loss=-100% min-rtt=395us avg-rtt=741us max-rtt=1ms87us
```

All hosts answer the same request, so several rows share one `SEQ`, and the list includes the router's own address on that interface. Each answer counts toward `count` and toward the summary line, which therefore shows more replies than requests.

## Ping a MAC address

MAC ping reaches a MikroTik device by its MAC address, without IP configuration, on the same layer-2 segment. The target answers when its MAC ping server is enabled, which it is by default (see [MAC server](../management-tools/mac-server)):

```ros
/tool/mac-server/ping/set enabled=yes
```

Ping the MAC address and name the interface after `%`:

```ros
/ping FE:14:80:BE:47:5B%ether1 count=2
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 FE:14:80:BE:47:5B                          70     775us
    1 FE:14:80:BE:47:5B                          70     579us
    sent=2 received=2 packet-loss=0% min-rtt=579us avg-rtt=677us max-rtt=775us
```

Without the `%interface` suffix, the router sends each request out of every interface. This adds traffic to all of them and returns duplicate replies when the target is reachable through more than one.

## Use ping in a script

In a script, ping returns the number of replies it received:

```ros
:if ([/ping 198.51.100.10 count=3] = 0) do={
    :log warning "Server 198.51.100.10 does not answer"
}
```

When the address is a name that does not resolve, ping fails with `resolve failed` and stops the script; put it in `:do { ... } on-error={ ... }` to handle that case. To run the check regularly, add the script to the [scheduler](../system-information-and-utilities/scheduler).

With `as-value`, ping returns one entry per reply, with the `host`, `seq`, `size`, `ttl` and `time` of the reply, or its `status` when it failed. To watch a host continuously and run scripts when it goes down or comes back, use [Netwatch](netwatch) instead of a scheduled ping.

## Technical details

### Packet size

`size` sets the size of the whole packet, IP header included: 28 to 65535 bytes for IPv4 and 48 to 65535 bytes for IPv6 (a smaller IPv6 size fails with `packet size is too small`), 56 by default. A packet larger than the MTU of the outgoing interface is fragmented, unless `do-not-fragment` is set. The `SIZE` column shows the size of the received packet, which for an error message from a router is the size of that message (576 and 84 in the examples on this page).

### Interval and count

The router sends one request per `interval`, 10 ms to 5 s, 1 s by default. A reply that arrives later than `interval` counts as a timeout, so on links with long round-trip times, such as satellite or congested mobile links, raise `interval` above the round-trip time. Without `count`, it sends requests until you stop it.

### TTL and hop limit

`ttl` sets the TTL of IPv4 requests and the hop limit of IPv6 requests, 1 to 255. Without it, IPv4 requests leave with TTL 255 and IPv6 requests with hop limit 64.

### DSCP

`dscp` sets the Differentiated Services Code Point in the IP header of the requests, 0 to 63. `dscp=46` (Expedited Forwarding) gives a ToS byte of `0xb8`. Use it to check how the path treats traffic of a QoS class.

### Link-local addresses

An IPv6 link-local address (`fe80::/10`) exists on every link, so it needs the interface as a suffix: `fe80::1%ether1`.

For all parameters, see the [`/tool/ping` CLI reference](../cli-reference/tool/ping).
