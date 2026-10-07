# enable-ssl-certificate

> RouterOS command reference for /certificate/enable-ssl-certificate.

-----------

## certificate/enable-ssl-certificate 
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="dns-name" typ="string">domain name for SSL certificate</ArgTableRow>
<ArgTableRow arg="directory-url" typ="string">ACME directory url</ArgTableRow>
<ArgTableRow arg="eab-hmac-key" typ="string">base64url encoded EAB hmac key</ArgTableRow>
<ArgTableRow arg="eab-kid" typ="string">EAB account id</ArgTableRow>
<ArgTableRow arg="reset-private-key" typ="bool">initialize new private key</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="progress" typ="string"></ArgTableRow>
</ArgTable>
