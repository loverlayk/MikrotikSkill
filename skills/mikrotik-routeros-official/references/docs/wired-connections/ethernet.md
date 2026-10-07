# Ethernet

> MikroTik RouterOS supports diverse Ethernet interfaces from 10Mbps to 100Gbps, including copper and fiber options with combo interfaces. It enables control over link speed, duplex mode, auto-negotiation, and SFP/QSFP...

# Ethernet

MikroTik RouterOS supports various types of Ethernet interfaces - ranging from 10Mbps to 10Gbps Ethernet over copper twisted pair, 1Gbps, 10Gbps, 25Gbps SFP/SFP+/SFP28 interfaces and 40Gbps, 100Gbps, 200Gbps, 400Gbps QSFP+/QSFP28/QSFP56/QSFP56-DD interfaces. Certain RouterBoard devices are equipped with a combo interface that simultaneously contains two interface types (e.g. Ethernet over twisted pair and SFP/SFP+ interface) allowing selection of the most suitable option or creation of a physical link failover. Through RouterOS, it is possible to control different Ethernet-related properties like link speed, auto-negotiation, duplex mode, etc, monitor transceiver diagnostic information and see a wide range of Ethernet-related statistics.

:::info
For additional information about MikroTik SFP and QSFP type of interfaces and their compatibility, please refer to the [wired interface compatibility](./mikrotik-wired-interface-compatibility.mdx) page.
:::

## Auto-negotiation and Forced Link Mode

Auto-negotiation is a communication method and a set of steps employed by Ethernet devices connected via twisted pair cables. It enables these devices to agree on key transmission settings, including speed, duplex mode, and flow control. During this process, the connected devices initially exchange information about their capabilities concerning these settings. Afterward, they mutually select the best possible transmission mode that both devices can support effectively.

However, in RouterOS auto-negotiation behaves differently on SFP/QSFP ports compared to standard RJ45 Ethernet ports. In the case of SFP/QSFP interfaces, the negotiation process does not involve the exchange of advertised capabilities (no advertisement bits are shared). Instead, RouterOS attempts to bring up the link using the highest supported mode on each side. For a successful connection, both devices must advertise the same highest common mode.

## For example

- Device A advertises `10G-baseCR` and `25G-baseCR`.
- Device B advertises only `10G-baseCR`.

In this case, the link will not establish, because Device A prioritizes 25G while Device B advertises only 10G.

## To ensure a successful link

- Both Device A and Device B must have the same highest advertised mode.  
  So if Device B advertises `25G-baseCR`, and Device A also includes `25G-baseCR` as its highest advertisement, the link will be established.

In summary, when configuring SFP/QSFP interfaces, make sure that the highest supported mode matches on both ends to ensure proper link establishment.

### Advertise

Prior to RouterOS version 7.12, when auto-negotiation was enabled, interfaces attempted to guess the maximum available speed of the interface on the other end (making the advertise setting inapplicable for SFP/QSFP interfaces).

After RouterOS version 7.12, you can now manually set the advertise bits to specify the desired link modes you want to use. The speed arguments have also been revised to provide clearer representation, as the previous values were too ambiguous. Additionally, the full-duplex setting has been removed because the new link modes already encompass the duplex options (see table below).

| Link Modes (for advertise and speed properties) | Description |
| :-- | :-- |
| 10M-baseT-half | 10M twisted-pair half-duplex |
| 10M-baseT-full | 10M twisted-pair full-duplex |
| 100M-baseT-half | 100M twisted-pair half-duplex |
| 100M-baseT-full | 100M twisted-pair full-duplex |
| 100M-baseFX-full | 100M optical-fiber |
| 1G-baseT-half | 1G twisted-pair half-duplex |
| 1G-baseT-full | 1G twisted-pair full-duplex |
| 1G-baseX | 1G optical-fiber |
| 2.5G-baseT | 2.5G twisted-pair full-duplex |
| 2.5G-baseX | 2.5G optical-fiber |
| 5G-baseT | 5G twisted-pair full-duplex |
| 10G-baseT | 10G twisted-pair full-duplex |
| 10G-baseSR-LR | 10G optical-fiber |
| 10G-baseCR | 10G twinaxial-copper |
| 40G-baseSR4-LR4 | 4x10G optical-fiber |
| 40G-baseCR4 | 4x10G twinaxial-copper |
| 25G-baseSR-LR | 25G optical-fiber |
| 25G-baseCR | 25G twinaxial-copper |
| 50G-baseSR2-LR2 | 2x25G optical-fiber |
| 50G-baseCR2 | 2x25G twinaxial-copper |
| 100G-baseSR4-LR4 | 4x25G optical-fiber |
| 100G-baseCR4 | 4x25G twinaxial-copper |
| 50G-baseSR-LR | 50G optical-fiber |
| 50G-baseCR | 50G twinaxial-copper |
| 100G-baseSR2-LR2 | 2x50G optical-fiber |
| 100G-baseCR2 | 2x50G twinaxial-copper |
| 200G-baseSR4-LR4 | 4x50G optical-fiber |
| 200G-baseCR4 | 4x50G twinaxial-copper |
| 400G-baseSR8-LR8 | 8x50G optical-fiber |
| 400G-baseCR8 | 8x50G twinaxial-copper |

:::info
**Link Mode Naming Scheme**

**Transmission Rates**: The first number followed by 'M' or 'G' (e.g., 10M, 100M, 1G) represents the data transmission rates in megabits or gigabits per second.

**Interface Types**: The symbols after "base" indicate the interface types:

