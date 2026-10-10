# cpu

> RouterOS directory reference for /system/resource/cpu.

-----------

## system/resource/cpu 
**Type:** Directory
Per-CPU usage breakdown of the system resource counters.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="cpu" typ="string">Identification number of the CPU whose usage is shown</ArgTableRow>
<ArgTableRow arg="load" typ="num">CPU usage in percent</ArgTableRow>
<ArgTableRow arg="irq" typ="num">IRQ usage in percent</ArgTableRow>
<ArgTableRow arg="disk" typ="num">Disk usage in percent</ArgTableRow>
</ArgTable>
