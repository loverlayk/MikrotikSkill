# monitor

> RouterOS command reference for /interface/lte/monitor.

-----------

## interface/lte/monitor 
**Conditions:** !smips
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="pin-status" typ="string"></ArgTableRow>
<ArgTableRow arg="registration-status" typ="string"></ArgTableRow>
<ArgTableRow arg="functionality" typ="enum (minimum | full | tx rf circuit disabled | rx rf circuit disabled | tx and rx rf circuit disabled | tx and rx rf circuit disabled) { minimum:0, full:1, tx rf circuit disabled:2, rx rf circuit disabled:3, tx and rx rf circuit disabled:4, tx and rx rf circuit disabled:7 }"></ArgTableRow>
<ArgTableRow arg="manufacturer" typ="string"></ArgTableRow>
<ArgTableRow arg="model" typ="string"></ArgTableRow>
<ArgTableRow arg="revision" typ="string"></ArgTableRow>
<ArgTableRow arg="current-operator" typ="string"></ArgTableRow>
<ArgTableRow arg="roaming" typ="bool"></ArgTableRow>
<ArgTableRow arg="psc" typ="num"></ArgTableRow>
<ArgTableRow arg="lac" typ="num"></ArgTableRow>
<ArgTableRow arg="current-cellid" typ="num"></ArgTableRow>
<ArgTableRow arg="enb-id" typ="num"></ArgTableRow>
<ArgTableRow arg="sector-id" typ="num"></ArgTableRow>
<ArgTableRow arg="phy-cellid" typ="num"></ArgTableRow>
<ArgTableRow arg="data-class" typ="string"></ArgTableRow>
<ArgTableRow arg="session-uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="imei" typ="string"></ArgTableRow>
<ArgTableRow arg="imsi" typ="string"></ArgTableRow>
<ArgTableRow arg="iccid" typ="string"></ArgTableRow>
<ArgTableRow arg="subscriber-number" typ="string"></ArgTableRow>
<ArgTableRow arg="earfcn" typ="string"></ArgTableRow>
<ArgTableRow arg="primary-band" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-band" typ="multi { array-id, ca: string
 }"></ArgTableRow>
<ArgTableRow arg="ul-ca-band" typ="multi { array-id, ca: string
 }"></ArgTableRow>
<ArgTableRow arg="frame-error-rate" typ="string"></ArgTableRow>
<ArgTableRow arg="dl-modulation" typ="string"></ArgTableRow>
<ArgTableRow arg="dl-mimo" typ="num"></ArgTableRow>
<ArgTableRow arg="cqi" typ="num"></ArgTableRow>
<ArgTableRow arg="ri" typ="num"></ArgTableRow>
<ArgTableRow arg="mcs" typ="num"></ArgTableRow>
<ArgTableRow arg="ecio" typ="num"></ArgTableRow>
<ArgTableRow arg="rscp" typ="num"></ArgTableRow>
<ArgTableRow arg="rssi" typ="num"></ArgTableRow>
<ArgTableRow arg="rsrp" typ="num"></ArgTableRow>
<ArgTableRow arg="rsrq" typ="num"></ArgTableRow>
<ArgTableRow arg="sinr" typ="num"></ArgTableRow>
<ArgTableRow arg="nr-dl-modulation" typ="string"></ArgTableRow>
<ArgTableRow arg="nr-rsrp" typ="num"></ArgTableRow>
<ArgTableRow arg="nr-rsrq" typ="num"></ArgTableRow>
<ArgTableRow arg="nr-sinr" typ="num"></ArgTableRow>
</ArgTable>
