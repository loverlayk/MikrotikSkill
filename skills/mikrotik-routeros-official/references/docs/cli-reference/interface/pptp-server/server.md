# server

> RouterOS settings reference for /interface/pptp-server/server.

-----------

## interface/pptp-server/server 
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool">Defines whether the PPTP server is enabled.</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">Maximum Transmission Unit. Maximum packet size that the PPTP interface can send without packet fragmentation.</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">Maximum Receive Unit. Maximum packet size that the PPTP interface can receive without packet fragmentation.</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">Maximum packet size that can be received on the link. If a packet is bigger than tunnel MTU, it is split into multiple packets, allowing full-size IP or Ethernet packets to be sent over the tunnel.</ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)">Authentication methods that the server accepts.</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">If the server does not receive any packet during the keepalive period, it sends keepalive packets every second five times. If the server does not receive a response from the client, the connection is disconnected after 5 seconds.</ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum">Specifies which PPP profile configuration is used when establishing the tunnel.</ArgTableRow>
</ArgTable>
