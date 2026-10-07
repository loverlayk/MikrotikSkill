# flat-snoop

> RouterOS command reference for /interface/wireless/snooper/flat-snoop.

-----------

## interface/wireless/snooper/flat-snoop 
**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (frequency | network | station)"></ArgTableRow>
<ArgTableRow arg="channel" typ="string"></ArgTableRow>
<ArgTableRow arg="use" typ="num"></ArgTableRow>
<ArgTableRow arg="bitrate" typ="alt { station-bandwidth: num
, network-bandwidth: num
, frequency-bandwidth: num
 }"></ArgTableRow>
<ArgTableRow arg="frequency-network-count" typ="num"></ArgTableRow>
<ArgTableRow arg="noise-floor" typ="num"></ArgTableRow>
<ArgTableRow arg="frequency-station-count" typ="num"></ArgTableRow>
<ArgTableRow arg="active" typ="alt { station-active: bool
, network-active: bool
 }"></ArgTableRow>
<ArgTableRow arg="frequency-known" typ="bool"></ArgTableRow>
<ArgTableRow arg="beacon-seen" typ="bool"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { station-address: macAddr
, network-address: macAddr
 }"></ArgTableRow>
<ArgTableRow arg="network-ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="beacon-hides-ssid" typ="bool"></ArgTableRow>
<ArgTableRow arg="beacon-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="beacon-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="last-beacon" typ="time"></ArgTableRow>
<ArgTableRow arg="beacon-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-to-noise" typ="alt { network-signal-to-noise: num
, station-signal-to-noise: num
 }"></ArgTableRow>
<ArgTableRow arg="ssid-source" typ="enum (none | association-discussion | probe-response | beacon) { none:0, association-discussion:1, probe-response:2, beacon:3 }"></ArgTableRow>
<ArgTableRow arg="supported-rates" typ="multi { array-id, rate: enum ()
 }"></ArgTableRow>
<ArgTableRow arg="basic-rates" typ="multi { array-id, rate: enum ()
 }"></ArgTableRow>
<ArgTableRow arg="network-capabilities" typ="multi { array-id, cap: enum (ess | ibss | cf-pollable | cf-pollreq | privacy | short-preamble | pbcc | channel-agility)
 }"></ArgTableRow>
<ArgTableRow arg="mt-network" typ="bool"></ArgTableRow>
<ArgTableRow arg="mt-info" typ="multi { array-id, cap: enum (nstreme | doing-wds | without-polling | dynamic-packing-size) { nstreme:0, doing-wds:2, without-polling:3, dynamic-packing-size:4 }
 }"></ArgTableRow>
<ArgTableRow arg="mt-name" typ="alt { station-mt-name: string
, network-mt-name: string
 }"></ArgTableRow>
<ArgTableRow arg="mt-routeros-version" typ="alt { station-mt-routeros-version: string
, network-mt-routeros-version: string
 }"></ArgTableRow>
<ArgTableRow arg="mt-mru" typ="alt { station-mt-mru: num
, network-mt-mru: num
 }"></ArgTableRow>
<ArgTableRow arg="mt-framing-mode" typ="enum (none | best-fit | exact-size) { none:0, best-fit:2, exact-size:3 }"></ArgTableRow>
<ArgTableRow arg="network-station-count" typ="num"></ArgTableRow>
<ArgTableRow arg="use-of-freq" typ="alt { station-use-of-freq: num
, network-use-of-freq: num
 }"></ArgTableRow>
<ArgTableRow arg="use-of-traffic" typ="alt { station-use-of-traffic: num
, network-use-of-traffic: num
 }"></ArgTableRow>
<ArgTableRow arg="freq-source" typ="enum (seen-frame-on-freq | network-on-freq) { seen-frame-on-freq:0, network-on-freq:1 }"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="time"></ArgTableRow>
<ArgTableRow arg="signal-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="network-source" typ="enum (none | seen-data-frame | seen-successful-auth | seen-successful-assoc | forms-network) { none:0, seen-data-frame:1, seen-successful-auth:2, seen-successful-assoc:3, forms-network:4 }"></ArgTableRow>
<ArgTableRow arg="seen-wep" typ="bool"></ArgTableRow>
<ArgTableRow arg="station-rates" typ="multi { array-id, rate: enum ()
 }"></ArgTableRow>
<ArgTableRow arg="station-capabilities" typ="multi { array-id, cap: enum (ess | ibss | cf-pollable | cf-pollreq | privacy | short-preamble | pbcc | channel-agility)
 }"></ArgTableRow>
<ArgTableRow arg="mt-station" typ="bool"></ArgTableRow>
<ArgTableRow arg="assoc-capabilities" typ="multi { array-id, cap: enum (ess | ibss | cf-pollable | cf-pollreq | privacy | short-preamble | pbcc | channel-agility)
 }"></ArgTableRow>
<ArgTableRow arg="assoc-id" typ="num"></ArgTableRow>
<ArgTableRow arg="assoc-mt-info" typ="multi { array-id, cap: enum (nstreme | doing-wds | without-polling | dynamic-packing-size) { nstreme:0, doing-wds:2, without-polling:3, dynamic-packing-size:4 }
 }"></ArgTableRow>
<ArgTableRow arg="assoc-mt-ap-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="assoc-mt-client-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="assoc-mt-framing-mode" typ="enum (none | best-fit | exact-size) { none:0, best-fit:2, exact-size:3 }"></ArgTableRow>
<ArgTableRow arg="assoc-mt-framing-limit" typ="num"></ArgTableRow>
</ArgTable>
