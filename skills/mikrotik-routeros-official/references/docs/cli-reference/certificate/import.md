# import

> RouterOS command reference for /certificate/import.

-----------

## certificate/import 
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name for the imported certificate.</ArgTableRow>
<ArgTableRow arg="file-name" typ="file">File to import. The file is deleted after the import.</ArgTableRow>
<ArgTableRow arg="pem" typ="string">import certificate or private key from a pasted PEM string; an encrypted private key is accepted when passphrase is supplied</ArgTableRow>
<ArgTableRow arg="passphrase" typ="string">Passphrase of an encrypted private key or PKCS12 file.</ArgTableRow>
<ArgTableRow arg="trusted" typ="bool">mark as trusted</ArgTableRow>
<ArgTableRow arg="trust-store" typ="alt { all: enum (all)
, component: ubit (ipsec, wpa-eap, capsman, fetch, sstp, ovpn, mqtt, email, netwatch, radius, container, userman, lora, wiliot, openflow, tr069, dot1x, dns, www, api, reverse-proxy, logging)
 }">Services that use the imported certificate as a trusted authority. Default: `all`.</ArgTableRow>
<ArgTableRow arg="no-key-export" typ="bool">disallow private key export</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="certificates-imported" typ="num"></ArgTableRow>
<ArgTableRow arg="private-keys-imported" typ="num"></ArgTableRow>
<ArgTableRow arg="files-imported" typ="num"></ArgTableRow>
<ArgTableRow arg="decryption-failures" typ="num"></ArgTableRow>
<ArgTableRow arg="keys-with-no-certificate" typ="num"></ArgTableRow>
<ArgTableRow arg="keys-decrypted" typ="num"></ArgTableRow>
</ArgTable>
