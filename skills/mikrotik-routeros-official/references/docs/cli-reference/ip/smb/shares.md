# shares

> RouterOS directory reference for /ip/smb/shares.

-----------

## ip/smb/shares 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">The entry is created automatically.</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">The share is disabled and not accessible to clients.</ArgTableRow>
<ArgTableRow arg="*" typ="default">The entry is a default entry created by the system.</ArgTableRow>
<ArgTableRow arg="r" typ="read-only">The share only allows clients to read; write access is denied.</ArgTableRow>
<ArgTableRow arg="c" typ="require-encryption">The share accepts only encrypted connections.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the SMB share that clients connect to.</ArgTableRow>
<ArgTableRow arg="directory" typ="file">Directory on the router that the share points to. When it is not set, the value of `name` from the root directory is used. The directory is created automatically if it does not exist.</ArgTableRow>
<ArgTableRow arg="read-only" typ="bool">Whether clients can only read the share. Access can also be restricted per user with `read-only` in [`users`](users). Default: no.</ArgTableRow>
<ArgTableRow arg="require-encryption" typ="bool">Whether only encrypted connections can access the share; recommended for macOS clients. Default: no.</ArgTableRow>
<ArgTableRow arg="valid-users" typ="multi { array-id, user: enum
 }">List of SMB users allowed to access the share. When the list is empty, all users can access it.</ArgTableRow>
<ArgTableRow arg="invalid-users" typ="multi { array-id, user: enum
 }">List of SMB users explicitly denied access to the share.</ArgTableRow>
</ArgTable>
