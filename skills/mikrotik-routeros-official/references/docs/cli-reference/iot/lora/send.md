# send

> RouterOS command reference for /iot/lora/send.

-----------

## iot/lora/send 
**Package:** iot
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device-id" typ="num">device id</ArgTableRow>
<ArgTableRow arg="payload" typ="string">TX packet payload</ArgTableRow>
<ArgTableRow arg="power" typ="num">RF power in dBm</ArgTableRow>
<ArgTableRow arg="frequency" typ="num">Radio TX frequency in MHz (e.g.868500000)</ArgTableRow>
<ArgTableRow arg="bandwidth" typ="enum (125kHz | 250kHz | 500kHz) { 125kHz:125, 250kHz:250, 500kHz:500 }">LoRa bandwidth in khz [125, 250, 500]</ArgTableRow>
<ArgTableRow arg="spread-factor" typ="enum (SF7 | SF8 | SF9 | SF10 | SF11 | SF12 | MULTI) { SF7:0x02, SF8:0x04, SF9:0x08, SF10:0x10, SF11:0x21, SF12:0x40, MULTI:0x7E }">Spread Factor</ArgTableRow>
<ArgTableRow arg="modulation" typ="enum (MOD_CW | MOD_LORA | MOD_FSK) { MOD_CW:0x08, MOD_LORA:0x10, MOD_FSK:0x20 }">modulation type</ArgTableRow>
<ArgTableRow arg="preamble" typ="num">preamble length</ArgTableRow>
<ArgTableRow arg="inverted" typ="bool">invert polarity</ArgTableRow>
</ArgTable>
