# disk

> RouterOS directory reference for /disk.

-----------

## disk 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The device is disabled and is not used.</ArgTableRow>
<ArgTableRow arg="A" typ="acquired">acquired</ArgTableRow>
<ArgTableRow arg="E" typ="empty">The slot is empty, with no disk present. After `eject`, the slot stays empty until the disk is rescanned with `scan` or replugged.</ArgTableRow>
<ArgTableRow arg="B" typ="block-device">The device is a block device, that is, it can be used as storage: formatted or used in a RAID array. Devices without this flag only describe the disk layout.</ArgTableRow>
<ArgTableRow arg="M" typ="mounted">The device is mounted and its files appear in `/file`.</ArgTableRow>
<ArgTableRow arg="F" typ="formatting">The device is currently being formatted.</ArgTableRow>
<ArgTableRow arg="S" typ="swap-enabled">Swap is enabled on the device (`swap=yes`); the device is used as swap space, for example by containers.</ArgTableRow>
<ArgTableRow arg="f" typ="raid-member-failed">A member of the RAID array is in failed state.</ArgTableRow>
<ArgTableRow arg="r" typ="raid-member">The device is a member of a RAID array.</ArgTableRow>
<ArgTableRow arg="c" typ="encrypted">The device is encrypted, for example with `type=crypted` (dm-crypt).</ArgTableRow>
<ArgTableRow arg="g" typ="guid-partition-table">The device has a GUID partition table (GPT).</ArgTableRow>
<ArgTableRow arg="p" typ="partition">The device is a partition of a disk.</ArgTableRow>
<ArgTableRow arg="t" typ="nvme-tcp-export">The device is exported as an NVMe-over-TCP target.</ArgTableRow>
<ArgTableRow arg="i" typ="iscsi-export">The device is exported as an iSCSI target.</ArgTableRow>
<ArgTableRow arg="s" typ="smb-sharing">The device is shared through the built-in SMB server.</ArgTableRow>
<ArgTableRow arg="n" typ="nfs-sharing">The device is shared with the NFS server.</ArgTableRow>
<ArgTableRow arg="m" typ="media-sharing">The device is shared through the DLNA media server.</ArgTableRow>
<ArgTableRow arg="L" typ="self-encrypted-and-locked">self-encrypted-and-locked</ArgTableRow>
<ArgTableRow arg="O" typ="self-encryption-enabled">TCG-Opal self-encryption is active on the drive.</ArgTableRow>
<ArgTableRow arg="o" typ="self-encryption-supported">The drive supports TCG-Opal self-encryption, but it is not enabled.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (raid | nvme-tcp | iscsi | nfs | smb | partition | tmpfs | ramdisk | crypted | sshfs | file | hardware)" mandatory="1">
Type of the item:
- `hardware` - a physical disk attached to the router, for example in a USB, SATA or NVMe slot.
- `partition` - a partition on a hardware disk (see `parent`).
- `file` - a file mounted as a block device (loop), for example a swap file or a mounted `.iso` / `.squashfs` image.
- `tmpfs` - a folder in RAM, see [Tmpfs](../../storage/tmpfs).
- `ramdisk` - part of RAM used as a block device, see [Ramdisk](../../storage/ramdisk) (storage package).
- `raid` - a RAID array built from several disks, see [RAID](../../storage/raid/) (storage package).
- `crypted` - a dm-crypt encrypted block device, see [Encrypted storage](../../storage/encrypted-storage) (storage package).
- `nvme-tcp` - a disk mounted over NVMe over TCP, see [NVMe over TCP](../../storage/nvme-over-tcp) (storage package).
- `iscsi` - an iSCSI target mounted as a disk, see [iSCSI](../../storage/iscsi) (storage package).
- `nfs` - an NFS share mounted as a disk, see [NFS](../../storage/nfs) (storage package).
- `smb` - an SMB share mounted as a disk, see [SMB](../../storage/smb) (storage package).
- `sshfs` - a remote folder mounted over SSH.
</ArgTableRow>
<ArgTableRow arg="slot" typ="string">Name of the disk item, normally based on where the device is physically connected, for example `nvme1` or `usb1`. The name is assigned automatically and can be set manually. Other commands and `parent` refer to the disk by this name.</ArgTableRow>
<ArgTableRow arg="parent" typ="enum ()">Parent device of the item. On a `type=partition` item it selects the hardware disk the partition is created on, for example `add type=partition parent=nvme9 ...`; on `type=crypted` it is the drive or partition that is encrypted.</ArgTableRow>
<ArgTableRow arg="mount-point-template" typ="string">
Template of the mount point, the folder under which the file system appears in `/file`. The following variables are replaced:
- `[slot]` (default) - the slot name.
- `[model]` - the device model.
- `[serial]` - the device serial number.
- `[fw-version]` - the device firmware version.
- `[fs-label]` - the file system label.
- `[fs-uuid]` - the file system UUID.
- `[fs]` - the file system type.
Variables can be combined, for example `[model]-[fs]`. An empty template is rejected, and `unset mount-point-template` restores the default `[slot]`. The default for newly added disks is set by `default-mount-point-template` in [`settings`](settings). See [Disks](../../hardware/disks/).
</ArgTableRow>
<ArgTableRow arg="mount-filesystem" typ="bool">Whether the device's file system is mounted, so its files are available in `/file`. `mount-filesystem=no` unmounts the file system, which is required before `/disk check` or `/disk repair`. Default: yes.</ArgTableRow>
<ArgTableRow arg="mount-read-only" typ="bool">Whether the mounted file system is read-only. Default: no.</ArgTableRow>
<ArgTableRow arg="compress" typ="bool">Whether the device's file system is mounted with compression. Only supported on `btrfs` file systems; RouterOS reports `compression only available for btrfs` when it is set on other file systems. Default: no.</ArgTableRow>
<ArgTableRow arg="partition-number" typ="num">Number of the partition on the parent disk, for example `partition-number=1` for the first partition.</ArgTableRow>
<ArgTableRow arg="partition-offset" typ="num">Start offset of the partition on the disk, in bytes. Use it to adjust where the partition begins.</ArgTableRow>
<ArgTableRow arg="partition-size" typ="num">Size of the partition in bytes. When it is not set, the partition takes the remaining space on the disk. See [Disks](../../hardware/disks/).</ArgTableRow>
<ArgTableRow arg="raid-type" typ="enum (0 | 1 | 4 | 5 | 6 | linear) { 0:0, 1:1, 4:4, 5:5, 6:6 }" syscap="storage">
RAID level of the array:
- `0` - striping: data is spread evenly over all disks, no fault tolerance, best performance.
- `1` - mirroring: the same data is written to all disks, best fault tolerance.
- `4` - block-level striping with parity stored on a dedicated disk.
- `5` - block-level striping with distributed parity, survives one disk failure.
- `6` - block-level striping with double parity, survives two disk failures.
- `linear` - the disks are joined into one large disk without redundancy.
See [RAID](../../storage/raid/).
</ArgTableRow>
<ArgTableRow arg="raid-device-count" typ="num" syscap="storage">Number of devices (disks) in the RAID array, set when the array is created.</ArgTableRow>
<ArgTableRow arg="raid-max-component-size" typ="num" syscap="storage">Maximum size of an individual device in the RAID array.</ArgTableRow>
<ArgTableRow arg="raid-chunk-size" typ="enum (64K | 128K | 256K | 512K | 1M | 2M | 4M) { 64K:64, 128K:128, 256K:256, 512K:512, 1M:1024, 2M:2048, 4M:4096 }" syscap="storage">Size of the chunks (stripes) written across the disks of the array, for example `1M`.</ArgTableRow>
<ArgTableRow arg="raid-master" typ="enum (none)" syscap="storage">RAID block device a disk belongs to. Set it together with `raid-role` on the member disks to add them to an array created with `add type=raid ...`. On the RAID item itself it is `none`.</ArgTableRow>
<ArgTableRow arg="raid-role" typ="num" syscap="storage">Position of the disk within the RAID array, set with `raid-master`, starting from 0, or `spare` to mark the disk as a hot spare.</ArgTableRow>
<ArgTableRow arg="raid-member-failed" typ="bool" syscap="storage">Marks a drive as failed in the RAID array. Used when a non-failed drive needs to be replaced.</ArgTableRow>
<ArgTableRow arg="nvme-tcp-export" typ="bool" syscap="storage">Whether the device is exported as an NVMe-over-TCP target, so other devices can mount it. Default: no. See [NVMe over TCP](../../storage/nvme-over-tcp).</ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-port" typ="num" syscap="storage">Port on which the NVMe-over-TCP server accepts connections from initiators. See [NVMe over TCP](../../storage/nvme-over-tcp).</ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-nqn" typ="string" syscap="storage">NVMe Qualified Name (NQN) of the exported device, used by initiators to connect. See [NVMe over TCP](../../storage/nvme-over-tcp).</ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-allow-host-name" typ="string" syscap="storage">Hostnames allowed to connect to the NVMe-over-TCP server, for host-based access control. See [NVMe over TCP](../../storage/nvme-over-tcp).</ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-password" typ="string" syscap="storage">Password the NVMe-over-TCP server requires from initiators. See [NVMe over TCP](../../storage/nvme-over-tcp).</ArgTableRow>
<ArgTableRow arg="nvme-tcp-address" typ="ipAddr" syscap="storage">IP address of the NVMe-over-TCP target (host) to mount, on the `nvme-tcp` client. See [NVMe over TCP](../../storage/nvme-over-tcp).</ArgTableRow>
<ArgTableRow arg="nvme-tcp-nqn" typ="string" syscap="storage">NVMe Qualified Name (NQN) of the target on the server to mount, on the `nvme-tcp` client. See [NVMe over TCP](../../storage/nvme-over-tcp).</ArgTableRow>
<ArgTableRow arg="nvme-tcp-host-name" typ="string" syscap="storage">Hostname the `nvme-tcp` initiator (client) identifies itself with; used for identification and authentication on the server. See [NVMe over TCP](../../storage/nvme-over-tcp).</ArgTableRow>
<ArgTableRow arg="nvme-tcp-password" typ="string" syscap="storage">Password used to authenticate the NVMe-over-TCP connection to the server. See [NVMe over TCP](../../storage/nvme-over-tcp).</ArgTableRow>
<ArgTableRow arg="nvme-tcp-port" typ="num" syscap="storage">Port the NVMe-over-TCP target listens on for connections from initiators. Default: 4420. See [NVMe over TCP](../../storage/nvme-over-tcp).</ArgTableRow>
<ArgTableRow arg="iscsi-export" typ="bool" syscap="storage">Whether the device is exported as an iSCSI target. Default: no. See [iSCSI](../../storage/iscsi).</ArgTableRow>
<ArgTableRow arg="iscsi-server-port" typ="num" syscap="storage">Port the iSCSI server listens on. See [iSCSI](../../storage/iscsi).</ArgTableRow>
<ArgTableRow arg="iscsi-server-iqn" typ="string" syscap="storage">iSCSI Qualified Name (IQN) of the iSCSI server, by default `iqn.2000-02.com.mikrotik:<slot>`. See [iSCSI](../../storage/iscsi).</ArgTableRow>
<ArgTableRow arg="iscsi-port" typ="num" syscap="storage">Port the iSCSI target listens on for connections from initiators. Default: 3260. See [iSCSI](../../storage/iscsi).</ArgTableRow>
<ArgTableRow arg="iscsi-address" typ="ipAddr" syscap="storage">IP address of the iSCSI target (host) to mount, on the `iscsi` client. See [iSCSI](../../storage/iscsi).</ArgTableRow>
<ArgTableRow arg="iscsi-iqn" typ="string" syscap="storage">iSCSI Qualified Name (IQN) of the target to mount, on the `iscsi` client. See [iSCSI](../../storage/iscsi).</ArgTableRow>
<ArgTableRow arg="nfs-sharing" typ="bool" syscap="storage">Whether the device is shared with NFS, so network clients can mount it. Default: no. See [NFS](../../storage/nfs).</ArgTableRow>
<ArgTableRow arg="nfs-address" typ="ipAddr" syscap="storage">IP address of the NFS server to mount, on the `nfs` client. See [NFS](../../storage/nfs).</ArgTableRow>
<ArgTableRow arg="nfs-share" typ="string" syscap="storage">Folder to mount on the NFS server, on the `nfs` client. See [NFS](../../storage/nfs).</ArgTableRow>
<ArgTableRow arg="smb-sharing" typ="bool">Whether the device is shared through the built-in SMB server (`/ip/smb`) when it is mounted. With `auto-smb-sharing=yes` in [`settings`](settings) it is enabled automatically. Default: no.</ArgTableRow>
<ArgTableRow arg="smb-server-user" typ="enum ()">SMB user of the auto-created share of this disk; the default for new disks is taken from `auto-smb-user` in [`settings`](settings).</ArgTableRow>
<ArgTableRow arg="smb-server-password" typ="string">Password of the SMB user of the auto-created share.</ArgTableRow>
<ArgTableRow arg="smb-server-encryption" typ="bool">Whether connections to the SMB share of this disk must be encrypted.</ArgTableRow>
<ArgTableRow arg="smb-address" typ="ipAddr">IP address of the SMB server to mount, on the `smb` client. See [SMB](../../storage/smb).</ArgTableRow>
<ArgTableRow arg="smb-share" typ="string">Name of the share to mount on the server, on the `smb` client. See [SMB](../../storage/smb).</ArgTableRow>
<ArgTableRow arg="smb-user" typ="string">SMB user to authenticate with, on the `smb` client. See [SMB](../../storage/smb).</ArgTableRow>
<ArgTableRow arg="smb-password" typ="string">Password of the SMB user, on the `smb` client.</ArgTableRow>
<ArgTableRow arg="smb-encryption" typ="bool">Whether the connection to the remote SMB share is encrypted, on the `smb` client.</ArgTableRow>
<ArgTableRow arg="media-sharing" typ="bool">Whether the device is shared through the DLNA media server (`/ip/media`) when it is mounted. With `auto-media-sharing=yes` in [`settings`](settings) it is enabled automatically. Default: no.</ArgTableRow>
<ArgTableRow arg="media-interface" typ="iface_enum { none }">Interface the DLNA media server uses for the share of this disk, set together with `media-sharing=yes`.</ArgTableRow>
<ArgTableRow arg="tmpfs-max-size" typ="num">Maximum size of a `tmpfs` folder, in decimal units (`100M` is 100 000 000 bytes). The folder uses RAM only for the files stored in it. When the size is not set (it reads `0`), the folder can grow to about half of the RAM. RouterOS adds up the maximum sizes of all tmpfs folders, counting a folder without `tmpfs-max-size` as half of the RAM, and refuses a new size when the total is more than the router can provide (`too much memory requested for tmpfs/ramdisk`). The size in `print` is rounded up to whole 4 KiB memory pages. A new value applies at once, also to a mounted folder. The contents of a `tmpfs` are lost on reboot or power loss. See [Tmpfs](../../storage/tmpfs). Default: not set.</ArgTableRow>
<ArgTableRow arg="ramdisk-size" typ="num" syscap="storage">Size of the RAM block device created with `type=ramdisk`, rounded up to a multiple of 16 KiB. The RAM is not reserved when the ramdisk is added. A reboot or power loss clears it: the ramdisk stays, but empty and without a file system, so format it again. Needs the `rose-storage` package. See [Ramdisk](../../storage/ramdisk).</ArgTableRow>
<ArgTableRow arg="crypted-backend" typ="enum (none)" syscap="storage">The drive or partition to encrypt with `type=crypted`. See [Encrypted storage](../../storage/encrypted-storage).</ArgTableRow>
<ArgTableRow arg="encryption-key" typ="string" syscap="storage">The key used to decrypt the `crypted` device. See [Encrypted storage](../../storage/encrypted-storage).</ArgTableRow>
<ArgTableRow arg="self-encryption-password" typ="string" syscap="storage">Password that enables TCG-Opal self-encryption on a supported (SED) drive; unsetting it disables self-encryption. See [Self-encrypting drives](../../storage/self-encrypting-drives).</ArgTableRow>
<ArgTableRow arg="sshfs-address" typ="string">Address (IP address or hostname) of the SSH server to mount, for `type=sshfs`. See [SSHFS](../../storage/sshfs).</ArgTableRow>
<ArgTableRow arg="sshfs-port" typ="num">Port of the SSH server to connect to, for `type=sshfs` (default: 22). See [SSHFS](../../storage/sshfs).</ArgTableRow>
<ArgTableRow arg="sshfs-user" typ="string">User to log in to the remote SSH server with, for `type=sshfs`. See [SSHFS](../../storage/sshfs).</ArgTableRow>
<ArgTableRow arg="sshfs-password" typ="string">Password of the remote SSH user, for `type=sshfs`. See [SSHFS](../../storage/sshfs).</ArgTableRow>
<ArgTableRow arg="sshfs-path" typ="string">Path on the remote SSH server to mount, for `type=sshfs`. See [SSHFS](../../storage/sshfs).</ArgTableRow>
<ArgTableRow arg="swap" typ="bool">Use the device as swap space. Swap is used only by containers, and its usable size is limited to 10 times the device's RAM. It applies to a whole disk or partition, or to a file with `type=file`. See [Disks](../../hardware/disks/).</ArgTableRow>
<ArgTableRow arg="file-path" typ="file">Path and name of the file mounted as a block device with `type=file`, for example a swap file (`swap=yes`) or a mounted `.iso` / `.squashfs` image. Removing the disk item does not delete the file. See [Disks](../../hardware/disks/).</ArgTableRow>
<ArgTableRow arg="file-size" typ="num">Size of the file, for example `file-size=1G`, when creating a `type=file` device.</ArgTableRow>
<ArgTableRow arg="file-offset" typ="num">Offset in the file at which the block device starts, for example `file-offset=0`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="slot-default" typ="string">Default slot name of the device, shown when no custom `slot` name is set.</ArgTableRow>
<ArgTableRow arg="fs-label" typ="string">Label of the file system. Formatting sets it automatically to `<slot>-fs`, unless a `label` is given to `/disk format`.</ArgTableRow>
<ArgTableRow arg="fs-uuid" typ="string">UUID of the file system, for example `58470fe2-...`.</ArgTableRow>
<ArgTableRow arg="fs" typ="enum (fat32 | ext4 | btrfs | xfs | nfs | smb | wipe | wipe-quick | tmpfs | exfat | ntfs | sshfs | squashfs | iso | discard | discard-secure | -)">File system of the device: `ext4`, `btrfs`, `xfs`, `fat32`, `exfat` and `ntfs` for local file systems, `tmpfs` for RAM folders, `nfs`, `smb` and `sshfs` for network mounts, and `iso` / `squashfs` for mounted images. `-` means the device has no recognised file system. The values `wipe`, `wipe-quick`, `discard` and `discard-secure` correspond to the file systems of `/disk format`.</ArgTableRow>
<ArgTableRow arg="model" typ="string">Model name of the device, for example `TS1TUTE210T`.</ArgTableRow>
<ArgTableRow arg="serial" typ="string">Serial number of the device.</ArgTableRow>
<ArgTableRow arg="fw-version" typ="string">Firmware version of the device.</ArgTableRow>
<ArgTableRow arg="size" typ="num">Total size of the device in bytes.</ArgTableRow>
<ArgTableRow arg="free" typ="num">Free space on the mounted file system in bytes.</ArgTableRow>
<ArgTableRow arg="total-inodes" typ="num">Total number of inodes of the file system.</ArgTableRow>
<ArgTableRow arg="free-inodes" typ="num">Number of free inodes of the file system.</ArgTableRow>
<ArgTableRow arg="use" typ="num">Used space of the file system in percent, for example `4%`.</ArgTableRow>
<ArgTableRow arg="mount-point" typ="string">Mount point of the file system, the folder under which it appears in `/file`, driven by `mount-point-template`.</ArgTableRow>
<ArgTableRow arg="sector-size" typ="num">Sector size of the device, for example 512 bytes.</ArgTableRow>
<ArgTableRow arg="interface" typ="string">Interface the device is connected to, for example `PCIe 2x8 GT/s` or `USB 2.00 480Mbps`.</ArgTableRow>
<ArgTableRow arg="interface-speed" typ="num">Speed of the interface the device is connected to, for example `15.7Gbps`.</ArgTableRow>
<ArgTableRow arg="raid-member-state" typ="string" syscap="storage">State of the disk as a member of its RAID array, for example `0:in_sync`; when the disk is not part of an assembled array, the details of the RAID superblock found on it are shown instead.</ArgTableRow>
<ArgTableRow arg="state" typ="string">State of a RAID array, for example `clean`.</ArgTableRow>
<ArgTableRow arg="last-seen" typ="string">Model and serial number of the disk that last occupied this slot, shown after the disk was ejected or removed, for example `TS1TUTE210T J398770033`.</ArgTableRow>
<ArgTableRow arg="raid-uuid" typ="string" syscap="storage">UUID of the RAID array.</ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-secret" typ="string" syscap="storage">Secret the NVMe-over-TCP server uses to authenticate connections from initiators.</ArgTableRow>
<ArgTableRow arg="nvme-tcp-secret" typ="string" syscap="storage">Secret used to authenticate the connection to the NVMe-over-TCP server.</ArgTableRow>
<ArgTableRow arg="sshfs-local-user" typ="string">Local RouterOS user the SSHFS mount runs under, for example `admin`. Read-only.</ArgTableRow>
<ArgTableRow arg="io-ops" typ="num">Total number of I/O operations on the device, as shown by [`monitor-traffic`](monitor-traffic).</ArgTableRow>
<ArgTableRow arg="io-errors" typ="num">Total number of I/O errors on the device.</ArgTableRow>
<ArgTableRow arg="read-ops" typ="num">Total number of read operations.</ArgTableRow>
<ArgTableRow arg="read-ops-per-second" typ="num">Number of read operations per second.</ArgTableRow>
<ArgTableRow arg="read-bytes" typ="num">Total number of bytes read.</ArgTableRow>
<ArgTableRow arg="read-rate" typ="num">Rate of reads, for example in bytes per second.</ArgTableRow>
<ArgTableRow arg="read-merges" typ="num">Number of adjacent read operations merged.</ArgTableRow>
<ArgTableRow arg="read-time" typ="time">Time spent on read operations.</ArgTableRow>
<ArgTableRow arg="write-ops" typ="num">Total number of write operations.</ArgTableRow>
<ArgTableRow arg="write-ops-per-second" typ="num">Number of write operations per second.</ArgTableRow>
<ArgTableRow arg="write-bytes" typ="num">Total number of bytes written.</ArgTableRow>
<ArgTableRow arg="write-rate" typ="num">Rate of writes, for example in bytes per second.</ArgTableRow>
<ArgTableRow arg="write-merges" typ="num">Number of adjacent write operations merged.</ArgTableRow>
<ArgTableRow arg="write-time" typ="time">Time spent on write operations.</ArgTableRow>
<ArgTableRow arg="in-flight-ops" typ="num">Number of I/O operations currently in flight.</ArgTableRow>
<ArgTableRow arg="active-time" typ="time">Time the device was busy handling requests.</ArgTableRow>
<ArgTableRow arg="wait-time" typ="time">Time requests spent waiting in the queue.</ArgTableRow>
<ArgTableRow arg="discard-ops" typ="num">Total number of discard (trim) operations.</ArgTableRow>
<ArgTableRow arg="discard-bytes" typ="num">Total number of bytes discarded.</ArgTableRow>
<ArgTableRow arg="discard-merges" typ="num">Number of adjacent discard operations merged.</ArgTableRow>
<ArgTableRow arg="discard-time" typ="time">Time spent on discard operations.</ArgTableRow>
<ArgTableRow arg="flush-ops" typ="num">Total number of flush operations.</ArgTableRow>
<ArgTableRow arg="flush-time" typ="time">Time spent on flush operations.</ArgTableRow>
<ArgTableRow arg="temperature" typ="num">Temperature of the drive in Celsius, reported by S.M.A.R.T. (storage package). See the [S.M.A.R.T. info](../../hardware/disks/smart) guide and [`smart-info`](smart-info).</ArgTableRow>
<ArgTableRow arg="temperatures" typ="multi { array-id, slot: num
 }">Temperatures of the drive's sensors in Celsius, one entry per sensor slot.</ArgTableRow>
