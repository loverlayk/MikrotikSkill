# transfer

> RouterOS directory reference for /disk/btrfs/transfer.

-----------

## disk/btrfs/transfer 
**Conditions:** !smips
**Syscap:** storage
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (receive | send)" mandatory="1">
Direction of the Btrfs transfer:
- `receive` - receive a Btrfs send stream at `file`, for example the destination side of a snapshot backup between two RouterOS devices.
- `send` - send subvolumes (snapshots) of the file system `fs` to a remote RouterOS device over SSH.

Transfers use the SSH user key authentication of `/user/ssh-keys`. See [Btrfs subvolumes and snapshots](../../../storage/btrfs/snapshots) for a working send/receive example.
</ArgTableRow>
<ArgTableRow arg="fs" typ="enum">Label of the Btrfs file system the transfer operates on, as shown in [`filesystem`](filesystem/).</ArgTableRow>
<ArgTableRow arg="send-parent" typ="enum">Snapshot of a previous successful send to base an incremental `send` on; only the changes since that snapshot are transferred.</ArgTableRow>
<ArgTableRow arg="send-subvolumes" typ="multi { array-id, subvolume: enum
 }">Snapshots to send, for a `send` transfer. Snapshot names (not paths), as shown under [`subvolume`](subvolume).</ArgTableRow>
<ArgTableRow arg="file" typ="file">Destination (or source) path of the transfer, for example the mount path `BackupBtrfsDisk/Snapshots` where received snapshots are stored.</ArgTableRow>
<ArgTableRow arg="ssh-address" typ="string">Address of the remote RouterOS device for a `send` transfer.</ArgTableRow>
<ArgTableRow arg="ssh-receive-mount" typ="string">Mount path on the remote device under which the snapshots are received, for example `BackupBtrfsDisk/Snapshots`.</ArgTableRow>
<ArgTableRow arg="ssh-port" typ="num">SSH port of the remote device. Default: 22.</ArgTableRow>
<ArgTableRow arg="ssh-user" typ="string">SSH user to authenticate with on the remote device; the SSH key of the local user must be imported for `ssh-user` on the remote device.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="bytes" typ="num">Number of bytes transferred so far.</ArgTableRow>
<ArgTableRow arg="status" typ="string">Status of the transfer, for example `done`, or an error message.</ArgTableRow>
</ArgTable>
