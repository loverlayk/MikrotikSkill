# copy

> RouterOS command reference for /disk/copy.

-----------

## disk/copy 
**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="src" typ="enum">Source disk, partition or file.</ArgTableRow>
<ArgTableRow arg="dst" typ="enum">Destination disk, partition or file. It must be at least as large as the copied data.</ArgTableRow>
<ArgTableRow arg="src-offset" typ="num">Byte offset in the source where the copy starts. Default: 0.</ArgTableRow>
<ArgTableRow arg="dst-offset" typ="num">Byte offset in the destination where the data is written. Default: 0.</ArgTableRow>
<ArgTableRow arg="size" typ="num">Number of bytes to copy. Without it, the whole source is copied.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string">Progress of the copy: `<bytes copied> / <total bytes> (<percent>%)`.</ArgTableRow>
</ArgTable>
