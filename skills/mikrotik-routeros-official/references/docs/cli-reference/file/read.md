# read

> Reads a chunk of a file's contents and returns it as a string in data. Works with files of any size, unlike the contents property, which is limited to just under 60 KiB. See the Files guide.

-----------

## file/read 
**Type:** Command

Reads a chunk of a file's contents and returns it as a string in `data`. Works with files of any size, unlike the `contents` property, which is limited to just under 60 KiB. See the [Files](../../system-information-and-utilities/files#read-file-contents) guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file" typ="file">Name of the file to read.</ArgTableRow>
<ArgTableRow arg="chunk-size" typ="num">Chunk size to read from the file. Required. Range: 1..32768.</ArgTableRow>
<ArgTableRow arg="offset" typ="num">Offset where to start reading the file. A chunk that continues past the end of the file is shortened; an offset past the end fails.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="data" typ="string">The read data returned as a string.</ArgTableRow>
</ArgTable>
