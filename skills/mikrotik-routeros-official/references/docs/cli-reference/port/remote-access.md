# remote-access

> RouterOS directory reference for /port/remote-access.

-----------

## port/remote-access 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="A" typ="active">active</ArgTableRow>
<ArgTableRow arg="B" typ="busy">busy</ArgTableRow>
<ArgTableRow arg="L" typ="logging-active">logging-active</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="port" typ="enum"></ArgTableRow>
<ArgTableRow arg="channel" typ="num"></ArgTableRow>
<ArgTableRow arg="remote-addresses" typ="object { peer-spec: super { addr0: address (flags=46/)
, [addr1] [ -address (flags=46)]
, [port] [ @num]
 }
 }"></ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { ipv4: ipAddr
, ipv6: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="ip-port" typ="num"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (tcp-server | rfc2217 | tcp-client | udp) { tcp-server:0, rfc2217:1, tcp-client:2, udp:3 }"></ArgTableRow>
<ArgTableRow arg="log-file" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="active-peer" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="active-peer-port" typ="num"></ArgTableRow>
</ArgTable>
