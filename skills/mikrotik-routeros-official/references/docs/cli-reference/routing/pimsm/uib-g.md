# uib-g

> The upstream information base menus show the any-source multicast (\,G) and source-specific multicast (S,G) groups and their statuses. These menus contain only read-only entries.

-----------

## routing/pimsm/uib-g 
**Conditions:** !smips
**Type:** Directory

The upstream information base menus show the any-source multicast (\*,G) and source-specific multicast (S,G) groups and their statuses. These menus contain only read-only entries.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="rp-local">The router itself is the Rendezvous Point (RP) for this group.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum">Name of the PIM instance the multicast group is created on.</ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46i)">The multicast group address.</ArgTableRow>
<ArgTableRow arg="rp" typ="address (flags=46i)">The address of the Rendezvous Point for this group.</ArgTableRow>
<ArgTableRow arg="rpf" typ="address (flags=46i)">The Reverse Path Forwarding (RPF) indicates the router address and outgoing interface that a Join message for that group is directed to.</ArgTableRow>
</ArgTable>
