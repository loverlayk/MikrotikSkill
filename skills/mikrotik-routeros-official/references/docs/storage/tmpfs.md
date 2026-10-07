# Tmpfs

> A tmpfs is a folder in RAM for temporary files such as packet captures and downloads. Its size is capped, and its contents are lost on reboot.

# Tmpfs

A tmpfs is a folder in RAM. RouterOS shows it as a disk, for example `tmp1`, and files go into it like into any other disk. Use it for files that are needed only for a while and should not wear out or fill the flash: packet captures, files that a script downloads and imports, and other temporary files. Tmpfs is part of the base RouterOS package and works on every device that has the `/disk` menu, which SMIPS devices do not have.

:::warning
The contents of a tmpfs are lost when the router reboots or loses power. Copy the files you want to keep to the flash, a USB disk or a computer.
:::

## Create a RAM folder

Add a folder that can hold up to 100 MB:

```ros
/disk/add type=tmpfs tmpfs-max-size=100M
```

```ros
[admin@MikroTik] > /disk/print
Flags: M - MOUNTED
Columns: SLOT, MOUNT-POINT, MODEL, INTERFACE, SIZE, FREE, USE, FS
#   SLOT  MOUNT-POINT  MODEL  INTERFACE         SIZE         FREE  USE  FS
0 M tmp1  tmp1         tmpfs  ram        100 003 840  100 003 840  0%   tmpfs
```

The first folder gets the slot name `tmp1`, the next one `tmp2`. The slot name is the start of the file path, for example `tmp1/capture.pcap`, and other commands refer to the folder by it.

Sizes use decimal units: `100M` is 100 000 000 bytes. The size in `/disk/print` is rounded up to whole 4 KiB memory pages, so the folder shows 100 003 840. `tmpfs-max-size` is the most the folder can grow to; RAM is used only by the files stored in it.

## Check what the folder shares

On routers whose default configuration turns on automatic disk sharing, a new tmpfs is shared as soon as it is created. Check the settings of your router first:

```ros
/disk/settings/print
```

The default configuration of the hAP ax², for example, sets `auto-smb-sharing=yes`, `auto-media-sharing=yes` and `auto-media-interface=bridge`. The folder then gets an SMB share for the read-only `guest` user, who needs no password, and a DLNA media server on `bridge`. When `/ip/smb` is set to `enabled=auto`, the share also starts the SMB server. The SMB server listens on all interfaces (`interfaces=all`), and only the firewall limits who reaches it; the default firewall allows the LAN. Anyone who reaches the SMB server can read the files in the folder as `guest`, packet captures included, unless the `guest` user is disabled in `/ip/smb/users`.

When automatic sharing is on, create the folder with sharing turned off. The setting stays after a reboot:

```ros
/disk/add type=tmpfs tmpfs-max-size=100M smb-sharing=no media-sharing=no
```

The flags `s` (SMB sharing) and `m` (media sharing) in `/disk/print` show which folders are shared. Here `tmp1` was created with the automatic sharing and `tmp2` with the previous command:

```ros
[admin@MikroTik] > /disk/print
Flags: M - MOUNTED; s - SMB-SHARING; m - MEDIA-SHARING
Columns: SLOT, MOUNT-POINT, MODEL, INTERFACE, SIZE, FREE, USE, FS
#     SLOT  MOUNT-POINT  MODEL  INTERFACE         SIZE         FREE  USE  FS
0 Msm tmp1  tmp1         tmpfs  ram        100 003 840  100 003 840  0%   tmpfs
1 M   tmp2  tmp2         tmpfs  ram        100 003 840  100 003 840  0%   tmpfs
```

The SMB share of a folder is a dynamic entry in `/ip/smb/shares`:

```ros
[admin@MikroTik] > /ip/smb/shares/print
Flags: D - DYNAMIC; X - DISABLED; * - DEFAULT
Columns: NAME, DIRECTORY, REQUIRE-ENCRYPTION, VALID-USERS
#     NAME  DIRECTORY  REQUIRE-ENCRYPTION  VALID-USERS
0  X* pub   /pub       no
1 D   tmp1  /tmp1      no                  guest
```

Stop sharing a folder that is already shared:

```ros
/disk/set tmp1 smb-sharing=no media-sharing=no
```

Stop sharing new disks and folders automatically:

```ros
/disk/settings/set auto-smb-sharing=no auto-media-sharing=no
```

To share files on purpose, with your own users, see [SMB](smb) and [DLNA media server](dlna).

## Keep packet captures in RAM

A packet capture can grow fast. Write it to the tmpfs instead of the flash, and keep `file-limit` (in KiB) below the folder size: `50000KiB` is about 51 MB, which fits in the 100 MB folder.

```ros
/tool/sniffer/set file-name=tmp1/capture.pcap file-limit=50000KiB \
    filter-interface=ether1
/tool/sniffer/start
```

Stop the capture when it has the packets you need:

```ros
/tool/sniffer/stop
```

Download `tmp1/capture.pcap` before the router reboots, with the Files menu in WinBox or WebFig (see [Manage files in WinBox](../system-information-and-utilities/files#manage-files-in-winbox)) or with `scp` from your computer:

```bash
scp admin@192.168.88.1:tmp1/capture.pcap .
```

For filters and live streaming, see [Packet sniffer](../diagnostics-monitoring-and-troubleshooting/packet-sniffer).

## Check how full the folder is

The `FREE` and `USE` columns of `/disk/print` show how much of the folder is used. They update a few seconds after a write. List the files in the folder:

```ros
[admin@MikroTik] > /file/print where name~"^tmp1"
Columns: NAME, TYPE, SIZE, LAST-MODIFIED
# NAME               TYPE        SIZE     LAST-MODIFIED
0 tmp1               disk                 2026-10-01 08:35:03
1 tmp1/capture.pcap  .pcap file  19.8KiB  2026-10-01 08:35:08
```

When the folder is full, writes to it fail. For example, `/tool/fetch` stops with `failure: cannot download: file too large, no space left on disk` and does not keep the partial file.

## Change the size or delete the folder

A new size applies at once, also to a mounted folder:

```ros
/disk/set tmp1 tmpfs-max-size=200M
```

Delete the folder together with all files in it. RouterOS does not ask for confirmation:

```ros
/disk/remove tmp1
```

## Technical details

### Size limit

Without `tmpfs-max-size` (it reads `0`), the folder can grow to about half of the router's RAM, for example 464 MB on a router with 1 GB of RAM. RouterOS adds up the maximum sizes of all tmpfs folders, counting a folder without `tmpfs-max-size` as half of the RAM, and refuses a new size when the total is more than the router can provide:

```text
failure: too much memory requested for tmpfs/ramdisk
```

### Memory use

An empty tmpfs reserves no RAM. The files in it use RAM and lower `free-memory` in `/system/resource`. Files that fill the RAM can make the router run out of memory, so keep `tmpfs-max-size` well below the free memory.

### After a reboot

The `/disk` entry and its settings stay in the configuration. After a reboot, RouterOS mounts the folder again under the same slot name, empty. Automatic SMB and DLNA shares of the folder come back with it, and a folder set to `smb-sharing=no` and `media-sharing=no` stays unshared.

### Not a block device

A tmpfs is a file system, not a block device, so it cannot be formatted:

```text
failure: cannot format nfs/smb/tmpfs/sshfs file systems
```

For RAM that works as a block device, for example as a RAID member, use a [Ramdisk](ramdisk).

For the parameters, see the [`/disk` CLI reference](../cli-reference/disk/).
