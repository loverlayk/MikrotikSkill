# show-devices

> Lists the devices the selected upgrade rule covers. A device is claimed by the first rule in the list that covers it, so a rule can list no devices when an earlier rule covers them all.

-----------

## cmr/upgrade/show-devices 
**Package:** cmr
**Type:** Command

Lists the devices the selected upgrade rule covers. A device is claimed by the first rule in the list that covers it, so a rule can list no devices when an earlier rule covers them all.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="p" typ="remote-pending">Controller requests pairing.</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">Device is inactive.</ArgTableRow>
<ArgTableRow arg="S" typ="stale">No connection (stale).</ArgTableRow>
<ArgTableRow arg="L" typ="controller">The CMR server itself (self-client).</ArgTableRow>
<ArgTableRow arg="C" typ="connected">Device is connected.</ArgTableRow>
<ArgTableRow arg="U" typ="upgrade-available">A newer update is available.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="only-upgradable" typ="bool">Show only the devices that can actually be upgraded.</ArgTableRow>
</ArgTable>
