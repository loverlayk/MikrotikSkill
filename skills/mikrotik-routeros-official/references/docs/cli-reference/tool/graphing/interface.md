# interface

> Rules that choose which interfaces are graphed and which clients can see their traffic graphs on the router's /graphs/ web page (/graphs/iface//). Nothing is graphed until you add a rule. You can add several rules...

-----------

## tool/graphing/interface 
**Type:** Directory

Rules that choose which interfaces are graphed and which clients can see their traffic graphs on the router's `/graphs/` web page (`/graphs/iface/<interface>/`). Nothing is graphed until you add a rule. You can add several rules for one interface, each with its own `allow-address`; a client sees the graph when any of them allows its address. An interface rule does not open the resource or queue graphs. The graphs show `In` for traffic received on the interface and `Out` for traffic sent, in bits per second. See [Graphing](../../../diagnostics-monitoring-and-troubleshooting/graphing).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Disabled rule: its graphs are not shown.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum { all:0 }">The interface to graph. `all` graphs every interface, also disabled interfaces, the loopback interface `lo` and dynamic interfaces such as PPPoE users while they exist. A rule for one dynamic interface loses it when the interface is created again, for example when a PPPoE user reconnects (the rule then shows an ID such as `*F00000`); graph a static PPPoE server binding instead. The interface of an existing rule cannot be changed (`Can't change interface, please create new config`): remove the rule and add a new one. Default: all.</ArgTableRow>
<ArgTableRow arg="allow-address" typ="alt { ip-prefix: ipPrefix
, ipv6-prefix: ip6Prefix
 }">The IPv4 or IPv6 prefix of the clients that can see this interface's graphs on the router's `/graphs/` web page. The pages need no login. A change applies immediately. To allow several prefixes, add a rule for each. Default: 0.0.0.0/0 (every IPv4 address).</ArgTableRow>
<ArgTableRow arg="store-on-disk" typ="bool">
- `yes` (default) - Keep the collected data in the system storage: the graphs survive a reboot. The data is written every [`store-every`](.).
- `no` - Keep the data in RAM only: the graphs start empty after a reboot.
</ArgTableRow>
</ArgTable>
