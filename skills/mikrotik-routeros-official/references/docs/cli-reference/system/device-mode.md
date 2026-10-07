# device-mode

> RouterOS settings reference for /system/device-mode.

-----------

## system/device-mode 
**Type:** Settings Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mode" typ="enum">Current device mode: basic, home, advanced, or ros.</ArgTableRow>
<ArgTableRow arg="allowed-versions" typ="string">List of RouterOS versions considered secure. Used to prevent downgrade to vulnerable releases.</ArgTableRow>
<ArgTableRow arg="flagged" typ="bool">Whether the device is in flagged state. Set to yes when suspicious configuration is detected.</ArgTableRow>
<ArgTableRow arg="flagging-enabled" typ="bool">Whether configuration analysis for suspicious code is enabled. Default: yes.</ArgTableRow>
<ArgTableRow arg="scheduler" typ="bool">Whether `/system/scheduler` is allowed.</ArgTableRow>
<ArgTableRow arg="socks" typ="bool">Whether `/ip/socks` is allowed.</ArgTableRow>
<ArgTableRow arg="fetch" typ="bool">Whether `/tool/fetch` is allowed.</ArgTableRow>
<ArgTableRow arg="pptp" typ="bool">Whether PPTP client and server interfaces are allowed.</ArgTableRow>
<ArgTableRow arg="l2tp" typ="bool">Whether L2TP client and server interfaces are allowed.</ArgTableRow>
<ArgTableRow arg="bandwidth-test" typ="bool">Whether `/tool/bandwidth-test` and `/tool/bandwidth-server` are allowed.</ArgTableRow>
<ArgTableRow arg="traffic-gen" typ="bool">Whether `/tool/traffic-generator`, `/tool/flood-ping`, and `/tool/ping-speed` are allowed.</ArgTableRow>
<ArgTableRow arg="sniffer" typ="bool">Whether `/tool/sniffer` is allowed.</ArgTableRow>
<ArgTableRow arg="ipsec" typ="bool">Whether `/ip/ipsec` is allowed.</ArgTableRow>
<ArgTableRow arg="romon" typ="bool">Whether `/tool/romon` is allowed.</ArgTableRow>
<ArgTableRow arg="proxy" typ="bool">Whether `/ip/proxy` is allowed.</ArgTableRow>
<ArgTableRow arg="hotspot" typ="bool">Whether `/ip/hotspot` is allowed.</ArgTableRow>
<ArgTableRow arg="smb" typ="bool">Whether `/ip/smb` is allowed.</ArgTableRow>
<ArgTableRow arg="email" typ="bool">Whether `/tool/e-mail` is allowed.</ArgTableRow>
<ArgTableRow arg="zerotier" typ="bool">Whether `/zerotier` is allowed.</ArgTableRow>
<ArgTableRow arg="container" typ="bool">Whether container functionality is allowed.</ArgTableRow>
<ArgTableRow arg="install-any-version" typ="bool">Whether downgrading to RouterOS versions outside the allowed-versions list is permitted.</ArgTableRow>
<ArgTableRow arg="partitions" typ="bool">Whether changing partition count is allowed.</ArgTableRow>
<ArgTableRow arg="routerboard" typ="bool">Whether `/system/routerboard/settings` (except auto-upgrade) is allowed, and SwOS/RouterOS transition on dual-boot devices.</ArgTableRow>
<ArgTableRow arg="attempt-count" typ="num">Number of unsuccessful device-mode change attempts.</ArgTableRow>
</ArgTable>
