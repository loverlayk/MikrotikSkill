# connections

> Read-only list of active proxied connections. An entry exists while a proxied connection is open. For more information, see SOCKS.

-----------

## ip/socks/connections 
**Type:** Directory

Read-only list of active proxied connections. An entry exists while a proxied connection is open. For more information, see [SOCKS](../../../network-management/socks).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="src-address" typ="composite { address: alt { addr-ipv4: ipAddr
, addr-ipv6: ip6Addr
 }
, port: num
 }">Address and port of the SOCKS client.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="composite { address: alt { addr-ipv4: ipAddr
, addr-ipv6: ip6Addr
, addr-domain: string
 }
, port: num
 }">The requested destination address and port.</ArgTableRow>
<ArgTableRow arg="type" typ="enum (unknown | out | in) { unknown:0, out:1, in:2 }">
Type of the connection.
- `unknown` - The connection was just initiated.
- `out` - The connection is being relayed to the requested destination.
- `in` - The connection is incoming.
</ArgTableRow>
<ArgTableRow arg="tx" typ="num">Bytes relayed to the destination on this connection.</ArgTableRow>
<ArgTableRow arg="rx" typ="num">Bytes received from the destination on this connection.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="user" typ="enum">Username from [`users`](users) the client authenticated with. Empty when `auth-method=none`.</ArgTableRow>
</ArgTable>
