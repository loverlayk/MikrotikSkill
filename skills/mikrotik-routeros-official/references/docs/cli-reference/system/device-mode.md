# device-mode

> Current device-mode settings. The mode and the per-feature switches apply at startup and can be changed only with update, which requires physical confirmation. See the Device mode guide.

-----------

## system/device-mode 
**Type:** Settings Directory

Current device-mode settings. The mode and the per-feature switches apply at startup and can be changed only with [`update`](update), which requires physical confirmation. See the [Device mode](../../../system-information-and-utilities/device-mode) guide.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mode" typ="enum">
Current device mode.
- `advanced` - For CCR and 1100 series devices; previously called `enterprise`.
- `basic` - For most other devices.
- `home` - For home routers.
- `rose` - For RDS and similar devices with wide disk use.
</ArgTableRow>
<ArgTableRow arg="allowed-versions" typ="string">Comma-separated list of RouterOS versions considered secure, used to block downgrades to vulnerable releases (for example `7.13+,6.49.8+`). An upgrade to a release that ships a newer list updates it; a downgrade does not. Ignored when `install-any-version` is enabled.</ArgTableRow>
<ArgTableRow arg="flagged" typ="bool">Whether the device is in the flagged state: the startup configuration analysis found signs of unauthorized access and disabled the suspicious configuration. Reviewed and cleared with `update flagged=no`.</ArgTableRow>
<ArgTableRow arg="flagging-enabled" typ="bool">Whether the configuration analysis for signs of unauthorized access runs at startup. Default: yes.</ArgTableRow>
<ArgTableRow arg="scheduler" typ="bool">Whether `/system/scheduler` is allowed to perform actions.</ArgTableRow>
<ArgTableRow arg="socks" typ="bool">Whether the SOCKS proxy in `/ip/socks` is allowed.</ArgTableRow>
<ArgTableRow arg="fetch" typ="bool">Whether `/tool/fetch` is allowed.</ArgTableRow>
<ArgTableRow arg="pptp" typ="bool">Whether `/interface/pptp-client` and `/interface/pptp-server` are allowed.</ArgTableRow>
<ArgTableRow arg="l2tp" typ="bool">Whether `/interface/l2tp-client` and `/interface/l2tp-server` are allowed.</ArgTableRow>
<ArgTableRow arg="bandwidth-test" typ="bool">Whether `/tool/bandwidth-test`, `/tool/bandwidth-server` and `/tool/speed-test` are allowed.</ArgTableRow>
<ArgTableRow arg="traffic-gen" typ="bool">Whether `/tool/traffic-generator`, `/tool/flood-ping` and `/tool/ping-speed` are allowed.</ArgTableRow>
<ArgTableRow arg="sniffer" typ="bool">Whether `/tool/sniffer` is allowed.</ArgTableRow>
<ArgTableRow arg="ipsec" typ="bool">Whether `/ip/ipsec` is allowed.</ArgTableRow>
<ArgTableRow arg="romon" typ="bool">Whether `/tool/romon` is allowed.</ArgTableRow>
<ArgTableRow arg="proxy" typ="bool">Whether the web proxy in `/ip/proxy` is allowed.</ArgTableRow>
<ArgTableRow arg="hotspot" typ="bool">Whether `/ip/hotspot` is allowed.</ArgTableRow>
<ArgTableRow arg="smb" typ="bool">Whether `/ip/smb` is allowed.</ArgTableRow>
<ArgTableRow arg="email" typ="bool">Whether `/tool/e-mail` is allowed.</ArgTableRow>
<ArgTableRow arg="zerotier" typ="bool">Whether `/zerotier` is allowed.</ArgTableRow>
<ArgTableRow arg="container" typ="bool">Whether container functionality (`/container`) is allowed.</ArgTableRow>
<ArgTableRow arg="install-any-version" typ="bool">Whether installing RouterOS versions outside the `allowed-versions` list is permitted.</ArgTableRow>
<ArgTableRow arg="partitions" typ="bool">Whether changing the partition count (`/partitions`) is allowed.</ArgTableRow>
<ArgTableRow arg="routerboard" typ="bool">Whether changing `/system/routerboard/settings` options (except auto-upgrade) and the SwOS/RouterOS transition on dual-boot devices is allowed.</ArgTableRow>
<ArgTableRow arg="attempt-count" typ="num">Number of unsuccessful device-mode update attempts since the last reset. After three, an `update` is refused and a reset window opens for the time set by the last `activation-timeout`; a button press or power cycle inside the window resets the counter. A confirmed update also resets it. Default: 0.</ArgTableRow>
</ArgTable>
