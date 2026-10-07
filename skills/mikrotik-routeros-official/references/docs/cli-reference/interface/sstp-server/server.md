# server

> RouterOS settings reference for /interface/sstp-server/server.

-----------

## interface/sstp-server/server 
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool">Enables or disables the SSTP server.</ArgTableRow>
<ArgTableRow arg="port" typ="num">Listening port for the SSTP server.</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">Maximum Transmission Unit.</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">Maximum Receive Unit.</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">Maximum packet size that can be received on the link. If a packet is bigger than tunnel MTU, it is split into multiple packets, allowing full-size IP or Ethernet packets to be sent over the tunnel.</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">Keepalive timeout in seconds.</ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum">Specifies which PPP profile configuration is used when establishing the tunnel.</ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)">Allowed authentication methods. By default all methods are allowed.</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none) { none:0 }">Server certificate from the certificate store.</ArgTableRow>
<ArgTableRow arg="verify-client-certificate" typ="bool">Verifies the client certificate against the router's certificate store.</ArgTableRow>
<ArgTableRow arg="pfs" typ="enum (no | yes | required) { no:0, yes:1, required:2 }">Specifies which TLS authentication to use. `yes` - TLS uses ECDHE-RSA and DHE-RSA. `required` - uses only ECDHE.</ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2) { any:0, only-1.2:2 }">Specifies which TLS version to allow.</ArgTableRow>
<ArgTableRow arg="ciphers" typ="ubit (aes256-sha, aes256-gcm-sha384)">Allowed ciphers.</ArgTableRow>
</ArgTable>
