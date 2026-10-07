# socksify

> Service that forwards traffic redirected to it by a firewall NAT rule (action=socksify, typically in the dstnat chain) through an upstream SOCKS5 server. Changes to a record's properties apply after you disable and...

-----------

## ip/socksify 
**Type:** Directory

Service that forwards traffic redirected to it by a firewall NAT rule (`action=socksify`, typically in the `dstnat` chain) through an upstream SOCKS5 server. Changes to a record's properties apply after you disable and re-enable the record.

See [Socksify](../../network-management/socks/socksify) for the full documentation.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled (set by default)</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the socksify service record.</ArgTableRow>
<ArgTableRow arg="connection-timeout" typ="num">Time in seconds (0 to 3000) to wait for the SOCKS server and the destination during connection setup before aborting with an error. Set to 0 to disable the timeout. Default: `60`.</ArgTableRow>
<ArgTableRow arg="port" typ="num">Local TCP port the service listens on; the `socksify` NAT action redirects intercepted connections to this port. Default: `952`.</ArgTableRow>
<ArgTableRow arg="socks5-server" typ="ipAddr">IPv4 address of the upstream SOCKS5 server. IPv6 addresses are not accepted. Default: `0.0.0.0`.</ArgTableRow>
<ArgTableRow arg="socks5-port" typ="num">Listening port of the SOCKS5 server. Default: `1080`.</ArgTableRow>
<ArgTableRow arg="socks5-user" typ="string">Username for the upstream SOCKS5 server. Shown as plain text in `print detail` output. Default: empty.</ArgTableRow>
<ArgTableRow arg="socks5-password" typ="string">Password for the upstream SOCKS5 server. Shown as plain text in `print detail` output. Default: empty.</ArgTableRow>
</ArgTable>
