# iSCSI

> iSCSI enables IP-based storage access with RouterOS supporting both target and initiator modes, featuring properties like iscsi-address, IQN identifiers, and configurable ports for both client and server roles.

# iSCSI

:::info
This feature requires the `rose-storage` package; see [Storage](./index.md).
:::

iSCSI gives access to block storage over an IP network: the initiator (client) sees the remote device as a local disk. RouterOS works as both. As a target, it exports a disk or a file disk (`iscsi-export=yes`); as an initiator, it adds a remote target as a new disk.

On the target, `iscsi-server-port` (default `3260`) sets the TCP port, and `iscsi-server-iqn` shows the IQN of the export, by default `iqn.2000-02.com.mikrotik:<slot>`. On the initiator, `iscsi-address`, `iscsi-port` and `iscsi-iqn` select the target.

## Configuration example

On the target, export a disk:

```routeros
/disk/set pcie1 iscsi-export=yes
```

A file can be exported as well. Create a file disk on a mounted disk and export it:

```routeros
/disk/add type=file file-path=pcie1/iscsi.img file-size=200M slot=file1
/disk/set file1 iscsi-export=yes
```

The export of `file1` has the IQN `iqn.2000-02.com.mikrotik:file1` (`/disk/print detail where slot=file1`).

On a RouterOS initiator, add a disk of `type=iscsi` with the target's address and IQN:

```routeros
/disk/add type=iscsi iscsi-address=192.168.1.1 \
    iscsi-iqn=iqn.2000-02.com.mikrotik:file1
```

The remote disk appears in `/disk/print` as `iscsi1` with `state="connected"`, and can be formatted and used like a local disk.

On a Linux initiator (open-iscsi), discover the targets and log in:

```bash
iscsiadm -m discovery -t sendtargets -p 192.168.1.1
iscsiadm -m node -T iqn.2000-02.com.mikrotik:file1 -p 192.168.1.1 --login
```
