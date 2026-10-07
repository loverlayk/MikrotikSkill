# pool

> IP pools are used to define ipv6 prefixes that can be used by various RouterOS utilities, for example, DHCP server, Point-to-Point servers and more. Whenever possible, the same IPv6 prefix is given out to each client...

-----------

## ipv6/pool 
**Type:** Directory

IP pools are used to define ipv6 prefixes that can be used by various RouterOS utilities, for example, DHCP server, Point-to-Point servers and more. Whenever possible, the same IPv6 prefix is given out to each client (OWNER/INFO pair).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the pool.</ArgTableRow>
<ArgTableRow arg="prefix" typ="ip6Prefix"></ArgTableRow>
<ArgTableRow arg="from-pool" typ="enum">Name of another pool from which to acquire prefix dynamically.</ArgTableRow>
<ArgTableRow arg="prefix-length" typ="num" mandatory="1">The option represents the prefix size that will be given out to the client.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="actual-prefix" typ="ip6Prefix"></ArgTableRow>
<ArgTableRow arg="valid-lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="preferred-lifetime" typ="time"></ArgTableRow>
</ArgTable>
