# Disks

> How RouterOS detects, formats and manages disks and partitions: slot names, automatic mounting, mount points, partitions, swap space, RAM-backed folders, file system checks and performance tests.

# Disks

[*Disks CLI Reference*](../../cli-reference/disk/)

RouterOS detects the storage drives connected to the router (USB, SATA, NVMe and microSD drives) and mounts them automatically at boot or when they are plugged in. You can use as many drives as the router supports, for example for the User Manager database, the web proxy cache, container storage or log files.

This page covers the drives themselves: how they are detected, formatted and managed. Network storage protocols (iSCSI, NFS, SMB, NVMe over TCP), RAID and the advanced file systems are part of the [Storage](../../storage/) package and are covered in the [Storage](../../storage/) section.

:::info
The **Storage package** adds disk monitoring, RAID, rsync, iSCSI, NVMe over TCP, NFS, an SMB client and the Btrfs and XFS file systems. See the [Storage](../../storage/) section for details.
:::

:::danger
Always use `/disk/eject` before physically removing a disk from a RouterOS device, otherwise data can be lost.
:::

## How disks are detected

The `/disk` menu lists every attached storage device that is supported and in working condition, including empty drive slots. Each drive gets a slot name from the interface it is connected with and a number, for example `usb1`, `sata1` or `nvme1`.

```ros
[admin@MikroTik] > /disk/print proplist=slot,model,interface,size,fs where slot=nvme9
Flags: B - BLOCK-DEVICE
Columns: SLOT, MODEL, INTERFACE, SIZE, FS
#   SLOT   MODEL        INTERFACE                   SIZE  FS
0 B nvme9  TS1TUTE210T  PCIe 2x8 GT/s  1 024 209 543 168  -
```

Key flags in the print output:

- `B - BLOCK-DEVICE` marks a device that stores data, so it can be formatted and used. Devices without this flag, for example a PCIe bridge, only describe the disk layout.
- `E - EMPTY` marks an empty slot.
- `M - MOUNTED` marks a disk or partition whose file system is mounted.

The complete flag list is described in the [Disks CLI Reference](../../cli-reference/disk/).

A drive with a supported file system and partition table is mounted automatically and appears in `/file`. To confirm that a drive is usable, check that it is present in `/file` after it is connected.

## Format a disk

The first thing to do with a new drive is to format it. To format a disk, select the file system and run `/disk/format` with the slot name. RouterOS asks for confirmation, formats the drive and mounts it automatically:

```ros
[admin@MikroTik] > /disk/format nvme9 file-system=ext4
nvme9: file-system: ext4
nvme9: mke2fs -t ext4 -L nvme9-fs /dev/nvme0n1
...
nvme9: Creating journal (262144 blocks): done
nvme9: Writing superblocks and filesystem accounting information: done
nvme9: format done
```

Without a label, RouterOS labels the file system `<slot>-fs`, so the label of `nvme9` is `nvme9-fs`. File system choices:

- `ext4`  -  the default choice for most use cases. Supports multiple partitions, journaling and is fast.
- `fat32` and `exfat`  -  readable by almost any device, for example cameras or Android phones. `fat32` has a 4 GB file size limit.
- `btrfs` and `xfs`  -  advanced file systems that need the [Storage](../../storage/) package. See [Btrfs](../../storage/btrfs/).
- `discard` and `discard-secure`  -  discard all blocks of the drive without writing a file system.
- `wipe` and `wipe-quick`  -  remove the file system and all data. `wipe` overwrites the data so it cannot be recovered; `wipe-quick` only removes the file system.

Formatting destroys all data on the target. For a disk with a partially filled file system, use `file-system=wipe-quick` to remove it fast.

After formatting, the drive is mounted automatically:

```ros
[admin@MikroTik] > /disk/print where slot=nvme9
Flags: B - BLOCK-DEVICE; M - MOUNTED
Columns: SLOT, MOUNT-POINT, MODEL, INTERFACE, SIZE, FS
#    SLOT   MOUNT-POINT  MODEL        INTERFACE                   SIZE  FS
0 BM nvme9  nvme9        TS1TUTE210T  PCIe 2x8 GT/s  1 024 209 543 168  ext4
```

```ros
[admin@MikroTik] > /file/print where name~"nvme9"
Columns: NAME, TYPE, LAST-MODIFIED
# NAME              TYPE       LAST-MODIFIED
0 nvme9             disk       2026-09-25 11:47:05
1 nvme9/lost+found  directory  2026-09-25 11:47:05
```

## Mount points

A mounted file system is accessible under its mount point, which is also the path prefix used in `/file` and when other features reference a file. By default the mount point is the slot name, so files on `nvme1` are addressed as `nvme1/...`.

When the same drive can end up in different slots between boots, for example in a multi-bay enclosure, give it a stable mount point with `mount-point-template`. The template can combine the following variables:

- `[slot]`
- `[model]`
- `[serial]`
- `[fw-version]`
- `[fs-label]`
- `[fs-uuid]`
- `[fs]`

