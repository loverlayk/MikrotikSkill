# lora

> RouterOS directory reference for /iot/lora.

-----------

## iot/lora 
**Package:** iot
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="gateway-id" typ="string"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="servers" typ="multi { server: enum
 }"></ArgTableRow>
<ArgTableRow arg="tx-immediate-delay-us" typ="num"></ArgTableRow>
<ArgTableRow arg="channel-plan" typ="enum (custom | eu-868 | as-923 | kr-920 | in-865 | il-917 | us-915-1 | us-915-2 | us-915-3 | us-915-4 | us-915-5 | us-915-6 | us-915-7 | us-915-8 | au-915-1 | au-915-2 | ru-864 | ru-864-mid | 2.4-ghz)"></ArgTableRow>
<ArgTableRow arg="antenna-gain" typ="num"></ArgTableRow>
<ArgTableRow arg="forward" typ="ubit (crc-validation, dev-addr-validation, proprietary-traffic)"></ArgTableRow>
<ArgTableRow arg="network" typ="enum (public | private)"></ArgTableRow>
<ArgTableRow arg="lbt-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="listen-time" typ="num"></ArgTableRow>
<ArgTableRow arg="rssi-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="spoof-gps" typ="bool"></ArgTableRow>
<ArgTableRow arg="lat" typ="num"></ArgTableRow>
<ArgTableRow arg="long" typ="num"></ArgTableRow>
<ArgTableRow arg="alt" typ="num"></ArgTableRow>
<ArgTableRow arg="antenna" typ="enum (internal-antenna | external-antenna)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="firmware-id" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="rx-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-toa" typ="num"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (unknown | 863-870 | 902-928 | 2.4-ghz)"></ArgTableRow>
</ArgTable>
