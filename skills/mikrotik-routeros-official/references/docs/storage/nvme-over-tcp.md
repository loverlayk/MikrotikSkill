# NVMe over TCP

> NVMe over TCP enables network-attached NVMe storage access for both initiators and targets, with configurable IP addresses, ports, and host-based access control. Examples show mounting a disk from a RouterOS client...

# NVMe over TCP

:::info
This feature requires the [Storage](./index.md) package.
:::

NVMe over TCP allows accessing storage over the network as an NVMe block device on the initiator (client) side. On the target (host) side the device can be an HDD/SSD/NVMe drive or even a RAID array.

The NVMe over TCP server listens on TCP port 4420 by default.

## Examples

### Mount a disk

In this example, one RouterOS device is used as a storage server ( **Host** ) and another RouterOS device requires a storage device to be mounted over the network ( **Client** ).

1. Use the following commands on **Host** :  

   ```ros
   /disk/set disk1 nvme-tcp-export=yes nvme-tcp-port=4420
   ```

2. Use the following commands on **Client** :  

   ```ros
   /disk/add type=nvme-tcp nvme-tcp-address=192.168.1.1 nvme-tcp-name=disk1
   ```

3. Your **Client**  will now see a disk that is actually mounted over network using NVMe over TCP.

#### Linux client

Use these commands to set up NVMe over TCP on a Linux **Client**.

1. Load kernel module.  

    ```bash
    modprobe nvme_tcp
    ```

2. Discover existing NVMe over TCP mounts.  

   ```bash
   nvme discover -t tcp -a 192.168.1.1 -s 4420
   ```

   ```routeros
   #OUTPUT:
   Discovery Log Number of Records 1, Generation counter 2
   =====Discovery Log Entry 0======
   trtype:  tcp
   adrfam:  ipv4
   subtype: nvme subsystem
   treq:    not specified, sq flow control disable supported
   portid:  4420
   trsvcid: 4420
   subnqn:  disk1
   traddr:  10.155.166.7
   sectype: none
   ```

3. Connect to the NVMe over TCP mount.  

   ```bash
   nvme connect -t tcp -a 192.168.1.1 -s 4420 -n disk1
   ```

4. Block devices now should be available.  

   ```bash
   ls /dev/nvme*
   ```

    ```bash
    #OUTPUT:
    /dev/nvme0  /dev/nvme0n1  /dev/nvme-fabrics
    ```

5. You can now use the mounted block device as any other block device on your Linux **Client**.

In case you want to disconnect the mounted block device:

```bash
nvme disconnect -d /dev/nvme0
```

### Mount a file as a block device

In this example, one RouterOS device is used as a storage server ( **Host** ) and another RouterOS device requires a storage device to be mounted over the network ( **Client** ).

:::warning

Such a setup is useful when you don't want to delegate the whole disk to a **Client** , but rather give a fraction of the disk size to the **Client** . Mounting a file rather than a disk is going to have lower performance than mounting a disk (or partition) using NVMe over TCP.

:::

1. Use the following commands on **Host**  to create a file that is going to be used as a block device:  

   ```routeros
   /disk/add type=file file-path=disk1/BIGFILE.img file-size=10G slot=blockdevice1
   /disk/set blockdevice1 nvme-tcp-export=yes 
   ```

2. Use the following commands on **Client** to mount the file as a block device:  

   ```routeros
   /disk/nvme-discover 192.168.1.1
   /disk/add nvme-tcp-address=192.168.1.1 nvme-tcp-name=blockdevice1 type=nvme-tcp
   /disk/format blockdevice1 file-system=ext4
   ```

3. Your **Client** will now see a new disk called `blockdevice1` even though on the **Server** the storage device is actually a file.

:::tip

In case you want to mount the block device on a Linux **Client**, then check the [Linux Client](#linux-client) section.

:::

### Mount a RAID array

In this example, one RouterOS device is used as a storage server ( **Host** ) and another RouterOS device requires a storage device to be mounted over the network ( **Client** ), but also provides data redundancy.

1. Set up a [RAID](./raid/) on the **Host**, for example:  

   ```routeros
   /disk/add raid-device-count=8 raid-type=6 slot=RAID6_array type=raid
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

2. Use the following commands on the **Client**:

    ```ros
    /disk/add type=nvme-tcp nvme-tcp-address=192.168.1.1 nvme-tcp-name=RAID6_array
    ```

3. Your **Client** will now see a single disk, but it is actually a highly redundant RAID array.

:::tip

In case you want to mount the block device on a Linux **Client**, then check the [Linux Client](#linux-client) section.

:::

:::danger

Do not mount multiple disks from different RouterOS devices on a Linux Client and put them into a software RAID configuration (for example, mdadm). While this type of configuration does provide some redundancy, you can expect abnormal latency issues or even timeouts. It is recommended to create a RAID array on your RouterOS and export the RAID array as a block device to your Linux Client.

:::
