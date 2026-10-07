# forwarding-table

> RouterOS directory reference for /mpls/forwarding-table.

-----------

## mpls/forwarding-table 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="L" typ="ldp"></ArgTableRow>
<ArgTableRow arg="P" typ="vpn"></ArgTableRow>
<ArgTableRow arg="T" typ="traffic-eng"></ArgTableRow>
<ArgTableRow arg="V" typ="vpls"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="label" typ="enum (expl-null | alert | expl-null6 | impl-null) { expl-null:0, alert:1, expl-null6:2, impl-null:3 }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (ldp | vpn | traffic-eng | vpls)"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="prefix" typ="address (flags=46/)"></ArgTableRow>
<ArgTableRow arg="nexthops" typ="object { label: enum (expl-null | alert | expl-null6 | impl-null) { expl-null:0, alert:1, expl-null6:2, impl-null:3 }
, nh: address
, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="te-sender" typ="string"></ArgTableRow>
<ArgTableRow arg="te-session" typ="string"></ArgTableRow>
<ArgTableRow arg="vpls" typ="iface_enum"></ArgTableRow>
</ArgTable>
