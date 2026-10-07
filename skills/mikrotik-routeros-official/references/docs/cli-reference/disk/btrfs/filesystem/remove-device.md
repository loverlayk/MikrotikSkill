# remove-device

> RouterOS command reference for /disk/btrfs/filesystem/remove-device.

-----------

## disk/btrfs/filesystem/remove-device 
**Conditions:** !smips
**Syscap:** storage
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum">Disk slot of the device to remove from the file system, for example `nvme9`. The data on the device is first migrated to the remaining devices; removal fails if the current profiles cannot be kept with fewer devices (for example `data,raid1` cannot be kept when the device count drops below two).</ArgTableRow>
<ArgTableRow arg="device-id" typ="num">Numeric device ID of the device to remove (see `dev-ids` in [`filesystem`](../filesystem)); needed when the device is missing and has no slot anymore.</ArgTableRow>
</ArgTable>
