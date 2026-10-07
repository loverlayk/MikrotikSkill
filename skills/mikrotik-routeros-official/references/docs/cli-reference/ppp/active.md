# active

> RouterOS directory reference for /ppp/active.

-----------

## ppp/active 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="radius">radius</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="service" typ="enum (any | async | pptp | pppoe | l2tp | ovpn | sstp) { any:0, async:1, pptp:2, pppoe:3, l2tp:5, ovpn:6, sstp:7 }"></ArgTableRow>
<ArgTableRow arg="caller-id" typ="string"></ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="encoding" typ="string"></ArgTableRow>
<ArgTableRow arg="session-id" typ="num"></ArgTableRow>
<ArgTableRow arg="limit-bytes-in" typ="num"></ArgTableRow>
<ArgTableRow arg="limit-bytes-out" typ="num"></ArgTableRow>
</ArgTable>
