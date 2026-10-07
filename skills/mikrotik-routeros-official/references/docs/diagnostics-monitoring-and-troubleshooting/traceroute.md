# Traceroute

> The RouterOS traceroute tool: list the routers on the path to a host, read the per-hop loss and round-trip statistics, find where a path breaks, loops or is filtered, and trace from a VRF or a chosen source address.

# Traceroute

Traceroute lists the routers that packets pass on their way to a remote host, and shows for each of them how many probes it answered and how long the answers took. Use it to find where a connection fails or slows down: in your own network, at the ISP gateway or further away. To test only whether one host answers, use [ping](ping).

Traceroute relies on the time to live (TTL) field in the IP header, which prevents routing loops: every router decrements the TTL of a packet it forwards, and when the TTL reaches zero, the router discards the packet and sends an ICMP time exceeded message back to the sender. Traceroute sends its first probe with TTL 1, so the first router on the path answers; the next probe has TTL 2 and reaches the second router, and so on, until the probe reaches the destination, which answers the probe itself.

RouterOS sends ICMP echo requests as probes, up to 30 hops away. When a round is done, it starts the next one, at most once a second, and keeps statistics for each hop, like the `mtr` tool, until you stop it with <kbd>Control</kbd>+<kbd>C</kbd>, or until it has done `count` rounds or run for `duration`. Other systems have similar tools: `traceroute` or `tracepath` on Unix-like systems and `tracert` on Windows.

## Trace the path to a host

To trace the path to a server, with three rounds of probes:

```ros
/tool/traceroute 198.51.100.10 count=3
```

```text
Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV
#  ADDRESS        LOSS  SENT  LAST   AVG  BEST  WORST  STD-DEV
0  203.0.113.1    0%       3  0.3ms  0.4  0.3   0.4          0
1  203.0.113.6    0%       3  0.4ms  0.4  0.4   0.4          0
2  198.51.100.10  0%       3  0.5ms  0.5  0.5   0.5          0
```

The packets pass two routers, 203.0.113.1 and 203.0.113.6, before they reach the server. The `#` column starts at 0, so row 0 is the first hop. The table updates in place after every round. The columns are:

- `ADDRESS` - The address of the router that answered for this hop: the address it sends its answer from, usually the address of its interface towards you.
- `LOSS` - The share of the probes to this hop that got no answer.
- `SENT` - The number of probes sent to this hop.
- `LAST`, `AVG`, `BEST`, `WORST` - The round-trip time of the last answer, and the average, shortest and longest round-trip time, in milliseconds. `LAST` shows `timeout` when the last probe got no answer.
- `STD-DEV` - The standard deviation of the round-trip times, in milliseconds: how much they vary from round to round.
- `STATUS` - Shown when a hop answers with an error instead of time exceeded, for example because a firewall rejects the traffic.

## Show host names

With `use-dns=yes`, traceroute shows the host name of each hop instead of its address. The router looks the names up with reverse DNS queries through its own [DNS resolver](../network-management/dns), so a hop without a reverse DNS record keeps its address. The destination can also be a host name:

```ros
/tool/traceroute server.example.com count=3 use-dns=yes
```

```text
Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV
#  ADDRESS                 LOSS  SENT  LAST   AVG  BEST  WORST  STD-DEV
0  edge1.isp.example.net.  0%       3  0.4ms  0.5  0.4   0.5    0
1  core1.isp.example.net.  0%       3  0.4ms  0.5  0.4   0.6    0.1
2  server.example.com.     0%       3  0.6ms  0.6  0.5   0.7    0.1
```

Names can show which network or location a router belongs to.

## Find where the path breaks

When a host does not answer, traceroute shows how far the packets get. Each of the following outputs shows one typical result.

### Hops stop answering

```ros
/tool/traceroute 198.51.100.10 count=1 max-hops=4
```

```text
Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV
#  ADDRESS      LOSS  SENT  LAST     AVG  BEST  WORST  STD-DEV
0  203.0.113.1  0%       1  0.4ms    0.4  0.4   0.4          0
1               100%     1  timeout
2               100%     1  timeout
3               100%     1  timeout
```

The first router answers, and nothing after it does. The problem is after the last hop that answers: a link that is down, a missing route, a missing route back to your address (for example when you trace with `src-address` set to a LAN address that the remote network does not route back), or a firewall that drops the packets without an answer. Check the router 203.0.113.1: its route to the destination and the link to its next hop. Without `max-hops`, the trace continues with timeouts up to 30 hops.

