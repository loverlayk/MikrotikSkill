# profile

> PPP profiles: settings shared by the users in /ppp/secret and by the PPP servers and clients that use the profile. See PPP AAA for the full guide.

-----------

## ppp/profile 
**Type:** Directory

PPP profiles: settings shared by the users in [`/ppp/secret`](secret) and by the PPP servers and clients that use the profile. See [PPP AAA](../../authentication-authorization-accounting/ppp-aaa) for the full guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">Built-in profile (`default` or `default-encryption`). It cannot be removed.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the profile.</ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { pool: enum
, address: ipAddr
 }">Address of the router inside the tunnel, or the name of an [IP pool](../ip/pool/) that gives it.</ArgTableRow>
<ArgTableRow arg="remote-address" typ="alt { pool: enum
, address: ipAddr
 }">Address of the user inside the tunnel, or the name of an [IP pool](../ip/pool/) that gives it. An address in the secret takes precedence.</ArgTableRow>
<ArgTableRow arg="remote-ipv6-prefix-pool" typ="enum ()">[IPv6 pool](../ipv6/pool/) that gives each user a prefix. The router advertises the prefix on the interface of the user and adds a route to it. Default: none.</ArgTableRow>
<ArgTableRow arg="remote-ipv6-prefix-reuse" typ="bool">With a `remote-ipv6-prefix-pool` that holds a single /64 prefix, the prefix can be given to one PPP client only. With `yes`, the same prefix is given to all clients of the profile. Default: no.</ArgTableRow>
<ArgTableRow arg="dhcpv6-pd-pool" typ="enum ()">[IPv6 pool](../ipv6/pool/) for prefix delegation. When a user connects, the router adds a dynamic DHCPv6 server on the interface of the user that delegates a prefix from this pool.</ArgTableRow>
<ArgTableRow arg="dhcpv6-use-radius" typ="bool">Value of `use-radius` of the dynamic DHCPv6 server. Default: no.</ArgTableRow>
<ArgTableRow arg="dhcpv6-lease-time" typ="time">Lease time of the dynamic DHCPv6 server. Default: 1d.</ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum">Bridge to which the interface of the user is added as a port. Both ends of the tunnel must bridge the PPP interface; see [Bridging and switching](../../bridging-and-switching/).</ArgTableRow>
<ArgTableRow arg="bridge-port-priority" typ="num">Priority of the dynamic bridge port, used by STP and RSTP to select the root port, and by MSTP to select the root port between regions. Has no effect when the bridge has `protocol-mode=none`. Range: 0..240.</ArgTableRow>
<ArgTableRow arg="bridge-path-cost" typ="num">Path cost of the dynamic bridge port, used by STP and RSTP to select the best path, and by MSTP to select the best path between regions. Has no effect when the bridge has `protocol-mode=none`. Range: 1..200000000.</ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num">Split-horizon value of the dynamic bridge port. Ports with the same value do not forward frames to each other, which prevents bridging loops and isolates traffic. Range: 0..429496729.</ArgTableRow>
<ArgTableRow arg="bridge-learning" typ="enum (default | no | yes) { default:0xffffffff, no:0, yes:1 }">
MAC learning on the dynamic bridge port.
- `default` (default) - Takes the value from the default profile of the PPP server; `yes` if this is that profile.
- `no` - MAC learning is off.
- `yes` - MAC learning is on.
</ArgTableRow>
<ArgTableRow arg="bridge-port-vid" typ="num">PVID of the dynamic bridge port. Has an effect only with `vlan-filtering=yes` on the bridge. Range: 1..4094. Default: 1.</ArgTableRow>
<ArgTableRow arg="bridge-port-trusted" typ="bool">Whether the dynamic bridge port is trusted for DHCP snooping. Default: no.</ArgTableRow>
<ArgTableRow arg="session-timeout" typ="time">Maximum time a session can stay connected. When it ends, the router disconnects the user. Default: not set, no limit.</ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="time">Time without traffic after which the router disconnects the user. Default: not set.</ArgTableRow>
<ArgTableRow arg="use-ipv6" typ="enum (default | no | yes | required) { default:0xffffffff, no:0, yes:1, required:2 }">
Whether IPv6 is negotiated on the link.
- `yes` (default) - IPv6 is allowed.
- `no` - IPv6 is off.
- `required` - The link is refused without IPv6.
- `default` - Takes the value from the default profile of the PPP server; `no` if this is that profile.
</ArgTableRow>
<ArgTableRow arg="use-mpls" typ="enum (default | no | yes | required) { default:0xffffffff, no:0, yes:1, required:2 }">
Whether MPLS is allowed over the link.
- `default` (default) - Takes the value from the default profile of the PPP server; `no` if this is that profile.
- `no` - MPLS is off.
- `yes` - MPLS is allowed.
- `required` - The link is refused without MPLS.
</ArgTableRow>
<ArgTableRow arg="use-compression" typ="enum (default | no | yes) { default:0xffffffff, no:0, yes:1 }">
Whether data compression is used. Has no effect on OpenVPN tunnels.
- `default` (default) - Takes the value from the default profile of the PPP server; `no` if this is that profile.
- `no` - Off.
- `yes` - On.
</ArgTableRow>
<ArgTableRow arg="use-encryption" typ="enum (default | no | yes | required) { default:0xffffffff, no:0, yes:1, required:2 }">
Whether data encryption (MPPE) is used. Has no effect on OpenVPN and SSTP tunnels.
- `default` (default) - Takes the value from the default profile of the PPP server; `no` if this is that profile.
- `no` - No encryption.
- `yes` - Encryption is used when the other side supports it.
- `required` - The link is refused without encryption.
</ArgTableRow>
<ArgTableRow arg="only-one" typ="enum (default | no | yes) { default:0xffffffff, no:0, yes:1 }">
Whether a user can have only one session at a time, on all PPP servers together. Also applies to users that a RADIUS server authenticates.
- `default` (default) - Takes the value from the default profile of the PPP server; `no` if this is that profile.
- `no` - A user can connect several times with the same name.
- `yes` - A second connection of the user is refused while the first one is active.
</ArgTableRow>
<ArgTableRow arg="change-tcp-mss" typ="enum (default | no | yes) { default:0xffffffff, no:0, yes:1 }">
Whether the router adjusts the MSS of TCP connections to the MTU of the link (IPv4 only).
- `default` (default) - Takes the value from the default profile of the PPP server; `no` if this is that profile.
- `no` - Off.
- `yes` - On.
</ArgTableRow>
<ArgTableRow arg="use-upnp" typ="enum (default | no | yes) { default:0xffffffff, no:0, yes:1 }">
Whether UPnP is allowed on the interface of the user.
- `default` (default) - Takes the value from the default profile of the PPP server; `no` if this is that profile.
- `no` - Off.
- `yes` - On.
</ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string">Rate limit of each user of the profile, applied as a dynamic simple queue when the user connects: `rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority [rx-rate-min[/tx-rate-min]]]]]]`. The rates are from the point of view of the router: `rx` is the upload of the user and `tx` the download. Rates are in bits per second, with an optional `k` or `M`. See [RADIUS](../../authentication-authorization-accounting/radius) for the details of the format.</ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (bottom | first) { bottom:0xffffffff, first:0 }">Place of the dynamic queue in the simple queue list: `bottom`, `first`, or the name of a queue to put it before.</ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none) { none:0 }">Simple queue that becomes the parent of the dynamic queues of the users. Default: none.</ArgTableRow>
<ArgTableRow arg="queue-type" typ="composite { upload-queue: enum
, download-queue: enum
 }">Queue types of the dynamic queue, as `upload/download`: the first is for the traffic received from the user, the second for the traffic sent to the user. Both must be given.</ArgTableRow>
