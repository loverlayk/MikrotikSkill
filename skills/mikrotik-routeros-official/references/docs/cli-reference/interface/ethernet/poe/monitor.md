# monitor

> RouterOS command reference for /interface/ethernet/poe/monitor.

-----------

## interface/ethernet/poe/monitor 
**Syscap:** (poe or poe-in)
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="port-type" typ="enum (poe-out | poe-in | poe-in/poe-out) { poe-out:0, poe-in:1, poe-in/poe-out:2 }" syscap="(poe or poe-in)"></ArgTableRow>
<ArgTableRow arg="poe-out" typ="enum (off | auto-on | forced-on | forced-on-a | forced-on-bt) { off:0, auto-on:1, forced-on:2, forced-on-a:3, forced-on-bt:4 }" syscap="poe"></ArgTableRow>
<ArgTableRow arg="poe-voltage" typ="enum (auto | low | high) { auto:0, low:1, high:2 }" syscap="poe">PoE out voltage selection</ArgTableRow>
<ArgTableRow arg="poe-out-status" typ="enum (disabled | waiting-for-load | powered-on | overload | short-circuit | voltage-too-low | current-too-low | power-cycle | voltage-too-high | controller-error | controller-upgrade | voltage-on-poe-in | no-valid-PSU | controller-init | low-voltage-too-low | lldp-power-off | low-voltage-pd-detected) { disabled:1, waiting-for-load:2, powered-on:3, overload:4, short-circuit:5, voltage-too-low:6, current-too-low:7, power-cycle:8, voltage-too-high:9, controller-error:10, controller-upgrade:11, voltage-on-poe-in:12, no-valid-PSU:13, controller-init:14, low-voltage-too-low:15, lldp-power-off:16, low-voltage-pd-detected:17 }"></ArgTableRow>
<ArgTableRow arg="poe-out-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="poe-out-current" typ="num"></ArgTableRow>
<ArgTableRow arg="poe-out-power" typ="num"></ArgTableRow>
<ArgTableRow arg="poe-out-power-pair" typ="enum (b | a | bt) { b:0, a:1, bt:2 }"></ArgTableRow>
<ArgTableRow arg="power-cycle-host-alive" typ="bool"></ArgTableRow>
<ArgTableRow arg="power-cycle-after" typ="time"></ArgTableRow>
</ArgTable>
