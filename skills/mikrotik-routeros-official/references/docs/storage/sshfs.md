# SSHFS

> SSHFS allows mounting a folder from a remote SSH server as a local disk in RouterOS, using the sshfs type of /disk. The mount is configured with the remote address, user credentials, and path, and appears in /file...

# SSHFS

SSHFS (SSH Filesystem) mounts a remote folder over SSH as a local disk on the router. It is configured with `/disk/add type=sshfs`, and the remote directory then appears under `/file` like other mounted storage, so files can be browsed and copied locally.

RouterOS tracks each sshfs item under `/disk` with the slot automatically derived from the address and path, for example `sshfs-192-168-88-1--srv-files` for address `192.168.88.1` and path `/srv/files`, and it exposes the mount as `sshfs://<user>@<address>:<port>//<path>`.

## Configuration example

```ros
/disk/add type=sshfs sshfs-address=192.168.88.1 sshfs-port=22 sshfs-user=user sshfs-password=superSecret sshfs-path=/srv/files
```

After the item is added, the router starts connecting in the background; while connecting (or as long as the remote side is unreachable) the item reports `state=mounting`:

```ros
[admin@MikroTik] > /disk/print where type=sshfs
Columns: SLOT, FS, MOUNT-POINT, STATE
#   SLOT                                FS     MOUNT-POINT  STATE
0   sshfs-192-168-88-1--srv-files  sshfs  sshfs-192-168-88-1--srv-files   mounting
```

Once mounted, the remote folder shows up as a directory in `/file` under the mount point (`/file/print`).

The entry can be adjusted with `/disk/set`, for example to change the port:

```ros
/disk/set [find where type=sshfs] sshfs-port=2222
```

Remove the mount with `/disk/remove <slot>`.

Authentication uses the user/password of the remote SSH server (`sshfs-user` / `sshfs-password`). `sshfs-local-user` is read-only on the router and indicates the local RouterOS user the mount runs under (for example `admin`).
