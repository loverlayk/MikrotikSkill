# sync-e

> RouterOS settings reference for /system/sync-e.

-----------

## system/sync-e 
**Syscap:** synce
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool">enable or disable SyncE</ArgTableRow>
<ArgTableRow arg="wait-to-restore" typ="time">time to wait before using a reference after it becomes valid again</ArgTableRow>
<ArgTableRow arg="hold-off" typ="time">time to wait before switching away from the current reference after it becomes invalid</ArgTableRow>
<ArgTableRow arg="quality-level" typ="enum (dnu | eprtc | eprc | prtc | prc | ssu-a | ssu-b | eec1 | prs | stu | st2 | tnc | st3e | eec2 | eeec | prov) { dnu:0, eprtc:5, eprc:15, prtc:6, prc:4, ssu-a:3, ssu-b:2, eec1:12, prs:7, stu:8, st2:9, tnc:10, st3e:11, eec2:13, eeec:16, prov:14 }">minimum accepted ESMC quality level; lower-quality references are not selected</ArgTableRow>
<ArgTableRow arg="network" typ="enum (option-1 | option-2) { option-1:0, option-2:1 }">ESMC network option used when interpreting quality levels</ArgTableRow>
<ArgTableRow arg="holdover" typ="time">time to keep the last reference active when no valid reference is available before entering local holdover</ArgTableRow>
<ArgTableRow arg="esmc-timeout" typ="time">time without a valid ESMC message before the reference is considered lost</ArgTableRow>
<ArgTableRow arg="essm" typ="bool">use eSSM quality-level information in transmitted and received ESMC frames</ArgTableRow>
</ArgTable>
