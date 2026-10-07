# leds

> RouterOS directory reference for /system/leds.

-----------

## system/leds 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="*" typ="default"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (interface-status | interface-receive | interface-transmit | interface-activity | wireless-signal-strength | wireless-status | modem-signal | modem-technology | flash-access | interface-speed | interface-speed-1G | interface-speed-25G | interface-speed-2.5G | interface-speed-100G | poe-out | ap-cap | on | off | fan-fault | poe-fault | gps-valid | align-left | align-right | align-up | align-down)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="leds" typ="object { led: enum
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="object { iface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="modem-signal-threshold" typ="num">RSSI threshold</ArgTableRow>
<ArgTableRow arg="color" typ="alt { color-name: enum (none | red | orange | yellow | green-yellow | green | green-cyan | cyan | blue-cyan | blue | blue-magenta | magenta | red-magenta) { none:0, red:0xff0000, orange:0xff7f00, yellow:0xffff00, green-yellow:0x7fff00, green:0x00ff00, green-cyan:0x00ff7f, cyan:0x00ffff, blue-cyan:0x007fff, blue:0x0000ff, blue-magenta:0x7f00ff, magenta:0xff00ff, red-magenta:0xff007f }
, color-number: num [0 .. 0xffffff]
 }"></ArgTableRow>
</ArgTable>
