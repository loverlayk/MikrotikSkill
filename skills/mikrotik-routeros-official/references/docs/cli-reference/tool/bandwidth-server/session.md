# session

> Tests that are running on this router's bandwidth test server (/tool/bandwidth-server), from the server's point of view: send means that the server sends. A session disappears when its test ends. See Bandwidth test.

-----------

## tool/bandwidth-server/session 
**Type:** Directory

Tests that are running on this router's bandwidth test server ([`/tool/bandwidth-server`](.)), from the server's point of view: `send` means that the server sends. A session disappears when its test ends. See [Bandwidth test](../../../diagnostics-monitoring-and-troubleshooting/bandwidth-test).

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="client" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }">Address of the client. IPv4 clients are shown as IPv4-mapped IPv6 addresses, for example `::ffff:192.0.2.1`.</ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (udp | tcp) { udp:0, tcp:1 }">Protocol of the test, `udp` or `tcp`.</ArgTableRow>
<ArgTableRow arg="direction" typ="enum (receive | send | both) { receive:0x00000100, send:0x00000200, both:0x00000300 }">
Which side sends, from the server's point of view:
- `receive` - The client sends, the server receives (the client's `transmit`).
- `send` - The server sends (the client's `receive`).
- `both` - Both sides send.
</ArgTableRow>
<ArgTableRow arg="user" typ="string">User the client logged in as; empty when the server has `authenticate=no` and the client gave no user.</ArgTableRow>
<ArgTableRow arg="random-data" typ="bool">Whether the test uses random data.</ArgTableRow>
<ArgTableRow arg="tx-current" typ="num">Rate the server sent at in the last second.</ArgTableRow>
<ArgTableRow arg="tx-10-second-average" typ="num">Average rate the server sent at over the last 10 seconds.</ArgTableRow>
<ArgTableRow arg="tx-total-average" typ="num">Average rate the server sent at since the test started.</ArgTableRow>
<ArgTableRow arg="rx-current" typ="num">Rate the server received at in the last second.</ArgTableRow>
<ArgTableRow arg="rx-10-second-average" typ="num">Average rate the server received at over the last 10 seconds.</ArgTableRow>
<ArgTableRow arg="rx-total-average" typ="num">Average rate the server received at since the test started.</ArgTableRow>
<ArgTableRow arg="lost-packets" typ="num">UDP packets the server found missing in the last second.</ArgTableRow>
<ArgTableRow arg="tx-size" typ="range">Size of the UDP packets the server sends, in bytes of the whole IP packet.</ArgTableRow>
<ArgTableRow arg="rx-size" typ="range">Size of the UDP packets the server receives, in bytes of the whole IP packet.</ArgTableRow>
<ArgTableRow arg="tcp-connection-count" typ="num">Number of connections of the test (`connection-count` of the client); also shown for UDP tests.</ArgTableRow>
<ArgTableRow arg="local-tx-speed" typ="num">Speed limit the client set for its own sending (`local-tx-speed`).</ArgTableRow>
<ArgTableRow arg="remote-tx-speed" typ="num">Speed limit the client set for the server's sending (`remote-tx-speed`).</ArgTableRow>
</ArgTable>
