# traffic-monitor

> Threshold trigger: run a script (on-event) when an interface's transmit or receive rate crosses a threshold.

-----------

## tool/traffic-monitor 
**Type:** Directory

Threshold trigger: run a [script](../../developer-guides/scripting/) (`on-event`) when an interface's transmit or receive rate crosses a threshold.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the traffic monitor entry</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Interface whose rate is watched</ArgTableRow>
<ArgTableRow arg="traffic" typ="enum (transmitted | received) { transmitted:1, received:2 }">Direction to watch: `transmitted` or `received`</ArgTableRow>
<ArgTableRow arg="trigger" typ="enum (above | below | always) { above:1, below:2, always:3 }">When `on-event` runs: when the rate crosses `above` the threshold, crosses `below` it, or `always` (on every poll).</ArgTableRow>
<ArgTableRow arg="threshold" typ="num">Traffic rate in bits per second that the trigger compares against</ArgTableRow>
<ArgTableRow arg="on-event" typ="alt { script: string
 }">Script run when the trigger condition is met</ArgTableRow>
</ArgTable>
