# monitor

> RouterOS command reference for /system/resource/monitor.

-----------

## system/resource/monitor 
**Type:** Command
Live system resource monitor output (the table keeps refreshing; stops after `duration`).

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="cpu-used" typ="num">Total CPU usage across cores</ArgTableRow>
<ArgTableRow arg="cpu-used-per-core" typ="multi { cpu-used: num
 }" syscap="smp">One line per core with its percent usage</ArgTableRow>
<ArgTableRow arg="free-memory" typ="num">Free memory in KiB</ArgTableRow>
</ArgTable>
