# scanners

> RouterOS directory reference for /iot/bluetooth/scanners.

-----------

## iot/bluetooth/scanners 
**Package:** iot
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (passive | active) { passive:0, active:1 }"></ArgTableRow>
<ArgTableRow arg="interval" typ="num"></ArgTableRow>
<ArgTableRow arg="window" typ="num"></ArgTableRow>
<ArgTableRow arg="own-address-type" typ="enum (public | random-static | rpa-fallback-to-public | rpa-fallback-to-random) { public:0, random-static:1, rpa-fallback-to-public:2, rpa-fallback-to-random:3 }">Address type used in scan requests</ArgTableRow>
<ArgTableRow arg="filter-policy" typ="enum (default | whitelist) { default:0, whitelist:1 }"></ArgTableRow>
<ArgTableRow arg="filter-duplicates" typ="enum (off | keep-oldest | keep-newest | keep-unique) { off:0, keep-oldest:1, keep-newest:2, keep-unique:3 }">Discard duplicate advertisements from the same advertiser</ArgTableRow>
<ArgTableRow arg="phy" typ="enum (1M | 2M | CODED) { 1M:0, 2M:1, CODED:2 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum"></ArgTableRow>
</ArgTable>
