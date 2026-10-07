# peers

> RouterOS directory reference for /interface/wireguard/peers.

-----------

## interface/wireguard/peers 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">Whether the peer was created dynamically.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Name of the WireGuard interface the peer belongs to.</ArgTableRow>
<ArgTableRow arg="name" typ="string">Adds a name to a peer, used as a reference in WireGuard logs. Available from RouterOS version 7.15.</ArgTableRow>
<ArgTableRow arg="public-key" typ="string">A base64 public key calculated from the private key. Public keys are used by peers to authenticate each other.</ArgTableRow>
<ArgTableRow arg="private-key" typ="alt { private-key: num
, private-key: string
 }">A base64 private key. `auto` generates the key automatically, `none` disables it.</ArgTableRow>
<ArgTableRow arg="endpoint-address" typ="address (flags=46D)">The IP address or hostname used by WireGuard to establish a secure connection between two peers.</ArgTableRow>
<ArgTableRow arg="endpoint-port" typ="num">The UDP port on which a WireGuard peer listens for incoming traffic.</ArgTableRow>
<ArgTableRow arg="allowed-address" typ="multi { allowed-address: address (flags=46/)
 }" mandatory="1">List of IP (v4 or v6) addresses with CIDR masks from which incoming traffic for this peer is allowed and to which outgoing traffic for this peer is directed. Allowed-address ranges cannot overlap on one interface.</ArgTableRow>
<ArgTableRow arg="preshared-key" typ="alt { preshared-key: num
, preshared-key: string
 }">A base64 preshared key. Adds an additional layer of symmetric-key cryptography for post-quantum resistance. `auto` generates the key automatically.</ArgTableRow>
<ArgTableRow arg="persistent-keepalive" typ="time">Interval in seconds of how often to send an authenticated empty packet to the peer to keep a stateful firewall or NAT mapping valid. A value of 0 disables the keepalive.</ArgTableRow>
<ArgTableRow arg="client-address" typ="multi { client-address: address (flags=46/)
 }">When imported with a QR code by a client, this address for the WireGuard interface is set on that device.</ArgTableRow>
<ArgTableRow arg="client-dns" typ="multi { client-dns: address (flags=46D)
 }">DNS servers included in the generated client configuration. This does not change the DNS configuration on this router.</ArgTableRow>
<ArgTableRow arg="client-endpoint" typ="address (flags=46D)">IP address or hostname included as the endpoint in the generated client configuration. The WireGuard interface's listen port is appended to it.</ArgTableRow>
<ArgTableRow arg="client-keepalive" typ="time">Same as persistent-keepalive but from the peer side.</ArgTableRow>
<ArgTableRow arg="client-listen-port" typ="num">The local port on which the WireGuard tunnel listens for incoming traffic from peers and from which it sources outgoing packets.</ArgTableRow>
<ArgTableRow arg="client-allowed-address" typ="multi { client-allowed-address: address (flags=46/)
 }">Allowed IPs configured for the client. Available from RouterOS version 7.21.</ArgTableRow>
<ArgTableRow arg="client-mtu" typ="num">MTU value set on the client when importing configuration.</ArgTableRow>
<ArgTableRow arg="responder" typ="bool">Specifies if the peer is a connection initiator or only a responder. Use on WireGuard devices that act as servers for client devices. Otherwise the router repeatedly tries to connect to endpoint-address or current-endpoint-address.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="current-endpoint-address" typ="address (flags=46)">The most recent source IP address of correctly authenticated packets from the peer.</ArgTableRow>
<ArgTableRow arg="current-endpoint-port" typ="num">The most recent source IP port of correctly authenticated packets from the peer.</ArgTableRow>
<ArgTableRow arg="rx" typ="num">The total amount of bytes received from the peer.</ArgTableRow>
<ArgTableRow arg="tx" typ="num">The total amount of bytes transmitted to the peer.</ArgTableRow>
<ArgTableRow arg="last-handshake" typ="time">Time in seconds after the last successful handshake.</ArgTableRow>
</ArgTable>
