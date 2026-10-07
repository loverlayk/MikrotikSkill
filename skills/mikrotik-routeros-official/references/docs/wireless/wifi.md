# Wi-Fi 6 / 7 (802.11ax/be)

> This page introduces the WiFi configuration menu in RouterOS, covering basic setup for password-protected and OWE transition mode access points. It explains configuration profiles, security settings, and includes...

# Wi-Fi 6 / 7 (802.11ax/be)

This section covers MikroTik **Wi-Fi 6 / 6E / 7 (802.11ax/be)** devices, all configured through the shared **`/interface/wifi`** menu. Which driver package a device needs depends on its wireless chipset and standard. The same menu also covers **Wi-Fi 5 (802.11ac)** devices running the **`wifi-qcom-ac`** package.

:::tip[Is this the right section for my device?]
This menu (and this manual) is used by every device running one of these driver packages:

| Package | Devices | Examples |
| :-- | :-- | :-- |
| `wifi-qcom` | Wi-Fi 6 / 6E (Qualcomm) | wAP ax, cAP ax, hAP ax³ |
| `wifi-qcom-be` | Wi-Fi 7 (Qualcomm) | hAP be3 media |
| `wifi-mediatek` | Wi-Fi 6 / 7 (MediaTek) | hAP ax S, hAP be lite |
| `wifi-qcom-ac` | Wi-Fi 5 / 802.11ac (Qualcomm) | see [Wi-Fi 5 (802.11ac)](../wifi-ac/index.md) |

The standard is usually encoded in the model name — **ax** for Wi-Fi 6, **be** for Wi-Fi 7. For `wifi-qcom-ac` devices, see [Wi-Fi 5 (802.11ac)](../wifi-ac/index.md) to confirm whether yours should use this menu or the legacy `/interface/wireless` one.

If your device uses the legacy `/interface/wireless` menu instead, see [802.11 a/b/g/n](../abgn/index.md).
:::

:::note
In RouterOS versions before 7.13 this menu was part of a separate package called `wifiwave2`.
:::

## Getting started

New to one of these devices? Start with a task-oriented guide, then use the property reference further down this page for individual settings:

- [Configuring a standalone access point](./configuring-standalone-access-point.md)
- [Configuring a repeater](./configuring-repeater.md)
- [Configuring outdoor CPE-to-AP links](./configuring-outdoor-cpe-to-ap-links.md)
- [Interworking (802.11u / Hotspot 2.0) for WiFi6](./interworking-for-wifi6.md)
- [Centralized management with WiFi CAPsMAN](./capsman.md)

## WiFi Terminology

Before we move on let's familiarize ourselves with terms important for understanding the operation of the menu. These terms will be used throughout the article.

- **Profile** - refers to the configuration preset created under one of these WiFi sub-menus: **aaa**, **channel**, **security**, **datapath**, or **interworking**.
- **Configuration** **profile** - configuration preset defined under `/interface/wifi/configuration`, it can reference various profiles.
- **Station** - wireless client.

## Basic Configuration

The easiest way to fully configure a compatible device is through the `/interface/wifi/network` menu, which bundles SSID, security, datapath and radio settings into a single configuration entity. Alternatively, settings can be applied per-interface as shown in the examples further below.

### Network

A network applies to WiFi interfaces that match its `labels`. If `labels` are not specified, the network's configuration gets applied to all interfaces.

For an example of network configuration usage, see the following:

```ros
# Creating a network preset with SSID, security and datapath settings, which gets applied to all available interfaces
/interface/wifi/network
add ssid=MikroTik mode=ap security.authentication-types=wpa2-psk,wpa3-psk security.passphrase="strong_password" datapath.bridge=bridge1 disabled=no

# Create a network radio preset, which gets applied to the whole radio.
/interface/wifi/network/radio
add configuration.country=Latvia
```

An example with Multi-Link Operation (MLO) enabled:

```ros
/interface/wifi/network
add datapath.bridge=bridge1 disabled=no mlo=yes mode=ap security.authentication-types=wpa3-psk ssid="MikroTik" security.passphrase="strong_password"
```

| Property | Description |
| :-- | :-- |
| **mlo** (*no* \| *yes; default: **yes***) | Enables Multi-Link Operation for Wi-Fi 7. |
| **labels** (*comma-separated strings*) | Enables the network config on radios which match any of the provided labels. |
| **ssid** (*string*) | The wireless network name (ESSID). |
| **mode** (*ap* \| *station* \| *station-bridge* \| *station-pseudobridge*; default: **ap***) | Interface operation mode. |
| **disabled** (*no* \| *yes; default: **no***) | Whether the network is disabled. |

