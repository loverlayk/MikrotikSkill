# irq

> RouterOS directory reference for /system/resource/irq.

-----------

## system/resource/irq 
**Type:** Directory
IRQ counters per interrupt source. With `cpu=auto` the IRQ handling is balanced by interrupt counts (NAPI-assisted); pin an IRQ to a fixed core only when needed.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="o" typ="read-only">read-only (the CPU assignment is fixed by the hardware)</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="cpu" typ="num">The CPU the IRQ is pinned to; `auto` lets the scheduler balance by interrupt counts</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="irq" typ="num">IRQ identification number</ArgTableRow>
<ArgTableRow arg="users" typ="object { user: alt { interface: iface_enum
, other: string
 }
 }">Process/driver bound to the IRQ</ArgTableRow>
<ArgTableRow arg="active-cpu" typ="num">The CPU currently serving the IRQ on multicore systems</ArgTableRow>
<ArgTableRow arg="count" typ="num">The number of interrupts handled (on ethernet interfaces interrupt = packet)</ArgTableRow>
<ArgTableRow arg="per-cpu-count" typ="multi { count: num
 }">Per-CPU interrupt counts as a list</ArgTableRow>
</ArgTable>
