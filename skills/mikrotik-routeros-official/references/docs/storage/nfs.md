# NFS

> NFS enables network directory sharing in RouterOS using NFS v4, requiring the Storage package. It uses port TCP/2049 and is configured via the nfs-sharing, nfs-address and nfs-share arguments of /disk.

# NFS

:::info
This feature requires the `rose-storage` package; see [Storage](./index.md).
:::

NFS shares the router's disks over the network, and mounts NFS shares of other devices as disks. The RouterOS NFS server supports NFS version 4 only; clients that use version 3 cannot mount it.

:::warning
NFS uses TCP port 2049. If the port is not reachable, the NFS disk on the client is not mounted, and `state` in `/disk/print detail` shows the error, for example `state="Connection refused"`.
:::

## Configuration example

On the host, enable NFS sharing of a mounted disk:

```routeros
/disk/set pcie1 nfs-sharing=yes
```

The host exports one tree, `/`, with a folder for each shared disk, named after the disk's mount point.

On a RouterOS client, add a disk of `type=nfs`. Without `nfs-share`, it mounts the whole tree, as the slot `nfs-<address>-`:

```routeros
/disk/add type=nfs nfs-address=192.168.1.1
```

With `nfs-share`, it mounts only the folder of one shared disk, as the slot `nfs-<address>-<share>`:

```routeros
/disk/add type=nfs nfs-address=192.168.1.1 nfs-share=pcie1
```

On a Linux client, mount the tree with NFS version 4:

```bash
mkdir /mnt/files
mount -t nfs4 192.168.1.1:/ /mnt/files
```