All security, authentication and encryption parameters (passphrase, WPA3/SAE, EAP, etc.) share the same properties described in [Security Properties](#security-properties). Datapath parameters (bridge, VLAN, client isolation, traffic processing) follow [Datapath Properties](#datapath-properties).

#### Network radio properties

Per-radio settings under `/interface/wifi/network/radio`:

| Property | Description |
| :-- | :-- |
| **labels** (*object*) | Matches the radio config to physical radios with the given labels. |
| **extra-labels** (*multi string*) | Additional labels for matching, extending the primary `labels` field. |
| **disabled** (*no* \| *yes; default: **no***) | Whether the radio entry is disabled. |

Radio parameters (country, band, frequency, width, chains, power, etc.) use the same properties described in [Channel Properties](#channel-properties) and [Configuration Properties](#configuration-properties).

### Basic password-protected AP

Direct per-interface setup works on every device and remains fully supported when the `/interface/wifi/network` menu is unavailable or when per-interface overrides are needed.

```ros
/interface/wifi
set wifi1 disabled=no configuration.country=Latvia configuration.ssid=MikroTik security.authentication-types=wpa2-psk,wpa3-psk security.passphrase=8-63_characters
```

### Open AP with OWE transition mode

Opportunistic wireless encryption (OWE) allows the creation of wireless networks that do not require the knowledge of a password to connect, but still offer the benefits of traffic encryption and management frame protection. It is an improvement on regular open access points.

However, since a network cannot be simultaneously encrypted and unencrypted, 2 separate interface configurations are required to offer connectivity to older devices that do not support OWE and offer the benefits of OWE to devices that do.

This configuration is referred to as OWE transition mode.

```ros
/interface/wifi
add master-interface=wifi1 name=wifi1_owe configuration.ssid=MikroTik_OWE security.authentication-types=owe security.owe-transition-interface=wifi1 configuration.hide-ssid=yes
set wifi1 configuration.country=Latvia configuration.ssid=MikroTik security.authentication-types="" security.owe-transition-interface=wifi1_owe
enable wifi1,wifi1_owe
```

With such a setting, the AP will broadcast two SSIDs →  visible `MikroTik` SSID, which should have "unencrypted" access (for legacy devices that do not support OWE), and hidden SSID `MikroTik_OWE`, which should have "OWE" security (non-password protected, but encrypted). The client devices will not see the hidden `MikroTik_OWE` SSID (in the client's WiFi list), however, the beacon packets of the visible `MikroTik` SSID will advertise the link to the hidden `MikroTik_OWE` network instead, using the "OWE Transition mode" parameter (in the beacon packet). As a result, the client devices should prioritize connecting to the "OWE" network via the `owe-transition-interface` setting.

Client devices that support OWE will prefer the OWE interface. If you don't see any devices in your registration table that are associated with the regular open AP, you may want to move on from running a transition mode setup to a single OWE-encrypted interface:

```ros
/interface/wifi
set wifi1 configuration.country=Latvia configuration.ssid=MikroTik_OWE security.authentication-types=owe
```

:::info
802.11r (fast roaming) does not work over OWE networks.
:::

### Resetting configuration

WiFi interface configurations can be reset by using the 'reset' command.

```ros
/interface/wifi/reset wifi1
```

The physical interface MAC address can be reset to default by the command 'reset-mac-address'.

```ros
/interface/wifi/reset-mac-address wifi1
```

## Configuration profiles

One of the new WiFi additions is configuration profiles. You can create various presets that can be assigned to interfaces as needed. Configuration settings for WiFi are grouped in **profiles** according to the parameter sections found at the end of this page - **aaa**, **channel**, **configuration**, **datapath**, **interworking**, and **security**, and can then be assigned to interfaces. **Configuration** **profiles** can include other profiles as well as separate parameters from other categories.

This optional flexibility is meant to allow each user to arrange their configuration in a way that makes the most sense for them, but it also means that each parameter may have different values assigned to it in different sections of the configuration.

The following priority determines which value is used:

1. Value in interface settings.
2. Value in a profile assigned to the interface.
3. Value in a configuration profile assigned to the interface.
4. Value in a profile assigned to the configuration profile (which in turn is assigned to the interface).

If you are at any point unsure of which parameter value will be used for an interface, you can issue "/interface/wifi/print detail". The print command will show all values that the interface will have, including inherited values.

To see only values that were configured directly on the interface, without displaying inherited ones, use "/interface/wifi/print config".

For an example of configuration profile usage, see the following (example for dual-band home AP):

```ros
# Creating a security profile, which will be common for both interfaces
/interface/wifi/security
add name=common-auth authentication-types=wpa2-psk,wpa3-psk passphrase="diceware makes good passwords" wps=disable
# Creating a common configuration profile and linking the security profile to it
/interface/wifi/configuration
add name=common-conf ssid=MikroTik country=Latvia security=common-auth
# Creating separate channel configurations for each band
/interface/wifi/channel
add name=ch-2ghz frequency=2412,2432,2472 width=20mhz
add name=ch-5ghz frequency=5180,5260,5500 width=20/40/80mhz
# Assigning to each interface the common profile as well as band-specific channel profile, in case of "no supported channels" message on interfaces, make sure that correct (channel) configuration is applied to each.
set wifi1 channel=ch-5ghz configuration=common-conf disabled=no
set wifi2 channel=ch-2ghz configuration=common-conf disabled=no

#"print detail" will show all values that the interface will use, including inherited ones
[admin@c52i] > /interface/wifi/print detail 
Flags: M - master; D - dynamic; B - bound; X - disabled, I - inactive, R - running 
 0 M B  default-name="wifi1" name="wifi1" l2mtu=1560 mac-address=18:FD:74:AF:F4:28 arp-timeout=auto radio-mac=18:FD:74:AF:F4:28 configuration=common-conf 
        configuration.mode=ap .ssid="MikroTik" .country=Latvia 
        security.authentication-types=wpa2-psk,wpa3-psk .passphrase="diceware makes good passwords" .wps=disable 
        channel=ch-5ghz 
        channel.frequency=5180,5260,5500 .width=20/40/80mhz 

 1 M B  default-name="wifi2" name="wifi2" l2mtu=1560 mac-address=18:FD:74:AF:F4:29 arp-timeout=auto radio-mac=18:FD:74:AF:F4:29 configuration=common-conf 
        configuration.mode=ap .ssid="MikroTik" .country=Latvia 
        security.authentication-types=wpa2-psk,wpa3-psk .passphrase="diceware makes good passwords" .wps=disable 
        channel=ch-2ghz 
        channel.frequency=2412,2432,2472 .width=20mhz 
#using "print detail config" will show only the values that were directly configured on the interface
[admin@c52i] > /interface/wifi/print detail config  
Flags: M - master; D - dynamic; B - bound; X - disabled, I - inactive, R - running 
 0 M B  default-name="wifi1" name="wifi1" l2mtu=1560 mac-address=18:FD:74:AF:F4:28 arp-timeout=auto radio-mac=18:FD:74:AF:F4:28 configuration=common-conf 
        configuration.mode=ap 
        channel=ch-5ghz 

 1 M B  default-name="wifi2" name="wifi2" l2mtu=1560 mac-address=18:FD:74:AF:F4:29 arp-timeout=auto radio-mac=18:FD:74:AF:F4:29 configuration=common-conf 
        configuration.mode=ap 
        channel=ch-2ghz 
```

:::info
`print detail` and `print detail config` can also be used on `/interface/wifi/configuration` and will work in the same manner as in `/interface/wifi/` menu.
:::

## Access List

The access list provides multiple ways of filtering and managing wireless connections.

RouterOS will check each new connection to see if its parameters match the parameters specified in any access list rule.

The rules are checked in the order they appear in the list. Only management actions specified in the first matching rule are applied to each connection.

Connections, which have been accepted by an access list rule, will be periodically checked, to see if they remain within the permitted **time, days** and **signal-range**. If they do not, they will be terminated.

:::warning
Take care when writing access list rules which reject clients. After being repeatedly rejected by an AP, a client device may start avoiding it. The VLAN ID can't be set by the access list to wifi-qcom-ac interface's clients, without configuring the pvid value for the interface first.
:::

The access list has two kinds of parameters - [filtering](#access-list), and [action](#access-list). Filtering properties are only used for matching clients, to whom the access list rule should be applied to. Action parameters can change connection parameters for that specific client and potentially overriding its default connection parameters with ones specified in the access list rule.

### MAC address authentication

Implemented through the **query-radius** action, MAC address authentication is a way to implement a centralized whitelist of client MAC addresses using a RADIUS server.

When a client device tries to associate with an AP, which is configured to perform MAC address authentication, the AP will send an access-request message to a RADIUS server with the device's MAC address as the user name and an empty password. If the RADIUS server answers with access-accept to such a request, the AP proceeds with whatever regular authentication procedure (passphrase or EAP authentication) is configured for the interface.

### Access rule examples

Only accept connections to guest network from nearby devices during business hours:

```ros
/interface/wifi/access-list/print detail
Flags: X - disabled 
 0   signal-range=-60..0 allow-signal-out-of-range=5m ssid-regexp="MikroTik Guest" time=7h-19h days=mon,tue,wed,thu,fri action=accept

 1   ssid-regexp="MikroTik Guest" action=reject 
```

Reject connections from locally-administered ('anonymous'/'randomized') MAC addresses:

```ros
/interface/wifi/access-list/print detail
Flags: X - disabled
 0   mac-address=02:00:00:00:00:00 mac-address-mask=02:00:00:00:00:00 action=reject
```

Assigning a different passphrase for a specific client can be useful, if you need to provide wireless access to a client, but don't want to share your wireless password, or don't want to create a separate SSID. When the matching client connects to this network, the access list will make that client use a different password instead of using the password defined in the interface configuration. Just make sure that the specific client doesn't get matched by a more generic access list rule first.

Or reject all unknown MAC addresses, can be added as an ultimate rule, at the end of the access list. - If you want to allow only specific clients on the network, make sure to also add a reject rule at the end of the access-list, as there is no implicit reject rule by default.

```ros
/interface/wifi/access-list
add action=accept disabled=no mac-address=22:F9:70:E5:D2:8E interface=wifi1 passphrase=StrongPassword
```

## Frequency scan

The `/interface/wifi/frequency-scan wifi1` command provides information about RF conditions on available channels that can be obtained by running the frequency-scan command. Used to approximate the spectrum usage, it can be useful to find less crowded frequencies.

![](./img/wifi-scan.png)

:::info
Running a frequency scan will disconnect all connected clients, or if the interface is in station mode, it will disconnect from the AP.
:::

## Scan command

The `/interface/wifi/scan` command will scan for access points and print out information about any APs it detects. It doesn't show the frequency usage, per channel, but it will reveal all access points that are transmitting. You can use the "connect" button to initiate a connection to a specific AP.

The scan command takes all the same parameters as the frequency-scan command.
![](./img/wifi-scan-command.png)

## Sniffer

The sniffer command enables monitor mode on a wireless interface. This turns the interface into a passive receiver for all WiFi transmissions.  
The command continuously prints out information on received packets and can save them locally to a pcap file or stream them using the TZSP protocol.

The sniffer will operate on whichever channel is configured for the chosen interface.

![](./img/wifi-sniffer.png)

## Spectral scan

The spectral scan can scan frequencies supported by your wifi interface, and plot them directly in the console.

:::info
Spectral scan is supported only by the wifi-qcom driver; it is not supported by the wifi-qcom-ac driver.
:::

```ros
/interface/wifi/spectral-scan <wifiinterface name> range=
```

![](./img/wifi-spectral-scan.png)

This command continuously monitors spectral data. This command uses the same data source as `spectral-history`, and shares many parameters.

To use spectral scan, you must use the `range=` attribute.

Each line displays one spectrogram bucket -- frequency, magnitude (dBm), peak, and a character graphic bar. A bar shows power value with ':' characters and average peak hold with '.' characters.

`data` - min/max/avg, by default average is used for data. The average should be used in most scenarios, but in some cases "min" can be useful to check if there are any frequencies that have a constant signal output on them. Max represents the strongest signal that was detected during the interval of the scan, similar to the peak.  
`duration` - terminate command after a specified time. Default is indefinite;  
`freeze-frame-interval` - Time interval at which to update command output  
`interval` - interval of how often to update the primary data values, not peak  
`peak-mode` - avg/max/disabled - peak reflects the strongest signal over peak-hold-duration. By default "avg" is used. It is the average of max values over "peak-hold-duration". If "max" is used, then the highest value will be shown until the next "peak-hold-duration" update.  
`peak-hold-duration` - changes the peak hold duration used by peak-mode, by default 5 seconds.  
`range` - scan specific range, required;  
`resolution` - frequency step for spectral scan  
`show-interference` - yes/no

Possible types of classified interference:

- Microwave oven (`MWO`).
- Continuous Wave (`CW`).
- WLAN (Wideband) (`WIFI`).
- Cordless phone 2.4 (`CORDLESS24`).
- Cordless phone 5 (`CORDLESS5`).
- Bluetooth (`BLUETOOTH`).
- Frequency hopping spread spectrum (`FHSS`).

## Spectral history

```ros
/interface/wifi/spectral-history <wifi interface name> range=
```

![](./img/wifi-spectral-history.png)

Plots a spectrogram. Power values that fall in different ranges are printed as different colored characters with the same foreground and background color, so it is possible to copy and paste the terminal output of this command.

`data` - min/max/avg, by default average is used for data. The average should be used in most scenarios, but in some cases "min" can be useful to check if there are any frequencies that have a constant signal output on them. Max will show the strongest signal that was detected, instead of the average signal.  
`interv` - interval of how often to update the data values;  
`interval` - interval at which spectrogram lines are printed;  
`duration` - terminate command after a specified time. Default is indefinite;  
`range` - scan a specific range, required;  
`resolution` - frequency step;  
`show-interference` - yes/no

Possible types of classified interference:

- Microwave oven (`O`).
- Continuous Wave (`C`).
- WLAN (Wideband)  (`W`).
- Cordless phone 2.4 (`T`).
- Cordless phone 5 (`T`).
- Bluetooth (`BB`).
- Frequency hopping spread spectrum (`F`).

## WPS

### WPS client

The wps-client command enables obtaining authentication information from a WPS-enabled AP.

```ros
/interface/wifi/wps-client/wifi1
```

### WPS server

An AP can be made to accept WPS authentication by a client device for 2 minutes by running the following command.

```ros
/interface/wifi/wps-push-button wifi1
```

## Radios

Information about the capabilities of each radio can be gained by running the `/interface/wifi/radio/print detail` command.  It can be useful to see what bands are supported by the interface and what channels can be selected. The country profile that is applied to the interface will influence the results.

```ros
/interface/wifi/radio/print detail 
Flags: L - local 
 0 L radio-mac=48:A9:8A:0B:F7:4A phy-id=0 tx-chains=0,1 rx-chains=0,1 
     bands=5ghz-a:20mhz,5ghz-n:20mhz,20/40mhz,5ghz-ac:20mhz,20/40mhz,20/40/80mhz,5ghz-ax:20mhz,
      20/40mhz,20/40/80mhz 
     ciphers=tkip,ccmp,gcmp,ccmp-256,gcmp-256,cmac,gmac,cmac-256,gmac-256 countries=all 
     5g-channels=5180,5200,5220,5240,5260,5280,5300,5320,5500,5520,5540,5560,5580,5600,5620,5640,5660,
            5680,5700,5720,5745,5765,5785,5805,5825 
     max-vlans=128 max-interfaces=16 max-station-interfaces=3 max-peers=120 hw-type="QCA6018" 
     hw-caps=sniffer interface=wifi1 current-country=Latvia 
     current-channels=5180/a,5180/n,5180/n/Ce,5180/ac,5180/ac/Ce,5180/ac/Ceee,5180/ax,5180/ax/Ce,
                 5180/ax/Ceee,5200/a,5200/n,5200/n/eC,5200/ac,5200/ac/eC,5200/ac/eCee,5200/ax...
                 ...5680/n/eC,5680/ac,5680/ac/eC,5680/ax,5680/ax/eC,5700/a,5700/n,5700/ac,5700/ax 
     current-gopclasses=115,116,128,117,118,119,120,121,122,123 current-max-reg-power=30 
```

While Radio information gives us information about supported channel width, it is also possible to deduce this information from the product page. To do so, you need to check the following parameters: **number of chains**, **max data rate**. Once you know these parameters, you need to check the modulation and coding scheme (MCS) table, for example, here: [https://mcsindex.com/](https://mcsindex.com/).

If we take hAP ax <sup>2</sup>, as an example, we can see that the number of chains is 2, and the max data rate is 1200 - 1201 in the MCS table. In the MCS table we need to find the entry for 2 spatial streams - chains, and the respective data rate, which in this case shows us that 80MHz is the maximum supported channel width.

## Registration table

`/interface/wifi/registration-table/` displays a list of connected wireless clients and detailed information about them.

![](./img/wifi-reg-table.png)

### De-authentication

Wireless peers can be manually de-authenticated (forcing re-association) by removing them from the registration table.

```ros
/interface/wifi/registration-table/remove [find where mac-address=02:01:02:03:04:05]
```

## WiFi CAPsMAN

CAPsMAN (Controlled Access Point system Manager) for the new WiFi menu lets you apply wireless settings to many MikroTik WiFi APs from a central controller. See the dedicated page: [WiFi CAPsMAN](./capsman.md).

## Advanced examples

[Enterprise wireless security with User Manager v5](../user-guides/enterprise-wireless-security-user.md)

## Replacing 'wireless' package

Some MikroTik Wi-Fi 5 APs, which ship with their interfaces managed by the 'wireless' menu, can replace the 'wireless' package with the 'wifi-qcom-ac' package to make their interfaces compatible with the 'wifi' menu instead.

To do this, it is necessary to uninstall the 'wireless' package, then install 'wifi-qcom-**ac**'.

:::info
Please note that "wifi-qcom-ac" drivers are much more resource-heavy. You will have less available RAM when using the new package and that is something to keep in mind.
:::

### Compatibility

The wifi-qcom-**ac** package includes alternative drivers for IPQ4018/4019 and QCA9984 radios that make them compatible with the WiFi configuration menu. For possible wifi-qcom-ac/wifi-qcom/wireless package combinations, please see the package types section [here](../index.md).

As a rule of thumb, the package is compatible with 802.11ac products, which have an ARM CPU. It is NOT compatible with any of our 802.11ac products which have a MIPS CPU.

| Compatibility | Devices |
| :-- | :-- |
| Compatible | Audience, Audience LTE kit, Chateau (all variants of D53), hAP ac<sup>2</sup>, hAP ac<sup>3</sup>, cAP ac, cAP XL ac, LDF 5 ac, LHG XL 5 ac, LHG XL 52 ac, NetMetal ac<sup>2</sup>, mANTBox 52 15s, wAP ac (RBwAPG-5HacD2HnD), SXTsq 5 ac |
| Incompatible | RB4011iGS+5HacQ2HnD-IN (no support for the 2.4GHz interface), Cube 60Pro ac (no support for the 60GHz interface), wAP ac (RBwAPG-5HacT2HnD) and **all other devices with a MIPSBE CPU** |

### Benefits

- WPA3 authentication and OWE (opportunistic wireless encryption).
- 802.11w standard management frame protection.
- 802.11r/k/v.
- MU-MIMO and beamforming.
- 400Mb/s maximum data rate in the 2.4GHz band for IPQ4019 interfaces.

:::info
These benefits apply both to the wifi-qcom and wifi-qcom-ac packages.
:::

### Lost features

The following notable features are lost when running 802.11ac products with drivers that are compatible with the 'wifi' management interface:

- Nstreme and Nv2 wireless protocols.
- VLAN configuration in the wireless settings (Per-interface VLANs can be configured in bridge settings).
- Compatibility with station-bridging as implemented in the 'wireless' package. Station-bridge only works between the same type of drivers. WiFi to WiFi, and [Wireless](../index.md) to Wireless.

## Property Reference

### AAA properties

Properties in this category configure an access point's interaction with AAA (RADIUS) servers.

Certain parameters in the table below take *format-string* as their value. In a *format-string*, certain characters are interpreted in the following way:

| Character | Interpretation |
| :-- | :-- |
| a | Hexadecimal character making up the MAC address of the client device in lowercase |
| A | Hexadecimal character making up the MAC address of the client device in upper case |
| i | Hexadecimal character making up the MAC address of the AP's interface in lowercase |
| I (capital 'i') | Hexadecimal character making up the MAC address of the AP's interface in upper case |
| N | The entire name of the AP's interface (e.g. 'wifi1') |
| S | The entire SSID |

All other characters are used without interpreting them in any way. For examples, see default values.

| Property | Description |
| :-- | :-- |
| **called-format** (*format-string*; *Default: **II-II-II-II-II-II:S**)* | Format for the value of the Called-Station-Id RADIUS attribute, in AP's messages to RADIUS servers. |
| **calling-format** (*format-string*; *Default: **AA:AA:AA:AA:AA:AA**)* | Format for the value of the Calling-Station-Id RADIUS attribute, in AP's messages to RADIUS servers. |
| **interim-update** (*time interval; Default: ****5m****)* | Interval at which to send interim updates about traffic accounting to the RADIUS server. |
| **mac-caching** (*time interval;* *Default: **disabled**)* | Length of time to cache RADIUS server replies, when MAC address authentication is enabled. This resolves issues with client device authentication timing out due to comparatively high latency of RADIUS server replies. |
| **name** (*string*; *Default: **no**)* | A unique name for the AAA profile. |
| **nas-identifier** (*string*) | Value of the NAS-Identifier attribute, in AP's messages to RADIUS servers. Defaults to the host name of the device (/system/identity). |
| **password-format** (*format-string*) | Format for the value to use in calculating the value of the User-Password attribute in AP's messages to RADIUS servers when performing MAC address authentication.  Default value: "" (an empty string). |
| **username-format** (*format-string*; *Default: **AA:AA:AA:AA:AA:AA**)* | Format for the value of the User-Name attribute in AP's messages to RADIUS servers when performing MAC address authentication. |

### Channel properties

Properties in this category specify the desired radio channel.

| Property | Description |
| :-- | :-- |
| **band** (*2ghz-g* \| *2ghz-n* \| *2ghz-ax*\| *2ghz-be* \| *5ghz-a* \| *5ghz-ac* \| *5ghz-an* \| *5ghz-ax* \| *5ghz-be*\| *6ghz-ax* \| *6ghz-be*) | Frequency band and wireless standard that will be used by the AP. Defaults to newest supported standard. **Note that band support is limited by radio capabilities.**  |
| **deprioritize-unii-3-4** (*no* \| *yes*) | Whether to assign lower priority to channels with a control frequency of 5720 or 5825-5885 MHz. These channels are unsupported by some client devices, making their automatic selection undesirable. Defaults to 'yes' in ETSI regulatory domains, elsewhere to 'no'.  |
| **frequency** (*list of numbers or number ranges*) | For an interface in AP mode, specifies frequencies (in MHz) to consider when picking control channel center frequency.  For an interface in station mode, specifies frequencies on which to scan for APs.  Leave unset (default) to consider all frequencies supported by the radio and permitted by the applicable regulatory profile.  The parameter can contain 1 or more comma-separated values of decimal numbers or, optionally, ranges of numbers denoted using the syntax RangeBeginning-RangeEnd:RangeStep  Examples of valid channel.frequency values: 24122412,2432,24725180-5240:20,5500-5580:20 |
| **preamble-puncturing** (*no \| yes; Default: **no***) |  Enables puncturing support on this interface for DFS/radar (802.11be only).  When set, the access point may disable ("puncture") only the affected 20 MHz part of a wide 80/160 MHz channel when  radar signal presence is detected, instead of switching the whole channel.  For 80 MHz channels a single 20 MHz sub-channel may be punctured.  For 160 MHz channels either one 20 MHz sub-channel or one 40 MHz block may be punctured.    The current puncturing state can be observed in `/interface/wifi/monitor` output for this interface,  where punctured sub-channels are marked with the letter `o`.  |
| **reselect-interval** (*time interval; Default: **disabled***) | Specifies the interval when the interface should run "rescan channel availability" and select the most appropriate one to use. Specifying the interval will allow the system to select this interval dynamically and randomly. This helps to avoid a situation when many APs at the same time scan the network, select the same channel, and prefer to use it at the same time. reselect-interval uses a background scan.  The reselect process will choose the most suitable channel considering the number of networks in the channel, channel usage, and overlap with networks in adjacent channels. It can be used with a list of frequencies defined, or with `frequency` not set - using all supported frequencies.  Example: 01:00..01:30 → Would set the rescan of channels to run every 1 hour + random time up to 30 minutes. The first time, it could run a rescan after "1 hour and 15 minutes", later, it could be "1 hour and 1 second", then, it could be "1 hour, 29 minutes and 59 seconds" ...at random, a rescan will happen between every 1 hour and 1 hour 30 minutes. |
| **reselect-time** (*time interval; Default: **disabled***) | Specifies the clock time when the interface should run "rescan channel availability" and select the most appropriate one to use. Specifying the clock time will allow the system to select this time dynamically and randomly. This helps to avoid a situation when many APs at the same time scan the network, select the same channel, and prefer to use it at the same time. reselect-time uses a background scan.  The reselect process will choose the most suitable channel considering the number of networks in the channel, channel usage, and overlap with networks in adjacent channels. It can be used with a list of frequencies defined, or with `frequency` not set - using all supported frequencies.  Example: 01:00..01:30 → Would set the rescan of channels to run every night, once, randomly, between 01:00 AM and 01:30 AM, system clock time.14:00..14:30 → Would set the rescan of channels to run every day (after midday), once, randomly between 14:00:00 and 14:30:00 (or 2 PM to 2:30 PM), system clock time. |
| **secondary-frequency** (*list of integers* \| *Default: **disabled***) | For split 80+80MHz channels, specifies permitted center frequencies for the secondary 80MHz segment.  For 320MHz channels, specifies permitted 320MHz channel centers.  When unset (default), does not limit channel selection.  E.g.  'width=20/40/80+80mhz frequency=5180' would allow combining channel 42 with any other supported 80MHz channel. 'width=20/40/80+80mhz frequency=5180 secondary-frequency=5530' would only allow combining channels 42 and 106.  'width=20/40/80/160/320mhz frequency=6115' would allow use of either channel 31 or 63.  'width=20/40/80/160/320mhz frequency=6115 secondary-frequency=6265' allows use of only channel 63.  Refer here for lists of valid [5GHz](https://en.wikipedia.org/wiki/List_of_WLAN_channels#5_GHz_(802.11a/h/n/ac/ax/be)) and [6GHz](https://en.wikipedia.org/wiki/List_of_WLAN_channels#6_GHz_(802.11ax_and_802.11be)) channels. |
| **skip-dfs-channels**  (*10min-cac* \| *all* \| *disabled; Default: **disabled***) | Whether to avoid using channels, on which channel availability check (listening for presence of radar signals) is required. 10min-cac - interface will avoid using channels, on which 10 minute long CAC is requiredall - interface will avoid using all channels, on which CAC is requireddisabled  - interface may select any supported channel, regardless of CAC requirements |
| **width** ( *20mhz* \| *20/40mhz* \| *20/40mhz-Ce* \| *20/40mhz-eC* \| *20/40/80mhz* \| *20/40/80+80mhz* \| *20/40/80/160mhz*\| *20/40/80/160/320mhz*) | Width of radio channel. Defaults to widest channel supported by the radio hardware. |

### Configuration properties

This section includes properties relating to the operation of the interface and the associated radio.

| Property | Description |
| :-- | :-- |
| **antenna-gain** (*integer 0..30*) | Overrides the default antenna gain. The *master* interface of each radio sets the antenna gain for every interface which uses the same radio.  This setting cannot override the antenna gain to be lower than the minimum antenna gain of a radio. No default value.  |
| **beacon-interval** (*time interval 100ms..1s; default: **100ms***) | Interval between beacon frames of an AP. 🛈 **Important:** The 802.11 standard defines beacon interval in terms of *time units* (1 TU = 1.024 ms). The actual interval between beacons will be 1 TU for every 1 ms configured.  ⚠️ **Warning:** Every AP running on the same radio (i.e. a master AP and all its 'virtual'/'slave' APs) must use the same beacon interval.  |
| **chains** (*list of integer 0..7* ) | [Radio chains](https://en.wikipedia.org/wiki/RF_chain) to use for receiving signals. Defaults to all chains available to the corresponding radio hardware. |
| **country** (*name of a country; default: **Latvia***) | Determines which regulatory domain restrictions are applied to an interface. ⚠️ **Warning:** It is important to set this value correctly to comply with local regulations and ensure interoperability with other devices.   In a controlled environment or if you have a special permission to use it in your region, you can select `country=Superchannel` (with this country profile, router's Tx output power will not be restricted by the software, and the router will output as much power as its hardware chip allows, unless manual `tx-power` is configured to lower it). Does not work for **wifi-qcom-ac** drivers. |
| **distance** () | Maximum link distance in kilometers, needs to be set for long-range outdoor links. The value should reflect the distance to the AP or station that is furthest from the device. Unconfigured value allows usage of 2 km links. ⚠️ **Warning:** `distance` is not used by the wifi-qcom-ac package. Setting `distance` above the actual needed value can have detrimental effects on throughput and latency.  |
| **dtim-period** (*integer 1..255; default: **1***) | DTIM is a part of the beacon frame that informs power saving (sleeping) stations about incoming multicast and broadcast traffic.  The setting configures a period at which to transmit multicast or broadcast traffic, when there are client devices in power save mode connected to the AP. Expressed as a multiple of the beacon interval (e.g. with default values `dtim-period=1` and `beacon-interval=100ms`, it is sent every 1 x 100 ms = 100 ms).  Higher values enable client devices to save more energy, but increase network latency. Lower values enable clients to wake up more often, using more energy. |
| **hide-ssid** (*no \| yes; default: **no***) | yes - AP does not include its SSID in beacon frames, and does not reply to probe requests that have broadcast SSID.no - AP includes its SSID in the beacon frames, and replies to probe requests that have broadcast SSID. |
| **hw-protection-mode** (*cts-to-self* \| none \| *rts-cts)* | To reduce frame collisions, you can use: cts-to-self  - Interface sends CTS frame to own address before transmitting an MPDU (to notify nearby devices to hold off talking over each other);none  - Interface does not use any hardware protection mechanism;rts-cts - Interface sends an RTS frame before each MPDU (RTS is followed by a CTS from a receiver and the communication happens after that - both RTS and CTS frames can hold off other devices); Default (unset): interface sends RTS frames before re-transmitted MPDUs. |
| **installation** (*indoor*\|*outdoor*; *default*: **indoor**) | Devices installed outdoors will avoid use of indoor-only radio channels. |
| **manager** (*capsman* \|*capsman-or-local* \| *local*; default: **local**) | capsman - the interface will act as CAP only; this option should **not** be passed via provisioning rules to the CAP  capsman-or-local - the interface will get configuration via CAPsMAN or use its own, if `/interface/wifi/cap` is not enabled.  local - interface won't contact CAPsMAN in order to get configuration. |
| **max-clients** (*integer 1..1000; default: **1000**)* | Maximum number of associated clients. |
| **mode** (*ap* \| *station*) | Interface operation mode ap (default) - interface operates as an access pointstation - interface acts as a client device, scanning for access points advertising the configured SSIDstation-bridge - interface acts as a client device and enables support for a 4-address frame format, so that the interface can be used as a bridge portstation-pseudobridge - the interface keeps track of outgoing IP connections and performs MAC address translation similarly to how IP masquerading works🛈  **Important:** The 'wifi' station-bridge mode is incompatible with APs running the older 'wireless' package and vice versa.     |
| **multicast-enhance** (*enabled*\| *disabled; default: **disabled***) | With the multicast-enhance feature enabled, an AP will convert every multicast-addressed IP or IPv6 packet into multiple unicast-addressed frames for each connected station. This may improve link throughput and reliability since, unlike multicast frames, unicasts are acknowledged by stations and transmitted using a higher data rate. |
| **qos-classifier** (*dscp-high-3-bits*\| *priority; default: **priority***) | Specify which WMM ruleset to follow. APs and clients classify packets based on the priority assigned to them (as per WMM specification) → 1,2 - background; 0,3 - best effort; 4,5 - video; 6,7 - voice. "Better" access category has a higher probability of getting access to medium (e.g. voice frames will have a shorter "back off" time after medium becomes "idle", ensuring that they are more likely to be sent out sooner than "worse" category frames). dscp-high-3-bits - interface will transmit data packets using a WMM priority equal to the value of the 3 most significant bits of the IP DSCP fieldpriority - interface will transmit data packets using a WMM priority equal to that set by IP firewall or bridge filter🛈  **Important:** 802.11ac wireless chipsets do not support the dscp-high-3-bits classifier mode. For 802.11ac interfaces, please see [DSCP from priority](../../bridging-and-switching/user-guides/wmm-and-vlan-priority.md#set-vlan-or-wmm-priority-from-dscp).     |
| **ssid** *(string; default: **no**)* | The name of the wireless network, aka the (E)SSID. |
| **station-roaming** *(no \| yes; Default: **no**)* | The Wifi interface running in station or station-bridge mode will periodically scan for AP candidates to roam to. The weaker the signal to the AP is, the more often the scan will be performed. If an AP with a better signal is found, the station will roam to it. FT is supported, and the station will respond to BSS Transition Request if `steering.wnm` is enabled. |
| **tx-chains** (*list of integer 0..7*) | [Radio chains](https://en.wikipedia.org/wiki/RF_chain) to use for transmitting signals. Defaults to all chains available to the corresponding radio hardware. |
| **tx-power** (*integer 0..40*) | A limit on the transmit power (in dBm) of the interface. Can not be used to set power above limits imposed by the regulatory profile. Unset by default. |

### Datapath properties

Parameters relating to forwarding packets to and from wireless client devices.

| Property | Description |
| :-- | :-- |
| **bridge** (*bridge interface*) | Bridge interface to add interface to, as a bridge port. Virtual ('slave') interfaces are by default added to the same bridge, if any, as the corresponding master interface. Master interfaces are not by default added to any bridge. |
| **bridge-cost** (*integer; default: **10***) | Bridge port cost to use when adding as bridge port. |
| **bridge-horizon** (*none* \| *integer; default: **none**)* | Bridge horizon to use when adding as bridge port. |
| **client-isolation** (*no* \| *yes; default: **no***) | Determines whether client devices connecting to this interface are (by default) isolated from others or not. This policy can be overridden on a per-client basis using access list rules, so an AP can have a mixture of isolated and non-isolated clients. Traffic from an isolated client will not be forwarded to other clients and unicast traffic from a non-isolated client will not be forwarded to an isolated one. |
| **interface-list** (*interface list; default: **no***) | List to which to add the interface as a member. |
| **traffic-processing** (*on-cap \| on-capsman \| on-capsman-secure*) | 🛈  **Important:** This setting is only available starting with **7.21beta2** version.  <code>on-cap</code>, will make it so that the CAP itself is responsible for handling all WiFi traffic (same as any standalone AP would);<code>on-capsman</code>, will make it so that the CAP's WiFi traffic is forwarded to a pseudo-tunnel to the CAPSMAN and the CAPsMAN becomes responsible for CAP's traffic handling;<code>on-capsman-secure</code>, will make it so that the CAP's WiFi traffic is forwarded to an encrypted pseudo-tunnel to the CAPSMAN and the CAPsMAN becomes responsible for CAP's traffic handling. 🛈  **Important:** When using `traffic-processing=on-capsman` setting, be aware that since all the CAP's WiFi traffic now gets handled by the CAPsMAN (gets pushed into the CAPsMAN), it will increase CAPSMAN's resource consumption (CPU and RAM usage).     |
| **vlan-id** (none \| integer 1..4095; default: **none**) | Default VLAN ID to assign to client devices connecting to this interface (only relevant to interfaces in AP mode). When a client is assigned a VLAN ID, traffic coming from the client is automatically tagged with the ID and only packets tagged with this ID are forwarded to the client.  ⚠️ **Warning:** 802.11ac chipsets do not support this type of VLAN tagging, but they can be [configured](../../bridging-and-switching/index.md#vlan-example-trunk-and-access-ports) as VLAN access ports in bridge settings.  |

### Security Properties

Parameters relating to authentication.

| Property | Description |
| :-- | :-- |
| **authentication-types** (*list of wpa-psk, wpa2-psk, wpa2-psk-sha2, wpa-eap, wpa2-eap, wpa3-psk, owe, wpa3-eap, wpa3-eap-192*) | Authentication types to enable on the interface.  The default value is an empty list (no authentication, an open network).  Configuring a passphrase adds to the default list the *wpa2-psk* authentication method (if the interface is an AP) or both *wpa-psk* and *wpa2-psk* (if the interface is a station).  Configuring an *eap-username* and an *eap-password* adds to the default list the *wpa-eap and wpa2-eap* authentication methods. |
| **beacon-protection** (*disabled*\| *enabled*) | Whether to enable beacon integrity protection. Support depends on 'beacon-protection' radio capability.  Enabled by default for 802.11be interfaces. |
| **connect-group** ( *string*) | APs within the same connect group do not allow more than 1 client device with the same MAC address. This is to prevent malicious authorized users from intercepting traffic intended for other users ('MacStealer' attack) or performing a denial of service attack by spoofing the MAC address of a victim.  Handling of new connections with duplicate MAC addresses depends on the connect-priority of AP interfaces involved.  By default, all APs are assigned the same connect-group. |
| **connect-priority** (accept-priority/hold-priority (*integers*)) | These parameters determine how a connection is handled if the MAC address of the client device is the same as that of another active connection to another AP. If (accept-priority of AP2) < (hold-priority of AP1), a connection to AP2 will cause the client to be dropped from AP1. If (accept-priority of AP2) = (hold-priority of AP1), a connection to AP2 will be allowed only if the MAC address can no longer be reached via AP1. If (accept-priority of AP2) > (hold-priority of AP1), a connection to AP2 will not be accepted.  If omitted, hold-priority is the same as accept-priority. By default, APs, which perform user authentication, have higher priority (lower integer value), than open APs. |
| **dh-groups** (*list of 19, 20, 21*) | Identifiers of [elliptic curve cryptography groups](http://www.iana.org/assignments/ipsec-registry/ipsec-registry.xhtml#ipsec-registry-10) to use in SAE (WPA3) authentication. |
| **disable-pmkid** (*no* \| *yes; default: **no***) | For interfaces in AP mode, disables inclusion of a PMKID in EAPOL frames. Disabling PMKID can cause compatibility issues with client devices that make use of it.yes - Do not include PMKID in EAPOL frames.no  - Include PMKID in EAPOL frames. |
| **eap-accounting** (*no* \| *yes; default: **no***) | Send accounting information to RADIUS server for EAP-authenticated peers. ⚠️ **Warning:** Properties related to EAP are only relevant to interfaces in station mode. APs delegate (passthrough) EAP authentication to the RADIUS server.  |
| **eap-anonymous-identity** (*string; default: **none***) | Optional anonymous identity for EAP outer authentication. |
| **eap-certificate-mode** (*dont-verify-certificate* \| *no-certificates* \| *verify-certificate* \| *verify-certificate-with-crl; default: **dont-verify-certificate***) | Policy for handling the TLS certificate of the RADIUS server. verify-certificate - require server to have a valid certificate. Check that it is signed by a trusted certificate authority.dont-verify-certificate - Do not perform any checks on the certificate.no-certificates - Attempt to establish the TLS tunnel by performing anonymous Diffie-Hellman key exchange. To be used if the RADIUS server has no certificate at all.verify-certificate-with-crl - Same as verify-certificate, but also checks if the certificate is valid by checking the Certificate Revocation List. |
| **eap-methods** (*list of* *peap, tls, ttls*) | EAP methods to consider for authentication. Defaults to all supported methods. |
| **eap-password** (*string; default: **none***) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | Password to use, when the chosen EAP method requires one. |
| **eap-tls-certificate** (*certificate; *default: **none***)* | Name or id of a certificate in the device's certificate store to use, when the chosen EAP authentication method requires one. |
| **eap-username** (*string; *default: **none***)* | Username to use when the chosen EAP method requires one. ⚠️ **Caution:** Take care when configuring encryption ciphers.  All client devices MUST support the group encryption cipher used by the AP to connect, and some client devices (notably, Intel® 8260) will also fail to connect if the list of unicast ciphers includes any they don't support.  |
| **encryption** (*list of  ccmp, ccmp-256, gcmp, gcmp-256, tkip; default: **ccmp***) | A list of ciphers to support for encrypting unicast traffic.  Defaults to *ccmp*. ⚠️ **Warning:** For a client device to successfully roam between 2 APs, the APs need to be managed by the same instance of RouterOS. For information on how to centrally manage multiple APs, see [CAPsMAN](./capsman.md)  |
| **ft** (*no \| yes: default: **no***) | Whether to enable 802.11r fast BSS transitions (roaming). |
| **ft-mobility-domain** (*integer 0..65535; default: **44484 (0xADC4)***) | The fast BSS transition mobility domain ID. |
| **ft-nas-identifier** (string of *2..96 hex characters*) | Fast BSS transition PMK-R0 key holder identifier. Default: MAC address of the interface. |
| **ft-over-ds** (*no* \| *yes; *default: **no****) | Whether to enable fast BSS transitions over DS (distributed system). |
| **ft-preserve-vlanid** (*no* \| *yes* ) | no - when a client connects to this AP via 802.11r fast BSS transition, it is assigned a VLAN ID according to the access and/or interface settingsyes (default) - when a client connects to this AP via 802.11r fast BSS transition, it retains the VLAN ID, which it was assigned during initial authentication The default behavior is essential when relying on a RADIUS server to assign VLAN IDs to users, since a RADIUS server is only used for initial authentication.  Not supported by **wifi-qcom-ac** drivers. |
| **ft-r0-key-lifetime** (*time interval 1s..6w3d12h15m; Default: **600000s (~7 days)***) | Lifetime of the fast BSS transition PMK-R0 encryption key. |
| **ft-reassociation-deadline** (*time interval 0..70s; default: **20s***) | Fast BSS transition reassociation deadline. |
| **group-encryption** (*ccmp* \| *ccmp-256* \| *gcmp* \| *gcmp-256* \| *tkip; default: **ccmp***) | Cipher to use for encrypting multicast traffic. |
| **group-key-update** (*time interval; default: **24 hours***) | The interval at which the group temporal key (key for encrypting broadcast traffic) is renewed. |
| **management-encryption** (*cmac* \| *cmac-256* \| *gmac* \| *gmac-256; default: **cmac***) | Cipher to use for encrypting protected management frames. |
| **management-protection** (*allowed* \| *disabled* \| *required*) | Whether to use 802.11w management frame protection. **Incompatible with management frame protection in standard wireless package**.  The default value depends on the value of the selected authentication type. WPA2 allows the use of management protection, WPA3 requires it. |
| **multi-passphrase-group** (*string*) | Name of `/interface/wifi/security/multi-passphrase/` group that will be used. Only a single group can be defined under the security profile. |
| **owe-transition-interface** (*interface* \| *auto*) | Name of an interface whose MAC address and SSID to advertise as the matching AP when running in OWE transition mode.  Setting the value to 'auto' will make RouterOS try to automatically match open and OWE APs on the same radio.  Required for setting up open APs that offer OWE, but also work with older devices that don't support the standard. See [configuration example above](#basic-configuration). |
| **passphrase** (*string of up to 63 characters*) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | The passphrase to use for PSK authentication types. Defaults to an empty string - "".  WPA-PSK and WPA2-PSK authentication requires a minimum of 8 chars, while WPA3-PSK does not have a minimum passphrase length. |
| **sae-anti-clogging-threshold** (*disabled* \| *integer; default: **5***) | Due to SAE (WPA3) associations being CPU resource intensive, overwhelming an AP with bogus authentication requests makes for a feasible denial-of-service attack.  This parameter provides a way to mitigate such attacks by specifying a threshold of in-progress SAE authentications, at which the AP will start requesting that client devices include a cookie bound to their MAC address in their authentication requests. It will then only process authentication requests that contain valid cookies. |
| **sae-max-failure-rate** (*disabled* \| *integer; default: **40***) | Rate of failed SAE (WPA3) associations per minute, at which the AP will stop processing new association requests. |
| **sae-pwe** (*both* \| *hash-to-element* \| *hunting-and-pecking; default: **both***) | Methods to support for deriving SAE password element. |
| **wps** (*disabled* \| *push-button; default: **push-button***) | push-button - AP will accept WPS authentication for 2 minutes after the 'wps-push-button' command is called. Physical WPS button functionality is not yet implemented.disabled - AP will not accept WPS authentication |

### Security multi-passphrase properties

`/interface/wifi/security/multi-passphrase`

`multi-passphrase` allows the use of PPSK - private pre-shared keys.
It can be used by creating an access list entry and setting `multi-passphrase-group` name, or by assigning the group to a security profile that the interface uses.

The total limit of supported passphrases is 10000. The limit is shared between all interfaces. When the interface has an associated multi-passphrase group, upon being enabled it will start caching all passphrases from the specified group. While caching is taking place, the authentication will be slower. Once caching is completed, there will be no perceptible added delay due to the use of a multi-passphrase group.

If an access-list is used to apply `multi-passphrase-group`, the caching will start upon the first match for the group, and will continue until a match for the passphrase is found.

If there are thousands of entries for possible passphrases under a single group - it might take a few minutes for caching to complete, depending on device configuration and model.

:::info
multi-passphrase is not supported for the WPA3-PSK authentication type.
:::

| Property | Description |
| :-- | :-- |
| **group** (*string*) | assigning the group to a security profile or an access list will enable use of all passphrases defined under it |
| **passphrase** (*string of up to 63 characters*) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | The passphrase to use for PSK authentication types. Multiple users can use the same passphrase.  Not compatible with WPA3-PSK. |
| **vlan-id** (*integer 0..4095; Default: **none***) | vlan-id that will be assigned to clients using this passphrase   ⚠️ **Caution:** Only supported on wifi-qcom interfaces. If wifi-qcom-ac AP has a client that uses a passphrase with an associated vlan-id, the client will not be able to join. |
| **expires** (*date and time*; "YYYY-MM-DD HH:SS") | The expiration date and time for the passphrase specified in this entry doesn't affect the whole group. Once the date is reached, existing clients using this passphrase will be disconnected, and new clients will not be able to connect using it. If not set, the passphrase can be used indefinitely. |
| **isolation** (*yes* \| *no*; Default: **no**) | Determines whether the client device using this passphrase is isolated from other clients on the AP. Traffic from an isolated client will not be forwarded to other clients and unicast traffic from a non-isolated client will not be forwarded to an isolated one. |
| **disabled** (*yes* \| *no*; Default: **no**) |  |

### Steering properties

:::info
Unsolicited 802.11v BSS transition management request functionality is supported starting with 7.21.
:::

Properties in this category govern mechanisms for advertising potential roaming candidates to client devices.

| Property | Description |
| :-- | :-- |
| **2g-probe-delay**(*no* \| *yes*; Default: *no*) | If This property is set to yes on a 2.4GHz AP andsaid AP is in a steering neighbor group with at least one 5GHz AP then the 2.4GHz AP will forego responding to the first 3 probe requests from each client in a 60 second interval which have a signal-to-noise ratio of > 35 dB.  |
| **neighbor-group** (*string*) | When sending neighbor reports and BSS transition management requests, an AP will list all other APs within its neighbor group as potential roaming candidates.  By default, a dynamic neighbor group is created for each set of APs with the same SSID and authentication settings. APs operating in the 5GHz band are indicated to be preferable to ones operating in the 2.4GHz band.  A dynamic neighbor group will not be created if EAP is used; it needs to be defined manually.    |
| **rrm** (*no* \| *yes; Default: **yes***) | Enables sending of 802.11k neighbor reports.  The client may request the "neighbor report" from the AP, when the device wants to "explore/map" its surroundings (the client device can store the report, and it can use it to roam at once or later). |
| **transition-threshold** (*integer; Default: **-80***) | Sets an RSSI threshold for sending unsolicited 802.11v BSS transition management requests. If the client device sits "below" the configured threshold for the duration of `transition-threshold-time`, it gets marked as a "transition candidate". |
| **transition-threshold-time** (*time interval; Default: **10***) | Defines a time, in seconds, for how long the client device can sit "below" the configured `transition-threshold` value, to be marked as "transition candidate". |
| **transition-request-period** (*time interval; Default: **30***) | Defines an interval in seconds, using which, the AP will send unsolicited 802.11v BSS transition management requests to the client device, if it is a "transition candidate".  E.g., using the default value (30s), a request will be sent to the client every 30 seconds for `transition-request-count` number of total requests. |
| **transition-request-count** (*count, unlimited; Default: **3***) | Defines how many unsolicited 802.11v BSS transition management requests should be sent out to the client marked as a "transition candidate". One request is sent out immediately after the client gets "transition candidate" status ("-1" count), and the remaining "count" will be sent every `transition-request-period`.  E.g., using the default value (3), the 1st request gets sent when a client gets "transition candidate" status; the second request gets sent after `transition-request-period` seconds and the third (last one), after another `transition-request-period`.  Set to `unlimited` if you want to send requests without a count limit. |
| **transition-time** (*time interval, immediate \| unlimited; Default: **unlimited***) | Defines the time, for how long the client device can be a "transition candidate" before it gets forcefully deauthenticated. It can be a `time interval` in seconds (to deauthenticate the client after the time, which starts running/counting as soon as the device becomes a "transition candidate", expires), it can be `immediate` (to instantly deauthenticate the client after it becomes a "transition candidate") or `unlimited` (to never force the client and to continue sending transition requests for the `transition-request-count` amount, every `transition-request-period` seconds). 🛈  **Important:** Note that with `transition-time=immediate`, `transition-request-period` and `transition-request-count` become useless, as the client will get deauthenticated instantly after `transition-threshold-time`.     |
| **wnm** (*no* \| *yes; Default: **yes***) | Enables sending of solicited 802.11v BSS transition management requests.  A client may request a "roaming suggestion" packet that contains "neighbor list", to help the device switch APs. The client device may accept the suggestion and roam at once, or it can ignore the suggestion and keep its current connection. |

:::info
Please understand that **the client can ignore BSS transition management requests**. BSS transition request is a "suggestion" for the client to look for other-better signal APs. After receiving the transition request, it is 100% up to the client to decide whether it wants to switch APs or whether it wants to stay connected to the current AP.
:::

:::info
**Solicited 802.11v BSS transition management request behaviour:**

A solicited 802.11v BSS transition management packet is sent to the client, per the client's own request. The client device "asks" the AP to provide a "roaming suggestion" (with a "neighbor list") and the AP responds with a transition request (containing the "neighbor list").
:::

:::info
**Unsolicited 802.11v BSS transition management request behaviour:**

An unsolicited 802.11v request is sent to the client, without waiting for the client to request it. The request gets sent, even if the client was not asking for it.

If the client's signal gets below `transition-threshold` (default value: -80 dBm) for longer than `transition-threshold-time` (default value: 10 s), then the client gets marked as a "transition candidate". If the client's signal gets above the `transition-threshold`, then the client's "transition candidate" status gets removed.

If the client is a "transition candidate", then it will start receiving **unsolicited 802.11v BSS transition management request** packets (packets "suggesting" to move to other nearby APs). The first such packet will be sent immediately after the client's status changes to the "transition candidate", and the follow-up packets will be sent every `transition-request-period` (default value: 30 s). The `transition-request-count` (default value: 3) number of transition requests will be sent out in total, after which, the AP will stop suggesting the transition (unless `transition-request-count=unlimited` is configured, which makes the AP send out requests non-stop, one request every `transition-request-period`). After the `transition-request-count` number runs out, the client will get the next transition request either after the client requests it itself, or after the client gets unmarked and marked as a "transition candidate" again.

The value in `transition-time` defines for how long the client device can stay as a "transition candidate", before it gets forcefully disconnected. Possible `transition-time` values: **unlimited** (to continue sending transition requests using `transition-request-period` for the amount of `transition-request-count` and to never forcefully deauthenticate the client), **configurable time** in seconds (to continue sending transition requests using the `transition-request-period` interval and `transition-request-count` number, and then to disconnect the client after the configured `transition-time` has run out), and **immediate** (to send a transition request to the client, when it becomes a "transition candidate", and to instantly disconnect it).
:::

### Miscellaneous properties

| Property | Description |
| :-- | :-- |
| **arp** (*disabled* \| *enabled* \| *local-proxy-arp*  \| *proxy-arp* \| *reply-only; default: **enabled**)* | Address Resolution Protocol mode:disabled - the interface will not use ARPenabled - the interface will use ARPlocal-proxy-arp - the router performs proxy ARP on the interface and sends replies to the same interfaceproxy-arp - the router performs proxy ARP on the interface and sends replies to other interfacesreply-only - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the  ARP table. No dynamic entries will be automatically stored in the ARP table. Therefore for communications to be successful, a valid static entry must already exist. |
| **arp-timeout** (*time interval* \| *'auto'; default: **30s***) | Determines how long a dynamically added ARP table entry is considered valid since the last packet was received from the respective IP address. Value *auto* equals the value of*arp-timeout* in*`/ip/settings`*, which defaults to 30s. |
| **disable-running-check** *(no* \| *yes; default: **no***) | yes - interface's running property will be true whenever the interface is not disabledno - interface's running property will only be true when it has established a link to another device |
| **disabled** *(no \| yes; default: **yes**)* |  |
| **mac-address** (*MAC*) | MAC address (BSSID) to use for an interface.  Hardware interfaces default to the MAC address of the associated radio interface.  Default MAC addresses for virtual interfaces are generated by Taking the MAC address of the associated master interfaceSetting the second-least-significant bit of the first octet to 1, resulting in a locally administered MAC addressIf needed, incrementing the last octet of the address to ensure it doesn't overlap with the address of another interface on the device |
| **mtu** *(integer [32..2290]; Default: **1500**)* | Layer 3 Maximum transmission unit. |
| **mld-interface** (*interface; default: **none***) | Specifies the affiliated MLD (Multi-Link Device) interface. When two or more wifi interfaces are assigned the same MLD interface (e.g. *mld-interface=mld1*), they operate together as a single logical AP MLD, enabling Multi-Link Operation (MLO). The MLD interface is the logical data forwarding point — traffic is handled at the MLD interface level rather than on the individual affiliated WiFi interfaces. All affiliated WiFi interfaces must share the same SSID, and all participating radios must belong to the same device. MLO requires compatible Wi-Fi 7 (802.11be) hardware. |
| **mld-name** (*string*) | A unique identifier that designates this interface as an MLD interface. Must be unique and explicitly set when creating an MLD interface manually. |
| **l2mtu** *(integer [32..2290]; Default: **2290**)* | Layer 2 Maximum transmission unit. |
| **master-interface** (*interface; default: **none***) | Multiple interface configurations can be run simultaneously on every wireless radio.  Only one of them determines the radio's state (whether it is enabled, what frequency it's using, etc). This 'master' interface is *bound* to a radio with the corresponding *radio-mac.*  To create additional ('virtual') interface configurations on a radio, they need to be *bound* to the corresponding master interface. |
| **name** (*string*) | A name for the interface. Defaults to *wifiN*, where *N* is the lowest integer that has not yet been used for naming an interface. |

### Read-only properties

| Property | Description |
| :-- | :-- |
| **bound** (*boolean*) (B) | True for *master* interfaces that are currently available for WiFi manager.  True for a virtual interface (configurations linked to a master interface) when both the interface itself and its master interface are not disabled and the *master* interface has a bound flag. |
| **cap** (string) | Shows information about a CAP device if this router is a CAPsMAN and interface does not belong to the device itself, but a CAPsMAN-controlled CAP device. |
| **default-name** (*string*) | The default name for an interface. |
| **inactive** (*boolean*) (I) | False for interfaces in AP mode when they've selected a channel for operation (i.e. configuration has been successfully applied).  False for interfaces in station mode when they've connected to an AP (i.e. configuration has been successfully applied, and an AP with matching settings has been found).  True otherwise. |
| **master** (*boolean*) (M) | True for physical interfaces on the router itself or detected CAP if running as CAPsMAN.  False for virtual interfaces. |
| **radio-mac** (*MAC*) | The MAC address of the associated radio. |
| **running** (*boolean*) (R) | True, when an interface has established a link to another device.  If *disable-running-check* is set to 'yes', true whenever the interface is not disabled. |

### Access List

Filtering parameters:

| Parameter | Description |
| :-- | :-- |
| **interface** (*interface* \| *interface-list* \| *any; default: **any***) | Match if the connection takes place on the specified interface or an interface belonging to a specified list. |
| **mac-address** (*MAC address; default: **none***) | Match if the client device has the specified MAC address. |
| **mac-address-mask** (*MAC address*) | Modifies the **mac-address** parameter to match if it is equal to the result of performing a bit-wise AND operation on the client MAC address and the given address mask.  Default: FF:FF:FF:FF:FF:FF (i.e. client's MAC address must match value of **mac-address** exactly) |
| **signal-range** (*min..max*) | Match if the strength of the received signal from the client device is within the given range. Allowed values: '-120..120' |
| **ssid-regexp** (*regex*) | Match if the given regular expression matches the SSID. |
| **time** (*start-end,days*) | Match during the specified time of day and (optionally) days of the week. Allowed values: 0s-1d |
| **multi-passphrase-group** (*string*) | Name of `/interface/wifi/security/multi-passphrase/` group that will be used. Only a single group can be set under one access list entry. |

Action parameters:

| Parameter | Description |
| :-- | :-- |
| **allow-signal-out-of-range** *(time period \| always; default: **0s**)* | The length of time which a connected peer's signal strength is allowed to be outside the range required by the **signal-range** parameter, before it is disconnected.  If the value is set to 'always', peer signal strength is only checked during association. |
| **action** (*accept* \| *reject* \| *query-radius; default: **accept***) | Whether to authorize a connection accept - connection is allowedreject - connection is not allowedquery-radius -  connection is allowed if MAC address authentication of the client's MAC address succeeds |
| **client-isolation** (*no* \| *yes; default: **none***) | Whether to [isolate](./#datapath-properties) the client from others connected to the same AP. |
| **passphrase** (*string; *default: **none***) [sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | Override the default passphrase with the given value. |
| **radius-accounting** (*no* \| *yes; *default: **none***)* | Override the default RADIUS accounting policy with the given value. |
| **vlan-id** (*none* \| *integer 1..4095; *default: **none***)* | Assign the given [VLAN ID](./#datapath-properties) to matched clients. |

### Frequency scan

Information about RF conditions on available channels can be obtained by running the frequency-scan command. 
Command parameters:

| Parameter | Description |
| :-- | :-- |
| **duration** (*time interval; *default: **none***)* | Length of time to perform the scan for before exiting. Useful for non-interactive use. |
| **freeze-frame-interval** (*time interval; default: **1s**)* | Time interval at which to update command output. |
| **frequency** (*list of frequencies/ranges)* | Frequencies to perform the scan on. See [channel.frequency parameter syntax](#channel-properties) above for more detail. Defaults to all supported frequencies. |
| **number** (*string*; *default*: **none**) | Either the name or internal id of the interface to perform the scan with. Required. |
| **rounds** (*integer*; *default*: **none**) | Number of times to go through the list of scannable frequencies before exiting. Useful for non-interactive use. |
| **save-file** (*string*; *default*: **none**) | Name of the file to save output to. |

Output parameters:

| Parameter | Description |
| :-- | :-- |
| **channel** (*integer*) | Frequency (in MHz) of the channel scanned. |
| **networks** (*integer*) | Number of access points detected on the channel. |
| **load** (*integer*) | Percentage of time the channel was busy during the scan. |
| **nf** (integer) | Noise floor (in dBm) of the channel. |
| **max-signal** (*integer*) | Maximum signal strength (in dBm) of APs detected in the channel. |
| **min-signal** (*integer*) | Minimum signal strength (in dBm) of APs detected in the channel. |
| **primary** (*boolean*) (P) | Channel is in use as the primary (control) channel by an AP. |
| **secondary** (*boolean*) (S) | Channel is in use as a secondary (extension) channel by an AP. |

### Flat-snoop

The `/interface/wifi/flat-snoop` is a tool for surveying APs and stations. Monitors frequency usage, and displays which devices occupy each frequency. Provides more detailed information regarding nearby APs than scan, and offers an easy overview of frequency usage by station/AP count.
Output parameters:

| Parameters | Description |
| :-- | :-- |
| **duration** (*time interval*; *default*: **none**) | Length of time to perform the scan before exiting. Useful for non-interactive use. |
| **filter-type** (*bss \| frequency \| stas*) | bss - list of active APs and their parameters.  frequency - list of station and AP count per scanned frequency  stas - a detailed list of stations on each scanned frequency  If filter-type is unspecified, all types will be returned. |
| **freeze-frame-interval** (*time interval; default: **1s**)* | Time interval at which to update command output. |

### Scan command

The `/interface/wifi/scan` command will scan for access points and print out information about any APs it detects.
The scan command takes all the same parameters as the frequency-scan command.
Output parameters:

| Parameter | Description |
| :-- | :-- |
| **active** (*boolean*) (A) | This signifies that beacons from the AP have been received in the last 30 seconds. |
| **address** (*MAC*) | The MAC address (BSSID) of the AP. |
| **channel** (*string*) | The control channel frequency used by the AP, its supported wireless standards and control/extension channel layout. |
| **security** (*string*) | Authentication methods supported by the AP. |
| **signal** (*integer*) | The signal strength of the AP's beacons (in dBm). |
| **ssid** (*string*) | The extended service set identifier of the AP. |
| **sta-count** (*integer*) | The number of client devices associated with the AP. It is only available if the AP includes this information in its beacons. |

### Sniffer

Command parameters:

| Parameters | Description |
| :-- | :-- |
| **duration** (*time interval*; **default: **none***)* | Automatically interrupt the sniffer after the specified time has passed. |
| **filter** (*string*) | A string that specifies a filter to apply to captured frames. Only frames matched by the filter expression will be displayed, saved or streamed.  This works similarly to filter strings in libpcap, for example.  The filter can match Address fields (addr1, addr2, addr3)Wireless frame type and subtype, including shortcuts such as 'beacon' (type == 0 &amp;&amp; subtype == 8)Flags (to-ds, from-ds, retry, power, protected) A string can include the following operators: == (exact match)!= (does not equal)&amp;&amp; (logical AND) \|\|  (logical OR)() (for grouping filter expressions) |
| **number** (*interface*)  | Interface to use for sniffing. |
| **pcap-file** (*string*) | Save captured frames to a file with the given name. No default value (captured frames are not saved to a file by default). |
| **pcap-size-limit** (*integer*; *default*: **none**) | File size limit (in bytes) when storing captured frames locally. When this limit has been reached, no new frames are added to the capture file. |
| **stream-address** (*IP address*; *default*: **none**) | Stream captured packets via the TZSP protocol to the given address. No default value (captured packets are not streamed anywhere by default). |
| **stream-rate** (*integer*) | Limit the rate (in packets per second) at which captured frames are streamed via TZSP. |

### WPS

`/interface/wifi/wps-client/wifi` 
Command parameters:

| Parameters | Description |
| :-- | :-- |
| **duration** (*time interval*) | Length of time after which the command will time out if no AP is found. Unlimited by default. |
| **interval** (*time interval; default: **1s***) | Time interval at which to update command output. Default: 1s. |
| **mac-address** (*MAC*; *default*: **none**) | Only attempt connecting to the AP with the specified MAC (BSSID). |
| **number** (*string; default: **none***) | Name or internal id of the interface with which to attempt a connection. |
| **ssid** (*string; default: **none***) | Only attempt to connect to APs with the specified SSID. |

### Radios

Information about the capabilities of each radio can be gained by running the `/interface/wifi/radio/print detail` command.

| Property | Description |
| :-- | :-- |
| **2g-channels** (*list of integers*) | Frequencies supported in the 2.4GHz band. |
| **5g-channels** (*list of integers*) | Frequencies supported in the 5GHz band. |
| **6g-channels** (*list of integers*) | Frequencies supported in the 6GHz band. |
| **bands** (*list of strings*) | Supported frequency bands, wireless standards, and channel widths. |
| **ciphers** (*list of strings*) | Supported encryption ciphers. |
| **countries** (*list of strings*) | Regulatory domains supported by the interface. |
| **hw-caps** (*list of strings*) | Additional supported features (e.g. sniffer, qos-classifier-dscp). |
| **hw-type** (*string*) | Radio hardware model number. |
| **max-interfaces** (*integer*) | Maximum number of logical interfaces. |
| **max-peers** (*integer*) | Maximum number of associated peers (connected stations). |
| **max-station-interfaces** (*integer*) | Maximum number of logical interfaces in station mode. |
| **max-vlans** (*integer*) | Maximum number of different per-user VLANs. |
| **min-antenna-gain** (*integer*) | Minimum antenna gain permitted for the interface. |
| **ml-group** (*MAC address*) | Radios with a common ML (multi-link) group can be configured to take advantage of multi-link operation. |
| **phy-id** (*string*) | A unique identifier. |
| **radio-mac** (*MAC*) | MAC address of the radio interface. Can be used to match radios to interface configurations. |
| **rx-chains** (*list of integers*) | IDs for radio chains available for receiving radio signals. |
| **tx-chains** (*list of integers*) | IDs for radio chains available for transmitting radio signals. |

### Registration table

The registration table contains read-only information about associated wireless devices.

| Parameter | Description |
| :-- | :-- |
| **authorized** (*boolean*) (A) | True when the peer has successfully authenticated. |
| **auth-type** (*string*) | Authentication type used for the particular client. |
| **band** (*string*) | Band on which particular router is communicating with the AP. |
| **bytes** (*list of integers*) | Number of bytes in packets transmitted to a peer and received from it. |
| **interface** (*string*) | Name of the interface, which was used to associate with the peer. |
| **last-activity**(time) | last interface data tx/rx activity |
| **mac-address** (*MAC*) | The MAC address of the peer. |
| **packets** (*list of integers*) | Number of packets transmitted to a peer and received from it. |
| **tx-bits-per-second** (*integer*) | Rate of transmitted data to peer per second. |
| **rx-bits-per-second** (*integer*) | Rate of received data from peer per second. |
| **rx-rate** *(string*) | Bitrate of received transmissions from peer. |
| **signal** (*integer*) | Strength of signal received from the peer (in dBm). |
| **ssid** *(string*) | The SSID on which the client is connected. |
| **tx-rate** (*string*) | Bitrate used for transmitting to the peer. |
| **uptime** (*time interval*) | Time since association. |
| **vlan-id** (*integer*) | VLAN which is assigned by AP or RADIUS for the particular peer traffic. |
