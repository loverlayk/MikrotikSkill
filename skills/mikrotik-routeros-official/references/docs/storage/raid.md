# RAID

> RAID technology in RouterOS enables data storage across multiple drives with improved performance and protection, supporting RAID levels 0,1,4,5,6, linear, and nested configurations. Includes configuration examples...

# RAID

:::info
This feature requires the `rose-storage` package; see [Storage](../index.md).
:::

RAID (Redundant Array of Independent Disks) stores data on multiple drives and combines them into one logical disk, for better performance, better protection against disk failures, or both.

RouterOS supports software RAID levels 0, 1, 4, 5, 6, linear, and nested RAID (a RAID array made of other RAID arrays). When a member of a redundant array fails, the array keeps working in a degraded state. With a [hot spare](./hot-spare.md), the rebuild starts on the spare at once; otherwise, [replace the failed disk](#replace-a-failed-disk).

<DocCardList />

## Create a RAID 6 array

The same procedure applies to the other RAID types. This example creates a RAID 6 array of six disks, `nvme1` to `nvme6`. All data on the disks is lost.

Create the RAID block device:

```routeros
/disk/add type=raid slot=raid6 raid-type=6 raid-device-count=6
```

Add the disks to the array. `raid-role` is the position of each disk in the array, starting from 0:

```routeros
/disk/set nvme1 raid-master=raid6 raid-role=0
/disk/set nvme2 raid-master=raid6 raid-role=1
/disk/set nvme3 raid-master=raid6 raid-role=2
/disk/set nvme4 raid-master=raid6 raid-role=3
/disk/set nvme5 raid-master=raid6 raid-role=4
/disk/set nvme6 raid-master=raid6 raid-role=5
```

Format the RAID block device:

```routeros
/disk/format raid6 file-system=ext4
```

Check the array with `/disk/print detail where slot=raid6`:

```text
7 BM type=raid slot="raid6" slot-default="" parent="" fs-label="raid6-fs"
     fs-uuid="3ffda391-66ff-40f1-8837-e716898d8a45" fs=ext4
     model="RAID6 2-parity-disks" size=8 585 740 288 free=8 346 079 232
     total-inodes=524 288 free-inodes=524 277 use=0% mount-point="raid6"
     mount-filesystem=yes mount-read-only=no compress=no sector-size=512
     raid-type=6 raid-device-count=6 raid-max-component-size=none
     raid-chunk-size=1M raid-master=none state="active"
     raid-uuid="9aea18da-07061d4e-fbd0175e-7ab46c87" nvme-tcp-export=no
     iscsi-export=no nfs-sharing=no smb-sharing=no media-sharing=no
     media-interface=none swap=no
```

`state` shows the condition of the array, for example `active` or `clean`, `degraded by 1` when a member is missing, and the progress of a rebuild (`sync:recover, recovery = 76.6%`).

:::warning
Avoid using multiple partitions on a single physical disk in multiple RAID arrays. Using the same physical disk in multiple RAID arrays can result in low performance.
:::

## Replace a failed disk

A failed member has the `f` (`raid-member-failed`) flag in `/disk/print`. To replace a member that has not failed, for example a disk that reports errors, mark it as failed first:

```routeros
/disk/set nvme3 raid-member-failed=yes
```

Remove the failed disk from the array, and add the new disk with the same `raid-role`:

```routeros
/disk/set nvme3 raid-master=none
/disk/set nvme7 raid-master=raid6 raid-role=2
```

The rebuild starts at once; `state` shows its progress and returns to `clean` when it is done. A role that a failed disk still holds cannot be given to another disk: `failure: already have device with raid-role=2 in this raid`.

## Monitor the array

Monitor the array for failures. This script checks every 30 seconds for members with the `raid-member-failed` flag, writes `ERROR: RAID has failed!` to the log and sends an e-mail:

```routeros
/system/scheduler
add interval=30s name=MRaidHealthCheckCall on-event=MraidHealthCheck policy=ftp,read,write,policy,test,sniff start-time=startup
/system/script
add dont-require-permissions=no name=MraidHealthCheck owner=admin policy=ftp,read,write,policy,test,sniff source=":global CheckRAID;\
    \n:local sysadmin; \
    \n\
    \n:set  \$sysadmin \"<servername@domain.tld>\";\
    \n\
    \n:local temp [/disk/print count-only where raid-member-failed];\
    \n:if ( \$temp > 0 ) do={\
    \n   :if ( \$CheckRAID < 1 ) do={\
    \n      /log/info message=\"ERROR: RAID has failed!\";\
    \n      /tool/e-mail/send to= \$sysadmin subject=([/system/identity/get name].\" RAID failed\") body=(\"Go check it! Value: \".\$temp);\
    \n      :set \$CheckRAID 7;\
    \n      :delay 5s;\
    \n    }\
    \n   }       \
    \n   :if ( \$CheckRAID > 0 ) do={\
    \n      :set \$CheckRAID ( \$CheckRAID -1 );\
    \n   }\
    \n"
```

You will also need to configure your RouterOS device's e-mail server settings:

```routeros
/tool/e-mail
set from=<raidcheck@domain.tld> port=587 server=smtp.domain.com tls=starttls
```

:::warning

Make sure you configure your e-mail server's settings under `/tool/e-mail` and change the e-mail address in the script above with the values that match your e-mail server's settings.

:::

## RAID types

### RAID 0

All data is written evenly over all disks in this RAID, this configuration does not provide any fault tolerance but provides best performance.

![RAID 0 diagram: data striped across disks](./img/raid-01.webp)

### RAID 1

The same data is written to all drives (data is mirrored), this configuration provides best fault tolerance, but performance-wise write speeds will be equal to the slowest disk used in the array.

![RAID 1 diagram: data mirrored between disks](./img/raid-02.webp)

### RAID 4

Block-level data is striped across data disks, with parity bits stored on a dedicated disk. Performance will be limited to the parity writing speed.

![RAID 4 diagram: block-level striping with dedicated parity disk](./img/raid-03.webp)

### RAID 5

Block-level data is striped evenly over the available disks. It can be recovered from 1 disk failure.

![RAID 5 diagram: block-level striping with distributed parity](./img/raid-04.webp)

### RAID 6

Block-level data is striped evenly over the available disks. It can be recovered from 2 disk failures.

![RAID 6 diagram: block-level striping with double distributed parity](./img/raid-05.webp)

### RAID linear

Data is appended over multiple disks combining them into a single large disk. Provides no redundancy and is limited to the single disk read/write speed.

![RAID linear diagram: data appended across disks](./img/raid-06.webp)

### Nested RAID

Combination of multiple RAID configurations into another RAID. For example RAID 10 (RAID 1+0) combines disk mirroring (RAID 1) and disk striping (RAID 0)

![Nested RAID diagram: RAID 1+0 combining mirroring and striping](./img/raid-07.webp)

### Create a nested RAID 10 array

RAID 10 is a RAID 0 array made of RAID 1 arrays. This example uses four disks, `nvme1` to `nvme4`, in two mirrors.

Create the RAID 0 array, and the two RAID 1 arrays as its members:

```routeros
/disk/add type=raid slot=raid10 raid-type=0 raid-device-count=2
/disk/add type=raid slot=mirror1 raid-type=1 raid-device-count=2 \
    raid-master=raid10 raid-role=0
/disk/add type=raid slot=mirror2 raid-type=1 raid-device-count=2 \
    raid-master=raid10 raid-role=1
```

Add the disks to the mirrors:

```routeros
/disk/set nvme1 raid-master=mirror1 raid-role=0
/disk/set nvme2 raid-master=mirror1 raid-role=1
/disk/set nvme3 raid-master=mirror2 raid-role=0
/disk/set nvme4 raid-master=mirror2 raid-role=1
```

Format the RAID 10 array:

```routeros
/disk/format raid10 file-system=ext4
```

The array has the size of two disks (`/disk/print detail where slot=raid10`):

```text
6 BM type=raid slot="raid10" slot-default="" parent="" fs-label="raid10-fs"
     fs-uuid="9efc2ffb-bd5e-4020-bf9d-0fdd23cf1147" fs=ext4
     model="RAID0 striped" size=4 290 772 992 free=4 139 458 560
     total-inodes=262 144 free-inodes=262 133 use=0% mount-point="raid10"
     mount-filesystem=yes mount-read-only=no compress=no sector-size=512
     raid-type=0 raid-device-count=2 raid-max-component-size=none
     raid-chunk-size=1M raid-master=none state="clean"
     raid-uuid="04cbbdec-baab5216-8ad762b2-2b74d214" nvme-tcp-export=no
     iscsi-export=no nfs-sharing=no smb-sharing=no media-sharing=no
     media-interface=none swap=no
```

For more disks, add more mirrors to the RAID 0 array. Other nested RAID types are built in the same way.
