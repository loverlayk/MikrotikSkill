# Encrypted storage (dm-crypt)

> Encrypted storage (dm-crypt) enables transparent disk encryption for block devices in RouterOS, configured with type=crypted and an encryption key. Examples show creating encrypted file systems on USB drives or on...

# Encrypted storage (dm-crypt)

:::info
This feature requires the `rose-storage` package; see [Storage](./index.md).
:::

RouterOS supports transparent block device encryption with `dm-crypt`. Add a disk item with `type=crypted` and point `crypted-backend` at the drive or partition to encrypt; decryption is done with `encryption-key`. The data written to the backend disk is encrypted, and the backend disk gets the `c` (encrypted) flag in `/disk/print`.

RouterOS keeps the key in its configuration and opens the encrypted device at startup without any input. The encryption therefore protects the data on a disk that is removed from the router, not on a router that is taken together with its disks. `/disk/export` hides the key; `/disk/export show-sensitive` shows it.

## Examples

### Encrypted file system on a disk

Create the encrypted device on `usb1`. All data on the disk is lost:

```routeros
/disk/add crypted-backend=usb1 encryption-key=<secret_key> \
    slot=crypted-usb1 type=crypted
```

Format the encrypted device:

```routeros
/disk/format crypted-usb1 file-system=ext4
```

### Encrypted RAID 1 array

Create a RAID 1 array and put an encrypted file system on top of it:

```routeros
/disk/add raid-device-count=2 raid-type=1 slot=raid1 type=raid
/disk/set nvme3 raid-master=raid1 raid-role=0
/disk/set nvme4 raid-master=raid1 raid-role=1
/disk/add crypted-backend=raid1 encryption-key=<secret_key> \
    slot=crypted-raid1 type=crypted
```

Format the encrypted device to Btrfs:

```routeros
/disk/format crypted-raid1 file-system=btrfs
```
