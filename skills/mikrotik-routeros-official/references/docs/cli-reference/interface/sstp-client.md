# sstp-client

> RouterOS directory reference for /interface/sstp-client.

-----------

## interface/sstp-client 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="R" typ="running">Whether the interface is running.</ArgTableRow>
<ArgTableRow arg="H" typ="hw-crypto">Whether hardware encryption is active.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Descriptive name of the interface.</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">Maximum Transmission Unit.</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">Maximum Receive Unit.</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">Maximum packet size that can be received on the link. If a packet is bigger than tunnel MTU, it is split into multiple packets, allowing full-size IP or Ethernet packets to be sent over the tunnel.</ArgTableRow>
<ArgTableRow arg="connect-to" typ="address (flags=D46v)" mandatory="1">Remote address of the SSTP server.</ArgTableRow>
<ArgTableRow arg="port" typ="num">Port to connect to.</ArgTableRow>
<ArgTableRow arg="http-proxy" typ="alt { address: ipAddr
, ipv6-address: ip6Addr
, name: string
 }">Proxy address.</ArgTableRow>
<ArgTableRow arg="proxy-port" typ="num">Proxy port.</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none) { none:0 }">Client certificate from the certificate store.</ArgTableRow>
<ArgTableRow arg="verify-server-certificate" typ="bool">Verifies the server certificate against the router's certificate store.</ArgTableRow>
<ArgTableRow arg="verify-server-address-from-certificate" typ="bool">Verifies the server address from the certificate.</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">User name used for authentication.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password used for authentication.</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">Specifies which PPP profile configuration is used when establishing the tunnel.</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">Keepalive timeout in seconds.</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool">Whether to add the SSTP remote address as a default route.</ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num">Distance value applied to the auto-created default route when add-default-route is enabled.</ArgTableRow>
<ArgTableRow arg="dial-on-demand" typ="bool">Connects only when outbound traffic is generated. If enabled, a route with a gateway address from 10.112.112.0/24 network is added while the connection is not established.</ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)">Allowed authentication methods. By default all methods are allowed.</ArgTableRow>
<ArgTableRow arg="pfs" typ="enum (no | yes | required) { no:0, yes:1, required:2 }">Specifies which TLS authentication to use. `yes` - TLS uses ECDHE-RSA and DHE-RSA. `required` - uses only ECDHE.</ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2) { any:0, only-1.2:2 }">Specifies which TLS version to allow.</ArgTableRow>
<ArgTableRow arg="ciphers" typ="ubit (aes256-sha, aes256-gcm-sha384)">Allowed ciphers.</ArgTableRow>
<ArgTableRow arg="add-sni" typ="bool">Adds TLS SNI extension to client hello packets. Available from RouterOS version 7.15.</ArgTableRow>
</ArgTable>
