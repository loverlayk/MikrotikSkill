# import-host-key

> Import and replace the private RSA/Ed25519 key from a specified file

-----------

## ip/ssh/import-host-key 
**Type:** Command

Import and replace the private RSA/Ed25519 key from a specified file

:::info
The private key is supported in PEM or PKCS#8 format.
:::

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="private-key-file" typ="file">Name of the private RSA/Ed25519 key file in PEM or PKCS#8 format.</ArgTableRow>
<ArgTableRow arg="passphrase" typ="string">Private key passphrase.</ArgTableRow>
</ArgTable>
