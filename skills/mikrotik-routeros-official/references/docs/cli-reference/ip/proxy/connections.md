# connections

> Open connections of the web proxy. Each connection from a client and each connection to a server is a row. The proxy keeps connections to servers open after a response and uses them for later requests. For an...

-----------

## ip/proxy/connections 
**Type:** Directory

Open connections of the web proxy. Each connection from a client and each connection to a server is a row. The proxy keeps connections to servers open after a response and uses them for later requests. For an overview, see [Web Proxy](../../../network-management/proxy/web-proxy).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="S" typ="server">server. A connection from the proxy to a server.</ArgTableRow>
<ArgTableRow arg="C" typ="client">client. A connection from a client to the proxy.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="src-address" typ="alt { ip4: ipAddr
, ip6: ip6Addr
 }">Address of the client whose request the connection serves.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="alt { ip4: ipAddr
, ip6: ip6Addr
 }">Address of the server.</ArgTableRow>
<ArgTableRow arg="last-protocol" typ="enum (HTTP/1.0 | HTTP/1.1 | FTP) { HTTP/1.0:1, HTTP/1.1:2, FTP:3 }">Protocol of the last request on the connection: `HTTP/1.0`, `HTTP/1.1` or `FTP`.</ArgTableRow>
<ArgTableRow arg="state" typ="enum (rx-header | resolving | connecting | waiting | rx-body | tx-header | tx-body | idle) { rx-header:0, resolving:1, connecting:2, waiting:3, rx-body:4, tx-header:5, tx-body:6, idle:7 }">
State of the connection, for example:
- `waiting` - A client connection waits for the response from the server.
- `rx-header` - A server connection receives the header of the response.
- `idle` - A server connection is open and has no request.
</ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num">Bytes the router sent on the connection.</ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num">Bytes the router received on the connection.</ArgTableRow>
</ArgTable>
