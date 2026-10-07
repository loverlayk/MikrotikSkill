# monitor

> RouterOS command reference for /interface/pwr-line/monitor.

-----------

## interface/pwr-line/monitor 
**Syscap:** pwrlink
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="connection-to-plc" typ="enum (ok | no-link) { ok:1, no-link:2 }"></ArgTableRow>
<ArgTableRow arg="tx-flow-control" typ="bool"></ArgTableRow>
<ArgTableRow arg="rx-flow-control" typ="bool"></ArgTableRow>
<ArgTableRow arg="phy-regs" typ="multi { array-id, method: string
 }"></ArgTableRow>
<ArgTableRow arg="plc-actual-network-key" typ="string"></ArgTableRow>
<ArgTableRow arg="plc-hw-platform" typ="string"></ArgTableRow>
<ArgTableRow arg="plc-sw-platform" typ="string"></ArgTableRow>
<ArgTableRow arg="plc-fw-version" typ="string"></ArgTableRow>
<ArgTableRow arg="plc-line-freq" typ="enum (unknown | 50Hz | 60Hz) { unknown:0, 50Hz:1, 60Hz:2 }"></ArgTableRow>
<ArgTableRow arg="plc-zero-crossing" typ="enum (not-yet-detected | detected | missing) { not-yet-detected:0, detected:4, missing:8 }"></ArgTableRow>
<ArgTableRow arg="plc-role" typ="enum (station | proxy-coordinator | central-coordinator) { station:0, proxy-coordinator:1, central-coordinator:2 }"></ArgTableRow>
<ArgTableRow arg="plc-station-count" typ="num"></ArgTableRow>
<ArgTableRow arg="plc-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="plc-cco-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="plc-station-info" typ="string"></ArgTableRow>
</ArgTable>
