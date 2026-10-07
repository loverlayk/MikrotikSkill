# access-list

> RouterOS directory reference for /caps-man/access-list.

-----------

## caps-man/access-list 
**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
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
, [day] ,ubit (sun, mon, tue, wed, thu, fri, sat)
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | reject | query-radius)" unset="1"></ArgTableRow>
<ArgTableRow arg="ap-tx-limit" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="client-tx-limit" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="private-passphrase" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="radius-accounting" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="client-to-client-forwarding" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-mode" typ="enum (no-tag | use-tag | use-service-tag)" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" unset="1"></ArgTableRow>
</ArgTable>
