# health

> RouterOS settings reference for /system/health.

-----------

## system/health 
**Conditions:** i386
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="state-after-reboot" typ="enum (disabled | enabled)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="core" typ="num"></ArgTableRow>
<ArgTableRow arg="3.3v" typ="num"></ArgTableRow>
<ArgTableRow arg="5v" typ="num"></ArgTableRow>
<ArgTableRow arg="12v" typ="num"></ArgTableRow>
<ArgTableRow arg="lm87-temp" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-temp" typ="num"></ArgTableRow>
<ArgTableRow arg="board-temp" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage1" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage2" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage3" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage4" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage5" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage6" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage7" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage8" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage9" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage10" typ="num"></ArgTableRow>
<ArgTableRow arg="temp1" typ="num"></ArgTableRow>
<ArgTableRow arg="temp2" typ="num"></ArgTableRow>
<ArgTableRow arg="temp3" typ="num"></ArgTableRow>
<ArgTableRow arg="fan1" typ="num"></ArgTableRow>
<ArgTableRow arg="fan2" typ="num"></ArgTableRow>
<ArgTableRow arg="fan3" typ="num"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (disabled | enabled)"></ArgTableRow>
</ArgTable>

## system/health 
**Conditions:** !i386
**Syscap:** health
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="value" typ="alt { valuet: num
, valuer: num
, valuev: num
, valuea: num
, valuew: num
, valueb: enum (ok | fail | not-present | idle | no-input) { ok:0, fail:1, not-present:2, idle:3, no-input:4 }
, values: string
 }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (C | RPM | V | A | W |  | )"></ArgTableRow>
</ArgTable>