- **T**: Stands for twisted pair cabling, followed by the duplex mode (either half or full).
- **SR-LR**: Stands for "short-range" and "long-range" optical modules, including other variants like LRM, ER, ZR, etc. These link modes should be used with optical modules.
- **CR**: Stands for twin-axial copper and is used with direct attach cable (DAC). For 1Gbps DAC, the appropriate link mode is 1G-baseX.
- **FX:** Stands for Fast Ethernet over Fiber optic cable. This also includes LX - long-wavelength standard.

**Number of Lines**:

- **SR2-LR2/CR2**: means two lines.
- **SR4-LR4/CR4**: means four lines.
- **SR8-LR8/CR8:** means eight lines.

:::

Before manually configuring the advertise bits for your interface, first determine which bits are supported by executing the command `/interface/ethernet/monitor` and checking the "supported" list. You can also view the advertise bits supported by your transceiver under the "sfp-supported" field. Additionally, the "advertising" will show the bits that RouterOS has automatically set. The list is generated by comparing the maximum available link mode values on your interface and transceiver and selecting the ones that match.

```ros
[admin@MikroTik] > /interface/ethernet/monitor qsfp28-1-1
                      name: qsfp28-1-1
                 supported: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full,
                            1G-baseX,2.5G-baseT,2.5G-baseX,5G-baseT,10G-baseT,10G-baseSR-LR,10G-baseCR,40G-baseSR4-LR4,
                            40G-baseCR4,25G-baseSR-LR,25G-baseCR,50G-baseSR2-LR2,50G-baseCR2,100G-baseSR4-LR4,100G-baseCR4
             sfp-supported: 10G-baseSR-LR,25G-baseSR-LR,100G-baseSR4-LR4
               advertising: 10G-baseSR-LR,25G-baseSR-LR,100G-baseSR4-LR4
... 
```

One application where manually set advertise settings could be used is for all sub-interfaces under QSFP. The overall configuration process starts with the topmost enabled port. If the chosen mode is valid and supported, it will be applied. If that particular link mode requires multiple lanes, the advertise and speed configuration of the next interface is ignored, but the interface should remain **enabled**. The next available free lane or port follows a similar process.

```ros
/interface/ethernet
set [ find default-name=qsfp28-1-1 ] advertise=50G-baseCR2
set [ find default-name=qsfp28-1-3 ] advertise=25G-baseCR
set [ find default-name=qsfp28-1-4 ] advertise=25G-baseCR
```

:::warning
**Note**: Multiple-channel interface link modes (50G-baseCR2, 50G-baseSR2-LR2 ) can not be configured for a single-channel interface (SFP28/SFP56).

IEEE 802.3az Energy Efficient Ethernet (EEE) capabilities are disabled on all our products. There is no option to manually enable or disable EEE settings.
:::

### Ethernet LED behavior

#### Green LED (Link/Speed)  

- On (solid) – max rate

#### Yellow/Amber LED (Activity/Speed)

- On (solid) - link established.  
- Off – No link.  
- Blinking – Data is being transmitted.

### Forced Mode

In the situation when a warning message appears in the log records after connecting the DAC cable or optical module, as an example:

```ros
10:20:47 interface,warning sfp-sfpplus1 module auto-initialization failed, try forced-mode
```

This may indicate that the connected cable or module has a corrupted or bad EEPROM checksum, which causes the automatic connection configuration to fail. This functionality was introduced in RouterOS version 7.12 and may affect some links that worked in the past by mistake with wrongly assumed module/cable attributes, which could lead to various problems related to link connection and device functionality.

In such cases, you can attempt to set the link mode manually, and this might help establish a working link. The following forced port setting examples are provided:

- For DAC cables and connection speeds of 1G/10G/25G.

```ros
/interface/ethernet
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=1G-baseX
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=10G-baseCR
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=25G-baseCR
```

:::info
Note: When selecting the interface speed setting, pay attention to what rates your DAC cable supports (check cable specification data)
:::

- For optical modules and connection speeds of 1G/10G/25G.

```ros
/interface/ethernet
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=1G-baseX
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=10G-baseSR-LR
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=25G-baseSR-LR
```

:::warning
Note: When selecting the interface speed setting, pay attention to what rates your optical module supports (check module specification data)

Modules with bad EEPROM checksum do not output any EEPROM information to the Ethernet monitor, which will also mean that the SFP DDM monitor does not work for such modules.
:::

### FEC

FEC (Forward Error Correction) is a digital signal processing method that improves the bit error rate of SFP28, QSFP+, and QSFP28 links by adding information (parity bits) to the data at the transmitter side. The receiver side then uses this information to detect and correct errors that may have been introduced during transmission.

