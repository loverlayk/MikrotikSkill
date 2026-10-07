# registration-table

> RouterOS directory reference for /dude/ros/registration-table.

-----------

## dude/ros/registration-table 
**Package:** dude
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="enum"></ArgTableRow>
<ArgTableRow arg="radio-name" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ap" typ="bool"></ArgTableRow>
<ArgTableRow arg="wds" typ="bool"></ArgTableRow>
<ArgTableRow arg="bridge" typ="bool"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="packets" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="bytes" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="frames" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="frame-bytes" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="hw-frames" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="hw-frame-bytes" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="packed-frames" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="packed-bytes" typ="composite { tx: num
, rx: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-frames-timed-out" typ="num"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="last-activity" typ="time"></ArgTableRow>
<ArgTableRow arg="signal-strength" typ="composite { strength: num
, rate: enum (1Mbps | 2Mbps | 5.5Mbps | 11Mbps | 6Mbps | 9Mbps | 12Mbps | 18Mbps | 24Mbps | 36Mbps | 48Mbps | 54Mbps | HT20-0 | HT20-1 | HT20-2 | HT20-3 | HT20-4 | HT20-5 | HT20-6 | HT20-7 | HT40-0 | HT40-1 | HT40-2 | HT40-3 | HT40-4 | HT40-5 | HT40-6 | HT40-7)
 }"></ArgTableRow>
<ArgTableRow arg="signal-to-noise" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-strength-ch0" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-strength-ch1" typ="num"></ArgTableRow>
<ArgTableRow arg="signal-strength-ch2" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch0" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch1" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength-ch2" typ="num"></ArgTableRow>
<ArgTableRow arg="evm-ch0" typ="num"></ArgTableRow>
<ArgTableRow arg="evm-ch1" typ="num"></ArgTableRow>
<ArgTableRow arg="evm-ch2" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-evm-ch0" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-evm-ch1" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-evm-ch2" typ="num"></ArgTableRow>
<ArgTableRow arg="strength-at-rates" typ="multi { strength-at-rate: super { strength: num
, [rate] @enum (1Mbps | 2Mbps | 5.5Mbps | 11Mbps | 6Mbps | 9Mbps | 12Mbps | 18Mbps | 24Mbps | 36Mbps | 48Mbps | 54Mbps | HT20-0 | HT20-1 | HT20-2 | HT20-3 | HT20-4 | HT20-5 | HT20-6 | HT20-7 | HT40-0 | HT40-1 | HT40-2 | HT40-3 | HT40-4 | HT40-5 | HT40-6 | HT40-7)
, [time]  time
 }
 }"></ArgTableRow>
<ArgTableRow arg="tx-signal-strength" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-ccq" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-ccq" typ="num"></ArgTableRow>
<ArgTableRow arg="p-throughput" typ="num"></ArgTableRow>
<ArgTableRow arg="ack-timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="distance" typ="num"></ArgTableRow>
<ArgTableRow arg="nstreme" typ="bool"></ArgTableRow>
<ArgTableRow arg="framing-mode" typ="enum (none | best-fit | exact-size) { none:0, best-fit:2, exact-size:3 }"></ArgTableRow>
<ArgTableRow arg="framing-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="framing-current-size" typ="num"></ArgTableRow>
<ArgTableRow arg="routeros-version" typ="string"></ArgTableRow>
<ArgTableRow arg="last-ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="ap-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="client-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="802.1x-port-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="authentication-type" typ="enum (wpa-psk | wpa2-psk | wpa-eap | wpa2-eap) { wpa-psk:0, wpa2-psk:1, wpa-eap:2, wpa2-eap:3 }"></ArgTableRow>
<ArgTableRow arg="encryption" typ="enum (none | 40bit-wep | 104bit-wep | aes-ccm | tkip)"></ArgTableRow>
<ArgTableRow arg="group-encryption" typ="enum (none | 40bit-wep | 104bit-wep | aes-ccm | tkip)"></ArgTableRow>
<ArgTableRow arg="management-protection" typ="bool"></ArgTableRow>
<ArgTableRow arg="compression" typ="bool"></ArgTableRow>
<ArgTableRow arg="wmm-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="wmm-ps-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="tx-rate-set" typ="string"></ArgTableRow>
<ArgTableRow arg="tdma-timing-offset" typ="num"></ArgTableRow>
<ArgTableRow arg="tdma-tx-size" typ="num"></ArgTableRow>
<ArgTableRow arg="tdma-rx-size" typ="num"></ArgTableRow>
<ArgTableRow arg="tdma-retx" typ="num"></ArgTableRow>
<ArgTableRow arg="tdma-winfull" typ="num"></ArgTableRow>
</ArgTable>
