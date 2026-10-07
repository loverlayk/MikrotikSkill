# Storage

> This page documents RouterOS storage features including disk encryption, RAID configurations, Btrfs/XFS filesystems, network protocols like iSCSI and NFS, media sharing via DLNA, file synchronization with rsync, and...

# Storage

This section covers RouterOS storage features: disk-level options (encryption, RAID, filesystems such as Btrfs), network storage protocols (iSCSI, NFS, SMB, NVMe over TCP), media sharing (DLNA), and file synchronization (rsync).

<DocCardList />

:::info

While regular drives are supported, for reliability purposes we recommend using drives that have Power Loss Protection (PLP).

:::

The **Storage package** (shown as `rose-storage` under `/system/package/print`) adds data-center functionality to RouterOS - disk monitoring with S.M.A.R.T., the Btrfs and XFS file systems, RAID, rsync, iSCSI, NVMe over TCP, NFS, and an SMB client. It is currently supported on **arm, arm64, x86** and **tile** platforms.

The built-in SMB **server** and DLNA media server are part of the base system and do not require the Storage package - see the [SMB](./smb) and [DLNA Media Server](./dlna) pages.
