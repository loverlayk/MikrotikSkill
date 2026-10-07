# advertisements

> RouterOS directory reference for /iot/bluetooth/scanners/advertisements.

-----------

## iot/bluetooth/scanners/advertisements 
**Package:** iot
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum"></ArgTableRow>
<ArgTableRow arg="pdu-type" typ="enum (adv-ind | adv-direct-ind | adv-scan-ind | adv-noconn-ind | scan-rsp | unknown) { adv-ind:0, adv-direct-ind:1, adv-scan-ind:2, adv-noconn-ind:3, scan-rsp:4, unknown:5 }"></ArgTableRow>
<ArgTableRow arg="time" typ="date"></ArgTableRow>
<ArgTableRow arg="epoch" typ="num">Milliseconds since Unix Epoch</ArgTableRow>
<ArgTableRow arg="address-type" typ="enum (public | random) { public:0, random:1 }"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr">Advertiser Bluetooth address</ArgTableRow>
<ArgTableRow arg="rssi" typ="num">Signal strength</ArgTableRow>
<ArgTableRow arg="length" typ="num">Advertisement data length</ArgTableRow>
<ArgTableRow arg="data" typ="string">Advertisement data in hex format</ArgTableRow>
<ArgTableRow arg="phy" typ="enum (1M | 2M | CODED-S8 | CODED-S2 | NONE) { 1M:0, 2M:1, CODED-S8:2, CODED-S2:3, NONE:4 }">Advertisement primary PHY</ArgTableRow>
<ArgTableRow arg="phy-secondary" typ="enum (1M | 2M | CODED-S8 | CODED-S2 | NONE) { 1M:0, 2M:1, CODED-S8:2, CODED-S2:3, NONE:4 }">Advertisement secondary PHY</ArgTableRow>
<ArgTableRow arg="legacy" typ="bool">Advertisement legacy compatibility</ArgTableRow>
<ArgTableRow arg="filter-comment" typ="string">Comment of the matching whitelist filter</ArgTableRow>
</ArgTable>
