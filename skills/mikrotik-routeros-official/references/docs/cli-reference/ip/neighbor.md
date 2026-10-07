# neighbor

> The neighbor list shows all discovered neighbors in the Layer 2 broadcast domain. It shows to which interface the neighbor is connected, its IP/MAC addresses, and other related parameters.

-----------

## ip/neighbor 
**Type:** Directory

The neighbor list shows all discovered neighbors in the Layer 2 broadcast domain. It shows to which interface the neighbor is connected, its IP/MAC addresses, and other related parameters.

The number of neighbor entries is limited to (total RAM in megabytes) * 16 per interface to avoid memory exhaustion.

```ros
[admin@MikroTik] /ip/neighbor/print 
 # INTERFACE ADDRESS         MAC-ADDRESS       IDENTITY   VERSION    BOARD      
 0 ether13   192.168.33.2    00:0C:42:00:38:9F MikroTik   5.99       RB1100AHx2
 1 ether11   1.1.1.4         00:0C:42:40:94:25 test-host  5.8        RB1000   
 2 Local     10.0.11.203     00:02:B9:3E:AD:E0 c2611-r1   Cisco I...                    
 3 Local     10.0.11.47      00:0C:42:84:25:BA 11.47-750  5.7        RB750  
 4 Local     10.0.11.254     00:0C:42:70:04:83 tsys-sw1   5.8        RB750G    
 5 Local     10.0.11.202     00:17:5A:90:66:08 c7200      Cisco I...
```

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="multi { interface: iface_enum
 }">Interface name to which the discovered device is connected. Shows both the master interface and the actual slave interface.</ArgTableRow>
<ArgTableRow arg="address" typ="alt { address4: ipAddr
, address6: ip6Addr
 }">The highest IP address configured on a discovered device.</ArgTableRow>
<ArgTableRow arg="address4" typ="ipAddr">IPv4 address configured on a discovered device.</ArgTableRow>
<ArgTableRow arg="address6" typ="ip6Addr">IPv6 address configured on a discovered device.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the remote device. Can be used to connect with mac-telnet.</ArgTableRow>
<ArgTableRow arg="identity" typ="string">Configured system identity of the discovered device.</ArgTableRow>
<ArgTableRow arg="platform" typ="string">Name of the platform, e.g. "MikroTik", "cisco".</ArgTableRow>
<ArgTableRow arg="version" typ="string">Version number of installed software on the remote device.</ArgTableRow>
<ArgTableRow arg="unpack" typ="enum (none | simple | uncompress-headers | uncompress-all) { none:0x00, simple:0x01, uncompress-headers:0x03, uncompress-all:0x07 }">The [IP packing](../../../system-information-and-utilities/ip-packing) unpacking setting that the neighbor announces. A router packs toward the neighbor only when it announces unpacking. `simple`, `uncompress-headers` and `uncompress-all` correspond to the `unpacking` values `simple`, `compress-headers` and `compress-all`.</ArgTableRow>
<ArgTableRow arg="age" typ="time">Time interval since the last discovery packet was received.</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">Uptime of the remote device. Shown only for devices with RouterOS installed.</ArgTableRow>
<ArgTableRow arg="software-id" typ="string">RouterOS software ID on the remote device. Applies only to devices with RouterOS installed.</ArgTableRow>
<ArgTableRow arg="board" typ="string">RouterBoard model. Displayed only for devices with RouterOS installed.</ArgTableRow>
<ArgTableRow arg="ipv6" typ="bool">Whether the device has IPv6 enabled.</ArgTableRow>
<ArgTableRow arg="interface-name" typ="string">Interface name on the neighbor device connected to the L2 broadcast domain. Applies to CDP.</ArgTableRow>
<ArgTableRow arg="system-description" typ="string">System description reported by the Link Layer Discovery Protocol (LLDP).</ArgTableRow>
<ArgTableRow arg="system-caps" typ="ubit (other, repeater, bridge, wlan-ap, router, telephone, docsis-cable-device, station-only)">System capabilities reported by LLDP.</ArgTableRow>
<ArgTableRow arg="system-caps-enabled" typ="ubit (other, repeater, bridge, wlan-ap, router, telephone, docsis-cable-device, station-only)">Enabled system capabilities reported by LLDP.</ArgTableRow>
<ArgTableRow arg="discovered-by" typ="ubit (cdp, lldp, mndp)">Discovery protocols through which the neighbor was discovered.</ArgTableRow>
<ArgTableRow arg="running" typ="multi { array-id, cap: string
 }" unset="1">List of features running on the neighbor device. Currently lists only the CAPsMAN feature.</ArgTableRow>
</ArgTable>
