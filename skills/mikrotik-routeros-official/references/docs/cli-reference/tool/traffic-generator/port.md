# port

> RouterOS directory reference for /tool/traffic-generator/port.

-----------

## tool/traffic-generator/port 
**Type:** Directory
Ports bind an interface to the traffic generator for transmitting and receiving generated packets. See the [Traffic Generator](../../../diagnostics-monitoring-and-troubleshooting/traffic-generator) guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Descriptive name of the port.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Name of the interface associated with the port. Mandatory.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="first-header" typ="enum (mac | vlan | ip | udp | raw | ipv6 | tcp) { mac:1, vlan:2, ip:3, udp:4, raw:5, ipv6:6, tcp:7 }">Suggested first header for packets sent out of this interface. Can be used when creating packet templates.</ArgTableRow>
</ArgTable>
