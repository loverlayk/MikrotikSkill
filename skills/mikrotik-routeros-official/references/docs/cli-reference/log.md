# log

> Log entries the router keeps in memory: the default memory buffer, the buffers of other memory actions and the newest entries of disk actions. /log/print lists the entries of every buffer; where buffer= limits the...

-----------

## log 
**Type:** Directory

Log entries the router keeps in memory: the default `memory` buffer, the buffers of other memory actions and the newest entries of disk actions. `/log/print` lists the entries of every buffer; `where buffer=<action name>` limits the output to one of them, `follow` keeps printing new entries, `follow-only` prints only new ones, `with-extra-info` appends the extra fields, and `file=<name>` saves the output to `<name>.txt`. The `/log/info`, `/log/warning`, `/log/error` and `/log/debug` commands add a message with the topics `script` and the level, the same as `:log` in a script. Which messages are kept is set by the rules in [`/system/logging`](system/logging/). See [Log](../diagnostics-monitoring-and-troubleshooting/log/).

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="buffer" typ="enum">Buffer the entry belongs to: `memory` for the default buffer, or the name of another memory action or of a disk action. A disk action's newest entries show here, and after a reboot the entries of its active file. `/log/print` without a filter lists every buffer, so a message passed to several actions shows once per action.</ArgTableRow>
<ArgTableRow arg="time" typ="date">Date and time the entry was added.</ArgTableRow>
<ArgTableRow arg="topics" typ="multi { array-id, topic: enum
 }">Topics of the entry, for example `system,info,account`. The rules in [`/system/logging`](system/logging/) select messages by these topics.</ArgTableRow>
<ArgTableRow arg="message" typ="string">Text of the entry, with the rule's `prefix` in front when the rule has one.</ArgTableRow>
<ArgTableRow arg="extra-info" typ="string">Extra `key=value` fields that some messages carry, for example a login: `app=ssh duser=admin outcome=success src=192.0.2.1`. `print with-extra-info` appends them to the message, and the `cef` remote log format sends them after `msg=`.</ArgTableRow>
</ArgTable>
