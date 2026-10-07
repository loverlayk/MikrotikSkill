# monitor

> RouterOS command reference for /interface/l2tp-ether/monitor.

-----------

## interface/l2tp-ether/monitor 
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string">Current connection status.</ArgTableRow>
<ArgTableRow arg="circuit-id" typ="string">L2TPv3 circuit identifier.</ArgTableRow>
<ArgTableRow arg="cookie-length" typ="num">L2TPv3 cookie length.</ArgTableRow>
<ArgTableRow arg="header-format" typ="string">L2TPv3 header format.</ArgTableRow>
<ArgTableRow arg="l2-sublayer" typ="bool">Whether L2 sublayer is enabled.</ArgTableRow>
<ArgTableRow arg="remote-sess-id" typ="num">Remote session ID.</ArgTableRow>
<ArgTableRow arg="local-sess-id" typ="num">Local session ID.</ArgTableRow>
<ArgTableRow arg="control-conn-id" typ="num">Control connection ID.</ArgTableRow>
<ArgTableRow arg="peer-address" typ="string">IP address of the connected peer.</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">Encryption encoding used.</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">Connection uptime.</ArgTableRow>
</ArgTable>