To ensure a successful link, the same *fec-mode* should be used on both ends of the link. RouterOS uses a disabled *fec-mode* as the default setting, but it can be changed to *fec74* (also known as FC-FEC) or *fec91* (also known as RS-FEC). For more information on FEC mode options, refer to the [property](./ethernet.md#properties) description. The table below shows link modes and supported FEC modes:

| Link Modes (for advertise and speed properties) | Supported FEC modes |
| :-- | :-- |
| 40G-baseSR4-LR4 | fec74 |
| 40G-baseCR4 | fec74 |
| 25G-baseSR-LR | fec74, fec91\* |
| 25G-baseCR | fec74, fec91\* |
| 50G-baseSR2-LR2 | fec74, fec91 |
| 50G-baseCR2 | fec74, fec91 |
| 100G-baseSR4-LR4 | fec91 |
| 100G-baseCR4 | fec91 |
| 50G-baseSR-LR | fec91 (required) |
| 50G-baseCR | fec91 (required) |
| 100G-baseSR2-LR2 | fec91 (required) |
| 100G-baseCR2 | fec91 (required) |
| 200G-baseSR4-LR4 | fec91 (required) |
| 200G-baseCR4 | fec91 (required) |
| 400G-baseSR8-LR8 | fec91 (required) |
| 400G-baseCR8 | fec91 (required) |

:::warning
**Note**: The CCR2004-1G-2XS-PCIe device does not support fec91 on SFP28 interfaces.
:::

## Properties

**Sub-menu:** `/interface/ethernet`

This section describes the Ethernet interface configuration options.

| Property | Description |
| :-- | :-- |
| **advertise** (since RouterOS v7.12: *10M-baseT-half \| 10M-baseT-full\| 100M-baseT-half \| 100M-baseT-full \| 1G-baseT-half \| 1G-baseT-full \| 1G-baseX \| 2.5G-baseT \| 2.5G-baseX \| 5G-baseT \| 10G-baseT \| 10G-baseSR-LR \| 10G-baseCR \| 40G-baseSR4-LR4 \| 40G-baseCR4 \| 25G-baseSR-LR \| 25G-baseCR \| 50G-baseSR2-LR2 \| 50G-baseCR2 \| 100G-baseSR4-LR4 \| 100G-baseCR4;* Default: )  (older RouterOS: *10M-full \| 10M-half \| 100M-full \| 100M-half \| 1000M-full \| 1000M-half \| 2500M-full \| 5000M-full \| 10000M-full*; Default: ) | Advertised link modes, only applies when auto-negotiation is enabled. Advertising higher speeds than the actual interface supported speed can result in undefined behavior. Multiple options are allowed. |
| **arp** (*disabled \| enabled \| local-proxy-arp \| proxy-arp \| reply-only*; Default: **enabled**) | Address Resolution Protocol mode:disabled - the interface will not use ARPenabled - the interface will use ARPlocal-proxy-arp - the router performs proxy ARP on the interface and sends replies to the same interfaceproxy-arp - the router performs proxy ARP on the interface and sends replies to other interfacesreply-only - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the ARP table. No dynamic entries will be automatically stored in the ARP table. Therefore for communications to be successful, a valid static entry must already exist. |
| **arp-timeout** (*auto \| integer*; Default: **auto**) | How long the ARP record is kept in the ARP table after no packets are received from IP. Value `auto` equals the value of `arp-timeout` in IP/Settings, default is 30s. |
| **auto-negotiation** (*yes \| no*; Default: **yes**) | When enabled, the interface "advertises" its maximum capabilities to achieve the best connection possible.Note1: Auto-negotiation should not be disabled on one end only, otherwise Ethernet Interfaces may not work properly.Note2: Gigabit Ethernet and NBASE-T Ethernet links cannot work with auto-negotiation disabled. |
| **bandwidth** (*integer/integer*; Default: **unlimited/unlimited**) | Sets max rx/tx bandwidth in kbps that will be handled by an interface. TX limit is supported on all Atheros [switch-chip](../bridging-and-switching/switch-chip-features.md) ports. RX limit is supported only on Atheros8327/QCA8337 switch-chip ports. |
| **cable-setting** (*default \| short \| standard*; Default: **default**) | Changes the cable length setting (only applicable to NS DP83815/6 cards) |
| **combo-mode** (*auto \| copper \| sfp*; Default: **auto**) | When auto mode is selected, the port that was first connected will establish the link. In case this link fails, the other port will try to establish a new link. In case of a reboot, any of the two ports can be running, it depends on which port will successfully establish the link first. When sfp mode is selected, the interface will only work through SFP/SFP+ cage. When copper mode is selected, the interface will only work through RJ45 Ethernet port. |
| **comment** (*string*; Default: ) | Descriptive name of an item |
| **disable-running-check** (*yes \| no*; Default: **yes**) | Disable running check. If this value is set to 'no', the router automatically detects whether the NIC is connected with a device in the network or not. The default value is 'yes' because older NICs do not support it. (relevant only to CHR and x86) |
| **fec-mode**(*auto \| fec74 \| fec91 \| off;* Default: **auto**) | Changes Forward Error Correction (FEC) mode for SFP28, QSFP+ and QSFP28 interfaces. The same mode should be used on both link ends, otherwise FEC mismatch could result in non-working link or even false link-ups.  **It is recommended to enable FEC, particularly when creating a link between CRS3xx, CRS5xx series switches. Some optical modules might rely on FEC functionality in MACs.** auto - same as offfec74 - enables IEEE 802.3 clause 74 FEC (aka FC-FEC), can be used with 25Gbps, 40Gbps and 50Gbps link modesfec91 - enables IEEE 802.3 clause 91 FEC (aka RS-FEC), can be used with 25Gbps, 50Gbps, 100Gbps, 200Gbps and 400Gbps link modesoff - disables FEC. |
| **tx-flow-control** (*on \| off \| auto*; Default: **off**) | When set to on, the port will generate pause frames to the upstream device to temporarily stop the packet transmission. Pause frames are only generated when some router's output interface is congested and packets cannot be transmitted anymore. **auto** is the same as **on** except when auto-negotiation=yes flow control status is resolved by taking into account what the other end advertises. |
| **rx-flow-control** (*on \| off \| auto*; Default: **off**) | When set to on, the port will process received pause frames and suspend transmission if required. **auto** is the same as **on** except when auto-negotiation=yes flow control status is resolved by taking into account what other end advertises. |
| **full-duplex** (*yes \| no*; Default: **yes**) | Defines whether the transmission of data appears in two directions simultaneously, only applies when auto-negotiation is disabled. Since RouterOS v7.12, the setting is replaced with new speed link modes. |
| **l2mtu** (*integer [0..65536]*; Default: ) | Layer2 Maximum transmission unit. [Read more](../hardware/mtu-in-routeros.md). |
| **mac-address** (*MAC*; Default: ) | Media Access Control number of an interface. |
| **mdix-enable** (*yes \| no*; Default: **yes**) | Whether the MDI/X auto cross over cable correction feature is enabled for the port (Hardware specific, e.g. ether1 on RB500 can be set to yes/no. Fixed to 'yes' on other hardware.) |
| **mtu** (*integer [0..65536]*; Default: **1500**) | Layer3 Maximum transmission unit |
| **name** (*string*; Default: ) | Name of an interface |
| **orig-mac-address** (*read-only: MAC*; Default: ) | Original Media Access Control number of an interface. |
| **passthrough-interface** (*interface*; Default: ) | Sets an interface in passthrough mode on the CCR2004-1G-2XS-PCIe device. By default, the PCIe interface will show up as four virtual Ethernet interfaces. Two interfaces in passthrough mode to the 25G SFP28 cages. The remaining two virtual Ethernet-PCIe interfaces are bridged with the Gigabit Ethernet port for management access. |
| **poe-out** (*auto-on \| forced-on \| off*; Default: **off**) | Poe Out settings. [`Read more`](../hardware/poe-out.mdx). |
| **poe-priority** (*integer [0..99]*; Default: ) | Poe Out settings. [`Read more`](../hardware/poe-out.mdx). |
| **sfp-shutdown-temperature** (*integer*; Default: **95** \| **80**) | The temperature in Celsius at which the interface will be temporarily turned off due to too high detected SFP module temperature (introduced v6.48). The default value for SFP/SFP+/SFP28 interfaces is 95, and for QSFP+/QSFP28 interfaces 80 (introduced v7.6). |
| **sfp-rate-select**(*high \| low*; Default: **high**) | Allows control of the rate select pin for SFP ports. |
| **speed** (since RouterOS v7.12: *10M-baseT-half \| 10M-baseT-full\| 100M-baseT-half \| 100M-baseT-full \| 1G-baseT-half \| 1G-baseT-full \| 1G-baseX \| 2.5G-baseT \| 2.5G-baseX \| 5G-baseT \| 10G-baseT \| 10G-baseSR-LR \| 10G-baseCR \| 40G-baseSR4-LR4 \| 40G-baseCR4 \| 25G-baseSR-LR \| 25G-baseCR \| 50G-baseSR2-LR2 \| 50G-baseCR2 \| 100G-baseSR4-LR4 \| 100G-baseCR4;* Default: )  (older RouterOS: *10Mbps \| 10Gbps \| 100Mbps \| 1Gbps \| 2.5Gbps \| 5Gbps \| 25Gbps \| 40Gbps \| 100Gbps*; Default: ) | Sets interface data transmission speed which takes effect only when auto-negotiation is disabled. Setting higher speeds than the actual interface supported speed can result in undefined behavior. Single option is allowed. |

**Read-only properties**

| Property | Description |
| :-- | :-- |
| **running** (*yes \| no*) | Whether the interface is running. Note that some interfaces do not have running check and they are always reported as "running". |
| **slave** (*yes \| no*) | Whether the interface is configured as a slave of another interface (for example [Bonding](../high-availability-solutions/bonding.md) or [Bridge](../bridging-and-switching/index.md) |
| **switch** (*integer*) | ID to which the switch chip interface belongs. |

## Menu specific commands

| Property | Description |
| :-- | :-- |
| **blink** (*[id, name]*) | Blink Ethernet leds |
| **monitor** (*[id, name]*) | Monitor ethernet status. [Read more](./ethernet.md#monitor). |
| **reset-counters** (*[id, name]*) | Reset stats counters. [Read more](./ethernet.md#stats). |
| **reset-mac-address** (*[id, name]*) | Reset MAC address to manufacturer's default. |
| **cable-test** (*string*) | Shows detected problems with cable pairs. [`Read More`](./ethernet.md#detect-cable-problems). |

## Monitor

To print out the current link rate and other Ethernet-related properties or to see detailed diagnostic information for transceivers, use the `/interface/ethernet/monitor` command. The provided information can differ for different interface types (e.g. Ethernet over twisted pair or SFP interface) or for different transceivers (e.g. SFP and QSFP).

### Properties

| Property | Description |
| :-- | :-- |
| **advertising** (since RouterOS v7.12: *10M-baseT-half \| 10M-baseT-full\| 100M-baseT-half \| 100M-baseT-full \| 1G-baseT-half \| 1G-baseT-full \| 1G-baseX \| 2.5G-baseT \| 2.5G-baseX \| 5G-baseT \| 10G-baseT \| 10G-baseSR-LR \| 10G-baseCR \| 40G-baseSR4-LR4 \| 40G-baseCR4 \| 25G-baseSR-LR \| 25G-baseCR \| 50G-baseSR2-LR2 \| 50G-baseCR2 \| 100G-baseSR4-LR4 \| 100G-baseCR4*) (older RouterOS: *10M-full \| 10M-half \| 100M-full \| 100M-half \| 1000M-full \| 1000M-half \| 2500M-full \| 5000M-full \| 10000M-full*) | Advertised link modes only apply when auto-negotiation is enabled |
| **auto-negotiation** (*disabled \| done \| failed \| incomplete*) | Current auto-negotiation status:disabled - negotiation disableddone - negotiation completedfailed - negotiation failedincomplete - negotiation not completed yet |
| **default-cable-settings** (*short \| standard*) | Default cable length setting (only applicable to NS DP83815/6 cards)short - supports short cablesstandard - supports standard cables |
| **fec** (*fec74 \| fec91 \| off*) | Current FEC mode. |
| **full-duplex** (*yes \| no*) | Whether transmission of data occurs in two directions simultaneously |
| **link-partner-advertising** (since RouterOS v7.12: *10M-baseT-half \| 10M-baseT-full\| 100M-baseT-half \| 100M-baseT-full \| 1G-baseT-half \| 1G-baseT-full \| 1G-baseX \| 2.5G-baseT \| 2.5G-baseX \| 5G-baseT \| 10G-baseT \| 10G-baseSR-LR \| 10G-baseCR \| 40G-baseSR4-LR4 \| 40G-baseCR4 \| 25G-baseSR-LR \| 25G-baseCR \| 50G-baseSR2-LR2 \| 50G-baseCR2 \| 100G-baseSR4-LR4 \| 100G-baseCR4*) (older RouterOS: *10M-full \| 10M-half \| 100M-full \| 100M-half \| 1000M-full \| 1000M-half \| 2500M-full \| 5000M-full \| 10000M-full*) | Link partner advertised link modes only apply when auto-negotiation is enabled |
| **rate** (*10Mbps \| 100Mbps \| 1Gbps \| 2.5Gbps \| 5Gbps \| 10Gbps \| 25Gbps \| 40Gbps \| 50Gbps \| 100Gbps \| 200Gbps \| 400Gbps*) | Actual data rate of the connection. |
| **status** (*link-ok \| no-link \| unknown*) | Current link status of an interfacelink-ok - the card is connected to the networkno-link - the card is not connected to the networkunknown - the connection is not recognized (if the card does not report connection status) |
| **tx-flow-control** (*yes \| no*) | Whether TX flow control is used |
| **rx-flow-control** (*yes \| no*) | Whether RX flow control is used |
| **combo-state** (*copper \| sfp*) | Used combo-mode for combo interfaces |
| **sfp-module-present** (*yes \| no*) | Whether a transceiver is in the cage |
| **sfp-rx-loss** (*yes \| no*) | Whether a receiver signal is lost |
| **sfp-tx-fault** (*yes \| no*) | Whether a transceiver transmitter is in fault state |
| **sfp-type** (*SFP/SFP+/SFP28/SFP56 \| DWDM-SFP/SFP+ \| QSFP \| QSFP+ \| QSFP28/QSFP56 \| QSFPDD*) | Used transceiver type |
| **sfp-cmis-revision** *(string)* | Transceiver CMIS revision number |
| **sfp-connector-type** (*SC \| LC \| optical-pigtail \| copper-pigtail \| multifiber-parallel-optic-1x12 \| multifiber-parallel-optic-1x16 \| no-separable-connector \| RJ45*) | Used transceiver connector type |
| **sfp-link-length-9um** (*m*) | Transceiver supported link length for single mode 9/125um fiber |
| **sfp-link-length-sm** *(km)* | Transceiver supported link length for single mode fiber |
| **sfp-link-length-om3** *(m)* | Transceiver supported link length for multi mode (OM3) |
| **sfp-link-length-om4** *(m)* | Transceiver supported link length for multi mode (OM4) |
| **sfp-link-length-om5** *(m)* | Transceiver supported link length for multi mode (OM5) |
| **sfp-link-length-om2** *(m)* | Transceiver supported link length for multi mode 50/125um fiber (OM2) |
| **sfp-link-length-om1** *(m)* | Transceiver supported link length for multi mode 62.5/125um fiber (OM1) |
| **sfp-link-length-copper** *(m)* | Supported link length of copper transceiver |
| **sfp-vendor-name** (*string*) | Transceiver manufacturer |
| **sfp-vendor-part-number** (*string*) | Transceiver part number |
| **sfp-vendor-revision** (*string*) | Transceiver revision number |
| **sfp-vendor-serial** (*string*) | Transceiver serial number |
| **sfp-manufacturing-date** (*date*) | Transceiver manufacturing date |
| **sfp-power-class** *(string)* | Transceiver power class |
| **sfp-max-power** *(W)* | Transceiver maximum power consumption |
| **sfp-wavelength** (*nm*) | Transceiver transmitter optical signal wavelength |
| **sfp-temperature***(C)* | Transceiver temperature |
| **sfp-supply-voltage** *(V)* | Transceiver supply voltage |
| **sfp-tx-bias-current** *(mA)* | Transceiver Tx bias current |
| **sfp-tx-power** *(dBm)* | Transceiver transmitted optical power |
| **sfp-rx-power** *(dBm)* | Transceiver received optical power |
| **sfp-supported**(*10M-baseT-half \| 10M-baseT-full\| 100M-baseT-half \| 100M-baseT-full \| 1G-baseT-half \| 1G-baseT-full \| 1G-baseX \| 2.5G-baseT \| 2.5G-baseX \| 5G-baseT \| 10G-baseT \| 10G-baseSR-LR \| 10G-baseCR \| 40G-baseSR4-LR4 \| 40G-baseCR4 \| 25G-baseSR-LR \| 25G-baseCR \| 50G-baseSR2-LR2 \| 50G-baseCR2 \| 100G-baseSR4-LR4 \| 100G-baseCR4 \| 50G-baseSR-LR \| 50G-baseCR \| 100G-baseSR2-LR2 \| 100G-baseCR2 \| 200G-baseSR4-LR4 \| 200G-baseCR4 \| 400G-baseSR8-LR8 \| 400G-baseCR8*) | Module supported link modes. This property only applies to certain devices. |
| **supported** (*10M-baseT-half \| 10M-baseT-full\| 100M-baseT-half \| 100M-baseT-full \| 1G-baseT-half \| 1G-baseT-full \| 1G-baseX \| 2.5G-baseT \| 2.5G-baseX \| 5G-baseT \| 10G-baseT \| 10G-baseSR-LR \| 10G-baseCR \| 40G-baseSR4-LR4 \| 40G-baseCR4 \| 25G-baseSR-LR \| 25G-baseCR \| 50G-baseSR2-LR2 \| 50G-baseCR2 \| 100G-baseSR4-LR4 \| 100G-baseCR4 \| 50G-baseSR-LR \| 50G-baseCR \| 100G-baseSR2-LR2 \| 100G-baseCR2 \| 200G-baseSR4-LR4 \| 200G-baseCR4 \| 400G-baseSR8-LR8 \| 400G-baseCR8*) | Shows the supported interface hardware link mode capabilities. |
| **eeprom-checksum** *(good \| bad)* | Whether EEPROM checksum is correct |
| **eeprom** *(hex dump)* | Raw EEPROM of the transceiver |

Example output of an Ethernet status:

```ros
[admin@MikroTik] > /interface/ethernet/monitor ether2 
                      name: ether2
                    status: link-ok
          auto-negotiation: done
                      rate: 1Gbps
               full-duplex: yes
           tx-flow-control: no
           rx-flow-control: no
                 supported: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full
               advertising: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full
  link-partner-advertising: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full
```

Example output of an SFP status:

```ros
[admin@MikroTik] > /interface/ethernet/monitor sfp3
                      name: sfp3
                    status: link-ok
          auto-negotiation: done
                       rate: 1Gbps
                full-duplex: yes
            tx-flow-control: no
           rx-flow-control: no
                 supported: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full,1G-baseX
             sfp-supported: 1G-baseX
               advertising: 1G-baseX
  link-partner-advertising: 
        sfp-module-present: yes
               sfp-rx-loss: no
              sfp-tx-fault: no
                  sfp-type: SFP/SFP+/SFP28/SFP56
        sfp-connector-type: LC
       sfp-link-length-om1: 500m
       sfp-link-length-om2: 550m
           sfp-vendor-name: Mikrotik
    sfp-vendor-part-number: S-85DLC05D
         sfp-vendor-serial: SG85M31401687
    sfp-manufacturing-date: 13-04-24
            sfp-wavelength: 850nm
           sfp-temperature: 33C
        sfp-supply-voltage: 3.237V
       sfp-tx-bias-current: 2mA
              sfp-tx-power: -5.792dBm
              sfp-rx-power: -5.22dBm
           eeprom-checksum: good
                    eeprom: 0000: 03 04 07 00 00 00 01 00  00 00 00 03 0d 00 00 00  ........ ........
                            0010: 37 32 00 00 4d 69 6b 72  6f 74 69 6b 20 20 20 20  72..Mikr otik    
                            0020: 20 20 20 20 00 00 00 00  53 2d 38 35 44 4c 43 30      .... S-85DLC0
                            0030: 35 44 20 20 20 20 20 20  00 00 00 00 03 52 00 50  5D       .....R.P
                            0040: 00 1a 00 00 53 47 38 35  4d 33 31 34 30 31 36 38  ....SG85 M3140168
                            0050: 37 20 20 20 31 33 30 34  32 34 20 20 68 b0 01 f3  7   1304 24  h...
                            0060: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ........ ........
                            *
                            0080: 64 00 d2 ff 5a 00 d7 ff  8c a0 75 30 88 b8 79 18  d...Z... ..u0..y.
                            0090: 75 30 00 fa 61 a8 01 f4  1f 07 03 1a 18 a5 03 e7  u0..a... ........
                            00a0: 31 2e 00 13 27 12 00 27  00 00 00 00 00 00 00 00  1...'..' ........
                            00b0: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ........ ........
                            00c0: 00 00 00 00 3f 80 00 00  00 00 00 00 01 00 00 00  ....?... ........
                            00d0: 01 00 00 00 01 00 00 00  01 00 00 00 00 00 00 23  ........ .......#
                            00e0: 21 7c 7e 72 05 27 0a 4b  0b be 00 00 00 00 00 94  !|~r.'.K ........
                            00f0: 00 00 00 00 00 00 00 00  20 21 2a ff ff ff ff 00  ........  !*.....

```

## Detect Cable Problems

A cable test can detect problems or measure the approximate cable length if the cable is unplugged on the other end and there is, therefore, "no-link". RouterOS will show:

- which cable pair is damaged
- the distance to the problem
- how exactly the cable is broken - short-circuited or open-circuited

This also works if the other end is simply unplugged - in that case, the total cable length will be shown.

Here is an example output:

```ros
[admin@CCR] > interface ethernet cable-test ether2 
name: ether2 
status: no-link 
cable-pairs: open:4,open:4,open:4,open:4
```

In the above example, the cable is not shorted but “open” at 4 meters distance; all cable pairs are equally faulty at the same distance from the switch chip.

Currently `cable-test` is implemented on the following devices:

| Devices |  |  |
| :-- | :-- | :-- |
| CCR1xxx series | RB952Ui-5ac2nD | RBLHGG-5acD |
| CRS1xx series | RB962UiGS-5HacT2HnT | RB5009 series (eth1) |
| CRS2xx series | RB1100AHx2 | C52iG-5HaxD2HaxD |
| OmniTIK series | RB1100x4 | C53UiG+5HPaxD2HPaxD |
| RB450G series | RBD52G-5HacD2HnD | S53UG+5HaxD2HaxD series |
| RB951 series | RBD53G-5HacD2HnD series | H53UiG-5HaxQ2HaxQ |
| RB2011 series | RBcAPGi-5acD2nD |  |
| RB4011 series | RBmAPL-2nD |  |
| RB750Gr2 | RBmAP2nD |  |
| RB750UPr2 | RBwsAP-5Hac2nD |  |
| RB751U-2HnD | RB3011UiAS-RM |  |
| RB850Gx2 | RBMetal 2SHPn |  |
| RB931-2nD | RBDynaDishG-5HacD |  |
| RB941-2nD | RBLDFG-5acD |  |

:::warning
Currently `cable-test` is not supported on Combo ports.
:::

## Stats

Using the `/interface/ethernet/print stats` command, it is possible to see a wide range of Ethernet-related statistics. The list of statistics can differ between RouterBoard devices due to different Ethernet drivers. The list below contains all available counters across all RouterBoard devices. Most of the Ethernet statistics can be remotely monitored using [SNMP](../diagnostics-monitoring-and-troubleshooting/snmp.md) and MIKROTIK-MIB.

| Property | Description |
| :-- | :-- |
| **driver-rx-byte** (*integer*) | Total count of received bytes on device CPU |
| **driver-rx-packet** (*integer*) | Total count of received packets on device CPU |
| **driver-tx-byte** (*integer*) | Total count of transmitted bytes by device CPU |
| **driver-tx-packet** (*integer*) | Total count of transmitted packets by device CPU |
| **fc-fec-block-corrected** (*integer*) | Total count of FC-FEC corrected blocks. Applies only when fec74 mode is used. |
| **fc-fec-block-uncorrected** (*integer*) | Total count of FC-FEC uncorrected blocks. Applies only when fec74 mode is used. |
| **fc-fec-rx-block** (*integer*) | Total count of FC-FEC received blocks. Applies only when fec74 mode is used. |
| **rs-fec-corrected** (*integer*) | Total count of RS-FEC corrected codewords. Applies only when fec91 mode is used. |
| **rs-fec-symbol-error** (*integer*) | Total count of RS-FEC symbol errors. Applies only when fec91 mode is used. |
| **rs-fec-uncorrected** (*integer*) | Total count of RS-FEC uncorrected codewords. Applies only when fec91 mode is used. |
| **rx-64** (*integer*) | Total count of received 64 byte frames |
| **rx-65-127** (*integer*) | Total count of received 65 to 127 byte frames |
| **rx-128-255** (*integer*) | Total count of received 128 to 255 byte frames |
| **rx-256-511** (*integer*) | Total count of received 256 to 511 byte frames |
| **rx-512-1023** (*integer*) | Total count of received 512 to 1023 byte frames |
| **rx-1024-1518** (*integer*) | Total count of received 1024 to 1518 byte frames |
| **rx-1519-max** (*integer*) | Total count of received frames larger than 1519 bytes |
| **rx-align-error** (*integer*) | Total count of received align error events - packets where bits are not aligned along octet boundaries |
| **rx-broadcast** (*integer*) | Total count of received broadcast frames |
| **rx-bytes** (*integer*) | Total count of received bytes |
| **rx-carrier-error** (*integer*) | Total count of received frames with carrier sense error |
| **rx-code-error** (*integer*) | Total count of received frames with code error |
| **rx-control** (*integer*) | Total count of received control or pause frames |
| **rx-error-events** (*integer*) | Total count of received frames with the active error event |
| **rx-fcs-error** (*integer*) | Total count of received frames with incorrect checksum |
| **rx-fragment** (*integer*) | Total count of received fragmented frames (not related to IP fragmentation) |
| **rx-ip-header-checksum-error** (*integer*) | Total count of received frames with IP header checksum error |
| **rx-jabber** (*integer*) | Total count of received jabbed packets - a packet that is transmitted longer than the maximum packet length |
| **rx-length-error** (*integer*) | Total count of received frames with frame length error |
| **rx-multicast** (*integer*) | Total count of received multicast frames |
| **rx-overflow** (*integer*) | Total count of received overflowed frames that can be caused when device resources are insufficient to receive a certain frame |
| **rx-pause** (*integer*) | Total count of received pause frames |
| **rx-runt** (*integer*) | Total count of received frames shorter than the minimum 64 bytes, usually caused by collisions |
| **rx-tcp-checksum-error** (*integer*) | Total count of received frames with TCP header checksum error |
| **rx-too-long** (*integer*) | Total count of received frames that were larger than the maximum supported frame size by the network device, see the max-l2mtu property |
| **rx-too-short** (*integer*) | Total count of received frames shorter than the minimum 64 bytes |
| **rx-udp-checksum-error** (*integer*) | Total count of received frames with UDP header checksum error |
| **rx-unicast** (*integer*) | Total count of received unicast frames |
| **rx-unknown-op** (*integer*) | Total count of received frames with unknown Ethernet protocol |
| **tx-64** (*integer*) | Total count of transmitted 64 byte frames |
| **tx-65-127** (*integer*) | Total count of transmitted 65 to 127 byte frames |
| **tx-128-255** (*integer*) | Total count of transmitted 128 to 255 byte frames |
| **tx-256-511** (*integer*) | Total count of transmitted 256 to 511 byte frames |
| **tx-512-1023** (*integer*) | Total count of transmitted 512 to 1023 byte frames |
| **tx-1024-1518** (*integer*) | Total count of transmitted 1024 to 1518 byte frames |
| **tx-1519-max** (*integer*) | Total count of transmitted frames larger than 1519 bytes |
| **tx-align-error** (*integer*) | Total count of transmitted align error events - packets where bits are not aligned along octet boundaries |
| **tx-broadcast** (*integer*) | Total count of transmitted broadcast frames |
| **tx-bytes** (*integer*) | Total count of transmitted bytes |
| **tx-collision** (*integer*) | Total count of transmitted frames that made collisions |
| **tx-control** (*integer*) | Total count of transmitted control or pause frames |
| **tx-deferred** (*integer*) | Total count of transmitted frames that were delayed on their first transmit attempt due to already busy medium |
| **tx-drop** (*integer*) | Total count of transmitted frames that were dropped due to the already full output queue |
| **tx-excessive-collision** (*integer*) | Total count of transmitted frames that already made multiple collisions and never got successfully transmitted |
| **tx-excessive-deferred** (*integer*) | Total count of transmitted frames that were deferred for an excessive period of time due to an already busy medium |
| **tx-fcs-error** (*integer*) | Total count of transmitted frames with incorrect checksum |
| **tx-fragment** (*integer*) | Total count of transmitted fragmented frames (not related to IP fragmentation) |
| **tx-carrier-sense-error** (*integer*) | Total count of transmitted frames with carrier sense error |
| **tx-late-collision** (*integer*) | Total count of transmitted frames that made a collision after being already halfway transmitted |
| **tx-multicast** (*integer*) | Total count of transmitted multicast frames |
| **tx-multiple-collision** (*integer*) | Total count of transmitted frames that made more than one collision and were subsequently transmitted successfully |
| **tx-overflow** (*integer*) | Total count of transmitted overflowed frames |
| **tx-pause** (*integer*) | Total count of transmitted pause frames |
| **tx-all-queue-drop-byte** (*integer*) | Total count of transmitted bytes dropped by all output queues |
| **tx-all-queue-drop-packet** (*integer*) | Total count of transmitted packets dropped by all output queues |
| **tx-queueX-byte** (*integer*) | Total count of transmitted bytes on a certain queue, the **X** should be replaced with a queue number |
| **tx-queueX-packet** (*integer*) | Total count of transmitted frames on a certain queue, the **X** should be replaced with a queue number |
| **tx-runt** (*integer*) | Total count of transmitted frames shorter than the minimum 64 bytes, usually caused by collisions |
| **tx-too-short** (*integer*) | Total count of transmitted frames shorter than the minimum 64 bytes |
| **tx-rx-64** (*integer*) | Total count of transmitted and received 64 byte frames |
| **tx-rx-64-127** (*integer*) | Total count of transmitted and received 64 to 127 byte frames |
| **tx-rx-128-255** (*integer*) | Total count of transmitted and received 128 to 255 byte frames |
| **tx-rx-256-511** (*integer*) | Total count of transmitted and received 256 to 511 byte frames |
| **tx-rx-512-1023** (*integer*) | Total count of transmitted and received 512 to 1023 byte frames |
| **tx-rx-1024-max** (*integer*) | Total count of transmitted and received frames larger than 1024 bytes |
| **tx-single-collision** (*integer*) | Total count of transmitted frames that made only a single collision and were subsequently transmitted successfully |
| **tx-too-long** (*integer*) | Total count of transmitted packets that were larger than the maximum packet size |
| **tx-underrun** (*integer*) | Total count of underrun frames which can be caused when device resources are insufficient to transmit a certain frame |
| **tx-unicast** (*integer*) | Total count of transmitted unicast frames |

For example, the output of Ethernet stats on the hAP ac2 device:

```ros
[admin@MikroTik] > /interface/ethernet/print stats
                      name:           ether1 ether2         ether3        ether4 ether5
            driver-rx-byte:  182 334 805 898      0  5 836 927 820    24 895 692      0
          driver-rx-packet:    4 449 562 546      0  4 320 155 362       259 449      0
            driver-tx-byte:   15 881 099 971      0 70 502 669 211    60 498 056     53
          driver-tx-packet:       52 724 428      0     54 231 229       106 498      1
                  rx-bytes:  178 663 398 808      0  5 983 590 739 1 358 140 795      0
              rx-too-short:                0      0              0             0      0
                     rx-64:       12 749 144      0        362 459       125 917      0
                 rx-65-127:        9 612 406      0     20 366 513       292 189      0
                rx-128-255:        6 259 883      0      1 672 588       261 013      0
                rx-256-511:        2 950 578      0        211 380       278 147      0
               rx-512-1023:        3 992 258      0        185 666       163 241      0
              rx-1024-1518:      119 034 611      0      2 796 559       696 254      0
               rx-1519-max:                0      0              0             0      0
               rx-too-long:                0      0              0             0      0
              rx-broadcast:       12 025 189      0      1 006 377        64 178      0
                  rx-pause:                0      0              0             0      0
              rx-multicast:        4 687 869      0         36 188       220 136      0
              rx-fcs-error:                0      0              0             0      0
            rx-align-error:                0      0              0             0      0
               rx-fragment:                0      0              0             0      0
               rx-overflow:                0      0              0             0      0
                  tx-bytes:   16 098 535 973      0 72 066 425 886   225 001 772      0
                     tx-64:        1 063 375      0        924 855        37 877      0
                 tx-65-127:       26 924 514      0      2 442 200       959 209      0
                tx-128-255:       14 588 113      0        924 746       295 961      0
                tx-256-511:        1 323 733      0      1 036 515        33 252      0
               tx-512-1023:        1 287 464      0      2 281 554         3 625      0
              tx-1024-1518:        7 537 154      0     48 212 304        64 659      0
               tx-1519-max:                0      0              0             0      0
               tx-too-long:                0      0              0             0      0
              tx-broadcast:              590      0        145 800       823 038      0
                  tx-pause:                0      0              0             0      0
              tx-multicast:                0      0      1 039 243        41 716      0
               tx-underrun:                0      0              0             0      0
              tx-collision:                0      0              0             0      0
    tx-excessive-collision:                0      0              0             0      0
     tx-multiple-collision:                0      0              0             0      0
       tx-single-collision:                0      0              0             0      0
     tx-excessive-deferred:                0      0              0             0      0
               tx-deferred:                0      0              0             0      0
         tx-late-collision:                0      0              0             0      0
```
