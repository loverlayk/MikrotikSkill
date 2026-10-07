# firmware-upgrade

> RouterOS command reference for /interface/ppp-client/firmware-upgrade.

-----------

## interface/ppp-client/firmware-upgrade 
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="upgrade" typ="bool">perform the upgrade or just check</ArgTableRow>
<ArgTableRow arg="firmware-file" typ="file">path or url for the upgrade image</ArgTableRow>
<ArgTableRow arg="update-channel" typ="enum (stable | testing)">firmware update channel</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="installed" typ="string"></ArgTableRow>
<ArgTableRow arg="latest" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="note" typ="string"></ArgTableRow>
</ArgTable>
