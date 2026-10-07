# monitor

> RouterOS command reference for /interface/bridge/port/mst-override/monitor.

-----------

## interface/bridge/port/mst-override/monitor 
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="port" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (inactive | in-bridge | in-bridge | disabled)"></ArgTableRow>
<ArgTableRow arg="identifier" typ="num"></ArgTableRow>
<ArgTableRow arg="port-id" typ="composite { priority: num
, number: num
 }"></ArgTableRow>
<ArgTableRow arg="role" typ="enum (disabled-port | root-port | designated-port | alternate-port | backup-port | master-port) { disabled-port:0, root-port:1, designated-port:2, alternate-port:3, backup-port:4, master-port:5 }"></ArgTableRow>
<ArgTableRow arg="learning" typ="bool"></ArgTableRow>
<ArgTableRow arg="forwarding" typ="bool"></ArgTableRow>
<ArgTableRow arg="internal-root-path-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="designated-bridge-id" typ="composite { number: num
, address: macAddr
 }"></ArgTableRow>
<ArgTableRow arg="designated-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="designated-internal-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="designated-port-id" typ="composite { priority: num
, number: num
 }"></ArgTableRow>
<ArgTableRow arg="designated-remaining-hops" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-rx-bpdu" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="discard-transitions" typ="num"></ArgTableRow>
<ArgTableRow arg="forward-transitions" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-rx-tc" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="topology-changes" typ="num"></ArgTableRow>
<ArgTableRow arg="last-topology-change" typ="time"></ArgTableRow>
</ArgTable>
