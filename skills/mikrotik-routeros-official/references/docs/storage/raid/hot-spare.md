# Set a hot spare disk

> This page explains how to configure a hot spare disk for a RAID array in RouterOS, enabling automatic rebuild on disk failure by assigning a spare disk to the RAID setup.

# Set a hot spare disk

A hot spare is a disk that waits in the array for a member to fail. When a member fails, the rebuild starts on the spare at once. The spare is a member of the array with `raid-role=spare`.

Add the RAID array with the desired number of disks:

```ros
/disk/add raid-device-count=4 raid-type=5 type=raid slot=raid5
```

Add the disks and the spare to the array. In this example, `nvme5` is the spare:

```ros
/disk/set raid-master=raid5 raid-role=0 nvme1
/disk/set raid-master=raid5 raid-role=1 nvme2
/disk/set raid-master=raid5 raid-role=2 nvme3
/disk/set raid-master=raid5 raid-role=3 nvme4

/disk/set raid-master=raid5 raid-role=spare nvme5
```

When a member fails, the spare takes its `raid-role`, and the failed disk gets the `f` (`raid-member-failed`) flag and the role `spare`. During the rebuild, `state` of the array shows its progress, for example `degraded by 1, clean, sync:recover, recovery = 97.4%`, and `clean` when it is done. To put a new disk in place of the failed one, see [Replace a failed disk](./index.md#replace-a-failed-disk).
