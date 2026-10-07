# igmp-interface-template

> RouterOS directory reference for /routing/pimsm/igmp-interface-template.

-----------

## routing/pimsm/igmp-interface-template 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The template is disabled.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum" mandatory="1">The PIM instance the template belongs to.</ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { interface: iface_enum
 }" unset="1">The interfaces that follow this template and run IGMP/MLD.</ArgTableRow>
<ArgTableRow arg="robustness" typ="num">The robustness value of the IGMP/MLD querier on the interfaces of this template.</ArgTableRow>
<ArgTableRow arg="query-interval" typ="time">How often to send out IGMP/MLD General Queries on the interfaces of this template.</ArgTableRow>
<ArgTableRow arg="query-response-interval" typ="time">The maximum response time advertised in IGMP/MLD General Queries on the interfaces of this template.</ArgTableRow>
<ArgTableRow arg="last-member-query-interval" typ="time">The response time advertised in IGMP/MLD group-specific queries on the interfaces of this template.</ArgTableRow>
</ArgTable>
