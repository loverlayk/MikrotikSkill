# Backup

> Save the RouterOS configuration to a binary file, encrypt it, and restore it later on the same device.

# Backup

The system backup saves the whole router configuration to a single binary file. Save a backup before a risky change, for example before an upgrade or a batch of firewall edits, and restore it when the configuration breaks. For a change that can cut your connection, or one you plan to undo, [safe mode](./#safe-mode) and [undo/redo](./#configuration-undo-and-redo) are lighter alternatives.

A backup restores reliably only on the device it was made on. The backup contains the device's MAC addresses, so restoring it on another device can leave the interfaces misconfigured. To copy a configuration between devices, [export and import](./#configuration-export) it instead.

:::warning
A backup contains sensitive parameters, such as passwords and keys; see the [list of menus with sensitive parameters](./list-of-menus-with-sensitive-parameters). A backup saved without a password stores the configuration in readable form. Encrypt the backup and keep it in a safe place.
:::

## Save a backup

Save the configuration to a backup file:

```ros
[admin@MikroTik] > /system/backup/save name=config-before-update password=StrongPass
Configuration backup saved
```

The command creates the file `config-before-update.backup` in the [`/file`](../../cli-reference/file/) menu:

```ros
[admin@MikroTik] > /file/print where name~"config-before-update"
Columns: NAME, TYPE, SIZE, LAST-MODIFIED
# NAME                         TYPE    SIZE     LAST-MODIFIED      
0 config-before-update.backup  backup  35.8KiB  2026-10-16 07:15:38
```

Store a copy off the router, for example by downloading the file with [WinBox or FTP](../../system-information-and-utilities/files). To create backups regularly, add a scheduler entry that runs the save command; see the [scheduler example](../../system-information-and-utilities/scheduler).

Provide a `password` to encrypt the backup file. Without a password, the backup is stored unencrypted. `encryption` selects the algorithm: `aes-sha256` by default, or `rc4` for compatibility with older RouterOS versions. `dont-encrypt=yes` stores the backup unencrypted even when a password is given.

## Restore a backup

Give the backup name as you used with `save`, without the `.backup` extension. Load the backup file and confirm the reboot:

```ros
[admin@MikroTik] > /system/backup/load name=config-before-update password=StrongPass
Restore and reboot? [y/N]: y
Restoring system configuration
System configuration restored, rebooting now
```

The router reboots with the restored configuration. Answer `n` to cancel the restore. When `password` is omitted, RouterOS asks for it; for an unencrypted backup, any password works.

:::note
Restore the backup on the same RouterOS version the backup was made on. To load a backup made on RouterOS v6, add `force-v6-to-v7-configuration-upgrade=yes`.
:::

## What the backup does not contain

The system backup does not include the databases of [The Dude](../../management-tools/dude) or [User Manager](../../authentication-authorization-accounting/user-manager#database). Both store their data separately on the device, so use their own backup mechanisms to save these databases.

## Cloud backup

Store an encrypted copy of the backup on the MikroTik cloud server and download it later to the same or a replacement device. See [Cloud backup](../../network-management/cloud/cloud-backup).

## Troubleshoot

- The restore fails with `failure: bad password`. The password does not match the one used with `save`; a wrong password is reported during the restore, after the confirmation.
- A script that runs `load` without the `password` argument fails with `missing value(s) of argument(s) password`. Pass the password as an argument; the interactive prompt is not available in scripts.
