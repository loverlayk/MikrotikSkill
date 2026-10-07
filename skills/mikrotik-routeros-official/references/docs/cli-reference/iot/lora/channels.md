# channels

> RouterOS directory reference for /iot/lora/channels.

-----------

## iot/lora/channels 
**Package:** iot
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="radio" typ="enum (radio0 | radio1 | radio2 | radio3) { radio0:0, radio1:1, radio2:2, radio3:3 }"></ArgTableRow>
<ArgTableRow arg="freq-off" typ="num"></ArgTableRow>
<ArgTableRow arg="bandwidth" typ="enum (7.8_kHz | 15.6_kHz | 31.2_kHz | 62.5_kHz | 125_kHz | 250_kHz | 500_kHz | 200_kHz | 400_kHz | 800_kHz | 1600_kHz)"></ArgTableRow>
<ArgTableRow arg="spread-factor" typ="enum (SF7 | SF8 | SF9 | SF10 | SF11 | SF12 | SF5 | SF6)"></ArgTableRow>
<ArgTableRow arg="datarate" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (MSF | LoRa | FSK)"></ArgTableRow>
<ArgTableRow arg="freq" typ="num"></ArgTableRow>
</ArgTable>
