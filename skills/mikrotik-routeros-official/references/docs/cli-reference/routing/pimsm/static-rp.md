# static-rp

> The static-rp menu allows manually defining the multicast group to RP mappings. Such a mechanism is not robust to failures but does at least provide a basic interoperability mechanism.

-----------

## routing/pimsm/static-rp 
**Conditions:** !smips
**Type:** Directory

The static-rp menu allows manually defining the multicast group to RP mappings. Such a mechanism is not robust to failures but does at least provide a basic interoperability mechanism.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum" mandatory="1">The name of the PIM instance this static RP belongs to.</ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46/)">The multicast group that belongs to a specific RP.</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)">The IP address of the static RP.</ArgTableRow>
</ArgTable>
