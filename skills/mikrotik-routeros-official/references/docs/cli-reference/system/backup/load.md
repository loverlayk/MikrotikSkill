# load

> Loads a configuration saved with /system/backup/save from a backup file, then reboots the router after confirmation.

-----------

## system/backup/load 
**Type:** Command

Loads a configuration saved with `/system/backup/save` from a [backup file](../../../getting-started/configuration-management/backup.md), then reboots the router after confirmation.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="file">Name of the backup file, as given to `save` (without the `.backup` extension).</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password used to decrypt the backup file. When omitted, RouterOS asks for it. For an unencrypted backup, any password works.</ArgTableRow>
<ArgTableRow arg="force-v6-to-v7-configuration-upgrade" typ="bool">Whether to load a backup made on RouterOS v6 and convert its configuration to v7. The flag has no effect on a backup made on v7.</ArgTableRow>
</ArgTable>
