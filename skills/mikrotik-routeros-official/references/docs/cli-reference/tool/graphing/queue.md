# queue

> Rules that choose which simple queues are graphed and which clients can see their traffic graphs on the router's /graphs/ web page (/graphs/queue//, with the name URL-encoded). Nothing is graphed until you add a...

-----------

## tool/graphing/queue 
**Type:** Directory

Rules that choose which simple queues are graphed and which clients can see their traffic graphs on the router's `/graphs/` web page (`/graphs/queue/<queue>/`, with the name URL-encoded). Nothing is graphed until you add a rule. A client sees a queue's graph when a rule for the queue allows its address, or, with `allow-target=yes`, when its address is in the queue's `target`. A queue rule does not open the interface or resource graphs. The graphs show `In` for traffic to the target (download) and `Out` for traffic from it (upload), also as a share of the queue's `max-limit`. See [Graphing](../../../diagnostics-monitoring-and-troubleshooting/graphing).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Disabled rule: its graphs are not shown.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="simple-queue" typ="enum (all) { all:0 }">The simple queue to graph, by name. `all` graphs every simple queue, also the queues added later and the dynamic queues of PPP users. The queue of an existing rule cannot be changed (`Can't change queue, please create new config`): remove the rule and add a new one. Default: all.</ArgTableRow>
<ArgTableRow arg="allow-address" typ="alt { ip-prefix: ipPrefix
, ipv6-prefix: ip6Prefix
 }">The IPv4 or IPv6 prefix of the clients that can see the graphs of this rule's queues on the router's `/graphs/` web page. The pages need no login. A change applies immediately. To allow several prefixes, add a rule for each. Default: 0.0.0.0/0 (every IPv4 address).</ArgTableRow>
<ArgTableRow arg="store-on-disk" typ="bool">
- `yes` (default) - Keep the collected data in the system storage: the graphs survive a reboot. The data is written every [`store-every`](.).
- `no` - Keep the data in RAM only: the graphs start empty after a reboot.
</ArgTableRow>
<ArgTableRow arg="allow-target" typ="bool">
Whether the addresses in a queue's `target` can also see that queue's graph, so that each customer of a simple queue sees their own traffic. A client sees a graph when any rule allows it, so another rule with `no` does not hide a graph that this rule shows.
- `yes` (default) - Every address in the target sees the graph, in addition to `allow-address`. A queue with a subnet target shows its graph to the whole subnet; a queue whose target is 0.0.0.0/0 or an interface, such as the dynamic queue of a PPP user, shows it to every client that reaches the web server.
- `no` - Only `allow-address` sees the graph.
</ArgTableRow>
</ArgTable>
