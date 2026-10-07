# Cloud backup

> Store one encrypted RouterOS backup on the MikroTik cloud server, replace or delete it, and download or restore it on the same or another router with its secret download key.

# Cloud backup

Cloud backup stores an encrypted [backup](../../getting-started/configuration-management/backup) of the router's configuration on the MikroTik cloud server. You can download it later to the same router, or with its secret download key to another router, for example a replacement device. Each device has one backup slot.

## Upload a backup

To create a backup of the current configuration and upload it in one step:

```ros
[admin@MikroTik] > /system/backup/cloud/upload-file action=create-and-upload name=home-router password=Str0ng-Passw0rd
  status: finished
[admin@MikroTik] > /system/backup/cloud/print detail
0  name="home-router" size=31.5KiB ros-version="7.25" date=2026-09-24 10:11:16
   status="ok" secret-download-key="Xy3kP9qLm2Rt7vWz8Bn4Cd5"
```

The router encrypts the backup with `password`, which is required. Keep the password: you need it to restore the backup. `name` is only the name in the cloud list.

To upload a backup file you saved earlier, save it with a password, so it is encrypted. The router refuses an unencrypted file with `src file must be AES encrypted`.

```ros
/system/backup/save name=home-router password=Str0ng-Passw0rd
/system/backup/cloud/upload-file action=upload src-file=home-router.backup name=home-router
```

## Replace or delete the backup

The slot holds one backup, so a second upload fails with `Server error: All slots used. Delete file to free up space.` To overwrite the stored backup, give its name in `replace`:

```ros
/system/backup/cloud/upload-file action=create-and-upload name=home-router password=Str0ng-Passw0rd replace=home-router
```

The new backup gets a new secret download key.

To delete the backup and free the slot:

```ros
/system/backup/cloud/remove-file number=0
```

## Download or restore the backup

To download this router's backup to its storage:

```ros
/system/backup/cloud/download-file action=download number=0
```

The router saves the file as `<name>.backup`, or under the name you give in `dst-file`. To restore the configuration from it, use [`/system/backup/load`](../../getting-started/configuration-management/backup#loading-a-backup).

To download and restore in one step, give the backup password. The router restores the configuration and reboots:

```ros
/system/backup/cloud/download-file action=download-and-apply number=0 password=Str0ng-Passw0rd
```

On another router, for example a replacement device, download the backup with the secret download key of the original router:

```ros
/system/backup/cloud/download-file action=download secret-download-key=Xy3kP9qLm2Rt7vWz8Bn4Cd5
```

Anyone who has the key can download the backup file, but cannot read it without the password. Keep the key private and use a strong password. A backup also contains the MAC addresses of the device it was made on (see [Backup](../../getting-started/configuration-management/backup)).

## Technical details

- The router connects to `cloud2.mikrotik.com` on TCP port 15252 for cloud backup.
- Every command in `/system/backup/cloud` connects to the server, `print` too, so a command can take a while to finish. While a command runs, it shows `status: working...`.
- `upload-file` checks the file on the router before it connects: without a password, `create-and-upload` fails with `missing password`, and `upload` refuses an unencrypted file with `src file must be AES encrypted`.
- `download-file` saves the file also with `download-and-apply`, so the downloaded backup stays in `/file` after the restore.

For all commands and properties, see [`/system/backup/cloud`](../../cli-reference/system/backup/cloud/) in the CLI reference.
