# Interworking Profiles

> This page describes MikroTik RouterOS interworking profiles for wireless networks, enabling devices to exchange information via IEEE 802.11u and Hotspot 2.0 standards. It details configuration properties like network...

# Interworking Profiles

## Interworking

Interworking is the occurrence of two or more things working together. For a better Wireless network experience, information about the network must be exchanged between Access Points and Wireless client devices. The information that can be found in basic Wireless beacons and probe requests is limited. For this reason, the IEEE 802.11u™-2011 (Interworking with External Networks) standard was created that specifies how devices should exchange information between each other. Network discovery and Access Point selection process can be enhanced with the interworking service. Wireless client devices can have more criteria upon which they can choose the network with which to associate.

## Hotspot 2.0

Hotspot 2.0 is a specification developed and owned by the Wi-Fi Alliance. It was designed to enable a more cellular-like experience when connecting to Wi-Fi networks. In an attempt to increase wireless network security, Hotspot 2.0 access points use mandatory WPA2 authentication. Hotspot 2.0 relies on Interworking and adds some of its own properties and procedures.

Interworking profiles are implemented according to IEEE 802.11u and Hotspot 2.0 Release 1 specifications.

:::info
This manual page describes interworking configuration for the legacy `wireless` package (`/interface/wireless`). For the `wifi` package (`/interface/wifi`), see [Interworking for WiFi6](../wifi/interworking-for-wifi6.md).
:::

## Configuration Properties

**Sub-menu:** `/interface/wireless/interworking-profiles`

### Information elements in beacon and probe response

Some information can be added to beacon and probe response packets with an Interworking element. Following parameters of an Interworking element can be configured:

| Property | Description |
| :-- | :-- |
| **asra** (*yes \| no*; Default: **no**) | Additional Steps Required for Access. Set to `yes`, if a user should take additional steps to access the internet, like the walled garden. |
| **esr** (*yes \| no*; Default: **no**) | Emergency services reachable (ESR). Set to `yes` in order to indicate that emergency services are reachable through the access point. |
| **hessid** (*MAC address*; Default: ) | Homogenous extended service set identifier (HESSID). Devices that provide access to the same external networks are in one homogenous extended service set. This service set can be identified by the HESSID that is the same on all access points in this set. The 6-byte value of HESSID is represented as a MAC address. It should be globally unique, therefore it is advised to use one of the MAC addresses of the access points in the service set. |
| **internet** (*yes \| no*; Default: **yes**) | Whether the internet is available through this connection or not. This information is included in the Interworking element. |
| **network-type** (*emergency-only \| personal-device \| private \| private-with-guest \| public-chargeable \| public-free \| test \| wildcard*; Default: **wildcard**) | Information about network access type.<code>emergency-only</code> - a network dedicated and limited to accessing emergency services;<code>personal-device</code> - a network of personal devices. An example of this type of network is a camera that is attached to a printer, thereby forming a network for the purpose of printing pictures;<code>private</code> - network for users with user accounts. Usually used in enterprises for employees, not guests;<code>private-with-guest</code> - same as private, but guest accounts are available;<code>public-chargeable</code> - a network that is available to anyone willing to pay. For example, a subscription to Hotspot 2.0 service or in-room internet access in a hotel;<code>public-free</code> - a network is available to anyone without any fee. For example, municipal network in city or airport Hotspot;<code>test</code> - a network used for testing and experimental uses. Not used in production;<code>wildcard</code> - It is used on Wireless clients. Sending a probe request with a wildcard as a network type value will make all Interworking Access Points respond despite their actual network-type setting.A client sends a probe request frame with network-type set to a value it is interested in. It will receive replies only from access points with the same value (except the case of wildcard). |
| **uesa** (*yes \| no*; Default: **no**) | Unauthenticated emergency service accessible (UESA).<code>no</code> - indicates that no unauthenticated emergency services are reachable through this Access Point;<code>yes</code> - indicates that higher layer unauthenticated emergency services are reachable through this Access Point. |
| **venue** (*venue*; Default: **unspecified**) | Specify the venue in which the Access Point is located. Choose the value from available ones. Some examples:`venue=business-bank``venue=mercantile-shopping-mall``venue=educational-university-or-college`|

