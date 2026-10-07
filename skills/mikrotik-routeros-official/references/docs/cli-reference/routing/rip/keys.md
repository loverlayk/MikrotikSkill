# keys

> MD5 authentication key chains.

-----------

## routing/rip/keys 
**Type:** Directory

MD5 authentication key chains.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="chain" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="key-id" typ="num" mandatory="1">Key identifier. This number is included in MD5 authenticated RIP messages, and determines which key to use to check authentication for a specific message.</ArgTableRow>
<ArgTableRow arg="key" typ="string" mandatory="1">Authentication key. Maximal length 16 characters</ArgTableRow>
<ArgTableRow arg="valid-from" typ="date">The key is valid from this date and time.</ArgTableRow>
<ArgTableRow arg="valid-till" typ="date">The key is valid until this date and time.</ArgTableRow>
</ArgTable>
