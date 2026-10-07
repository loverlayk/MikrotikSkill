# l2tp-client

> RouterOS directory reference for /interface/l2tp-client.

-----------

## interface/l2tp-client 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="R" typ="running">Whether the interface is running.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Descriptive name of the interface.</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">Maximum Transmission Unit. Maximum packet size that the L2TP interface can send without packet fragmentation.</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">Maximum Receive Unit. Maximum packet size that the L2TP interface can receive without packet fragmentation.</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">Maximum packet size that can be received on the link. If a packet is bigger than tunnel MTU, it is split into multiple packets, allowing full-size IP or Ethernet packets to be sent over the tunnel.</ArgTableRow>
<ArgTableRow arg="connect-to" typ="address (flags=D46v)" mandatory="1">Remote address of the L2TP server. If the address is in the VRF table, VRF should be specified, for example, `192.168.88.1@vrf1` .</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">User name used for authentication.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password used for authentication.</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">Specifies which PPP profile configuration is used when establishing the tunnel.</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">Keepalive timeout in seconds.</ArgTableRow>
<ArgTableRow arg="src-address" typ="ipAddr">Source address used for the L2TP connection.</ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="enum (no | yes | exclusively) { no:0, yes:1, exclusively:2 }">Whether to use DNS settings from the peer.</ArgTableRow>
<ArgTableRow arg="use-ipsec" typ="bool">
When this option is enabled, dynamic IPSec peer configuration and policy (transport mode) is added to encapsulate the L2TP connection into an IPSec tunnel.

Multiple L2tp/ipsec clients behind the same NAT will not work in this mode. To achieve such a scenario, disable use-ipsec and set static policies for clients with enabled tunnel=yes, level=unique settings.
</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string">IPsec pre-shared key.</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">Whether to allow FastPath processing. Must be disabled if IPsec is used.</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool">Whether to add the L2TP remote address as a default route.</ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num">Distance value applied to the auto-created default route when add-default-route is enabled.</ArgTableRow>
<ArgTableRow arg="dial-on-demand" typ="bool">Connects to the L2TP server only when outbound traffic is generated. If enabled, a route with a gateway address from 10.112.112.0/24 network is added while the connection is not established.</ArgTableRow>
<ArgTableRow arg="allow" typ="ubit (pap, chap, mschap1, mschap2)">Allowed authentication methods.</ArgTableRow>
<ArgTableRow arg="random-source-port" typ="bool">Whether to randomize the source port for L2TP connections.</ArgTableRow>
<ArgTableRow arg="l2tp-proto-version" typ="enum (l2tpv2 | l2tpv3-ip | l2tpv3-udp) { l2tpv2:0, l2tpv3-ip:1, l2tpv3-udp:2 }">L2TP protocol version to use.</ArgTableRow>
<ArgTableRow arg="l2tpv3-circuit-id" typ="string">L2TPv3 circuit identifier.</ArgTableRow>
<ArgTableRow arg="l2tpv3-cookie-length" typ="enum (0 | 4-bytes | 8-bytes) { 0:0, 4-bytes:4, 8-bytes:8 }">L2TPv3 cookie length.</ArgTableRow>
<ArgTableRow arg="l2tpv3-digest-hash" typ="enum (none | md5 | sha1) { none:99, md5:0, sha1:1 }">L2TPv3 digest hash algorithm.</ArgTableRow>
</ArgTable>
