# radio

> RouterOS directory reference for /interface/wifi/radio.

-----------

## interface/wifi/radio 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="L" typ="local">local</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="cap" typ="string"></ArgTableRow>
<ArgTableRow arg="radio-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="tx-chains" typ="ubit ()"></ArgTableRow>
<ArgTableRow arg="rx-chains" typ="ubit ()"></ArgTableRow>
<ArgTableRow arg="bands" typ="object { band: composite { band-band: enum ()
, band-widths: ubit (20mhz, 20/40mhz, 20/40/80mhz, 20/40/80/160mhz, 20/40/80+80mhz, 20/40/80/160/320mhz, 1mhz, 1/2mhz, 1/2/4mhz, 1/2/4/8mhz, 1/2/4/8/16mhz, 2160mhz)
 }
 }"></ArgTableRow>
<ArgTableRow arg="ciphers" typ="ubit (tkip, ccmp, gcmp, ccmp-256, gcmp-256, cmac, gmac, cmac-256, gmac-256)"></ArgTableRow>
<ArgTableRow arg="min-antenna-gain" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="countries" typ="multi { array-id, country: string
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="2g-channels" typ="multi { array-id, frequency: num
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="5g-channels" typ="multi { array-id, frequency: num
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="6g-channels" typ="multi { array-id, frequency: num
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="60g-channels" typ="multi { array-id, frequency: num
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="s1g-channels" typ="multi { array-id, frequency: num
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="max-vlans" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="max-interfaces" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="max-station-interfaces" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="max-peers" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="hw-type" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="hw-caps" typ="multi { array-id, hw-cap: enum (sniffer | qos-classifier-dscp | spectral | channel-switch | mlo | hw-protection-mode | beacon-protection | meshpoint)
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="ml-group" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" unset="1"></ArgTableRow>
<ArgTableRow arg="current-country" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="current-halow-regdom" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="current-channels" typ="multi { array-id, channel: string
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="current-gopclasses" typ="multi { array-id, gopclass: num
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="current-max-reg-power" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="afc-deployment" typ="string" unset="1"></ArgTableRow>
</ArgTable>
