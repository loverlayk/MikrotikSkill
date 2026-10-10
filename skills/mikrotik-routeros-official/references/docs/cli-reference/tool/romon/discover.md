# discover

> Discover the routers reachable through the RoMON overlay network. The table refreshes continuously (stop with q); duration stops after the given time.

-----------

## tool/romon/discover 
**Type:** Command

Discover the routers reachable through the [RoMON](../../../management-tools/romon) overlay network. The table refreshes continuously (stop with `q`); `duration` stops after the given time.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="A" typ="active">active</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="macAddr">RoMON ID (MAC address) of the discovered router</ArgTableRow>
<ArgTableRow arg="cost" typ="num">Accumulated cost of the RoMON path to the router (sum of the port costs configured with `/tool/romon/port`)</ArgTableRow>
<ArgTableRow arg="hops" typ="num">Number of RoMON hops between this router and the discovered router</ArgTableRow>
<ArgTableRow arg="path" typ="multi { array-id, path-hop: macAddr
 }">Path of RoMON IDs (MAC addresses) through which the discovery reply passed</ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num">The smallest L2 MTU on the RoMON path</ArgTableRow>
<ArgTableRow arg="identity" typ="string">The RouterOS system identity of the discovered router</ArgTableRow>
<ArgTableRow arg="version" typ="string">The RouterOS version of the discovered router</ArgTableRow>
<ArgTableRow arg="board" typ="string">The board name of the discovered router</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">The uptime of the discovered router</ArgTableRow>
</ArgTable>
