# license

> RouterOS settings reference for /system/license.

-----------

## system/license 
**Type:** Settings Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="software-id" typ="string" syscap="nochr">Unique identifier for MikroTik hardware and x86 systems, used for licensing. Bound to the device storage.</ArgTableRow>
<ArgTableRow arg="old-software-id" typ="string" syscap="nochr">The previous Software ID, shown when the ID has changed.</ArgTableRow>
<ArgTableRow arg="nlevel" typ="num" syscap="nochr">The license level number (0-6).</ArgTableRow>
<ArgTableRow arg="features" typ="ubit (AP, synchronous, radiolan, wireless, extra-channels, , , )" syscap="nochr">Bitmask of licensed features.</ArgTableRow>
<ArgTableRow arg="expires-in" typ="time" syscap="nochr">Time remaining until the trial license expires.</ArgTableRow>
<ArgTableRow arg="system-id" typ="string" syscap="chr">Unique identifier for CHR instances, used for licensing. The license is tied directly to the CHR system ID.</ArgTableRow>
<ArgTableRow arg="level" typ="enum (free | p1 | p10 | p-unlimited) { free:0, p1:1, p10:2, p-unlimited:3 }" syscap="chr">Current CHR license level.</ArgTableRow>
<ArgTableRow arg="limited-upgrades" typ="bool" syscap="chr">Indicates whether RouterOS upgrades are limited. When the value is `yes`, RouterOS cannot be upgraded and package changes are disabled.</ArgTableRow>
<ArgTableRow arg="next-renewal-at" typ="date" syscap="chr">The next time the router attempts to contact the MikroTik license server.</ArgTableRow>
<ArgTableRow arg="deadline-at" typ="date" syscap="chr">The latest time by which successful communication with the license server must occur.</ArgTableRow>
</ArgTable>
