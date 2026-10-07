# advertisers

> RouterOS directory reference for /iot/bluetooth/advertisers.

-----------

## iot/bluetooth/advertisers 
**Package:** iot
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="min-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="max-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="own-address-type" typ="enum (public | random-static | rpa-fallback-to-public | rpa-fallback-to-random)">Address type used in AdvA field</ArgTableRow>
<ArgTableRow arg="channel-map" typ="ubit (37, 38, 39)"></ArgTableRow>
<ArgTableRow arg="phy" typ="enum (1M | 2M | CODED) { 1M:0, 2M:1, CODED:2 }"></ArgTableRow>
<ArgTableRow arg="legacy" typ="bool"></ArgTableRow>
<ArgTableRow arg="ad-structures" typ="multi { array-id, structure: enum
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum"></ArgTableRow>
<ArgTableRow arg="ad-size" typ="num"></ArgTableRow>
</ArgTable>
