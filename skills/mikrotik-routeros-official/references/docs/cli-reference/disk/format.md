# format

> RouterOS command reference for /disk/format.

-----------

## disk/format 
**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file-system" typ="enum (fat32 | ext4 | btrfs | xfs | wipe | wipe-quick | exfat | discard | discard-secure)">
What filesystem to format the disk.
- `ext4` - Format with ext4; the default for most use cases.
- `fat32` - Format with FAT32, readable by almost any device.
- `exfat` - Format with exFAT, for large files on memory cards and USB drives.
- `btrfs` - Format with Btrfs (data checksums, snapshots, RAID); needs the [Storage](../../storage/) package.
- `xfs` - Format with XFS; needs the [Storage](../../storage/) package.
- `discard` - Discard all blocks of the disk (the equivalent of `blkdiscard`) without writing a file system.
- `discard-secure` - Same, but with a secure discard that also erases the underlying data.
- `wipe` - Overwrite all data on the disk so it cannot be recovered.
- `wipe-quick` - Remove the file system without overwriting the data; fast, but data can be recovered with tools.
</ArgTableRow>
<ArgTableRow arg="label" typ="string">File system label. Default: `<slot>-fs`.</ArgTableRow>
<ArgTableRow arg="mbr-partition-table" typ="bool">Write an MBR partition table to the disk as part of the format. Without it the disk receives no partition table; use `add type=partition` afterwards to create partitions, which are stored in a GUID partition table. Default: no.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="output" typ="string">Progress of the format: the `mkfs` command line and its output, a progress percentage or byte counter, and a final `format done` line.</ArgTableRow>
</ArgTable>
