# Btrfs subvolumes and snapshots

> This page guides users through creating Btrfs subvolumes and snapshots in RouterOS, explaining how to organize data, format disks, set up subvolumes like Documents and Photos, and create snapshots for efficient...

# Btrfs subvolumes and snapshots

:::info
This feature requires the [Storage](../) package.
:::

## Creating subvolumes

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

## Creating snapshots

Snapshots are a space efficient way to create backups for your data. By creating a snapshot you save the current state of your data which you can later access.

:::warning

Snapshots don't create a copy of your data, they save the current state of your data while allowing you to make changes to your current data. Snapshots contain the information on how to revert the current data to a state that was present at the time when the snapshot was created. Snapshots don't create multiple copies of your data like, for example, a full backup does.

:::

:::note

While you can create snapshots of a root subvolume, it is recommended to create a new subvolume for your data and then use the snapshot feature. This is only a preference when managing many snapshots.

:::

1. Create subvolumes (or use the root subvolume, see above) and put data inside these subvolumes, for example:  

   ```routeros
   [admin@MikroTik] > /file/print 
    # NAME   
    0 BtrfsDisk
    1 BtrfsDisk/Documents
    2 BtrfsDisk/Photos 
    3 BtrfsDisk/Documents/document1.txt
    4 BtrfsDisk/Photos/photo1.jpg
   ```

2. In this example, we have created `/BtrfsDisk/Documents` and `/BtrfsDisk/Photos/` subvolumes and you can view them with:  

   ```routeros
   /disk/btrfs/subvolume/print
   ```

3. In order to make snapshots more organized, create a new subvolume called `Snapshots`:  

   ```routeros
   /disk/btrfs/subvolume/add name=Snapshots fs=BtrfsDisk
   ```

4. Create a snapshot for `Documents` and `Photos`:  

   ```routeros
   /disk/btrfs/subvolume/add read-only=yes parent=Documents fs=BtrfsDisk  name=Snapshots/Documents-22012025
   /disk/btrfs/subvolume/add read-only=yes parent=Photos fs=BtrfsDisk  name=Snapshots/Photos-22012025
   ```

5. You should now have new subvolumes that are read-only and contain your files:  

   ```routeros
   [admin@MikroTik] > /file/print 
    # NAME      
    0 BtrfsDisk
    1 BtrfsDisk/Documents
    2 BtrfsDisk/Photos
    3 BtrfsDisk/Snapshots
    4 BtrfsDisk/Documents/document1.txt
    5 BtrfsDisk/Photos/photo1.jpg
    6 BtrfsDisk/Snapshots/Documents-22012025
    7 BtrfsDisk/Snapshots/Photos-22012025
    8 BtrfsDisk/Snapshots/Documents-22012025/document1.txt
    9 BtrfsDisk/Snapshots/Photos-22012025/photo1.jpg
   ```

6. For testing purposes, you can add more data to your subvolumes and you should notice that newly added files do not appear in the snapshots, but only in the subvolumes:  

   ```routeros
   [admin@infra1.mikrotikls.lv] > /file/print 
    # NAME   
    0 BtrfsDisk
    1 BtrfsDisk/Documents
    2 BtrfsDisk/Photos
    3 BtrfsDisk/Snapshots
    4 BtrfsDisk/Documents/document1.txt
    5 BtrfsDisk/Documents/document2.txt
    6 BtrfsDisk/Photos/photo1.jpg
    7 BtrfsDisk/Photos/photo2.jpg 
    8 BtrfsDisk/Snapshots/Photos-22012025
    9 BtrfsDisk/Snapshots/Documents-22012025
   10 BtrfsDisk/Snapshots/Documents-22012025/document1.txt
   11 BtrfsDisk/Snapshots/Photos-22012025/photo1.jpg
   ```

7. You can now create a new snapshot:  

   ```routeros
   /disk/btrfs/subvolume/add read-only=yes parent=Documents fs=BtrfsDisk  name=Snapshots/Documents-23012025 
   /disk/btrfs/subvolume/add read-only=yes parent=Photos fs=BtrfsDisk  name=Snapshots/Photos-23012025 
   ```

8. After a new snapshot, you will have 2 snapshots for each subvolume. One contains older files and another one contains older and newer files:  

   ```routeros
   [admin@MikroTik] > /file/print 
    # NAME   
    0 BtrfsDisk
    1 BtrfsDisk/Documents
    2 BtrfsDisk/Photos
    3 BtrfsDisk/Snapshots
    4 BtrfsDisk/Documents/document1.txt
    5 BtrfsDisk/Documents/document2.txt
    6 BtrfsDisk/Photos/photo1.jpg
    7 BtrfsDisk/Photos/photo2.jpg
    8 BtrfsDisk/Snapshots/Photos-22012025
    9 BtrfsDisk/Snapshots/Documents-22012025
   10 BtrfsDisk/Snapshots/Documents-23012025
   11 BtrfsDisk/Snapshots/Photos-23012025
   12 BtrfsDisk/Snapshots/Documents-22012025/document1.txt 
   13 BtrfsDisk/Snapshots/Documents-23012025/document1.txt
   14 BtrfsDisk/Snapshots/Documents-23012025/document2.txt
   15 BtrfsDisk/Snapshots/Photos-22012025/photo1.jpg
   16 BtrfsDisk/Snapshots/Photos-23012025/photo1.jpg
   17 BtrfsDisk/Snapshots/Photos-23012025/photo2.jpg
   ```

   :::note

   Multiple snapshots do not create multiple copies of each file, but if a file has been deleted and it still exists in a snapshot, then the deleted file will take up space. If a file exists in multiple snapshots, then it will take up space for only 1 file.

   :::
