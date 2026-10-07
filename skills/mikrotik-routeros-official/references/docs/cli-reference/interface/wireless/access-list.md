# access-list

> RouterOS directory reference for /interface/wireless/access-list.

-----------

## interface/wireless/access-list 
**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum { any:0 }"></ArgTableRow>
<ArgTableRow arg="signal-range" typ="composite { min: num [-120 .. 120]
, max: num [-120 .. 120]
 }"></ArgTableRow>
<ArgTableRow arg="allow-signal-out-of-range" typ="alt { signal-out-of-range-always: enum (always) { always:0 }
, signal-out-of-range-time: time
 }"></ArgTableRow>
<ArgTableRow arg="authentication" typ="bool"></ArgTableRow>
<ArgTableRow arg="forwarding" typ="bool"></ArgTableRow>
<ArgTableRow arg="ap-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="client-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="private-algo" typ="enum (none | 40bit-wep | 104bit-wep | aes-ccm | tkip) { none:0, 40bit-wep:1, 104bit-wep:2, aes-ccm:3, tkip:4 }"></ArgTableRow>
<ArgTableRow arg="private-key" typ="string"></ArgTableRow>
<ArgTableRow arg="private-pre-shared-key" typ="string"></ArgTableRow>
<ArgTableRow arg="time" typ="super { start: time [0 .. 86400]
, [end] -time [0 .. 86400]
, [day] ,ubit (sun, mon, tue, wed, thu, fri, sat)
 }"></ArgTableRow>
<ArgTableRow arg="management-protection-key" typ="string"></ArgTableRow>
<ArgTableRow arg="vlan-mode" typ="enum (default | no-tag | use-tag | use-service-tag)"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
</ArgTable>
