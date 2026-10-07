# Self-encrypting drives (SED)

> RouterOS supports Self-Encrypting Drives (SED) using the TCG-Opal standard, requiring the Storage package. Supported drives show o (inactive) / O (active) flags in /disk/print, and encryption can be enabled with...

# Self-encrypting drives (SED)

:::info
This feature requires the [Storage](./index.md) package.
:::

For using SED, drives have to be [Opal](https://en.wikipedia.org/wiki/Opal_Storage_Specification)-compliant. Please consult the drive manufacturer's documentation to find out if a particular drive supports this feature before buying drives.

SED is not supported on setups using USB bridges; the disk must be attached directly (SATA or NVMe).

RouterOS marks supported drives with the **o (TCG-OPAL supported, encryption not active)** or **O (TCG-OPAL supported and encryption active)** flags:

```ros
/disk/print
Flags: B - BLOCK-DEVICE; M, F - FORMATTING; o - TCG-OPAL-SELF-ENCRYPTION-SUPPORTED (inactive); O - TCG-OPAL-SELF-ENCRYPTION-SUPPORTED (active)
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS, RAID-MASTER
#     SLOT   MODEL                  SERIAL           INTERFACE                   SIZE             FREE  FS    RAID
0 BMo sata1  Samsung SSD 860 2.5in  S3Z9NX0N414510L  SATA 6.0 Gbps  1 000 204 886 016  983 351 111 680  ext4  none
1 BMo sata2  Samsung SSD 860        S5GENG0N307602J  SATA 6.0 Gbps  1 000 204 886 016  983 351 128 064  ext4  none
2 BMO sata3  Samsung SSD 860        S5GENG0N307604H  SATA 6.0 Gbps  1 000 204 886 016  983 351 128 064  ext4  none
3 BMO sata4  Samsung SSD 860 2.5in  S4CSNX0N838150B  SATA 6.0 Gbps  1 000 204 886 016  983 351 128 064  ext4  none
```

To enable self-encryption on a drive, set `self-encryption-password`:

```ros
/disk/set sata1 self-encryption-password=securepassword
```

Once set, the drive locks itself on power loss and requires the password every time it's connected; RouterOS supplies it automatically (the flag changes to `O`).

To disable self-encryption, unset the password:

```ros
/disk/unset sata1 self-encryption-password
```

or:

```ros
/disk/set sata1 !self-encryption-password
```
