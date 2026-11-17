# add-scep

> RouterOS command reference for /certificate/add-scep.

-----------

## certificate/add-scep 
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-identity" typ="string"></ArgTableRow>
<ArgTableRow arg="template" typ="enum">Template to enrol.</ArgTableRow>
<ArgTableRow arg="scep-url" typ="string">URL of the SCEP server.</ArgTableRow>
<ArgTableRow arg="challenge-password" typ="string">One-time password generated on the SCEP server.</ArgTableRow>
<ArgTableRow arg="on-smart-card" typ="bool">stores private key on smart card if hardware supports it</ArgTableRow>
<ArgTableRow arg="refresh" typ="bool">check certificate expiry and refresh it if expired</ArgTableRow>
</ArgTable>
