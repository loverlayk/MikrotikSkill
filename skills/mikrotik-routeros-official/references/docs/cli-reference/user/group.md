# group

> User groups define the rights (policies) granted to the group members. The built-in groups read, write and full cannot be removed. See User for the full guide.

-----------

## user/group 
**Type:** Directory

User groups define the rights (policies) granted to the group members. The built-in groups `read`, `write` and `full` cannot be removed. See [User](../../authentication-authorization-accounting/user) for the full guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Group name.</ArgTableRow>
<ArgTableRow arg="policy" typ="multi { array-id, array-id, policy: super { !
, policy: enum
 }
 }">
Rights granted to group members. Prefix a policy with `!` to revoke it. `add` revokes every policy it does not list, and a new group created without `policy` gets every policy negated (no rights). `set` changes only the policies it lists: `set policy=read,rest-api` on a group with `api` keeps `api`; `policy=!api` revokes it. Default: none.
- `local` - Log in on the local console.
- `telnet` - Log in through Telnet.
- `ssh` - Log in through SSH.
- `ftp` - Log in through FTP; allows reading, writing and erasing files (use together with `read` and `write`).
- `reboot` - Reboot the router.
- `read` - Read access to the router configuration.
- `write` - Write access to the configuration except user management; does not include `read`.
- `policy` - User management rights (use together with `write`); also allows seeing script variables created by other users (requires `test`) and designing WebFig skins (requires `sensitive`).
- `test` - Run ping, traceroute, bandwidth-test, wireless scan and snooper, fetch, email and other test tools.
- `winbox` - Log in through WinBox and use bandwidth-test authentication.
- `password` - Change the user's own password with `/password`.
- `web` - Log in through WebFig.
- `sniff` - Use the packet sniffer, torch and traffic generator.
- `sensitive` - See and change sensitive information.
- `api` - Access the router through the API.
- `romon` - Connect to the RoMON server.
- `rest-api` - Access the router through the REST API.
</ArgTableRow>
<ArgTableRow arg="skin" typ="enum">WebFig skin applied to group members logging in through WebFig. Default: default.</ArgTableRow>
</ArgTable>
