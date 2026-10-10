# rps

> RouterOS directory reference for /system/resource/irq/rps.

-----------

## system/resource/irq/rps 
**Syscap:** rps
**Type:** Directory
Receive Packet Steering (RPS) entries: each entry enables RPS for its interface (the packet-processing work of that interface's receive path is spread over the CPU cores in software). See the [Resource guide](../../../../diagnostics-monitoring-and-troubleshooting/resource) for when RPS pays off.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled entry (RPS steering off for this interface)</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Interface whose receive path is steered</ArgTableRow>
</ArgTable>
