# Btrfs subvolumes and snapshots

> This page guides users through creating Btrfs subvolumes and snapshots in RouterOS, explaining how to organize data, format disks, set up subvolumes like Documents and Photos, and create snapshots for efficient...

# Btrfs subvolumes and snapshots

:::info
This feature requires the `rose-storage` package; see [Storage](../).
:::

## Create subvolumes

The main benefit of creating subvolumes is to organize data on your Btrfs main (root) subvolume. Consider subvolumes as folders with features of a partition, while still sharing the total disk space between all subvolumes. You can later use these subvolumes for much more advanced tasks and it is recommended to create subvolumes when you have large amounts of different types of data, especially data that requires frequent backups. Follow the guide to set up a few example subvolumes:

:::tip
Subvolumes are most useful when used together with snapshots. Be sure to check out the snapshot feature as well.

:::

1. Find the disk name of your disk that you want to use as your Btrfs disk:  

   ```routeros
   /disk/print
   ```

   :::warning
   In this example, the disk used is going to be called `<disk-name-1>` , make sure you replace the placeholder with your actual disk name!
   :::
2. Format the disk to Btrfs, in this case `<disk-name-1>` :  

   ```routeros
   /disk/format <disk-name-1> file-system=btrfs
   ```

3. Add a label for the Btrfs disk for simplicity (by default it is automatically labelled `<disk-name-1>-fs` after the format):  

   ```routeros
   /disk/btrfs/filesystem/set [find where devs=<disk-name-1>] label=BtrfsDisk
   ```

4. You can also change the Btrfs disk mount point for simplicity:  

   ```routeros
   /disk/set <disk-name-1> mount-point-template=BtrfsDisk
   ```

5. Create a new subvolume called `Documents` to `BtrfsDisk`:  

   ```routeros
   /disk/btrfs/subvolume/add name=Documents fs=BtrfsDisk
   ```

   :::info
   Subvolumes are also snapshots. You might encounter both of these names in various menus. In simple terms, snapshots are subvolumes created at a specific time and contain data from that time point.
   :::
6. Create another subvolume called `Photos` to `BtrfsDisk`:  

   ```routeros
   /disk/btrfs/subvolume/add name=Photos fs=BtrfsDisk
   ```

7. You can view the currently available subvolumes:  

   ```routeros
   /disk/btrfs/subvolume/print
   ```

8. You can now access these subvolumes as `/BtrfsDisk/Documents` and `/BtrfsDisk/Photos`.

## Create snapshots

Snapshots are a space efficient way to create backups for your data. By creating a snapshot you save the current state of your data which you can later access.

:::warning

Snapshots don't create a copy of your data, they save the current state of your data while allowing you to make changes to your current data. Snapshots contain the information on how to revert the current data to a state that was present at the time when the snapshot was created. Snapshots don't create multiple copies of your data like, for example, a full backup does.

:::

:::note

While you can create snapshots of a root subvolume, it is recommended to create a new subvolume for your data and then use the snapshot feature. This is only a preference when managing many snapshots.

:::

1. Create subvolumes (or use the root subvolume, see above) and put data in them, for example `BtrfsDisk/Documents/document1.txt` and `BtrfsDisk/Photos/photo1.jpg`.

2. To keep the snapshots organized, create a subvolume called `Snapshots`:  

   ```routeros
   /disk/btrfs/subvolume/add name=Snapshots fs=BtrfsDisk
   ```

3. Create read-only snapshots of `Documents` and `Photos`:  

   ```routeros
   /disk/btrfs/subvolume/add read-only=yes parent=Documents fs=BtrfsDisk \
       name=Snapshots/Documents-22012025
   /disk/btrfs/subvolume/add read-only=yes parent=Photos fs=BtrfsDisk \
       name=Snapshots/Photos-22012025
   ```

   The snapshots contain the files that the subvolumes had at that time. Files that you add later, for example `document2.txt` and `photo2.jpg`, appear only in the subvolumes.

