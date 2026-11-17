# profile

> The /ip/hotspot/user/profile menu lists the user profiles. A profile holds the settings that users share: the rate limit, the timeouts, the number of devices, the address list, and the login and logout scripts. See...

-----------

## ip/hotspot/user/profile 
**Type:** Directory

The `/ip/hotspot/user/profile` menu lists the user profiles. A profile holds the settings that users share: the rate limit, the timeouts, the number of devices, the address list, and the login and logout scripts. See the [HotSpot](../../../../authentication-authorization-accounting/hotspot-captive-portal) guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">The default profile. It cannot be removed.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the profile.</ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (none) { none:0 }">IP pool from which the users of the profile get their address through the HotSpot address translation. Default: `none`.</ArgTableRow>
<ArgTableRow arg="session-timeout" typ="time">Time after which a user is logged out. The user can log in again. `0s` - no limit.</ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="super { idle-timeout: alt { symbolic-names: enum (none) { none:0 }
, time-interval: time
 }
 }">Time without traffic from a logged-in user after which the user is logged out. Default: `none`.</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="super { keepalive-timeout: alt { symbolic-names: enum (none) { none:0 }
, time-interval: time
 }
 }">Time for which the device of a logged-in user can be unreachable before the user is logged out. Default: `2m`.</ArgTableRow>
<ArgTableRow arg="status-autorefresh" typ="alt { symbolic-names: enum (none) { none:0 }
, time-interval: time
 }">Refresh interval of the status page. Default: `1m`.</ArgTableRow>
<ArgTableRow arg="shared-users" typ="enum (unlimited) { unlimited:0 }">Number of devices that can be logged in with the same user name at the same time. Default: `1`.</ArgTableRow>
<ArgTableRow arg="add-mac-cookie" typ="bool">Whether to create a MAC cookie for the users of the profile, for the `mac-cookie` login method. Default: `yes`.</ArgTableRow>
<ArgTableRow arg="mac-cookie-timeout" typ="time">Time for which a MAC cookie is valid. Default: `3d`.</ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string">Rate limit in the form `rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]]`. `rx` is what the router receives from the user (upload), `tx` is what it sends to the user (download). For example, `512k/2M` limits upload to 512 kbps and download to 2 Mbps. The router creates a dynamic simple queue with this limit for each logged-in user.</ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="super { queue: enum (bottom | first) { bottom:0xffffffff, first:0 }
 }">Position of the dynamic simple queue of a user in the queue list: `first`, `bottom`, or the name of a queue before which it is placed.</ArgTableRow>
<ArgTableRow arg="parent-queue" typ="super { queue: enum (none) { none:0 }
 }">Parent of the dynamic simple queue of a user. Default: `none`.</ArgTableRow>
<ArgTableRow arg="queue-type" typ="super { queue: enum
 }">Queue type of the dynamic simple queue of a user.</ArgTableRow>
<ArgTableRow arg="address-list" typ="multi { address-list: string
 }">Firewall address lists to which the address of each logged-in user is added.</ArgTableRow>
<ArgTableRow arg="incoming-filter" typ="string">Firewall filter chain for the packets from the users of the profile. Add a jump rule from the `hotspot` chain to this chain.</ArgTableRow>
<ArgTableRow arg="outgoing-filter" typ="string">Firewall filter chain for the packets to the users of the profile. Add a jump rule from the `hotspot` chain to this chain.</ArgTableRow>
<ArgTableRow arg="incoming-packet-mark" typ="string">Packet mark for the packets from the users of the profile.</ArgTableRow>
<ArgTableRow arg="outgoing-packet-mark" typ="string">Packet mark for the packets to the users of the profile.</ArgTableRow>
<ArgTableRow arg="on-login" typ="alt { script: string
 }">Script that runs when a user of the profile logs in. It can use the variables `$user`, `$username`, `$address`, `$"mac-address"`, and `$interface`.</ArgTableRow>
<ArgTableRow arg="on-logout" typ="alt { script: string
 }">Script that runs when a user of the profile logs out. In addition to the `on-login` variables it can use `$cause`, `$"uptime-secs"`, `$"bytes-in"`, `$"bytes-out"`, `$"bytes-total"`, `$"packets-in"`, `$"packets-out"`, and `$"packets-total"`.</ArgTableRow>
<ArgTableRow arg="transparent-proxy" typ="bool">Whether to send the HTTP requests of the logged-in users of the profile through the HotSpot proxy. Default: `no`.</ArgTableRow>
<ArgTableRow arg="open-status-page" typ="enum (http-login | always)">When to open the status page after login: `always` - also after a `mac` login; `http-login` - only after a login on the login page.</ArgTableRow>
<ArgTableRow arg="advertise" typ="bool">Whether to show advertisement pages to the users of the profile. Default: `no`.</ArgTableRow>
<ArgTableRow arg="advertise-url" typ="multi { url: string
 }">URLs of the advertisement pages. After the last one, the list starts again.</ArgTableRow>
<ArgTableRow arg="advertise-interval" typ="multi { time-interval: time
 }">Intervals between the advertisements. After the list ends, the last value is used.</ArgTableRow>
<ArgTableRow arg="advertise-timeout" typ="alt { symbolic-names: enum (immediately | never) { immediately:0, never:0xffffffff }
, time-interval: time
 }">Time to wait for the advertisement to be shown before the network access of the user is blocked: a time, `immediately`, or `never`.</ArgTableRow>
</ArgTable>
