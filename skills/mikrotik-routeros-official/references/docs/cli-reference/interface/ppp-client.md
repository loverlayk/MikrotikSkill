# ppp-client

> RouterOS directory reference for /interface/ppp-client.

-----------

## interface/ppp-client 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="max-mru" typ="num"></ArgTableRow>
<ArgTableRow arg="mrru" typ="num"></ArgTableRow>
<ArgTableRow arg="port" typ="enum"></ArgTableRow>
<ArgTableRow arg="data-channel" typ="num"></ArgTableRow>
<ArgTableRow arg="info-channel" typ="num"></ArgTableRow>
<ArgTableRow arg="network-mode" typ="enum (lte-m | nb-iot | auto) { lte-m:0, nb-iot:1, auto:2 }"></ArgTableRow>
<ArgTableRow arg="apn" typ="string"></ArgTableRow>
<ArgTableRow arg="pin" typ="string"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="phone" typ="string"></ArgTableRow>
<ArgTableRow arg="dial-command" typ="string"></ArgTableRow>
<ArgTableRow arg="modem-init" typ="string"></ArgTableRow>
<ArgTableRow arg="null-modem" typ="bool"></ArgTableRow>
<ArgTableRow arg="dial-on-demand" typ="bool"></ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool"></ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num"></ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="bool"></ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="allow" typ="ubit (pap, chap, mschap1, mschap2)"></ArgTableRow>
</ArgTable>
