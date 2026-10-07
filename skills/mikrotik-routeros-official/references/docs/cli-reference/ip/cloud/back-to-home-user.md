# back-to-home-user

> Back To Home users. Each user is a WireGuard client of the back-to-home-vpn interface with its own keys and addresses, and the router adds a dynamic peer for it. The Back To Home app creates a user for each tunnel it...

-----------

## ip/cloud/back-to-home-user 
**Syscap:** cloud-vpn
**Type:** Directory

Back To Home users. Each user is a WireGuard client of the `back-to-home-vpn` interface with its own keys and addresses, and the router adds a dynamic peer for it. The Back To Home app creates a user for each tunnel it sets up: `name` is the model identifier of the phone, for example `iPhone18,1`, and the comment is the tunnel name shown in the app. Several users can have the same name. [`show-client-config`](show-client-config) prints the client configuration of a user. Users can only be added while Back To Home runs (`vpn-status: running`); otherwise, `add` fails with `back-to-home vpn not enabled`. Revoking Back To Home (`back-to-home-vpn=revoked-and-disabled` in [`/ip/cloud`](../)) deletes all users. For an overview, see [Back To Home](../../../../network-management/cloud/back-to-home).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The user is disabled.</ArgTableRow>
<ArgTableRow arg="A" typ="active">The user is active.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the user. Names do not have to be unique; the Back To Home app uses the phone's model identifier. The client configuration carries the user's comment, or the name when there is no comment, in the `# Name` comment line, which the Back To Home app uses as the tunnel name.</ArgTableRow>
<ArgTableRow arg="expires" typ="alt { expires: enum (never) { never:0xFFFFFFFF }
, interval: time
, date-time: date
 }">When the user stops working: `never` (default), a date and time such as `"2026-10-01 00:00:00"`, or a time interval such as `1d`. The router converts an interval to a date. The value cannot be changed after the user is created: `set` accepts it but keeps the old date. To change it, create the user again.</ArgTableRow>
<ArgTableRow arg="client-dns" typ="address (flags=46/)">DNS server written into the user's client configuration (`DNS =`). Without it, the configuration has no DNS line and the client keeps its own DNS servers.</ArgTableRow>
<ArgTableRow arg="client-allowed-address" typ="multi { client-allowed-address: address (flags=46/)
 }">Addresses the client sends through the tunnel, written into the client configuration as `AllowedIPs` of the router's peer, for example `192.168.88.0/24` for access to the local network only. Default: empty (`0.0.0.0/0, ::/0`, all traffic).</ArgTableRow>
<ArgTableRow arg="allow-lan" typ="bool">Whether the user can reach the local network. With `no`, the router puts the user's address in the dynamic address list `back-to-home-lan-restricted-peers`, and a dynamic forward rule drops its traffic to the `LAN` interface list, so the user can only use the internet through the router. Default: no.</ArgTableRow>
<ArgTableRow arg="private-key" typ="string">Private key of the user's client configuration. The router generates it when it is not set.</ArgTableRow>
<ArgTableRow arg="public-key" typ="string">Public key of the user. The router derives it from the generated key when it is not set.</ArgTableRow>
<ArgTableRow arg="file-access" typ="enum (disabled | read-only | full)">
Access of the user to files in `file-access-path` through the File Share service. Adding a user with file access makes the router request the File Share certificate.
- `disabled` (default) - No file access.
- `read-only` - Read files.
- `full` - Read and change files.
</ArgTableRow>
<ArgTableRow arg="file-access-path" typ="string">Directory the user can access with `file-access`, as `/file/print` shows it. Required when `file-access` is not `disabled`; otherwise, adding the user fails with `invalid files path`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="client-address" typ="multi { address: address (flags=46/)
 }">IPv4 and IPv6 addresses of the user in the tunnel, the next free addresses from 192.168.216.0/24 and fc00:0:0:216::/64. The router assigns them; they cannot be set.</ArgTableRow>
<ArgTableRow arg="file-access-token" typ="string">Token the router generates for the user's file access. The client configuration includes it in a `# FilesToken` line when `file-access` is not `disabled`.</ArgTableRow>
</ArgTable>
