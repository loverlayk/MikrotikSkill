# config

> Settings shared by all DHCP servers: how often leases are saved, and RADIUS accounting. For details, see DHCP Server.

-----------

## ip/dhcp-server/config 
**Type:** Settings Directory

Settings shared by all DHCP servers: how often leases are saved, and RADIUS accounting. For details, see [DHCP Server](../../../network-management/dhcp/server).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="store-leases-disk" typ="alt { symbolic-names: enum (immediately | never) { immediately:0, never:0xffffffff }
, time-interval: time
 }">How often leases are saved to disk: a time interval, `immediately`, or `never`. Saving less often reduces writes to the flash storage. Default: 5m.</ArgTableRow>
<ArgTableRow arg="accounting" typ="bool">Whether to send RADIUS accounting for the leases of servers that use RADIUS (`use-radius`). Default: yes.</ArgTableRow>
<ArgTableRow arg="interim-update" typ="time">Interval of RADIUS interim accounting updates. Default: 0s.</ArgTableRow>
<ArgTableRow arg="radius-password" typ="alt { user: enum (empty | same-as-user)
, password: string
 }">Password sent in RADIUS Access-Request messages: `empty`, `same-as-user` (the user name, which is the MAC address of the client), or a fixed password. Default: empty.</ArgTableRow>
</ArgTable>
