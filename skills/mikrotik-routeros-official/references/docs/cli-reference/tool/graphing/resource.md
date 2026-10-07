# resource

> Rules for the graphs of the CPU, memory and disk usage (/graphs/cpu/, /graphs/ram/ and /graphs/hdd/ on the router's web page) and which clients can see them. Nothing is graphed until you add a rule. You can add...

-----------

## tool/graphing/resource 
**Type:** Directory

Rules for the graphs of the CPU, memory and disk usage (`/graphs/cpu/`, `/graphs/ram/` and `/graphs/hdd/` on the router's web page) and which clients can see them. Nothing is graphed until you add a rule. You can add several rules, each with its own `allow-address`; a client sees the graphs when any of them allows its address. A resource rule does not open the interface or queue graphs. See [Graphing](../../../diagnostics-monitoring-and-troubleshooting/graphing).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Disabled rule: its graphs are not shown.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="allow-address" typ="alt { ip-prefix: ipPrefix
, ipv6-prefix: ip6Prefix
 }">The IPv4 or IPv6 prefix of the clients that can see the CPU, memory and disk graphs on the router's `/graphs/` web page. The pages need no login. A change applies immediately. To allow several prefixes, add a rule for each. Default: 0.0.0.0/0 (every IPv4 address).</ArgTableRow>
<ArgTableRow arg="store-on-disk" typ="bool">
- `yes` (default) - Keep the collected data in the system storage: the graphs survive a reboot. The data is written every [`store-every`](.).
- `no` - Keep the data in RAM only: the graphs start empty after a reboot.
</ArgTableRow>
</ArgTable>
