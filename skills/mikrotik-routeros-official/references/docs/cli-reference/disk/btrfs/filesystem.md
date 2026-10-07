# filesystem

> RouterOS directory reference for /disk/btrfs/filesystem.

-----------

## disk/btrfs/filesystem 
**Conditions:** !smips
**Syscap:** storage
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="missing-devs">One or more devices of the file system are missing, so the file system is degraded.</ArgTableRow>
<ArgTableRow arg="b" typ="balancing">A balance operation is running on the file system.</ArgTableRow>
<ArgTableRow arg="r" typ="replacing">A device replace operation is running on the file system.</ArgTableRow>
<ArgTableRow arg="s" typ="scrubbing">A scrub operation is running on the file system.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="label" typ="string">Label of the Btrfs file system, used to address the file system in the btrfs menus, for example `btrfsdisk`.</ArgTableRow>
<ArgTableRow arg="default-subvolume" typ="enum">Subvolume that is presented as the root folder of the file system in `/file`. `<FS_ROOT>` (default) is the root of the Btrfs file system itself.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="uuid" typ="string">UUID of the Btrfs file system.</ArgTableRow>
<ArgTableRow arg="total-devs" typ="num">Number of devices in the file system.</ArgTableRow>
<ArgTableRow arg="dev-ids" typ="multi { array-id, devid: num
 }">Numeric device IDs of the devices in the file system; needed by [`replace-device`](replace-device) when a device is missing.</ArgTableRow>
<ArgTableRow arg="devs" typ="multi { array-id, dev: enum
 }">Disk slots of the devices in the file system, for example `nvme8,nvme9`.</ArgTableRow>
<ArgTableRow arg="spaces" typ="multi { array-id, space: string
 }">Space allocation of the file system, per device and per storage profile (`data`, `system`, `meta`, `global-reserve`), for example `data,raid1:1.07GB nvme8:1.07GB nvme9:1.07GB, used:1%`.</ArgTableRow>
<ArgTableRow arg="balance-status" typ="string">Status of the balance operation, for example `done`, or an error message such as `BTRFS_IOC_BALANCE_V2 failed: ...`.</ArgTableRow>
<ArgTableRow arg="replace-status" typ="string">Status of the replace or device removal operation, for example `done`, or an error message such as `BTRFS_IOC_DEV_REPLACE failed: File exists` or `BTRFS_IOC_RM_DEV_V2 failed: Resource temporarily unavailable`.</ArgTableRow>
<ArgTableRow arg="scrub-status" typ="string">Status of the scrub operation, for example `done`.</ArgTableRow>
<ArgTableRow arg="write-errors" typ="multi { snapshot: num
 }">Write error counters, one value per device in the file system. Reset with [`reset-counters`](reset-counters).</ArgTableRow>
<ArgTableRow arg="read-errors" typ="multi { snapshot: num
 }">Read error counters, one value per device.</ArgTableRow>
<ArgTableRow arg="flush-errors" typ="multi { snapshot: num
 }">Flush error counters, one value per device.</ArgTableRow>
<ArgTableRow arg="corruption-errors" typ="multi { snapshot: num
 }">Data corruption error counters, one value per device.</ArgTableRow>
<ArgTableRow arg="generation-errors" typ="multi { snapshot: num
 }">Generation mismatch error counters, one value per device.</ArgTableRow>
</ArgTable>
