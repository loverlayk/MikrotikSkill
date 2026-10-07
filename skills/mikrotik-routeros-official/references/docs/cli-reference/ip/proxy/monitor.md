# monitor

> Shows the state and the counters of the web proxy. Add once for a single reading, for example /ip/proxy/monitor once. For an overview, see Web Proxy.

-----------

## ip/proxy/monitor 
**Type:** Command

Shows the state and the counters of the web proxy. Add `once` for a single reading, for example `/ip/proxy/monitor once`. For an overview, see [Web Proxy](../../../network-management/proxy/web-proxy).

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="enum (stopped | running | invalid-address | building-cache | passthrough) { stopped:0, running:1, invalid-address:4, building-cache:5 }">
State of the proxy, for example:
- `running` - The proxy is enabled and serves requests.
- `stopped` - The proxy is disabled.
</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">Time since the proxy started.</ArgTableRow>
<ArgTableRow arg="client-connections" typ="num">Open connections from clients.</ArgTableRow>
<ArgTableRow arg="server-connections" typ="num">Open connections to servers.</ArgTableRow>
<ArgTableRow arg="requests" typ="num">Number of requests the proxy received.</ArgTableRow>
<ArgTableRow arg="hits" typ="num">Number of requests answered from the cache.</ArgTableRow>
<ArgTableRow arg="cache-used" typ="num">Size of the objects in the cache, in KiB.</ArgTableRow>
<ArgTableRow arg="total-ram-used" typ="num"></ArgTableRow>
<ArgTableRow arg="received-from-servers" typ="num">Data received from servers, in KiB.</ArgTableRow>
<ArgTableRow arg="sent-to-clients" typ="num">Data sent to clients, in KiB.</ArgTableRow>
<ArgTableRow arg="hits-sent-to-clients" typ="num">Data sent to clients from the cache, in KiB.</ArgTableRow>
</ArgTable>
