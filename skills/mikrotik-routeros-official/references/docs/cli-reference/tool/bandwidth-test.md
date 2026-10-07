# bandwidth-test

> Runs a bandwidth test against the bandwidth test server of another RouterOS device (/tool/bandwidth-server) and prints the results every second until duration ends or you stop it. The test sends TCP or UDP traffic in...

-----------

## tool/bandwidth-test 
**Type:** Command

Runs a bandwidth test against the bandwidth test server of another RouterOS device ([`/tool/bandwidth-server`](bandwidth-server/)) and prints the results every second until `duration` ends or you stop it. The test sends TCP or UDP traffic in one or both directions; the server must be enabled, reachable on TCP port 2000 and UDP ports from its `allocate-udp-ports-from`, and the `bandwidth-test` device mode must be on (see [Device mode](../../system-information-and-utilities/device-mode)). The server lists running tests in [`/tool/bandwidth-server/session`](bandwidth-server/session). To measure latency and both directions of TCP and UDP in one run, use [`/tool/speed-test`](speed-test). See [Bandwidth test](../../diagnostics-monitoring-and-troubleshooting/bandwidth-test).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="address (flags=46viD)">IPv4 or IPv6 address of the server. A link-local IPv6 address needs the interface, for example `fe80::1%ether1`.</ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (udp | tcp) { udp:0, tcp:1 }">
Traffic to send:
- `udp` (default) - UDP packets of `local-udp-tx-size` and `remote-udp-tx-size` bytes; the receiver counts lost packets.
- `tcp` - TCP connections (`connection-count`); TCP adapts its rate to the path.
</ArgTableRow>
<ArgTableRow arg="local-udp-tx-size" typ="range">Size of the UDP packets the client sends, in bytes of the whole IP packet: 1500 sends a 1472-byte UDP payload. Values below 52 fail with `failure: size too small` over IPv4. Range `28..64000`. Default: 1500.</ArgTableRow>
<ArgTableRow arg="remote-udp-tx-size" typ="range">Size of the UDP packets the server sends, counted the same way as `local-udp-tx-size`. Default: 1500.</ArgTableRow>
<ArgTableRow arg="direction" typ="enum (receive | transmit | both) { receive:0x00000100, transmit:0x00000200, both:0x00000300 }">
Which side sends:
- `receive` (default) - The server sends, the client receives (`rx-*` values).
- `transmit` - The client sends, the server receives (`tx-*` values).
- `both` - Both sides send at the same time.
</ArgTableRow>
<ArgTableRow arg="connection-count" typ="num">Number of TCP connections, or of UDP streams with their own ports, that the test uses. Range `1..255`. Default: 20, or the number of CPU cores on routers with more than 20 cores.</ArgTableRow>
<ArgTableRow arg="local-tx-speed" typ="num">Maximum rate the client sends at, in bits per second (suffixes such as `50M` work). Without it, the client sends as fast as it can: an unlimited UDP test floods for about the first second and then sends more than the receiver reports, so `lost-packets` stays above zero.</ArgTableRow>
<ArgTableRow arg="remote-tx-speed" typ="num">Maximum rate the server sends at, in bits per second (suffixes such as `50M` work). Without it, the server sends as fast as it can.</ArgTableRow>
<ArgTableRow arg="user" typ="string">User name on the server. The user's group needs both the `test` and `winbox` policies (see [`/user/group`](../user/group)). Not needed when the server has `authenticate=no`.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password of `user` on the server.</ArgTableRow>
<ArgTableRow arg="duration" typ="time">How long the test runs. Without it, the test runs until you stop it, for example with <kbd>Control</kbd>+<kbd>C</kbd>.</ArgTableRow>
<ArgTableRow arg="random-data" typ="bool">Whether to fill the payload with random, incompressible data, so that links that compress traffic do not show a higher rate than they carry. It costs more CPU time on both sides. Default: no.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="enum (connecting | can not start test | can not connect | remote is busy | test unsupported | running | disconnected | authentication failed | done testing) { connecting:0, can not start test:1, can not connect:2, remote is busy:3, test unsupported:4, running:5, disconnected:6, authentication failed:7, done testing:8 }">
State of the test:
- `connecting` - The client is connecting to the server.
- `running` - The test runs.
- `done testing` - The test ended after `duration`.
- `authentication failed` - The server refused the user name or password, or no user was given while the server authenticates.
- `can not connect` - The server is disabled or not reachable, the client is not in its `allowed-addresses4`/`allowed-addresses6`, or `max-sessions` is reached.
- `disconnected` - The connection to the server ended during the test, also when the test uses more connections than the server's `max-sessions`.

Other values report that the server refused or could not start the test.
</ArgTableRow>
<ArgTableRow arg="duration" typ="time">How long the test has run.</ArgTableRow>
<ArgTableRow arg="tx-current" typ="num">Rate the client sent at in the last second. UDP counts whole IP packets (IP and UDP headers included), TCP counts the TCP payload only.</ArgTableRow>
<ArgTableRow arg="tx-10-second-average" typ="num">Average rate the client sent at over the last 10 seconds.</ArgTableRow>
<ArgTableRow arg="tx-total-average" typ="num">Average rate the client sent at since the test started.</ArgTableRow>
<ArgTableRow arg="rx-current" typ="num">Rate the client received at in the last second. UDP counts whole IP packets (IP and UDP headers included), TCP counts the TCP payload only.</ArgTableRow>
<ArgTableRow arg="rx-10-second-average" typ="num">Average rate the client received at over the last 10 seconds.</ArgTableRow>
<ArgTableRow arg="rx-total-average" typ="num">Average rate the client received at since the test started.</ArgTableRow>
<ArgTableRow arg="lost-packets" typ="num">UDP packets lost in the last second, not a total since the start.</ArgTableRow>
<ArgTableRow arg="random-data" typ="bool">Whether the test uses random data (`random-data`).</ArgTableRow>
<ArgTableRow arg="direction" typ="enum (receive | transmit | both) { receive:0x00000100, transmit:0x00000200, both:0x00000300 }">Direction of the test (`direction`).</ArgTableRow>
<ArgTableRow arg="tx-size" typ="range">Size of the UDP packets the client sends, in bytes of the whole IP packet.</ArgTableRow>
<ArgTableRow arg="rx-size" typ="range">Size of the UDP packets the client receives, in bytes of the whole IP packet.</ArgTableRow>
<ArgTableRow arg="connection-count" typ="num">Number of TCP connections or UDP streams the test uses.</ArgTableRow>
<ArgTableRow arg="local-cpu-load" typ="num">CPU load of the client during the test, shown after the first seconds.</ArgTableRow>
<ArgTableRow arg="remote-cpu-load" typ="num">CPU load of the server during the test, shown after the first seconds.</ArgTableRow>
<ArgTableRow arg="tcp-info" typ="multi { name: string
 }"></ArgTableRow>
</ArgTable>
