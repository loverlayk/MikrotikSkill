# update

> RouterOS command reference for /system/device-mode/update.

-----------

## system/device-mode/update 
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="mode" typ="enum">Device mode to apply: basic, home, advanced, or ros.</ArgTableRow>
<ArgTableRow arg="flagged" typ="bool">Set to no to exit the flagged state. Requires physical confirmation.</ArgTableRow>
<ArgTableRow arg="flagging-enabled" typ="bool">Enable or disable configuration analysis for suspicious code. Default: yes.</ArgTableRow>
<ArgTableRow arg="scheduler" typ="bool">Allow or block `/system/scheduler`.</ArgTableRow>
<ArgTableRow arg="socks" typ="bool">Allow or block `/ip/socks`.</ArgTableRow>
<ArgTableRow arg="fetch" typ="bool">Allow or block `/tool/fetch`.</ArgTableRow>
<ArgTableRow arg="pptp" typ="bool">Allow or block PPTP client and server interfaces.</ArgTableRow>
<ArgTableRow arg="l2tp" typ="bool">Allow or block L2TP client and server interfaces.</ArgTableRow>
<ArgTableRow arg="bandwidth-test" typ="bool">Allow or block `/tool/bandwidth-test` and `/tool/bandwidth-server`.</ArgTableRow>
<ArgTableRow arg="traffic-gen" typ="bool">Allow or block `/tool/traffic-generator`, `/tool/flood-ping`, and `/tool/ping-speed`.</ArgTableRow>
<ArgTableRow arg="sniffer" typ="bool">Allow or block `/tool/sniffer`.</ArgTableRow>
<ArgTableRow arg="ipsec" typ="bool">Allow or block `/ip/ipsec`.</ArgTableRow>
<ArgTableRow arg="romon" typ="bool">Allow or block `/tool/romon`.</ArgTableRow>
<ArgTableRow arg="proxy" typ="bool">Allow or block `/ip/proxy`.</ArgTableRow>
<ArgTableRow arg="hotspot" typ="bool">Allow or block `/ip/hotspot`.</ArgTableRow>
<ArgTableRow arg="smb" typ="bool">Allow or block `/ip/smb`.</ArgTableRow>
<ArgTableRow arg="email" typ="bool">Allow or block `/tool/e-mail`.</ArgTableRow>
<ArgTableRow arg="zerotier" typ="bool">Allow or block `/zerotier`.</ArgTableRow>
<ArgTableRow arg="container" typ="bool">Allow or block container functionality.</ArgTableRow>
<ArgTableRow arg="install-any-version" typ="bool">Allow or block downgrading to RouterOS versions outside the allowed-versions list.</ArgTableRow>
<ArgTableRow arg="partitions" typ="bool">Allow or block changing partition count.</ArgTableRow>
<ArgTableRow arg="routerboard" typ="bool">Allow or block `/system/routerboard/settings` (except auto-upgrade) and SwOS/RouterOS transition on dual-boot devices.</ArgTableRow>
<ArgTableRow arg="activation-timeout" typ="time">Time to wait for physical confirmation (reset button press or power cycle) before canceling the update. Range: 00:00:10 to 1d00:00:00. Default: 5m.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="update" typ="string">Status message for a pending device-mode update. Prompts the user to confirm by power off or button press.</ArgTableRow>
</ArgTable>
