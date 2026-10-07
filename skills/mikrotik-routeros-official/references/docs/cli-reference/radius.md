# radius

> RouterOS directory reference for /radius.

-----------

## radius 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="service" typ="ubit (ppp, login, hotspot, wireless, dhcp, ipsec, dot1x)"></ArgTableRow>
<ArgTableRow arg="called-id" typ="string"></ArgTableRow>
<ArgTableRow arg="domain" typ="string"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46v)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="secret" typ="string"></ArgTableRow>
<ArgTableRow arg="authentication-port" typ="num"></ArgTableRow>
<ArgTableRow arg="accounting-port" typ="num"></ArgTableRow>
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="radsec-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="accounting-backup" typ="bool"></ArgTableRow>
<ArgTableRow arg="realm" typ="string"></ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip-address: ipAddr
, ipv6-address: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (udp | radsec)"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="require-message-auth" typ="enum (no | yes-for-request-resp)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>
