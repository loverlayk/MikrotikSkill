# server

> Ports where the router is an 802.1X authenticator. A port passes only EAPOL frames until a device on it authenticates with the RADIUS server (/radius entry with service=dot1x).

-----------

## interface/dot1x/server 
**Conditions:** !smips
**Type:** Directory

Ports where the router is an 802.1X authenticator. A port passes only EAPOL frames until a device on it authenticates with the RADIUS server (`/radius` entry with `service=dot1x`).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Ethernet interface or interface list.</ArgTableRow>
<ArgTableRow arg="accounting" typ="bool">Sends RADIUS accounting for the sessions. Default: `yes`.</ArgTableRow>
<ArgTableRow arg="interim-update" typ="time">Interval of the accounting updates of a session. Default: `0s` (no updates).</ArgTableRow>
<ArgTableRow arg="auth-types" typ="ubit (dot1x, mac-auth)">
Default: `dot1x`.
- `dot1x` - the device authenticates with EAP.
- `mac-auth` - the router asks the RADIUS server with the MAC address of the device as the user name. The device must send at least one frame.

With both, the router tries `dot1x` first and uses `mac-auth` when the device does not answer in three `retrans-timeout` periods.
</ArgTableRow>
<ArgTableRow arg="mac-auth-mode" typ="enum (mac-as-username | mac-as-username-and-password)">
User-Password of a MAC authentication request. Default: `mac-as-username`.
- `mac-as-username` - the password is empty.
- `mac-as-username-and-password` - the MAC address is also the password.
</ArgTableRow>
<ArgTableRow arg="radius-mac-format" typ="enum (XX:XX:XX:XX:XX:XX | XX-XX-XX-XX-XX-XX | XXXXXXXXXXXX | xx:xx:xx:xx:xx:xx | xx-xx-xx-xx-xx-xx | xxxxxxxxxxxx) { XX:XX:XX:XX:XX:XX:0, XX-XX-XX-XX-XX-XX:3, XXXXXXXXXXXX:5, xx:xx:xx:xx:xx:xx:7, xx-xx-xx-xx-xx-xx:10, xxxxxxxxxxxx:12 }">How the MAC address is written in User-Name and User-Password of a MAC authentication request. Default: `XX:XX:XX:XX:XX:XX`.</ArgTableRow>
<ArgTableRow arg="reauth-timeout" typ="time" deprecated="1"></ArgTableRow>
<ArgTableRow arg="reauth-period" typ="time">Authenticates each device again after this time: a Dot1X device gets a new EAP request, a MAC-authenticated device is checked with the RADIUS server again. Not set by default: devices are not authenticated again.</ArgTableRow>
<ArgTableRow arg="auth-timeout" typ="time">Total time for the EAP authentication of a device. Default: `1m`.</ArgTableRow>
<ArgTableRow arg="retrans-timeout" typ="time">Time after which the router sends an EAP request again when the device does not answer. Default: `30s`.</ArgTableRow>
<ArgTableRow arg="reject-vlan-id" typ="num">VLAN for the port when the RADIUS server answers with Access-Reject. Not used when the server does not answer. Needs a bridge with `vlan-filtering=yes`. Not set by default.</ArgTableRow>
<ArgTableRow arg="guest-vlan-id" typ="num">VLAN for the port when the device does not answer EAP requests in three `retrans-timeout` periods and `mac-auth` is not used. When a supplicant later authenticates, the port leaves this VLAN. Needs a bridge with `vlan-filtering=yes`. Not set by default.</ArgTableRow>
<ArgTableRow arg="server-fail-vlan-id" typ="num">VLAN for the port when the RADIUS server does not answer. Needs a bridge with `vlan-filtering=yes`. Not set by default.</ArgTableRow>
</ArgTable>
