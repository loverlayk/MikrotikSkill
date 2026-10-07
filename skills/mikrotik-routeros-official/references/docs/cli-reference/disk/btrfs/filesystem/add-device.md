# add-device

> RouterOS command reference for /disk/btrfs/filesystem/add-device.

-----------

## disk/btrfs/filesystem/add-device 
**Conditions:** !smips
**Syscap:** storage
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum">Disk slot to add to the Btrfs file system, for example `nvme9`. After adding a device, run [`balance-start`](balance-start) with the desired profiles (for example `data-profile=raid1`) to actually use it for storage redundancy; otherwise the device is only listed under `devs`.</ArgTableRow>
</ArgTable>
