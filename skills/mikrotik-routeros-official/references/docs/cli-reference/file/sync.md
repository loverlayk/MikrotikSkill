# sync

> RouterOS directory reference for /file/sync.

-----------

## file/sync 
**Package:** rose-storage
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The sync entry is disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The entry is invalid, for example it references a missing or unusable path.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">The entry is created automatically.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="remote-address" typ="multi { array-id, address: string
 }" mandatory="1">IP address of the remote RouterOS device to synchronize with. The remote device must have the rsync daemon enabled ([`rsync-daemon`](../rsync-daemon)).</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (upload | download)" mandatory="1">
Direction of the synchronization:
- `upload` - send the `local-path` file or folder to the remote device.
- `download` - fetch `remote-path` from the remote device to this router.
</ArgTableRow>
<ArgTableRow arg="local-path" typ="file">File or folder path on this router; the source for `mode=upload` and the destination for `mode=download`.</ArgTableRow>
<ArgTableRow arg="remote-path" typ="string">File or folder path on the remote device.</ArgTableRow>
<ArgTableRow arg="user" typ="string">RouterOS user on the remote device used for authentication.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password of the user on the remote device. When it is set, the transfers run over automatically created IPsec.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string">Status of the synchronization, for example `in sync`, `making control connection to <ip>` or `initializing transfer`.</ArgTableRow>
</ArgTable>
