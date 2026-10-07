# server

> RouterOS directory reference for /interface/dot1x/server.

-----------

## interface/dot1x/server 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="accounting" typ="bool"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="time"></ArgTableRow>
<ArgTableRow arg="auth-types" typ="ubit (dot1x, mac-auth)"></ArgTableRow>
<ArgTableRow arg="mac-auth-mode" typ="enum (mac-as-username | mac-as-username-and-password)"></ArgTableRow>
<ArgTableRow arg="radius-mac-format" typ="enum (XX:XX:XX:XX:XX:XX | XX-XX-XX-XX-XX-XX | XXXXXXXXXXXX | xx:xx:xx:xx:xx:xx | xx-xx-xx-xx-xx-xx | xxxxxxxxxxxx) { XX:XX:XX:XX:XX:XX:0, XX-XX-XX-XX-XX-XX:3, XXXXXXXXXXXX:5, xx:xx:xx:xx:xx:xx:7, xx-xx-xx-xx-xx-xx:10, xxxxxxxxxxxx:12 }"></ArgTableRow>
<ArgTableRow arg="reauth-timeout" typ="time" deprecated="1"></ArgTableRow>
<ArgTableRow arg="reauth-period" typ="time"></ArgTableRow>
<ArgTableRow arg="auth-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="retrans-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="reject-vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="guest-vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="server-fail-vlan-id" typ="num"></ArgTableRow>
</ArgTable>