<ArgTableRow arg="critical-warning" typ="ubit (spare-space, temperature, reliability-degraded, read-only, volatile-backup-failed)">Bitmask of critical warnings the drive reports: `spare-space` (available spare is below `available-spare-threshold`), `temperature` (temperature out of range), `reliability-degraded`, `read-only` (the device entered read-only mode) and `volatile-backup-failed`.</ArgTableRow>
<ArgTableRow arg="available-spare" typ="num">Remaining spare blocks of the drive in percent, for example 100%. Below `available-spare-threshold` the drive reports a warning.</ArgTableRow>
<ArgTableRow arg="available-spare-threshold" typ="num">Threshold in percent below which the available spare space of the drive is reported as a warning.</ArgTableRow>
<ArgTableRow arg="percentage-used" typ="num">Estimated percentage of the drive's life used, based on how many spare blocks have been consumed.</ArgTableRow>
<ArgTableRow arg="host-read-bytes" typ="num">Total number of bytes read by the host from the drive.</ArgTableRow>
<ArgTableRow arg="host-write-bytes" typ="num">Total number of bytes written by the host to the drive.</ArgTableRow>
<ArgTableRow arg="host-read-cmds" typ="num">Total number of read commands the host sent to the drive.</ArgTableRow>
<ArgTableRow arg="host-write-cmds" typ="num">Total number of write commands the host sent to the drive.</ArgTableRow>
<ArgTableRow arg="controller-busy-time" typ="time">Total time the drive controller was busy with commands.</ArgTableRow>
<ArgTableRow arg="power-cycles" typ="num">Number of power cycles of the drive.</ArgTableRow>
<ArgTableRow arg="power-on-time" typ="time">Total time the drive was powered on.</ArgTableRow>
<ArgTableRow arg="unsafe-shutdowns" typ="num">Number of unsafe (unexpected) shutdowns of the drive.</ArgTableRow>
<ArgTableRow arg="unrecovered-integrity-errors" typ="num">Number of unrecovered media and data integrity errors of the drive.</ArgTableRow>
<ArgTableRow arg="warning-temperature" typ="num">Temperature in Celsius at which the drive starts reporting a warning.</ArgTableRow>
<ArgTableRow arg="warning-temperature-time" typ="time">Time the drive spent above `warning-temperature`.</ArgTableRow>
<ArgTableRow arg="critical-temperature" typ="num">Temperature in Celsius at which the drive reports a critical condition.</ArgTableRow>
<ArgTableRow arg="critical-temperature-time" typ="time">Time the drive spent above `critical-temperature`.</ArgTableRow>
</ArgTable>
