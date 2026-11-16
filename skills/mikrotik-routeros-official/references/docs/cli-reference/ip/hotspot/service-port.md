# service-port

> The /ip/hotspot/service-port menu lists the protocols for which the HotSpot has a helper, with their ports.

-----------

## ip/hotspot/service-port 
**Type:** Directory

The `/ip/hotspot/service-port` menu lists the protocols for which the HotSpot has a helper, with their ports.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The helper is disabled.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ports" typ="multi { port: num [1 .. 65535]
 }">Ports on which the helper handles connections.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the protocol, for example `ftp`.</ArgTableRow>
</ArgTable>
