# Netinstall for Linux

> This page documents netinstall-cli, the Linux command-line version of the MikroTik Netinstall utility, covering all command-line options for single and multiple device reinstallation, scripting and configuration...

# Netinstall for Linux

The Linux version of Netinstall, `netinstall-cli`, is a command-line tool that provides nearly the same functionality as the Windows version.

:::tip
Make sure you have set a static IP address on your computer's interface before running the netinstall tool.

```bash
sudo ip addr add 192.168.88.2/24 dev <interface>
sudo ip link set <interface> up
```

:::

:::info
This tool requires root privileges. You must run it as root or use `sudo` to execute it.
:::

## netinstall-cli Command Line Options

The `netinstall-cli` command syntax is:

```
netinstall-cli [-r] [-e] [-b] [-m [-o]] [-f] [-c] [-v] [--reboot] [--shutdown] [-k <keyfile>] [-s <userscript>] [-sm <modescript>] [--mac <mac address>] {-i <interface> | -a <client-ip>} [PACKAGE]+ 
```

## General Options

| Parameter | Description |
| :-- | :-- |
| **-r** | Reinstall the device and apply the default configuration script. |
| **-e** | Reinstall the device without applying the default configuration script, leaving the device with an empty configuration. |
| **-b** | Discard the currently installed branding package from the device. If not specified, the branding package is preserved. Factory-installed branding packages cannot be discarded and are always preserved. |
| **-f** | Ignore storage size constraints. By default, netinstall-cli checks the router's storage capacity. If the total size of selected packages exceeds available storage, an error is displayed: **"Ignoring XX:XX:XX:XX:XX:XX, not enough space (override with -f)"** |
| **-c** | Allow multiple Netinstall instances to run simultaneously on the same computer. |
| **-v** | Enable verbose mode for detailed output. |

### Multiple Device Reinstallation Options

| Parameter | Description |
| :-- | :-- |
| **-m** | Enable multiple device reinstallation. The same device will be reinstalled as many times as BOOTP requests are received. |
| **-o** | Restrict installation to once per Netinstall run. The tool tracks MAC addresses of successfully installed devices and ignores subsequent BOOTP requests from the same MAC address during the current session. |

**Combination behavior:**

- No `-m` and no `-o`: Only one successful installation proceeds, then Netinstall closes.
- `-m` only: Enables multiple reinstallation; the same device reinstalls repeatedly.
- `-o` only: Same as no flags; one installation per run, then close.
- Both `-m` and `-o`: Enables multiple reinstallation, but each device installs only once per session.

### Script and Configuration Options

| Parameter | Description |
| :-- | :-- |
| **--reboot** | Reboots the selected MikroTik device that is booted in Netinstall mode. |
| **--shutdown** | Shuts down the selected MikroTik device that is booted in Netinstall mode. |
| **-k \<keyfile>** | Provide a license key file in .KEY format to the device (optional). |
| **-s \<userscript>** | Allows installation of a custom default configuration script on the device during installation. This replaces the RouterOS-supplied default configuration script. See `/system/default-configuration/custom-script/print`. The script is retained during RouterOS updates and used after subsequent configuration resets until the device is reinstalled with a new script or the script is removed. |
| **-sm \<modescript>** | Specifies a one-time custom script that runs on the device's first boot after installation. Use this script to configure **device‑mode**, **protected‑routerboot**, and other settings during device deployment. The mode script executes before any custom or default configuration scripts. Upon completion, the script is automatically removed from the device. If the script modifies the device-mode, the device reboots immediately after execution. **This feature requires RouterOS and Netinstall version 7.22 or newer.** |

### Network Options

| Parameter | Description |
| :-- | :-- |
| **--mac \<mac address>** | Specify a MAC address to allow for installation. When provided, all other BOOTP requests are ignored. |
| **-i \<interface>** | Specify a network interface for the installation (optional, recommended). |
| **-a \<client-ip>** | Specify a specific IP address that the Netinstall server assigns to the device. This is mandatory unless using the `-i` parameter, which allows auto-assignment. |

### Package Selection

| Parameter | Description |
| :-- | :-- |
| **PACKAGES** | Specify a list of RouterOS packages in .NPK format to install on the device. This parameter is mandatory. The **system package** must be listed first. |

:::warning
**Configuration Preservation Behavior:**

When neither `-r` nor `-e` is specified, netinstall-cli reinstalls RouterOS while preserving the current configuration. It downloads the existing configuration database from the router, reformats the disk during reinstallation, then uploads the configuration back to the device. This matches the **"Keep old configuration"** option in the Netinstall GUI.

Note: This process applies only to the configuration itself. Files and databases such as User Manager database, Dude database, and other data stored separately are not preserved.
:::

## Linux Netinstall Example

Download the tool from the [MikroTik Download Page](https://mikrotik.com/download):

```bash
wget https://download.mikrotik.com/routeros/[VERSION]/netinstall-[VERSION].tar.gz
```

Extract the archive:

```bash
tar -xzf netinstall-[VERSION].tar.gz
```

Configure the network interface (replace eth0 with your interface name):

```bash
sudo ip link set eth0 down
sudo ip addr add 192.168.88.2/24 dev eth0
sudo ip link set eth0 up
```

Run the installation. The tool requires root privileges, use sudo:

```bash
sudo ./netinstall-cli [-parameters] [address/interface] routeros-[architecture]-[package VERSION].npk
```

```bash
sudo ./netinstall-cli -i eth0 -v -e  routeros-7.23.1-arm64.npk wifi-qcom-7.23.1-arm64.npk container-7.23.1-arm64.npk 
Version: 7.24beta1(2026-05-26 11:17:51)
Will apply empty config
Waiting for Link-UP on eth0
Using client IP 192.168.88.3
Waiting for RouterBOARD...
Received a BOOTP request from 01:23:45:67:89:AA (arm64)
Assigned 192.168.88.3 to 01:23:45:67:89:AA
blksize 1452
Booting device 01:23:45:67:89:AA into setup mode
Formatting device 01:23:45:67:89:AA
Sending packages to device 01:23:45:67:89:AA
Packages sent to device 01:23:45:67:89:AA
Rebooting device 01:23:45:67:89:AA
Successfully finished installing device 01:23:45:67:89:AA
```

:::tip
Looking for a different installation method? See the [**Windows**](./netinstall-windows.md) or [**Netinstall Package**](./netinstall-package.md) instructions.
:::
