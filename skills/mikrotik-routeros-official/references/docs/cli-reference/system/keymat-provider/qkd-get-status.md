# qkd-get-status

> RouterOS command reference for /system/keymat-provider/qkd-get-status.

-----------

## system/keymat-provider/qkd-get-status 
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="sae-id" typ="string">if not specified, peer-sae-id will be used</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="source-kme-id" typ="string"></ArgTableRow>
<ArgTableRow arg="target-kme-id" typ="string"></ArgTableRow>
<ArgTableRow arg="master-sae-id" typ="string"></ArgTableRow>
<ArgTableRow arg="slave-sae-id" typ="string"></ArgTableRow>
<ArgTableRow arg="key-size" typ="num"></ArgTableRow>
<ArgTableRow arg="stored-key-count" typ="num"></ArgTableRow>
<ArgTableRow arg="max-key-count" typ="num"></ArgTableRow>
<ArgTableRow arg="max-key-per-request" typ="num"></ArgTableRow>
<ArgTableRow arg="max-key-size" typ="num"></ArgTableRow>
<ArgTableRow arg="min-key-size" typ="num"></ArgTableRow>
<ArgTableRow arg="max-sae-id-count" typ="num"></ArgTableRow>
</ArgTable>