9. In case you don't need an older snapshot, you can delete it:  

   ```routeros
   /disk/btrfs/subvolume/remove [find where name=Documents-22012025]
   /disk/btrfs/subvolume/remove [find where name=Photos-22012025]
   ```

## Transfer your snapshots

Btrfs allows you to easily send a snapshot between two devices that are using Btrfs with [`/disk/btrfs/transfer`](../../cli-reference/disk/btrfs/transfer) on both sides: a `send` entry on the sender and a `receive` entry on the receiver. In this example we will use two RouterOS devices running the Storage package. The RouterOS device containing snapshots that need to be backed up is going to be called `RouterA` and the RouterOS device that is going to receive backups is going to be called `RouterB`.

:::info

This guide only shows an example of how to use Btrfs transfer between RouterOS devices, but you can transfer snapshots between RouterOS and Linux devices as well. If you require such functionality, then make sure to check the documentation of your Linux distribution on how to use Btrfs transfer on it.

:::

:::tip

This guide will use the SSH host key for an SSH user key on the same RouterOS device. If you wish to use your own key for the SSH user, then you can use these commands on a Linux computer and later import the key pair under `/user/ssh-keys` :  

```routeros
openssl genpkey -outform PEM -out btrfstransfer_key.pem -algorithm ED25519
openssl pkey -in btrfstransfer_key.pem -pubout -out btrfstransfer_key_pub.pem
```

:::

1. OPTIONAL: Increase the security level of your SSH server, run the following commands on `RouterA` and `RouterB` :  

   ```routeros
   /ip/ssh/set host-key-type=ed25519 strong-crypto=yes
   /ip/ssh/regenerate-host-key
   ```

   :::warning

   Regenerating the host key will create an error message next time you try to connect to the RouterOS device using SSH. You will need to adjust your SSH client's configuration (usually in `~/.ssh/known_hosts` ) to trust the new host key.

   :::
2. On `RouterA` export the SSH private and public key:  

   ```routeros
   /ip/ssh/export-host-key key-file-prefix=admin
   ```

3. On `RouterA` import the SSH private key for user `admin` :  

   ```routeros
   /user/ssh-keys/private/import private-key-file=admin_ed25519.pem user=admin
   ```

4. Upload the SSH public key from `RouterA` to `RouterB` :  

   ```routeros
   /file/sync/add local-path=admin_ed25519_pub.pem remote-address=RouterB user=admin mode=upload
   /file/sync/remove [find where local-path=admin_ed25519_pub.pem]
   ```

5. On `RouterB` create a new user, for example `btrfstransfer`  and set a secure password for it:  

   ```routeros
   /user/add name=btrfstransfer group=write
   ```

   :::warning

   While the password is not going to be used for the Btrfs transfer feature, you still need to use a secure password to prevent unauthorized access to your device.

   :::
6. On `RouterB` import the uploaded SSH public key and set it for user `btrfstransfer` :  

   ```routeros
   /user/ssh-keys/import public-key-file=admin_ed25519_pub.pem user=btrfstransfer
   ```

7. On `RouterA` set up type `send` :  

   ```routeros
   /disk/btrfs/transfer/add type=send fs=BtrfsDisk ssh-address=RouterB send-subvolumes=Documents-23012025 ssh-user=btrfstransfer ssh-receive-mount=BackupBtrfsDisk/Snapshots
   ```

   Where:  
   - `BtrfsDisk` is the Btrfs disk label found under `/disk/btrfs/filesystem/print` on `RouterA`.
   - `Documents-23012025` is the snapshot name (not the path).
   - `btrfstransfer` is the SSH user on `RouterB`.
   - `BackupBtrfsDisk` is the Btrfs disk label found under `/disk/btrfs/filesystem/print` on `RouterB`.
   - `Snapshots` is the subvolume for your snapshots under `BackupBtrfsDisk`.
8. On `RouterB` set up type `receive` :  

   ```routeros
   /disk/btrfs/transfer/add fs=BackupBtrfsDisk type=receive file=BackupBtrfsDisk/Snapshots
   ```

   Where:  
   - `BackupBtrfsDisk` is the Btrfs disk label found under `/disk/btrfs/filesystem/print` on `RouterB`
   - `BackupBtrfsDisk/Snapshots` is the mount path for `Snapshots` subvolume.
