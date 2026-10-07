# detect-internet

> Settings of Detect Internet, which gives each interface of detect-interface-list a state (see state) from its link, the routes through it and whether cloud.mikrotik.com answers on UDP port 30000 through it, and adds...

-----------

## interface/detect-internet 
**Type:** Settings Directory

Settings of Detect Internet, which gives each interface of `detect-interface-list` a state (see [`state`](state)) from its link, the routes through it and whether `cloud.mikrotik.com` answers on UDP port 30000 through it, and adds the interfaces to the LAN, WAN and internet interface lists set here. See [Detect Internet](../../../diagnostics-monitoring-and-troubleshooting/detect-internet).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="detect-interface-list" typ="enum">Interface list whose interfaces Detect Internet watches. `none` turns Detect Internet off. Default: none.</ArgTableRow>
<ArgTableRow arg="lan-interface-list" typ="enum">Interface list that gets the interfaces in the `lan` state as dynamic members, with the comment `LAN detected`. Default: none.</ArgTableRow>
<ArgTableRow arg="wan-interface-list" typ="enum">Interface list that gets the interfaces in the `wan` state as dynamic members, with the comment `WAN detected`. Default: none.</ArgTableRow>
<ArgTableRow arg="internet-interface-list" typ="enum">Interface list that gets the interfaces in the `internet` state as dynamic members, with the comment `INTERNET detected`. Default: none.</ArgTableRow>
<ArgTableRow arg="request-interval" typ="time">Sets how often the router checks the cloud: it sends its UDP message to `cloud.mikrotik.com` at half of this interval, about every minute with `2m`. With the default, an `internet` interface falls back to `wan` after about 4 minutes without an answer. Range: 1m..1d. Default: 2m.</ArgTableRow>
</ArgTable>
