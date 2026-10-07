# upload-file

> Uploads an AES-encrypted backup to this device's slot on the cloud server. When the slot is used, the upload fails with Server error: All slots used. Delete file to free up space., unless replace names the stored backup.

-----------

## system/backup/cloud/upload-file 
**Type:** Command

Uploads an AES-encrypted backup to this device's slot on the cloud server. When the slot is used, the upload fails with `Server error: All slots used. Delete file to free up space.`, unless `replace` names the stored backup.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="action" typ="enum (upload | create-and-upload)">
What to upload:
- `create-and-upload` - Create a backup of the current configuration, encrypt it with `password` and upload it.
- `upload` - Upload the backup file given in `src-file`.
</ArgTableRow>
<ArgTableRow arg="name" typ="string">Name of the backup in the cloud list. It does not have to match a file name.</ArgTableRow>
<ArgTableRow arg="replace" typ="enum">Name of the stored backup to overwrite. The new backup gets a new `secret-download-key`.</ArgTableRow>
<ArgTableRow arg="src-file" typ="file">Backup file to upload with `action=upload`. The file must be saved with a password (`/system/backup/save password=...`), otherwise the command fails with `src file must be AES encrypted`.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password that encrypts the backup with `action=create-and-upload`. Required for that action; you need it to restore the backup.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string">Progress of the command: `working...` while it runs, `finished` when it is done, or the error message, for example from the cloud server.</ArgTableRow>
</ArgTable>
