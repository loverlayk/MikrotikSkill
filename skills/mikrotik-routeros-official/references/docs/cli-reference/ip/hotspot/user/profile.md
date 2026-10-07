# profile

> RouterOS directory reference for /ip/hotspot/user/profile.

-----------

## ip/hotspot/user/profile 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="session-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="super { idle-timeout: alt { symbolic-names: enum (none) { none:0 }
, time-interval: time
 }
 }"></ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="super { keepalive-timeout: alt { symbolic-names: enum (none) { none:0 }
, time-interval: time
 }
 }"></ArgTableRow>
<ArgTableRow arg="status-autorefresh" typ="alt { symbolic-names: enum (none) { none:0 }
, time-interval: time
 }"></ArgTableRow>
<ArgTableRow arg="shared-users" typ="enum (unlimited) { unlimited:0 }"></ArgTableRow>
<ArgTableRow arg="add-mac-cookie" typ="bool"></ArgTableRow>
<ArgTableRow arg="mac-cookie-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string"></ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="super { queue: enum (bottom | first) { bottom:0xffffffff, first:0 }
 }"></ArgTableRow>
<ArgTableRow arg="parent-queue" typ="super { queue: enum (none) { none:0 }
 }"></ArgTableRow>
<ArgTableRow arg="queue-type" typ="super { queue: enum
 }"></ArgTableRow>
<ArgTableRow arg="address-list" typ="multi { address-list: string
 }"></ArgTableRow>
<ArgTableRow arg="incoming-filter" typ="string"></ArgTableRow>
<ArgTableRow arg="outgoing-filter" typ="string"></ArgTableRow>
<ArgTableRow arg="incoming-packet-mark" typ="string"></ArgTableRow>
<ArgTableRow arg="outgoing-packet-mark" typ="string"></ArgTableRow>
<ArgTableRow arg="on-login" typ="alt { script: string
 }"></ArgTableRow>
<ArgTableRow arg="on-logout" typ="alt { script: string
 }"></ArgTableRow>
<ArgTableRow arg="transparent-proxy" typ="bool"></ArgTableRow>
<ArgTableRow arg="open-status-page" typ="enum (http-login | always)"></ArgTableRow>
<ArgTableRow arg="advertise" typ="bool"></ArgTableRow>
<ArgTableRow arg="advertise-url" typ="multi { url: string
 }"></ArgTableRow>
<ArgTableRow arg="advertise-interval" typ="multi { time-interval: time
 }"></ArgTableRow>
<ArgTableRow arg="advertise-timeout" typ="alt { symbolic-names: enum (immediately | never) { immediately:0, never:0xffffffff }
, time-interval: time
 }"></ArgTableRow>
</ArgTable>
