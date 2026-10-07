# multi-passphrase

> RouterOS directory reference for /interface/wifi/security/multi-passphrase.

-----------

## interface/wifi/security/multi-passphrase 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="E" typ="expired">expired</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="group" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="expires" typ="date" unset="1"></ArgTableRow>
<ArgTableRow arg="isolation" typ="bool" unset="1"></ArgTableRow>
</ArgTable>
