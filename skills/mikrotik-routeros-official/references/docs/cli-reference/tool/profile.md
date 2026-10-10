# profile

> Show CPU usage per RouterOS process type, summed for all cores or per core. See the Profiler guide.

-----------

## tool/profile 
**Type:** Command

Show CPU usage per RouterOS process type, summed for all cores or per core. See the [Profiler](../../diagnostics-monitoring-and-troubleshooting/profiler) guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="cpu" typ="enum (all | total) { all:0xfffffffe, total:0xfffffffd }" syscap="smp">Selects the CPU view on multi-core systems: `total` (default) sums the usage of all cores, `all` shows separate rows per core, and an integer (`0` .. number of cores minus one) shows only that core.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">The process classifier name (for example `wireless`, `console`). The per-core summary rows are named `cpu0`, `cpu1`, ..., and the summed view adds a `total` row.</ArgTableRow>
<ArgTableRow arg="cpu" typ="num" syscap="smp">The CPU core the row's usage belongs to (per-core view only).</ArgTableRow>
<ArgTableRow arg="usage" typ="num">Usage share of the CPU, in percent, measured since the previous output frame.</ArgTableRow>
</ArgTable>
