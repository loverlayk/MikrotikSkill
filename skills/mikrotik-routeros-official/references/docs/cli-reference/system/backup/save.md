# save

> Saves the whole router configuration in a binary backup file. The backup file appears in the /file menu and can be copied off the router.

-----------

## system/backup/save 
**Type:** Command

Saves the whole router configuration in a binary [backup file](../../../getting-started/configuration-management/backup.md). The backup file appears in the `/file` menu and can be copied off the router.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="file">Name of the backup file. The file is saved as `<name>.backup` and appears in the `/file` menu.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password that encrypts the backup file. Without a password, the backup is saved unencrypted.</ArgTableRow>
<ArgTableRow arg="dont-encrypt" typ="bool">Save the backup unencrypted even when `password` is given. Default: no.</ArgTableRow>
<ArgTableRow arg="encryption" typ="enum (aes-sha256 | rc4) { aes-sha256:0, rc4:1 }">
Encryption algorithm used when `password` is given.
- `aes-sha256` (default) - Encryption with AES and SHA-256.
- `rc4` - Legacy weak algorithm, kept for compatibility with older RouterOS versions.
</ArgTableRow>
</ArgTable>
