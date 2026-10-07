# Netinstall package

> This page documents the RouterOS Netinstall package, which allows reinstalling RouterOS on MikroTik devices remotely from another router running RouterOS 7.24beta1 or newer, covering prerequisites, the...

# Netinstall package

The **Netinstall package** is an extra package, available for all devices running RouterOS starting from version 7.24beta1 and is available for all of the architectures excluding SMIPS.

This package allows RouterOS to be reinstalled remotely from another MikroTik device running RouterOS.

## Prerequisites

- RouterOS version 7.24beta1 and later.
- Netinstall package enabled.
- Target MikroTik hardware router connected to the same L2 network segment as the device being reinstalled.

:::warning
By default, the **Netinstall package** creates a `NetinstallCache` directory in the root directory. On devices with a `flash` directory, Netinstall-related files are stored in RAM. On devices without a `flash` directory, these files are stored on the device's persistent storage.

Ensure that the **Netinstall** server device has sufficient free storage space or RAM available.

You can also configure an external storage device to be used as the `NetinstallCache/` directory in **Netinstall → Settings**.
:::

> Physically removed files from the `Files` menu will be automatically redownloaded if they are currently cached. In order to delete cached files, remove them from a `Netinstall Cache` menu.
> In case files were previously downloaded before the device was rebooted, they will be deleted.

## Installation Workflow

1. Install and enable the Netinstall package. The **Netinstall package** is available for WinBox, WebFig GUI and CLI and is located under the **Tools** menu or `/tools/netinstall` in the CLI.

2. Configure a Netinstall interface. Add a new **Netinstall** interface, set the required parameters and run the device connected to that interface in BOOTP mode.

3. Download or select the required RouterOS packages. The **Netinstall package** automatically installs the appropriate **System** package for the target device architecture.

4. Boot the target device into Etherboot mode.

5. Install RouterOS.

:::tip
If the **Version** parameter is not set, **Netinstall package** installs the latest RouterOS version available in the `Check for Updates` channel currently selected on the **Netinstall server**.
:::

Additional packages must be selected explicitly.

## General Configuration Options

