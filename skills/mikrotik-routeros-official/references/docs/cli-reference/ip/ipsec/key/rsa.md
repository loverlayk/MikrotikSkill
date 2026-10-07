# rsa

> RouterOS directory reference for /ip/ipsec/key/rsa.

-----------

## ip/ipsec/key/rsa 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="P" typ="private-key">Whether the item contains a private key.</ArgTableRow>
<ArgTableRow arg="R" typ="rsa">Whether the item uses an RSA key.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Key name.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="key-size" typ="num">RSA key size in bits.</ArgTableRow>
</ArgTable>
