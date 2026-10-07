# pool

> IP pools are used to define a range of IP addresses that can be used by various RouterOS utilities, for example, DHCP server, Point-to-Point servers and more. Separate lists for IPv4 and IPv6 are available. Whenever...

-----------

## ip/pool 
**Type:** Directory

IP pools are used to define a range of IP addresses that can be used by various RouterOS utilities, for example, DHCP server, Point-to-Point servers and more. Separate lists for IPv4 and IPv6 are available. Whenever possible, the same IP address is given out to each client (OWNER/INFO pair).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the pool.</ArgTableRow>
<ArgTableRow arg="ranges" typ="multi { range: ipRange
 }" mandatory="1">IP address list of non-overlapping IP address ranges in the form of: `from1-to1,from2-to2,...,fromN-toN`. For example, `10.0.0.1-10.0.0.27,10.0.0.32-10.0.0.47`.</ArgTableRow>
<ArgTableRow arg="next-pool" typ="enum (none) { none:0 }">When IP address acquisition is performed from a pool that has no free addresses, and the next-pool property is set, then an IP address will be acquired from the next pool.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="total" typ="num"></ArgTableRow>
<ArgTableRow arg="used" typ="num"></ArgTableRow>
<ArgTableRow arg="available" typ="num"></ArgTableRow>
</ArgTable>
