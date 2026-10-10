# hardware

> RouterOS directory reference for /system/resource/hardware.

-----------

## system/resource/hardware 
**Conditions:** !powerpc, !smips
**Type:** Directory
Detected hardware devices connected over PCI, USB or SCSI buses. Empty on boards with no such bus (for example the hAP ax²).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive">inactive: the device is present but not active</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="device-name" typ="string">Name of the device as reported by its firmware (name column refinement)</ArgTableRow>
<ArgTableRow arg="location" typ="string">Device location in the system topology</ArgTableRow>
<ArgTableRow arg="parent" typ="enum">Parent bus or controller</ArgTableRow>
<ArgTableRow arg="type" typ="enum (usb | pci | scsi | serial)">Bus type of the device: `usb`, `pci`, `scsi` or `serial`</ArgTableRow>
<ArgTableRow arg="vendor" typ="string">Device vendor name</ArgTableRow>
<ArgTableRow arg="name" typ="string">Device name or model</ArgTableRow>
<ArgTableRow arg="category" typ="string">Device category</ArgTableRow>
<ArgTableRow arg="serial-number" typ="string">Device serial number</ArgTableRow>
<ArgTableRow arg="vendor-id" typ="string">Vendor identifier (VID)</ArgTableRow>
<ArgTableRow arg="device-id" typ="string">Device identifier (PID / Device ID)</ArgTableRow>
<ArgTableRow arg="speed" typ="string">Negotiated device speed</ArgTableRow>
<ArgTableRow arg="ports" typ="num">Number of ports provided by the device</ArgTableRow>
<ArgTableRow arg="usb-version" typ="string">Supported USB version</ArgTableRow>
<ArgTableRow arg="manufacturer-reported-max-power" typ="string">Maximum power draw reported by the device (for example a USB modem)</ArgTableRow>
<ArgTableRow arg="irq" typ="num">Assigned interrupt number</ArgTableRow>
<ArgTableRow arg="memory" typ="multi { range: composite { min: num
, max: num
 }
 }">Memory window assigned to the device</ArgTableRow>
<ArgTableRow arg="io" typ="multi { range: composite { min: num
, max: num
 }
 }">I/O window assigned to the device</ArgTableRow>
<ArgTableRow arg="owner" typ="string">Subsystem or driver owning the device</ArgTableRow>
<ArgTableRow arg="device-path" typ="multi { path: string
 }">Device path from root bus to endpoint</ArgTableRow>
</ArgTable>
