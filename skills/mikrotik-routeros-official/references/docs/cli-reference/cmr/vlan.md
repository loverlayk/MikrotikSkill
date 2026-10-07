# vlan

> The /cmr/vlan menu creates bridge and VLAN configuration on the selected CMR clients. Each rule selects the devices with labels and the ports with port-labels (matched against the interface names of a device and...

-----------

## cmr/vlan 
**Package:** cmr
**Type:** Directory

The `/cmr/vlan` menu creates bridge and VLAN configuration on the selected CMR clients. Each rule selects the devices with `labels` and the ports with `port-labels` (matched against the interface names of a device and against the port labels assigned in `/cmr/device`), lists the `vlan-ids`, and assigns each port a `role`. On a selected device the rule creates a dedicated bridge named `cmr-bridge` with VLAN filtering enabled and moves the selected ports into it. Removing a rule restores the previous configuration. See the [VLAN provisioning](../../management-tools/cmr/#vlan-provisioning) section of the CMR guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">VLAN provisioning rule is disabled.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="labels" typ="object" unset="1">Select the CMR clients this rule provisions. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used. If omitted, the rule applies to all connected devices.</ArgTableRow>
<ArgTableRow arg="port-labels" typ="object" unset="1">Select the ports to configure on the selected devices, by interface name (for example `ether1`) or by a port label assigned to the port in `/cmr/device` (for example `uplink`). If omitted, all ports of the selected devices are configured.</ArgTableRow>
<ArgTableRow arg="vlan-ids" typ="multi { vlan-range: range [1 .. 4094]
 }" mandatory="1">VLAN IDs assigned to the selected ports, as a comma-separated list or a range, for example `100,200` or `100-200`. On a trunk port every VLAN ID is tagged; on an access port only the first VLAN ID is used, as the port's PVID.</ArgTableRow>
<ArgTableRow arg="role" typ="enum (access | trunk)" unset="1">
Port role assigned to the selected ports:
- `access` (default) - the port belongs to a single VLAN, which is set as the port's PVID, and carries untagged frames
- `trunk` - the port carries multiple VLANs; frames are tagged with 802.1Q headers so the far end can tell them apart
</ArgTableRow>
</ArgTable>
