# scep-server

> RouterOS directory reference for /certificate/scep-server.

-----------

## certificate/scep-server 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ca-cert" typ="enum" mandatory="1">Authority certificate that signs the requests.</ArgTableRow>
<ArgTableRow arg="next-ca-cert" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="path" typ="string" mandatory="1">Path of the server in the URL, for example `/scep/example`.</ArgTableRow>
<ArgTableRow arg="days-valid" typ="num"></ArgTableRow>
<ArgTableRow arg="request-lifetime" typ="time"></ArgTableRow>
</ArgTable>
