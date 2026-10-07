# ping

> Sends ICMP echo requests (IPv4) or ICMPv6 echo requests (IPv6) to a host and shows each reply with its round-trip time, TTL and status, then a summary. /ping is the short form of /tool/ping. With arp-ping or nd-ping,...

-----------

## tool/ping 
**Type:** Command

Sends ICMP echo requests (IPv4) or ICMPv6 echo requests (IPv6) to a host and shows each reply with its round-trip time, TTL and status, then a summary. `/ping` is the short form of `/tool/ping`. With `arp-ping` or `nd-ping`, the router sends ARP requests or IPv6 Neighbor Solicitations instead; with a MAC address as `address`, it sends MAC pings. In a script, the command returns the number of replies. See [Ping](../../diagnostics-monitoring-and-troubleshooting/ping) for the full documentation.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="address (flags=46v%Dm)">Host to ping: an IPv4 or IPv6 address, a DNS name, or a MAC address for MAC ping. The router resolves a name with its own DNS settings. An IPv6 link-local address and a MAC address take the interface as a suffix, for example `fe80::1%ether1` or `00:11:22:33:44:55%ether1`; a MAC ping without the suffix goes out of every interface. See [address flags](../../cli-reference/#address-flags).</ArgTableRow>
<ArgTableRow arg="interval" typ="time">Time between two requests, `00:00:00.010..00:00:05` (10 ms to 5 s). A reply that arrives later than the interval counts as a timeout. Default: 1s.</ArgTableRow>
<ArgTableRow arg="size" typ="num">Size of each request in bytes, as the whole IP packet including the IP header, `28..65535` for IPv4 and `48..65535` for IPv6. `size=1500` is a full-size packet on an Ethernet link. A request larger than the MTU of the outgoing interface is fragmented, unless `do-not-fragment` is set. Default: 56.</ArgTableRow>
<ArgTableRow arg="ttl" typ="num">TTL of IPv4 requests and hop limit of IPv6 requests, `1..255`. Default: 255 for IPv4, 64 for IPv6.</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">Differentiated Services Code Point set in the IP header of the requests, `0..63`. For example, `dscp=46` (Expedited Forwarding) gives a ToS byte of `0xb8`. Default: 0.</ArgTableRow>
<ArgTableRow arg="do-not-fragment" typ="switch">Sets the Don't Fragment flag in the requests, so that they are not fragmented. A request larger than the path MTU then fails: a router with a smaller link on the path answers with the status `fragmentation needed and DF set`, and a request larger than the MTU of the outgoing interface, or than the path MTU the router has learned, fails with `packet too large and cannot be fragmented`. Use it with `size` to find the path MTU.</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip-src-address: ipAddr
, ip6-src-address: ip6Addr
 }">Source address of the requests. Use it when the test needs a particular address, for example the LAN address to test an IPsec site-to-site tunnel. Default: the `pref-src` of the route, otherwise the address of the outgoing interface.</ArgTableRow>
<ArgTableRow arg="arp-ping" typ="bool">Send ARP requests instead of ICMP echo requests, to reach a host on a directly connected IPv4 subnet that drops ICMP. Needs `interface`; without it the command fails with `interface needs to be specified for arp ping`. `host` shows the MAC address of the host that answered. Default: no.</ArgTableRow>
<ArgTableRow arg="count" typ="num">Number of requests to send. Without it, ping runs until you stop it with Ctrl-C. In a script, the command returns the number of replies. Default: unlimited.</ArgTableRow>
<ArgTableRow arg="nd-ping" typ="bool">Use IPv6 Neighbor Discovery instead of ICMPv6 echo: the router sends Neighbor Solicitations (NS) and counts a Neighbor Advertisement (NA) as a reply. Works only for on-link IPv6 addresses; a global address also needs `interface`. Default: no.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">Interface the requests leave through. When no route through the interface covers the destination, the router treats the destination as directly connected there and sends ARP requests for it. Needed for `arp-ping`, for `nd-ping` to a global address and for IPv6 link-local addresses (or give the interface as the address suffix).</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">VRF the ping runs in. Only VRFs are accepted; a routing table that exists for policy routing is refused with `input does not match any value of vrf`. Default: main.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="seq" typ="num">Number of the request the row answers. Replies to a multicast request share one number.</ArgTableRow>
<ArgTableRow arg="host" typ="alt { ipv6-address: ip6Addr
, mac-address: macAddr
, ip-address: ipAddr
 }">Address the reply came from: the host, or a router on the path that sent an ICMP error (see `status`). For ARP ping and MAC ping, the MAC address of the host that answered.</ArgTableRow>
<ArgTableRow arg="size" typ="num">Size of the received packet in bytes. For an ICMP error from a router, the size of that message.</ArgTableRow>
<ArgTableRow arg="ttl" typ="num">TTL (IPv4) or hop limit (IPv6) of the received packet. The difference from the value the sender used shows roughly how many routers the reply crossed.</ArgTableRow>
<ArgTableRow arg="time" typ="time">Round-trip time: the time between sending the request and receiving the reply.</ArgTableRow>
<ArgTableRow arg="status" typ="string">
Empty for an IPv4 reply, otherwise what happened to the request:
- `timeout` - No reply arrived within `interval`.
- `net unreachable` - The router in `host` has no route to the destination network, or a firewall rule there rejects the packet with the default `reject` action.
- `host unreachable` - The router in `host` reports that it cannot reach the host, or a firewall rule there rejects the packet with `icmp-host-unreachable`.
- `admin prohibited` - A firewall rule on the router in `host` rejects the packet.
- `TTL exceeded` - The TTL ran out on the router in `host`, usually because of a routing loop.
- `fragmentation needed and DF set` - The router in `host` has a link with a smaller MTU, and `do-not-fragment` is set.
- `packet too large and cannot be fragmented` - The request is larger than the MTU of the outgoing interface or than the learned path MTU, and `do-not-fragment` is set.
- `no route to host` - The router has no route to the address; for `nd-ping`, the address is not on a directly connected subnet.
- `echo reply` - An IPv6 echo reply.
</ArgTableRow>
<ArgTableRow arg="sent" typ="num">Number of requests sent.</ArgTableRow>
<ArgTableRow arg="received" typ="num">Number of replies received.</ArgTableRow>
<ArgTableRow arg="packet-loss" typ="num">Share of requests without a reply, in percent.</ArgTableRow>
<ArgTableRow arg="min-rtt" typ="time">Shortest round-trip time of the run.</ArgTableRow>
<ArgTableRow arg="avg-rtt" typ="time">Average round-trip time of the run.</ArgTableRow>
<ArgTableRow arg="max-rtt" typ="time">Longest round-trip time of the run.</ArgTableRow>
</ArgTable>
