# PtP CLI example

> This page provides a step-by-step CLI example for configuring a transparent wireless bridge between two MikroTik W60G devices, including connecting via MAC-Telnet, setting up a bridge with interface members, and...

# PtP CLI example

### Summary

This example shows how to configure a transparent wireless bridge in CLI from one W60G device to another.

The example is done from an empty configuration state with the [[WinBox](https://mikrotik.com/download)] utility

### Connect to the device step by step

- After configuration reset - only mac-telnet is possible.
   Connect to the device by connecting to its MAC address or use WinBox New terminal to find device MAC address of the W60G device by issuing command:

```ros
/ip/neighbor/print
```

- To connect to the W60G device issue a command:

```ros
/tool/mac-telnet/mac-address
```

- Enter username and password. By default the username is **admin** and no password is set:

```ros
[admin@KD_GW] > /tool/mac-telnet C4:AD:34:84:EE:5D
Login: admin
Password:
Trying C4:AD:34:84:EE:5D...
Connected to C4:AD:34:84:EE:5D
```

### Configure bridge

- Add a new bridge and assign bridge members to it by issuing the following command:

```ros
/interface/bridge/add name=bridge
```

&emsp;&emsp;   To check if the bridge has been created, issue a command:

```ros
[admin@MikroTik] > /interface/bridge/print
Flags: X - disabled, R - running
0 R name="bridge" mtu=auto actual-mtu=1500 l2mtu=65535 arp=enabled arp-timeout=auto mac-address=1A:7F:BB:41:B0:94 protocol-mode=rstp  fast-forward=yes igmp-snooping=no auto-mac=yes ageing-time=5m priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6  vlan-filtering=no dhcp-snooping=no
```

- Add interface members (ether1 and wlan60-1) to the newly created bridge:

```ros
[admin@MikroTik] > /interface/bridge/port/add interface=ether1 bridge=bridge
[admin@MikroTik] > /interface/bridge/port/add interface=wlan60-1 bridge=bridge
[admin@MikroTik] > /interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload
#     INTERFACE                              BRIDGE                              HW   PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
0     ether1                                 bridge                             yes     1     0x80         10                 10       none
1 I   wlan60-1                               bridge                                     1     0x80         10                 10       none
```

### Set up wireless connection

All previously explained steps are identical to Bridge and Station devices. When configuring the wireless interface different modes need to be used.  
  
#### For bridge device

- Choose SSID, Password, frequency and choose bridge mode option that will act as a **bridge** for the setup, please see the example;
- Enable W60G interface after required parameters have been set:

```ros
[admin@MikroTik] > /interface/w60g/set wlan60-1 mode=bridge frequency=auto ssid=MySSID password=choosepassword put-stations-in-bridge=bridge isolate-stations=yes
[admin@MikroTik] > /interface/w60g/print
Flags: X - disabled, R - running 
0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=bridge ssid="MySSID"  frequency=auto default-scan-list=58320,60480,62640,64800 password="choosepassword" tx-sector=auto put-stations-in-bridge=bridge isolate-stations=yes
[admin@MikroTik] > /interface/w60g/enable wlan60-1
```

#### For station device

- Choose the same SSID, password, and frequency as the bridge device and choose the station-bridge mode option that will act as a **station** for the setup, please see the example;
- Enable the W60G interface after required parameters have been set:

```ros
[admin@MikroTik] > /interface/w60g/set wlan60-1 mode=station-bridge frequency=auto ssid=MySSID password=choosepassword
[admin@MikroTik] > /interface/w60g/print
Flags: X - disabled, R - running 
0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=station-bridge  ssid="MySSID" frequency=auto default-scan-list=58320,60480,62640,64800 password="choosepassword" tx-sector=auto put-stations-in-bridge=bridge isolate-stations=yes
[admin@MikroTik] > /interface/w60g/enable wlan60-1
```

### Additional configuration

The link should be established after all previously explained steps are done. It's recommended to set up administrator's password on both devices.

### Troubleshooting

Ensure the connection is established to the correct device by checking the device settings like serial number and model name by issuing a command:

```ros
[admin@MikroTik] > /system/routerboard/print
```

If the bridge wlan60-1 interface in bridge settings is inactive and the configuration is done properly  to enable the interface on a device - issue a command:

```ros
[admin@MikroTik] > /interface/w60g/enable wlan60-1 
```
