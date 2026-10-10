# interface

> RouterOS directory reference for /interface.

-----------

## interface 
**Type:** Directory
Interface list with counters and state. Each interface row counts its own packets and bytes; values beginning with `fp` show the Fast Path share of that traffic (streamlined CPU forwarding; HW-offloaded traffic shows in neither), and `tx-queue-drop` counts the packets dropped by the interface queue.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic (created automatically)</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="S" typ="slave">slave (member of a bridge or bond)</ArgTableRow>
<ArgTableRow arg="P" typ="passthrough">passthrough</ArgTableRow>
<ArgTableRow arg="w" typ="power-limited">power-limited (on PoE-out boards the power budget is in effect)</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the interface</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Configured MTU</ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num">Configured layer-2 MTU</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-name" typ="string">The factory-set name of the interface</ArgTableRow>
<ArgTableRow arg="type" typ="string">Interface type</ArgTableRow>
<ArgTableRow arg="actual-mtu" typ="num">MTU in effect (hardware/driver negotiated)</ArgTableRow>
<ArgTableRow arg="max-l2mtu" typ="num">Maximum layer-2 MTU the hardware/driver supports</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">VRF the interface is bound to (blank for the main routing table)</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the interface</ArgTableRow>
<ArgTableRow arg="last-link-down-time" typ="date">Time the link last went down</ArgTableRow>
<ArgTableRow arg="last-link-up-time" typ="date">Time the link last came up</ArgTableRow>
<ArgTableRow arg="link-downs" typ="num">How many times the link has gone down</ArgTableRow>
<ArgTableRow arg="rx-byte" typ="num">Bytes received</ArgTableRow>
<ArgTableRow arg="tx-byte" typ="num">Bytes transmitted</ArgTableRow>
<ArgTableRow arg="rx-packet" typ="num">Packets received</ArgTableRow>
<ArgTableRow arg="tx-packet" typ="num">Packets transmitted</ArgTableRow>
<ArgTableRow arg="rx-drop" typ="num">Packets received and dropped</ArgTableRow>
<ArgTableRow arg="tx-drop" typ="num">Packets dropped during transmission</ArgTableRow>
<ArgTableRow arg="tx-queue-drop" typ="num">Packets dropped by the interface queue (congestion signal)</ArgTableRow>
<ArgTableRow arg="rx-error" typ="num">Corrupted receive frames</ArgTableRow>
<ArgTableRow arg="tx-error" typ="num">Transmission errors</ArgTableRow>
<ArgTableRow arg="fp-rx-byte" typ="num">Bytes received over Fast Path</ArgTableRow>
<ArgTableRow arg="fp-tx-byte" typ="num">Bytes transmitted over Fast Path</ArgTableRow>
<ArgTableRow arg="fp-rx-packet" typ="num">Packets received over Fast Path</ArgTableRow>
<ArgTableRow arg="fp-tx-packet" typ="num">Packets transmitted over Fast Path</ArgTableRow>
<ArgTableRow arg="fp-rps-drop" typ="num">Packets dropped in the receive-packet-steering path</ArgTableRow>
</ArgTable>
