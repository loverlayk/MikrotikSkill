# Packages

> RouterOS features come in packages (.npk files): the routeros package and optional extra packages such as container, wifi-qcom or user-manager. Install, disable, uninstall and downgrade packages from the router or...

# Packages

RouterOS features come in packages, files with the `.npk` extension. Most features are in the
`routeros` package. Some features come as extra packages, for example Containers, The Dude or the
drivers for Wi-Fi hardware. Packages are made only by MikroTik. Download them from the
[MikroTik download page](https://mikrotik.com/download) or install them directly from the router.

## Which packages a router needs

A router needs the `routeros` package and the driver packages for its hardware, for example
`switch-marvell` on CRS8xx switches or `extra-nic` on arm64 boards that are not made by MikroTik.
On devices with Wi-Fi, the Wi-Fi drivers are in a separate package:

- 802.11ax and 802.11be (Wi-Fi 6 and 7) devices need a driver package such as `wifi-qcom`,
  `wifi-qcom-be` or `wifi-mediatek` (the package `wifi-qcom` was earlier called `wifiwave2`).
- Earlier Wi-Fi devices (up to 802.11ac) and 60 GHz devices use the `wireless` package or, on some
  802.11ac devices, `wifi-qcom-ac`.

See the [Wireless manual](../../wireless/) for which package your device uses. Other packages are
optional: install them only for the feature they add.

## Install a package from the router

The router can download and install extra packages from the MikroTik download server. The router
itself needs access to the server (HTTPS by default, see the `mode` setting in [Upgrade](./upgrade)).

1. Check for updates. The packages that exist for the router's architecture and version appear in
   the list with the `X` (disabled) and `A` (available) flags.
2. Enable the package.
3. Apply the changes. The router downloads the package and reboots to install it.

Packages are made for an architecture. `/system/resource/print` shows the router's
`architecture-name`, for example `arm64` on a hAP ax²; the router lists only packages for its own
architecture.

```routeros
/system/package/update/check-for-updates
/system/package/print
```

```text
Flags: X - DISABLED; A - AVAILABLE
Columns: NAME, VERSION, BUILD-TIME, SIZE
 #    NAME          VERSION  BUILD-TIME           SIZE
 0    routeros      7.25.2   2026-11-20 11:11:10  20.0MiB
 1 XA calea                                       24.1KiB
 2 XA container                                   1116.1KiB
 3 XA dude                                        1388.1KiB
 4 XA gps                                         24.1KiB
 5 XA iot                                         576.1KiB
 6 XA netinstall                                  76.1KiB
 7 XA openflow                                    80.1KiB
 8 XA rose-storage                                5.2MiB
 9 XA tr069-client                                156.1KiB
10 XA ups                                         36.1KiB
11 XA user-manager                                408.1KiB
12 XA wireless                                    1112.1KiB
```

Enable the `iot` package (`enable` also takes several names, for example `enable iot,gps`):

```routeros
/system/package/enable iot
/system/package/print where name=iot or name=routeros
```

```text
Flags: X - DISABLED; A - AVAILABLE
Columns: NAME, VERSION, SCHEDULED
#    NAME      VERSION  SCHEDULED
0    routeros  7.25.2
5 XA iot                Use "apply-changes" to proceed with install
```

```routeros
/system/package/apply-changes
```

In an interactive session, the router asks `Apply scheduled changes and reboot device? [y/N]:`.
After the reboot, the package is in the list and the log shows the installation:

```routeros
/system/package/print
/log/print where message~"install"
```

```text
Columns: NAME, VERSION, BUILD-TIME, SIZE
# NAME      VERSION  BUILD-TIME           SIZE
0 iot       7.25.2   2026-11-20 11:11:10  576.1KiB
1 routeros  7.25.2   2026-11-20 11:11:10  20.0MiB

 2026-11-23 10:29:53 system,info installed iot-7.25.2
```

In WinBox, the same steps are in **System → Packages**: **Check for Updates**, select the
package, **Enable**, **Apply Changes**.

| Package list | After loading the list with "Check for updates" | Enabling a package | Selecting "Apply Changes" |
| :--- | :--- | :--- | :--- |
| [![WinBox Packages window with only the routeros package installed](img/packages1.webp)](img/packages1.webp) | [![WinBox Packages window listing the available packages with the X and A flags](img/packages2.webp)](img/packages2.webp) | [![WinBox Packages window with the iot package scheduled for install](img/packages3.webp)](img/packages3.webp) | [![WinBox asking Apply scheduled changes and reboot device?](img/packages4.webp)](img/packages4.webp) |

## Install a package from a file

1. Download the package for your router's architecture (`/system/resource/print` shows
   `architecture-name`) and RouterOS version from the
   [MikroTik download page](https://mikrotik.com/download). The extra packages are in the
   "Extra packages" archive: extract the archive and upload only the `.npk` files you need.
2. Upload the `.npk` file to the router, for example with WinBox (drag it to **Files**), SFTP or
   FTP.
3. Reboot the router. It installs the package during the boot.

Use extra packages of the same version as the installed RouterOS. Upload the file to the root of
the file system, not into a folder.

A package file whose name ends in `.auto.npk` is installed as soon as it is uploaded over FTP or
SFTP: the router reboots by itself and installs it. Rename the file before the upload, for
example to `iot-7.25.1.auto.npk`.

## Check the installation

After the reboot, the log shows what was installed, and why a package was not. The `routeros`
package appears as `system`:

```text
 2026-11-23 09:56:17 system,info installed system-7.25.1
 2026-11-23 09:56:17 system,info installed iot-7.25.1
```

```text
 2026-11-23 09:57:41 system,warning omitting package system-7.24.7: newer package system-7.25.1 is already installed
```

Uploaded package files are removed after the reboot.

## Disable, uninstall and downgrade

A disabled package stays on the router but does not run; `enable` turns it on again. An
uninstalled package is removed. The changes take effect after `apply-changes`; a scheduled disable
also takes effect at the next reboot:

```routeros
/system/package/disable iot
/system/package/print
```

```text
Flags: X - DISABLED; A - AVAILABLE
Columns: NAME, VERSION, SCHEDULED, BUILD-TIME
 #    NAME          VERSION  SCHEDULED              BUILD-TIME
 0    iot           7.25.2   scheduled for disable  2026-11-20 11:11:10
 1    routeros      7.25.2                          2026-11-20 11:11:10
 2 XA calea
 3 XA container
 4 XA dude
 5 XA gps
 6 XA netinstall
 7 XA openflow
 8 XA rose-storage
 9 XA tr069-client
10 XA ups
11 XA user-manager
12 XA wireless
```

`/system/package/unschedule iot` cancels the scheduled change.

```routeros
/system/package/uninstall iot
/system/package/apply-changes
```

To install an older RouterOS version, upload the older `routeros` package and the matching versions
of all installed extra packages (for example `wifi-qcom`), then run `/system/package/downgrade`.
If an installed extra package is missing, the router reboots, logs `missing package`, and keeps the
installed version. On a router whose device-mode limits the installable versions, a version outside
the allowed list cannot be installed, see
[Device-mode](../../system-information-and-utilities/device-mode). The router asks
`Router will be rebooted. Continue? [y/N]:` and installs the older packages during the reboot. A
plain reboot does not install older packages: the log shows `omitting package ... newer package
... is already installed`. To downgrade from the router without files, see
[Upgrade](./upgrade).

## System packages

The `routeros` package exists for every architecture. Inside RouterOS it is called `routeros`; the
file name says the architecture:

| Architecture | File name |
| :--- | :--- |
| x86, CHR | `routeros-<version>.npk` |
| arm | `routeros-<version>-arm.npk` |
| arm64 | `routeros-<version>-arm64.npk` |
| mipsbe | `routeros-<version>-mipsbe.npk` |
| mmips | `routeros-<version>-mmips.npk` |
| smips | `routeros-<version>-smips.npk` |
| tile | `routeros-<version>-tile.npk` |
| ppc | `routeros-<version>-ppc.npk` |

## Extra packages

The x86 packages are also used on CHR.

| Package (architectures) | Description |
| :--- | :--- |
| **calea** (*arm, arm64, mipsbe, mmips, tile, ppc, x86*) | Data gathering tool for specific use due to "Communications Assistance for Law Enforcement Act" in the USA. |
| **cmr** (*arm, arm64, x86*) | [CMR](../../management-tools/cmr) is a centralized monitoring platform for fleets of RouterOS devices. |
| **container** (*arm, arm64, x86*) | [Container](../../containers/) implementation of Linux containers, allowing users to run containerized environments in RouterOS. Containers also need to be enabled in device-mode. |
| **dude** (*arm, arm64, mmips, tile, x86*) | [Dude](../../management-tools/dude) tool that allows monitoring of the network environment. |
| **extra-nic** (*arm64*) | ARM64 CPU architecture Network Interface Card (NIC) support, recommended for UEFI installation on non-MikroTik boards. |
| **gps** (*arm, arm64, mipsbe, mmips, tile, ppc, x86*) | [Global Positioning System](../../mobile-networking/gps/) device support. |
| **hotspot** (*smips*) | [HotSpot](../../authentication-authorization-accounting/hotspot-captive-portal/) for smips devices. |
| **iot** (*arm, arm64, mipsbe, mmips, tile, ppc, x86*) | Enables [MQTT](../../internet-of-things/mqtt/), [LoRa](../../internet-of-things/lora/general-properties) (for devices with LR8/9/2 miniPCIe cards), [Bluetooth](../../internet-of-things/bluetooth/) (for devices with a Bluetooth chip), [GPIO](../../internet-of-things/gpio) (for devices with GPIO pins) and [Modbus](../../internet-of-things/modbus) (for devices with an RS485 port). |
| **iot-bt-extra** (*arm, arm64*) | USB Bluetooth adapter support (LE 4.0 or newer). Not every adapter is tested. |
| **netinstall** (*arm, arm64, mipsbe, mmips, tile, ppc, x86*) | [Netinstall package](./netinstall/netinstall-package): reinstalls RouterOS on other MikroTik devices from this router. |
| **openflow** (*arm, arm64, mipsbe, mmips, tile, ppc, x86*) | [OpenFlow](../../network-management/openflow) support. |
| **rose-storage** (*arm, arm64, tile, x86*) | Additional [enterprise data center functionality](../../storage/) in RouterOS, supporting disk monitoring, improved formatting, RAIDs, rsync, iSCSI, NVMe over TCP, NFS, and improved SMB. |
| **switch-marvell** (*arm64*) | Required driver package for CRS8xx series switches. |
| **tr069-client** (*arm, arm64, mipsbe, mmips, smips, tile, ppc, x86*) | [TR-069](../../management-tools/tr-069) client. |
| **ups** (*arm, arm64, mipsbe, mmips, tile, ppc, x86*) | [APC UPS management](../../system-information-and-utilities/ups) interface. |
| **user-manager** (*arm, arm64, mipsbe, mmips, tile, ppc, x86*) | [MikroTik User Manager](../../authentication-authorization-accounting/user-manager) server for controlling HotSpot and other service users. |
| **wifi-halow-mm** (*arm*) | Wi-Fi HaLow (802.11ah) driver for supported hardware. |
| **wifi-mediatek** (*arm*) | Required MediaTek Wi-Fi driver for supported MediaTek wireless hardware. |
| **wifi-qcom** (*arm, arm64*) | Required driver package for 802.11ax interfaces. [WiFi CAPsMAN](../../wireless/wifi/#wifi-capsman) support comes with the system package. |
| **wifi-qcom-ac** (*arm*) | Optional [WiFi](../../wireless/wifi/) driver package for compatible 802.11ac interfaces. |
| **wifi-qcom-be** (*arm64*) | Required driver package for Wi-Fi 7 802.11be hardware. |
| **wireless** (*arm, arm64, mipsbe, mmips, smips, tile, ppc, x86*) | Utilities and drivers for managing Wi-Fi (up to 802.11ac) and 60 GHz wireless interfaces. The **wireless** package conflicts with the **wifi-qcom** and **wifi-qcom-ac** packages: they cannot be active at the same time. |
| **zerotier** (*arm, arm64*) | Enables [ZeroTier](../../virtual-private-networks/zerotier) functionality. |

For all `/system/package` commands, see the [CLI reference](../../cli-reference/system/package/).
