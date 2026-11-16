# active

> The /ip/hotspot/active menu lists the logged-in users. Remove an entry to log the user out.

-----------

## ip/hotspot/active 
**Type:** Directory

The `/ip/hotspot/active` menu lists the logged-in users. Remove an entry to log the user out.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="radius">The session is authenticated by a RADIUS server.</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">The network access of the user is blocked until the advertisement is shown.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="server" typ="enum">HotSpot server on which the user is logged in.</ArgTableRow>
<ArgTableRow arg="user" typ="string">User name.</ArgTableRow>
<ArgTableRow arg="domain" typ="string">Domain of the user, if it is split from the user name.</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr">IP address of the device.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the device.</ArgTableRow>
<ArgTableRow arg="login-by" typ="string">Login method of the session, for example `http-chap`, `mac-cookie`, or `trial`. `admin` - the session is created with `/ip/hotspot/active/login`.</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">Time since login.</ArgTableRow>
<ArgTableRow arg="session-time-left" typ="time">Time after which the user is logged out, from `session-timeout` or `limit-uptime`.</ArgTableRow>
<ArgTableRow arg="idle-time" typ="time">Time since the last traffic from the user.</ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="time">Idle timeout that applies to the session.</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="time">Keepalive timeout that applies to the session.</ArgTableRow>
<ArgTableRow arg="bytes-in" typ="num">Bytes received from the user in this session.</ArgTableRow>
<ArgTableRow arg="bytes-out" typ="num">Bytes sent to the user in this session.</ArgTableRow>
<ArgTableRow arg="packets-in" typ="num">Packets received from the user in this session.</ArgTableRow>
<ArgTableRow arg="packets-out" typ="num">Packets sent to the user in this session.</ArgTableRow>
<ArgTableRow arg="limit-bytes-in" typ="num">Bytes that the user can still send.</ArgTableRow>
<ArgTableRow arg="limit-bytes-out" typ="num">Bytes that the user can still receive.</ArgTableRow>
<ArgTableRow arg="limit-bytes-total" typ="num">Bytes that the user can still send and receive together.</ArgTableRow>
<ArgTableRow arg="advertisement" typ="enum (disabled | sleeping | pending | pending,block) { disabled:0, sleeping:1, pending:2, pending,block:3 }">State of the advertisement for this user.</ArgTableRow>
</ArgTable>
