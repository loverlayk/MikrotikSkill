# lease

> Leases of the DHCP servers. Dynamic leases are created when clients get an address from a pool; static leases give a specific client a fixed address, a pool, or its own settings. For details, see DHCP Server.

-----------

## ip/dhcp-server/lease 
**Type:** Directory

Leases of the DHCP servers. Dynamic leases are created when clients get an address from a pool; static leases give a specific client a fixed address, a pool, or its own settings. For details, see [DHCP Server](../../../../network-management/dhcp/server).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The lease is disabled.</ArgTableRow>
<ArgTableRow arg="R" typ="radius">The lease was assigned by a RADIUS server.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">The lease is dynamic: it was created when a client got an address from the pool. Use `make-static` to turn it into a static lease.</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">The client is blocked (`block-access=yes`) and gets no reply from the server.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="alt { ip-address: ipAddr
, pool: enum
 }">IP address of a static lease, or the name of an IP pool to give the client an address from. With `0.0.0.0`, the address pool of the server is used.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the client the static lease is for.</ArgTableRow>
<ArgTableRow arg="use-src-mac" typ="bool">Whether to identify the client by the source MAC address of its packets instead of the client hardware address field (`chaddr`) of the DHCP message.</ArgTableRow>
<ArgTableRow arg="client-id" typ="string">Client identifier (option 61) of the client the static lease is for, in the format shown in `active-client-id`, for example `1:4e:97:a1:4c:d1:38`.</ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string">
Bandwidth limit for the client, as `rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time]]]]`. Rates are in bits per second, with an optional `k` or `M` suffix, and missing tx values are taken from the rx values. Only static leases can have a rate limit.

The server creates a dynamic simple queue named `dhcp-ds<hostname/MAC>` for the address of the lease, with this limit as `limit-at` and `max-limit`.
</ArgTableRow>
<ArgTableRow arg="routes" typ="object { route: composite { dst-address: address (flags=4/)
, gateway: [ composite { gateway: address (flags=46ivL)
, distance: [ num [1 .. 255]]
 }]
 }
 }">Routes the server adds while the lease is bound, as `dst-address/mask gateway distance` entries separated by commas, for example `10.77.0.0/24 172.31.255.105 5`.</ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (bottom | first) { bottom:0xffffffff, first:0 }">Where to place the dynamic simple queue created for this lease: `first` (default) at the top of `/queue/simple`, `bottom` at the end, or before the named queue.</ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none) { none:0 }">Parent of the dynamic simple queue created for this lease. Default: none.</ArgTableRow>
<ArgTableRow arg="queue-type" typ="enum">Queue type of the dynamic simple queue created for this lease.</ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, address-list: string
 }">Firewall address lists to which the address of the lease is added while the lease is bound.</ArgTableRow>
<ArgTableRow arg="server" typ="enum (all) { all:0 }">DHCP server the lease belongs to. With `all`, the static lease is valid on every server.</ArgTableRow>
<ArgTableRow arg="block-access" typ="bool">Whether to block the client: the server does not answer it, and the lease gets the `B` flag. Default: no.</ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool">Whether this lease and a DHCPv6 binding of the same client share one dynamic simple queue, which then contains both the IPv4 and the IPv6 address. Default: yes.</ArgTableRow>
<ArgTableRow arg="lease-time" typ="time">Lease time for this client. When not set, or set to `0s`, the `lease-time` of the server is used.</ArgTableRow>
<ArgTableRow arg="always-broadcast" typ="bool">Whether to broadcast replies to this client even when it has not set the broadcast flag. Default: no.</ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, option: enum
 }">Options (`/ip/dhcp-server/option`) to send to this client. They take precedence over the options of the server and of the network.</ArgTableRow>
<ArgTableRow arg="dhcp-option-set" typ="enum (none)">Option set (`/ip/dhcp-server/option/sets`) to send to this client. It takes precedence over the options of the server and of the network.</ArgTableRow>
<ArgTableRow arg="agent-circuit-id" typ="string">When set, the lease matches requests whose relay agent information (option 82) contains this circuit ID, even if the MAC address or client ID differ.</ArgTableRow>
<ArgTableRow arg="agent-remote-id" typ="string">When set, the lease matches requests whose relay agent information (option 82) contains this remote ID, even if the MAC address or client ID differ.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="enum (waiting | testing | declined | offered | bound | authorizing | conflict) { waiting:0, testing:1, declined:2, offered:3, bound:4, authorizing:5 }">
State of the lease:
- `waiting` - A static lease that is not in use.
- `testing` - The server is checking the address for conflicts (`conflict-detection`).
- `offered` - The server offered the address and waits for the client's request.
- `bound` - The client uses the address.
- `authorizing` - The server waits for the reply from the RADIUS server.
- `conflict` - Another host already uses the address. The lease keeps the address out of use for the lease time; `check-status` frees it when the other host no longer answers.
- `declined` - The client declined the address with a DHCPDECLINE message.
</ArgTableRow>
<ArgTableRow arg="expires-after" typ="time">Time until the lease expires.</ArgTableRow>
<ArgTableRow arg="last-seen" typ="alt { symbolic-names: enum (never | sometime) { never:0xffffffff, sometime:0xfffffffe }
, time: time
 }">Time since the server last received a request from the client, or `never`.</ArgTableRow>
<ArgTableRow arg="age" typ="time">Time since the lease was created.</ArgTableRow>
<ArgTableRow arg="active-address" typ="ipAddr">IP address the client uses.</ArgTableRow>
<ArgTableRow arg="active-mac-address" typ="macAddr">MAC address of the client that uses the lease.</ArgTableRow>
<ArgTableRow arg="active-client-id" typ="string">Client identifier (option 61) of the client that uses the lease.</ArgTableRow>
<ArgTableRow arg="active-server" typ="enum">DHCP server that serves the client.</ArgTableRow>
<ArgTableRow arg="active-agent-circuit-id" typ="string">Circuit ID from the relay agent information (option 82) of the client's request, in hex.</ArgTableRow>
<ArgTableRow arg="active-agent-remote-id" typ="string">Remote ID from the relay agent information (option 82) of the client's request, in hex.</ArgTableRow>
<ArgTableRow arg="active-agent-circuit-id-ascii" typ="string">Circuit ID from the relay agent information (option 82) of the client's request, as text.</ArgTableRow>
<ArgTableRow arg="active-agent-remote-id-ascii" typ="string">Remote ID from the relay agent information (option 82) of the client's request, as text.</ArgTableRow>
<ArgTableRow arg="host-name" typ="string">Host name the client sent (option 12).</ArgTableRow>
<ArgTableRow arg="class-id" typ="string">DHCP option 60 from last received DHCP request</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="macAddr">Source MAC address of the client's last request.</ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string">Key the server gave the client, in its reply when the client bound, for authenticating Reconfigure messages (RFC 6704, HMAC-MD5). Requires `use-reconfigure` on the server.</ArgTableRow>
<ArgTableRow arg="reconfigure-last-sent" typ="string">Replay-detection counter of the last Reconfigure message sent to the client. It increases with every Reconfigure message.</ArgTableRow>
<ArgTableRow arg="reconfigure-status" typ="string"></ArgTableRow>
</ArgTable>
