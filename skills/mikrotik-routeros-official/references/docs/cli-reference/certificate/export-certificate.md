# export-certificate

> RouterOS command reference for /certificate/export-certificate.

-----------

## certificate/export-certificate 
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="export-passphrase" typ="string">Passphrase that encrypts the exported private key. Without it, only the certificate is exported.</ArgTableRow>
<ArgTableRow arg="type" typ="enum (pem | pkcs12)">
Format of the export.
- `pem` (default) - A `.crt` file with the certificate and, with `export-passphrase`, a `.key` file with the encrypted private key.
- `pkcs12` - One `.p12` file with the certificate, its private key and the certificate of the authority.
</ArgTableRow>
<ArgTableRow arg="file-name" typ="file">Name of the exported files without the extension. Default: `cert_export_<certificate name>`.</ArgTableRow>
</ArgTable>
