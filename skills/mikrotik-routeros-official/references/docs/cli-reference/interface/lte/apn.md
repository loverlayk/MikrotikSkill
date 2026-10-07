# apn

> RouterOS directory reference for /interface/lte/apn.

-----------

## interface/lte/apn 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="apn" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-network-apn" typ="bool">in LTE mode use APN provided by the network</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool"></ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num"></ArgTableRow>
<ArgTableRow arg="ip-type" typ="enum (ipv4 | ipv6 | auto)">requested PDN type</ArgTableRow>
<ArgTableRow arg="authentication" typ="enum (none | pap | chap)"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="passthrough-interface" typ="iface_enum { none:0 }"></ArgTableRow>
<ArgTableRow arg="passthrough-mac" typ="alt { auto: enum (static | auto)
, passthrough-peer: macAddr
 }">auto will learn MAC from first packet</ArgTableRow>
<ArgTableRow arg="passthrough-subnet-size" typ="alt { subnet-enum: enum (auto | 32) { auto:0, 32:32 }
, subnet-size: num [16 .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-interface" typ="iface_enum { none:0 }">interface on which to advertise IPv6 prefix</ArgTableRow>
</ArgTable>