<ArgTableRow arg="incoming-filter" typ="enum">Firewall filter chain for the packets that come from the user. The router adds a dynamic rule to the chain `ppp` that jumps to this chain. The chain `ppp` is reached only when a rule of another chain jumps to it.</ArgTableRow>
<ArgTableRow arg="outgoing-filter" typ="enum">Firewall filter chain for the packets that go to the user. The router adds a dynamic rule to the chain `ppp` that jumps to this chain. The chain `ppp` is reached only when a rule of another chain jumps to it.</ArgTableRow>
<ArgTableRow arg="address-list" typ="multi { address-list: enum
 }">Firewall address list to which the address of the user is added while the user is connected. On a PPP client, the address the client received.</ArgTableRow>
<ArgTableRow arg="interface-list" typ="enum">Interface list to which the interface of the user is added while the user is connected.</ArgTableRow>
<ArgTableRow arg="dns-server" typ="multi { address: ipAddr
 }">One or two IP addresses of DNS servers that the router gives to the PPP clients in the IPCP negotiation (RFC 1877). A client gets them only if it asks for them; a RouterOS client does with `use-peer-dns=yes`.</ArgTableRow>
<ArgTableRow arg="wins-server" typ="multi { address: ipAddr
 }">IP address of the WINS server that is offered to Windows clients.</ArgTableRow>
<ArgTableRow arg="on-up" typ="alt { script: string
 }">Script that runs when a user connects. It can read the variables `user`, `local-address`, `remote-address`, `caller-id`, `called-id` and `interface`. `interface` has the ID of the interface, not its name.</ArgTableRow>
<ArgTableRow arg="on-down" typ="alt { script: string
 }">Script that runs when a user disconnects. It has the same variables as `on-up`.</ArgTableRow>
</ArgTable>
