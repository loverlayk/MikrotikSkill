# interface

> The interface menu shows all interfaces that are currently participating in PIM and their statuses. This menu contains dynamic and read-only entries that get created by defined interface templates.

-----------

## routing/pimsm/interface 
**Conditions:** !smips
**Type:** Directory

The interface menu shows all interfaces that are currently participating in PIM and their statuses. This menu contains dynamic and read-only entries that get created by defined interface templates.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="P" typ="pim-enabled">The interface has PIM enabled on it.</ArgTableRow>
<ArgTableRow arg="G" typ="gmp-enabled">The interface is configured for GMP (IGMP/MLD) operation.</ArgTableRow>
<ArgTableRow arg="R" typ="designated-router">The router is the designated router (DR) on this interface's network.</ArgTableRow>
<ArgTableRow arg="J" typ="join-tracking">Join tracking is enabled on this interface.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum">The PIM instance this interface belongs to.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">The name of the interface.</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)">The IP address used by PIM on this interface.</ArgTableRow>
<ArgTableRow arg="pim.priority" typ="num">The DR priority of this router on the interface's network. The router with the highest DR priority is elected as the designated router.</ArgTableRow>
<ArgTableRow arg="pim.propagation-delay" typ="time">The propagation delay used by the DR on this interface's network, advertised in PIM hello messages.</ArgTableRow>
<ArgTableRow arg="pim.override-interval" typ="time">The override interval used by the DR on this interface's network, advertised in PIM hello messages.</ArgTableRow>
<ArgTableRow arg="gmp.robustness" typ="num">The configured robustness value of the IGMP/MLD querier on this interface.</ArgTableRow>
<ArgTableRow arg="gmp.query-interval" typ="time">The configured interval between IGMP/MLD General Queries sent on this interface.</ArgTableRow>
<ArgTableRow arg="gmp.query-response-interval" typ="time">The configured maximum response time advertised in IGMP/MLD General Queries on this interface.</ArgTableRow>
<ArgTableRow arg="gmp.last-member-query-interval" typ="time">The configured response time advertised in IGMP/MLD group-specific queries on this interface.</ArgTableRow>
<ArgTableRow arg="gmp.querier" typ="bool">Whether this router is currently the elected IGMP/MLD querier on this interface.</ArgTableRow>
<ArgTableRow arg="gmp.state.robustness" typ="num">The effective robustness value in use on this interface. When the router is not the elected querier, it adopts the robustness value announced by the elected querier in its queries.</ArgTableRow>
<ArgTableRow arg="gmp.state.query-interval" typ="time">The effective query interval in use on this interface. When the router is not the elected querier, it adopts the query interval announced by the elected querier in its queries.</ArgTableRow>
</ArgTable>
