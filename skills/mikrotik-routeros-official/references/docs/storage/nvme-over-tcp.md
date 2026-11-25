# NVMe over TCP

> NVMe over TCP enables network-attached NVMe storage access for both initiators and targets, with configurable IP addresses, ports, and host-based access control. Examples show mounting a disk from a RouterOS client...

# NVMe over TCP

:::info
This feature requires the `rose-storage` package; see [Storage](./index.md).
:::

NVMe over TCP allows accessing storage over the network as an NVMe block device on the initiator (client) side. On the target (host) side the device can be an HDD/SSD/NVMe drive, a file, or a RAID array.

On the target, `nvme-tcp-server-port` (default `4420`) sets the TCP port, and `nvme-tcp-server-nqn` shows the NQN of the export, by default `nqn.2000-02.com.mikrotik:<slot>`. On the client, `nvme-tcp-address`, `nvme-tcp-port` and `nvme-tcp-nqn` select the export. The remote disk appears on a RouterOS client as `nvme-tcp1`, `nvme-tcp2` and so on, with `state="live"` when it is connected.

## Examples

### Mount a disk

In this example, one RouterOS device is used as a storage server (**Host**) and another RouterOS device mounts the storage over the network (**Client**).

1. On the **Host**, export the disk:

   ```routeros
   /disk/set disk1 nvme-tcp-export=yes
   ```

2. On the **Client**, add the remote disk. `/disk/nvme-discover 192.168.1.1` lists the NQNs that the host exports:

   ```routeros
   /disk/add type=nvme-tcp nvme-tcp-address=192.168.1.1 \
       nvme-tcp-nqn=nqn.2000-02.com.mikrotik:disk1
   ```

3. The **Client** now has a disk, `nvme-tcp1`, that is mounted over the network using NVMe over TCP.

#### Linux client

Use these commands to set up NVMe over TCP on a Linux **Client** (nvme-cli).

1. Load the kernel module:

   ```bash
   modprobe nvme_tcp
   ```

2. Discover the exports of the host. In this output, the host exports a file disk called `file2`:

   ```bash
   nvme discover -t tcp -a 192.168.1.1 -s 4420
   ```

   ```text
   Discovery Log Number of Records 1, Generation counter 5
   =====Discovery Log Entry 0======
   trtype:  tcp
   adrfam:  ipv4
   subtype: nvme subsystem
   treq:    not specified, sq flow control disable supported
   portid:  4420
   trsvcid: 4420
   subnqn:  nqn.2000-02.com.mikrotik:file2
   traddr:  10.0.2.15
   eflags:  none
   sectype: none
   ```

3. Connect to an export:

   ```bash
   nvme connect -t tcp -a 192.168.1.1 -s 4420 -n nqn.2000-02.com.mikrotik:disk1
   ```

4. A new NVMe block device is now available, for example `/dev/nvme0n1`; the number depends on the NVMe devices that the client already has:

   ```bash
   ls /dev/nvme*
   ```

5. You can now use the block device like any other block device on your Linux **Client**.

To disconnect the block device:

```bash
nvme disconnect -n nqn.2000-02.com.mikrotik:disk1
```

### Mount a file as a block device

In this example, one RouterOS device is used as a storage server (**Host**) and another RouterOS device mounts the storage over the network (**Client**).

:::note
A file lets you give the **Client** a part of a disk instead of the whole disk. Mounting a file has lower performance than mounting a disk (or partition) using NVMe over TCP.
:::

1. On the **Host**, create a file that is used as a block device, and export it:

   ```routeros
   /disk/add type=file file-path=disk1/BIGFILE.img file-size=10G \
       slot=blockdevice1
   /disk/set blockdevice1 nvme-tcp-export=yes
   ```

2. On the **Client**, add the remote disk and format it:

   ```routeros
   /disk/nvme-discover 192.168.1.1
   /disk/add type=nvme-tcp nvme-tcp-address=192.168.1.1 \
       nvme-tcp-nqn=nqn.2000-02.com.mikrotik:blockdevice1
   /disk/format nvme-tcp1 file-system=ext4
   ```

3. The **Client** now has a new disk, `nvme-tcp1`, even though on the **Host** the storage device is a file.

:::tip
To mount the block device on a Linux **Client**, see the [Linux client](#linux-client) section.
:::

### Mount a RAID array

In this example, the **Host** exports a [RAID](./raid/) array, so the **Client** gets a single disk with data redundancy.

1. Set up a RAID array on the **Host** and export it, for example:

   ```routeros
   /disk/add type=raid slot=RAID6_array raid-type=6 raid-device-count=8
   /disk/set disk1 raid-master=RAID6_array raid-role=0
   /disk/set disk2 raid-master=RAID6_array raid-role=1
   /disk/set disk3 raid-master=RAID6_array raid-role=2
   /disk/set disk4 raid-master=RAID6_array raid-role=3
   /disk/set disk5 raid-master=RAID6_array raid-role=4
   /disk/set disk6 raid-master=RAID6_array raid-role=5
   /disk/set disk7 raid-master=RAID6_array raid-role=6
   /disk/set disk8 raid-master=RAID6_array raid-role=7
   /disk/set RAID6_array nvme-tcp-export=yes
   ```

2. On the **Client**, add the remote disk:

   ```routeros
   /disk/add type=nvme-tcp nvme-tcp-address=192.168.1.1 \
       nvme-tcp-nqn=nqn.2000-02.com.mikrotik:RAID6_array
   ```

3. The **Client** now sees a single disk that is a RAID array on the **Host**.

:::tip
To mount the block device on a Linux **Client**, see the [Linux client](#linux-client) section.
:::

:::danger
Do not mount multiple disks from different RouterOS devices on a Linux Client and put them into a software RAID configuration (for example, mdadm). While this type of configuration does provide some redundancy, you can expect abnormal latency issues or even timeouts. Create a RAID array on your RouterOS device instead and export the RAID array as a block device to your Linux Client.
:::

## Limit access to an export

`nvme-tcp-server-allow-host-name` on the exported disk limits it to clients with that host name. A client sends its host name in `nvme-tcp-host-name`, by default `MikroTik`:

```routeros
# On the host:
/disk/set disk1 nvme-tcp-server-allow-host-name=backup-client
# On the client:
/disk/set nvme-tcp1 nvme-tcp-host-name=backup-client
```

A client with another host name cannot use the disk; its `state` shows `I/O error`. For authentication with a secret, see `nvme-tcp-server-password` and `nvme-tcp-server-secret` in the [`/disk`](../cli-reference/disk/disk.md) reference.
