# port

> RouterOS directory reference for /system/ptp/port.

-----------

## system/ptp/port 
**Conditions:** !smips
**Syscap:** ptp
**Type:** Directory
PTP ports: the interfaces that join a [`/system/ptp`](./) profile instance.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ptp" typ="enum" mandatory="1">The [`/system/ptp`](./) profile instance this port joins</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Interface used for PTP (the hardware must support PTP timestamping — see the supported device list in the [guide](../../../system-information-and-utilities/precision-time-protocol))</ArgTableRow>
<ArgTableRow arg="role" typ="enum (bmca | master | slave)">Port role selection: `bmca` (best master clock algorithm decides between master and slave), or a fixed `master` or `slave`</ArgTableRow>
<ArgTableRow arg="announce-interval" typ="num">Log2 interval between announce messages in seconds (for example -3...4 for 0.125s-16s)</ArgTableRow>
<ArgTableRow arg="sync-interval" typ="num">Log2 interval between sync messages in seconds</ArgTableRow>
<ArgTableRow arg="delay-interval" typ="num">Log2 interval between delay request messages in seconds (E2E mode)</ArgTableRow>
<ArgTableRow arg="pdelay-interval" typ="num">Log2 interval between peer delay messages in seconds (P2P mode)</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num">VLAN ID under which the port participates in PTP when the interface carries tagged PTP traffic</ArgTableRow>
</ArgTable>
