# database

> RouterOS settings reference for /user-manager/database.

-----------

## user-manager/database 
**Package:** userman-5
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="db-path" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="found-legacy-db-path" typ="string">Folder of a RouterOS v6 User Manager database found on the router. Use it as `database-path` of `migrate-legacy-db`.</ArgTableRow>
<ArgTableRow arg="db-size" typ="num"></ArgTableRow>
<ArgTableRow arg="free-disk-space" typ="num"></ArgTableRow>
</ArgTable>
