# status

> RouterOS directory reference for /system/ptp/status.

-----------

## system/ptp/status 
**Conditions:** !smips
**Syscap:** ptp
**Type:** Directory
Current PTP port state per instance and interface.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum">Interface of the PTP port</ArgTableRow>
<ArgTableRow arg="state" typ="string">Current port state (for example `listening`, `master` or `slave`)</ArgTableRow>
<ArgTableRow arg="delay" typ="num">Measured path delay on slave ports, in nanoseconds</ArgTableRow>
<ArgTableRow arg="port-nr" typ="num">Port number of this port within the PTP data set</ArgTableRow>
<ArgTableRow arg="as-capable" typ="bool">Whether the port is asCapable per IEEE 802.1AS</ArgTableRow>
<ArgTableRow arg="neigh-freq-drift" typ="num">Measured frequency drift of the neighbour clock, in parts per billion</ArgTableRow>
</ArgTable>
