# default

> RouterOS settings reference for /ipv6/nd/prefix/default.

-----------

## ipv6/nd/prefix/default 
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="autonomous" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp6-pd-preferred" typ="bool"></ArgTableRow>
<ArgTableRow arg="valid-lifetime" typ="alt { special: enum (infinity) { infinity:0xffffffff }
, value: time
 }"></ArgTableRow>
<ArgTableRow arg="preferred-lifetime" typ="alt { special: enum (infinity) { infinity:0xffffffff }
, value: time
 }"></ArgTableRow>
</ArgTable>
