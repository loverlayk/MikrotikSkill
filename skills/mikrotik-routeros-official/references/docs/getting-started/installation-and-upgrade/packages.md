# Packages

> RouterOS organizes features into packages with .npk extensions, including the core routeros bundle and optional extras like Containers or The Dude. Wireless devices require specific packages depending on hardware,...

# Packages

## Summary

RouterOS features are organized into packages, which are files with a `.npk` extension. Most features are bundled in the ***routeros*** package, while some features are provided as separate packages. Installing an additional `.npk` package enables specific features such as Containers or The Dude. Package files are provided exclusively by MikroTik and cannot be created by third parties. You can download extra packages from our download page, or add them directly from your router.

## Minimum requirements

RouterOS requires only the system package to operate at a bare minimum, but for most devices standard operation and features are available when you install the "routeros" bundle package.

For wireless devices, several wireless packages are available, depending on the hardware you are using:

- Starting with RouterOS 7.13, the ***routeros*** (system) package and one of the following wireless packages are needed for the basic operation of a simple home router:
  1. 802.11ax WiFi APs require radio drivers, which are provided by the ***wifi-qcom*** package (for RouterOS versions earlier than 7.13 it was called the *wifiwave2* package).
  2. Previous generation WiFi APs require a ***wireless*** package.

More information about which wireless package to use is available in the [Wireless manual](../../wireless/index.md).

Other packages are optional and not required for a home router. Install them only if you are sure of their purpose.

## Installing packages

### Manual download

