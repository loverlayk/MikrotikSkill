# Btrfs maintenance

> This page covers Btrfs maintenance tasks including periodic scrubbing to detect and correct data corruption in RAID arrays, balancing to optimize storage space usage, and creating snapshots for data recovery. It...

# Btrfs maintenance

Similar to other feature-rich filesystems, Btrfs needs periodic maintenance. This page covers the routine tasks relevant to Btrfs.

## Periodic scrubbing

In a RAID array, your data is stored on multiple disks or multiple disks contain information how to reassemble the data. Without RAID your disks in rare events might corrupt a few bytes of your data and you might not even notice that the data has been corrupted. With RAID arrays your data is compared with other copies of data (or checked on assembly) when you read a file and will alert you that data is corrupted. With [regular RAID](../raid/) and, for example, in RAID1 configuration the RAID array is not able to tell which copy of the file is correct. It will only inform you that the data corruption has been detected. With Btrfs RAID you are not only able to detect the data corruption, but you are also able to distinguish which copy of the file is the correct one by using checksums and restore it automatically.

Scrubbing is a process that re-reads the whole RAID array and, in case of Btrfs RAID, corrects any data corruption. While Btrfs RAID will correct the data on file read operations, for example, you want to download a file from your RouterOS device, avoiding scrubbing is highly **NOT** recommended. In rare events it is possible that, for example, in RAID1 configuration both disks have corrupted data and Btrfs RAID might not be able to restore the data. To avoid such situations and protect valuable data, consider running scrubbing on a regular basis.

:::warning

Excessive detected data corruption usually indicates a failing storage device. Consider checking the storage device when you notice many data corruption warnings.

:::

The interval of how often to run scrubbing is going to depend on each use case. Scrubbing is an intensive task on your storage devices. It re-reads the whole RAID array and performs additional checks. During scrubbing you can experience a noticeable performance drop on the disks until the scrubbing has finished. If you are worried about the performance during scrubbing, consider running scrubbing less often. If you are more worried about data integrity, consider running scrubbing more often.

