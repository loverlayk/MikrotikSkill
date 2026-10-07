# lease

> RouterOS directory reference for /dude/ros/lease.

-----------

## dude/ros/lease 
**Package:** dude
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="R" typ="radius"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="B" typ="blocked"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { ip-address: ipAddr
, prefix: ip6Addr
, pool: enum
 }"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="use-src-mac" typ="bool"></ArgTableRow>
<ArgTableRow arg="client-id" typ="string"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string"></ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="super { queue: enum (bottom | first) { bottom:0xffffffff, first:0 }
 }"></ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, address-list: string
 }"></ArgTableRow>
<ArgTableRow arg="server" typ="enum (all) { all:0 }"></ArgTableRow>
<ArgTableRow arg="block-access" typ="bool"></ArgTableRow>
<ArgTableRow arg="lease-time" typ="time"></ArgTableRow>
<ArgTableRow arg="always-broadcast" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, option: enum
 }"></ArgTableRow>
<ArgTableRow arg="dhcp-option-set" typ="enum (none)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="enum (waiting | testing | busy | offered | bound | authorizing) { waiting:0, testing:1, busy:2, offered:3, bound:4, authorizing:5 }"></ArgTableRow>
<ArgTableRow arg="expires-after" typ="time"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="alt { symbolic-names: enum (never | sometime) { never:0xffffffff, sometime:0xfffffffe }
, time: time
 }"></ArgTableRow>
<ArgTableRow arg="active-address" typ="alt { active-address: ipAddr
, active-address6: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="active-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="active-client-id" typ="string"></ArgTableRow>
<ArgTableRow arg="active-server" typ="enum"></ArgTableRow>
<ArgTableRow arg="host-name" typ="string"></ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="agent-circuit-id" typ="string"></ArgTableRow>
<ArgTableRow arg="agent-remote-id" typ="string"></ArgTableRow>
</ArgTable>
