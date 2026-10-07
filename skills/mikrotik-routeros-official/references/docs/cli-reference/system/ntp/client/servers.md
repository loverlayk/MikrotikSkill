# servers

> NTP servers of the client. Static entries are added here or with servers in /system/ntp/client; entries learned from DHCP (when the DHCP client has use-peer-ntp=yes) are dynamic. See the NTP guide.

-----------

## system/ntp/client/servers 
**Type:** Directory

NTP servers of the client. Static entries are added here or with `servers` in [`/system/ntp/client`](../client); entries learned from DHCP (when the DHCP client has `use-peer-ntp=yes`) are dynamic. See the [NTP](../../../../system-information-and-utilities/ntp) guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The entry is disabled.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">Dynamic entry, learned from DHCP. Dynamic entries cannot be edited.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="address (flags=46D)" mandatory="1">IP address or domain name of the NTP server. IPv4 and IPv6 addresses can carry a `@vrf` suffix, and a link-local IPv6 address an `%interface` suffix. Domain names are resolved with `/ip/dns`; the result shows in `resolved-address`.</ArgTableRow>
<ArgTableRow arg="min-poll" typ="num">Shortest interval between queries to this server, as the power of 2 in seconds (6 means every 64 s). Must be lower than `max-poll`. Range: 3..17. Default: 6.</ArgTableRow>
<ArgTableRow arg="max-poll" typ="num">Longest interval between queries to this server, as the power of 2 in seconds (10 means every 1024 s). Range: 3..17. Default: 10.</ArgTableRow>
<ArgTableRow arg="iburst" typ="bool">When enabled, the client sends a burst of about a second interval queries right after the server is added, to get an initial estimate quickly. Default: yes.</ArgTableRow>
<ArgTableRow arg="auth-key" typ="enum (none) { none:0 }">Key from [`/system/ntp/key`](../key) used to authenticate replies from this server. Replies that fail authentication are rejected (crypto NAK) and the client does not synchronize. Default: none.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="resolved-address" typ="address (flags=46)">IP address that the domain name in `address` resolved to.</ArgTableRow>
</ArgTable>
