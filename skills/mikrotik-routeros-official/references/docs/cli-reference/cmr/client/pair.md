# pair

> Initiate pairing process to CMR server.

-----------

## cmr/client/pair 
**Conditions:** !mipsel, !smips, !powerpc
**Type:** Command

Initiate pairing process to CMR server.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="username" typ="string" unset="1">CMR server username.</ArgTableRow>
<ArgTableRow arg="password" typ="string" unset="1">CMR server password.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="address (flags=46)">CMR server IP address.</ArgTableRow>
<ArgTableRow arg="status" typ="string">Pairing status.</ArgTableRow>
</ArgTable>
