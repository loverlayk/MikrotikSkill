# socks

> The SOCKS proxy server accepts SOCKS client connections on its TCP port and relays them to the requested destinations, applying the access rules and, optionally, users authentication. For more information, see SOCKS.

-----------

## ip/socks 
**Type:** Settings Directory

The SOCKS proxy server accepts SOCKS client connections on its TCP port and relays them to the requested destinations, applying the [`access`](access) rules and, optionally, [`users`](users) authentication. For more information, see [SOCKS](../../../network-management/socks).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool">Whether the SOCKS proxy server runs. Default: `no`.</ArgTableRow>
<ArgTableRow arg="port" typ="num">TCP port the proxy listens on. Default: `1080`.</ArgTableRow>
<ArgTableRow arg="connection-idle-timeout" typ="time">Time after which an idle proxied connection is terminated. Default: `2m`.</ArgTableRow>
<ArgTableRow arg="max-connections" typ="num">Maximum number of simultaneous proxied connections, `1` to `500`. Default: `200`.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">VRF the proxy listens in. With a VRF other than `main`, the port is reachable only inside that VRF. Default: `main`.</ArgTableRow>
<ArgTableRow arg="version" typ="enum (4 | 5)">
SOCKS protocol version the server accepts.
- `4` (default) - Accept only SOCKS4 clients.
- `5` - Accept only SOCKS5 clients. Required for password authentication and for the [`socksify`](../socksify) service, which always speaks SOCKS5.
</ArgTableRow>
<ArgTableRow arg="auth-method" typ="enum (none | password)">
Authentication the server requires from clients.
- `none` (default) - No authentication.
- `password` - Clients must authenticate with a username and password from [`users`](users). If no users exist, every connection is rejected.
</ArgTableRow>
</ArgTable>
