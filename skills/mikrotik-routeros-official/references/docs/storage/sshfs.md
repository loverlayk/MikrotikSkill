# SSHFS

> SSHFS allows mounting a folder from a remote SSH server as a local disk in RouterOS, using the sshfs type of /disk. The mount is configured with the remote address, user credentials, and path, and appears in /file...

# SSHFS

SSHFS (SSH Filesystem) mounts a remote folder over SSH as a local disk on the router. It is configured with `/disk/add type=sshfs`, and the remote directory then appears under `/file` like other mounted storage, so files can be browsed and copied locally. SSHFS is part of the base system; the [Storage](./index.md) package is not needed. The remote side can be any SSH server with SFTP, including another RouterOS device.

RouterOS tracks each sshfs item under `/disk` with the slot automatically derived from the address and path, for example `sshfs-192-168-88-1--srv-files` for address `192.168.88.1` and path `/srv/files`, and it exposes the mount as `sshfs://<user>@<address>:<port>//<path>`.

## Configuration example

```routeros
/disk/add type=sshfs sshfs-address=192.168.88.1 sshfs-port=22 \
    sshfs-user=user sshfs-password=superSecret sshfs-path=/srv/files
```

After the item is added, the router connects in the background. While it connects, `state` in `/disk/print detail` is `mounting`; if the connection fails, `state` shows the error, for example `state="connectHandler: Host is unreachable"`. A mounted item has the `M` flag:

```text
Flags: M - MOUNTED
Columns: SLOT, FS, MOUNT-POINT
 #   SLOT                              FS     MOUNT-POINT                     
11 M sshfs-10-99-0-2--BackupBtrfsDisk  sshfs  sshfs-10-99-0-2--BackupBtrfsDisk
12   sshfs-10-99-0-9--srv-files        sshfs                                  
```

Once mounted, the remote folder shows up as a directory in `/file` under the mount point (`/file/print`).

The entry can be adjusted with `/disk/set`, for example to change the port:

```routeros
/disk/set [find where type=sshfs] sshfs-port=2222
```

Remove the mount with `/disk/remove <slot>`.

Authentication uses the user/password of the remote SSH server (`sshfs-user` / `sshfs-password`). `sshfs-local-user` is read-only on the router and indicates the local RouterOS user the mount runs under (for example `admin`).
