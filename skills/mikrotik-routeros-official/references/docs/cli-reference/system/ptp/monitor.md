# monitor

> RouterOS command reference for /system/ptp/monitor.

-----------

## system/ptp/monitor 
**Conditions:** !smips
**Syscap:** ptp
**Type:** Command
Show the detailed status and synchronization accuracy of a PTP profile instance, `monitor <number or name>`.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the PTP profile instance</ArgTableRow>
<ArgTableRow arg="clock-id" typ="string">Identifier of the local clock</ArgTableRow>
<ArgTableRow arg="priority1" typ="num">The local priority1 value in the grandmaster election</ArgTableRow>
<ArgTableRow arg="priority2" typ="num">The local priority2 value in the grandmaster election</ArgTableRow>
<ArgTableRow arg="i-am-gm" typ="bool">Whether this device is the grandmaster clock</ArgTableRow>
<ArgTableRow arg="gm-clock-id" typ="string">Identifier of the grandmaster clock</ArgTableRow>
<ArgTableRow arg="gm-priority1" typ="num">The priority1 of the grandmaster clock</ArgTableRow>
<ArgTableRow arg="gm-priority2" typ="num">The priority2 of the grandmaster clock</ArgTableRow>
<ArgTableRow arg="master-clock-id" typ="string">Identifier of the master clock in the PTP path (the grandmaster clock or a boundary clock)</ArgTableRow>
<ArgTableRow arg="slave-port" typ="iface_enum">The local port connected towards the master clock</ArgTableRow>
<ArgTableRow arg="freq-drift" typ="num">Frequency drift between the master and the slave clock, in parts per billion</ArgTableRow>
<ArgTableRow arg="offset" typ="num">Time difference between the master and the slave clock, in nanoseconds</ArgTableRow>
<ArgTableRow arg="slave-port-delay" typ="num">Measured delay for packets between the two clocks, in nanoseconds (cable and transceiver lengths matter)</ArgTableRow>
</ArgTable>
