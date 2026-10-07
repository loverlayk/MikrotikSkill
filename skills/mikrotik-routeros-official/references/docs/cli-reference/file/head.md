# head

> Prints the first lines of a file's contents. With as-value, the lines are returned as an array of strings in lines. See the Files guide.

-----------

## file/head 
**Type:** Command

Prints the first lines of a file's contents. With `as-value`, the lines are returned as an array of strings in `lines`. See the [Files](../../system-information-and-utilities/files#head-or-tail-a-file) guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="n" typ="num" unset="1">Number of lines to output from the beginning of the file. Range: 1..1000. Default: 10.</ArgTableRow>
<ArgTableRow arg="numbered" typ="switch">Show line numbers in front of each line.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="lines" typ="object { line: string
 }">The output lines returned as an array of strings.</ArgTableRow>
</ArgTable>
