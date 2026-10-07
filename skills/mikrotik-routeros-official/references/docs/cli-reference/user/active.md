# active

> Currently logged-in management sessions. All properties are read-only. Terminate a session with /user/active/remove. See User for the full guide.

-----------

## user/active 
**Type:** Directory

Currently logged-in management sessions. All properties are read-only. Terminate a session with `/user/active/remove`. See [User](../../authentication-authorization-accounting/user) for the full guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="radius">User authenticated through RADIUS (see [`/user/aaa`](aaa)).</ArgTableRow>
<ArgTableRow arg="M" typ="by-romon">Session came through RoMON; `by-romon` holds the MAC address of the RoMON agent.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="when" typ="date">Date and time the session logged in.</ArgTableRow>
<ArgTableRow arg="name" typ="string">Name of the logged-in user from [`/user`](.).</ArgTableRow>
<ArgTableRow arg="address" typ="alt { ip: ipAddr
, ip6: ip6Addr
, address: macAddr
 }">Source address of the session: IP, IPv6 or MAC address.</ArgTableRow>
<ArgTableRow arg="by-romon" typ="macAddr">MAC address of the RoMON agent the session came through; set only for RoMON sessions (flag `M`).</ArgTableRow>
<ArgTableRow arg="via" typ="enum (unknown | winbox | console | telnet | ftp | web | ssh | mac-telnet | bandwidth-test | api | romon | rest-api) { unknown:0, winbox:1, console:2, telnet:3, ftp:4, web:5, ssh:6, mac-telnet:7, bandwidth-test:8, api:9, romon:10, rest-api:13 }">Management service the session connected through: `unknown`, `winbox`, `console`, `telnet`, `ftp`, `web`, `ssh`, `mac-telnet`, `bandwidth-test`, `api`, `romon` or `rest-api`.</ArgTableRow>
<ArgTableRow arg="group" typ="enum">Group of the logged-in user, which grants the session's rights.</ArgTableRow>
</ArgTable>
