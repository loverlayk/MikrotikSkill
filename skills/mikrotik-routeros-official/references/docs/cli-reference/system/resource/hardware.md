# hardware

> RouterOS directory reference for /system/resource/hardware.

-----------

## system/resource/hardware 
**Conditions:** !powerpc, !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="device-name" typ="string"></ArgTableRow>
<ArgTableRow arg="location" typ="string"></ArgTableRow>
<ArgTableRow arg="parent" typ="enum"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (usb | pci | scsi | serial)"></ArgTableRow>
<ArgTableRow arg="vendor" typ="string"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="category" typ="string"></ArgTableRow>
<ArgTableRow arg="serial-number" typ="string"></ArgTableRow>
<ArgTableRow arg="vendor-id" typ="string"></ArgTableRow>
<ArgTableRow arg="device-id" typ="string"></ArgTableRow>
<ArgTableRow arg="speed" typ="string"></ArgTableRow>
<ArgTableRow arg="ports" typ="num"></ArgTableRow>
<ArgTableRow arg="usb-version" typ="string"></ArgTableRow>
<ArgTableRow arg="manufacturer-reported-max-power" typ="string"></ArgTableRow>
<ArgTableRow arg="irq" typ="num"></ArgTableRow>
<ArgTableRow arg="memory" typ="multi { range: composite { min: num
, max: num
 }
 }"></ArgTableRow>
<ArgTableRow arg="io" typ="multi { range: composite { min: num
, max: num
 }
 }"></ArgTableRow>
<ArgTableRow arg="owner" typ="string"></ArgTableRow>
<ArgTableRow arg="device-path" typ="multi { path: string
 }"></ArgTableRow>
</ArgTable>
