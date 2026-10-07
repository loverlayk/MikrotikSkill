# pair

> Starts pairing with the selected devices.

-----------

## cmr/device/pair 
**Package:** cmr
**Type:** Command

Starts pairing with the selected devices.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="labels" typ="object" unset="1">Select the devices to pair using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.</ArgTableRow>
<ArgTableRow arg="username" typ="string" unset="1">Username used for pairing when the device requires it.</ArgTableRow>
<ArgTableRow arg="password" typ="string" unset="1">Password used for pairing when the device requires it.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum">Device being paired.</ArgTableRow>
<ArgTableRow arg="status" typ="string">Pairing status.</ArgTableRow>
</ArgTable>
