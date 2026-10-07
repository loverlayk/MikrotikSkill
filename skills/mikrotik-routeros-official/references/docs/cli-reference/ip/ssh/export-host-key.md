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
<ArgTableRow arg="key-file-prefix" typ="string">Prefix for the generated files: for example `my` produces `my_rsa.pem` (private key) and `my_rsa_pub.pem` (public key) for an RSA host key, or `my_ed25519.pem` and `my_ed25519_pub.pem` for an Ed25519 one. Both files are in PKCS#8 PEM format.</ArgTableRow>
<ArgTableRow arg="passphrase" typ="string">Private key passphrase.</ArgTableRow>
</ArgTable>
