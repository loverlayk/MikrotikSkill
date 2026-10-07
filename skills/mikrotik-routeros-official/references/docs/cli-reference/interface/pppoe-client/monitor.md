# monitor

> Command will display current PPPoE status.

-----------

## interface/pppoe-client/monitor 
**Type:** Command

Command will display current PPPoE status.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string">
Current link status. Available values are:
- dialing,
- verifying password...,
- connected,
- disconnected.
</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">Connection time displayed in days, hours, minutes, and seconds.</ArgTableRow>
<ArgTableRow arg="active-links" typ="num">Number of bonded MLPPP connections (1 if not using MLPPP).</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">Encryption and encoding (if asymmetric, separated with '/') being used in this connection.</ArgTableRow>
<ArgTableRow arg="service-name" typ="string">Used service name.</ArgTableRow>
<ArgTableRow arg="ac-name" typ="string">Name of the Access Concentrator.</ArgTableRow>
<ArgTableRow arg="ac-mac" typ="macAddr">MAC address of the access concentrator (AC) the client is connected to.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Effective MTU of the link.</ArgTableRow>
<ArgTableRow arg="mru" typ="num">Effective MRU of the link.</ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr">IP address allocated to the client.</ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr">Remote IP address allocated to the server (i.e., gateway address).</ArgTableRow>
<ArgTableRow arg="local-ipv6-address" typ="ip6Addr">Local IPv6 address of the connection.</ArgTableRow>
<ArgTableRow arg="remote-ipv6-address" typ="ip6Addr">Remote IPv6 address of the connection.</ArgTableRow>
</ArgTable>
