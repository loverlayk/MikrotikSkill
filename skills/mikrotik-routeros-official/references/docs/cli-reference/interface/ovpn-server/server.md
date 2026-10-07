# server

> RouterOS directory reference for /interface/ovpn-server/server.

-----------

## interface/ovpn-server/server 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive">Whether the server is inactive.</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the server.</ArgTableRow>
<ArgTableRow arg="port" typ="num">Port to run the server on.</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (ip | ethernet) { ip:0, ethernet:1 }">Layer3 or Layer2 tunnel mode (alternatively tun, tap).</ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (tcp | udp)">Transport protocol to use when connecting with the remote endpoint.</ArgTableRow>
<ArgTableRow arg="netmask" typ="num">Subnet mask applied to the client.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">Automatically generated MAC address of the server.</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">Maximum Transmission Unit. Maximum packet size that the OVPN interface can send without packet fragmentation.</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">Defines the time period (in seconds) after which the router starts sending keepalive packets every second. If no traffic and no keepalive responses are received for twice the keepalive-timeout, the non-responding client is disconnected.</ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum">Specifies which PPP profile configuration is used when establishing the tunnel.</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum">Certificate from the certificate store that the OVPN server uses.</ArgTableRow>
<ArgTableRow arg="require-client-certificate" typ="bool">If set to yes, the server checks whether the client's certificate belongs to the same certificate chain.</ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2) { any:0, only-1.2:2 }">Specifies which TLS versions to allow.</ArgTableRow>
<ArgTableRow arg="auth" typ="ubit (sha1, md5, sha256, sha384, sha512, null)">Authentication methods that the server accepts.</ArgTableRow>
<ArgTableRow arg="cipher" typ="ubit (blowfish128, aes128-cbc, aes192-cbc, aes256-cbc, aes128-gcm, aes192-gcm, aes256-gcm, null)">Allowed ciphers.</ArgTableRow>
<ArgTableRow arg="reneg-sec" typ="num">Encryption key re-negotiation interval in seconds. 0 disables re-negotiation.</ArgTableRow>
<ArgTableRow arg="redirect-gateway" typ="ubit (disabled, def1, ipv6)">Specifies which routes the OVPN client must add to the routing table. `def1` - overrides the default gateway with 0.0.0.0/1 and 128.0.0.0/1 instead of 0.0.0.0/0. `disabled` - does not push redirect-gateway flags. `ipv6` - redirects IPv6 routing into the tunnel by adding 2000::/4 and 3000::/4 routes.</ArgTableRow>
<ArgTableRow arg="push-routes" typ="string">Routes to push to the client. Maximum input is limited to 1400 characters or 37 routes. IPv6 support added in version 7.21.</ArgTableRow>
<ArgTableRow arg="push-routes-ipv6" typ="string">IPv6 routes to push to the client.</ArgTableRow>
<ArgTableRow arg="enable-tun-ipv6" typ="bool">Whether IPv6 tunneling is enabled for this OVPN server.</ArgTableRow>
<ArgTableRow arg="tun-server-ipv6" typ="ip6Addr">IPv6 prefix address used when generating the OVPN interface on the server side.</ArgTableRow>
<ArgTableRow arg="ipv6-prefix-len" typ="num">Prefix length used for the tunneled IPv6 address.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">VRF in which to listen for connection attempts.</ArgTableRow>
<ArgTableRow arg="user-auth-method" typ="enum (pap | mschap2) { pap:16, mschap2:2 }">By default PAP authentication is used. Set to mschap2 to use CHAP challenge authentication.</ArgTableRow>
</ArgTable>
