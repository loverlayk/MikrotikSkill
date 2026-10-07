# raid

> This page provides step-by-step instructions for setting up a Btrfs RAID1 array using two disks in RouterOS, covering disk preparation, formatting, adding devices, balancing data, and ensuring consistent RAID profiles.

:::info
This feature requires the [Storage](../) package.
:::

# Btrfs RAID

A Btrfs file system can span multiple disks with different *storage profiles* per data kind (`data`, `meta`, `system`). Converting a one-disk file system into RAID1 or RAID10 takes two steps: add the disks with [`add-device`](../../cli-reference/disk/btrfs/filesystem/add-device), then convert the profiles with [`balance-start`](../../cli-reference/disk/btrfs/filesystem/balance-start) - all without unmounting and without losing data.

## Two disk Btrfs-RAID (RAID1)

In case you want to create a reliable data storage solution with just two disks (for example, NAS), then you can follow these steps to successfully create a RAID1 array with Btrfs:

1. Find the names of the disks you want to use for setting up a Btrfs-RAID.  

   ```routeros
   /disk/print
   ```

   :::warning
   In this example, the disks used are going to be called `<disk-name-1>`  and `<disk-name-2>` , make sure you replace these placeholders with your actual disk names!
   :::
2. Format one of your disks to Btrfs, in this case `<disk-name-1>`. The newly created Btrfs file system is automatically labelled `<disk-name-1>-fs`.  

   ```routeros
   /disk/format <disk-name-1> file-system=btrfs
   ```

3. You can check the current status of Btrfs disks using the following command.  

   ```routeros
   /disk/btrfs/filesystem/print
   ```

   :::info
   In case there was an existing RAID on your disks and you want to remove any obsolete configuration for simplicity, then you can wipe the disks with `/disk/format <disk-name-x> file-system=wipe-quick` . This is useful when you have unwanted entries under `/disk/btrfs/filesystem/print`
   :::
4. Add a label for the Btrfs drive for simplicity.  

   ```routeros
   /disk/btrfs/filesystem/set [find where devs=<disk-name-1>] label=BtrfsRAID
   ```

5. Add a disk to an existing Btrfs disk. This only adds the disk to the file system - the new disk receives no data yet.  

   ```routeros
   /disk/btrfs/filesystem/add-device [find where devs=<disk-name-1>] device=<disk-name-2>
   ```

6. Start the Btrfs balance process to convert the file system to RAID1. The balance rewrites every chunk to the new profile on both disks:  

   ```routeros
   /disk/btrfs/filesystem/balance-start [find where label=BtrfsRAID] data-profile=raid1 metadata-profile=raid1 system-profile=raid1
   ```

   Progress is reported under `balance-status` in `/disk/btrfs/filesystem/print detail`; the finished state is `done`. Cancel a running balance with [`balance-cancel`](../../cli-reference/disk/btrfs/filesystem/balance-cancel).
