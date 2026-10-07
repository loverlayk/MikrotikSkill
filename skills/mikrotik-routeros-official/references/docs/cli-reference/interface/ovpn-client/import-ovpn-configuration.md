# import-ovpn-configuration

> RouterOS command reference for /interface/ovpn-client/import-ovpn-configuration.

-----------

## interface/ovpn-client/import-ovpn-configuration 
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file-name" typ="file">Path to the .ovpn client configuration file to import.</ArgTableRow>
<ArgTableRow arg="skip-cert-import" typ="bool">Ignore certificate information in the .ovpn file if certificates are added manually.</ArgTableRow>
<ArgTableRow arg="key-passphrase" typ="string">Passphrase for the certificate private key.</ArgTableRow>
<ArgTableRow arg="ovpn-user" typ="string">Username for authentication with the OVPN server.</ArgTableRow>
<ArgTableRow arg="ovpn-password" typ="string">Password for authentication with the OVPN server.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="progress" typ="string">Import progress status.</ArgTableRow>
</ArgTable>
