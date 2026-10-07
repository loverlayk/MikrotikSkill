# LTE/5G

> This page documents LTE and 5G configuration in MikroTik RouterOS, covering interface setup, APN profiles, LTE settings, and operational modes including MBIM support in RouterOS v7. It includes CLI commands for...

# LTE/5G

```ros
Package: system
Optional lte-mipsbe.npk package is only required for SXT 3-7 built-in modem.
```

Support for Direct-IP mode type cards only. MBIM support is available in RouterOS v7 releases and the MBIM driver is loaded automatically. If the modem is not recognized in RouterOS v6. Please test it in v7 releases before asking for support in RouterOS v6.

To enable access via a PPP interface instead of an LTE Interface, change the operational mode to "serial" with `/interface/lte/settings/set mode=serial` CLI command and issue a reboot. Note that using PPP emulation mode you may not get the same throughput speeds as using the LTE interface emulation type.

:::warning
For RouterOS v7 the `ignore-direct-modem` parameter was renamed to `mode` and moved to `/interface/lte/settings` menu.
:::

### LTE Client

**Sub-menu:** `/interface/lte`

#### Properties

| Property | Description |
| :-- | :-- |
| **allow-roaming** (*yes \| no*; Default: **no**) | Enable data roaming for connecting to other countries' data-providers. Not all LTE modems support this feature. Some modems, that do not fully support this feature, will connect to the network but will not establish an IP data connection with allow-roaming set to no. |
| **apn-profile** (*string*; Default: **default**) | Which APN profile to use for this interface (old deprecated value "apn-profiles" still accepted for single APN configuration, for multi-apn see the [Multi APN](#multi-apn) section)|
| **band** (*integer list*; Default: **""**) | LTE Frequency band used in communication `LTE Bands and bandwidths` |
| **nr-band** (*integer list*; Default: "") | 5G NR Frequency band used in communication `5G NR Bands and bandwidths` |
| **comment** (*string*; Default: **""**) | Descriptive name of an item |
| **disabled** (*yes \| no*; Default: **no**) | Whether the interface is disabled or not. By default it is enabled. |
| **modem-init** (*string*; Default: **""**) | Modem init string (AT command that will be executed at modem startup) |
| **mtu** (*integer \| auto*; Default: **1500**) | Maximum Transmission Unit. Max packet size that the LTE interface will be able to send without packet fragmentation. auto - use network advertised MTU for modems that support it (MBIM modems). Other modems will fall back to the default value (1500). |
| **name** (*string*; Default: **""**) | Descriptive name of the interface. |
| **network-mode** (*3g \| gsm \| lte \| 5g*) | Select/force RAT mode for LTE interface to operate with. For 5G NSA to work both lte and 5g network modes need to be selected! Selecting 5g alone will only allow to connect to 5G SA. |
| **operator** (*integer*; Default: **""**) | Used to lock the device to a specific operator. The full PLMN number is used for the lock consisting of MCC+MNC. [PLMN codes](https://en.wikipedia.org/wiki/Public_land_mobile_network) |
| **pin** (*integer*; Default: **""**) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | SIM Card's PIN code. |
| **sms-protocol** (*at \| auto \| mbim*) | SMS functionality.  **mbim**: uses MBIM driver.  **at**: uses AT-Commands.  **auto**: selects the appropriate option depending on the modem. |

#### APN profiles

All network-related settings are under profiles

**Sub-menu:** `/interface/lte/apn`

| Property | Description |
| :-- | :-- |
| **add-default-route** (*yes \| no*) | Whether to add a default route to forward all traffic over the LTE interface. |
| **apn** (*string*) | Service Provider's Access Point Name |
| **authentication** (*pap \| chap \| none*; Default: **none**) | Allowed protocol to use for authentication |
| **default-route-distance** (*integer*; Default: **2**) | Sets distance value applied to auto-created default route, if add-default-route is also selected. The LTE route by default has distance 2 to prefer wired routes over LTE |
| **ip-type** (*auto \| ipv4 \| ipv4-ipv6 \| ipv6*; Default:auto ) | Requested PDN type |
| **ipv6-interface** (; Default: ) | Interface on which to advertise IPv6 prefix |
| **name** (*string*; Default: ) | APN profile name |
| **number** (*integer*; Default: ) | APN profile number |
| **passthrough-interface** (; Default: ) | Interface to passthrough IP configuration (activates passthrough) |
| **passthrough-mac** (*MAC*; Default: **auto**) | If set to auto, then it will learn the MAC from the first packet |
| **passthrough-subnet-selection** (*auto / p2p*; Default: **auto**) | "auto" selects the smallest possible subnet to be used for the passthrough interface. "p2p" sets the passthrough interface subnet as /32 and picks the gateway address from the 10.177.0.0/16 range. The gateway address stays the same until the apn configuration is changed. |
| **password** (*string*; Default: ) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | Password used if any of the authentication protocols are active |
| **use-network-apn** (*yes \| no*; Default: **yes**) | Parameter is available starting from RouterOS v7 and used only for MBIM modems. If set to yes, uses the network provided APN. |
| **use-peer-dns** (*yes \| no*; Default: **yes**) | If set to yes, uses the DNS received from the LTE interface |
| **user** (*string*) | Username used if any of the authentication protocols are active |

#### LTE settings

LTE and router-specific LTE settings. The menu is available starting from RouterOS v7.

**Sub-menu:** `/interface/lte/settings`

| Property | Description |
| :-- | :-- |
| **mode** (*auto \| mbim \| serial* / *user*; *Default: **auto***) | Operation mode setting. auto - automatically selects the operation mode.serial - provides only serial portsmbim - switches modem into MBIM mode if possibleuser - OS will not attempt to automatically switch the modem mode. (Available from RouterOS 7.16) |
| **firmware-path** (*string*) | Firmware path in host OS. [Modem gobi firmware](lte-5g.md#modem-fotadfota-downloads) |
| **external-antenna** (*auto \| both \| div \| main \| none*; Default: **auto**) | This setting is only available for "Chateau" routers, except for Chateau 5G versions. auto - measures the signal levels on both internal and external antennas and selects the antennas with the best signal (RSRP).both - both antennas are set to externaldiv - diversity antenna set to externalmain - main antenna set to externalnone - no external antenna selected (using internal antennas)  |
| **external-antenna-selected** () | This setting is only available for "Chateau" routers, except for Chateau 5G versions. Shows the currently selected antenna if "**external-antenna**" is set to "auto" |
| **sim-slot** () | This setting is available for routers that have switchable SIM slots (LtAP, SXT). Selection options differ between products. |
| **esim-channel** (*auto \| at;* Default: *auto*)  | Control channel to use for esim management |
| **link-recovery-timer** (*integer* Default: *120* Range: *120..4294967295*)  | Time in seconds after which the lte interface will be reconfigured if it does not get to (R)running state |

#### LTE eSIM

```ros
RouterOS version: 7.18+
```

[MikroTips: How to activate your eSIM for the first time!](https://www.youtube.com/watch?v=v0WtU1xBB-Q)

This menu contains commands related to eSIM ([embedded Subscriber Identification Module](http://en.wikipedia.org/wiki/ESIM)) provisioning and management using RouterOS built-in LPA (eSIM [Local Profile Assistant](http://en.wikipedia.org/wiki/Remote_SIM_provisioning)).

A single eSIM chip can store multiple eSIM profiles, the maximum profile count depends on the eSIM chip used.

RouterOS LPA supports:

- AT modems whose firmware supports SIM low access commands (AT+CCHO; AT+CCHC; AT+CGLA).
- MBIM modems which support SIM low level access service in its firmware (UUID\_SERVICE\_MS\_UICC).

Other requirements:

- eSIM in SIM card form factor (physical eSIM) inserted in the RouterBoard SIM slot.
- eSIM/eUICC is present on the modem (soldered chip) and the modem is set to use this slot.
- Connectivity to eSIM SIM profile provider SM-DP+ provisioning server during provisioning and deletion of SIM profiles on the eSIM chip (for connectivity, you can use another eSIM profile or another WAN interface).
- eSIM can be provisioned only if the active slot is eSIM.
- Some devices have multiple SIM slots, and to use an eSIM, you need to switch the slot using the command "/interface/lte/settings/set sim-slot=esim".

The command `/interface/lte/esim/esim-id [find /interface/lte]` can be used to check whether the modem supports SIM low access commands and eSIM presence.

If a 3rd party modem with embedded eSIM chip is used, please consult the modem manual regarding AT commands needed to select the eSIM slot (AT!UIMS; AT+QUIMSLOT etc).

**Commands**

| Property | Description |
| :-- | :-- |
| **deactivate** | Deactivate (disable) eSIM profile. `/interface/lte/esim/deactivate number=0` |
| **activate** | Activate (enable) eSIM profile. `/interface/lte/esim/activate number=0` |
| **delete** | Permanently delete eSIM profile from the eSIM card. `/interface/lte/esim/delete number=0` |
| **print** | List the eSIM profiles installed on the eSIM `/interface/lte/esim/print` |
| **provision** | Provision new eSIM profile. The command takes four parameters: interface - the interface for which the eSIM profile will be enabled.matching-id - an activation code token. Example:  matching-id=ABCD10EFGHI5KL6Msm-dp-plus - SM-DP+ server hostnameconfirmation-code - confirmation code (a one-time password that is required in some cases)activate - Activate the newly created profile after it is provisioned (yes\|no; default: yes) [Available starting from 7.20beta6 version. Before 7.20beta6, profiles do not get activated by default after provisioning.] Example eSIM LPA string decoded from QR: **LPA:1$server.example.io$ABCD10EFGHI5KL6M** `/interface/lte/esim/provision interface=lte1 sm-dp-plus=server.example.io matching-id=ABCD10EFGHI5KL6M` |
| **esim-id** | Query the eSIM ID. The command takes one parameter: interface - select the interface for which to query the eSIM ID.`/interface/lte/esim/esim-id interface=lte1   eid: 8903302342630000000004181FFFFFFF` |
| **set-nickname** | Set a nickname for an eSIM profile. `/interface/lte/esim/set-nickname number=0 nickname=nickname1` |
| **refresh-profile-list** | Re-query the eSIM profile list. The command takes one parameter: interface - Select an interface for which the eSIM profiles will be re-queried. |

##### Devices with built in eSIM chip (MikroTik Connectivity)

:::info
These devices have pre-loaded MikroTik Connectivity eSIM profiles.
https://mikrotik.com/connectivity
:::

| Device Model | Modem |
| :-- | :-- |
| S53UG+5HaxD2HaxD-TC&RG650E-EU | RG650E-EU |
| ATLGM&RG520F-EU | RG520F-EU |
| EC25-EU&KNe | EC25-EU |

##### Modem eSIM management support table

:::note
\* These modems do not have eSIM built in. They require an external eSIM chip. For example, a physical eSIM card (eSIM in a standard SIM form factor).
:::

| Modem | Support | Comment |
| :-- | :-- | :-- |
| EC200A-EU | yes\* |  |
| EG06-A | yes\* |  |
| EG18-EA | yes\* |  |
| EG12-EA | yes\* |  |
| EG120K-EA | yes\* |  |
| RG520F-EU | yes\* |  |
| EP06-A | yes\* |  |
| RG502Q-EA | yes\* |  |
| FG621-EA | yes\* | Can't manage empty eSIM (no profiles) |
| R11e-LTE6 | yes\* | Starting from firmware revision R11e-LTE6\_V039 |
| R11e-LTE-US | no |  |
| R11e-4G | no |  |
| R11e-LTE | no |  |

#### Scanner

It is possible to scan LTE interfaces with `/interface/lte/scan` command. Example:

```ros
[admin@MikroTik] > /interface/lte/scan duration=60 number=0
Columns: OPERATOR, MCC-MNC, RSSI, RSRP, RSRQ
OPERATOR  MCC-MNC  RSSI    RSRP    RSRQ
LMT         24701  -36dBm  -63dBm  -7dB
```

Available properties:

| Property | Description |
| :-- | :-- |
| **duration** (*integer*) | Duration of scan in seconds |
| **freeze-frame-interval** (*integer*) | Time between data printout |
| **number** (*integer*) | Interface number or name |

#### Monitoring LTE details

You can monitor the LTE interface parameters with the CLI command: `/interface/lte/monitor`. It returns both cell‑level data (e.g., operator, cell ID, signal info) and modem metadata (firmware, model, SIM identifiers).

```
[admin@MikroTik] > /interface/lte/monitor lte1
            status: connected
             model: EG18-EA
          revision: EG18EAPAR01A12M4G
  current-operator: LMT
    current-cellid: 3103242
            enb-id: 12122
         sector-id: 10
        phy-cellid: 480
        data-class: LTE
    session-uptime: 15m54s
              imei: 86981604098XXXX
              imsi: 24701060267XXXX
              iccid: 8937101122102057XXXX
      primary-band: B3@20Mhz earfcn: 1300 phy-cellid: 480
     dl-modulation: qpsk
               cqi: 7
                ri: 2
               mcs: 1
              rssi: -68dBm
              rsrp: -97dBm
              rsrq: -9dB
              sinr: 6dB
```

#### LTE interface capabilities

You can check the lte interface capabilities with the `/interface/lte/show-capabilities` CLI command.

##### Example output

```
[admin@MikroTik] > interface/lte/show-capabilities lte1
  modem-bus-location: 2-1
           cell-scan: yes
        network-scan: yes
     roaming-barring: yes
  apn-address-family: IPv4,IPv6
       max-apn-count: 8
           rat-modes: 3g,lte,5g
      band-selection: yes
           lte-bands: 1,3,5,7,8,20,28,32,38,40,41,42,43
            nr-bands: 1,3,5,7,8,20,28,38,40,41,75,76,77,78
         passthrough: yes
     firmware-update: yes
   lte-attach-config: yes
             at-chat: yes
    framed-route-apn: any
```

| Capability | Description |
|------------|-------------|
| **modem-bus-location** | Physical USB bus to which the LTE modem is connected |
| **cell-scan** | `interface/lte/cell-monitor` command support |
| **network-scan** | `interface/lte/scan` command support |
| **roaming-barring** | Roaming barring support |
| **apn-address-family** | IP families supported (IPv4, IPv6) |
| **max-apn-count** | Maximum number of APN profiles that can be active simultaneously |
| **rat-modes** | Supported Radio Access Technologies (GSM, 3G, LTE, 5G) |
| **band-selection** | LTE/5G band set command support |
| **lte-bands** | List of LTE bands the modem supports |
| **nr-bands** | List of 5G bands the modem supports |
| **passthrough** | LTE passthrough support |
| **firmware-update** | `interface/lte/firmware-upgrade` support |
| **lte-attach-config** | LTE attach apn configuration support (Sets the same APN as configured) |
| **at-chat** | `interface/lte/at-chat` support |
| **framed-route-apn** | Which APN supports framed routing (Routing behind) in multi apn setup|

#### Modem firmware-upgrade command

The command allows to check and upgrade modem firmware if an update is available for supported MikroTik modems.

For firmware update availability check and installation, an active internet connection is required, depending on the modem internet connection can be provided using any  RouterOS  interface or modem interface (FOTA), please see table below regarding each modem's supported connection methods.

| Arguments / Properties | Description |
| :-- | :-- |
| **upgrade** (*yes \| no; Default: **no***) | Set command execution mode: no - displays current modem firmware version and shows latest available firmware versionyes - performs firmware installation |
| **update-channel** (*stable \| testing*; Default: **stable**)  | Sets which firmware update channel is used: stable - firmware version for general usetesting - early access/testing channel where modem firmware is published before releasing it in the stable channel Feature available from v7.17beta2. |
| **firmware-file** (*string*; Default:"" ) | Allows the user to override firmware update source and perform an upgrade from a custom location (file, url) in environments where upgrade using an internet connection to MikroTik upgrade servers is not a viable option, eg private networks etc. |

:::warning
Before attempting an LTE modem firmware upgrade - upgrade RouterOS version to the latest release [How To Upgrade RouterOS](../getting-started/installation-and-upgrade/upgrade.md)
:::

##### Modems with firmware update support and connectivity required

Use command ***`/interface/lte/monitor [find]` once*** to get the returned property "model" for installed modem model identification.

| Modem | Required connectivity to MikroTik upgrade servers |
| :-- | :-- |
| **EC200A-EU**  R11eL-EC200A-EU | Using the modem LTE interface Using any RouterOS interface (7.18beta1+) |
| **EG06-A** | Using any RouterOS interface |
| **EP06-A** | Using any RouterOS interface |
| **EG12-EA** | Using any RouterOS interface |
| **EG18-EA** | Using any RouterOS interface |
| **FG621-EA**  R11eL-FG621-EA | Using any RouterOS interface |
| **R11-LTE** | Using the modem LTE interface |
| **R11e-4G** | Using any RouterOS interface |
| **R11e-LTE6** | Using any RouterOS interface |
| **RG502Q-EA** | Using any RouterOS interface |
| **RG520F-EU** | Using any RouterOS interface |

##### Modem firmware-upgrade command examples

Check for new firmware update availability

```ros
[admin@D53G] > /interface/lte/firmware-upgrade lte1
  installed: EG12EAPAR01A13M4G_02.001.02.001
     latest: EG12EAPAR01A15M4G_01.201.01.201
```

Check for new firmware update availability in the early access/testing channel

```ros
[admin@D53G] > /interface/lte/firmware-upgrade lte1 update-channel=testing
  installed: EG12EAPAR01A15M4G_01.201.01.201
     latest: EG12EAPAR01A15M4G_01.203.01.203
```

Install the latest firmware

```ros
[admin@D53G] > /interface/lte/firmware-upgrade lte1 upgrade=yes
```

Install the latest firmware from the early access/testing channel

```ros
[admin@D53G] > /interface/lte/firmware-upgrade lte1 upgrade=yes update-channel=testing
```

Perform a firmware upgrade from a custom location (file or HTTP URL).
The interface must be in R (running) or X (disabled) state before executing the `firmware-upgrade` command.

```ros
[admin@D53G] > /interface/lte/firmware-upgrade lte1 firmware-file=R11e-LTE6_V039_image upgrade=yes

[admin@D53G] > /interface/lte/firmware-upgrade lte1 firmware-file=http://firmwareserver.com/R11e-LTE6_V039_image upgrade=yes
```

##### Modem FOTA/DFOTA Downloads

Here are all the latest FW versions for our modems:
https://box.mikrotik.com/d/bfa49081454e4da1972d/

You can use these FOTA files for offline updates or in setups where MikroTik upgrade server is not accessible for standard modem FW upgrade.

:::warning
Before attempting an LTE modem firmware upgrade, upgrade RouterOS to the latest release. [How to upgrade RouterOS](../getting-started/installation-and-upgrade/upgrade)

LTE modems are designed to reject incompatible FOTA/DFOTA firmware packages whenever possible. However, manual firmware upgrades always carry a risk. Installing an incorrect firmware image may result in modem malfunction, loss of functionality, or permanent damage that could require modem replacement.

Do not interrupt the upgrade process. Power loss, device reboot, modem reset, or any other interruption while the firmware is being written may leave the modem in an unrecoverable state.

It is the user's responsibility to verify that the firmware file is intended for the exact modem model and hardware revision being upgraded and to ensure a stable power supply throughout the upgrade process. MikroTik does not take responsibility for any damage, loss of functionality, or other issues resulting from flashing an incorrect firmware file or from interruption of the firmware upgrade process.
:::

###### FOTA modems

FOTA (Firmware Over‑The‑Air). These modems have no source-version subfolder. You can install the latest modem FW from any current FW version.

| Modem model | Note |
|---|---|
| R11e-LTE | The modem downloads the firmware itself over its LTE connection (FOTA). Offline upgrade is not possible, you can host the FW on some http server the modem can reach and upgrade the FW like that if the MikroTik upgrade server is not reachable in your setup |
| R11e-LTE6 | - |
| R11l-LTE7 | - |
| R11e-4G | - |
| EC25-EU | Modem firmware installed as an NPK package |
| EG25-G | Modem firmware installed as an NPK package |
| SXT-LTE | Only single product - RBSXTLTE3-7. Modem firmware installed as an NPK package |

###### DFOTA modems

DFOTA (Delta Firmware Over‑The‑Air). These modems have per-version subfolders `modem/<model>/<currentVersion>/<targetVersion>_image` the targetVersion is the latest available upgrade from your current FW version. If your current FW version is old, it might need multiple step upgrade.

| Modem model | Note |
|---|---|
| EC200A-EU | Supports Offline DFOTA upgrade with the latest RouterOS v7 versions. In older versions the modem downloads the firmware itself over its LTE connection |
| EP06-A | - |
| EG06-A | - |
| EG12-EA | - |
| EG18-EA | - |
| EG120K-EA | - |
| RG502Q-EA | - |
| RG520F-EU | - |
| RG520F-EUX | Special modem FW version for ATL 5G R16 (ATLGM&RG520F-EU) |
| RG650E-EU | This modem uses an A/B System Update mechanism instead of DFOTA. As the complete firmware image is written to the inactive system partition, the firmware package is significantly larger than a typical DFOTA package |
| FG621-EA | - |
| BG77 | PPP serial modem. `/interface/ppp-client/firmware-upgrade ppp-out1 upgrade=yes firmware-file=` |
| BG770A | PPP serial modem. `/interface/ppp-client/firmware-upgrade ppp-out1 upgrade=yes firmware-file=` |

#### User at-chat command

It is possible to send a user-defined "at-chat" command to the LTE interface with the `/interface/lte/at-chat` command.

```ros
[admin@MikroTik] > /interface/lte/at-chat lte1 input="AT"
  output: OK
```

It is also possible to use the "wait" parameter *wait=yes*  with the command to make "at-chat" wait for 5 seconds and return all the output instead of returning only the first received data. This is useful for some commands that return multiline output or a large block of data.

```ros
[admin@MikroTik] > /interface/lte/at-chat lte1 input="at+qcfg=?"
  output:

[admin@MikroTik] > /interface/lte/at-chat lte1 input="at+qcfg=?" wait=yes
  output: +QCFG: "rrc",(0-5)
          +QCFG: "hsdpacat",(6,8,10-24)
          +QCFG: "hsupacat",(5,6)
          +QCFG: "pdp/duplicatechk",(0,1)
          +QCFG: "risignaltype",("respective","physical")
          +QCFG: "lte/bandprior",(1-43),(1-43),(1-43)
          +QCFG: "volte_disable",(0,1)
          +QCFG: "diversity/config",(4,6),(1-4),(0)
          +QCFG: "div_test_mode",(0,1)
          +QCFG: "usbspeed",("20","30")
          +QCFG: "data_interface",(0,1),(0,1)
          +QCFG: "pcie/mode",(0,1)
          +QCFG: "pcie_mbim",(0,1)
          +QCFG: "sms_control",(0,1),(0,1)
          +QCFG: "call_control",(0,1),(0,1)
          +QCFG: "usb/maxpower",(0-900)
          +QCFG: "efratctl",(0,1)
          +QCFG: "netmaskset",(0,1)[,<netmask>]
          +QCFG: "mmwave",ant_chip,ant_type
          +QCFG: "gatewayset",(0,1)[,<gateway>]
          +QCFG: "clat",(0,1),(0,1),<prefix>,(0,32,40,48,56,64,96),<fqdn>,(0,1),(0,1,2,4,8),(0,1),(0,1),(0,1,2),(0,1,2)
          +QCFG: "usage/apmem"
          +QCFG: "enable_gea1"[,(0,1)]
          +QCFG: "dhcppktfltr",(0,1)
          OK
```

You can also use the "at-chat" function in scripts and assign command output to a variable.

```ros
[admin@MikroTik] > :global "lte_command" [/interface/lte/at-chat lte1 input="AT+CEREG?" as-value ]
[admin@MikroTik] > :put $"lte_command"
output=+CEREG: 0,1
OK
```

### Quick setup example

Start with network settings - Add new connection parameters under the LTE apn profile (provided by the network provider):

```ros
/interface/lte/apn/add name=profile1 apn=phoneprovider.net authentication=chap password=web user=web
```

Select the newly created profile for an LTE connection:

```ros
/interface/lte/set [find] apn-profile=profile1
```

The LTE interface should appear with the running (R) flag:

```ros
[admin@MikroTik] > /interface/lte/print
Flags: X - disabled, R - running
0 R name="lte1" mtu=1500 mac-address=AA:AA:AA:AA:AA:AA
```

If required, add NAT Masquerade for LTE Interface to get internet to the local network:

```ros
/ip/firewall/nat/add action=masquerade chain=srcnat out-interface=lte1
```

After the interface is added, you can use the "info" command to see what parameters the client acquired (parameters returned depend on the LTE hardware device):

```
[admin@MikroTik] > /interface/lte/monitor lte1
            status: connected
             model: EG18-EA
          revision: EG18EAPAR01A12M4G
  current-operator: LMT
    current-cellid: 3103242
            enb-id: 12122
         sector-id: 10
        phy-cellid: 480
        data-class: LTE
    session-uptime: 15m54s
              imei: 86981604098XXXX
              imsi: 24701060267XXXX
              iccid: 8937101122102057XXXX
      primary-band: B3@20Mhz earfcn: 1300 phy-cellid: 480
     dl-modulation: qpsk
               cqi: 7
                ri: 2
               mcs: 1
              rssi: -68dBm
              rsrp: -97dBm
              rsrq: -9dB
              sinr: 6dB
```

### Multi APN

Some LTE modems support multiple simultaneous APN connections. Each connection receives its own IP configuration, and in RouterOS every extra connection is exposed as a separate **APN slave LTE interface** bound to the physical modem interface (`master`).

#### Capability check

Before configuring multiple APNs, verify that the modem supports them:

```ros
[admin@MikroTik] > /interface/lte/show-capabilities lte1
            ...
       max-apn-count: 8
    framed-route-apn: any
```

| Capability | Description |
| :-- | :-- |
| **max-apn-count** | Maximum number of APN connections that can be active simultaneously. Multi APN is only available when this value is greater than `1` |
| **framed-route-apn** | Which APN supports framed routing (routing behind) in a multi APN setup |

#### Configuration

For every additional APN, create a new LTE slave interface and attach it to the physical LTE interface(master):

```ros
/interface/lte/add apn-profile=default master=lte1
```

| Property | Description |
| :-- | :-- |
| **name** | Descriptive name of the new slave interface (optional parameter, by default will create a new name using the set apn-profile) |
| **apn-profile** | APN profile to be used for the additional connection |
| **master** | The physical LTE interface that the modem is attached to (for example `lte1`) |

The slave interface behaves like a regular LTE interface: it receives its own IP configuration and can be used in routes, firewall and NAT rules independently of the master interface.

#### Example: three simultaneous APNs

Given that the router currently has default configuration, with only the default APN profile present and one lte interface:

```ros
[admin@MikroTik] > interface/lte/apn/print
Flags: * - DEFAULT
Columns: NAME, APN, IP-TYPE, ADD-DEFAULT-ROUTE, DEFAULT-ROUTE-DISTANCE
#   NAME     APN       IP-TYPE  ADD-DEFAULT-ROUTE  DEFAULT-ROUTE-DISTANCE
0 * default  internet  auto     yes                                     2

[admin@MikroTik] > interface/lte/print
Flags: R - RUNNING
Columns: NAME, MTU, NETWORK-MODE, APN-PROFILE
#   NAME   MTU  NETWORK-MODE  APN-PROFILE
0 R lte1  1500  3g            default
                lte
                5g
```

First add the new APN profiles:

```ros
[admin@MikroTik] > /interface/lte/apn add apn=internet2
[admin@MikroTik] > /interface/lte/apn add apn=internet3
```

Then add the new slave APN interfaces using the previously added APN profiles:

```ros
[admin@MikroTik] > /interface/lte/add apn-profile=internet2 master=lte1
[admin@MikroTik] > /interface/lte/add apn-profile=internet3 master=lte1
```

```ros
[admin@D53G] > interface/lte/print
Flags: R - RUNNING
Columns: NAME, MASTER, MTU, NETWORK-MODE, APN-PROFILE
#   NAME              MASTER   MTU  NETWORK-MODE  APN-PROFILE
0 R lte1                      1500  3g            default
                                    lte
                                    5g
1 R lte1.1.internet2  lte1    1500                internet2
2 R lte1.2.internet3  lte1    1500                internet3
```

#### Removing slave APN interfaces

The same as you can add new slave APN interface you can remove them with the `remove` command. In case of using 3 or more APN interfaces you can only remove starting from the last added interface, so in this case it is `lte1.2.internet3` or `numbers=2`. Trying to remove the not last interface will give an error. In 2 APN setup there is only one slave interface so there is no issues with this, but do keep this in mind for 3 and more APN setups.

```ros
[admin@MikroTik] > interface/lte/remove lte1.1.internet2
failure: only the last slave apn interface can be removed

[admin@MikroTik] > /interface/lte/remove lte1.2.internet3

[admin@MikroTik] > interface/lte/print
Flags: R - RUNNING
Columns: NAME, MASTER, MTU, NETWORK-MODE, APN-PROFILE
#   NAME              MASTER   MTU  NETWORK-MODE  APN-PROFILE
0 R lte1                      1500  3g            default
                                    lte
                                    5g
1 R lte1.1.internet2  lte1    1500                internet2
```

#### Changes from the previous method

Before 7.26beta1 version multiple APNs were configured by attaching several APN profiles to a single LTE interface with `apn-profiles` parameter which created dynamic slave interfaces:

```ros
/interface/lte/apn/add name=apn1 apn=provider1
/interface/lte/apn/add name=apn2 apn=provider2
/interface/lte/set lte1 apn-profiles=apn1,apn2
```

:::note
**Deprecation:** the `apn-profiles` parameter is deprecated starting with RouterOS 7.26. It still accepts a single APN value, but it will be removed in a future release - use `apn-profile` in new configurations.

**Configuration conversion:** On upgrade from old multi-APN configuration will automatically be converted to the new add/remove method and on downgrade will be converted back to the dynamic.
:::

### Passthrough Example

Some LTE interfaces support the LTE Passthrough feature where the IP configuration is applied directly to the client device. In this case, modem firmware is responsible for the IP configuration, and the router is used only to configure modem settings - APN, Network Technologies, and IP-Type. In this configuration, the router will not get IP configuration from the modem. The LTE Passthrough modem can pass both IPv4 and IPv6 addresses if that is supported by the modem. Some modems support multiple APNs where you can pass the traffic from each APN to a specific router interface.

Passthrough will only work for one host. The router will automatically detect the MAC address of the first received packet and use it for the Passthrough. If there are multiple hosts on the network it is possible to lock the Passthrough to a specific MAC. On the host on the network where the Passthrough is providing the IP a DHCP-Client should be enabled on that interface too. Note that it will not be possible to connect to the LTE router via a public lte IP address or from the host which is used by the passthrough. It is suggested to create an additional connection from the LTE router to the host for configuration purposes. For example, a vlan interface between the LTE router and host.

To enable Passthrough a new entry is required or the default entry should be changed in the `/interface/lte/apn` menu

:::warning
Passthrough is not supported by all chipsets.
To check if your modem supports passthrough:

```ros
/interface/lte/show-capabilities [find]
```

:::

#### Examples

To configure Passthrough on ether1:

```ros
[admin@MikroTik] > /interface/lte/apn/add apn=apn1 passthrough-interface=ether1
[admin@MikroTik] > /interface/lte/set lte1 apn-profile=apn1
```

To configure the Passthrough on ether1 host 00:0C:42:03:06:AB:

```ros
[admin@MikroTik] > /interface/lte/apn/add apn=apn1 passthrough-interface=ether1 passthrough-mac=00:0C:42:03:06:AB
[admin@MikroTik] > /interface/lte/set lte1 apn-profile=apn1
```

To configure multiple APNs on ether1 and ether2:

```ros
[admin@MikroTik] > /interface/lte/apn/add apn=apn1 passthrough-interface=ether1
[admin@MikroTik] > /interface/lte/apn/add apn=apn2 passthrough-interface=ether2
[admin@MikroTik] > /interface/lte/set lte1 apn-profile=apn1,apn2
```

To configure multiple APNs with the same APN for different interfaces:

```ros
[admin@MikroTik] > /interface/lte/apn/add name=interface1 apn=apn1
[admin@MikroTik] > /interface/lte/apn/add name=interface2 apn=apn1 passthrough-interface=ether1
[admin@MikroTik] > /interface/lte/set lte1 apn-profile=interface1
[admin@MikroTik] > /interface/lte/set lte2 apn-profile=interface2
```

Additionally, you can override the default dynamic dhcp server parameters/options by creating a DHCP server manually on the same passthrough-interface. For example, the default lease-time is 1 minute:

```routeros
[admin@MikroTik] > /ip/dhcp-server/print detail
Flags: D - dynamic; X - disabled, I - invalid
 0 D  name="apn2" interface=ether2 lease-time=1m address-pool=static-only use-radius=no lease-script="" address-lists=""
```

Now if you want to change the lease-time to, for example, 30 minutes, then you can create a new dhcp-server on the passthrough-interface, in this case, ether2:

```routeros
[admin@MikroTik] > /ip/dhcp-server/add interface=ether2 name=dhcp1 lease-time=30m
[admin@MikroTik] > /ip/dhcp-server/print detail
Flags: D - dynamic; X - disabled, I - invalid
 0    name="dhcp1" interface=ether2 lease-time=30m address-pool=static-only use-radius=no lease-script="" address-lists=""
```

### Dual SIM

#### Boards with switchable SIM slots

| RouterBoard | Modem slot | SIM slot 1 | SIM slot 2 | Switchable |
| :-- | :-- | :-- | :-- | :-- |
| LtAP | lower | 2 | 3 | Y |
|  | upper | 1 |  | N |
| LtAP mini |  | up | down | Y |
| SXT R |  | a | b | Y |
| ATL 5G |  | sim | esim | Y |

SIM slots switching commands

- RouterOS v7

```ros
/interface/lte/settings/set sim-slot=down
```

- RouterOS v6 after 6.45.1

```ros
/system/routerboard/modem/set sim-slot=down
```

- RouterOS v6 pre 6.45.1:

```ros
/system/routerboard/sim/set sim-slot=down
```

For more reference please see the board block diagram,  Quick Guide, and User manual.

#### Usage Example

Follow this link - [Dual SIM Application](./dual-sim-application.md), to see examples of how to change the SIM slot based on the roaming status and in case the interface status is down, with the help of RouterOS scripts and scheduler.

### Tips and Tricks

This paragraph contains information for additional features and usage cases.

#### Find device location using Cell information

On devices using the R11e-LTE International version card (wAP LTE kit), some extra information is provided under info command.

```
   current-operator: 24701
                lac: 40
     current-cellid: 2514442
```

| Property | Description |
| :-- | :-- |
| **current-operator** (*integer*; Default: ) | Contains MCC and MNC. For example: current-operator: 24701 breaks to: MCC=247 MNC=01 |
| **lac** (*integer*; Default: ) | Location area code (LAC) |
| **current-cellid** (*integer*; Default: ) | Station identification number |

Values can be used to find location in databases: [Cell Mapper](http://www.cellmapper.net)

#### Using Cell lock

It is possible to lock R11e-LTE, R11e-LTE6 and R11e-4G modems and equipped devices to the exact LTE tower. The LTE info command provides currently used cellular tower information:

```
         phy-cellid: 384
             earfcn: 1300 (band 3, bandwidth 20Mhz)
```

| Property | Description |
| :-- | :-- |
| **phy-cellid** (*integer*; Default: ) | Physical Cell Identification (PCI) of currently used cell tower. |
| **earfcn** (*integer*; Default: ) | Absolute Radio Frequency Channel Number |

The exact tower location as well as available bands and other information can be acquired from the mobile carrier or by using online services:

[CellMapper](https://www.cellmapper.net/map)

By using those acquired variables it's possible to send the AT command to the modem for locking to the tower in the current format:

**for R11e-LTE and R11e-LTE6**

```
AT*Cell=<mode>,<NetworkMode>,<band>,<EARFCN>,<PCI>

where

<mode> :
0 – Cell/Frequency disabled
1 – Frequency lock enabled
2 – Cell lock enabled

<NetworkMode>
0 – GSM
1 – UMTS_TD
2 – UMTS_WB
3 – LTE

<band>
Not in use, leave this blank

<EARFCN>
earfcn from lte info

<PCI>
phy-cellid from lte info
```

To lock the modem at the previously used tower, at-chat can be used:

```ros
/interface/lte/at-chat lte1 input="AT*Cell=2,3,,1300,384"
```

For R11e-LTE all set locks are lost after reboot or modem reset. Cell data can also be gathered from "cell-monitor".

For R11e-LTE6 cell lock works only for the primary band. This can be useful if you have multiple channels on the same band and you want to lock it to a specific earfcn. Note that cell lock is not band-specific and for ca-band it can also use other frequency bands, unless you use band lock.

Use cell lock to set the primary band to the 1300 earfcn and use the second channel for the ca-band:

```ros
/interface/lte/at-chat lte1 input="AT*Cell=2,3,,1300,138"
```

Now it uses the earfcn: 1300 for the primary channel:

```
         primary-band: B3@20Mhz earfcn: 1300 phy-cellid: 138
              ca-band: B3@5Mhz earfcn: 1417 phy-cellid: 138
```

You can also set it the other way around:

```ros
/interface/lte/at-chat lte1 input="AT*Cell=2,3,,1417,138"
```

Now it uses the earfcn: 1417 for the primary channel:

```
         primary-band: B3@5Mhz earfcn: 1417 phy-cellid: 138
              ca-band: B3@20Mhz earfcn: 1300 phy-cellid: 138
```

For the R11e-LTE6 modem, cell lock information will not be lost after reboot or modem reset. To remove the cell lock, use the at-chat command:

```ros
/interface/lte/at-chat lte1 input="AT*Cell=0"
```

**for R11e-4G**

```
AT%CLCMD=<mode>,<mode2>,<EARFCN>,<PCI>,<PLMN>
AT%CLCMD=1,1,3250,244,\"24705\"

where

<mode> :
0 – Cell/Frequency disabled
1 – Cell lock enabled

<mode2> :
0 - Save lock for first scan
1 - Always use lock
(after each reset modem will clear out previous settings no matter what is used here)

<EARFCN>
earfcn from lte info

<PCI>
phy-cellid from lte info

<PLMN>
Mobile operator code
```

All PLMN codes available [here](https://en.wikipedia.org/wiki/Mobile_country_code). This variable can be also left blank

To lock the modem to the cell - the modem needs to be in a non-operating state, the easiest way for the **R11e-4G** modem is to add a CellLock line to the "modem-init" string:

```ros
/interface/lte/set lte1 modem-init="AT%CLCMD=1,1,3250,244,\"24705\""
```

Multiple cells can also be added by providing a list instead of one tower's information in the following format:

```
AT%CLCMD=<mode>,<mode2>,<EARFCN_1>,<PCI_1>,<PLMN_1>,<EARFCN_2>,<PCI_2>,<PLMN_2>
```

For example to lock to two different PCIs within the same band and operator:

```ros
/interface/lte/set lte1 modem-init="AT%CLCMD=1,1,6300,384,\"24701\",6300,385,\"24701\""
```

**for Chateau LTE12, Chateau LTE18, Chateau 5G, Chateau 5G R16, LHG LTE18, ATL LTE18, ATL 5G R16, Chateau 5G R17 ax**

```
AT+QNWLOCK="common/4g",<num of cells>,[[<freq>,<pci>],...]
AT+QNWLOCK=\"common/4g\",1,6300,384

where

<num of cells>
number of cells to cell lock

<freq>
earfcn from lte info

<pci>
phy-cellid from lte info

```

Single-cell lock example:

```ros
/interface/lte/at-chat lte1 input="AT+QNWLOCK=\"common/4g\",1,3050,448"
```

Query current configuration:

```ros
/interface/lte/at-chat lte1 input="AT+QNWLOCK=\"common/4g\""
```

Multiple cells can also be added to the cell lock. For example to lock to two different cells:

```ros
/interface/lte/at-chat lte1 input="AT+QNWLOCK=\"common/4g\",2,3050,448,1574,474"
```

To remove the cell lock, use this at-chat command:

```ros
/interface/lte/at-chat lte1 input="at+qnwlock=\"common/4g\",0"
```

:::warning

1. Cell lock information will not be saved after a reboot or modem reset. 2. AT+QNWLOCK command can lock the cell and frequency. Therefore, the module can be given priority to register to the locked cell, however, according to the 3gpp protocol, the module will be redirected or handed over to a cell with better signal instructions, even if it is not within the lock of the command. This phenomenon is normal.

:::

**For the 5G-capable devices, it is also possible to lock the 5G SA cell**

```
AT+QNWLOCK="common/5g",<pci>,<freq>,<scs>,<band>
AT+QNWLOCK=\"common/5g\",901,504990,30,41

where
<pci> String type. Cell physical ID. 0 indicates disabling locking module to the specified cell.
<freq> Integer type. Cell frequency (earfcn).
<scs> Integer type. NR sub carrier space. Unit: kHz. For FR1(Sub-6 GHz) FDD band, please set <scs> to 15; for FR1 TDD band, please set <scs> to 30. Otherwise, an error code may be returned.
15
30
<band> Integer type. NR5G frequency band.
```

Cell lock example to TDD n78 band with earfcn=628032 and phy-cellid=138:

```ros
/interface/lte/at-chat lte1 input="AT+QNWLOCK=\"common/5g\",138,628032,30,78"
```

Query the current configuration:

```ros
[admin@MikroTik] > /interface/lte/at-chat lte1 input="AT+QNWLOCK=\"common/5g\""
  output: +QNWLOCK: "common/5g",138,628032,30,78
          OK
```

To remove the cell lock use this at-chat command:

```ros
/interface/lte/at-chat lte1 input="AT+QNWLOCK=\"common/5g\",0"
```

:::warning

1. Cell lock information will not be saved after a reboot or modem reset.

2. The AT+QNWLOCK command can lock the cell and frequency. Therefore, the module can be given priority to register to the locked cell, however, according to the 3gpp protocol, the module will be redirected or handed over to a cell with better signal instructions, even if it is not within the lock of the command. This phenomenon is normal.

3. When locking a cell, please make sure that the module supports the frequency band corresponding to the locked cell, otherwise an error code will be returned.

4. AT+QNWLOCK="common/5g" does not support locking 5G cells of NSA. (You can still lock to the lte anchor cell using the AT+QNWLOCK="common/4g" command.)

5. This Write Command can only be executed when the module is in full functionality (lte interface is not disabled).

6. This command is not recommended for commercial use.

:::

**for FG621-EA**

```
AT+GTCELLLOCK=<mode>[,<rat>,<type>,<earfcn>[,<PCI>]]

where

< mode >: integer type; 0 Disable this function 1 Enable this function 2 Add new cell to be locked

<rat>: integer type; 0 LTE 1 WCDMA

<type>: integer type; 0 Lock PCI 1 Lock frequency

<earfcn>: integer type; the range is 0-65535.

<PCI>: integer type; If second parameter value is 0, the range is 0-503 for LTE If second parameter value is 1, the range is 0-512 for WCDMA
```

Example:

```ros
/interface/lte/at-chat lte1 input="AT+GTCELLLOCK=1,0,0,6175,176"
```

#### Cell Monitor

Cell monitor allows scanning available nearby mobile network cells:

```ros
[admin@MikroTik] > /interface/lte/cell-monitor lte1
PHY-CELLID BAND         PSC EARFCN                 RSRP          RSRQ          RSSI         SINR
        49 B20              6300                -110dBm       -19.5dB
       272 B20              6300                -116dBm       -19.5dB
       374 B20              6300                -108dBm         -16dB
       384 B1               150                 -105dBm       -13.5dB
       384 B3               1300                -106dBm         -12dB
       384 B7               2850                -107dBm       -11.5dB
       432 B7               2850                -119dBm       -19.5dB
```

Gathered data can be used for more precise location detection or for Cell lock.

:::warning
Not all modems support this feature
:::

### Troubleshooting

#### Enable LTE logging

```ros
[admin@MikroTik] > /system/logging/add topics=lte
```

#### Check for errors in log

```ros
[admin@MikroTik] > /log/print

11:08:59 lte,async lte1: sent AT+CPIN?
11:08:59 lte,async lte1: rcvd +CME ERROR: 10
```

search for the CME error description online,

In this case: CME error 10 - SIM not inserted

#### Locking band on Huawei and other modems

To lock the band for Huawei modems, the `/interface/lte/set lte1 band=""` option can't be used.

It is possible to use AT commands to lock to the desired band manually.

To check all supported bands run the at-chat command:

```ros
[admin@MikroTik] /interface/lte/at-chat lte1 input="AT^SYSCFGEX=\?"

output: ^SYSCFGEX: ("00","03","02","01","99"),((2000004e80380,"GSM850/GSM900/GSM1800/GSM1900/WCDMA BCI/WCDMA BCII/WCDMA BCV/WCDMA BCVIII"),
(3fffffff,"All Bands")),(0-2),(0-4),((800d7,"LTE BC1/LTE BC2/LTE
BC3/LTE BC5/LTE BC7/LTE BC8/LTE BC20"),(7fffffffffffffff,"All Bands"))
OK

```

Example to lock to LTE band 7:

```ros
[admin@MikroTik] /interface/lte/set lte1 modem-init="AT^SYSCFGEX=\"03\",3FFFFFFF,2,4,40,,"
```

Change the last part **40** to the desired band specified hexadecimal value where:

```
4 LTE BC3
40 LTE BC7
80000 LTE BC20
7FFFFFFFFFFFFFFF  All bands
etc
```

All band HEX values and AT commands can be found in [Huawei AT Command Interface Specification guide](https://download-c.huawei.com/download/downloadCenter?downloadId=29741&version=72288&siteCode=)

Check if the band is locked:

```ros
[admin@MikroTik] /interface/lte/at-chat lte1 input="AT^SYSCFGEX\?"

output: ^SYSCFGEX: "03",3FFFFFFF,0,2,40
OK
```

For more information check modem manufacturers' AT command reference manuals.

#### mPCIe modems with RB9xx series devices

In case your modem is not being recognized after a soft reboot, then you might need to add a delay before the USB port is initialized. This can be done using the following command:

```ros
/system/routerboard/settings/set init-delay=5s
```

#### Boards with USB-A port and mPCIe

Some devices such as specific RB9xx and the RBLtAP-2HnD share the same USB lines between a single mPCIe slot and a USB-A port. If auto switch is not taking place and a modem is not getting detected, you might need to switch manually to either use the USB-A or the mini-PCIe:

```ros
/system/routerboard/usb/set type=mini-PCIe
```

#### Avoiding tethering speed throttling

Some operators allow unlimited data only for the device the SIM card is used on, all other data coming from mobile hotspots or tethering is highly limited by volume or by throughput speed. Some sources have found out that this limitation is done by monitoring TTL (Time To Live) values from packets to determine if limitations need to be applied (TTL is decreased by 1 for each "hop" made). RouterOS allows changing the TTL parameter for packets going from the router to allow hiding subnetworks. Keep in mind that this may conflict with the fair use policy.

```ros
IPv4 mangle rule:
/ip/firewall/mangle
add action=change-ttl chain=postrouting new-ttl=set:65 out-interface=lte1 passthrough=yes
IPv6 mangle rule:
/ipv6/firewall/mangle
add action=change-hop-limit chain=postrouting new-hop-limit=set:65 passthrough=yes
```

#### Unlocking SIM card after multiple wrong PIN code attempts

After locking the SIM card, unlocking can be done through "at-chat"

Check current PIN code status:

```ros
/interface/lte/at-chat lte1 input="at+cpin\?"
```

If the card is locked - unlock it by providing:

```ros
/interface/lte/at-chat lte1 input="AT+CPIN=\"PUK_code\",\"NEW_PIN\""
```

Replace PUK\_code and NEW\_PIN with matching values.

:::warning
The command for sim slot selection changes in v6.45.1 and again in v7. Some device models like SXT have SIM slots named "a" and "b" instead of "up" and "down"
:::
