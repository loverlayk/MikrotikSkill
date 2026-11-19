# tracking

> Settings and state of connection tracking. See Connection tracking.

-----------

## ip/firewall/connection/tracking 
**Type:** Settings Directory

Settings and state of connection tracking. See [Connection tracking](../../../../firewall-and-quality-of-service/connection-tracking).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="enum (auto | yes | no) { auto:0, yes:1, no:2 }">
Whether connection tracking works.
- `auto` (default) - Connection tracking is off until the router has an enabled filter, mangle or NAT rule, separately for IPv4 and IPv6. RAW rules alone do not start it.
- `yes` - Connection tracking works for IPv4 and IPv6, also without firewall rules.
- `no` - Connection tracking is off. Firewall rules that need it, such as rules with `connection-state` and the masquerade rule, get the `I` flag and match no packets.
</ArgTableRow>
<ArgTableRow arg="tcp-syn-sent-timeout" typ="time">Timeout of a TCP connection for which the router has seen the first SYN packet and no reply. Default: 5s.</ArgTableRow>
<ArgTableRow arg="tcp-syn-received-timeout" typ="time">Timeout of a TCP connection after the reply to the first SYN packet, until the handshake is complete. Default: 5s.</ArgTableRow>
<ArgTableRow arg="tcp-established-timeout" typ="time">Timeout of an established TCP connection that is idle. Default: 1d.</ArgTableRow>
<ArgTableRow arg="tcp-fin-wait-timeout" typ="time">Timeout of a TCP connection after the first FIN packet. Default: 10s.</ArgTableRow>
<ArgTableRow arg="tcp-close-wait-timeout" typ="time">Timeout of a TCP connection in the `close-wait` state, while it is closing. Default: 10s.</ArgTableRow>
<ArgTableRow arg="tcp-last-ack-timeout" typ="time">Timeout of a TCP connection in the `last-ack` state, while it is closing. Default: 10s.</ArgTableRow>
<ArgTableRow arg="tcp-time-wait-timeout" typ="time">Timeout of a TCP connection in the `time-wait` state, after both sides have closed it. Default: 10s.</ArgTableRow>
<ArgTableRow arg="tcp-close-timeout" typ="time">Timeout of a TCP connection in the `close` state. Default: 10s.</ArgTableRow>
<ArgTableRow arg="tcp-max-retrans-timeout" typ="time">Timeout of a TCP connection in which packets are retransmitted and not acknowledged. Default: 5m.</ArgTableRow>
<ArgTableRow arg="tcp-unacked-timeout" typ="time">Timeout of an established TCP connection while sent data is not yet acknowledged. Default: 5m.</ArgTableRow>
<ArgTableRow arg="loose-tcp-tracking" typ="bool">
What the router does with a packet from the middle of a TCP connection that matches no entry of the connection list.
- `yes` (default) - The router creates an entry from the packet, and the connection continues.
- `no` - The packet is invalid.
</ArgTableRow>
<ArgTableRow arg="liberal-tcp-tracking" typ="bool">Whether TCP tracking is liberal (the kernel parameter `nf_conntrack_tcp_be_liberal`). With `no`, a TCP segment outside the window of its connection makes the packet `invalid`. With `yes`, the router accepts out-of-window segments. This can let through malformed packets that the `connection-state=invalid` matcher would otherwise catch, and increases the exposure to certain evasion techniques. Enable it only to troubleshoot or to work around a known issue. Default: no.</ArgTableRow>
<ArgTableRow arg="udp-timeout" typ="time">Timeout of a UDP connection that is not a stream: it has seen packets in one direction, or a single request and reply. Default: 30s.</ArgTableRow>
<ArgTableRow arg="udp-stream-timeout" typ="time">Timeout of a UDP connection with packets flowing in both directions. Such an entry has the `A` (assured) flag. Default: 3m.</ArgTableRow>
<ArgTableRow arg="icmp-timeout" typ="time">Timeout of an ICMP connection, for example a ping. Default: 10s.</ArgTableRow>
<ArgTableRow arg="generic-timeout" typ="time">Timeout of connections of the protocols that connection tracking has no own timeout for, for example IPIP. Default: 10m.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="active-ipv4" typ="bool">Whether connection tracking works for IPv4 at the moment.</ArgTableRow>
<ArgTableRow arg="active-ipv6" typ="bool">Whether connection tracking works for IPv6 at the moment.</ArgTableRow>
<ArgTableRow arg="max-entries" typ="num">Number of entries that the connection list can hold. It depends on the amount of RAM. The router does not create a list of the maximum size when it starts: the list grows when needed while free RAM is available, up to 1048576 entries.</ArgTableRow>
<ArgTableRow arg="total-entries" typ="num">Number of connections in the list, IPv4 and IPv6 together.</ArgTableRow>
<ArgTableRow arg="total-ip4-entries" typ="num">Number of IPv4 connections in the list.</ArgTableRow>
<ArgTableRow arg="total-ip6-entries" typ="num">Number of IPv6 connections in the list.</ArgTableRow>
</ArgTable>
