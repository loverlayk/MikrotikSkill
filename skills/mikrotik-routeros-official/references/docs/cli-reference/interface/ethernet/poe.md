# poe

> RouterOS directory reference for /interface/ethernet/poe.

-----------

## interface/ethernet/poe 
**Syscap:** (poe or poe-in)
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="poe-out" typ="enum (off | auto-on | forced-on) { off:0, auto-on:1, forced-on:2 }" syscap="(!poe-4p-power and poe)"></ArgTableRow>
<ArgTableRow arg="poe-voltage" typ="enum (auto | low | high) { auto:0, low:1, high:2 }" syscap="poe"></ArgTableRow>
<ArgTableRow arg="poe-priority" typ="num" syscap="poe"></ArgTableRow>
<ArgTableRow arg="power-cycle-ping-enabled" typ="bool" syscap="poe"></ArgTableRow>
<ArgTableRow arg="power-cycle-ping-address" typ="alt { ip: ipAddr
, ipv6: ip6Addr
, mac: macAddr
 }" syscap="poe"></ArgTableRow>
<ArgTableRow arg="power-cycle-ping-timeout" typ="time" syscap="poe"></ArgTableRow>
<ArgTableRow arg="power-cycle-interval" typ="alt { symbolic-names: enum (none) { none:0 }
, time-interval: time
 }" syscap="poe"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="port-type" typ="enum (poe-out | poe-in | poe-in/poe-out) { poe-out:0, poe-in:1, poe-in/poe-out:2 }" syscap="(poe or poe-in)"></ArgTableRow>
</ArgTable>
