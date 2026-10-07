# settings

> RouterOS settings reference for /system/health/settings.

-----------

## system/health/settings 
**Conditions:** !i386
**Syscap:** health and health-settings
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="fan-full-speed-temp" typ="num"></ArgTableRow>
<ArgTableRow arg="fan-target-temp" typ="num"></ArgTableRow>
<ArgTableRow arg="fan-min-speed-percent" typ="num"></ArgTableRow>
<ArgTableRow arg="fan-control-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="fan-mode" typ="enum (manual | auto) { manual:0, auto:1 }"></ArgTableRow>
<ArgTableRow arg="use-fan" typ="enum (auxiliary | main) { auxiliary:0, main:1 }"></ArgTableRow>
<ArgTableRow arg="use-fan2" typ="enum (auxiliary | main) { auxiliary:0, main:1 }"></ArgTableRow>
<ArgTableRow arg="fan-switch" typ="enum (auto | on | off) { auto:0, on:1, off:2 }"></ArgTableRow>
<ArgTableRow arg="fan-on-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-overtemp-check" typ="bool"></ArgTableRow>
<ArgTableRow arg="cpu-overtemp-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-overtemp-startup-delay" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="active-fan" typ="enum (auxiliary | main | none) { auxiliary:0, main:1, none:2 }"></ArgTableRow>
<ArgTableRow arg="active-fan2" typ="enum (auxiliary | main | none) { auxiliary:0, main:1, none:2 }"></ArgTableRow>
</ArgTable>
