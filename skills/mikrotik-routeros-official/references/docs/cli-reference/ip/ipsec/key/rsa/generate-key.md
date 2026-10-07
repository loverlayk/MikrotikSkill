# generate-key

> Generate a private key. Takes two parameters, name of the newly generated key and key size 1024,2048 and 4096.

-----------

## ip/ipsec/key/rsa/generate-key 
**Type:** Command

Generate a private key. Takes two parameters, name of the newly generated key and key size 1024,2048 and 4096.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name for the generated key.</ArgTableRow>
<ArgTableRow arg="key-size" typ="alt { key-size: enum (2048 | 4096 | 8192) { 2048:2048, 4096:4096, 8192:8192 }
 }">RSA key size in bits.</ArgTableRow>
</ArgTable>