For example, to mount a drive by its serial number:

```ros
/disk/set nvme1 mount-point-template="[serial]"
```

Variables can be combined, for example `mount-point-template="[model]-[fs]"`. An empty template is rejected. The `default-mount-point-template` setting in `/disk/settings` applies the template to every new disk and partition.

## Partitions

To split a drive into several partitions, format it without a partition table and then add partitions. RouterOS keeps the partition information in a GUID partition table (GPT).

```ros
/disk/format nvme9 file-system=ext4
/disk/add type=partition parent=nvme9 partition-size=4G
```

```ros
[admin@MikroTik] > /disk/print where slot~"nvme9"
Flags: B - BLOCK-DEVICE; g - GUID-PARTITION-TABLE, p - PARTITION
Columns: SLOT, MODEL, INTERFACE, SIZE, FS
#    SLOT         MODEL        INTERFACE                   SIZE  FS
0 Bg nvme9        TS1TUTE210T  PCIe 2x8 GT/s  1 024 209 543 168  -
1 Bp nvme9-part1  TS1TUTE210T                     4 000 000 000  -
```

Each partition gets a slot name of its own, derived from the parent: the first partition of `nvme9` is `nvme9-part1`. The `g - GUID-PARTITION-TABLE` flag marks the parent and `p - PARTITION` marks the partitions.

- Without `partition-size`, the partition uses all remaining space on the drive.
- Use `partition-offset` to set where the partition starts, in bytes.
- A partition is used like a disk: format it, mount it and manage it under its own slot name.
- `mbr-partition-table=yes` in `/disk/format` writes an MBR partition table instead; use it only when a GPT table is not accepted by the target system.

## Swap space

:::info
Swap space requires the [container](../../containers/) package.
:::

Swap space is reserved for [containers](../../containers/) and lets them run with more memory than the router has. It can be a whole partition or a file. Swap size is limited to 10 times the router's available RAM.

A swap partition dedicates the whole disk or partition to swap and gives better performance than a file:

```ros
/disk/set nvme9-part1 swap=yes
```

A swap file resides on an existing file system, for example on a [Btrfs](../../storage/btrfs/) disk, and uses only as much space as its size:

```ros
/disk/add type=file file-path=nvme9-part1/swapfile file-size=512M swap=yes
```

The swap file appears in `/disk` with the `S - SWAP-ENABLED` flag:

```ros
[admin@MikroTik] > /disk/print where slot~"nvme9"
Flags: B - BLOCK-DEVICE; M - MOUNTED, S - SWAP-ENABLED
       g - GUID-PARTITION-TABLE, p - PARTITION
Columns: SLOT, MOUNT-POINT, SIZE, FS, SWAP
#     SLOT                       MOUNT-POINT               SIZE  FS    SWAP
0 B g nvme9                                   1 024 209 543 168  -     no
1 BMp nvme9-part1                nvme9-part1      4 000 000 000  ext4  no
2  S  file-nvme9-part1-swapfile                     536 866 816  -     yes
```

## RAM-backed folder

To keep files in RAM, add a `tmpfs` folder. Its content is emptied when the router reboots or loses power.

```ros
/disk/add type=tmpfs tmpfs-max-size=100M
```

The folder appears in `/file` as a disk entry, for example `tmp1`. `tmpfs-max-size` caps how much RAM the folder can use. Use a RAM-backed folder on devices with limited storage or for data that must be cleared on reboot. For size limits, sharing and what happens after a reboot, see [Tmpfs](../../storage/tmpfs).

## Mount images

RouterOS can also mount `.iso` and `.squashfs` images directly. To mount an image, use the following command:

```ros
/disk/add type=file file-path=disk1/mycopy.iso
```

Make sure you change `disk1/mycopy.iso` to your correct path, where the image is located.

## Log on disk

When configuring logging on disk, make sure that you create directories in which you want to store the log files manually, as non-existent directories will not be created automatically in this case.

```ros
[admin@MikroTik] >  /system/logging/action/set disk disk-file-name=disk1/log
```

The log files appear in `/file` under the directory you created:

```ros
[admin@MikroTik] >  /file/print where name~"disk1/log"
 # NAME                                              TYPE                             SIZE CREATION-TIME
 0 disk1/log                                        directory                             2015-07-03 12:44:09
 1 disk1/log/syslog.0.txt                           .txt file                         160 2015-07-03 12:44:11
```

:::note
Logging topics such as firewall and web-proxy tend to save a large amount or rapid printing of logs on the system NAND disk, which can wear it out faster. Use attached storage or remote logging in this case, or save data in a RAM folder.
:::

## Web proxy cache on a disk

The web proxy carries its cache on a disk, usually a USB drive. Set the cache path under `IP -> Proxy` (the `cache-path` setting of `/ip/proxy`) and the web proxy store is automatically created in `/file`. If a non-existent directory path is used, the additional sub-directories are also created automatically:

