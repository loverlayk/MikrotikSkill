# flow

> RouterOS directory reference for /mpls/traffic-eng/flow.

-----------

## mpls/traffic-eng/flow 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="N" typ="ingress"></ArgTableRow>
<ArgTableRow arg="E" typ="egress"></ArgTableRow>
<ArgTableRow arg="F" typ="forwarding"></ArgTableRow>
<ArgTableRow arg="R" typ="reservation"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="session" typ="string"></ArgTableRow>
<ArgTableRow arg="sender" typ="string"></ArgTableRow>
<ArgTableRow arg="label" typ="num"></ArgTableRow>
<ArgTableRow arg="out-labels" typ="multi { array-id, out-label: num
 }"></ArgTableRow>
<ArgTableRow arg="out-nexthop" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="bw" typ="num"></ArgTableRow>
<ArgTableRow arg="style" typ="enum (unknown | shared | fixed) { unknown:0, shared:1, fixed:2 }"></ArgTableRow>
<ArgTableRow arg="psb" typ="string"></ArgTableRow>
<ArgTableRow arg="blockade" typ="string"></ArgTableRow>
<ArgTableRow arg="resv" typ="string"></ArgTableRow>
<ArgTableRow arg="rsb" typ="string"></ArgTableRow>
</ArgTable>
