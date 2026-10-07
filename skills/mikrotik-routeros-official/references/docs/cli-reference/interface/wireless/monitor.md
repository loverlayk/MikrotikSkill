# monitor

> RouterOS command reference for /interface/wireless/monitor.

-----------

## interface/wireless/monitor 
**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="enum (disabled | searching-for-network | connected-to-ess | initializing | searching-for-frequency | radar-detecting | running-ap | tkip-countermeasures | nstreme-dual-slave) { disabled:0, searching-for-network:1, connected-to-ess:2, initializing:3, searching-for-frequency:100, radar-detecting:101, running-ap:102, tkip-countermeasures:103, nstreme-dual-slave:200 }"></ArgTableRow>
<ArgTableRow arg="status-reason" typ="string"></ArgTableRow>
<ArgTableRow arg="channel" typ="string"></ArgTableRow>
<ArgTableRow arg="wireless-protocol" typ="enum (802.11 | nstreme | nv2) { 802.11:1, nstreme:2, nv2:3 }"></ArgTableRow>
<ArgTableRow arg="nstreme-status" typ="enum (ok | degraded)"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="bssid" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="radio-name" typ="string"></ArgTableRow>
<ArgTableRow arg="signal-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-strength-ch0" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-strength-ch1" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-strength-ch2" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-strength-ch3" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch0" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch1" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch2" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch3" typ="num"></ArgTableRow>
<ArgTableRow arg="noise-floor" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-to-noise" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-ccq" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-ccq" typ="num"></ArgTableRow>
<ArgTableRow arg="p-throughput" typ="num"></ArgTableRow>
<ArgTableRow arg="overall-tx-ccq" typ="num"></ArgTableRow>
<ArgTableRow arg="registered-clients" typ="num"></ArgTableRow>
<ArgTableRow arg="authenticated-clients" typ="num"></ArgTableRow>
<ArgTableRow arg="current-ack-timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="current-distance" typ="num"></ArgTableRow>
<ArgTableRow arg="wds-link" typ="bool"></ArgTableRow>
<ArgTableRow arg="bridge" typ="bool"></ArgTableRow>
<ArgTableRow arg="nstreme" typ="bool"></ArgTableRow>
<ArgTableRow arg="polling" typ="bool"></ArgTableRow>
<ArgTableRow arg="csma-disabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="framing-mode" typ="enum (none | best-fit | exact-size) { none:0, best-fit:2, exact-size:3 }"></ArgTableRow>
<ArgTableRow arg="framing-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="framing-current-size" typ="num"></ArgTableRow>
<ArgTableRow arg="routeros-version" typ="string"></ArgTableRow>
<ArgTableRow arg="last-ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="802.1x-port-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="authentication-type" typ="enum (wpa-psk | wpa2-psk | wpa-eap | wpa2-eap) { wpa-psk:0, wpa2-psk:1, wpa-eap:2, wpa2-eap:3 }"></ArgTableRow>
<ArgTableRow arg="encryption" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="group-encryption" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="management-protection" typ="bool"></ArgTableRow>
<ArgTableRow arg="compression" typ="bool"></ArgTableRow>
<ArgTableRow arg="wmm-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="nv2-sync-state" typ="enum (searching | syncing | synced) { searching:0, syncing:1, synced:2 }"></ArgTableRow>
<ArgTableRow arg="nv2-sync-master" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="nv2-sync-distance" typ="num"></ArgTableRow>
<ArgTableRow arg="nv2-sync-period-size" typ="num"></ArgTableRow>
<ArgTableRow arg="nv2-sync-downlink-ratio" typ="num"></ArgTableRow>
<ArgTableRow arg="current-tx-powers" typ="multi { current-tx-power: super { rate: enum ()
, [tx-power] :num
, [tx-power-real] (num
, tx-power-total: num
 }
 }"></ArgTableRow>
<ArgTableRow arg="current-ofdm-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="current-cck-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="1s-frames" typ="composite { compressed: num
, total: num
 }"></ArgTableRow>
<ArgTableRow arg="1s-compressed-frames" typ="num"></ArgTableRow>
<ArgTableRow arg="1s-bytes" typ="composite { compressed: num
, total: num
 }"></ArgTableRow>
<ArgTableRow arg="1s-length-of-orig" typ="num"></ArgTableRow>
<ArgTableRow arg="total-frames" typ="composite { compressed: num
, total: num
 }"></ArgTableRow>
<ArgTableRow arg="total-compressed-frames" typ="num"></ArgTableRow>
<ArgTableRow arg="total-bytes" typ="composite { compressed: num
, total: num
 }"></ArgTableRow>
<ArgTableRow arg="total-length-of-orig" typ="num"></ArgTableRow>
<ArgTableRow arg="notify-external-fdb" typ="bool"></ArgTableRow>
<ArgTableRow arg="cloned-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="searching-for-address-to-clone" typ="bool"></ArgTableRow>
</ArgTable>
