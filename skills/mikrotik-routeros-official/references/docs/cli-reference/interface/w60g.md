# w60g

> RouterOS directory reference for /interface/w60g.

-----------

## interface/w60g 
**Syscap:** 60ghz
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
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }"></ArgTableRow>
<ArgTableRow arg="region" typ="enum (no-region-set | usa | canada | asia | eu | japan | australia | china) { no-region-set:0, usa:1, canada:2, asia:3, eu:4, japan:5, australia:6, china:7 }"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (ap-bridge | station-bridge | sniff | bridge)"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="frequency" typ="enum (auto | 58320 | 60480 | 62640 | 64800 | 66000 | 66960) { auto:0, 58320:58320, 60480:60480, 62640:62640, 64800:64800, 66000:66000, 66960:66960 }"></ArgTableRow>
<ArgTableRow arg="scan-list" typ="multi { array-id, frequency: enum (58320 | 60480 | 62640 | 64800 | 66000 | 66960) { 58320:58320, 60480:60480, 62640:62640, 64800:64800, 66000:66000, 66960:66960 }
 }"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="tx-sector" typ="num"></ArgTableRow>
<ArgTableRow arg="put-stations-in-bridge" typ="iface_enum { none:0 }"></ArgTableRow>
<ArgTableRow arg="isolate-stations" typ="bool"></ArgTableRow>
<ArgTableRow arg="mdmg-fix" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="default-scan-list" typ="multi { array-id, frequency: enum (58320 | 60480 | 62640 | 64800 | 66000 | 66960 | 69120) { 58320:58320, 60480:60480, 62640:62640, 64800:64800, 66000:66000, 66960:66960, 69120:69120 }
 }"></ArgTableRow>
<ArgTableRow arg="beamforming-event" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-io-msdu" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-sw-msdu" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-fw-msdu" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-ppdu" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-ppdu-from-q" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-mpdu-new" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-mpdu-total" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-mpdu-retry" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-ppdu" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-mpdu-crc-err" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-mpdu-crc-ok" typ="num"></ArgTableRow>
</ArgTable>
