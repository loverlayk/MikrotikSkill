# nstreme-dual

> RouterOS directory reference for /interface/wireless/nstreme-dual.

-----------

## interface/wireless/nstreme-dual 
**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }"></ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool"></ArgTableRow>
<ArgTableRow arg="tx-radio" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="rx-radio" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="remote-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="tx-band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n)"></ArgTableRow>
<ArgTableRow arg="tx-channel-width" typ="enum (20mhz | 40mhz | 10mhz | 5mhz)"></ArgTableRow>
<ArgTableRow arg="tx-frequency" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n)"></ArgTableRow>
<ArgTableRow arg="rx-channel-width" typ="enum (20mhz | 40mhz | 10mhz | 5mhz)"></ArgTableRow>
<ArgTableRow arg="rx-frequency" typ="num"></ArgTableRow>
<ArgTableRow arg="disable-csma" typ="bool"></ArgTableRow>
<ArgTableRow arg="rates-b" typ="ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps)"></ArgTableRow>
<ArgTableRow arg="rates-a/g" typ="ubit (6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps)"></ArgTableRow>
<ArgTableRow arg="ht-rates" typ="ubit (1, 2, 3, 4, 5, 6, 7, 8)"></ArgTableRow>
<ArgTableRow arg="ht-guard-interval" typ="enum (long | short | both) { long:1, short:2, both:3 }"></ArgTableRow>
<ArgTableRow arg="ht-channel-width" typ="enum (20mhz | 40mhz | 2040mhz) { 20mhz:1, 40mhz:2, 2040mhz:3 }"></ArgTableRow>
<ArgTableRow arg="ht-streams" typ="enum (single | double | both) { single:1, double:2, both:3 }"></ArgTableRow>
<ArgTableRow arg="framer-policy" typ="enum (none | best-fit | exact-size) { none:0, best-fit:1, exact-size:2 }"></ArgTableRow>
<ArgTableRow arg="framer-limit" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
</ArgTable>
