# reboot

> Reboots the selected devices. The command returns right away, and the server logs rebooted when a device has restarted, where is identity@address.

-----------

## cmr/device/reboot 
**Package:** cmr
**Type:** Command

Reboots the selected devices. The command returns right away, and the server logs `<device> rebooted` when a device has restarted, where `<device>` is `identity@address`.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="labels" typ="object" unset="1">Select the devices to reboot using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.</ArgTableRow>
</ArgTable>
