# aaa

> AAA settings for management logins: authentication against a RADIUS server and RADIUS accounting of management sessions. See User for the full guide.

-----------

## user/aaa 
**Type:** Settings Directory

AAA settings for management logins: authentication against a RADIUS server and RADIUS accounting of management sessions. See [User](../../authentication-authorization-accounting/user) for the full guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="use-radius" typ="bool">Authenticate management logins against a RADIUS server; a [`/radius`](../radius/) entry with `service=login` must exist. The local user database is consulted first — RADIUS is used only for user names not found locally. A `Mikrotik-Group` attribute in the Access-Accept selects the local group. Password authentication over RADIUS for SSH logins uses MS-CHAPv2. Default: no.</ArgTableRow>
<ArgTableRow arg="accounting" typ="bool">Send RADIUS accounting Start and Stop messages when a management session logs in and out. Management-session accounting carries no bandwidth counters. Default: yes.</ArgTableRow>
<ArgTableRow arg="interim-update" typ="time">Interval between Interim-Update accounting messages for active sessions. Default: 0s.</ArgTableRow>
<ArgTableRow arg="default-group" typ="enum">Group assigned to RADIUS-authenticated users when the server sends no group, or when the sent group is listed in `exclude-groups`. Default: read.</ArgTableRow>
<ArgTableRow arg="exclude-groups" typ="multi { group: enum
 }">Groups never accepted from the RADIUS server. If the server sends one of them, the user receives `default-group` instead; this protects against a rogue RADIUS server granting full rights. Default: none.</ArgTableRow>
</ArgTable>
