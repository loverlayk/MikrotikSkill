# port

> RouterOS directory reference for /system/sync-e/port.

-----------

## system/sync-e/port 
**Syscap:** synce
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="E" typ="elected"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ql-mode" typ="enum (disable | prc | prs | ssu-a | ssu-b | st2 | st3e | stu | tnc | eprtc | eprc | prtc | eec1 | eec2 | eeec | prov) { disable:0, prc:1, prs:2, ssu-a:5, ssu-b:6, st2:7, st3e:9, stu:11, tnc:12, eprtc:13, eprc:18, prtc:14, eec1:15, eec2:16, eeec:19, prov:17 }"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
</ArgTable>
