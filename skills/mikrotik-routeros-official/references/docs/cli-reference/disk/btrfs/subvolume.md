# subvolume

> RouterOS directory reference for /disk/btrfs/subvolume.

-----------

## disk/btrfs/subvolume 
**Conditions:** !smips
**Syscap:** storage
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">The entry is the root subvolume of the file system, shown as `<FS_ROOT>`; it is created automatically with the file system.</ArgTableRow>
<ArgTableRow arg="S" typ="snapshot">The subvolume is a snapshot, created with the `parent` argument.</ArgTableRow>
<ArgTableRow arg="r" typ="read-only">The subvolume is read-only.</ArgTableRow>
<ArgTableRow arg="D" typ="dead">The subvolume is dead, for example it is being removed.</ArgTableRow>
<ArgTableRow arg="M" typ="mounted">The subvolume is mounted (`mount=yes`) under its `mountpoint`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="fs" typ="enum" mandatory="1">Label of the Btrfs file system the subvolume belongs to, as shown in [`filesystem`](filesystem/).</ArgTableRow>
<ArgTableRow arg="parent" typ="enum">Subvolume the new subvolume is created from. With `parent`, the new subvolume becomes a snapshot of the parent and shares its content at the time of creation. See [Btrfs subvolumes and snapshots](../../../storage/btrfs/snapshots).</ArgTableRow>
<ArgTableRow arg="name" typ="string">Name of the subvolume. A path-like name, for example `Snapshots/backup-10`, places the subvolume inside another subvolume; `top-level` then shows the containing subvolume.</ArgTableRow>
<ArgTableRow arg="read-only" typ="bool">Whether the subvolume is read-only (`r - READ-ONLY` flag). Default: no.</ArgTableRow>
<ArgTableRow arg="mount" typ="bool">Whether the subvolume is mounted under its `mountpoint` (`M - MOUNTED` flag). Default: no.</ArgTableRow>
<ArgTableRow arg="mountpoint" typ="string">Mount point the subvolume is mounted under, relative to the file system mount point. Defaults to the name of the subvolume.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="top-level" typ="enum">Top-level subvolume the subvolume is located in, for example `Snapshots`; `<FS_ROOT>` when the subvolume sits directly under the file system root.</ArgTableRow>
<ArgTableRow arg="fullname" typ="string">Full path of the subvolume within the file system, for example `Snapshots/backup-10`.</ArgTableRow>
<ArgTableRow arg="uuid" typ="string">UUID of the subvolume.</ArgTableRow>
<ArgTableRow arg="received-uuid" typ="string">UUID of the subvolume on the sender when the subvolume was received with a Btrfs [`transfer`](transfer); empty for locally created subvolumes.</ArgTableRow>
<ArgTableRow arg="creation-time" typ="date">Date and time the subvolume was created.</ArgTableRow>
<ArgTableRow arg="subvolume-id" typ="num">Btrfs ID number of the subvolume.</ArgTableRow>
<ArgTableRow arg="generation" typ="num">Btrfs transaction generation of the subvolume.</ArgTableRow>
<ArgTableRow arg="dead" typ="bool">Whether the subvolume is dead (`D - DEAD` flag).</ArgTableRow>
<ArgTableRow arg="snapshot" typ="bool">Whether the subvolume is a snapshot (`S - SNAPSHOT` flag).</ArgTableRow>
<ArgTableRow arg="send-trans-id" typ="num">Btrfs transaction ID of the last send the subvolume was part of.</ArgTableRow>
<ArgTableRow arg="send-time" typ="date">Time the subvolume was last sent with a Btrfs transfer.</ArgTableRow>
<ArgTableRow arg="recv-trans-id" typ="num">Btrfs transaction ID of the receive that created the subvolume.</ArgTableRow>
<ArgTableRow arg="recv-time" typ="date">Time the subvolume was received with a Btrfs transfer.</ArgTableRow>
<ArgTableRow arg="snapshots" typ="multi { array-id, snapshot: enum
 }">Snapshots that were created from this subvolume.</ArgTableRow>
<ArgTableRow arg="path" typ="string">Path the subvolume was received into by a Btrfs [`transfer`](transfer) (`file=` on the receiver); empty for locally created subvolumes.</ArgTableRow>
</ArgTable>
