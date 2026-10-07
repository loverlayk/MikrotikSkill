# traceroute

> Traces the path to a host: sends probes with a growing TTL and lists the routers that answer, with loss and round-trip statistics for each hop. The trace repeats every second until you stop it, until count rounds are...

-----------

## tool/traceroute 
**Type:** Command

Traces the path to a host: sends probes with a growing TTL and lists the routers that answer, with loss and round-trip statistics for each hop. The trace repeats every second until you stop it, until `count` rounds are done or until `duration` ends. For examples and how to read the results, see [Traceroute](../../diagnostics-monitoring-and-troubleshooting/traceroute).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="address (flags=46viD)">IP or IPv6 address, or DNS name, of the destination. A name is resolved by the router's DNS resolver. See [address flags](../../cli-reference/#address-flags).</ArgTableRow>
<ArgTableRow arg="port" typ="num">Destination UDP port of the probes with `protocol=udp`. Every probe uses the same port. Default: 33434.</ArgTableRow>
<ArgTableRow arg="size" typ="num">Size of each probe as a whole IP packet, in bytes, including the IP header. Default: 28, which is an IPv4 probe without payload.</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">DSCP value set in the IP header of the probes.</ArgTableRow>
<ArgTableRow arg="do-not-fragment" typ="switch">Sets the Don't Fragment flag in the IP header of the probes. With a large `size`, the router with a smaller link on the path answers with `fragmentation needed from <address>`.</ArgTableRow>
<ArgTableRow arg="use-dns" typ="bool">Show the host names of the hops instead of their addresses. The names are looked up with reverse DNS queries through the router's DNS resolver; a hop without a reverse DNS record keeps its address. Default: no.</ArgTableRow>
<ArgTableRow arg="count" typ="num">Number of rounds to run. Without `count`, the trace repeats every second until you stop it. Default: unlimited.</ArgTableRow>
<ArgTableRow arg="max-hops" typ="num">Highest TTL to try: when the destination does not answer, the round ends after this many hops. Default: 30.</ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (icmp | udp)">
Type of the probes.
- `icmp` (default) - ICMP echo requests. The destination answers with an echo reply.
- `udp` - UDP datagrams to `port`. The destination answers with an ICMP port unreachable message.
</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ipv6-address: ip6Addr
, ip-address: ipAddr
 }">Source address of the probes. Routing rules that match the source address apply to the probes. Default: the `pref-src` of the route, otherwise the address of the outgoing interface.</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">How long each probe waits for its answer before the next probe is sent. Default: 1s.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">VRF whose routing table the probes use. Only VRFs are accepted; a routing table created for policy routing is refused. Default: main.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">Interface to send the probes out of. When no route through the interface covers the destination, the router treats the destination as directly connected there and sends ARP requests for it.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="object { address: alt { name: string
, address: ip6Addr
 }
 }">Address of the router that answered for this hop, or its host name with `use-dns=yes`. Empty when no probe to the hop got an answer.</ArgTableRow>
<ArgTableRow arg="loss" typ="num">Percentage of the probes to this hop that got no answer.</ArgTableRow>
<ArgTableRow arg="sent" typ="num">Number of probes sent to this hop.</ArgTableRow>
<ArgTableRow arg="last" typ="num">Round-trip time of the last answer from this hop. The printed table shows `timeout` when the last probe got no answer.</ArgTableRow>
<ArgTableRow arg="avg" typ="num">Average round-trip time of the answers from this hop.</ArgTableRow>
<ArgTableRow arg="best" typ="num">Shortest round-trip time of the answers from this hop.</ArgTableRow>
<ArgTableRow arg="worst" typ="num">Longest round-trip time of the answers from this hop.</ArgTableRow>
<ArgTableRow arg="std-dev" typ="num">Standard deviation of the round-trip times of this hop: how much they vary from round to round.</ArgTableRow>
<ArgTableRow arg="status" typ="string">Error the hop answered with instead of time exceeded, for example `network unreachable from 203.0.113.1` (no route, or a firewall `reject` with the default message), `host unreachable from 203.0.113.1`, `packet filtered from 203.0.113.1` (a firewall rejects the probe as administratively prohibited) or `fragmentation needed from 203.0.113.6` (with `do-not-fragment`, the probe is larger than the next link's MTU). The round ends at such a hop. Empty when the hop answers normally.</ArgTableRow>
<ArgTableRow arg="error" typ="string"></ArgTableRow>
</ArgTable>
