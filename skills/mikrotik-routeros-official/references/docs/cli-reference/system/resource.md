# resource

> RouterOS settings reference for /system/resource.

-----------

## system/resource 
**Type:** Settings Directory
Overall resource usage and identity of the router: uptime, memory, disk, version, board. See the [Resource](../../../diagnostics-monitoring-and-troubleshooting/resource) guide.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="uptime" typ="time">Time interval passed since boot-up</ArgTableRow>
<ArgTableRow arg="version" typ="string">Installed RouterOS version number</ArgTableRow>
<ArgTableRow arg="build-time" typ="string">Installed RouterOS version build-time</ArgTableRow>
<ArgTableRow arg="minimum-version" typ="string">Minimum RouterOS version the board allows downgrading to (was factory-software)</ArgTableRow>
<ArgTableRow arg="free-memory" typ="num">The unused amount of RAM</ArgTableRow>
<ArgTableRow arg="total-memory" typ="num">Amount of installed RAM</ArgTableRow>
<ArgTableRow arg="cpu" typ="string">CPU model that is on the board</ArgTableRow>
<ArgTableRow arg="cpu-count" typ="num">Number of CPUs present on the system; each core is a separate CPU, Intel HT also counts as one CPU</ArgTableRow>
<ArgTableRow arg="cpu-frequency" typ="num">Current CPU frequency</ArgTableRow>
<ArgTableRow arg="cpu-load" typ="num">Percentage of used CPU resources, combined for all CPUs; per-core values are in [`/system/resource/cpu`](cpu)</ArgTableRow>
<ArgTableRow arg="free-hdd-space" typ="num">Free space on the hard drive or NAND</ArgTableRow>
<ArgTableRow arg="total-hdd-space" typ="num">Size of the hard drive or NAND</ArgTableRow>
<ArgTableRow arg="write-sect-since-reboot" typ="num">The number of sector writes to the drive/NAND since the router was last rebooted</ArgTableRow>
<ArgTableRow arg="write-sect-total" typ="num">The number of sector writes in total</ArgTableRow>
<ArgTableRow arg="bad-blocks" typ="num">Percentage of bad blocks on the NAND</ArgTableRow>
<ArgTableRow arg="architecture-name" typ="string">CPU architecture of this build (arm, arm64, x86, tile ...)</ArgTableRow>
<ArgTableRow arg="board-name" typ="string">RouterBOARD model name</ArgTableRow>
<ArgTableRow arg="platform" typ="string">Platform name</ArgTableRow>
</ArgTable>
