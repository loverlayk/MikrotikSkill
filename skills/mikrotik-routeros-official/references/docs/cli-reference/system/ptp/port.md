# port

> RouterOS directory reference for /system/ptp/port.

-----------

## system/ptp/port 
**Conditions:** !smips
**Syscap:** ptp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ptp" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="role" typ="enum (bmca | master | slave)"></ArgTableRow>
<ArgTableRow arg="announce-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="sync-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="delay-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="pdelay-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
</ArgTable>
