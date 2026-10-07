# secret

> RouterOS directory reference for /ppp/secret.

-----------

## ppp/secret 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="service" typ="enum (any | async | pptp | pppoe | l2tp | ovpn | sstp) { any:0, async:1, pptp:2, pppoe:3, l2tp:5, ovpn:6, sstp:7 }"></ArgTableRow>
<ArgTableRow arg="caller-id" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="local-address" typ="super { address: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="super { remote-address: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="routes" typ="string"></ArgTableRow>
<ArgTableRow arg="ipv6-routes" typ="string"></ArgTableRow>
<ArgTableRow arg="remote-ipv6-prefix" typ="super { remote-prefix: ip6Prefix
 }"></ArgTableRow>
<ArgTableRow arg="limit-bytes-in" typ="num"></ArgTableRow>
<ArgTableRow arg="limit-bytes-out" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="last-logged-out" typ="date"></ArgTableRow>
<ArgTableRow arg="last-caller-id" typ="string"></ArgTableRow>
<ArgTableRow arg="last-disconnect-reason" typ="enum (peer-request | hung-up | idle-timeout | session-timeout | reset | reboot | port-error | nas-error | nas-request) { peer-request:1, hung-up:2, idle-timeout:4, session-timeout:5, reset:6, reboot:7, port-error:8, nas-error:9, nas-request:10 }"></ArgTableRow>
</ArgTable>
