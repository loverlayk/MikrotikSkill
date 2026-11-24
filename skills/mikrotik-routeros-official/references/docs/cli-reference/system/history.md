# history

> List of configuration changes, made from any session (CLI, GUI or API). /undo and /redo take back or reapply the last change; each further /undo takes back the change before it. The list keeps the last 100 changes...

-----------

## system/history 
**Type:** Directory

List of configuration changes, made from any session (CLI, GUI or API). `/undo` and `/redo` take back or reapply the last change; each further `/undo` takes back the change before it. The list keeps the last 100 changes and is cleared when the router reboots. Changes made while safe mode is on are kept with the `F` flag and undone if the safe mode session ends without releasing safe mode. See [Configuration Management](../../getting-started/configuration-management/#undo-and-redo-changes).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="U" typ="undoable">The change can be undone with `/undo`.</ArgTableRow>
<ArgTableRow arg="R" typ="redoable">The change was undone and can be applied again with `/redo`.</ArgTableRow>
<ArgTableRow arg="F" typ="floating-undo">The change was made in safe mode. It is undone if the safe mode session ends without releasing safe mode.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="redo" typ="cfg">Command that applies the change again.</ArgTableRow>
<ArgTableRow arg="undo" typ="cfg">Command that takes the change back.</ArgTableRow>
<ArgTableRow arg="action" typ="string">Description of the change, for example `filter rule added`.</ArgTableRow>
<ArgTableRow arg="by" typ="string">User who made the change.</ArgTableRow>
<ArgTableRow arg="policy" typ="multi { array-id, policy: enum
 }">Policies the change needed.</ArgTableRow>
<ArgTableRow arg="time" typ="date">Time of the change.</ArgTableRow>
<ArgTableRow arg="trace" typ="string">Session that made the change, for example `ssh-cmd:admin@192.0.2.10/redo`.</ArgTableRow>
</ArgTable>