### ANQP elements

Access network query protocol (ANQP). Not all necessary information is included in probe response and beacon frames. For a client device to get more information before choosing an access point to associate with, ANQP is used. The Access Point can have stored information in multiple ANQP elements. The client device will use ANQP to query only for the information it is interested in. This reduces the time needed before association.

| Property | Description |
| :-- | :-- |
| **3gpp-raw** (*octet string in hex*; Default: ) | Cellular network advertisement information - country and network codes. This helps Hotspot 2.0 clients in the selection of an Access Point to access 3GPP network. Please see 3GPP TS 24.302. (Annex H) for a format of this field. This value is sent in an ANQP response if queried. |
| **3gpp-info**(*number/number*; Default: ) | Cellular network advertisement information - country and network codes. This helps Hotspot 2.0 clients in the selection of an Access Point to access 3GPP network.  Written as "mcc/mnc". Usage is identical to "3gpp-raw", but without using hex. Multiple mcc/mnc pairs can be defined, by separating them with a comma. |
| **authentication-types** (*dns-redirection:`url` \| https-redirection:`url` \| online-enrollment:`url` \| terms-and-conditions:`url`*; Default: ) | This property is only effective when asra is set to `yes`. Value of `url` is optional and not needed if `dns-redirection` or `online-enrollment` is selected. To set the value of `url` to empty string use double quotes. For example:`authentication-types=online-enrollment:""` |
| **connection-capabilities** (*number:number:closed\|open\|unknown*; Default: ) | This option allows providing information about the allowed IP protocols and ports. This information can be provided in ANQP response. The first number represents the IP protocol number, the second number represents a port number.<code>closed</code> - set if protocol and port combination is not allowed;<code>open</code> - set if protocol and port combination is allowed;<code>unknown</code> - set if protocol and port combination is either open or closed. Example: `connection-capabilities=6:80:open,17:5060:closed`  Setting such a value on an Access Point informs the Wireless client, which is connecting to the Access Point, that HTTP (6 - TCP, 80 - HTTP) is allowed and VoIP (17 - UDP; 5060 - VoIP) is not allowed. This property does not restrict or allow usage of these protocols and ports, it only gives information to station device which is connecting to Access Point. |
| **domain-names** (*list of strings*; Default: ) | None or more fully qualified domain names (FQDN) that indicate the entity operating the Hotspot. A station that is connecting to the Access Point can request this ANQP property and check if there is a suffix match with any of the domain names it has credentials to. |
| **ipv4-availability** (*double-nated \| not-available \| port-restricted \| port-restricted-double-nated \| port-restricted-single-nated \| public \| single-nated \| unknown*; Default: **not-available**) | Information about what IPv4 address and access is available.<code>not-available</code> - Address type not available;<code>public</code> - public IPv4 address available;<code>port-restricted</code> - port-restricted IPv4 address available;<code>single-nated</code> - single NATed private IPv4 address available;<code>double-nated</code> - double NATed private IPv4 address available;<code>port-restricted-single-nated</code> -port-restricted IPv4 address and single NATed IPv4 address available;<code>port-restricted-double-nated</code> - port-restricted IPv4 address and double NATed IPv4 address available;<code>unknown</code> - availability of the address type is not known. |
| **ipv6-availability** (*available \| not-available \| unknown*; Default: **not-available**) | Information about what IPv6 address and access is available.<code>not-available</code> - Address type not available;<code>available</code> - address type available;<code>unknown</code> - availability of the address type is not known. |
| **realms** (*string:eap-sim\|eap-aka\|eap-tls\|not-specified*; Default: ) | Information about supported realms and the corresponding EAP method.`realms=example.com:eap-tls,foo.ba:not-specified` |
| **realms-raw** (*octet string in hex*; Default: ) | Set NAI Realm ANQP-element manually. |
| **roaming-ois** (*octet string in hex*; Default: ) | Organization identifier (OI) is usually a 24-bit unique identifier like organizationally unique identifier (OUI) or company identifier (CID). In some cases, OI is longer for example OUI-36. A subscription service provider (SSP) can be specified by its OI. roaming-ois property can contain zero or more SSPs OIs whose networks are accessible via this AP. Length of OI should be specified before OI itself. For example, to set E4-8D-8C and 6C-3B-6B: `roaming-ois=03E48D8C036C3B6B`|
| **venue-names** (*string:lang*; Default: ) | Venue name can be used to provide additional info on the venue. It can help the client to choose a proper Access Point. The Venue-names parameter consists of zero or more duples that contain Venue Name and Language Code: `venue-names=CoffeeShop:eng,TiendaDeCafe:es`The Language Code field value is a two or three-character language code selected from ISO-639. |

