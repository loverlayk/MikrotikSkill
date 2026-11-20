# secret

> PPP users of the router. All PPP servers use this list. See PPP AAA for the full guide.

-----------

## ppp/secret 
**Type:** Directory

PPP users of the router. All PPP servers use this list. See [PPP AAA](../../authentication-authorization-accounting/ppp-aaa) for the full guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The secret is disabled and cannot be used to log in.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the user.</ArgTableRow>
<ArgTableRow arg="service" typ="enum (any | async | pptp | pppoe | l2tp | ovpn | sstp) { any:0, async:1, pptp:2, pppoe:3, l2tp:5, ovpn:6, sstp:7 }">PPP server that the user can log in to: `async`, `pptp`, `pppoe`, `l2tp`, `ovpn` or `sstp`. A login to another server is refused. Default: any.</ArgTableRow>
<ArgTableRow arg="caller-id" typ="string">Address the user must connect from. For L2TP and PPTP it is the IP address of the client, for PPPoE the MAC address in capital letters. A login from another address is refused. Default: empty, any address.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password of the user. This is a [sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters) parameter.</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">[Profile](profile) of the user. Default: default.</ArgTableRow>
<ArgTableRow arg="local-address" typ="super { address: ipAddr
 }">Address of the router inside the tunnel for this user. Takes precedence over the profile.</ArgTableRow>
<ArgTableRow arg="remote-address" typ="super { remote-address: ipAddr
 }">Address of the user inside the tunnel. Takes precedence over the address or the pool of the profile.</ArgTableRow>
<ArgTableRow arg="routes" typ="string">Routes that the router adds while the user is connected, as `dst-address gateway metric`, for example `192.168.50.0/24 10.0.0.5 1`. Other forms are not accepted. Several routes are separated with commas. Ignored for OpenVPN.</ArgTableRow>
<ArgTableRow arg="ipv6-routes" typ="string">IPv6 networks that the router routes to the interface of the user while the user is connected, for example `2001:db8:99::/64`.</ArgTableRow>
<ArgTableRow arg="remote-ipv6-prefix" typ="super { remote-prefix: ip6Prefix
 }">IPv6 prefix of the user. The router adds it to the [ND prefix list](../ipv6/nd/prefix) of the interface of the user, so the client can configure an address with stateless address autoconfiguration.</ArgTableRow>
<ArgTableRow arg="limit-bytes-in" typ="num">Number of bytes the user can upload in one session. When it is reached, the router disconnects the user. Default: 0, no limit.</ArgTableRow>
<ArgTableRow arg="limit-bytes-out" typ="num">Number of bytes the user can download in one session. When it is reached, the router disconnects the user. Default: 0, no limit.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="last-logged-out" typ="date">Time of the last disconnect of the user.</ArgTableRow>
<ArgTableRow arg="last-caller-id" typ="string">Address the user connected from the last time.</ArgTableRow>
<ArgTableRow arg="last-disconnect-reason" typ="enum (peer-request | hung-up | idle-timeout | session-timeout | reset | reboot | port-error | nas-error | nas-request) { peer-request:1, hung-up:2, idle-timeout:4, session-timeout:5, reset:6, reboot:7, port-error:8, nas-error:9, nas-request:10 }">Reason of the last disconnect, for example `peer-request` (the client disconnected), `session-timeout`, or `nas-request` (the session was removed on the router).</ArgTableRow>
</ArgTable>