```ros
[admin@MikroTik] >  /ip/proxy/set cache-path=usb1/cache-n-db/proxy/
```

```ros
[admin@MikroTik] >  /file/print
 # NAME                                              TYPE                             SIZE CREATION-TIME
 0 skins                                             directory                             2015-03-02 18:56:23
 1 sys-note.txt                                      .txt file                        23   2015-07-03 11:40:48
 2 usb1                                             disk                                  2015-07-03 11:35:05
 3 usb1/lost+found                                  directory                             2015-07-03 11:34:56
 4 usb1/cache-n-db                                  directory                             2015-07-03 11:41:54
 5 usb1/cache-n-db/proxy                            web-proxy store                       2015-07-03 11:42:09
```

See [Web proxy](../../network-management/proxy/web-proxy) for the cache configuration.

## Check and repair

`/disk/check` and `/disk/repair` run a file system check on a drive, the equivalent of `fsck`/`e2fsck`. They work on ext4, Btrfs and XFS. A file system that is still in use cannot be checked:

```ros
/disk/check nvme9-part1
Columns: OUTPUT
OUTPUT
could not unmount, stop using it first
```

This also happens when a swap file on the partition keeps it in use  -  remove the swap item before checking the partition. Unmount the file system first:

```ros
/disk/set nvme9-part1 mount-filesystem=no
```

`check` reports errors without changing anything:

```ros
/disk/check nvme9-part1
Columns: OUTPUT
OUTPUT
e2fsck 1.46.5 (30-Dec-2021)
Pass 1: Checking inodes, blocks, and sizes
Pass 2: Checking directory structure
Pass 3: Checking directory connectivity
Pass 4: Checking reference counts
Pass 5: Checking group summary information
nvme9-part1-fs: 12/244320 files (0.0% non-contiguous), 166617/976562 blocks
```

`repair` fixes the errors it finds:

```ros
/disk/repair nvme9-part1
Columns: OUTPUT
OUTPUT
e2fsck 1.46.5 (30-Dec-2021)
nvme9-part1-fs: clean, 12/244320 files, 166617/976562 blocks
```

## Test disk performance

`/disk/test` measures the sustained throughput and IOPS of a drive. The test runs in the background and prints a row per completed block, plus a `TOT` row that aggregates the result.

```ros
/disk/test disk=nvme9-part2 direction=read pattern=sequential type=device block-size=4K duration=20
Columns: SEQ, RATE, IOPS, BYTES, DISK, THREAD, TYPE, PATTERN, DIR, BSIZE, STATE
  ...  11.7Gbps  359 651  1404.9MiB  nvme9-part2  0  device  sequential  read  4096
  ...  11.8Gbps  360 192  1407.0MiB  nvme9-part2  0  device  sequential  read  4096
R TOT  11.8Gbps  360 676  26.1GiB    nvme9-part2  0  device  sequential  read  4096
```

- `direction=read` leaves the drive content unchanged and works on a mounted file system.
- `direction=write` destroys all data on the target; run write tests only on drives you are ready to wipe.
- Give the test a `duration` so it stops by itself; without one it keeps running until stopped.
- A new test prepares for a while  -  the `state` column shows `clear caches` until it starts producing numbers.

:::danger
Disk performance tests may slowly degrade disk health.

A write will destroy all data on the drive it is run on.
:::

## Monitor traffic and counters

`/disk/monitor-traffic` shows live activity of a drive: I/O operations, transferred bytes and speed, as totals and per second:

```ros
/disk/monitor-traffic nvme9-part2 once
                  slot:    nvme9-part2
              read-ops:        113 229
   read-ops-per-second:              0
            read-bytes: 29 668 814 848
             read-rate:           0bps
           read-merges:              0
             read-time:       48s149ms
             write-ops:              0
```

`/disk/reset-counters` resets these counters to zero, including the error counters.

## Eject and scan

Before removing a drive, eject it so no data is lost:

```ros
/disk/eject nvme9
```

An ejected drive is unmounted and its slot shows the `E - EMPTY` flag until the drive is removed. `/disk/scan` re-detects drives that were plugged in or removed without a reboot and brings back a drive after reconnecting it.

`/disk/trim` discards the unused blocks of a mounted file system (`fstrim` equivalent) so SSD write performance does not degrade. Trimming is not supported on USB drives, and some NVMe enclosures do not support it either.

## S.M.A.R.T. drive health

Drive health monitoring with S.M.A.R.T. reads the diagnostics of drives that support it, for example temperature, use and error counters. See [S.M.A.R.T. info](./smart).

## Related

- [Storage](../../storage/)  -  RAID, network storage protocols and the advanced file systems.
- [Containers](../../containers/)  -  uses disk space for images and swap space.
- [S.M.A.R.T. info](./smart)  -  drive health monitoring.
- [Disks CLI Reference](../../cli-reference/disk/)  -  every command and parameter of `/disk`.
