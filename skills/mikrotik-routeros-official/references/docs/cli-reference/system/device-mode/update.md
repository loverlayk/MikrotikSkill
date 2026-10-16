# update

> Starts a device-mode configuration change. The change activates after a button press or power cycle and reboots the device; if it is not confirmed within activation-timeout, it is canceled. Running a new update...

-----------

## system/device-mode/update 
**Type:** Command

Starts a device-mode configuration change. The change activates after a button press or power cycle and reboots the device; if it is not confirmed within `activation-timeout`, it is canceled. Running a new `update` cancels a pending one. See the [Device mode](../../../system-information-and-utilities/device-mode) guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="mode" typ="enum">
Device mode to apply. Specifying `mode` replaces the entire device-mode configuration except the other parameters given in the same command; omitted features get the new mode's defaults.
- `advanced` - Previously called `enterprise`.
- `basic` - For most other devices.
- `home` - For home routers.
- `rose` - For RDS and similar devices with wide disk use.
</ArgTableRow>
<ArgTableRow arg="flagged" typ="bool">Set to `no` to clear the flagged state, after inspecting the configuration for unauthorized changes. Requires physical confirmation.</ArgTableRow>
<ArgTableRow arg="flagging-enabled" typ="bool">Enable or disable the configuration analysis for signs of unauthorized access. Default: yes.</ArgTableRow>
<ArgTableRow arg="scheduler" typ="bool">Allow or block `/system/scheduler`.</ArgTableRow>
<ArgTableRow arg="socks" typ="bool">Allow or block `/ip/socks`.</ArgTableRow>
<ArgTableRow arg="fetch" typ="bool">Allow or block `/tool/fetch`.</ArgTableRow>
<ArgTableRow arg="pptp" typ="bool">Allow or block PPTP client and server interfaces.</ArgTableRow>
<ArgTableRow arg="l2tp" typ="bool">Allow or block L2TP client and server interfaces.</ArgTableRow>
<ArgTableRow arg="bandwidth-test" typ="bool">Allow or block `/tool/bandwidth-test`, `/tool/bandwidth-server` and `/tool/speed-test`.</ArgTableRow>
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
<ArgTableRow arg="activation-timeout" typ="time">How long to wait for the physical confirmation (button press or power cycle) before the update is canceled. Also sets the length of the `attempt-count` reset window when an update is refused after three unsuccessful attempts. Range: 00:00:10 to 1d00:00:00. Default: 5m.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="update" typ="string">Status of a pending update with the time left to confirm it; empty when no update is pending.</ArgTableRow>
</ArgTable>
