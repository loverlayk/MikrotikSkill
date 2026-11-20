# active

> Connected PPP users. Remove an entry to disconnect the user. See PPP AAA for the full guide.

-----------

## ppp/active 
**Type:** Directory

Connected PPP users. Remove an entry to disconnect the user. See [PPP AAA](../../authentication-authorization-accounting/ppp-aaa) for the full guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="radius">A RADIUS server authenticated the user.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">User name given at the login.</ArgTableRow>
<ArgTableRow arg="service" typ="enum (any | async | pptp | pppoe | l2tp | ovpn | sstp) { any:0, async:1, pptp:2, pppoe:3, l2tp:5, ovpn:6, sstp:7 }">PPP server the user is connected to.</ArgTableRow>
<ArgTableRow arg="caller-id" typ="string">Address the user connected from: an IP address for L2TP and PPTP, a MAC address for PPPoE.</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr">Address the user got from the router.</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">Time since the user connected.</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">Encryption and compression of the link, for example `MPPE128 stateless`.</ArgTableRow>
<ArgTableRow arg="session-id" typ="num">ID of the session.</ArgTableRow>
<ArgTableRow arg="limit-bytes-in" typ="num">Number of bytes the user can upload in this session. 0 means no limit.</ArgTableRow>
<ArgTableRow arg="limit-bytes-out" typ="num">Number of bytes the user can download in this session. 0 means no limit.</ArgTableRow>
</ArgTable>
