# mounts

> Lists of mounts: a directory on the router mounted into containers. A container uses them with mountlists. If the source directory does not exist, it is created and filled with the content of the destination in the...

-----------

## container/mounts 
**Package:** container
**Type:** Directory

Lists of mounts: a directory on the router mounted into containers. A container uses them with `mountlists`. If the source directory does not exist, it is created and filled with the content of the destination in the image.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The entry is disabled.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="list" typ="enum" mandatory="1">Name of the list.</ArgTableRow>
<ArgTableRow arg="src" typ="file">Directory on the router, for example `disk1/volumes/pihole/pihole`.</ArgTableRow>
<ArgTableRow arg="dst" typ="string" mandatory="1">Directory in the container, for example `/etc/pihole`.</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (rw | ro | rw,noexec | ro,noexec)"></ArgTableRow>
</ArgTable>
