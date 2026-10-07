# mac-telnet

> Opens a MAC Telnet session to a device on the same layer-2 segment, by its MAC address. The client asks for a user name and password. When the device does not answer or refuses the connection, the command returns to...

-----------

## tool/mac-telnet 
**Type:** Command

Opens a MAC Telnet session to a device on the same layer-2 segment, by its MAC address. The client asks for a user name and password. When the device does not answer or refuses the connection, the command returns to the prompt without an error message. For examples, see [MAC server](../../management-tools/mac-server).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="host" typ="enum ()">MAC address of the device to connect to.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" unset="1">Interface to send the connection attempts out of. Without it, the client sends them out of every interface.</ArgTableRow>
</ArgTable>
