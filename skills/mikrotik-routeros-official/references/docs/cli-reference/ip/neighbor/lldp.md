# lldp

> This menu shows detailed LLDP type-length-values (TLVs) received from neighboring devices.

-----------

## ip/neighbor/lldp 
**Type:** Directory

This menu shows detailed LLDP type-length-values (TLVs) received from neighboring devices.

:::note
The `lldpRemTable` SNMP table reports only neighbors discovered through LLDP. Entries discovered exclusively by CDP or MNDP are excluded from the SNMP LLDP-MIB.
:::

Example output:

```ros
[admin@Switch] > /ip/neighbor/lldp/print
Columns: INTERFACE, ADDRESS4, ADDRESS6, MAC-ADDRESS, LLDP-CHASSIS-ID, LLDP-PORT-ID, LLDP-PORT-DESCRIPTION, LLDP-SYSTEM-NAME, LLDP-SYSTEM-DESCRIPTION
#  INTERFACE  ADDRESS4        ADDRESS6                   MAC-ADDRESS        LLDP-CHASSIS-ID    LLDP-PORT-ID  LLDP-PORT-DESCRIPTION  LLDP-SYSTEM-NAME  LLDP-SYSTEM-DESCRIPTION                                                     
0  ether2     192.168.88.128  fe80::f61e:57ff:fe13:d794  F4:1E:57:13:D7:94  F4:1E:57:13:D7:94  ether1        ether1                 Tested_CRS812     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS812-8DS-2DQ-2DDQ 
   bridge1                                                                                                                                                                                                                        
1  ether3     192.168.88.127  fe80::f61e:57ff:fe47:9255  F4:1E:57:47:92:55  F4:1E:57:47:92:55  ether1        ether1                 Tested_CRS520     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS520-4XS-16XQ     
   bridge1                                                                                                                                                                                                                        
2  ether4     192.168.88.9    fe80::1afd:74ff:fe81:9a    18:FD:74:81:00:9A  18:FD:74:81:00:86  ether1        ether1                 Tester6           MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CCR2216-1G-12XS-2XQ 
   bridge1                                                                                                                                                                                                                        
3  ether5     192.168.88.132  fe80::d601:c3ff:fe43:c035  D4:01:C3:43:C0:35  D4:01:C3:43:C0:35  ether1        ether1                 Tested_L009       MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 L009UiGS            
   bridge1                                                                                                                                                                                                                        
4  ether8     192.168.88.129  fe80::f61e:57ff:fec2:8a3d  F4:1E:57:C2:8A:3D  F4:1E:57:C2:8A:2B  ether17       ether17                Tested_CRS418     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS418-8P-8G-2S+    
   bridge1   
```

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="multi { interface: iface_enum
 }">Interface on which the LLDP neighbor was discovered.</ArgTableRow>
<ArgTableRow arg="address" typ="alt { address4: ipAddr
, address6: ip6Addr
 }">IPv4 or IPv6 address of the LLDP neighbor.</ArgTableRow>
<ArgTableRow arg="address4" typ="ipAddr">IPv4 address of the LLDP neighbor.</ArgTableRow>
<ArgTableRow arg="address6" typ="ip6Addr">IPv6 address of the LLDP neighbor.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the LLDP neighbor.</ArgTableRow>
<ArgTableRow arg="lldp-chassis-id-subtype" typ="enum (chassis-component | interface-alias | port-component | mac-address | network-address | interface-name | local) { chassis-component:1, interface-alias:2, port-component:3, mac-address:4, network-address:5, interface-name:6, local:7 }">Subtype of the LLDP chassis ID.</ArgTableRow>
<ArgTableRow arg="lldp-chassis-id" typ="string">LLDP chassis ID of the neighbor.</ArgTableRow>
<ArgTableRow arg="lldp-port-id-subtype" typ="enum (interface-alias | port-component | mac-address | network-address | interface-name | agent-circuit-id | local) { interface-alias:1, port-component:2, mac-address:3, network-address:4, interface-name:5, agent-circuit-id:6, local:7 }">Subtype of the LLDP port ID.</ArgTableRow>
<ArgTableRow arg="lldp-port-id" typ="string">LLDP port ID of the neighbor.</ArgTableRow>
<ArgTableRow arg="lldp-port-description" typ="string">LLDP port description of the neighbor.</ArgTableRow>
<ArgTableRow arg="lldp-system-name" typ="string">LLDP system name of the neighbor (system identity).</ArgTableRow>
<ArgTableRow arg="lldp-system-description" typ="string">LLDP system description of the neighbor.</ArgTableRow>
<ArgTableRow arg="lldp-ttl" typ="time">LLDP time-to-live value for the neighbor entry.</ArgTableRow>
<ArgTableRow arg="lldp-system-caps" typ="ubit (other, repeater, bridge, wlan-ap, router, telephone, docsis-cable-device, station-only)">LLDP system capabilities of the neighbor.</ArgTableRow>
<ArgTableRow arg="lldp-system-caps-enabled" typ="ubit (other, repeater, bridge, wlan-ap, router, telephone, docsis-cable-device, station-only)">LLDP enabled system capabilities of the neighbor.</ArgTableRow>
</ArgTable>