#### Realms raw

**realms-raw** - a list of strings with hex values. Each string specifies the contents of "NAI Realm Tuple", excluding the "NAI Realm Data Field Length" field.

Each hex encoded string must consist of the following fields:

```
- NAI Realm Encoding (1 byte)
- NAI Realm Length (1 byte)
- NAI Realm (variable)
- EAP Method Count (1 byte)
- EAP Method Tuples (variable)
```

For example, the value "00045465737401020d00" decodes as:

```
- NAI Realm Encoding: 0 (rfc4282)
- NAI Realm Length: 4
- NAI Realm: Test
- EAP Method Count: 1
- EAP Method Length: 2
- EAP Method Tuple: TLS, no EAP method parameters
```

Note that setting "realms-raw=00045465737401020d00" produces the same advertisement contents as setting "realms=Test:eap-tls".

Refer to 802.11-2016, section 9.4.5.10 for full NAI Realm encoding.

### Hotspot 2.0 ANQP elements

The Hotspot 2.0 specification introduced some additional ANQP elements. These elements use an ANQP vendor specific element ID. Here are the available properties to change these elements.

| Property | Description |
| :-- | :-- |
| **hotspot20** (*yes \| no*; Default: **yes**) | Indicates Hotspot 2.0 capability of the Access Point. |
| **hotspot20-dgaf** (*yes \| no*; Default: **yes**) | Downstream Group-Addressed Forwarding (DGAF). Sets value of DGAF bit to indicate whether multicast and broadcast frames to clients are disabled or enabled.<code>yes</code> - multicast and broadcast frames to clients are enabled;<code>no</code> - multicast and broadcast frames to clients are disabled.To disable multicast and broadcast frames set `multicast-helper=full`. |
| **operational-classes** (*list of numbers*; Default: ) | Information about other available bands of the same ESS. |
| **operator-names** (*string:lang*; Default: ) | Sets operator name. Language must be specified for each operator name entry. Operator-names parameter consists of zero or more duples that contain Operator Name and Language Code: `operator-names=BestOperator:eng,MejorOperador:es`The Language Code field value is a two or three-character language code selected from ISO-639. |
| **wan-at-capacity** (*yes \| no*; Default: **no**) | Whether the Access Point or the network is at its max capacity. If set to `yes` no additional mobile devices will be permitted to associate to the AP. |
| **wan-downlink** (*number*; Default: **0**) | The downlink speed of the WAN connection set in kbps. If the downlink speed is not known, set to 0. |
| **wan-downlink-load** (*number*; Default: **0**) | The downlink load of the WAN connection measured over `wan-measurement-duration`. Values from 0 to 255.<code>0</code> - unknown;<code>255</code> - 100%. |
| **wan-measurement-duration** (*number*; Default: **0**) | Duration during which wan-downlink-load and `wan-uplink-load` are measured. Value is a numeric value from 0 to 65535 representing tenths of seconds.<code>0</code> - not measured;<code>10</code> - 1 second;<code>65535</code> - 1 hour 49 minutes or more. |
| **wan-status** (*down \| reserved \| test \| up*; Default: **reserved**) | Information about the status of the Access Point's WAN connection. The value `reserved` indicates status is not advertised. |
| **wan-symmetric** (*yes \| no*; Default: **no**) | Whether the WAN link is symmetric (upload and download speeds are the same) or not. |
| **wan-uplink** (*number*; Default: **0**) | The uplink speed of the WAN connection set in kbps. If the uplink speed is not known set to 0. |
| **wan-uplink-load** (*number*; Default: **0**) | The uplink load of the WAN connection measured over wan-measurement-duration. Values from 0 to 255.<code>0</code> - unknown;<code>255</code> - 100%. |

