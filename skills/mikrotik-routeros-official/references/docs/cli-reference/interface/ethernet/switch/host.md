# host

> RouterOS directory reference for /interface/ethernet/switch/host.

-----------

## interface/ethernet/switch/host 
**Syscap:** rbswitch and oldswitch
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1">Name of the switch to which the MAC address is going to be assigned.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">Host's MAC address.</ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id, port: alt { port: enum
, trunk: iface_enum
 }
 }" mandatory="1">Name of the interface, a static MAC address can be mapped to more than one port, including the switch CPU port.</ArgTableRow>
<ArgTableRow arg="copy-to-cpu" typ="bool">Whether to send a frame copy to the switch CPU port from a frame with a matching MAC destination address (matching destination or source address for CRS3xx series switches).</ArgTableRow>
<ArgTableRow arg="redirect-to-cpu" typ="bool">Whether to redirect a frame to the switch CPU port from a frame with a matching MAC destination address (matching destination or source address for CRS3xx series switches).</ArgTableRow>
<ArgTableRow arg="drop" typ="bool">Whether to drop a frame with a matching MAC source address received on a certain port (matching destination or source address for CRS3xx series switches).</ArgTableRow>
<ArgTableRow arg="mirror" typ="bool">Whether to send a frame copy to the `mirror-target` port from a frame with a matching MAC destination address (matching destination or source address for CRS3xx series switches).</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num">VLAN ID for the statically added MAC address entry.</ArgTableRow>
<ArgTableRow arg="share-vlan-learned" typ="bool">Whether the static host MAC address lookup is used with shared-VLAN-learning (SVL) or independent-VLAN-learning (IVL).</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
</ArgTable>
