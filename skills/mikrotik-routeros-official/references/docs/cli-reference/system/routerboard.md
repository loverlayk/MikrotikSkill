# routerboard

> This menu allows you to view basic hardware and firmware information on RouterBOARD devices.

-----------

## system/routerboard 
**Conditions:** !i386
**Type:** Settings Directory

This menu allows you to view basic hardware and firmware information on RouterBOARD devices.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="routerboard" typ="bool">Indicates whether the device is a RouterBOARD unit.</ArgTableRow>
<ArgTableRow arg="board-name" typ="string"></ArgTableRow>
<ArgTableRow arg="model" typ="string">The RouterBOARD model number.</ArgTableRow>
<ArgTableRow arg="revision" typ="string"></ArgTableRow>
<ArgTableRow arg="serial-number" typ="string">The unique serial number of the device.</ArgTableRow>
<ArgTableRow arg="firmware-type" typ="string">The type of bootloader firmware used by the device.</ArgTableRow>
<ArgTableRow arg="minimum-firmware" typ="string">The firmware version installed at the factory.</ArgTableRow>
<ArgTableRow arg="current-firmware" typ="string">The version of the RouterBOOT loader currently in use. This should not be confused with the RouterOS operating system version.</ArgTableRow>
<ArgTableRow arg="upgrade-firmware" typ="string">RouterOS upgrades may include a new RouterBOOT version file, but it must be applied manually. This line indicates whether a new RouterBOOT file has been found on the device. The file may be included with a recent RouterOS upgrade or uploaded manually as an FWF file. In both cases, the newest available version is shown here.</ArgTableRow>
</ArgTable>
