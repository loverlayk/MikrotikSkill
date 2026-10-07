# NFS

> NFS enables network directory sharing in RouterOS using NFS v4, requiring the Storage package. It uses port TCP/2049 and is configured via the nfs-sharing, nfs-address and nfs-share arguments of /disk.

# NFS

:::info
This feature requires the [Storage](./index.md) package.
:::

NFS allows sharing local directories over a network. RouterOS currently supports NFS v4-only mode.

:::warning

NFS uses port TCP/2049. If the port is not available, in `/disk print detail` you will see the state stuck at `nfs-state="mounting"`.

:::

## Configuration example

Host: enable NFS sharing of a mounted disk.

```ros
/disk/set pcie1-nvme1 nfs-sharing=yes
```

Client: add a device of `type=nfs` that mounts the share.

```ros
/disk/add type=nfs nfs-address=192.168.1.1
```

Linux client:

```bash
mkdir /mnt/files
mount -t nfs 192.168.1.1:/ /mnt/files
```
