# device

> Devices managed by this CMR server. A device appears in the list as soon as it connects to the server, with the P flag until the pairing is approved. The server itself is shown as the device with the L flag. Use the...

-----------

## cmr/device 
**Package:** cmr
**Type:** Directory

Devices managed by this CMR server. A device appears in the list as soon as it connects to the server, with the **P** flag until the pairing is approved. The server itself is shown as the device with the **L** flag. Use the commands in this menu to operate on the fleet, for example `run-script`, `upgrade`, `reboot`, or `pair`. See [CMR](../../../management-tools/cmr) for how devices connect and pair.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="P" typ="pending">Pairing pending.</ArgTableRow>
<ArgTableRow arg="p" typ="remote-pending">Controller requests pairing.</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">Device is inactive.</ArgTableRow>
<ArgTableRow arg="S" typ="stale">No connection (stale).</ArgTableRow>
<ArgTableRow arg="L" typ="controller">The CMR server itself (self-client).</ArgTableRow>
<ArgTableRow arg="C" typ="connected">Device is connected.</ArgTableRow>
<ArgTableRow arg="U" typ="upgrade-available">The upgrade channel of the device offers a different version than the installed one. The offered version can also be earlier than the installed version.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ids" typ="object { ids: super { his-id: string
, [our-id] [ /string]
 }
 }">Identities (his-id / our-id) of the managed device.</ArgTableRow>
<ArgTableRow arg="pairing-requirement" typ="enum (none | password | confirm)">Pairing requirement applied to this device, overriding the server default: `none`, `password`, or `confirm`.</ArgTableRow>
<ArgTableRow arg="labels" typ="multi { array-id, label: enum
 }" unset="1">User labels assigned to the device (grouping/filtering).</ArgTableRow>
<ArgTableRow arg="port-labels" typ="object { port-and-labels: super { port: string
, labels: multi { array-id, label: string
 }
 }
 }" unset="1">Labels per port. Quote the label, for example `port-labels=ether1:"uplink"`. `/cmr/vlan` rules can select ports by these labels.</ArgTableRow>
<ArgTableRow arg="identity" typ="string">System identity (editable) of the device.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="peer" typ="enum">The management peer this device is connected to.</ArgTableRow>
<ArgTableRow arg="board" typ="string">Board name.</ArgTableRow>
<ArgTableRow arg="version" typ="string">RouterOS version of the device.</ArgTableRow>
<ArgTableRow arg="minimum-version" typ="string">Minimum supported version.</ArgTableRow>
<ArgTableRow arg="allowed-versions" typ="string">Safe (safepkg) upgrade indicator.</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)">Current connection address.</ArgTableRow>
<ArgTableRow arg="auto-labels" typ="multi { array-id, label: string
 }" unset="1">Automatically assigned labels.</ArgTableRow>
<ArgTableRow arg="packages" typ="multi { array-id, label: string
 }" unset="1">Installed packages.</ArgTableRow>
<ArgTableRow arg="state" typ="string">Device state.</ArgTableRow>
<ArgTableRow arg="upgrade-rule" typ="enum">Upgrade rule covering this device. The first rule in the [`/cmr/upgrade`](../upgrade) rule list that covers the device claims it, so a `labels=all` rule placed at the top covers every device.</ArgTableRow>
<ArgTableRow arg="channel" typ="alt">Current upgrade channel/version.</ArgTableRow>
<ArgTableRow arg="available-version" typ="string">Newest available upgrade.</ArgTableRow>
<ArgTableRow arg="connected-time" typ="time" unset="1">Time the device has been connected.</ArgTableRow>
<ArgTableRow arg="uptime" typ="time" unset="1">Device uptime.</ArgTableRow>
<ArgTableRow arg="disconnected-since" typ="date" unset="1">Time since the device disconnected.</ArgTableRow>
<ArgTableRow arg="alerts" typ="super { on: num
, [all] /num
, [critical]  num
, [high] /num
, [medium] /num
, [low] /num
 }">Enabled/total alert counts by severity.</ArgTableRow>
<ArgTableRow arg="serial" typ="string">Factory serial number.</ArgTableRow>
</ArgTable>