7. **IMPORTANT:** Double check that all Btrfs profiles for the disks match. In this case, you need to make sure that the `data` , `meta`  and `system` profiles are `raid1` in the `spaces` column.  

   ```routeros
   /disk/btrfs/filesystem/print
   ```

    :::danger
    If you notice, for example, in the output `data,single:1` , then you will need to execute the `/disk/btrfs/filesystem/balance-start` command again.
    :::

   :::info
   The desired state is when the output is similar to the one below with the Btrfs profile for `data` , `system` and `meta set to raid1` :

   ```routeros
   > /disk/btrfs/filesystem/print
   ...
   data,raid1:1.07GB disk1:1.07GB disk2:1.07GB, used:0%                                                                                                       
   system,raid1:33.6MB disk1:33.6MB disk2:33.6MB, used:0%                                                                                                     
   meta,raid1:1.07GB disk1:1.07GB disk2:1.07GB, used:0%    
   ```

   :::

   :::tip
   Use the [BtrfsRAIDCheck](#creating-btrfs-raid-check) script to warn you about Btrfs profile inconsistencies!
   :::
8. Set `mount-filesystem=no` for the second disk to prevent the files showing up twice.  

   ```routeros
   /disk/set <disk-name-2> mount-filesystem=no
   ```

   :::info
   Btrfs has a feature that allows you to mount any of the Btrfs-RAID members and you will still be able to access the whole Btrfs-RAID array. A downside of this feature is that if you have mounted the same array twice, then your files will appear twice as well. To prevent this, you can simply disable mounting one of the Btrfs-RAID members automatically.
   :::
9. You can also change the mount point's name for simplicity.  

   ```routeros
   /disk/set <disk-name-1> mount-point-template=BtrfsRAID
   ```

10. Your newly created Btrfs-RAID array is now accessible through the `/BtrfsRAID/` folder.

With a reliable storage solution such as Btrfs-RAID, consider adding useful features to your RouterOS device by following the suggested guides below:

- running your own [Containers](../../containers/)
- [DLNA Media Server](../dlna)
- [SMB server](../smb)
- [NFS server](../nfs)

:::warning
When regular [RAID](../raid/) is used with Btrfs filesystem, then your RAID array will not be able to heal itself from Bitrot, your RAID array can only detect Bitrot with regular RAID. It is recommended to use Btrfs-RAID (the configuration described in this section) when possible.
:::

## Four disk Btrfs-RAID (RAID10)

In case you want to create a redundant and high capacity RAID10 array using Btrfs, follow the commands below:

1. Find the names of the disks you want to use for setting up a Btrfs-RAID.  

```routeros
/disk/print
```

   :::warning
   In this example, the disks used are going to be called `<disk-name-1>,``<disk-name-2>, <disk-name-3> and <disk-name-4>`, make sure you replace these placeholders with your actual disk names!
   :::

1. Format one of your disks to Btrfs, in this case `<disk-name-1>` :  

   ```routeros
   /disk/format <disk-name-1> file-system=btrfs
   ```

2. You can check the current status of Btrfs disks using the following command:  

   ```routeros
   /disk/btrfs/filesystem/print
   ```

   :::info
   In case there was an existing RAID on your disks and you want to remove any obsolete configuration for simplicity, then you can wipe the disks with `/disk/format <disk-name-x> file-system=wipe-quick` . This is useful when you have unwanted entries under `/disk/btrfs/filesystem/print`
   :::
3. Add a label for the Btrfs drive for simplicity:  

   ```routeros
   /disk/btrfs/filesystem/set [find where devs=<disk-name-1>] label=BtrfsRAID
   ```

4. Add other disks to an existing Btrfs disk:  

   ```routeros
   /disk/btrfs/filesystem/add-device [find where devs=<disk-name-1>] device=<disk-name-2>
   /disk/btrfs/filesystem/add-device [find where devs=<disk-name-1>] device=<disk-name-3>
   /disk/btrfs/filesystem/add-device [find where devs=<disk-name-1>] device=<disk-name-4>
   ```

5. Start the Btrfs balance process to convert the file system to RAID10:  

   ```routeros
   /disk/btrfs/filesystem/balance-start [find where label=BtrfsRAID] data-profile=raid10 metadata-profile=raid1c4 system-profile=raid1c4
   ```

   :::info
   There are many possible configurations of `data-profile` , `metadata-profile` and `system-profile` . For a RAID10 array it is recommended to use either `raid1c3` or `raid1c4` for both `system-profile` and `metadata-profile. The raid1c4 profile is going to store 4 copies of the data on different disks. This makes the data more redundant, but uses more disk space.`
   :::

   :::danger
   Btrfs RAID5 and RAID6 is not supported. Use [regular RAID](../raid/) if you need such RAID configurations. Be aware that when using [regular RAID](../raid/) with Btrfs you will not have bit-rot protection.
   :::

   :::warning
   For most use cases set `metadata-profile` to the same value as `system-profile` . Avoid using different values for both of these profiles.
   :::
6. Set `mount-filesystem=no` for other disks to prevent the files from showing up twice:  

   ```routeros
   /disk/set <disk-name-2> mount-filesystem=no
   /disk/set <disk-name-3> mount-filesystem=no
   /disk/set <disk-name-4> mount-filesystem=no
   ```

7. You can also change the mount point's name for simplicity:  

   ```routeros
   /disk/set <disk-name-1> mount-point-template=BtrfsRAID
   ```

8. Your newly created Btrfs-RAID array is now accessible through the `/BtrfsRAID/` folder.

## Replacing a disk in a Btrfs RAID array

In case of a disk failure or you need to replace a disk in your existing Btrfs RAID array, then follow the procedure below:

1. Make sure you determine the correct disk that needs replacing. Use `/disk/print detail` and `/disk/blink` to determine the correct disk. We will assume that the faulty disk is `disk2` .
2. Eject the faulty disk:  

   ```routeros
   /disk/eject disk2
   ```

3. Physically remove the faulty disk.
4. Print out the current status of your Btrfs RAID array:  

   ```routeros
   /disk/btrfs/filesystem/print
   ```

5. Look for the `DEV-ID` in the command's output for the missing disk:  

   ```routeros
   [admin@MikroTik] /disk> /disk/btrfs/filesystem/print
   Flags: I - MISSING-DEVS
   Columns: LABEL, DEV-IDS, DEVS, DEFAULT-SUBVOLUME, SPACES, BALANCE-STATUS, UUID, WRITE-ERRORS, READ-ERRORS, FLUSH-ERRORS, CORRUPTION-ERRORS, GENERATION-ERRORS
   #   LABEL      DEV-IDS  DEVS     DEFAULT-SUBVOLUME  SPACES                                     BALANCE-STATUS  UUID                                  W  R  F  C  G
   0 I BtrfsRAID        1  disk1    <FS_ROOT>          disk1:480GB, used:0%                       done            9246dfaa-be9f-4e08-a560-53cb8e82023b  0  0  0  0  0
                        2  missing                     data,raid1:1.07GB disk1:1.07GB, used:0%                                                          0  0  0  0  0
                                                        data,single:1.07GB, used:0%                                                                                   
                                                        system,raid1:33.6MB disk1:33.6MB, used:0%                                                                     
                                                        meta,raid1:1.07GB disk1:1.07GB, used:0%                                                                       
                                                        global-reserve:3.41MB, used:0%                                                                                

   ```

   :::info
   In this case the missing disk's `DEV-ID` is "2".
   :::
6. Insert a new disk.
7. Determine the new disk's name:  

   ```routeros
   /disk/print
   ```

   :::info
   In this case the new disk's name is `disk3`
   :::
8. Run the following command to replace the disk in the Btrfs RAID array:  

   ```routeros
   /disk/btrfs/filesystem/replace-device device-to-remove-id=2 device-to-add=disk3 BtrfsRAID
   ```

   :::warning
   Make sure you set the correct `device-to-remove-id` to the `DEV-ID` that you determined previously!
   :::

   :::info
   [`replace-device`](../../cli-reference/disk/btrfs/filesystem/replace-device) works on a missing (ejected) or unmounted device. If the source disk is healthy and still mounted, unmount it first (`/disk/set <disk> mount-filesystem=no`), otherwise the command fails with `could not unmount <disk>`. Track it under `replace-status`; stop it with [`replace-cancel`](../../cli-reference/disk/btrfs/filesystem/replace-cancel).
   :::
9. Check the replace status and make sure that `REPLACE-STATUS` is marked as `done` .  

   ```routeros
   > /disk/btrfs/filesystem/print
   Columns: LABEL, DEV-IDS, DEVS, DEFAULT-SUBVOLUME, SPACES, BALANCE-STATUS, REPLACE-STATUS, UUID, WRITE-ERRORS, READ-ERRORS, FLUSH-ERRORS, CORRUPTION-ERRORS, GENERATION-ERRORS
   # LABEL   DEV-IDS  DEVS   DEFAULT-SUBVOLUME  SPACES                                                 BALANCE-STATUS  REPLACE-STATUS  UUID                                  WRITE-ERRORS  READ-ERRORS  F  C  G
   0 BtrfsRAID     1  disk1  <FS_ROOT>          disk1:480GB, used:9%                                   done            done            9246dfaa-be9f-4e08-a560-53cb8e82023b             0            0  0  0  0
                   2  disk3                     disk3:480GB, used:9%                                                                                                                    0  0  0  0  0
                                                 data,raid1:40.8GB disk1:40.8GB disk3:40.8GB, used:72%                                                                                                          
                                                 system,raid1:101MB disk1:101MB disk3:101MB, used:0%                                                                                                            
                                                 meta,raid1:3.22GB disk1:3.22GB disk3:3.22GB, used:1%                                                                                                           
                                                 global-reserve:30.7MB, used:0%                                                 
   ```

   :::info
   Ensure that your Btrfs RAID array does not have inconsistent Btrfs profiles for `data` , `system`  or `meta` . The desired profiles will depend on your specific setup. For RAID1 setups you will most likely want these profiles to match, but in a RAID10 setup these values can be different. In any RAID setup there should not be a `single` profile for either `data` , `system`  or `meta` .
   :::

## Creating Btrfs-RAID check

It is extremely important for you to monitor the Btrfs-RAID array's health. One way you can do this is by using the script below as a working example:

```routeros
/system/scheduler
add interval=1w30s name=BraidBalanceStartCall on-event=BraidBalanceStart policy=ftp,read,write,policy,test,sniff start-date=1970-01-01 start-time=01:00:00
add interval=1w30s name=BraidScrubStartCall on-event=BraidScrubStart policy=ftp,read,write,policy,test,sniff start-date=1970-01-01 start-time=02:00:00
add interval=2m name=BraidBalanceStatusCheckCall on-event=BraidBalanceStatus policy=ftp,read,write,policy,test,sniff start-time=startup
add interval=2m name=BraidScrubStatusCheckCall on-event=BraidScrubStatus policy=ftp,read,write,policy,test,sniff start-time=startup
add interval=30s name=BraidHealthCheckCall on-event=BraidHealthCheck policy=ftp,read,write,policy,test,sniff start-time=startup
add interval=2m name=BraidReplaceStatusCheckCall on-event=BraidReplaceStatus policy=ftp,read,write,policy,test,sniff start-time=startup

/system/script
add dont-require-permissions=no name=BraidScrubStart owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfsscrubstatuscheck;\
    \nif (\$btrfsscrubstatuscheck != \"started\") do={\
    \n  :set \$btrfsscrubstatuscheck (\$btrfsscrubstatuscheck \"started\");\
    \n  foreach i in=[/disk/btrfs/filesystem/find] do={ /disk/btrfs/filesystem/scrub-start \$i;\
    \n    :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n    /log/info message=\"INFO: Btrfs scrub process started on  \$temp\";\
    \n    :delay 3; \
    \n  }\
    \n}\
    \n"
add dont-require-permissions=no name=BraidBalanceStart owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfsbalancestatuscheck;\
    \nif (\$btrfsbalancestatuscheck != \"started\") do={\
    \n:set \$btrfsbalancestatuscheck (\$btrfsbalancestatuscheck \"started\");\
    \n:local percentage;\
    \n:set \$percentage (\$percentage 50);\
    \n  foreach i in=[/disk/btrfs/filesystem/find] do={ /disk/btrfs/filesystem/balance-start data-usage=\$percentage \$i;\
    \n    :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n    /log/info message=\"INFO: Btrfs balance process started on  \$temp\";\
    \n    :delay 3; \
    \n  }\
    \n}"
add dont-require-permissions=no name=BraidBalanceStatus owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfsbalancestatuscheck;\
    \nif (\$btrfsbalancestatuscheck = \"started\") do={\
    \n:local arraycnt [/disk/btrfs/filesystem/print count-only as-value];\
    \n:local counter [:set \$counter (\$counter 0)];\
    \n:local counterdiff [:set \$counterdiff (\$counterdiff 0)];\
    \n  foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n    :local barray [ /disk/btrfs/filesystem/get value-name=balance-status  \$i;]\
    \n    :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n    if ( \$barray != \"done\" and \$btrfsbalancestatuscheck = \"started\") do={\
    \n        /log/info message=\"INFO: Btrfs current balance status on  \$temp is \$barray\";\
    \n    }\
    \n    if ( \$barray = \"done\" and \$btrfsbalancestatuscheck = \"started\") do={\
    \n      :set \$counter (\$counter +1);\
    \n      :set \$counterdiff (\$arraycnt - \$counter);\
    \n      if (\$counterdiff =1) do={\
    \n        /log/info message=\"INFO: Btrfs balancing already done on \$counter arrays\";\
    \n      }\
    \n    }\
    \n    if ( \$counter = \$arraycnt) do={\
    \n      /log/info message=\"INFO: Btrfs array balance status on  \$temp is \$barray \";\
    \n      :set \$btrfsbalancestatuscheck (\$btrfsbalancestatuscheck \"done\");\
    \n    }\
    \n  } \
    \n}"
add dont-require-permissions=no name=BraidScrubStatus owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfsscrubstatuscheck;\
    \nif (\$btrfsscrubstatuscheck = \"started\") do={\
    \n:local arraycnt [/disk/btrfs/filesystem/print count-only as-value];\
    \n:local counter [:set \$counter (\$counter 0)];\
    \n:local counterdiff [:set \$counterdiff (\$counterdiff 0)];\
    \n  foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n    :local barray [ /disk/btrfs/filesystem/get value-name=scrub-status  \$i;]\
    \n    :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n    if ( \$barray != \"done\" and \$btrfsscrubstatuscheck = \"started\") do={\
    \n      /log/info message=\"INFO: Btrfs current scrub status on  \$temp is \$barray\";\
    \n    }\
    \n    if ( \$barray = \"done\" and \$btrfsscrubstatuscheck = \"started\") do={\
    \n      :set \$counter (\$counter +1);\
    \n      :set \$counterdiff (\$arraycnt - \$counter);\
    \n      if (\$counterdiff =1) do={\
    \n        /log/info message=\"INFO: Btrfs scrubbing already done on \$counter arrays\";\
    \n      }\
    \n    }\
    \n    if ( \$counter = \$arraycnt ) do={\
    \n      /log/info message=\"INFO: Btrfs array scrub status on  \$temp is \$barray \";\
    \n      :set \$btrfsscrubstatuscheck (\$btrfsscrubstatuscheck \"done\");\
    \n    }\
    \n  } \
    \n}"
add dont-require-permissions=no name=BraidReplaceStatus owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfsreplacestatuscheck;\
    \nif (\$btrfsreplacestatuscheck = \"started\") do={\
    \n:local arraycnt [/disk/btrfs/filesystem/print count-only as-value];\
    \n:local counter [:set \$counter (\$counter 0)];\
    \n:local counterdiff [:set \$counterdiff (\$counterdiff 0)];\
    \n  foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n    :local barray [ /disk/btrfs/filesystem/get value-name=replace-status  \$i;]\
    \n    :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n    :local multipleprofiles [ /disk/btrfs/filesystem/get value-name=spaces \$i; ]\
    \n    if ( \$barray ~ \"working\" and \$btrfsreplacestatuscheck = \"started\") do={\
    \n      /log/info message=\"INFO: Btrfs current replace status on  \$temp is \$barray\";\
    \n    }\
    \n    if ( \$barray ~ \"done\" and \$btrfsreplacestatuscheck = \"started\" and \$multipleprofiles~\"single\" ) do={\
    \n      /log/info message=\"INFO: Braid balance after replace-device  started on  \$temp\";\
    \n         if (\$btrfsbalancestatuscheck!=\"started\") do={\
    \n             /disk/btrfs/filesystem/balance-start \$temp;\
    \n             :set \$btrfsbalancestatuscheck (\$btrfsbalancestatuscheck \"started\");\
    \n         }\
    \n    }\
    \n    if ( \$barray = \"done\" and \$btrfsreplacestatuscheck = \"started\") do={\
    \n      :set \$counter (\$counter +1);\
    \n      :set \$counterdiff (\$arraycnt - \$counter);\
    \n      if (\$counterdiff =1) do={\
    \n        /log/info message=\"INFO: Btrfs replace already done on \$counter arrays\";\
    \n      }\
    \n    }\
    \n    if ( \$counter = \$arraycnt ) do={\
    \n      /log/info message=\"INFO: Btrfs array replace status on  \$temp is \$barray \";\
    \n      :set \$btrfsreplacestatuscheck (\$btrfsreplacestatuscheck \"done\");\
    \n    }\
    \n  } \
    \n}\
    \n:set \$btrfsreplacestatuscheck (\$btrfsreplacestatuscheck \"started\");"
add dont-require-permissions=no name=BraidHealthCheck owner=admin policy=ftp,read,write,policy,test,sniff source="foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n:local sysadmin; \
    \n\
    \n:set  \$sysadmin \"<servername@domain.tld>\";\
    \n\
    \n:local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n:local haserror [/disk/btrfs/filesystem/get value-name=about \$i; ]\
    \n:local hasmissing [ /disk/btrfs/filesystem/get value-name=devs \$i; ]\
    \n:local hasmultiprofile [ /disk/btrfs/filesystem/get value-name=spaces \$i; ]\
    \n:local replacestatus [ /disk/btrfs/filesystem/get value-name=replace-status \$i; ]\
    \n:local multiplediskarray [:len [/disk/btrfs/filesystem/find where label=\$temp and dev-ids~\"2\"];]\
    \n\
    \n  if ( \$hasmissing~\"missing\" and ([:len \$replacestatus]=0)) do= {\
    \n    /log/info message=\"ERROR: BtrfsHealthCheck found missing array member on \$temp\";\
    \n    /tool/e-mail/send to= \$sysadmin  subject=([/system/identity/get name].\" BtrfsHealthCheck found missing array member\") body=(\"Btrfs array where found missing array member on \" .\$temp . \"   \");\
    \n   :delay 19; \
    \n  }\
    \n\
    \n  if ( \$multiplediskarray > 0 and \$hasmultiprofile~\"single\") do= {\
    \n    /log/info message=\"ERROR: BtrfsHealthCheck found multiprofile on \$temp array. To start balance process, run  /disk/btrfs/filesystem/balance-start \$temp command \";\
    \n    /tool/e-mail/send to= \$sysadmin  subject=([/system/identity/get name].\" BtrfsHealthCheck found multiprofile on \" .\$temp. \" array.\") body=(\"Btrfs array where found with multiprofile status on \" .\$temp . \"To start balance process, run once\
    \_ /disk/btrfs/filesystem/balance-start \" .\$temp. \" command \");\
    \n   :delay 19; \
    \n  }  \
    \n\
    \n  if (([:len \$haserror]) > 0 ) do= {\
    \n    /log/info message=\"ERROR: BtrfsHealthCheck found errors on \$temp\";\
    \n    /tool/e-mail/send to= \$sysadmin  subject=([/system/identity/get name].\" BtrfsHealthCheck found errors\") body=(\"Btrfs array where found errors on \" .\$temp . \"   \");\
    \n    :delay 20; \
    \n  }\
    \n}\
    \n"
```

You also need to adjust e-mail server settings on your RouterOS device:

```routeros
/tool/e-mail
set from=<raidcheck@domain.tld> port=587 server=smtp.domain.com tls=starttls
```

:::warning
Make sure you adjust the e-mail settings with the required settings on your e-mail server. Remember to adjust the e-mail address in the script above.

:::
