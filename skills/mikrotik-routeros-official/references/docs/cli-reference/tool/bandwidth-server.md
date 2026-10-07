# bandwidth-server

> Settings of the bandwidth test server, which answers tests that other RouterOS devices start with /tool/bandwidth-test and /tool/speed-test. The server listens on TCP port 2000 (the btest entry in /ip/service) and...

-----------

## tool/bandwidth-server 
**Type:** Settings Directory

Settings of the bandwidth test server, which answers tests that other RouterOS devices start with [`/tool/bandwidth-test`](../bandwidth-test) and [`/tool/speed-test`](../speed-test). The server listens on TCP port 2000 (the `btest` entry in `/ip/service`) and sends and receives the test data on UDP ports from `allocate-udp-ports-from` upward. Running tests are listed in [`session`](session). It works only when the `bandwidth-test` device mode is on (see [Device mode](../../../system-information-and-utilities/device-mode)). See [Bandwidth test](../../../diagnostics-monitoring-and-troubleshooting/bandwidth-test).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool">Whether the server answers tests. Default: yes.</ArgTableRow>
<ArgTableRow arg="authenticate" typ="bool">Whether clients must log in with a user whose group has the `test` and `winbox` policies (see [`/user/group`](../../user/group)). With `no`, anyone who reaches TCP port 2000 can run tests that load the router and its links; do not turn it off on a router reachable from the internet. Default: yes.</ArgTableRow>
<ArgTableRow arg="allocate-udp-ports-from" typ="num">Beginning of UDP port range. The server and the client take the UDP ports for test data from this port upward, for example 2192 on the server and 2448 to 2467 for a client's 20 streams; firewalls must allow UDP to these ports in both directions. Range `1000..64000`. Default: 2000.</ArgTableRow>
<ArgTableRow arg="max-sessions" typ="num">Maximal simultaneous test count. Tests are counted, not their connections. When this many tests run, a new test gets `can not connect`. A single test cannot use more connections than this value either: with `max-sessions=1`, only a test with `connection-count=1` runs. Range `1..1000`. Default: 100.</ArgTableRow>
<ArgTableRow arg="allowed-addresses4" typ="object { address: ipPrefix
 }">IPv4 addresses or prefixes of the clients allowed to run tests. Empty allows every client. A client outside the list gets `can not connect`. Use this list to limit clients: a user's own `address` setting does not limit bandwidth test logins. Default: empty.</ArgTableRow>
<ArgTableRow arg="allowed-addresses6" typ="object { address: ip6Prefix
 }">IPv6 addresses or prefixes of the clients allowed to run tests, the same as `allowed-addresses4`. Default: empty.</ArgTableRow>
</ArgTable>