The same output appears when every router on the path answers but the destination itself drops ICMP echo requests: the rows after the last router stay empty. [Ping](ping) the destination, or use [ARP ping](ping#find-a-host-that-does-not-answer-ping) when it is on a directly connected subnet.

### A router rejects the traffic

```ros
/tool/traceroute 198.51.100.10 count=1
```

```text
Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV, STATUS
#  ADDRESS      LOSS  SENT  LAST   AVG  BEST  WORST  STD-DEV  STATUS
0  203.0.113.1  0%       1  0.4ms  0.4  0.4   0.4          0
1  203.0.113.1  0%       1  0.3ms  0.3  0.3   0.3          0  host unreachable from 203.0.113.1
2               0%       0  0ms
```

The router 203.0.113.1 answers the second probe with an error instead of forwarding it, and the trace ends there; the empty row after it is the hop the probes did not reach. `host unreachable from 203.0.113.1` means that the router cannot deliver the packet to the host; a firewall rule that rejects packets with `reject-with=icmp-host-unreachable` gives the same answer. `network unreachable from 203.0.113.1` means that the router has no route to the destination network, or that a firewall rule rejects the packet with the default `reject` action. `packet filtered from 203.0.113.1` means that a firewall on the router rejects the packet as administratively prohibited (`reject-with=icmp-admin-prohibited`); [ping](ping) shows the same answer as `admin prohibited`.

### The same routers repeat

```ros
/tool/traceroute 198.51.100.10 count=1 max-hops=8
```

```text
Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV
#  ADDRESS      LOSS  SENT  LAST   AVG  BEST  WORST  STD-DEV
0  203.0.113.1  0%       1  0.4ms  0.4  0.4   0.4          0
1  203.0.113.6  0%       1  0.4ms  0.4  0.4   0.4          0
2  203.0.113.1  0%       1  0.4ms  0.4  0.4   0.4          0
3  203.0.113.6  0%       1  0.6ms  0.6  0.6   0.6          0
4  203.0.113.1  0%       1  0.5ms  0.5  0.5   0.5          0
5  203.0.113.6  0%       1  0.6ms  0.6  0.6   0.6          0
6  203.0.113.1  0%       1  0.7ms  0.7  0.7   0.7          0
7  203.0.113.6  0%       1  0.8ms  0.8  0.8   0.8          0
```

Two routers alternate: a routing loop. Each of them routes the destination to the other, so the packets go back and forth until their TTL runs out. Check the routes to the destination on both routers. A [ping](ping) to the destination then reports `TTL exceeded` from one of the routers instead of a reply.

The router 203.0.113.1 receives the looping packets from 203.0.113.6 on a different interface than the probes that come from you, but it answers every time from its address towards you.

### One hop shows loss, later hops do not

```ros
/tool/traceroute 198.51.100.10 count=10
```

```text
Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV
#  ADDRESS        LOSS  SENT  LAST     AVG  BEST  WORST  STD-DEV
0  203.0.113.1    0%      10  0.2ms    0.2  0.2   0.4    0.1
1  203.0.113.6    90%     10  timeout  0.4  0.4   0.4    0
2  198.51.100.10  0%      10  0.8ms    0.8  0.5   0.8    0.1
```

The router 203.0.113.6 answered only one probe of ten, but every probe to the server, which passes through the same router, got an answer. Many routers limit how often they send time exceeded messages, or give them a low priority, so loss that does not continue to the later hops is not packet loss on the path. Real packet loss starts at one hop and shows on every hop after it. A router that never sends time exceeded messages shows as a hop with 100% loss and no address between hops that answer.

### Round-trip times grow

The round-trip time of a hop includes the way back from that router to you. A time that rises at one hop and stays higher at every later hop points to a slow, long or congested link before that hop. A high time or a large `STD-DEV` at one hop only, with normal times after it, means that this router is slow to answer, not that traffic through it is slow.

## Find the hop with the smaller MTU

With `do-not-fragment` and a large `size`, the probes cannot be fragmented, and the router that must forward them over a link with a smaller MTU answers with an error instead:

```ros
/tool/traceroute 198.51.100.10 size=1500 do-not-fragment count=1
```

```text
Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV, STATUS
#  ADDRESS      LOSS  SENT  LAST   AVG  BEST  WORST  STD-DEV  STATUS
0  203.0.113.1  0%       1  0.5ms  0.5  0.5   0.5          0
1  203.0.113.6  0%       1  0.6ms  0.6  0.6   0.6          0
2  203.0.113.6  0%       1  0.6ms  0.6  0.6   0.6          0  fragmentation needed from 203.0.113.6
3               0%       0  0ms
```

The router 203.0.113.6 has the smaller link. To find the MTU of the path, see [Find the path MTU](ping#find-the-path-mtu) on the ping page.

## Trace from a VRF or a specific source

By default, traceroute sends the probes by the main routing table, from the address of the outgoing interface. On a provider router, a customer's network is often in a [VRF](../user-guides/routing-and-networking-protocols/vrf); `vrf` traces the path the customer's traffic takes:

```ros
/tool/traceroute 198.51.100.10 vrf=customer1
```

`vrf` accepts only VRFs. A routing table created for policy routing is not a VRF, and the command refuses it.

To trace the path as traffic from a particular network sees it, for example from the LAN address instead of the WAN address, set the source address of the probes. [Routing rules](../user-guides/routing-and-networking-protocols/policy-routing) that match the source address apply to the probes too, so `src-address` also traces the path of a policy-routing table:

```ros
/tool/traceroute 198.51.100.10 src-address=192.168.88.1
```

`interface` sends the probes out of one interface. When no route through that interface covers the destination, the router treats the destination as directly connected there and sends ARP requests for it, so the trace only times out.

## Technical details

### Probes

- The probes are ICMP echo requests. `size` is the size of the whole IP packet: the default of 28 bytes is an IPv4 header and an ICMP header without any payload.
- The first probe of a round has TTL 1, and each next probe one more. A probe waits up to `timeout`, 1 second by default, for its answer; the next probe is sent as soon as the answer arrives or the timeout expires.
- A round ends when the destination answers, when a router answers with a destination unreachable message, or after `max-hops` probes, 30 by default. The next round starts when the round is done, at the earliest one second after the previous round started.
- With `protocol=udp`, the probes are UDP datagrams to `port`, 33434 by default. The destination port is the same for every probe; the source port changes from hop to hop. The destination answers with an ICMP port unreachable message instead of an echo reply.

### Host names in WinBox and WebFig

When you enter a host name in Tools > Traceroute in WinBox 4 or in WebFig, the router resolves the name with its own [DNS resolver](../network-management/dns). WinBox 3 resolves the name on the computer it runs on.

For all parameters, see [`/tool/traceroute`](../cli-reference/tool/traceroute) in the CLI reference.