To manually download and install extra packages, download the necessary package from the [MikroTik download](https://mikrotik.com/download) page, selecting the RouterOS section based on your device's architecture found in the System/Resources menu. Extract the archive and upload the required package to your router by using any convenient method, and proceed to reboot the router.

### Download directly from the router

You can download and install extra packages directly from the router by using the *System Packages* section.

1. After executing the ***Check For Updates*** command, available packages will be listed in the *Packages* list, but they will show up as disabled. The available package list comes from the MikroTik download server. Those packages are available, but not yet on your router (as indicated by the flags X (Disabled) and A (Available)).
2. To download an extra package, first select the package and select ***Enable***.
3. To make the router download the package, select ***Apply Changes*** and the device will ask for a reboot.

| Package list | After loading the list with "Check for updates" | Enabling a package | Selecting "Apply Changes" |
| :--- | :--- | :--- | :--- |
| [![](img/packages1.png)](img/packages1.png) | [![](img/packages2.png)](img/packages2.png) | [![](img/packages3.png)](img/packages3.png) | [![](img/packages4.png)](img/packages4.png) |

### Verification of install

To make sure the package is installed successfully, check the "Log" section after the device is rebooted. If the package is installed successfully, you will see a message about it. If there have been conflicts or some requirement is not met, this will be explained, so you can take further steps to rectify that.

![](./img/packages-01.webp)Success in the log entries![](./img/packages-02.webp)Failure in the log entries

### System packages

| **Package** | Description |
| :--- | :--- |
| **routeros-arm** (*arm*) | System package for arm devices. |
| **routeros-arm64** (*arm64*) | System package for arm64 devices. |
| **routeros-mipsbe** (*mipsbe*) | System package for mipsbe devices. |
| **routeros-mmips** (*mmips*) | System package for mmips devices. |
| **routeros-smips** (*smips*) | System package for smips devices. |
| **routeros-tile** (*tile*) | System package for tile devices. |
| **routeros-ppc** (*ppc*) | System package for ppc devices. |
| **routeros** (*x86, CHR*) | System package for x86 installations and CHR environment. |

### Extra packages

| Package (supported architecture) | Description |
| :--- | :--- |
| **calea** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | Data gathering tool for specific use due to "Communications Assistance for Law Enforcement Act" in the USA. |
| **cmr** (*arm, arm64, x86*) | [CMR](../../management-tools/cmr) is a centralized monitoring platform for fleets of RouterOS devices. |
| **container** (*arm, arm64, x86, CHR*) | [Container](../../containers/index.md) implementation of Linux containers, allowing users to run containerized environments in RouterOS. |
| **dude** (*arm, arm64, mmips, tile, x86, CHR*) | [Dude](../../management-tools/dude.md) tool that allows monitoring of the network environment. |
| **extra-nic** (*arm64*) | ARM64 CPU architecture Network Interface Card (NIC) support, recommended for UEFI installation on non-MikroTik boards. |
| **gps** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | [Global Positioning System](../../mobile-networking/gps/index.md) device support. |
| **iot** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | Enables: MQTTLoRa (for devices with LR8/9/2 miniPCIe cards)Bluetooth (for devices with Bluetooth chip)GPIO (for devices with GPIO pins)Modbus (for devices with RS485 port) |
| **iot-bt-extra** (*arm, arm64*) | A package for ARM and ARM64 devices which enables the use of USB Bluetooth adapters (must support LE 4.0+).  ***note:** Not all adapters were tested. We cannot guarantee beforehand that a specific adapter will work. |
| **lora** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | Dummy package for [LoRa](../../internet-of-things/lora/general-properties.md) support. LoRa package is not obligatory anymore and is left only for compatibility reasons. LoRa functionality is moved into the iot package. |
| **lte** (*mipsbe*) | Required package only for SXT LTE (RBSXTLTE3-7), which contains drivers for the built-in LTE interface. |
| **rose-storage** (*arm, arm64, tile, x86, CHR*) | Additional [enterprise data center functionality](../../storage/index.md) in RouterOS, supporting disk monitoring, improved formatting, RAIDs, rsync, iSCSI, NVMe over TCP, NFS, and improved SMB. |
| **switch-marvell** (*arm64*) | Required driver package for CRS8xx series switches. |
| **tr069-client** (*arm, arm64, mipsbe, mmips, smips, tile, ppc, x86, CHR*) | [TR069 Client](../../management-tools/tr-069.md) package. |
| **ups** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | [APC UPS management](../../system-information-and-utilities/ups.md) interface. |
| **user-manager** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | [MikroTik User Manager](../../authentication-authorization-accounting/user-manager.md) server for controlling Hotspot and other service users. |
| **wifi-mediatek** (*arm*) | Required MediaTek WiFi driver for supported MediaTek wireless hardware. |
| **wifi-qcom** (*arm, arm64*) | Required driver package for 802.11ax interfaces. Introduced in 7.13. [WiFi CAPsMAN](../../wireless/wifi/index.md#wifi-capsman) support comes with the system package. |
| **wifi-qcom-ac** (*arm*) | Optional [WiFi](../../wireless/wifi/index.md) driver package for compatible 802.11ac interfaces. Introduced in 7.13. |
| **wifi-qcom-be** (*arm64*) | Required driver package for WiFi-7 802.11be hardware. |
| **wireless** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | Utilities and drivers for managing WiFi (up to 802.11ac) and 60GHz wireless interfaces. This package is bundled into RouterOS for versions up to 7.12. Starting with 7.13, it is a separate package.  The **wireless** package conflicts with **wifi-qcom** and **wifi-qcom-ac** packages — they cannot be active at the same time. |
| **zerotier** (*arm, arm64*) | Enables [ZeroTier](../../virtual-private-networks/zerotier.md) functionality. |

## Auto install

You can also automatically install packages after uploading them to the router with FTP or SFTP. The package file must be named with the extension `*.auto.npk`. Once the file is uploaded, the router will automatically go into reboot to install the package. This can be useful for scripting and automation.

The `.auto.npk` extension in the filename is mandatory for a package to be automatically installed.

## Working with packages

___

### List packages

The *zerotier* package is disabled, but installed; the *iot* package is available on the server, but has not been downloaded to the router and enabled; the *dude* package is scheduled for uninstall.

```ros
/system/package/print 
Flags: X - DISABLED; A - AVAILABLE
Columns: NAME, VERSION, SCHEDULED, BUILD-TIME, SIZE
#    NAME            VERSION     SCHEDULED                      BUILD-TIME           SIZE  
0    wireless        7.24beta1                                  2026-05-26 10:47:52  1388.1KiB
1 X  container       7.24beta1                                  2026-05-26 10:47:52  1156.1KiB
2    routeros        7.24beta1                                  2026-05-26 10:47:52  11.0MiB  
3    zerotier        7.24beta1                                  2026-05-26 10:47:52  372.1KiB 
4 XA calea                                                                           20.1KiB  
5 XA gps                                                                             24.1KiB  
6 XA iot                                                                             788.1KiB 
7 XA openflow                                                                        76.1KiB  
8 XA tr069-client                                                                    120.1KiB 
9 XA ups                                                                             44.1KiB  
```

### Install package

```ros
/system/package/enable gps,zerotier,container
/system/package/apply-changes
Apply scheduled changes and reboot device? [y/N]: 

```

### Uninstall package

```ros
/system/package/uninstall gps,container;
/system/package/apply-changes
Apply scheduled changes and reboot device? [y/N]: 
```

### Disable package

```ros
/system/package/disable container; 
/system/package/apply-changes
Apply scheduled changes and reboot device? [y/N]:
```

### Cancel the uninstall or disable action

```ros
/system/package/unschedule container;
```

### Downgrade

```ros
/system/package/downgrade; /system/reboot;
Router will be rebooted. Continue? [y/N]: 
```
