# mac-scan

> Lists the devices that send MikroTik Neighbor Discovery (MNDP) announcements on an interface, with their MAC address and IPv4 address, to find the MAC address for MAC Telnet or MAC WinBox. A device appears whatever...

-----------

## tool/mac-scan 
**Conditions:** !smips
**Type:** Command

Lists the devices that send MikroTik Neighbor Discovery (MNDP) announcements on an interface, with their MAC address and IPv4 address, to find the MAC address for MAC Telnet or MAC WinBox. A device appears whatever its MAC server settings are; a device whose neighbor discovery is off on that interface does not appear. Without `duration`, the scan runs until you stop it. For examples, see [MAC server](../../management-tools/mac-server).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum">Interface to scan, or `all` for all interfaces.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the device.</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr">IPv4 address the device announces in neighbor discovery.</ArgTableRow>
<ArgTableRow arg="age" typ="num">Seconds since the device's last neighbor discovery announcement.</ArgTableRow>
</ArgTable>
