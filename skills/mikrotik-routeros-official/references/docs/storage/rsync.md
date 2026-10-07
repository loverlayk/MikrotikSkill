# Rsync

> Rsync in RouterOS allows efficient file synchronization between systems, with configurable local/remote paths and modes for upload/download. Dynamic IPsec entries are created when a password is set, ensuring secure...

# Rsync

:::info
This feature requires the [Storage](./index.md) package.
:::

`rsync` (Remote Sync) is a powerful file synchronization and file transfer program. It allows for efficient transfer and synchronization of files and directories between different systems or within the same system.

If you make changes in a file, only the changes are transferred, reducing data transfer volume. The RouterOS rsync implementation uses IPsec for data transfer when a password is set. When configured, you will see dynamic IPsec entries (see below).

Rsync sync entries can be found in the `/file/sync` menu, and the receiving router has to run the rsync daemon, enabled under `/file/rsync-daemon`.

:::warning

Port TCP/873 is used for the rsync control connection (if not open, `/file/sync/print` gets stuck at `making control connection to <ip>`).

Port UDP/500 and protocol 50 (ipsec-esp) are used to create a secure connection and start the transfer (if not open, `/file/sync/print` gets stuck at `initializing transfer`).

:::

## Configuration example

Basic configuration is easy: on the host device add the file you want to sync to another device, give the IP of the remote device, and the mode of the sync. The remote device must have the rsync daemon enabled:

```ros
# Remote device (receives the transfer):
/file/rsync-daemon/set enabled=yes
```

```ros
# Host device (initiates the sync):
/file/sync/add local-path=/ipv6route.txt.rsc mode=upload remote-address=192.168.88.2 remote-path=RAID/
```

If configured correctly, the entry shows `in sync` on the host device:

```ros
0 192.168.88.2  upload  /ipv6route.txt.rsc  RAID/        in sync
```

And on the remote device:

```ros
#   REMOTE-ADDRESS   MODE      LOCAL-PATH  REMOTE-PATH         STATUS 
0 D 192.168.88.1 download  RAID/       /ipv6route.txt.rsc  in sync
```

### IPsec dynamic entries

When rsync is configured with a password, it creates dynamic IPsec entries for the secure transfer:

```ros
#     PEER                     TUNNEL  SRC-ADDRESS       DST-ADDRESS       PROTOCOL  ACTION   LEVEL    PH2-COUNT
;;; file-sync-10.155.145.11
1  D  file-sync-10.155.145.11  no      10.155.145.17/32  10.155.145.11/32  tcp       encrypt  require          1

/ip/ipsec/peer print
 0  D  name="file-sync-10.155.145.11" address=10.155.145.11/32 local-address=10.155.145.17 profile=default exchange-mode=main send-initial-contact=yes
/ip/ipsec/identity print
 0 D  ;;; file-sync-10.155.145.11
      peer=file-sync-10.155.145.11 auth-method=pre-shared-key secret="secret" generate-policy=no
```
