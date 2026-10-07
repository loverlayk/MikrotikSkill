# clear

> Empties the buffer of a memory action, for example /system/logging/action/clear action=memory for the default buffer. A buffer with memory-stop-on-full=yes accepts new entries again after it is cleared. A disk action...

-----------

## system/logging/action/clear 
**Type:** Command

Empties the buffer of a memory action, for example `/system/logging/action/clear action=memory` for the default buffer. A buffer with `memory-stop-on-full=yes` accepts new entries again after it is cleared. A disk action refuses with `cleanup not supported on this target`. See [`/system/logging/action`](.) and [Log](../../../../diagnostics-monitoring-and-troubleshooting/log/).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="action" typ="enum">Name of the memory action whose buffer to empty.</ArgTableRow>
</ArgTable>
