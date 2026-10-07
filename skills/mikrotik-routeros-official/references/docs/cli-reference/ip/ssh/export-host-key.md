# export-host-key

> Export public and private RSA/Ed25519 keys to files.

-----------

## ip/ssh/export-host-key 
**Type:** Command

Export public and private RSA/Ed25519 keys to files.

:::info
Host keys are exported in PKCS#8 format.

Exporting the SSH host key requires "sensitive" user policy.
:::

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="key-file-prefix" typ="string">Prefix for generated files. For example, prefix 'my' generates files 'my_rsa', 'my_rsa.pub'. Host keys are exported in PKCS#8 format.</ArgTableRow>
<ArgTableRow arg="passphrase" typ="string">Private key passphrase.</ArgTableRow>
</ArgTable>
