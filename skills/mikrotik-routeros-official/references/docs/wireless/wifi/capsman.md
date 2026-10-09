# WiFi CAPsMAN

> WiFi CAPsMAN (Controlled Access Point system Manager) for the wifi-qcom / wifi-qcom-ac packages centralizes management of multiple WiFi access points. Covers CAP discovery, radio provisioning, datapath/forwarding...

# WiFi CAPsMAN

:::info
This section describes the operation of the CAPsMAN feature in the wifi-qcom and wifi-qcom-ac packages. For devices with the older "wireless" package, see [the respective manual here](../abgn/capsman/index.md). Here and further below, when talking about "WiFi", we mean the new WiFi menu, not the technology.
:::

Controlled Access Point system Manager (CAPsMAN) allows applying wireless settings to multiple MikroTik WiFi AP devices from a central configuration interface, i.e. allows the centralization of wireless network management. When using CAPsMAN, the network will consist of a number of 'Controlled Access Points' (CAP) that provide wireless connectivity and a 'system Manager' (CAPsMAN) that manages the configuration of the APs, and it also takes care of client authentication.

Requirements:

- Any RouterOS device, that supports the WiFi package, can be a controlled wireless access point (CAP) as long as it has at least a Level 4 RouterOS license.
- WiFi CAPsMAN server can be installed on any RouterOS device that supports the WiFi package, even if the device itself does not have a wireless interface.
- Unlimited CAPs (access points) are supported by CAPsMAN.

:::info
WiFi CAPsMAN can only control WiFi interfaces, and WiFi CAPs can join only WiFi CAPsMAN. Similarly, regular CAPsMAN only supports non-WiFi caps.

The CAPs don't send traffic usage information to CAPsMAN.
:::

### CAPsMAN Discovery by CAP

CAP discovers CAPsMAN address/hostname via:

- Layer 2 discovery.
- DHCP option 138 (CAPsMAN address).
- DHCP option 15 (custom domain): `resolves _capsman._tcp.<domain>.`
- Default MikroTik 'lan' domain: `resolves _capsman._tcp.lan.`

### Radio Provisioning

Once configuration templates have been created, you can select which devices should be provisioned with each of the templates. Of course, in simple setups it is enough to have only one provisioning rule, but if you wish to send one configuration to 2.4GHz interfaces and a different one to 5GHz interfaces, you can create two provisioning rules and define which template is sent where, using the `supported-bands` parameter.

CAPsMAN distinguishes between actual wireless interfaces (radios) based on their built-in MAC address (radio-mac). This implies that it is impossible to manage two radios with the same MAC address on one CAPsMAN. Radios currently managed by CAPsMAN (provided by connected CAPs) are listed in `/interface/wifi/radio` menu. This list will also include the built-in wifi interfaces that are present on CAPsMAN itself if there are any:

```ros
[admin@c52i] > /interface/wifi/radio/print 
Flags: L - LOCAL
Columns: CAP, RADIO-MAC, INTERFACE
#   CAP                  RADIO-MAC          INTERFACE 
0 L                      18:FD:74:AF:F4:28  wifi1     
1 L                      18:FD:74:AF:F4:29  wifi2     
2   hapAX3@192.168.88.30  48:A9:8A:0B:F7:4B  cap1
```

When CAP connects, CAPsMAN at first tries to bind each CAP radio to CAPsMAN master interface based on radio-mac. If an appropriate interface is found, the radio gets set up using master interface configuration and configuration of slave interfaces that refer to a particular master interface. At this moment interfaces (both master and slaves) are considered bound to radio and radio is considered provisioned. This happens only if there were matching static entries already present under `/interface/wifi` , typically if the entry was made previously either manually, or with provisioning rules that contain action "create-enabled" or "create-disabled".

If no matching master interface for radio is found, CAPsMAN executes 'provisioning rules', which are defined under `/interface/wifi/provisioning/`. Provisioning rules is an ordered list of rules that contain settings that specify which radio to match and settings that determine what action to take if a radio matches.

When CAP joins CAPsMAN, and there is no matching interface for it present under`/interface/wifi` , provisioning rules will automatically be checked, once a match is found, the CAP's wireless interface will appear under `/interface/wifi`. Such an interface is "provisioned", provisioned in this context means that there is a wifi interface present for the radio, and it has a configuration profile assigned to it.

