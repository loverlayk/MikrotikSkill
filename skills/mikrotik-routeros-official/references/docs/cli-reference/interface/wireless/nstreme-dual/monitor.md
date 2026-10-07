# monitor

> RouterOS command reference for /interface/wireless/nstreme-dual/monitor.

-----------

## interface/wireless/nstreme-dual/monitor 
**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="rx-signal-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="connected" typ="bool"></ArgTableRow>
<ArgTableRow arg="packets" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="bytes" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="frames" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="frame-bytes" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="hw-frames" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="hw-frame-bytes" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-retries-timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-retries-lost" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bad-seqs" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-duplicates" typ="num"></ArgTableRow>
</ArgTable>
