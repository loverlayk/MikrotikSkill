# server

> RouterOS settings reference for /interface/l2tp-server/server.

-----------

## interface/l2tp-server/server 
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool">Enables or disables the L2TP server.</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">Maximum Transmission Unit. Maximum packet size that the L2TP interface can send without packet fragmentation.</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">Maximum Receive Unit. Maximum packet size that the L2TP interface can receive without packet fragmentation.</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">Maximum packet size that can be received on the link. If a packet is bigger than tunnel MTU, it is split into multiple packets, allowing full-size IP or Ethernet packets to be sent over the tunnel.</ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)">Allowed authentication methods.</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">Keepalive timeout in seconds.</ArgTableRow>
<ArgTableRow arg="max-sessions" typ="num">Maximum number of concurrent L2TP sessions.</ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum">Specifies which PPP profile configuration is used when establishing the tunnel.</ArgTableRow>
<ArgTableRow arg="use-ipsec" typ="enum (no | yes | required) { no:0, yes:1, required:2 }">Whether to use IPsec encryption. `required` forces all clients to use IPsec.</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string">IPsec pre-shared key.</ArgTableRow>
<ArgTableRow arg="caller-id-type" typ="enum (ip-address | number) { ip-address:0, number:1 }">Caller ID type reported to the client.</ArgTableRow>
<ArgTableRow arg="one-session-per-host" typ="bool">Whether to allow only one session per host.</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">Whether to allow FastPath processing.</ArgTableRow>
<ArgTableRow arg="l2tpv3-circuit-id" typ="string">L2TPv3 circuit identifier.</ArgTableRow>
<ArgTableRow arg="l2tpv3-cookie-length" typ="enum (0 | 4-bytes | 8-bytes) { 0:0, 4-bytes:4, 8-bytes:8 }">L2TPv3 cookie length.</ArgTableRow>
<ArgTableRow arg="l2tpv3-digest-hash" typ="enum (none | md5 | sha1) { none:99, md5:0, sha1:1 }">L2TPv3 digest hash algorithm.</ArgTableRow>
<ArgTableRow arg="l2tpv3-ether-interface-list" typ="enum">Interface list for L2TPv3 Ethernet pseudowire endpoints.</ArgTableRow>
<ArgTableRow arg="accept-pseudowire-type" typ="enum (all | ether | ppp) { all:0, ether:5, ppp:7 }">Accepted pseudowire types.</ArgTableRow>
<ArgTableRow arg="accept-proto-version" typ="enum (all | l2tpv2 | l2tpv3) { all:0, l2tpv2:2, l2tpv3:3 }">Accepted L2TP protocol versions.</ArgTableRow>
</ArgTable>
