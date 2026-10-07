# save

> Command saves the configuration in binary backup file.

-----------

## system/backup/save 
**Type:** Command

Command saves the configuration in binary [backup file](../../../getting-started/configuration-management/backup.md).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="file">The filename for the backup file.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password for the encrypted backup file. Since RouterOS v6.43, without a provided password, the backup file is unencrypted.</ArgTableRow>
<ArgTableRow arg="dont-encrypt" typ="bool">Disable backup file encryption. Since RouterOS v6.43, without a provided password, the backup file is unencrypted.</ArgTableRow>
<ArgTableRow arg="encryption" typ="enum (aes-sha256 | rc4) { aes-sha256:0, rc4:1 }">The encryption algorithm to use for encrypting the backup file. `rc4` is not a secure encryption method and is only available for compatibility with older RouterOS versions.</ArgTableRow>
</ArgTable>
