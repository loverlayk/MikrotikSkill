# replace-device

> RouterOS command reference for /disk/btrfs/filesystem/replace-device.

-----------

## disk/btrfs/filesystem/replace-device 
**Conditions:** !smips
**Syscap:** storage
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device-to-remove" typ="enum">Disk slot of the device to replace in the Btrfs file system.</ArgTableRow>
<ArgTableRow arg="device-to-remove-id" typ="num">Numeric device ID of the device to replace; use this instead of `device-to-remove` when the device is missing from the system (the `I - MISSING-DEVS` flag), as the slot is then no longer available.</ArgTableRow>
<ArgTableRow arg="device-to-add" typ="enum">Disk slot of the new device that takes over the data of the removed device.</ArgTableRow>
</ArgTable>
