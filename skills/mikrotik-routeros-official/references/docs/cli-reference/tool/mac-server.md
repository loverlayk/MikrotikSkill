# mac-server

> MAC Telnet server settings. The MAC server lets devices on the same layer-2 segment reach the router by its MAC address, without IP configuration: MAC Telnet (this menu), MAC WinBox (/tool/mac-server/mac-winbox) and...

-----------

## tool/mac-server 
**Type:** Settings Directory

MAC Telnet server settings. The MAC server lets devices on the same layer-2 segment reach the router by its MAC address, without IP configuration: MAC Telnet (this menu), MAC WinBox ([`/tool/mac-server/mac-winbox`](mac-winbox)) and MAC ping ([`/tool/mac-server/ping`](ping)). Open MAC Telnet sessions are listed in [`/tool/mac-server/sessions`](sessions). The IP firewall does not stop MAC access; limit it with `allowed-interface-list`. For examples, see [MAC server](../../../management-tools/mac-server).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="allowed-interface-list" typ="enum">Interface list on which the router accepts MAC Telnet connections. A bridge in the list also allows connections that arrive through its ports; a bridge port alone in the list does not. `none`, or a list without members, turns MAC Telnet off. A change applies to the next connection at once; open sessions stay. The default configuration sets `LAN`. Default: all.</ArgTableRow>
</ArgTable>
