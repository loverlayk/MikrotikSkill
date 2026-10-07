# frequency-scan

> RouterOS command reference for /interface/wifi/frequency-scan.

-----------

## interface/wifi/frequency-scan 
**Type:** Command

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="radar">radar</ArgTableRow>
<ArgTableRow arg="P" typ="primary">primary</ArgTableRow>
<ArgTableRow arg="S" typ="secondary">secondary</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="rounds" typ="num"></ArgTableRow>
<ArgTableRow arg="save-file" typ="string"></ArgTableRow>
<ArgTableRow arg="frequency" typ="object" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="channel" typ="string"></ArgTableRow>
<ArgTableRow arg="networks" typ="num"></ArgTableRow>
<ArgTableRow arg="load" typ="num"></ArgTableRow>
<ArgTableRow arg="nf" typ="num"></ArgTableRow>
<ArgTableRow arg="max-signal" typ="num"></ArgTableRow>
<ArgTableRow arg="min-signal" typ="num"></ArgTableRow>
<ArgTableRow arg="srp-networks" typ="num"></ArgTableRow>
<ArgTableRow arg="srp-load" typ="num"></ArgTableRow>
</ArgTable>
