# Rsync

> Rsync in RouterOS allows efficient file synchronization between systems, with configurable local/remote paths and modes for upload/download. Dynamic IPsec entries are created when a password is set, ensuring secure...

# Rsync

:::info
This feature requires the `rose-storage` package; see [Storage](./index.md).
:::

`/file/sync` keeps a file or folder in sync with another RouterOS device. When a file changes, only the changes are transferred.

A sync entry on one router (the host) connects to the other router (the remote device) and logs in with `user` and `password`, like WinBox: it needs the remote device's WinBox [service](../system-information-and-utilities/services.md) port, TCP 8291, and a user on the remote device. The rsync daemon in `/file/rsync-daemon` is not needed for a sync between RouterOS devices. When a `password` is set, RouterOS also creates dynamic IPsec entries and encrypts the transfer.

:::warning
If the remote device's TCP port 8291 is not reachable, the status in `/file/sync/print` stays at `making control connection to <ip>`. With a password, the IPsec connection also needs UDP port 500 and IPsec ESP (protocol 50) between the devices.
:::

## Configuration example

Upload the file `BtrfsDisk/rs2.txt` to the `BackupBtrfsDisk` disk of the remote device 10.99.0.2, logging in as `syncuser`:

```routeros
/file/sync/add local-path=BtrfsDisk/rs2.txt mode=upload \
    remote-address=10.99.0.2 remote-path=BackupBtrfsDisk/ \
    user=syncuser password=<password>
```

When the file is transferred, the entry has the status `in sync` on the host device (`/file/sync/print`):

```text
# REMOTE-ADDRESS  MODE    LOCAL-PATH         REMOTE-PATH       STATUS 
2 10.99.0.2       upload  BtrfsDisk/rs2.txt  BackupBtrfsDisk/  in sync
```

The remote device shows a dynamic entry in the opposite direction:

```text
#   REMOTE-ADDRESS  MODE      LOCAL-PATH                REMOTE-PATH       
1 D 10.99.0.1       download  BackupBtrfsDisk/          BtrfsDisk/rs2.txt 
```

### IPsec dynamic entries

With a password, both devices get a dynamic IPsec peer and policy named `file-sync-<address of the other device>` (`/ip/ipsec/policy/print where dynamic` on the host):

```text
Flags: D - DYNAMIC, A - ACTIVE
Columns: PEER, TUNNEL, SRC-ADDRESS, DST-ADDRESS, PROTOCOL, ACTION, LEVEL
#   PEER                 TU  SRC-ADDRESS   DST-ADDRESS   PRO  ACTION   LEVEL  
;;; file-sync-10.99.0.2
0 D file-sync-10.99.0.2  no  10.99.0.1/32  10.99.0.2/32  tcp  encrypt  require
```