| Parameter | Description |
| :-- | :-- |
| **Settings** | Allows to set the `NetinstallCache/` path directory. See the [Prerequisites warning information](#prerequisites). Example: `/tool/netinstall/settings/set cache-directory=...` |

## Netinstall Parameters

| Parameter | Description |
| :-- | :-- |
| **allow-etherboot** (yes / no ; Default: **yes**) |  Allows the BOOTP requests on the selected interface. Will ignore the device if set to no.  |
| **allow-flashfig** (yes / no ; Default: **yes**) |  Enables the [FlashFig](../../../management-tools/flashfig.md) functionality |
| **apply-default-configuration** (yes / no ; Default: **no**) | If enabled, the device will apply the default configuration script after installation and reboot. See `/system/default-configuration/script/print`. |
| **auto-reboot** (none / reboot / shutdown ; Default: **reboot**) | Defines the action performed after device installation completes successfully. |
| **etherboot-image** | Allows to select the previously cached package to be installed. |
| **etherboot-image-arch** |  Specifies the CPU architecture required for the etherboot image. All other architecture requests will be ignored. If not specified, the detected architecture will be used. |
| **extra-packages** | Allows to add the extra packages to be installed alongside the `system` package. The `routeros` package will be installed by default. |
| **install-once** (yes / no ; Default: **yes**) | Restrict installation to once per Netinstall run. The tool tracks **MAC addresses** of successfully installed devices and ignores subsequent **BOOTP** requests from the same **MAC address** during the current session. |
| **interface** | Specifies the **Netinstall server** network interface. |
| **ip-range** | Customizes the **BOOTP** ip-range to be used for netinstall process. |
| **keep-old-configuration** (yes / no ; Default: **yes**) | Instructs Netinstall to read and restore the device core configuration (/export; /users) after installation. This option does not retain user files, containers, or similar data. |
| **mac-address** | Specify a MAC address to allow for installation. When provided, all other BOOTP requests are ignored. |
| **mode-file** | Similar to `Mode script`. Specifies a one-time custom script that runs on the device's first boot after installation. Use this script to configure **device‑mode**, **protected‑routerboot**, and other settings during device deployment. The mode script executes before any custom or default configuration scripts. Upon completion, the script is automatically removed from the device. If the script modifies the device-mode, the device reboots immediately after execution. **This feature requires RouterOS and Netinstall version 7.22 or newer.** |
| **place-before** | Insert rule before existing rules |
| **remove-branding** (yes / no ; Default: **no**) | Discard the currently installed branding package from the device. If not specified, the branding package is preserved. Factory-installed branding packages cannot be discarded and are always preserved. |
| **script-file** | Allows installation of a custom default configuration script on the device during installation. This replaces the RouterOS-supplied default configuration script. See `/system/default-configuration/custom-script/print`. The script is retained during RouterOS updates and used after subsequent configuration resets until the device is reinstalled with a new script or the script is removed. |
| **version** | Specifies the RouterOS version to be installed. If the **Version** parameter is not set, **Netinstall** installs the latest RouterOS version available in the `Check for Updates` channel currently selected on the **Netinstall server**. |
| **wait** (yes / no ; Default: **no**) | Keeps the device in the etherboot state and wait for user command to start installing. |

## Cache

Available action - `Add` for both GUI and CLI.

| Parameter | Description |
| :-- | :-- |
| **arch** |  Mandatory parameter. Specifies the CPU architecture of the necessary files to be downloaded. |
| **packages** | Allows to add the extra packages list to be downloaded to the `NetinstallCache/` directory. |
| **version** | Specifies the RouterOS version packages to download. If the **Version** parameter is not set, **Netinstall** downloads the latest RouterOS version available in the `Check for Updates` channel currently selected on the **Netinstall server**. |

## Devices

The **Netinstall Devices** menu displays the list of the netinstalled devices and its states.

Available actions:

- `Clear` the list.
- `Install` menu. If additional parameters are chosen with an `Install` menu, all the previously set settings are overridden.

Available `install` parameters: `auto-reboot`, `extra-packages`, `numbers`, `version`.

```bash
/tool/netinstall/devices> install auto-reboot=reboot extra-packages=user-manager version=7.24beta1
```

| Parameter | Description |
| :-- | :-- |
| **auto-reboot** (none / reboot / shutdown ; Default: **reboot**) | Defines the action performed after device installation completes successfully. |
| **extra-packages** | Allows to add the extra packages to be installed alongside the `system` package. The `routeros` package will be installed by default. |
| **numbers** | Allows to Select for which devices from the list the RouterOS to be reinstalled. |
| **version** | Specifies the RouterOS version packages to download. If the **Version** parameter is not set, **Netinstall** installs the **version** selected for the interface main settings or if not specified, downloads the latest RouterOS version available in the `Check for Updates` channel currently selected on the **Netinstall server**. |

## Use cases

The **Netinstall package** can be used within the [Preboot Etherboot](../../../hardware/routerboard.md#preboot-etherboot) for the scenario when one of the MikroTik routers with a Netinstall package installed is dedicated for remote recovery purposes.
Set the `preboot-etherboot-server=ip_address` of the Netinstall server and reinstall the RouterOS remotely in case of any issues with a target device.
When using `preboot-etherboot-server`, configure an appropriate **IP range** on the Netinstall server to handle the Etherboot requests.

:::danger
Remember to disable or strictly filter the rules created not to unintentionally reinstall the system on each reboot.
:::

### Netinstall package Example

```bash
[admin@MikroTik] /tool/netinstall/add interface=bridge1 keep-old-configuration=no apply-default-configuration=yes auto-reboot=reboot mac-address=01:23:45:67:89:BB extra-packages=wifi-qcom,container version=7.23.1 ip-range=192.168.88.10-192.168.88.20
```

Verify the cached packages:

```bash
[admin@MikroTik] /tool/netinstall/cache/print 
Columns: PATH, URL, STATUS
#  PATH                                               URL                                                                                STATUS    
0  NetinstallCache/container-7.23.1-arm64.npk  https://upgrade.mikrotik.com/routeros/7.23.1/container-7.23.1-arm64.npk  downloaded
1  NetinstallCache/linux.arm64                 https://upgrade.mikrotik.com/routeros/7.23.1/netinstk/linux.arm64        downloaded
2  NetinstallCache/linux.arm64-uefi            https://upgrade.mikrotik.com/routeros/7.23.1/netinstk/linux.arm64-uefi   downloaded
3  NetinstallCache/wifi-qcom-7.23.1-arm64.npk  https://upgrade.mikrotik.com/routeros/7.23.1/wifi-qcom-7.23.1-arm64.npk  downloaded
```

Check the device state after installation:

```bash
[admin@MikroTik] /tool/netinstall/devices/print 
Flags: N - NETINSTALL
Columns: MAC-ADDRESS, INTERFACE, STATE, LAST-STATE-UPDATE, EXTRA-PACKAGES, VERSION, ARCH, MODEL, LAST-STATE, AUTO-REBOOT
#   MAC-ADDRESS        INTERFACE  STATE    LAST-STATE-UPDATE  EXTRA-PACKAGES  VERSION    ARCH   MODEL       LAST-STATE        AUTO-REBOOT
0 N 01:23:45:67:89:BB  bridge1    done     58s                container       7.23.1     arm64   L009UiGS   bootp reply sent  reboot     
                                                              wifi-qcom 
```

### Netinstall package FlashFig Example

The Netinstall package includes FlashFig functionality, making the batch configuration process much simpler.
A common setup uses a PoE switch with bridged ports.

:::warning
Set the bridge `protocol-mode=none` or `/interface/bridge/port set 0,1... edge=yes`.
:::

The physical setup:

- Connect the **Netinstall server** (Router1, ether2) to a port on the PoE switch.
- Connect the **target device** to another port on the same PoE switch.

```bash
[admin@MikroTik] /tool/netinstall/devices/print 
Flags: F - FLASHFIG
Columns: MAC-ADDRESS, INTERFACE, STATE, LAST-STATE-UPDATE, MODEL, AUTO-REBOOT
#   MAC-ADDRESS        INTERFACE  STATE                  LAST-STATE-UPDATE  MODEL   AUTO-REBOOT
0 F 01:23:45:67:89:BB  ether2     done, won't reinstall  21s                952-hb  reboot 
```

:::tip
Looking for a different installation method? See the [**Windows**](./netinstall-windows.md) or [**Linux**](./netinstall-linux.md) instructions.
:::
