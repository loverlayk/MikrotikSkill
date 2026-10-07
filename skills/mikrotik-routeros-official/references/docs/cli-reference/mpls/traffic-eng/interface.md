# interface

> RouterOS directory reference for /mpls/traffic-eng/interface.

-----------

## mpls/traffic-eng/interface 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="bandwidth" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="k-factor" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="resource-class" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="refresh-time" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="use-udp" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="blockade-k-factor" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="te-metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="igp-flood-period" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="up-flood-thresholds" typ="multi { array-id, up-flood-threshold: num [0 .. 100]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="down-flood-thresholds" typ="multi { array-id, down-flood-threshold: num [0 .. 100]
 }" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="remaining-bw" typ="num"></ArgTableRow>
<ArgTableRow arg="remaining-bw-prios" typ="multi { array-id, remaining-bw-prio: num
 }"></ArgTableRow>
<ArgTableRow arg="lih" typ="num"></ArgTableRow>
<ArgTableRow arg="local-address-ip" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="local-address-ip6" typ="address (flags=46)"></ArgTableRow>
</ArgTable>