### Other Properties

| Property | Description |
| :-- | :-- |
| **comment** (*string*; Default: ) | Short description of the profile |
| **name** (*string*; Default: ) | Name of the Interworking profile. |

## Configuration guide using native RadSec and Orion Wifi

This guide describes how to set up your MikroTik devices so you can use them with RadSec proxy and Orion Wifi, though the main configuration steps remain the same and will work with different providers as well:
Make sure to use the latest long-term or stable RouterOS releases.

It is important to set up a secure RADIUS connection between the wireless LAN controller and Orion Wifi.  
Orion Wifi uses RADIUS over TLS (RadSec) to ensure end-to-end encryption of AAA traffic.

1) Import RadSec certificates you have downloaded from Orion:

Drag and drop the certificate in WinBox, and then use the import function for it, which can be found under `/system/certificates` in WinBox. The command line equivalent is:

```
/certificate/import file-name=bw.radsec.cacert.pem passphrase=""
/certificate/import file-name=cert.pem passphrase=""
/certificate/import file-name=key.pem passphrase=""
```

![](./img/interworking-profiles-01.webp)

![](./img/interworking-profiles-02.webp)

![](./img/interworking-profiles-03.webp)

Once certificates are imported, they should look like this:

![](./img/interworking-profiles-04.webp)

1) Configure the Radius client:

![](./img/interworking-profiles-05.webp)

Command line equivalent:

```
/radius/add address=216.239.32.91 certificate=cert.pem_0 protocol=radsec service=wireless timeout=1s500ms
```

1) Create a wireless security profile that performs 802.1x authentication:

![](./img/interworking-profiles-06.webp)

![](./img/interworking-profiles-07.webp)

![](./img/interworking-profiles-08.webp)

The Command line equivalent is:

```
/interface/wireless/security-profiles/add authentication-types=wpa2-eap management-protection=allowed mode=dynamic-keys name=dot1x_profile supplicant-identity="" radius-eap-accounting=yes eap-methods=passthrough
```

1) The next step is configuring the wireless interface and assigning the created security profile. Press “Advanced mode” to see all the options:

![](./img/interworking-profiles-09.webp)

The command line equivalent is:

```
/interface/wireless/set [ find default-name=wlan1 ] mode=ap-bridge security-profile=dot1x_profile wps-mode=disabled
```

Make sure the correct country profile is configured. In this example, we are using “wlan1”, but the same command would work with other interfaces, or as `/interface/wireless/set wlan1`.

1) Configure interworking settings (hotspot 2.0):

![](./img/interworking-profiles-10.webp)

![](./img/interworking-profiles-11.webp)

![](./img/interworking-profiles-12.webp)

Command line equivalent:

```
/interface/wireless/interworking-profile/add domain-names=orion.area120.com ipv4-availability=public name=Orion_MikroTik network-type=public-chargeable operator-names=Orion:eng realms=orion.area120.com:eap-tls roaming-ois=f4f5e8f5f4,baa2D00100,baa2d00000 venue=business-unspecified venue-names=Orion:eng wan-downlink=50 wan-uplink=50 wan-status=up
```

:::warning
Pay special attention to "wan-downlink" and "wan-uplink", in this scenario the value of "50" is used as a placeholder, make sure to adjust the values according to your setup. Some client devices use it to evaluate if they should join the network. Set “venue” – venue type, ”venue-names” and other attributes as applicable. “domain-names” should be of the hotspot 2.0 Operator.
:::

1) Assign the interworking profile to the interface:

![](./img/interworking-profiles-13.webp)

The command-line equivalent is:

```
/interface/wireless/set wlan1 interworking-profile=Orion_MikroTik
```

If you don't see the interworking-profile field, press "Advanced mode".