There is also an option to manually provision interfaces, which will make CAPsMAN start evaluating provisioning rules against the specific interface, and a new interface will be created upon match. If there was already an entry present for the radio under `/interface/wifi/`, that entry will be deleted and re-created. Manual provisioning re-creates the interface and is **generally not needed**, since provisioning rules are evaluated automatically, and if you change the configuration profile associated with the provisioning rule, the changes will be applied to all wifi interfaces that use that configuration. If you manually provision interfaces, the interface ID or name can change, resulting in broken references to other objects, for example, bridge ports.

Manual provision can be done under `/interface/wifi/capsman/remote-cap/provision` to provision all radios associated with specific CAPs, it can also be done under `/interface/wifi/radio/provision`, to provision specific radios.

CAPsMAN cannot manage it's own wifi interfaces using `configuration.manager=capsman`, it is enough to just set the same configuration profile on local interfaces manually as you would with provisioning rules, and the end result will be the same as if they were CAPs. That being said, it is also possible to provision local interfaces via `/interface/wifi/radio` menu, it should be noted that to regain control of local interfaces after provisioning, you will need to disable the matching provisioning rules and press "provision" again, which will return local interfaces to an unconfigured state.

:::info
Provision must be done only initially, and is done automatically upon CAP joining if there are matching provisioning rules that are enabled.  
If you adjust any configuration profile that is linked to the provisioned interface, all changes will be "pushed" as soon as you apply changes to the profile, with no need to re-create the already existing interface.  
Provisioning itself is not for sending configuration, it is for essentially creating a new interface. In most cases, there is no reason to perform manual provisioning once you already have CAP interfaces running.
:::

### CAPSMAN Datapath

