# neighbor

> List of currently active OSPF neighbors.

-----------

## routing/ospf/neighbor 
**Type:** Directory

List of currently active OSPF neighbors.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="V" typ="virtual">virtual</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="area" typ="enum"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">Name of the interface this neighbor was discovered.</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)">An IP address of the OSPF neighbor router.</ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="router-id" typ="ipAddr">Neighbor router's **RouterID**</ArgTableRow>
<ArgTableRow arg="dr" typ="ipAddr">An IP address of the Designated Router.</ArgTableRow>
<ArgTableRow arg="bdr" typ="ipAddr">An IP address of the Backup Designated Router.</ArgTableRow>
<ArgTableRow arg="state" typ="string">
- `Down` - No Hello packets have been received from a neighbor.
- `Attempt` - Applies only to NBMA clouds. The state indicates that no recent information was received from a neighbor.
- `Init` - Hello packet received from the neighbor, but bidirectional communication is not established (Its own RouterID is not listed in the Hello packet).
- `2-way` - This state indicates that bi-directional communication is established. DR and BDR elections occur during this state. Routers build adjacencies based on whether the router is DR or BDR, and the link is point-to-point or a virtual link.
- `ExStart` - Routers try to establish the initial sequence number that is used for the packet information exchange. The router with a higher ID becomes the master and starts the exchange.
- `Exchange` - Routers exchange database description (DD) packets.
- `Loading` - In this state, actual link state information is exchanged. Link State Request packets are sent to neighbors to request any new LSAs that were found during the Exchange state.
- `Full` - Adjacency is complete, and neighbor routers are fully adjacent. LSA information is synchronized between adjacent routers. Routers achieve the full state with their DR and BDR only. An exception is P2P links.
</ArgTableRow>
<ArgTableRow arg="state-changes" typ="num"></ArgTableRow>
<ArgTableRow arg="ls-retransmits" typ="num"></ArgTableRow>
<ArgTableRow arg="ls-requests" typ="num"></ArgTableRow>
<ArgTableRow arg="db-summaries" typ="num"></ArgTableRow>
<ArgTableRow arg="adjacency" typ="time">Elapsed time since adjacency was formed.</ArgTableRow>
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
</ArgTable>