Note: NAS-id that's used by Orion to differentiate networks is equal to system identity, to adjust the nas-id, you can do `/system/identity/set name=exampleName`.

## Configuration guide using RadSec proxy and Orion Wifi

This guide describes how to set up your MikroTik devices so you can use them with a RadSec proxy and Orion Wifi, though the main configuration steps remain the same and will work with different providers as well:
This guide assumes that you have configured a radsecproxy with Orion Wifi credentials. Make sure to use the latest long-term or stable RouterOS releases.  
  
It is important to set up a secure RADIUS connection between the wireless LAN controller and Orion Wifi.  
Orion Wifi uses RADIUS over TLS (RadSec) to ensure end-to-end encryption of AAA traffic. This guide is made for scenarios where the RouterOS access point redirects AAA traffic to a RadSec proxy (radsecproxy) before the traffic is sent over the internet.

1) Configure the Radius client that points to radsecproxy:

![](./img/interworking-profiles-14.webp)

The command line equivalent is:

```
/radius/add address=192.168.88.233 secret=yourSecret service=wireless timeout=1s500ms
```

The secret should match the one configured on the radsecproxy. In this example, “192.168.88.233” is a virtual machine running the proxy.

1) Create a wireless security profile that would perform 802.1x authentication:

![](./img/interworking-profiles-06.webp)

![](./img/interworking-profiles-07.webp)

![](./img/interworking-profiles-08.webp)

The Command line equivalent is:

```
/interface/wireless/security-profiles/add authentication-types=wpa2-eap management-protection=allowed mode=dynamic-keys name=dot1x_profile supplicant-identity="" radius-eap-accounting=yes eap-methods=passthrough
```

1) The next step is configuring the wireless interface and assigning the created security profile. Press “Advanced mode” to see all the options:

![](./img/interworking-profiles-09.webp)

The command line equivalent is:

```
/interface/wireless/set [ find default-name=wlan1 ] mode=ap-bridge security-profile=dot1x_profile wps-mode=disabled
```

Make sure the correct country profile is configured. In this example, we are using “wlan1”, but the same command would work with other interfaces, or as `/interface/wireless/set wlan1`.

1) Configure interworking settings (hotspot 2.0):

![](./img/interworking-profiles-10.webp)

![](./img/ANQP_1.png)

![](./img/interworking-profiles-12.webp)

Command line equivalent:

```
/interface/wireless/interworking-profile/add domain-names=orion.area120.com ipv4-availability=public name=Orion_MikroTik network-type=public-chargeable operator-names=Orion:eng realms=orion.area120.com:eap-tls roaming-ois=f4f5e8f5f4,baa2D00100,baa2d00000 venue=business-unspecified venue-names=Orion:eng wan-downlink=50 wan-uplink=50 wan-status=up
```

:::warning
Be sure to specify some value in "wan-downlink" and "wan-uplink", in this scenario the value of "50" is used as a placeholder, some client devices use it to evaluate, if they should join the network. Set “venue” – venue type, ”venue-names” and other attributes as applicable. “domain-names” should be of the hotspot 2.0 Operator.
:::

1) Assign the interworking profile to the interface:

![](./img/interworking-profiles-13.webp)

This step can also be done with the following command:

```
/interface/wireless/set wlan1 interworking-profile=Orion_MikroTik
```

If the radsecproxy is working, then clients with the appropriate Hotspot profile installed should be able to connect.

Note: NAS-id that's used by Orion to differentiate networks is equal to system identity. To adjust the nas-id, you can do `/system/identity/set name=exampleName`.

## Troubleshooting

To check the status of RADIUS messages, you can use the radius menu.  
![](./img/interworking-profiles-15.webp)  
Or alternatively, via the command line, run `/radius/monitor X`, X being the numerical ID. You can see the IDs with `/radius/print`.  
For more information, additional logging can be configured under `/system/logging/add topics=radius,debug,packet`. You can view results under [`/log`](../../diagnostics-monitoring-and-troubleshooting/log/index.md).

To view active wireless connections check the wireless registration table `/interface/wireless/registration-table/print`:

![](./img/interworking-profiles-16.webp)
