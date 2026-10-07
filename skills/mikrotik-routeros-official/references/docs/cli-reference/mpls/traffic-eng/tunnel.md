# tunnel

> RouterOS directory reference for /mpls/traffic-eng/tunnel.

-----------

## mpls/traffic-eng/tunnel 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="F" typ="forwarding"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="from-address" typ="address (flags=46)" unset="1"></ArgTableRow>
<ArgTableRow arg="to-address" typ="address (flags=46)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="bandwidth" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="primary-path" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="secondary-paths" typ="multi { array-id, primary-path: enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="primary-retry-interval" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="secondary-standby" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="bandwidth-limit" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="auto-bandwidth-range" typ="composite { min: num [1 .. ]
, max: num [1 .. ]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="auto-bandwidth-reserve" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="auto-bandwidth-avg-interval" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="auto-bandwidth-update-interval" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="setup-priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="holding-priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="record-route" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="affinity-include-all" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="affinity-include-any" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="affinity-exclude" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="reoptimize-interval" typ="time" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="session" typ="string"></ArgTableRow>
<ArgTableRow arg="forwarding-on" typ="string"></ArgTableRow>
<ArgTableRow arg="primary" typ="string"></ArgTableRow>
<ArgTableRow arg="primary-pending" typ="string"></ArgTableRow>
<ArgTableRow arg="secondary" typ="string"></ArgTableRow>
<ArgTableRow arg="secondary-pending" typ="string"></ArgTableRow>
</ArgTable>
