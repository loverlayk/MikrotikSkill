# Fail-over PtMP CLI example

> This page provides a step-by-step CLI guide for configuring automatic failover between 60Ghz and 5Ghz wireless links using MikroTik RouterOS, including bridge setup, interface bonding, and W60G device connection...

# Fail-over PtMP CLI example

### Summary

This example shows how to configure an automatic fail-over (bonding) 5Ghz link in combination with 60Ghz devices in the CLI.  
When a connection between 60Ghz wireless is lost, it will automatically use the bonded interface.  
The example is done from an empty configuration state with the [[WinBox](https://mikrotik.com/download)] utility

### Connect to the device step by step

- After configuration reset - only mac-telnet is possible.
   Connect to the device by connecting to its MAC address or use WinBox New terminal to find the device MAC address of the W60G device by issuing command:

```ros
/ip/neighbor/print
```

- To connect to the W60G device, issue a command:

```ros
/tool/mac-telnet/mac-address
```

- Enter the username and password. By default the username is **admin** and the password is either blank or printed on the device sticker.

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

To check if the bridge has been created, issue a command:

```ros
admin@MikroTik] > /interface/bridge/print
Flags: X - disabled, R - running
 0 R name="bridge" mtu=auto actual-mtu=1500 l2mtu=65535 arp=enabled arp-timeout=auto mac-address=1A:7F:BB:41:B0:94 protocol-mode=rstp  fast-forward=yes igmp-snooping=no auto-mac=yes ageing-time=5m priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6  vlan-filtering=no dhcp-snooping=no
```

### Set up 60Ghz wireless connection

All previously explained steps are identical to Bridge and Station devices. When configuring the wireless interface different modes need to be used.  
  
#### For ap-bridge device

- Choose SSID, Password, frequency and choose the bridge mode option that will act as **ap-bridge** for the setup, please see the example.
- Enable W60G interface after required parameters have been set.

```ros
[admin@MikroTik] > /interface/w60g/set wlan60-1 mode=ap-bridge frequency=auto ssid=MySSID password=choosepassword isolate-stations=no
[admin@MikroTik] > /interface/w60g/print
Flags: X - disabled, R - running
0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=ap-bridge ssid="MySSID"  frequency=auto default-scan-list=58320,60480,62640,64800 password="choosepassword" tx-sector=auto put-stations-in-bridge=none isolate-stations=no
[admin@MikroTik] > /interface/w60g/enable wlan60-1 
```

#### For station devices

- Choose the same SSID, Password, and frequency as the bridge device and choose the station-bridge mode option that will act as a **station** for the setup, please see the example.
- It is possible to connect up to 8 station devices to a single AP to act as a fail-over.
- Enable the W60G interface after required parameters have been set.

```ros
[admin@MikroTik] > /interface/w60g/set wlan60-1 mode=station-bridge frequency=auto ssid=MySSID password=choosepassword isolate-stations=no
[admin@MikroTik] > /interface/w60g/print
Flags: X - disabled, R - running
0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=station-bridge ssid="MySSID" frequency=auto default-scan-list=58320,60480,62640,64800password="choosepassword" tx-sector=auto put-stations-in-bridge=bridge isolate-stations=no
[admin@MikroTik] > /interface/w60g/enable wlan60-1
```

### Set up 5Ghz wireless connection

#### For ap-bridge device

- Choose SSID, Password, frequency and choose bridge mode option that will act as a **bridge** for the setup, please see the example.
- Enable 5GHz interface after required parameters have been set.

```ros
[admin@MikroTik] > /interface/wireless/security-profiles/set [ find default=yes ] supplicant-identity=MikroTik authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key=choosepassword
[admin@MikroTik] > /interface/wireless/set wlan1 frequency=auto scan-list=default installation=outdoor mode=ap-bridge ssid=MikroTik1 channel-width=20/40/80mhz-Ceee wireless-protocol=any security-profile=default band=5ghz-a/n/ac
[admin@MikroTik] > /interface/wireless/enable wlan1 
```

#### For station devices

- Choose the same SSID, Password, frequency as the bridge device and choose the station-bridge mode option that will act as a **station** for the setup. Please see the example.
- It is possible to connect up to 8 station devices to a single AP to act as a fail-over.
- Enable the W60G interface after required parameters have been set.

```ros
[admin@MikroTik] > /interface/wireless/security-profiles/set [ find default=yes ] supplicant-identity=MikroTik authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key=choosepassword
[admin@MikroTik] > /interface/wireless/set wlan1 frequency=auto scan-list=default installation=outdoor mode=station-bridge ssid=MikroTik1 channel-width=20/40/80mhz-Ceee wireless-protocol=any security-profile=default band=5ghz-a/n/ac
[admin@MikroTik] > /interface/wireless/enable wlan1
```

### Configure bridge for Access Point

- Configure the bridge for the AP to ensure that 5ghz is working as fail-over. It is required to bridge **wlan1**, **ether1**, and all 60ghz **station interfaces**.
   *In the example it shows only 2 station devices but it is possible to add up to 8 devices.*  

   For the ap-bridge device please set **configuration** as follows:

```ros
[admin@MikroTik] > /interface/bridge/port/
add bridge=bridge hw=no interface=ether1
add bridge=bridge interface=wlan1
add bridge=bridge interface=wlan60-station-1
add bridge=bridge interface=wlan60-station-2
[admin@MikroTik] > interface/bridge/port/pr
# INTERFACE         BRIDGE  HW  PVID  PRIORITY  PATH-COST  INTERNAL-PATH-COST  HORIZON
0 ether1            bridge      no     1  0x80             10                  10  none
1 wlan1             bridge             1  0x80             10                  10  none
2 wlan60-station-1  bridge             1  0x80             10                  10  none
3 wlan60-station-2  bridge             1  0x80             10                  10  none 
```

### Configure bridge and bonding for station devices

- Configure bonding and assign slave interfaces. In this setup it is selected as the built-in wlan1 interface, but it can be also an ether interface in other kinds of setups.

   For station-bridge devices, please set **bonding** as:

```ros
[admin@MikroTik] > /interface/bonding/add mode=active-backup name=bond1 primary=wlan60-1 slaves=wlan60-1,wlan1
```

- Add interface members (ether1 and bond1) to the newly created bridge.

```ros
[admin@MikroTik] > /interface/bridge/port/add interface=ether1 bridge=bridge
[admin@MikroTik] > /interface/bridge/port/add interface=bond1  bridge=bridge
[admin@MikroTik] > /interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload
#     INTERFACE                              BRIDGE                              HW   PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
0     ether1                                 bridge                             yes     1     0x80         10                 10       none
1     bond1                                  bridge                             yes     1     0x80         10                 10       none
```

### Additional configuration

The link should be established after all previously explained steps are done. It's recommended to set up an administrator password on both devices.

### Troubleshooting

Ensure the connection is established to the correct device by checking the device settings like serial number and model name by issuing a command:

```ros
[admin@MikroTik] > /system/routerboard/print
```

If the bridge wlan60-1 interface in bridge settings is inactive and configuration is done properly  to enable the interface on a device - issue a command:

```ros
[admin@MikroTik] > /interface/w60g/enable wlan60-1
```
