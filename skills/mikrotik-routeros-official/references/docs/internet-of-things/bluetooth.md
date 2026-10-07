# Bluetooth

> This page documents MikroTik RouterOS's Bluetooth IoT functionality, covering Bluetooth channel structure, advertising packet formats, and configuration via the /iot/bluetooth submenu. It explains PDU types, antenna...

# Bluetooth

This section covers Bluetooth-based IoT examples. Use it to configure Bluetooth tag tracking and integrate collected data with MQTT and ThingsBoard.

<DocCardList />

Bluetooth is a short-range wireless technology that allows broadcasting the data over specific Bluetooth channels.

There are 40 unique bands (channels) and each band has a 2 MHz separation. Channels 37, 38, and 39 are used for primary advertising, and 0-36 are used for data transmission.

During the advertising process, the BLE advertising packet is broadcasted. This packet contains the Preamble, Access Address, PDU and CRC fields.

The Preamble and Access Address fields help the receiver detect frames. The CRC field is used to check errors. The PDU consists of PDU Header and PDU Payload. The PDU defines the packet itself.

PDU Header contains information about the PDU type. Based on the type, the payload fields may differ.

For example, when the PDU type is ADV\_NOCONN\_IND → the PDU Payload consists of "AdvA" (a field that contains information about the advertiser's address) and "AdvData" (a field that contains data information) fields:

1 octet = 1 byte = 8 bits

| Name | Length |
| :-- | :-- |
| Preamble | 1 octet | |
| Access-Address | 4 octets |
| PDU | PDU Header = 2 octetsPDU Payload = AdvA (6 octets)+AdvData (0...31 octets) |
| CRC | 3 octets |

There are different PDU types:

- ADV\_IND (where payload consists of AdvA [6octets] + AdvData [0-31 octets] and which is used for connectable, scannable undirected advertising).
- ADV\_NOCONN\_IND (where payload consists of AdvA [6octets] + AdvData [0-31 octets] and which is used for non-connectable, non-scannable undirected advertising).
- ADV\_SCAN\_IND (where payload consists of AdvA [6octets] + AdvData [0-31 octets] and which is used for scannable, undirected advertising).
- SCAN\_REQ (where payload consists of ScanA [6octets] + AdvA [6octets], where the ScanA field contains scanner's address and AdvA contains advertiser's address, and which is used for requesting SCAN\_RSP response).
- SCAN\_RSP (where payload consists of AdvA [6octets] + ScanRspData [0-31 octets], where ScanRspData can contain any data from the advertiser's host and which is used to respond to a SCAN\_REQ request).
- ADV\_DIRECT\_IND (where payload consists of AdvA [6octets] + TargetA [6octets], where TargetA is the device address field to which the PDU is addressed, and which is used for connectable, directed advertising).
- Etc.

You can find more information about the packet structure over [here](https://www.bluetooth.com/specifications/specs/core-specification/) (Bluetooth specifications).

The main application for the Bluetooth interface in RouterOS is to monitor Bluetooth advertising packets (scanner feature) that are broadcast by other devices (like for example, [Bluetooth tags](https://help.mikrotik.com/docs/display/UM/TG-BT5-IN)) or broadcast advertising packets (advertiser feature).

## Configuration

**Sub-menu:** `/iot/bluetooth`

:::info
**iot** package is required for a device with a built-in Bluetooth chip, like the [KNOT](https://mikrotik.com/product/knot) or [KNOT Embedded LTE](https://mikrotik.com/product/knot_embedded_lte4).

If your device is ARM, ARM64 architecture and it has a USB slot, the **iot-bt-extra** package can enable Bluetooth functionality via a USB-Bluetooth dongle. Not all Bluetooth adapters were tested. Adapters must support **LE 4.0+**. There is no "peripheral" list yet.

**Iot** package is available with RouterOS version 6.48.3. **Iot-bt-extra package** is available with RouterOS 7.18. You can get them from our [download page](https://mikrotik.com/download) - under "Extra packages".
:::

### Devices

In this menu you can check and set general Bluetooth chip parameters:

```ros
/iot/bluetooth/print
Columns: NAME, PUBLIC-ADDRESS, RANDOM-STATIC-ADDRESS, ANTENNA
  #  NAM  PUBLIC-ADDRESS     RANDOM-STATIC-ADD  ANTENNA 
  0  bt1  00:00:00:00:00:00  F4:4E:E8:04:77:3A  internal
/iot/bluetooth/set
```

***note**:* Public address is the IEEE registered, permanent address. This address can not be changed. In the "print" example above, the device does not have a public address assigned (all octets are set to 0).

Configurable settings are shown below:

| Property | Description |
| :-- | :-- |
| **antenna** (*string*; Default: internal) | Choose whether to use an internal or an external Bluetooth antenna |
| **name** (*string*; Default: ) | Descriptive name of Bluetooth chip/interface |
| **random-static-address** (*MAC address*; Default: ) | A user-configurable address for the Bluetooth chip |

You can monitor chip stats with the command:

```ros
/iot/bluetooth/print stats
Columns: NAME, RX-BYTES, TX-BYTES, RX-ERRORS, TX-ERRORS, RX-EVT, TX-CMD, RX-ACL, TX-ACL
  #  NAM  RX-BYTE  TX-  R  T  RX-EV  TX  R  T
  0  bt1  1857835  235  0  0  46677  45  0  0
```

### Advertisers

In this menu, it is possible to set up the Bluetooth chip to broadcast advertising packets. You can check and set advertiser settings with the commands:

```ros
/iot/bluetooth/advertisers/print
Flags: X - DISABLED
Columns: DEVICE, MIN-INTERVAL, MAX-INTERVAL, OWN-ADDRESS-TYPE, CHANNEL-MAP, AD-SIZE
#   DEVICE  MIN-INTERVAL  MAX-INTERVAL  OWN-ADDRESS-TYPE  CHANNEL-MAP  AD-SIZE
0 X bt1     1280ms        2560ms        random-static              37        0
                                                                   38         
                                                                   39         
/iot/bluetooth/advertisers/set
```

Configurable settings are shown below:

| Property | Description |
| :-- | :-- |
| **ad-structures** (*string*; Default: ) | Choose a pre-configured structure for the advertisement packets. For more information see the "AD structures" section. |
| **channel-map** (*37 \| 38 \| 39*; Default: 37, 38, 39) | Channels used for advertising. |
| **disabled** (*yes \| no*; Default: **yes**) | An option to disable or enable the Bluetooth chip to broadcast advertising packets. |
| **max-interval** (*integer:*20..10240;** Default: **2560** **ms**) | The maximal interval for broadcasting advertising packets. |
| **min-interval** (*integer:*20..10240;** Default: **1280 ms**) | The minimal interval for broadcasting advertising packets. |
| **own-address-type** (*public \| random-static \| rpa-fallback-to-public \| rpa-fallback-to-random*; Default: **random-static**) | The MAC address that is going to be used in the advertising packet's payload: public →  To use the IEEE registered, permanent address.random-static →  To use a user-configurable address (will be changed on the next power-cycle).rpa-fallback-to-public → To use a Resolvable Random Private Address (RPA) that can only be resolved if the receiver has our Identity Resolving Key (IRK). If RPA can not be generated, the public address will be used instead.rpa-fallback-to-random → Same as "rpa-fallback-to-public" but if RPA can not be generated, the random-static address will be used instead. |
| **phy** (*1M \| 2M \| CODED*; default: **1M**) | Set the "physical layer" for the device to use during advertising: CODED → the lowest rate of 125 kbps = longer range;1M → the standard rate of 1 Mbps = average range;2M → the highest rate of 2 Mbps = short range;**Important:** CODED is only supported by [KNOT Embedded LTE](https://mikrotik.com/product/knot_embedded_lte4).  |
| **legacy** (*yes \| no*) | Set the advertising type → extended or legacy.  When using `legacy=no`, AD structure length is extended up to 191 bytes. When using `legacy=yes`, AD structure length is limited to 31 bytes.  Legacy advertising uses only the "primary" Bluetooth channel to advertise the payload. Extended advertising uses "primary" and "secondary" channels at the same time.  |

***note**:* Advertising packets will be broadcasted each *min-interval* \<= **X** \<= *max-interval* milliseconds.

### AD structures

This section allows you to define the payload for the advertising packets that are going to be broadcasted by the Bluetooth chip.

Currently, only 4 types are supported: 0x08 "Shortened Local Name"; 0x09 "Complete Local Name"; 0xFF "Manufacturer Specific Data"; "Service Data"

You can check and set "AD structures" settings with the commands:

```ros
/iot/bluetooth/advertisers/ad-structures/print
Columns: NAME, TYPE, DATA
#  NAME  TYPE              DATA
0  test  short-local-name  TEST
/iot/bluetooth/advertisers/ad-structures/set 
```

Configurable properties are shown below:

| Property | Description |
| :-- | :-- |
| **data** (*string*; Default: ) | Defines advertising packet's AdvData part of the payload |
| **name**(*string*; Default: ) | Descriptive name of AD structure |
| **type** (complete-local-name \| manufacturer-data \| short-local-name \| service-data; Default: ) | An option to set AD structure's type: 0x08 "Shortened Local Name" (in "text" format)0x09 "Complete Local Name" (in "text" format)0xFF "Manufacturer Specific Data" (in "hex" format)0x20 "Service Data 32-bit" (in "hex" format) |

If, for example, the "Shortened Local Name" type is chosen and the "data" field is configured with "TEST" → the AdvData part of the payload is going to look like this:

05 08 54 45 53 54 (hexadecimal format)

, where the first octet (05) shows the number of bytes to follow (5 bytes) and the second octet (08) shows the type (Shortened Local Name). 3rd, 4th, 5th and 6th (etc.) octets are the "data" [54 (hex)=**T** (ASCII), 45 (hex)=**E** (ASCII), 53 (hex)=**S** (ASCII), 54 (hex)=**T** (ASCII)].

The same applies to the "Complete Local Name" type. Only the second octet in the AdvData payload is going to differ and will be set to 09.

For the "Manufacturer Specific Data" type, you will need to configure the "data" field in the hexadecimal format. The second octet for this type is going to be set to FF.

### Connections

:::info
Available starting with v**7.12beta9**.
:::

Currently, only the `central` role is supported. `Peripheral device` role, `pairing` and `encryption` options are not supported.

Available sections are:

| Section | Description |
| :-- | :-- |
| async-data | used to view subscribed data. |
| characteristics | used to view all supported characteristics of the device. |
| connect | used to connect to the device that is in the `connactable` state. |
| disconnect | used to disconnect from the device. |
| read | used to read characteristics values. |
| write | used to write characteristics values. |
| subscribe | used to subscribe to a characteristic value. |
| unsubscribe | used to unsubscribe from a characteristic value. |

In order to connect to a Bluetooth device that is in the `connectable` state, use the command (where `pdev` is the device address):

```ros
/iot/bluetooth/connections/connect pdev=DC:2C:6E:0F:C0:3D
```

:::info
To connect to TG-BT5-IN/OUT tags, make sure to put them into the `connectable` state by applying a magnet to the magnetic switch.
:::

To view an already established connection:

```ros
/iot/bluetooth/connections/print
```

To view device characteristics:

```ros
/iot/bluetooth/connections/characteristics/print
Columns: PDEV, NAME, UUID
 #  PDEV               NAME                              UUID                            
 0  DC:2C:6E:0F:C0:3D  Service Changed                   2a05                            
 1  DC:2C:6E:0F:C0:3D  Database Hash                     2b2a                            
 2  DC:2C:6E:0F:C0:3D  Client Supported Features         2b29                            
 3  DC:2C:6E:0F:C0:3D  Device Name                       2a00                            
 4  DC:2C:6E:0F:C0:3D  Appearance                        2a01                            
...
...
...
```

To read a specific characteristic, specify the `pdev` address and the `uuid`:

```ros
/iot/bluetooth/connections/read pdev=DC:2C:6E:0F:C0:3D uuid=2a00
```

### Scanners

In this menu, you can set up the scanner settings for the Bluetooth chip. When disabled, the device is no longer able to receive advertising reports. When enabled, you can monitor advertising reports in the "Advertising reports" tab (which will be explained later in the guide). You can check and set scanner settings with the commands:

```ros
/iot/bluetooth/scanners/print
Flags: X - DISABLED
Columns: DEVICE, TYPE, INTERVAL, WINDOW, OWN-ADDRESS-TYPE, FILTER-POLICY, FILTER-DUPL
ICATES
#   DEVICE  TYPE     INTERVAL  WINDOW  OWN-ADDRESS-TYPE  FILTER-POLICY  FIL
0 X bt1     passive  10ms      10ms    random-static     default        off
/iot/bluetooth/scanners/set
```

Configurable properties are shown below:

| Property | Description |
| :-- | :-- |
| **disabled** (*yes \| no*; Default: **no**) | An option to disable or enable the Bluetooth chip to receive advertising reports. |
| **filter-duplicates** (keep-newest \| keep-oldest \| keep-unique \| off; Default: **off**) | An option to discard duplicate advertisements from the same advertiser: keep-newest → Keeps the newest report (discards the oldest). Only the newest PDU from a single AdvA will be kept.keep-oldest → Keeps the oldest report (discards the newest). Only the oldest PDU from a single AdvA will be kept. This type of PDU filtering happens at the controller level and as such it's the most efficient (energy/bandwidth-wise) method of duplicate filtering.keep-unique → Only displays advertisements that have a unique payload. Meaning, if 1+ identical payloads (AdvData) are found, only the first payload is going to be displayed, while the "clones" are discarded/ignored.off → Duplicates are not discarded. All PDUs with the same AdvA will be kept.**Important:** A duplicate advertising report is an advertising report sent from the same device address. The actual data ("AdvData" part of the payload) may change/differ and it is not considered significant when determining duplicate advertising reports. Meaning that, for example, if the Bluetooth interface receives 10 payloads (payload after payload with a 1-second interval) from the same tag:  if you are using the "keep-oldest" setting → Bluetooth interface will only display the first payload received (9 follow-up payloads will be filtered out) from that tag.if you are using the "keep-newest" setting → Bluetooth interface will only display the last payload received (each follow-up payload will rewrite the previous one) from that tag. |
| **filter-policy** (default \| whitelist *\| no*; Default: **default**) | An option to set up a filtering policy (controller-level advertisement filtering): default → When this policy is enabled, the scanner will only accept ADV_IND, ADV_NOCONN_IND, ADV_SCAN_IND, SCAN_RSP, and ADV_DIRECT_IND (where TargetA is the scanner's own Bluetooth address) PDU types.whitelist → When this policy is enabled, the scanner will only accept ADV_IND, ADV_NOCONN_IND, ADV_SCAN_IND, SCAN_RSP PDU types that are broadcasted by the advertiser, whose address is configured in the "Whitelist" section, and ADV_DIRECT_IND type PDU (where TargetA is the scanner's own Bluetooth address). |
| **interval** (*integer:3..10240*;** Default: **10 ms**) | Time after which the scanner will start scanning the next advertisement channel. |
| **own-address-type** (*public \| random-static \| rpa-fallback-to-public \| rpa-fallback-to-random*; Default: **random-static**) | Address type used in scan requests (if active scanning type is used): public →  To use the IEEE registered, permanent address.random-static →  To use a user-configurable address (will be changed on the next power-cycle).rpa-fallback-to-public → To use a Resolvable Random Private Address (RPA) that can only be resolved with our Identity Resolving Key (IRK). If RPA can not be generated, the public address will be used instead.rpa-fallback-to-random → Same as "rpa-fallback-to-public" but if RPA can not be generated, the random-static address will be used instead. |
| **type** (*active \| passive;* Default: **passive**) | Defines the scanner's type: active → Scanner can send scan requests if it receives a scannable advertisement. The scanner can send a SCAN_REQ in order to acquire a SCAN_RSP response.passive → Scanner will only listen for advertisements, no data (e.g. scan requests) will be sent. |
| **window** (*integer:3..10240;* Default: **10 ms**) | The time that the scanner will spend scanning a single advertisement channel. |
| **phy** (*1M \| 2M \| CODED*; default: **1M**) | Set the "physical layer" for the device to use during scanning: CODED → the lowest rate of 125 kbps = longer range;1M → standard rate of 1 Mbps = average range;2M → the highest rate of 2 Mbps = short range;**Important:** CODED is only supported by [KNOT Embedded LTE](https://mikrotik.com/product/knot_embedded_lte4).     |

For example, if the scanner interval is set to 20ms, it means that only after 20ms, the device will begin scanning the next channel in line. If the scanner window is set to 10ms, it means that the device will scan each channel only during that 10ms window. This means it will scan channel 37 for 10ms (window time) and begin scanning the next channel after 10 more ms (20ms[interval]-10ms[window]). It will take 10ms to scan channel 38, and after 10 more ms, the device will begin scanning channel 39.

The scanner will be able to capture both "extended" and "legacy" advertising types at the same time.

### Advertising reports

In this section, it is possible to monitor Bluetooth advertising reports (from the nearby broadcasters). The list is limited to 1024 entries (if the list gets full with 1024 entries, each new payload received will overwrite the "oldest" one). You can monitor advertising reports with the command:

```ros
/iot/bluetooth/scanners/advertisements/print      
Columns: DEVICE, PDU-TYPE, TIME, ADDRESS-TYPE, ADDRESS, RSSI
 #  DEV  PDU-TYPE        TIME                  ADDRES  ADDRESS            RSSI  
 0  bt1  adv-noconn-ind  2021-07-28 09:30:56  public  2C:C8:1B:93:16:49  -24dBm
 1  bt1  adv-noconn-ind  2021-07-28 09:30:56  random  0B:16:17:9E:7B:EF  -60dBm
```

It is possible to set up a filter for the reports with the command:

```ros
/iot/bluetooth/scanners/advertisements/print where  
```

For example, to print reports that are broadcasted by a specific Bluetooth address, use the command:

```ros
/iot/bluetooth/scanners/advertisements/print where address=XX:XX:XX:XX:XX:XX
 # DEVICE    PDU-TYPE       TIME                 ADD... ADDRESS                    RSSI     LENGTH DATA    
79 bt1       adv-noconn-ind 2021-07-28 09:46:38 public XX:XX:XX:XX:XX:XX        -70dBm         30 02010...
80 bt1       adv-noconn-ind 2021-07-28 09:46:43 public XX:XX:XX:XX:XX:XX        -67dBm         30 02010...
81 bt1       adv-noconn-ind 2021-07-28 09:46:44 public XX:XX:XX:XX:XX:XX        -70dBm         28 1bff0...
82 bt1       adv-noconn-ind 2021-07-28 09:46:48 public XX:XX:XX:XX:XX:XX        -75dBm         30 02010...
```

To show only advertising reports that have RSSI stronger than -30 dBm, use the command:

```ros
/iot/bluetooth/scanners/advertisements/print where rssi > -30
 # DEVICE         PDU-TYPE       TIME                 ADDRESS-TYPE ADDRESS                    RSSI     LENGTH DATA       
307 bt1            adv-noconn-ind 2021-07-29 10:11:31 public       2C:C8:1B:93:16:49        -24dBm         22 15ff4f09.>
308 bt1            adv-noconn-ind 2021-07-29 10:11:31 public       2C:C8:1B:93:16:49        -26dBm         22 15ff4f09.>
```

Possible filters (you can filter the list of advertising reports with the help of the following parameters):

| Filter | Description |
| :-- | :-- |
| **address** | Bluetooth advertiser's address |
| **address-type** | Advertiser's address type (for example, public or random) |
| **data** | Advertisement data in hex format (AdvData payload) |
| **device** | Bluetooth chip/interface name |
| **epoch** | Milliseconds since Unix Epoch |
| **filter-comment** | Comment of the matching whitelist filter |
| **length** | Advertisement data length |
| **pdu-type** | Advertisement PDU type |
| **rssi** | Signal strength |
| **time** | Time of the advertisement packet reception |

### Whitelist

In this tab, it is possible to configure a whitelist that is going to be used in the filter policy in the "Scanners" section. In other words, it is an option to specify which Bluetooth addresses are going to be scanned (displayed in the "Advertising reports").

You can view the whitelisted entries with the command:

```ros
/iot/bluetooth/whitelist/print
Columns: DEVICE, ADDRESS-TYPE, ADDRESS
# DEVICE  ADDRESS-TYPE  ADDRESS    
0 bt1     any           *:*:*:*:*:*
```

You can add a new whitelist entry with the command:

```ros
/iot/bluetooth/whitelist/add
```

### Configurable properties

| Property | Description |
| :-- | :-- |
| **address** (*MAC address*; Default: ) | Advertiser's address |
| **address-type** (*any \| public \| random*; Default:) | Advertiser's address type |
| **comment**(*string*; Default: ) | Short description of the whitelisted entry |
| **copy-from** | An option to copy an entry - for more information check the [console commands](../../developer-guides/scripting/index.md#common-commands) |
| **device** (*bt1*; Default: ) | Select the Bluetooth interface/chip name |
| **disabled** (*yes \| no*; Default: ) | An option to disable or to enable the entry |

:::info
Only 8 whitelisted entries can be added prior to the **7.14beta8** version.  
Starting with the **7.14beta8** version, the whitelist is no longer limited to 8 entries and the address field supports asterisk wildcards.
:::

If, for example, you want to whitelist all MAC addresses that begin with the "DC:2C:..." octets, add an entry using wildcard asterisk characters:

```ros
/iot/bluetooth/whitelist/add address=DC:2C:*:*:*:*
```

Wildcard asterisk cannot be used in-between specific octets, like `AA:*:*:BB:*:*` (it is an invalid entry).

Valid entries would be:

- `AA:BB:CC:DD:*:*`
- `AA:BB:CC:DD:EE:*`
- `AA:*:*:*:*:*`

### Peripheral Devices

This section displays decoded Eddystone TLM, Eddystone UID, iBeacon and MikroTik Bluetooth payloads. If the "Peripheral Devices" capture other beacon types, they will not be decoded.

You can view a decoded list with a `print detail` command:

```ros
/iot/bluetooth/peripheral-devices/print detail 
 0 address-type=public address=60:C0:BF:87:E2:1C name="60:C0:BF:87:E2:1C" persist=no 
   mtik-key="" rssi=-64 
   last-data="0201041BFFCD0960C0BF87E21C025B1F198B21AC62CDAE0045FAFEFE057D7B" 
   last-seen=2023-08-22 11:20:09 beacon-types="" 

 1 address-type=public address=DC:2C:6E:0F:C0:3D name="DC:2C:6E:0F:C0:3D" persist=no 
   mtik-key="" rssi=-47 
   last-data="0303AAFE1716AAFE00E5B2B98DE4C81C47C2B14E7500000000000000" 
   last-seen=2023-08-22 11:20:05 beacon-types=mikrotik,ibeacon,eddystone-uid 
   mtik-version=1 mtik-encrypted=no mtik-acc-x=-0.007G mtik-acc-y=-0.015G 
   mtik-acc-z=-0.007G mtik-temperature=23.808C mtik-battery=100% 
   mtik-uptime=14342160s mtik-flags="" 
   ibeacon-uuid="55555555-5555-5555-5555-222222222222" ibeacon-major=1280 
   ibeacon-minor=512 ibeacon-rssi-at-1m=-68dBm eddy-rssi-at-1m=-27dBm 
   eddy-namespace="b2b98de4c81c47c2b14e" eddy-instance="750000000000" 

 2 address-type=public address=DC:2C:6E:F6:54:7D name="DC:2C:6E:F6:54:7D" persist=no 
   mtik-key="" rssi=-74 
   last-data="0201060303AAFE1116AAFE20000B701549023532D802384F46" 
   last-seen=2023-08-22 11:20:13 beacon-types=eddystone-tlm eddy-version=0 
   eddy-battery-voltage=2.928V eddy-temperature=21.285C eddy-packet-count=37040856 
   eddy-uptime=3724474.2s 

 3 address-type=public address=DC:2C:6E:0F:C0:3E name="DC:2C:6E:0F:C0:3E" persist=no 
   mtik-key="" rssi=-72 last-data="15FF4F0901000214FFFF0200FDFF4F1774E00F000064" 
   last-seen=2023-08-22 11:20:06 beacon-types=mikrotik mtik-version=1 
   mtik-encrypted=no mtik-acc-x=-0.003G mtik-acc-y=0.007G mtik-acc-z=-0.011G 
   mtik-temperature=23.308C mtik-battery=100% mtik-uptime=1040500s mtik-flags="" 

 4 address-type=public address=60:C0:BF:20:9A:50 name="60:C0:BF:20:9A:50" persist=no 
   mtik-key="" rssi=-66 
   last-data="0201041BFF4160C0BF209A50FFA4CA8906E48C0377DCFDD2DF7AF02FFC6AC5" 
   last-seen=2023-08-22 11:20:11 beacon-types="" 
```

You can filter the list, for example, based on the "address" of the device (knowing the MAC-address of the tag):

```ros
/iot/bluetooth/peripheral-devices/print detail where address="DC:2C:6E:0F:C0:3E"
 0 address-type=public address=DC:2C:6E:0F:C0:3E name="my_tag" persist=yes 
   mtik-key="" rssi=-60 last-data="15FF4F090100669DFCFF0600FCFF6117F1E50F000064" 
   last-seen=2023-08-22 11:43:31 beacon-types=mikrotik mtik-version=1 
   mtik-encrypted=no mtik-acc-x=-0.015G mtik-acc-y=0.023G mtik-acc-z=-0.015G 
   mtik-temperature=23.378C mtik-battery=100% mtik-uptime=1041905s mtik-flags=""

/iot/bluetooth/peripheral-devices/print value-list where address="DC:2C:6E:0F:C0:3E"
      address-type: public
           address: DC:2C:6E:0F:C0:3E
              name: my_tag
           persist: yes
          mtik-key: 
              rssi: -71
         last-data: 15FF4F0901002AC60400000004004F17D4E90F000064
         last-seen: 2023-08-22 12:00:06
      beacon-types: mikrotik
      mtik-version: 1
    mtik-encrypted: no
        mtik-acc-x: 0.015G
        mtik-acc-y: 0G
        mtik-acc-z: 0.015G
  mtik-temperature: 23.308C
      mtik-battery: 100%
       mtik-uptime: 1042900s
        mtik-flags: 
```

Or, for example, filter the list based on the beacon type:

```ros
/iot/bluetooth/peripheral-devices/print detail where beacon-types=mikrotik 
 0 address-type=public address=DC:2C:6E:0F:C0:3E name="my_tag" persist=yes 
   mtik-key="" rssi=-69 last-data="15FF4F0901000747020002000100611778E60F000064" 
   last-seen=2023-08-22 11:45:46 beacon-types=mikrotik mtik-version=1 
   mtik-encrypted=no mtik-acc-x=0.007G mtik-acc-y=0.007G mtik-acc-z=0.003G 
   mtik-temperature=23.378C mtik-battery=100% mtik-uptime=1042040s mtik-flags="" 

 7 address-type=public address=2C:C8:1B:4B:BB:0A name="2C:C8:1B:4B:BB:0A" persist=no 
   mtik-key="" rssi=-44 last-data="15FF4F09010077090000FCFFFDFFD519BF9EFF00005B" 
   last-seen=2023-08-22 11:45:53 beacon-types=mikrotik mtik-version=1 
   mtik-encrypted=no mtik-acc-x=0G mtik-acc-y=-0.015G mtik-acc-z=-0.011G 
   mtik-temperature=25.832C mtik-battery=91% mtik-uptime=16752319s mtik-flags="" 
```

Additionally, you have the option to set `persist=yes`, which will make sure that the device/tag stays on the list forever (because devices that stop broadcasting payloads will be timed out after one minute and removed from the list until new payloads start appearing in the air):

```ros
/iot/bluetooth/peripheral-devices/set persist=yes address="DC:2C:6E:0F:C0:3E"
```

You can also set a name for the device, so you can more easily find it on the list, with the command:

```ros
/iot/bluetooth/peripheral-devices/set name="my_tag" address="DC:2C:6E:0F:C0:3E"
```

### Decode-ad

In this menu, you can decode static MikroTik, Eddystone TLM, Eddystone UID and iBeacon payloads.

To decode a payload, just input it into the "data" field:

```ros
/iot/bluetooth/decode-ad data=0201060303AAFE1116AAFE20000B6E158402353AF20238576B 
             type: eddystone-tlm
          version: 0
  battery-voltage: 2.926V
      temperature: 21.515C
     packet-count: 37042930
           uptime: 3724682.7s

/iot/bluetooth/decode-ad data=15FF4F090100032E0100FFFF00004F17C1E80F000064      
         type: mikrotik
      version: 1
    encrypted: no
        acc-x: 0.003G
        acc-y: -0.003G
        acc-z: 0G
  temperature: 23.308C
       uptime: 1042625s
        flags: 
      battery: 100%
```
