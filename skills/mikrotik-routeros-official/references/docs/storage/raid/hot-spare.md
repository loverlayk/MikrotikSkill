# Setting a hot spare disk

> This page explains how to configure a hot spare disk for a RAID array in RouterOS, enabling automatic rebuild on disk failure by assigning a spare disk to the RAID setup.

# Setting a hot spare disk

It's possible to assign a hot spare disk for your RAID array. In case of a disk failure - the rebuild immediately begins on the assigned spare disk. The spare is a member of the array configured with `raid-role=spare` on it.

Add the RAID array with the desired number of disks:

```ros
/disk/add raid-device-count=4 raid-type=5 type=raid slot=raid5
```

Then add the disks, as well as the spare, to the RAID. In this case we will add `nvme5` as the spare:

```ros
/disk/set raid-master=raid5 raid-role=0 nvme1
/disk/set raid-master=raid5 raid-role=1 nvme2
/disk/set raid-master=raid5 raid-role=2 nvme3
/disk/set raid-master=raid5 raid-role=3 nvme4

/disk/set raid-master=raid5 raid-role=spare nvme5
```
