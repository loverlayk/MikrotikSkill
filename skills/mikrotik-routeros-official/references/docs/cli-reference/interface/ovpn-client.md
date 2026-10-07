# ovpn-client

> RouterOS directory reference for /interface/ovpn-client.

-----------

## interface/ovpn-client 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="R" typ="running">Whether the interface is running.</ArgTableRow>
<ArgTableRow arg="H" typ="hw-crypto">Whether hardware encryption is active.</ArgTableRow>
<ArgTableRow arg="Ta" typ="tls-auth">Whether TLS authentication (tls-auth) is active.</ArgTableRow>
<ArgTableRow arg="Tc" typ="tls-crypt">Whether tls-crypt authentication is active.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Descriptive name of the interface.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the OVPN interface. Automatically generated if not specified.</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">Maximum Transmission Unit. Maximum packet size that the OVPN interface can send without packet fragmentation.</ArgTableRow>
<ArgTableRow arg="connect-to" typ="address (flags=D46v)" mandatory="1">Remote address of the OVPN server.</ArgTableRow>
<ArgTableRow arg="port" typ="num">Port to connect to.</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (ip | ethernet) { ip:0, ethernet:1 }">Layer3 or Layer2 tunnel mode (alternatively tun, tap).</ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (tcp | udp)">Transport protocol to use when connecting to the remote endpoint.</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">User name used for authentication.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password used for authentication. Must not be longer than 1000 characters.</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">Specifies which PPP profile configuration is used when establishing the tunnel.</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none) { none:0 }">Client certificate from the certificate store.</ArgTableRow>
<ArgTableRow arg="verify-server-certificate" typ="bool">Checks the server certificate's CN or SAN against the connect-to parameter and enables trust-chain validation against the router's certificate store. The IP or hostname must be present in the server's certificate.</ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2) { any:0, only-1.2:2 }">Specifies which TLS versions to allow.</ArgTableRow>
<ArgTableRow arg="auth" typ="enum (sha1 | md5 | sha256 | sha384 | sha512 | null) { sha1:1, md5:2, sha256:8, sha384:32, sha512:16, null:4 }">Allowed authentication methods.</ArgTableRow>
<ArgTableRow arg="cipher" typ="enum (blowfish128 | aes128-cbc | aes192-cbc | aes256-cbc | aes128-gcm | aes192-gcm | aes256-gcm | null) { blowfish128:1, aes128-cbc:2, aes192-cbc:4, aes256-cbc:8, aes128-gcm:16, aes192-gcm:32, aes256-gcm:64, null:128 }">Allowed ciphers. To use GCM ciphers, set auth to null, because the GCM cipher also handles authentication.</ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="enum (no | yes | exclusively) { no:0, yes:1, exclusively:2 }">Whether to add DNS servers provided by the OVPN server to IP/DNS configuration.</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool">Whether to add the OVPN remote address as a default route.</ArgTableRow>
<ArgTableRow arg="route-nopull" typ="bool">If enabled, the client does not use routes pushed by the server (including def1).</ArgTableRow>
<ArgTableRow arg="disconnect-notify" typ="bool">Sends explicit disconnect notification in UDP mode.</ArgTableRow>
</ArgTable>
