# monitor

> RouterOS command reference for /system/ups/monitor.

-----------

## system/ups/monitor 
**Package:** ups
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="on-line" typ="bool"></ArgTableRow>
<ArgTableRow arg="on-battery" typ="bool"></ArgTableRow>
<ArgTableRow arg="transfer-cause" typ="string"></ArgTableRow>
<ArgTableRow arg="rtc-running" typ="bool"></ArgTableRow>
<ArgTableRow arg="runtime-left" typ="time"></ArgTableRow>
<ArgTableRow arg="offline-after" typ="time"></ArgTableRow>
<ArgTableRow arg="battery-charge" typ="num"></ArgTableRow>
<ArgTableRow arg="battery-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="line-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="output-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="load" typ="num"></ArgTableRow>
<ArgTableRow arg="temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="frequency" typ="num"></ArgTableRow>
<ArgTableRow arg="replace-battery" typ="bool"></ArgTableRow>
<ArgTableRow arg="smart-boost" typ="bool"></ArgTableRow>
<ArgTableRow arg="smart-trim" typ="bool"></ArgTableRow>
<ArgTableRow arg="overload" typ="bool"></ArgTableRow>
<ArgTableRow arg="low-battery" typ="bool"></ArgTableRow>
<ArgTableRow arg="self-test" typ="string"></ArgTableRow>
<ArgTableRow arg="hid-self-test" typ="enum (done-and-passed | done-and-warning | done-and-error | aborted | in-progress | no-test-initiated) { done-and-passed:1, done-and-warning:2, done-and-error:3, aborted:4, in-progress:5, no-test-initiated:6 }"></ArgTableRow>
</ArgTable>
