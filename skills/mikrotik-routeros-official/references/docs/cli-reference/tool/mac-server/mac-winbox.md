# mac-winbox

> MAC WinBox server settings: on which interfaces WinBox can connect to the router by its MAC address. MAC Telnet has its own setting in /tool/mac-server. For examples, see MAC server.

-----------

## tool/mac-server/mac-winbox 
**Type:** Settings Directory

MAC WinBox server settings: on which interfaces WinBox can connect to the router by its MAC address. MAC Telnet has its own setting in [`/tool/mac-server`](.). For examples, see [MAC server](../../../management-tools/mac-server).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="allowed-interface-list" typ="enum">Interface list on which the router accepts MAC WinBox connections, set the same way as for MAC Telnet in [`/tool/mac-server`](.): put the bridge in the list, not its ports. `none` turns MAC WinBox off. The default configuration sets `LAN`. Default: all.</ArgTableRow>
</ArgTable>
