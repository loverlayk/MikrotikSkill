# user

> The /ip/hotspot/user menu lists the users that the HotSpot authenticates from the router itself, with their limits and counters. See the HotSpot guide.

-----------

## ip/hotspot/user 
**Type:** Directory

The `/ip/hotspot/user` menu lists the users that the HotSpot authenticates from the router itself, with their limits and counters. See the [HotSpot](../../../../authentication-authorization-accounting/hotspot-captive-portal) guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">The default entry, `default-trial`. It holds the counters and limits of trial users.</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">The user is disabled.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">The user is dynamic, for example a trial user.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="server" typ="enum (all) { all:0 }">HotSpot server on which the user can log in. Default: `all`.</ArgTableRow>
<ArgTableRow arg="name" typ="string" mandatory="1">User name. For the `mac` login method, the MAC address of the device.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password of the user.</ArgTableRow>
<ArgTableRow arg="otp-secret" typ="string">Secret for the time-based one-time passwords of the user.</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr">IP address that the device of the user gets through the HotSpot address translation. The user can still log in from any address.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC address from which the user can log in. `00:00:00:00:00:00` - any MAC address.</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">User profile from `/ip/hotspot/user/profile`. Default: `default`.</ArgTableRow>
<ArgTableRow arg="routes" typ="string">Routes that are added while the user is logged in, in the form `dst-address gateway metric`, for example `192.168.1.0/24 192.168.0.1 1`.</ArgTableRow>
<ArgTableRow arg="email" typ="string">E-mail address of the user. Informational.</ArgTableRow>
<ArgTableRow arg="limit-uptime" typ="time">Total time for which the user can be logged in, over all sessions. When it is reached, the user is logged out and cannot log in. `0s` - no limit.</ArgTableRow>
<ArgTableRow arg="limit-bytes-in" typ="num">Number of bytes that the user can send, over all sessions. When it is reached, the user is logged out and cannot log in. `0` - no limit.</ArgTableRow>
<ArgTableRow arg="limit-bytes-out" typ="num">Number of bytes that the user can receive, over all sessions. When it is reached, the user is logged out and cannot log in. `0` - no limit.</ArgTableRow>
<ArgTableRow arg="limit-bytes-total" typ="num">Number of bytes that the user can send and receive together, over all sessions. When it is reached, the user is logged out and cannot log in. `0` - no limit.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="uptime" typ="time">Time for which the user has been logged in, over all sessions.</ArgTableRow>
<ArgTableRow arg="bytes-in" typ="num">Bytes received from the user, over all sessions.</ArgTableRow>
<ArgTableRow arg="bytes-out" typ="num">Bytes sent to the user, over all sessions.</ArgTableRow>
<ArgTableRow arg="packets-in" typ="num">Packets received from the user, over all sessions.</ArgTableRow>
<ArgTableRow arg="packets-out" typ="num">Packets sent to the user, over all sessions.</ArgTableRow>
</ArgTable>
