# pptp-client

> RouterOS directory reference for /interface/pptp-client.

-----------

## interface/pptp-client 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="R" typ="running">Whether the interface is running.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Descriptive name of the interface.</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">Maximum Transmission Unit. Maximum packet size that the PPTP interface can send without packet fragmentation.</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">Maximum Receive Unit. Maximum packet size that the PPTP interface can receive without packet fragmentation.</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">Maximum packet size that can be received on the link. If a packet is bigger than tunnel MTU, it is split into multiple packets, allowing full-size IP or Ethernet packets to be sent over the tunnel.</ArgTableRow>
<ArgTableRow arg="connect-to" typ="alt { address: ipAddr
, name: string
 }" mandatory="1">Remote address of the PPTP server.</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">User name used for authentication.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password used for authentication.</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">Specifies which PPP profile configuration is used when establishing the tunnel.</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">Keepalive timeout in seconds.</ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="enum (no | yes | exclusively) { no:0, yes:1, exclusively:2 }">Whether to use DNS settings from the peer.</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool">Whether to add the PPTP remote address as a default route.</ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num">Distance value applied to the auto-created default route when add-default-route is enabled.</ArgTableRow>
<ArgTableRow arg="dial-on-demand" typ="bool">Connects to the PPTP server only when outbound traffic is generated. If enabled, a route with a gateway address from 10.112.112.0/24 network is added while the connection is not established.</ArgTableRow>
<ArgTableRow arg="allow" typ="ubit (pap, chap, mschap1, mschap2)">Allowed authentication methods.</ArgTableRow>
</ArgTable>
