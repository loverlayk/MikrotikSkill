# session

> Active and finished sessions of users. Sessions are listed only when the router sends accounting.

-----------

## user-manager/session 
**Package:** userman-5
**Type:** Directory

Active and finished sessions of users. Sessions are listed only when the router sends accounting.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="A" typ="active">Active session.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="user" typ="enum">Name of the user.</ArgTableRow>
<ArgTableRow arg="acct-session-id" typ="string">Session ID from the router.</ArgTableRow>
<ArgTableRow arg="acct-multi-session-id" typ="string"></ArgTableRow>
<ArgTableRow arg="nas-port-type" typ="enum (async | sync | isdn-sync | isdn-sync-v120 | isdn-sync-v110 | virtual | piafs | hdlc | x25 | x75 | g3-fax | sdsl | adsl-cap | adsl-dmt | idsl | ethernet | dsl | cable | wireless | wireless-802.11) { async:0, sync:1, isdn-sync:2, isdn-sync-v120:3, isdn-sync-v110:4, virtual:5, piafs:6, hdlc:7, x25:8, x75:9, g3-fax:10, sdsl:11, adsl-cap:12, adsl-dmt:13, idsl:14, ethernet:15, dsl:16, cable:17, wireless:18, wireless-802.11:19 }">Port type from the router, for example `virtual` for a PPP tunnel.</ArgTableRow>
<ArgTableRow arg="nas-port-id" typ="string">Port name from the router.</ArgTableRow>
<ArgTableRow arg="nas-ip-address" typ="alt { ip-address: ipAddr
, ipv6-address: ip6Addr
 }">Address of the router.</ArgTableRow>
<ArgTableRow arg="nas-identifier" typ="string">Identity of the router.</ArgTableRow>
<ArgTableRow arg="calling-station-id" typ="string">Calling-Station-Id of the user: the address or the MAC address that the user connects from.</ArgTableRow>
<ArgTableRow arg="user-address" typ="ipAddr">IP address that the user has in the session.</ArgTableRow>
<ArgTableRow arg="status" typ="ubit (start, stop, interim, close-acked, expired)">Accounting messages received for the session (`start`, `interim`, `stop`) and `close-acked` for a closed session. A closed session can also have `expired`.</ArgTableRow>
<ArgTableRow arg="started" typ="date">Date and time when the session started.</ArgTableRow>
<ArgTableRow arg="ended" typ="date">Date and time when the session ended.</ArgTableRow>
<ArgTableRow arg="terminate-cause" typ="enum (user-request | lost-carrier | lost-service | idle-timeout | session-timeout | admin-reset | admin-reboot | port-error | nas-error | nas-request | nas-reboot | port-unneeded | port-preempted | port-suspended | service-unavailable | callback | user-error | host-request | supplicant-restart | reauthentication-failure | port-reinitialized | port-administratively-disabled | um-user-deleted | um-user-disabled | um-admin-request | um-nas-rebooted | um-simultaneous-sessions | um-limits-reached | um-limits-changed | um-unknown) { user-request:1, lost-carrier:2, lost-service:3, idle-timeout:4, session-timeout:5, admin-reset:6, admin-reboot:7, port-error:8, nas-error:9, nas-request:10, nas-reboot:11, port-unneeded:12, port-preempted:13, port-suspended:14, service-unavailable:15, callback:16, user-error:17, host-request:18, supplicant-restart:19, reauthentication-failure:20, port-reinitialized:21, port-administratively-disabled:22 }">Why the session ended, for example `user-request` or `um-limits-reached`.</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">Duration of the session.</ArgTableRow>
<ArgTableRow arg="download" typ="num">Bytes sent to the user.</ArgTableRow>
<ArgTableRow arg="upload" typ="num">Bytes received from the user.</ArgTableRow>
<ArgTableRow arg="last-accounting-packet" typ="date">Date and time of the last accounting message.</ArgTableRow>
</ArgTable>
