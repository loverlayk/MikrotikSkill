# radio

> Radio configuration replicated to the selected devices. The arguments extend the standard RouterOS /interface/wifi radio configuration parameters.

-----------

## cmr/wifi/radio 
**Package:** cmr
**Type:** Directory

Radio configuration replicated to the selected devices. The arguments extend the standard RouterOS `/interface/wifi` radio configuration parameters.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Radio configuration is disabled.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="labels" typ="object" unset="1">Select the devices the radio configuration is replicated to using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.</ArgTableRow>
<ArgTableRow arg="configuration.country" typ="enum" unset="1">Country code.</ArgTableRow>
<ArgTableRow arg="configuration.chains" typ="ubit (0, 1, 2, 3, 4, 5, 6, 7)" unset="1">Radio chains to use.</ArgTableRow>
<ArgTableRow arg="configuration.tx-chains" typ="ubit ()" unset="1">Transmit chains.</ArgTableRow>
<ArgTableRow arg="configuration.tx-power" typ="num" unset="1">Transmit power.</ArgTableRow>
<ArgTableRow arg="configuration.antenna-gain" typ="num" unset="1">Antenna gain.</ArgTableRow>
<ArgTableRow arg="configuration.distance" typ="num" unset="1">Distance to the farthest connected client.</ArgTableRow>
<ArgTableRow arg="configuration.installation" typ="enum (outdoor | indoor)" unset="1">Installation type: `outdoor` or `indoor`.</ArgTableRow>
<ArgTableRow arg="security.authentication-types" typ="ubit (wpa-psk, wpa2-psk, wpa2-psk-sha2, wpa-eap, wpa2-eap, wpa3-psk, wpa3-psk-gd, owe, wpa3-eap, wpa3-eap-192)" unset="1">Supported authentication types.</ArgTableRow>
<ArgTableRow arg="channel.frequency" typ="object" unset="1">Channel frequency.</ArgTableRow>
<ArgTableRow arg="channel.secondary-frequency" typ="multi { array-id, secondary-frequency: alt { secondary-frequency-disable: enum (disabled)
, secondary-frequency-num: num
 }
 }" unset="1">Secondary channel frequency.</ArgTableRow>
<ArgTableRow arg="channel.band" typ="enum (60ghz-ad | 5ghz-a | 5ghz-n | 5ghz-ac | 5ghz-ax | 5ghz-be | 2ghz-g | 2ghz-n | 2ghz-ax | 2ghz-be | s1ghz-ah | 6ghz-ax | 6ghz-be)" unset="1">Operating band.</ArgTableRow>
<ArgTableRow arg="channel.width" typ="enum (20mhz | 20/40mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz | 20/40/80+80mhz | 20/40/80/160mhz | 20/40/80/160/320mhz | 1mhz | 1/2mhz | 1/2/4mhz | 1/2/4/8mhz | 2160mhz)" unset="1">Channel width.</ArgTableRow>
<ArgTableRow arg="channel.skip-dfs-channels" typ="enum (disabled | all | 10min-cac)" unset="1">DFS channel handling: `disabled`, `all`, `10min-cac`.</ArgTableRow>
<ArgTableRow arg="channel.deprioritize-unii-3-4" typ="bool" unset="1">Deprioritize UNII-3/UNII-4 channels.</ArgTableRow>
<ArgTableRow arg="channel.reselect-interval" typ="super { reselect-interval-min: time [1 .. 60*60*24*300]
, [reselect-interval-max] ..time [1 .. 60*60*24*300]
 }" unset="1">Channel reselection interval range.</ArgTableRow>
<ArgTableRow arg="channel.reselect-time" typ="super { reselect-time-min: date
, [reselect-time-max] ..date
 }" unset="1">Channel reselection time range.</ArgTableRow>
<ArgTableRow arg="channel.preamble-puncturing" typ="alt { preamble-puncturing: enum (yes | no) { yes:-1, no:0 }
 }" unset="1">Preamble puncturing: `yes` or `no`.</ArgTableRow>
<ArgTableRow arg="channel.afc" typ="bool" unset="1">Enable AFC (Automatic Frequency Coordination).</ArgTableRow>
</ArgTable>
