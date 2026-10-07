# Ramdisk

> A ramdisk is a block device in RAM. Format it before use, or use it as a RAID member. It needs the rose-storage package and is empty after every reboot.

# Ramdisk

A ramdisk is a block device in RAM. Like a disk, it needs a file system before it can hold files, and it can be a member of a RAID or be used anywhere else a device is needed. A [tmpfs](tmpfs) is a folder in RAM instead: it holds files without formatting, but it is not a device and cannot be formatted or be a RAID member.

:::info
Ramdisks need the `rose-storage` package (see [Storage](./)). To install the package when it is available on the router, enable it and apply the change. Applying the change reboots the router:

```ros
/system/package/enable rose-storage
/system/package/apply-changes
```

For more about packages, see [Packages](../getting-started/installation-and-upgrade/packages).
:::

## Create and format a ramdisk

Add a ramdisk of 500 MB:

```ros
/disk/add type=ramdisk ramdisk-size=500M
```

The first ramdisk gets the slot name `ramdisk1`, the next ones `ramdisk2`, `ramdisk3` and so on. The size is rounded up to a multiple of 16 KiB. The router does not reserve the RAM when the ramdisk is added.

Format the ramdisk before you use it:

```ros
/disk/format ramdisk1 file-system=ext4
```

The formatted ramdisk is mounted at its slot name, so files go to paths such as `ramdisk1/capture.pcap`.

:::warning
The contents of a ramdisk are lost when the router reboots or loses power. After a reboot, the ramdisk is there again but empty and without a file system, so format it again before you use it.
:::

## Use ramdisks in a RAID

Ramdisks can be RAID members, for example to try a RAID configuration on a router without disks. To build a RAID 1 from two ramdisks, add the RAID and assign both ramdisks to it:

```ros
/disk/add type=raid raid-type=1 raid-device-count=2 slot=raid1
/disk/set ramdisk1 raid-master=raid1 raid-role=0
/disk/set ramdisk2 raid-master=raid1 raid-role=1
```

`/disk/print` then shows `raid1` with the model `RAID1 mirrored` and the state `clean`, and both ramdisks as RAID members with the member state `in_sync`. After a reboot, the router assembles the RAID again from the empty ramdisks. For more about RAID, see [RAID](raid/).

## Remove a ramdisk

Remove a RAID that uses ramdisks first, then the ramdisks:

```ros
/disk/remove raid1
/disk/remove ramdisk1
/disk/remove ramdisk2
```

For all parameters, see the [`/disk`](../cli-reference/disk/) CLI reference.
