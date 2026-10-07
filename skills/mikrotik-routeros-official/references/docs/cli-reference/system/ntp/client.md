# client

> Network Time Protocol (NTP) client settings. The client synchronizes the router's clock with one or more NTP servers. Static servers are set in servers or in the servers list; the DHCP client adds servers dynamically...

-----------

## system/ntp/client 
**Type:** Settings Directory

Network Time Protocol (NTP) client settings. The client synchronizes the router's clock with one or more NTP servers. Static servers are set in `servers` or in the [servers](./servers) list; the DHCP client adds servers dynamically when its `use-peer-ntp` is enabled. See the [NTP](../../../../system-information-and-utilities/ntp) guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool">Enable the NTP client. When disabled, `status` is `stopped`. Default: no.</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (unicast | broadcast | multicast | manycast)">
How the client gets time from servers:
- `unicast` (default) - Query each configured server directly.
- `broadcast` - Listen for time broadcast by servers on the local network.
- `multicast` - Listen for time multicast by servers on the local network.
- `manycast` - Discover servers by sending manycast queries to the local network.
</ArgTableRow>
<ArgTableRow arg="servers" typ="multi { server-list: address (flags=46D)
 }">Space-separated list of NTP servers. Accepts IPv4 and IPv6 addresses (with `@vrf` or `%interface` suffixes where needed) and domain names, which are resolved with `/ip/dns`. Servers from this list also appear in the [servers](./servers) list alongside dynamic entries.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">VRF used for communication with the servers. Default: main.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="freq-drift" typ="num">Estimated frequency drift of the local clock, in PPM. Reset with [`reset-freq-drift`](./reset-freq-drift).</ArgTableRow>
<ArgTableRow arg="status" typ="enum (stopped | waiting | synchronized | using-local-clock)">
Current client state:
- `stopped` - The client is disabled.
- `waiting` - No server is usable yet (no answer, or all peers rejected).
- `synchronized` - The clock is synchronized to `synced-server`.
- `using-local-clock` - The local clock is used as the reference (requires `use-local-clock=yes` in [`/system/ntp/server`](../server)).
</ArgTableRow>
<ArgTableRow arg="synced-server" typ="address (flags=46D)">Address of the server the clock is synchronized to. `127.127.1.0` when the local clock is the reference.</ArgTableRow>
<ArgTableRow arg="synced-stratum" typ="num">Stratum of the synchronized source. Primary servers are stratum 1; each synchronization step adds one.</ArgTableRow>
<ArgTableRow arg="system-offset" typ="num">Offset between the local clock and the NTP source; shown in milliseconds when read with `print`.</ArgTableRow>
</ArgTable>
