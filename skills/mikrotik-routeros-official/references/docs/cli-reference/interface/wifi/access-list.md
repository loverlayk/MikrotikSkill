# access-list

> RouterOS directory reference for /interface/wifi/access-list.

-----------

## interface/wifi/access-list 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr" unset="1"></ArgTableRow>
<ArgTableRow arg="mac-address-mask" typ="macAddr" unset="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum { any:0 }" unset="1"></ArgTableRow>
<ArgTableRow arg="signal-range" typ="composite { min: num [-120 .. 120]
, max: num [-120 .. 120]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="allow-signal-out-of-range" typ="alt { signal-out-of-range-always: enum (always) { always:0 }
, signal-out-of-range-time: time
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="ssid-regexp" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="time" typ="super { start: time [0 .. 86400]
, [end] -time [0 .. 86400]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="days" typ="ubit (sun, mon, tue, wed, thu, fri, sat)" unset="1"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | reject | query-radius)" unset="1"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="multi-passphrase-group" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="radius-accounting" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="client-isolation" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="last-logged-in" typ="date" unset="1"></ArgTableRow>
<ArgTableRow arg="last-logged-out" typ="date" unset="1"></ArgTableRow>
<ArgTableRow arg="match-count" typ="num" unset="1"></ArgTableRow>
</ArgTable>
