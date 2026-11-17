# create-certificate-request

> Create a certificate request and a private key from a template. Writes the files certificate-request.pem and certificate-requestkey.pem.

-----------

## certificate/create-certificate-request 
**Type:** Command

Create a certificate request and a private key from a template. Writes the files `certificate-request.pem` and `certificate-request_key.pem`.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="template" typ="enum">Template to create the request from.</ArgTableRow>
<ArgTableRow arg="key-passphrase" typ="string">Passphrase that encrypts the private key file.</ArgTableRow>
<ArgTableRow arg="challenge-passphrase" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="progress" typ="string"></ArgTableRow>
</ArgTable>
