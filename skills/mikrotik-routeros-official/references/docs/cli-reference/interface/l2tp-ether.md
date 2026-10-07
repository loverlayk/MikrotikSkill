# l2tp-ether

> Layer 2 Tunnel Protocol Version 3 (L2TPv3).

-----------

## interface/l2tp-ether 
**Type:** Directory

Layer 2 Tunnel Protocol Version 3 (L2TPv3).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">Whether the interface was created dynamically.</ArgTableRow>
<ArgTableRow arg="R" typ="running">Whether the interface is running.</ArgTableRow>
<ArgTableRow arg="u" typ="unmanaged">Whether the interface is unmanaged.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Interface name.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="connect-to" typ="address (flags=D46v)">Remote server address. Set to 0.0.0.0 for incoming connections.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the L2TP interface.</ArgTableRow>
<ArgTableRow arg="use-ipsec" typ="bool">Ignored for passive (incoming) connections. For incoming connections use l2tp-server settings.</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string">Ignored for passive (incoming) connections. For incoming connections use l2tp-server settings.</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">Whether to allow FastPath processing.</ArgTableRow>
<ArgTableRow arg="l2tp-proto-version" typ="enum (l2tpv3-ip | l2tpv3-udp) { l2tpv3-ip:1, l2tpv3-udp:2 }">L2TPv3 encapsulation mode (IP or UDP).</ArgTableRow>
<ArgTableRow arg="circuit-id" typ="string">L2TPv3 remote end identifier (virtual circuit ID).</ArgTableRow>
<ArgTableRow arg="cookie-length" typ="enum (0 | 4-bytes | 8-bytes) { 0:0, 4-bytes:4, 8-bytes:8 }">Ignored for passive (incoming) connections. For incoming connections use l2tp-server settings.</ArgTableRow>
<ArgTableRow arg="digest-hash" typ="enum (none | md5 | sha1) { none:99, md5:0, sha1:1 }">Ignored for passive (incoming) connections. For incoming connections use l2tp-server settings.</ArgTableRow>
<ArgTableRow arg="use-l2-specific-sublayer" typ="bool">Enables L2TPv3 Ethernet pseudowire Level 2 default sublayer.</ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { local-ipv4-address: ipAddr
, local-ipv6-address: ip6Addr
 }">Local IPv4 or IPv6 address for unmanaged L2TP connections.</ArgTableRow>
<ArgTableRow arg="local-tunnel-id" typ="num">Local tunnel ID for unmanaged L2TP connections.</ArgTableRow>
<ArgTableRow arg="local-session-id" typ="num">Local session ID for unmanaged L2TP connections.</ArgTableRow>
<ArgTableRow arg="remote-tunnel-id" typ="num">Remote tunnel ID for unmanaged L2TP connections.</ArgTableRow>
<ArgTableRow arg="remote-session-id" typ="num">Remote session ID for unmanaged L2TP connections.</ArgTableRow>
<ArgTableRow arg="peer-cookie" typ="string">Cookie hex value for received packets (8 or 16 characters or empty) for unmanaged L2TP connections.</ArgTableRow>
<ArgTableRow arg="send-cookie" typ="string">Cookie hex value for sent packets (8 or 16 characters or empty) for unmanaged L2TP connections.</ArgTableRow>
<ArgTableRow arg="unmanaged-mode" typ="bool">Enables or disables unmanaged (static) tunnel mode.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="actual-mtu" typ="num">Actual maximum transmission unit of the tunnel.</ArgTableRow>
</ArgTable>
