# macsec

> RouterOS directory reference for /interface/macsec.

-----------

## interface/macsec 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">hw-offloaded</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="cak" typ="string"></ArgTableRow>
<ArgTableRow arg="ckn" typ="string"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="tx-untagged" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-untagged" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-too-long" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-no-tag" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bad-tag" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-unknown-sci" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-no-sci" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-overrun" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-sc-protected-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sc-protected-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sc-encrypted-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sc-encrypted-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-validated-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-decrypted-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-unchecked" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-delayed" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-ok" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-invalid" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-late" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-not-valid" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-not-using-sa" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sc-unused-sa" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sa-ok" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sa-invalid" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sa-not-valid" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sa-not-using-sa" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-sa-unused-sa" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sa-protected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-sa-encrypted" typ="multi { counter: num
 }"></ArgTableRow>
</ArgTable>
