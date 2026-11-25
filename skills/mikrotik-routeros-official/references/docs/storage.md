# Storage

> This page documents RouterOS storage features including disk encryption, RAID configurations, Btrfs/XFS filesystems, network protocols like iSCSI and NFS, media sharing via DLNA, file synchronization with rsync, and...

# Storage

This section covers RouterOS storage features: disk-level options (encryption, RAID, filesystems such as Btrfs), network storage protocols (iSCSI, NFS, SMB, NVMe over TCP), media sharing (DLNA), and file synchronization (rsync).

<DocCardList />

:::info

While regular drives are supported, for reliability purposes we recommend using drives that have Power Loss Protection (PLP).

:::

The **Storage package** (shown as `rose-storage` under `/system/package/print`) adds data-center functionality to RouterOS: disk monitoring with S.M.A.R.T., the Btrfs and XFS file systems, RAID, encrypted disks, file synchronization (`/file/sync`), iSCSI, NVMe over TCP, and NFS. It is available for the **arm, arm64, x86** and **tile** platforms.

The SMB server and client, SSHFS, and the DLNA media server are part of the base system and do not require the Storage package - see the [SMB](./smb), [SSHFS](./sshfs) and [DLNA Media Server](./dlna) pages.