Datapath settings control data forwarding related aspects. On CAPsMAN datapath settings are configured in the datapath profile menu **/interface/wifi/datapath/** or directly in a configuration profile or interface menu as settings with **datapath.** prefix.

There are 2 major forwarding/traffic-processing modes:

- local forwarding mode (`traffic-processing=on-cap`), where CAP is locally forwarding data to and from wireless interface;
- CAPsMAN forwarding mode (`traffic-processing=on-capsman`), where CAP sends to CAPsMAN all data received over wireless and only sends out the wireless data received from CAPsMAN.

:::info
CAPsMAN forwarding is only possible starting with **7.21beta2** version. **On older versions, only CAP forwarding is supported.**

CAPsMAN forwarding is not supported by **wifi-qcom-ac** devices (wifi-qcom-ac drivers only **support** **local forwarding**).
:::

### CAPsMAN - CAP simple configuration example

CAPsMAN in WiFi uses the same menu as a regular WiFi interface, meaning when you pass configuration to CAPs, you have to use the same configuration, security, channel configuration, etc. as you would for regular WiFi interfaces.

:::info
You can configure sub-configuration menus, directly under `/interface/wifi/configuration` or reference previously created profiles in the main configuration profile
:::

#### CAPsMAN

```ros
#create a security profile
/interface/wifi/security
add authentication-types=wpa3-psk name=sec1 passphrase=HaveAg00dDay

#create configuration profiles to use for provisioning
/interface/wifi/configuration
add country=Latvia name=5ghz security=sec1 ssid=CAPsMAN_5
add name=2ghz security=sec1 ssid=CAPsMAN2
add country=Latvia name=5ghz_v security=sec1 ssid=CAPsMAN5_v

#configure provisioning rules, configure band matching as needed
/interface/wifi/provisioning
add action=create-dynamic-enabled master-configuration=5ghz slave-configurations=5ghz_v supported-bands=\
    5ghz-n
add action=create-dynamic-enabled master-configuration=2ghz supported-bands=2ghz-n

#enable CAPsMAN service
/interface/wifi/capsman
set ca-certificate=auto enabled=yes
```

#### CAP

```ros
#enable CAP service, in this case CAPsMAN is on the same LAN, but you can also specify "caps-man-addresses=x.x.x.x" here
/interface/wifi/cap/set enabled=yes

#set configuration.manager= on the WiFi interface that should act as CAP
/interface/wifi/set wifi1,wifi2 configuration.manager=capsman-or-local
```

:::warning
If the CAP is hAP ax<sup>2</sup> or hAP ax<sup>3</sup>, it is strongly recommended to enable RSTP in the bridge configuration, on the CAP

configuration.manager should only be set on the CAP device itself, don't pass it to the CAP or configuration profile that you provision.
:::

:::info
The interface that should act as CAP needs additional configuration under `/interface/wifi/set wifi1 configuration.manager=`
:::

### CAPsMAN - CAP VLAN configuration example

In this example, we will assign VLAN10 to our main SSID, and will add VLAN20 for the guest network, ether5 from CAPsMAN is connected to CAP.

:::info
CAPs using "wifi-qcom" package can get "vlan-id" via Datapath from CAPsMAN, CAPs using "wifi-qcom-ac" package will need to use the configuration provided at the end of this example.
:::

#### CAPsMAN

```ros
/interface/bridge
add name=br vlan-filtering=yes
/interface/vlan
add interface=br name=MAIN vlan-id=10
add interface=br name=GUEST vlan-id=20
/interface/wifi/datapath
add bridge=br name=MAIN vlan-id=10
add bridge=br name=GUEST vlan-id=20
/interface/wifi/security
add authentication-types=wpa2-psk,wpa3-psk ft=yes ft-over-ds=yes name=Security_MAIN passphrase=HaveAg00dDay
add authentication-types=wpa2-psk,wpa3-psk ft=yes ft-over-ds=yes name=Security_GUEST passphrase=HaveAg00dDay
/interface/wifi/configuration
add datapath=MAIN name=MAIN security=Security_MAIN ssid=MAIN_Network
add datapath=GUEST name=GUEST security=Security_GUEST ssid=GUEST_Network
/ip/pool
add name=dhcp_pool0 ranges=192.168.1.2-192.168.1.254
add name=dhcp_pool1 ranges=192.168.10.2-192.168.10.254
add name=dhcp_pool2 ranges=192.168.20.2-192.168.20.254
/ip/dhcp-server
add address-pool=dhcp_pool0 disabled=yes interface=br name=dhcp1
add address-pool=dhcp_pool1 interface=MAIN name=dhcp2
add address-pool=dhcp_pool2 interface=GUEST name=dhcp3
/interface/bridge/port
add bridge=br interface=ether5 
add bridge=br interface=ether4 
add bridge=br interface=ether3 
add bridge=br interface=ether2 
/interface/bridge/vlan
add bridge=br tagged=br,ether5,ether4,ether3,ether2 vlan-ids=20
add bridge=br tagged=br,ether5,ether4,ether3,ether2 vlan-ids=10
/interface/wifi/capsman
set enabled=yes interfaces=br
/interface/wifi/provisioning
add action=create-dynamic-enabled master-configuration=MAIN slave-configurations=GUEST supported-bands=5ghz-ax
add action=create-dynamic-enabled master-configuration=MAIN slave-configurations=GUEST supported-bands=2ghz-ax
/ip/address
add address=192.168.1.1/24 interface=br network=192.168.1.0
add address=192.168.10.1/24 interface=MAIN network=192.168.10.0
add address=192.168.20.1/24 interface=GUEST network=192.168.20.0
/ip/dhcp-server/network
add address=192.168.1.0/24 gateway=192.168.1.1
add address=192.168.10.0/24 gateway=192.168.10.1
add address=192.168.20.0/24 gateway=192.168.20.1
/system/identity
set name=cAP_Controller
```

#### CAP using "wifi-qcom" package

```ros
/interface/bridge
add name=bridgeLocal
/interface/wifi/datapath
add bridge=bridgeLocal comment=defconf disabled=no name=capdp
/interface/wifi
set [ find default-name=wifi1 ] configuration.manager=capsman datapath=capdp disabled=no
set [ find default-name=wifi2 ] configuration.manager=capsman datapath=capdp disabled=no
/interface/bridge/port
add bridge=bridgeLocal comment=defconf interface=ether1
add bridge=bridgeLocal comment=defconf interface=ether2
add bridge=bridgeLocal comment=defconf interface=ether3
add bridge=bridgeLocal comment=defconf interface=ether4
add bridge=bridgeLocal comment=defconf interface=ether5
/interface/wifi/cap
set discovery-interfaces=bridgeLocal enabled=yes slaves-datapath=capdp
/ip/dhcp-client
add interface=bridgeLocal disabled=no
```

#### CAP using "wifi-qcom-ac" package

```ros
/interface/bridge
add name=bridgeLocal vlan-filtering=yes
/interface/wifi
set [ find default-name=wifi1 ] configuration.manager=capsman disabled=no
set [ find default-name=wifi2 ] configuration.manager=capsman disabled=no
/interface/bridge/port
add bridge=bridgeLocal comment=defconf interface=ether1
add bridge=bridgeLocal comment=defconf interface=ether2
add bridge=bridgeLocal comment=defconf interface=ether3
add bridge=bridgeLocal comment=defconf interface=ether4
add bridge=bridgeLocal comment=defconf interface=ether5
add bridge=bridgeLocal interface=wifi1 pvid=10
add bridge=bridgeLocal interface=wifi21 pvid=20
add bridge=bridgeLocal interface=wifi2 pvid=10
add bridge=bridgeLocal interface=wifi22 pvid=20
/interface/bridge/vlan
add bridge=bridgeLocal tagged=ether1 untagged=wifi1,wifi2 vlan-ids=10
add bridge=bridgeLocal tagged=ether1 untagged=wifi21,wifi22 vlan-ids=20
/interface/wifi/cap
set discovery-interfaces=bridgeLocal enabled=yes slaves-static=yes
```

:::info
Check the dynamically created interface and assign the PVID to the appropriate one. Make sure not to use `/interface/bridge/port/add bridge=bridgeLocal interface=all`, as this will prevent you from applying PVIDs to wifi interfaces.
:::

Additionally, the configuration below has to be added to the **CAPsMAN configuration**:

```ros
/interface/wifi/datapath
add bridge=br name=DP_AC
/interface/wifi/configuration
add datapath=DP_AC name=MAIN_AC security=Security_MAIN ssid=MAIN_Network
add datapath=DP_AC name=GUEST_AC security=Security_GUEST ssid=GUEST_Network
/interface/wifi/provisioning
add action=create-dynamic-enabled master-configuration=MAIN_AC slave-configurations=GUEST_AC supported-bands=5ghz-ac
add action=create-dynamic-enabled master-configuration=MAIN_AC slave-configurations=GUEST_AC supported-bands=2ghz-n
```

:::info
Passing datapaths "MAIN/GUEST" from the start of the example to "wifi-qcom-ac" CAP would be a misconfiguration, make sure to use datapath without "vlan-id" specified to such devices.

With wifi-qcom-ac drivers, datapath setting on the CAPSMAN is not needed. The example, simply, showcases that "vlan-id" must be omitted.
:::

### CAPsMAN - OWE configuration example

#### CAPsMAN

```ros
/interface/wifi/configuration
add country=Latvia disabled=no hide-ssid=yes name=OWE security.authentication-types=owe .owe-transition-interface=auto ssid=MikroTik_OWE
add country=Latvia disabled=no name=open security.owe-transition-interface=auto ssid=Mikrotik_open

/interface/wifi/provisioning
add action=create-dynamic-enabled disabled=no master-configuration=open slave-configurations=OWE

/interface/wifi/capsman
set ca-certificate=auto enabled=yes
```

#### CAP

```ros
/interface/wifi/cap/set enabled=yes
/interface/wifi/set wifi1,wifi2 configuration.manager=capsman-or-local
```

## Property reference

### CAPsMAN Global Configuration

Menu: `/interface/wifi/capsman`

| Property | Description |
| :-- | :-- |
| **ca-certificate** (*auto* \| *certificate name*; default: **auto**) | Device CA certificate, CAPsMAN server requires a certificate, certificate on CAP is optional. |
| **certificate** (*auto* \| *certificate name* \| *none*; default: **none**) | Device certificate |
| **enabled** (*no* \| *yes*) | Disable or enable CAPsMAN functionality |
| **package-path** (*string*) | Folder location for the RouterOS packages. For example, use "/upgrade" to specify the upgrade folder from the files section. If an empty string is set, CAPsMAN can use built-in RouterOS packages. Note that in this case only CAPs with the same architecture as CAPsMAN will be upgraded. |
| **require-peer-certificate** (*yes* \| *no*; default: **no**) | Require all connecting CAPs to have a valid certificate |
| **upgrade-policy** (*none* \| *require-same-version* \| *suggest-same-upgrade*; default: **none**) | Upgrade policy options none - do not perform upgraderequire-same-version - CAPsMAN suggests upgrading the CAP RouterOS version and, if it fails, it will not provision the CAP. (Manual provision is still possible)suggest-same-version - CAPsMAN suggests upgrading the CAP RouterOS version and if it fails, it will still be provisioned |
| **interfaces** (*all* \| *interface name* \| *none*; default: **all**) | Interfaces on which CAPsMAN will listen for layer 2 CAP connections |

### Provisioning

Provisioning rules for matching radios are configured in `/interface/wifi/provisioning/` menu:

| Property | Description |
| :-- | :-- |
| **action** (*create-disabled* \| *create-enabled* \| *create-dynamic-enabled* \| none; default: **none**) | Action to take if rule matches are specified by the following settings:create-disabled - create disabled static interfaces for radio. I.e., the interfaces will be bound to the radio, but the radio will not be operational until the interface is manually enabled;create-enabled - create enabled static interfaces. I.e., the interfaces will be bound to the radio and the radio will be operational;create-dynamic-enabled - create enabled dynamic interfaces. I.e., the interfaces will be bound to the radio, and the radio will be operational;none - do nothing, leaves radio in the non-provisioned state; The basic difference between enabled and dynamic-enabled, is that dynamic interfaces can't be manually edited to override settings and can't be referenced in firewall or other menus, since they will be recreated. In both cases any `/interface/wifi/configuration` changes will be pushed to CAP automatically. |
| **comment** (*string*) | Short description of the Provisioning rule |
| **common-name-regexp** (*string*) | Regular expression to match radios by common name. Each CAP's common name identifier can be found under `/interface/wifi/radio` as value "REMOTE-CAP-NAME" |
| **supported-bands** (*2ghz-ax* \| *2ghz-be* \| *2ghz-g* \| *2ghz-n* \| *5ghz-a* \| *5ghz-ac* \| *5ghz-ax* \| *5ghz-be* \| *5ghz-n* \| *60ghz-ad* \| *6ghz-ax* \| *6ghz-be*) | Match radios by supported wireless modes. This parameter accepts one or more bands as a comma-separated list (for example, *supported-bands=5ghz-ac,5ghz-ax*). When multiple bands are specified, the device must support all listed bands for the match to succeed and for the defined configuration to be applied. |
| **supported-hw-caps** (*beacon-protection* \| *channel-switch* \| *hw-protection-mode* \| *mlo* \| *qos-qualifier* \| *sniffer* \| *spectral*) | Matches radios by their supported additional features, as reported in the *hw-caps* field under `/interface/wifi/radio`. Accepts one or more comma-separated values. A radio must support all listed capabilities to match this provisioning rule. |
| **identity-regexp** (*string*) | Regular expression to match radios by router identity |
| **address-ranges** (*IpAddressRange[,IpAddressRanges] max 100x*;) | Match CAPs with IPs within the configured address range. Will only work for CAPs that joined CAPsMAN using IP, not MAC address. |
| **master-configuration** (*string*) | If **action** specifies to create interfaces, then a new master interface with its configuration set to this configuration profile will be created |
| **multi-link-mode** (*all* \| *auto* \| *disabled* \| *master*; default: **disabled**) | Controls MLO (Multi-Link Operation) behavior during provisioning.all  or auto - CAPsMAN will automatically assign the provisioned WiFi interfaces as affiliated links of an MLD interface. If a matching MLD interface does not already exist, one will be created using the corresponding configuration. This applies to both master and slave interfaces;disabled - no MLD interface is created or assigned during provisioning;master - same behavior as **all** or **auto**, but only the master interface is added as an affiliated MLD link; |
| **name-format** (*string*) | Base string to use when constructing names of provisioned interfaces. Each new interface will be created by taking the base string and appending a number to the end of it. A number will only be appended if the string is not unique.  If included in the string, the character sequence **%I** will be replaced by the system identity of the cAP, **%C** will be replaced with the cAP's TLS certificate's Common Name, **%R**, or **%r** for lowercase, will be replaced with the CAP's radio MAC  Default: "cap-wifi" |
| **slave-name-format** (*string*) | Base string to use when constructing names of virtual interfaces. Each new interface will be created by taking the base string and appending a number to the end of it. A number will only be appended if the string is not unique.  If included in the string, the character sequence  **%v** will be replaced with "virtual", the character sequence  **%m** will be replaced with the name of the master interface, if included in the string, the character sequence **%I** will be replaced by the system identity of the cAP, **%C** will be replaced with the cAP's TLS certificate's Common Name, **%R**, or **%r** for lowercase, will be replaced with the CAP's radio MAC  Default: "*master-interface-name*-virtual" |
| **radio-mac** (*MAC address*) | MAC address of radio to be matched. No default value. |
| **slave-configurations** (*string*) | If the **action** specifies to create interfaces, then a new slave interface for each configuration profile in this list is created. |
| **disabled** (*yes* \| *no*) | Specifies if the provision rule is disabled. |

### CAP configuration

Menu: `/interface/wifi/cap`

| Property | Description |
| :-- | :-- |
| **caps-man-addresses** (*list of IP addresses or host names* ; default: **_capsman._tcp.lan**) | List of comma-separated Manager IP addresses or host names that CAP will attempt to contact during discovery |
| **caps-man-names** () | An ordered list of CAPs Manager names that the CAP will connect to, if empty - CAP does not check manager name |
| **discovery-interfaces** (*list of interfaces*) | List of interfaces over which CAP should attempt to discover the Manager |
| **lock-to-caps-man** (*yes* \| no; default: **no**) | Sets if CAP should lock to the first CAPsMAN it connects to. |
| **slaves-static** (*yes* \| *no*; default: **no**) | Creates Static Virtual Interfaces and allows the possibility to assign IP configuration to those interfaces. MAC address is used to remember each static-interface when applying the configuration from the CAPsMAN. |
| **mld-static** (*yes* \| *no*; default: **no**) | When set to yes, MLD interfaces created on cAP by CAPsMAN ar static; otherwise, they are dynamic. Static interfaces have persistent internal IDs and can be manually manipulated, added to bridges, referenced in firewall rules etc. Dynamic interfaces do not persist between reboots. They should be assigned an appopriate datapath profile. |
| **caps-man-certificate-common-names** () | List of Manager certificate CommonNames that CAP will connect to, if empty - CAP does not check Manager certificate CommonName |
| **certificate** () | Certificate to use for authenticating |
| **enabled** (*yes* \| *no*; default: **no**) | Disable or enable the CAP feature |
| **current-caps-man-address** () | Shows currently used CAPsMAN address |
| **current-caps-man-identity** () | Shows currently used CAPsMAN identity |
| **slaves-datapath** (*datapath profile*) | Datapath profile to apply to the slave interfaces. Primarily used to designate a bridge that slave interfaces are automatically added to on the CAP. Required when using local forwarding (*traffic-processing=on-cap*), since in that mode all routing and forwarding decisions are made by the CAP itself — CAPsMAN does not include those interfaces in its own bridge, so a datapath must be set either here or manually on the CAP. |
| **mld-datapath** (*datapath profile*) | Datapath profile to apply to the MLD interfaces created by CAPsMAN. Determines how traffic is forwarded on the MLD interface, including which bridge it is added to and whether forwarding is handled locally on the CAP or centrally by CAPsMAN. Has effect only when MLD is in use. |

### Remote CAP

Information about the remote CAPs can be seen by running the `/interface/wifi/capsman/remote-cap/print detail` command.

| Property | Description |
| :-- | :-- |
| **address**(*IP address/MAC address%interface*) | IP address of CAP or MAC address used to connect to CAPsMAN |
| **identity** (*list of integers*) | Configured system identity of CAP |
| **board-name** (*string*) | Describes the model name |
| **serial** (*string*) | The serial number of CAP |
| **version** (*string*) | RouterOS version of CAP |
| **base-mac** (*MAC address*) | Base-MAC provided by CAP in the form: '[XX:XX:XX:XX:XX:XX]' |
| **common-name** (*string*) | Common name of the CAP |
| **connected-time** (*time*) | Time interval passed since the CAP connected to CAPsMAN |
| **uptime** (*time*) | Time interval passed since boot-up |