4. Create new snapshots:  

   ```routeros
   /disk/btrfs/subvolume/add read-only=yes parent=Documents fs=BtrfsDisk \
       name=Snapshots/Documents-23012025
   /disk/btrfs/subvolume/add read-only=yes parent=Photos fs=BtrfsDisk \
       name=Snapshots/Photos-23012025
   ```

   Each subvolume now has two snapshots: one with the older files, and one with the older and the newer files (`/file/print where name~"^BtrfsDisk"`):  

   ```text
    # NAME                                                
    2 BtrfsDisk                                           
    3 BtrfsDisk/Documents                                 
    4 BtrfsDisk/Photos                                    
    5 BtrfsDisk/Snapshots                                 
    6 BtrfsDisk/Documents/document1.txt                   
    7 BtrfsDisk/Documents/document2.txt                   
    8 BtrfsDisk/Photos/photo1.jpg                         
    9 BtrfsDisk/Photos/photo2.jpg                         
   10 BtrfsDisk/Snapshots/Documents-22012025              
   11 BtrfsDisk/Snapshots/Photos-22012025                 
   12 BtrfsDisk/Snapshots/Documents-23012025              
   13 BtrfsDisk/Snapshots/Photos-23012025                 
   14 BtrfsDisk/Snapshots/Documents-22012025/document1.txt
   15 BtrfsDisk/Snapshots/Documents-23012025/document1.txt
   16 BtrfsDisk/Snapshots/Documents-23012025/document2.txt
   17 BtrfsDisk/Snapshots/Photos-22012025/photo1.jpg      
   18 BtrfsDisk/Snapshots/Photos-23012025/photo1.jpg      
   19 BtrfsDisk/Snapshots/Photos-23012025/photo2.jpg
   ```

   :::note
   Multiple snapshots do not create multiple copies of each file, but if a file has been deleted and it still exists in a snapshot, then the deleted file will take up space. If a file exists in multiple snapshots, then it will take up space for only 1 file.
   :::

5. Delete a snapshot that you no longer need. `name` is the last part of the full name, without `Snapshots/`:  

   ```routeros
   /disk/btrfs/subvolume/remove [find where name=Documents-22012025]
   /disk/btrfs/subvolume/remove [find where name=Photos-22012025]
   ```

## Transfer your snapshots

[`/disk/btrfs/transfer`](../../cli-reference/disk/btrfs/transfer) sends a read-only snapshot as a stream and receives it on another Btrfs file system. In this example, `RouterA` (10.99.0.1) has the snapshots, and `RouterB` (10.99.0.2) keeps the backups on a Btrfs file system labelled `BackupBtrfsDisk`.

### Between RouterOS devices

Send the snapshot to a file, copy the file to the other router, and receive it there.

1. On `RouterA`, send the snapshot `Documents-23012025` to a file. `send-subvolumes` takes the snapshot name, not its path:  

   ```routeros
   /disk/btrfs/transfer/add type=send fs=BtrfsDisk \
       send-subvolumes=Documents-23012025 file=BtrfsDisk/doc.send
   ```

   When the stream is written, the entry in `/disk/btrfs/transfer/print detail` has `status="done"` and the size in `bytes`.

2. Copy the file to `RouterB`, for example with [`/file/sync`](../rsync.md), and remove the sync entry afterwards:  

   ```routeros
   /file/sync/add local-path=BtrfsDisk/doc.send remote-address=10.99.0.2 \
       remote-path=BackupBtrfsDisk/doc.send user=admin mode=upload
   ```

3. On `RouterB`, receive the snapshot from the file:  

   ```routeros
   /disk/btrfs/transfer/add fs=BackupBtrfsDisk type=receive \
       file=BackupBtrfsDisk/doc.send
   ```

   The snapshot appears as a read-only subvolume at the top of the file system, `BackupBtrfsDisk/Documents-23012025`, with its files.

### Send over SSH to a Linux host

With `ssh-address`, `ssh-user` and `ssh-receive-mount` instead of `file`, the router connects to a remote host over SSH and runs a `btrfs` command there to receive the stream. The receiver must therefore be a host with the Btrfs tools, such as a Linux server; a RouterOS router cannot receive over SSH. The router authenticates with the private key imported for its user in [`/user/ssh-keys/private`](../../cli-reference/user/ssh-keys/private/private.md), and the remote host key must be trusted in [`/ip/ssh/known-hosts`](../../management-tools/ssh.md#verify-remote-host-keys); check the result on the receiving host.
