# import

> Imports a public SSH key from a file in the router's root directory and assigns it to a user. Accepted formats: OpenSSH single-line, PKCS#1 PEM ("BEGIN RSA PUBLIC KEY") and PKCS#8/SPKI PEM ("BEGIN PUBLIC KEY"). See...

-----------

## user/ssh-keys/import 
**Type:** Command

Imports a public SSH key from a file in the router's root directory and assigns it to a user. Accepted formats: OpenSSH single-line, PKCS#1 PEM ("BEGIN RSA PUBLIC KEY") and PKCS#8/SPKI PEM ("BEGIN PUBLIC KEY"). See [User](../../../authentication-authorization-accounting/user) for the full guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="public-key-file" typ="file">Name of the key file in the router's root directory.</ArgTableRow>
<ArgTableRow arg="user" typ="enum">System user to assign the key to.</ArgTableRow>
<ArgTableRow arg="info" typ="string">Free-text label for the key.</ArgTableRow>
</ArgTable>
