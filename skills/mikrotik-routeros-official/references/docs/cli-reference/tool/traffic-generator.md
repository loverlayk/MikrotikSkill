# traffic-generator

> RouterOS settings reference for /tool/traffic-generator.

-----------

## tool/traffic-generator 
**Type:** Settings Directory
Overall traffic generator settings and commands. See the [Traffic Generator](../../../diagnostics-monitoring-and-troubleshooting/traffic-generator) guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="test-id" typ="num">ID of the test session. The `start` and `quick` commands accept `test-id` to override it. Default: 0.</ArgTableRow>
<ArgTableRow arg="measure-out-of-order" typ="bool">Whether received packets that arrive out of order are measured and reported. When enabled on a multi-core device, a single stream uses a single CPU core. Default: no on multi-core devices, yes on single-core devices.</ArgTableRow>
<ArgTableRow arg="latency-distribution-max" typ="time">Maximum latency range for latency-distribution measurements. RouterOS derives the `latency-distribution-measure-interval` range from this value. Default: 100us.</ArgTableRow>
<ArgTableRow arg="stats-samples-to-keep" typ="num">How many statistics samples to keep. Default: 100.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="running" typ="bool">Whether the traffic generator is currently running.</ArgTableRow>
<ArgTableRow arg="latency-distribution-samples" typ="num">Number of individual latency ranges into which latency-distribution-measure-interval is divided.</ArgTableRow>
<ArgTableRow arg="latency-distribution-measure-interval" typ="string">The total latency measurement range currently in use, for example 0-2.67us.</ArgTableRow>
</ArgTable>
