# active

> Devices that are authenticated on the Dot1X server ports.

-----------

## interface/dot1x/server/active 
**Conditions:** !smips
**Type:** Directory

Devices that are authenticated on the Dot1X server ports.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum">Port of the device.</ArgTableRow>
<ArgTableRow arg="username" typ="string">Identity of the supplicant, or the MAC address for MAC authentication.</ArgTableRow>
<ArgTableRow arg="client-mac" typ="macAddr">MAC address of the device.</ArgTableRow>
<ArgTableRow arg="session-id" typ="string">Session ID, as sent to the RADIUS server in Acct-Session-Id.</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num">VLAN that the port is in as an untagged port: from the RADIUS server, or the guest, reject or server-fail VLAN.</ArgTableRow>
<ArgTableRow arg="auth-info" typ="string">How the device got access: `dot1x`, `dot1x (guest vlan)`, `dot1x (reject vlan)`, `dot1x (server fail vlan)`, `mac-auth`, `mac-auth (reject vlan)`, `mac-auth (server fail vlan)`.</ArgTableRow>
</ArgTable>
