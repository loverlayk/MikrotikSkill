# iSCSI

> iSCSI enables IP-based storage access with RouterOS supporting both target and initiator modes, featuring properties like iscsi-address, IQN identifiers, and configurable ports for both client and server roles.

# iSCSI

:::info
This feature requires the [Storage](./index.md) package.
:::

iSCSI allows accessing storage over an IP-based network. On the initiator (client) the iSCSI device appears as a local block device. RouterOS supports both target and initiator modes: the target exports a disk or a file (`iscsi-export=yes` on the host device), and the initiator mounts a remote target over the network as a new device.

The iSCSI server listens on TCP port 3260 by default. The IQN identifier the server presents is by default formed as `iqn.2000-02.com.mikrotik:<slot>`.

## Configuration example

Host: export the disk with:

```ros
/disk set pcie1-nvme1 iscsi-export=yes
```

Client: add a device with `type=iscsi` and point it at the server address and IQN:

```ros
/disk add type=iscsi iscsi-address=192.168.1.1 iscsi-iqn=iqn.2000-02.com.mikrotik:pcie1-nvme1
```

The mounted device then appears in `/disk/print` as a normal block device and can be formatted and used locally.
