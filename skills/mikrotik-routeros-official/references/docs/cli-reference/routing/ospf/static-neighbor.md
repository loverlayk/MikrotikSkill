# static-neighbor

> Static configuration of the OSPF neighbors. Required for non-broadcast multi-access networks.

-----------

## routing/ospf/static-neighbor 
**Type:** Directory

Static configuration of the OSPF neighbors. Required for non-broadcast multi-access networks.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="area" typ="enum" mandatory="1">Name of the area the neighbor belongs to.</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)" mandatory="1">The unicast IP address and an interface that can be used to reach the IP of the neighbor. For example, `address=1.2.3.4%ether1` indicates that a neighbor with IP `1.2.3.4` is reachable on the `ether1` interface.</ArgTableRow>
<ArgTableRow arg="instance-id" typ="num"></ArgTableRow>
<ArgTableRow arg="poll-interval" typ="time">How often to send hello messages to the neighbors that are in a `down` state (i.e., there is no traffic from them).</ArgTableRow>
</ArgTable>
