# uib-sg

> RouterOS directory reference for /routing/pimsm/uib-sg.

-----------

## routing/pimsm/uib-sg 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="K" typ="keepalive">keepalive</ArgTableRow>
<ArgTableRow arg="S" typ="spt-bit">The Shortest Path Tree (SPT) bit indicates whether forwarding is taking place on the (S,G) Shortest Path Tree or on the (\*,G) tree. A router can have an (S,G) state and still be forwarding on a (\*,G) state during the interval when the source-specific tree is being constructed. When the SPT bit is false, only the (\*,G) forwarding state is used to forward packets from S to G. When the SPT bit is true, both (\*,G) and (S,G) forwarding states are used.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum">Name of the PIM instance the multicast group is created on.</ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46i)">The multicast group address.</ArgTableRow>
<ArgTableRow arg="source" typ="address (flags=46i)">The source IP address of the multicast group.</ArgTableRow>
<ArgTableRow arg="rpf" typ="address (flags=46i)">The Reverse Path Forwarding (RPF) indicates the router address and outgoing interface that a Join message for that group is directed to.</ArgTableRow>
<ArgTableRow arg="register" typ="enum (join | join-pending | prune)"></ArgTableRow>
</ArgTable>
