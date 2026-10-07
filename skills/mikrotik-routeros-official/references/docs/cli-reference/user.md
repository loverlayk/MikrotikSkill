# user

> Router administration user accounts. Each user belongs to exactly one group that grants the rights (policies) the user has. See User for the full guide.

-----------

## user 
**Type:** Directory

Router administration user accounts. Each user belongs to exactly one [group](group) that grants the rights (policies) the user has. See [User](../../authentication-authorization-accounting/user) for the full guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="E" typ="expired">Password expired with [`/user/expire-password`](expire-password). At the next interactive login the user is asked to set a new password; setting a new password clears the flag.</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">User account is disabled and cannot log in.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Login user name. Letters, digits and the characters `_` `.` `#` `-` `@` are allowed; the name must end with a letter or a digit and cannot start with `.` or `-`.</ArgTableRow>
<ArgTableRow arg="group" typ="enum" mandatory="1">User group that grants the rights (policies) the user has.</ArgTableRow>
<ArgTableRow arg="password" typ="string" mandatory="1">Login password. Any characters are accepted, including spaces, symbols and UTF-8. An explicitly empty value (`password=""`) allows logging in with a blank password. The complexity policy from [`/user/settings`](settings) applies when set.</ArgTableRow>
<ArgTableRow arg="inactivity-timeout" typ="time">Idle time after which `inactivity-policy` is applied to an interactive console session. Range 00:01:00 to 1d00:00:00. Default: 10m.</ArgTableRow>
<ArgTableRow arg="inactivity-policy" typ="enum (none | logout | lockscreen)">
Action taken when `inactivity-timeout` expires:
- `none` (default) - The idle session keeps running.
- `logout` - Closes the idle session with the message "`<name>` was logged out due to inactivity".
- `lockscreen` - Locks the session ("Session is locked (Ctrl-D to Quit)") and asks for the user's password to resume; wrong passwords print "Sorry, try again.".
</ArgTableRow>
<ArgTableRow arg="address" typ="object { address: alt { address: ipPrefix
, address: ip6Prefix
 }
 }">IP address with mask or IPv6 prefix. When set, the user may log in only from matching source addresses; logins from other addresses are refused.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="last-logged-in" typ="date">Date and time of the user's last login.</ArgTableRow>
</ArgTable>