- Summary: Used to detect and correct data corruption
- Recommended interval: 1 week
- [Working example](./raid#creating-btrfs-raid-check)

Example command:

```routeros
/disk/btrfs/filesystem/print
/disk/btrfs/filesystem/scrub-start 0
```

You can also cancel scrubbing using the following command:

```routeros
/disk/btrfs/filesystem/scrub-cancel
```

## Periodic balance

In Btrfs data is stored in allocated chunks, which then allow storing your data in blocks. Over time due to various data activities, the chunks can become partially full and distributed between many chunks in a suboptimal way. Balancing a Btrfs file system means re-arranging the data in these chunks and restoring the unallocated space. As a result you can restore lost usable free space and performance of the Btrfs file system. This is somewhat similar to a defragmentation operation on other file systems.

An important parameter for balancing is the `data-usage` parameter. This is a filter that prevents the balancing function from processing chunks that are above a certain usage percentage. For example, `data-usage=50` will only process chunks that are 50% full or less. You can run the balancing command multiple times with different values and therefore reduce the amount of time each balancing operation requires. Balancing can be an intensive task depending on your free space available and how data has been written since last balancing action, and therefore you might benefit from running the balance command with different `data-usage` values separately to reduce the time window when balancing causes a performance drop due to intensive disk reads and writes.

In case you want to run balancing commands separately, you should use `data-usage` values of 25, 50, 75 and 90. It is not recommended to go above 90%. For most users running the balance command separately is not required and running it once per interval with `data-usage` of 50% is sufficient.

- Summary: Used to restore free space and improve performance.
- Recommended interval: twice a month.
- Recommended `data-usage`: 50.
- [Working example](./raid#creating-btrfs-raid-check).

Example command:

```routeros
/disk/btrfs/filesystem/print
/disk/btrfs/filesystem/balance-start data-usage=50 0
```

You can also cancel balance using the following command:

```routeros
/disk/btrfs/filesystem/balance-cancel
```

## Periodic snapshots

Snapshots can be used to save changes of your files at a set interval. Snapshots are most useful when you have a reliable interval at which data is copied so you can always revert your data to a previous state. Below you can find a ready-to-use script that creates periodic snapshots:

```routeros
/system/scheduler
add interval=1d name=BraidSnapshotStartCall on-event=BraidSnapshotStart policy=ftp,read,write,policy,test,sniff start-date=1970-01-01 start-time=23:15:00
add interval=1d name=BraidSnapshotCleanUpStartCall on-event=BraidSnapshotCleanUpStart policy=ftp,read,write,policy,test,sniff start-date=1970-01-01 start-time=23:00:00
add interval=3m name=SystemBackupStartCall on-event=SystemBackupStart policy=ftp,read,write,policy,test,sniff start-time=startup

/system/script
add dont-require-permissions=no name=SystemBackupStart owner=admin policy=ftp,read,write,policy,test,sniff source=":global systembackupstatuscheck;\
    \n:global systembackupdirectoryname; \
    \n:local sysadmin;\
    \n\
    \n:set \$sysadmin ( \$sysadmin \"servername@domain.tld\" );\
    \n:set \$systembackupdirectoryname (\$systembackupdirectoryname \"Braid17-20/@system-backup/\");\
    \n\
    \n if (\$systembackupstatuscheck != \"started\") do={\
    \n         :set \$systembackupstatuscheck (\$systembackupstatuscheck \"started\");\
    \n               :local datentime ([/system/clock/get date].\"-\".[/system/clock/get time]);\
    \n               :local servername ([/system/identity/get name]);\
    \n               /system/backup/save name=\"\$systembackupdirectoryname\$servername-\$datentime\";\
    \n\
    \n        :set \$systembackupstatuscheck (\$systembackupstatuscheck \"done\");\
    \n} else={\
    \n         /log/info message=\"ERROR: Cannot create  \$systembackupdirectoryname\$servername-\$datentime. Set manually :set systembackupstatuscheck (systembackupstatuscheck \\\"done\\\");\";\
    \n}\
    \n"
add dont-require-permissions=no name=BraidSnapshotStart owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfssnapshotstatuscheck;\
    \n:global snapshotdirectoryname; \
    \n:local maxusedspace;\
    \n:local sysadmin;\
    \n\
    \n:set \$maxusedspace ( \$maxusedspace 80 );\
    \n:set \$sysadmin ( \$sysadmin \"<servername@domain.tld>\" );\
    \n:set \$snapshotdirectoryname (\$snapshotdirectoryname \"@snapshots\");\
    \n\
    \n if (\$btrfssnapshotstatuscheck != \"started\") do={\
    \n         :set \$btrfssnapshotstatuscheck (\$btrfssnapshotstatuscheck \"started\");\
    \n         foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n           :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n           :local valueofusedspace [/disk/print count-only where use>=\$maxusedspace and fs-label=\$temp];\
    \n           if ( \$valueofusedspace=0) do={\
    \n            foreach j in=[/disk/btrfs/subvolume/find  where fs=\$temp and top-level!=\$snapshotdirectoryname and fullname!=\$snapshotdirectoryname ] do={\
    \n               :local parentvar [ /disk/btrfs/subvolume/get value-name=name \$j; ];\
    \n               :local datentime ([/system/clock/get date].\"-\".[/system/clock/get time]);\
    \n                  /disk/btrfs/subvolume/add read-only=yes fs=\"\$temp\" parent=\"\$parentvar\" name=\"\$snapshotdirectoryname/\$temp-\$parentvar-\$datentime\";\
    \n                   /log/info message=\"INFO: Braid snapshot created for  \$temp subvolume \$parentvar snapshotname  \$snapshotdirectoryname/\$temp-\$parentvar-\$datentime\";\
    \n                :delay 1;\
    \n            }\
    \n          } else={\
    \n                   /log/info message=\"ERROR: Snapshot was not created for safety reason.  Braid array \$temp used space exceeded \$maxusedspace %. Add more disks or cleanup storage.\"; \
    \n                   /tool/e-mail/send to= \$sysadmin  subject=([/system/identity/get name].\" ERROR: Braid snapshot was not created \") body=(\"Snapshot was not created for safety reason.  Braid array \" .\$temp. \" used space exceeded \" .\$max\
    usedspace. \" % Add more disks or cleanup storage. \" );\
    \n          }\
    \n\
    \n          :delay 3; \
    \n         }\
    \n        :set \$btrfssnapshotstatuscheck (\$btrfssnapshotstatuscheck \"done\");\
    \n}\
    \n"
add dont-require-permissions=no name=BraidSnapshotCleanUpStart owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfssnapshotcleanupstatuscheck;\
    \n:global snapshotdirectoryname; \
    \n:local maxsnapshotstokeep;\
    \n:local maxdaysoldsnapshotstokeep;\
    \n:local sysadmin;\
    \n\
    \n:set \$maxsnapshotstokeep ( \$maxsnapshotstokeep 10);\
    \n:set \$maxdaysoldsnapshotstokeep (\$maxdaysoldsnapshotstokeep \"10d\");\
    \n:set \$sysadmin ( \$sysadmin \"<servername@domain.tld>\" );\
    \n:set \$snapshotdirectoryname (\$snapshotdirectoryname \"@snapshots\");\
    \n\
    \n if (\$btrfssnapshotcleanupstatuscheck != \"started\") do={\
    \n         :set \$btrfssnapshotcleanupstatuscheck (\$btrfssnapshotcleanupstatuscheck \"started\");\
    \n         foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n           :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n           :local currenttimestamp; :set  \$currenttimestamp ( \$currenttimestamp [/system/clock/get date ] );\
    \n          :set  \$currenttimestamp ( \$currenttimestamp  -\$maxdaysoldsnapshotstokeep);\
    \n            foreach j in=[/disk/btrfs/subvolume/find  where fs=\$temp and top-level=\$snapshotdirectoryname ] do={\
    \n               :local parentname [ /disk/btrfs/subvolume/get value-name=name \$j;];\
    \n               :local parentsubvol [ /disk/btrfs/subvolume/get value-name=parent \$j; ];\
    \n               :local creationtimeofsnapshot; :set \$creationtimeofsnapshot (\$creationtimeofsnapshot [/disk/btrfs/subvolume/get value-name=creation-time \$j; ]);\
    \n               :local countparentsnapshots;  :set \$countparentsnapshots (\$countparentsnapshots [/disk/btrfs/subvolume/print count-only  where fs=\$temp and top-level=\$snapshotdirectoryname and parent=\$parentsubvol]);\
    \n               if ([:len \$parentsubvol]=0) do={\
    \n                   :local parentfullname [ /disk/btrfs/subvolume/get value-name=fullname \$j;];\
    \n                    /log/info message=\"INFO: SnapshotCleanup found snapshot of completely deleted subvolume. Location of snapshot \$temp/\$snapshotdirectoryname/\$parentname. This can only be removed manually.\";\
    \n               } else={\
    \n                if (\$currenttimestamp>=\$creationtimeofsnapshot or  \$countparentsnapshots>\$maxsnapshotstokeep ) do={\
    \n                   /log/info message=\"INFO: Braid snapshot  \$snapshotdirectoryname/\$parentname deleted. SnapshotCleanUp keeps  \$maxsnapshotstokeep snapshots or snapshots not older than \$maxdaysoldsnapshotstokeep days.\";\
    \n                  /disk/btrfs/subvolume/remove \$parentname;\
    \n                :delay 1;\
    \n               }\
    \n             }\
    \n            }\
    \n          :delay 3; \
    \n         }\
    \n        :set \$btrfssnapshotcleanupstatuscheck (\$btrfssnapshotcleanupstatuscheck \"done\");\
    \n}\
    \n"
```

## Free space

In Btrfs, due to how data is stored in chunks, it is important to make sure there is enough free space in order for not just regular maintenance tasks to run properly, but also for the performance of the file system to be optimal. To make sure your Btrfs file system is working properly, consider checking that there is enough free space on your Btrfs file system. An optimal value of free space is 10%, but you should not allow your Btrfs file system to fill up to 5% free space.

- Summary: Do not allow the Btrfs file system to be full.
- Recommended free space: 5-10%.

## Example command

```routeros
/disk/btrfs/filesystem/print
```

:::tip

In case you require more space, consider adding the disk to a Btrfs RAID array with one or more disks.

:::
