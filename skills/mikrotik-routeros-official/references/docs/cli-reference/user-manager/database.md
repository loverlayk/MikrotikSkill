# database

> Location and size of the User Manager database. The database is not part of the system backup: use save and load.

-----------

## user-manager/database 
**Package:** userman-5
**Type:** Settings Directory

Location and size of the User Manager database. The database is not part of the system backup: use `save` and `load`.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="db-path" typ="string">Folder of the database files. Default: `/user-manager5`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="found-legacy-db-path" typ="string">Folder of a RouterOS v6 User Manager database found on the router. Use it as `database-path` of `migrate-legacy-db`.</ArgTableRow>
<ArgTableRow arg="db-size" typ="num">Size of the database.</ArgTableRow>
<ArgTableRow arg="free-disk-space" typ="num">Free space on the disk that has the database.</ArgTableRow>
</ArgTable>
