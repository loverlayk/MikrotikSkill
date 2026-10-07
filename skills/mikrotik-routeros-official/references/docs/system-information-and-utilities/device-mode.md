# Device mode

> The device-mode feature restricts router access and limits configuration options to enhance security, available in advanced, home, basic, or ros modes depending on device type and RouterOS version. Changes require...

# Device mode

The **device-mode** is a feature which sets specific limitations on a device, or limits access to specific configuration options. It helps to protect your router and network from attackers who might gain unauthorized access and use it as a gateway for attacks to other networks.

Available device-modes are `advanced`, `home`, `basic` and `rose`. Device-mode configuration is factory pre-installed on routers (for devices with MikroTik RouterOS v7.17 or later). `Advanced` (previously called `enterprise`) mode is configured for CCR and 1100 series devices, `home` mode is configured for home routers and `basic` mode is configured for any other type of device. For devices running versions prior to RouterOS version 7.17, all devices use the *advanced/enterprise* mode.

The device-mode is configured from [`/system/device-mode`](../cli-reference/system/device-mode) menu.

```ros
[admin@MikroTik] > /system/device-mode/print 
                 mode: advanced     
     allowed-versions: 7.13+,6.49.8+
              flagged: no           
     flagging-enabled: yes          
            scheduler: yes          
                socks: yes          
                fetch: yes          
                 pptp: yes          
                 l2tp: yes          
       bandwidth-test: yes          
          traffic-gen: no           
              sniffer: yes          
                ipsec: yes          
                romon: yes          
                proxy: yes          
              hotspot: yes          
                  smb: yes          
                email: yes          
             zerotier: yes          
            container: no           
  install-any-version: no           
           partitions: no           
          routerboard: yes          
        attempt-count: 0   
```

The device-mode parameters can be changed by the authorized RouterOS user, but physical access to the device is required to approve the changes.  
After changing the device-mode, you need to confirm it by pressing a button on the device itself, or perform a "cold reboot" — that is, unplug the power. When the change is confirmed, regardless of confirmation mode, the **device will be rebooted**.

## Check device mode in WinBox

Open **System > Device Mode** to inspect the restrictions:

1. **Mode** and **Allowed Versions** identify the configured mode and permitted RouterOS versions.
2. The per-tool fields show which operations are allowed. For example, check **Scheduler**, **Fetch**, or **Email** when one of those tools reports a device-mode restriction.

![WinBox Device Mode overview with the current mode and per-tool restrictions](./img/device-mode-winbox.webp)

The screenshot shows this router's existing `rose` configuration; it is not a factory default for every device. The overview is read-only. The **Update** action starts a mode-change procedure, which requires physical confirmation and reboots the device as described in the next section.

## Changing device-mode

Available modes or specific features can be changed with [`update`](../cli-reference/system/device-mode/update) command.

For example, change mode to `home`:

```ros
[admin@MikroTik] > /system/device-mode/update mode=home 
  update: please activate by turning power off or pressing reset or mode button 
          in 5m00s
-- [Q quit|D dump|C-z pause]
```

If no power off or button press is performed within the specified time, the mode change is canceled. If another update command is run in parallel, both will be canceled.

:::danger
There are several EOL products which do not confirm mode changes with a reset button press. These routers can confirm a mode change only with a power cycle.
:::

To protect the device against an attacker who might silently gain access to your router, abuse it with some scripts and simply try to wait until you reboot your router and not even know that at that time you are accepting changes requested by some intruder, you can update the mode only three times. A counter tracks how many update attempts are made and will not allow any more updates. This counter can be reset only when the administrator does a power cycle or presses a button when seeing a warning on mode settings update attempt (same as with accepting any updates).

```ros
[admin@MikroTik] > /system/device-mode/update container=yes 
  update: too many unsuccessful attempts, turn off power or reboot by pressing reset or mode button in 4m55s to reset attempt-count
```

If the update command specifies any of the mode parameters, this update replaces the entire device-mode configuration. In this case, all per-feature settings will be lost, except those specified with this command. For instance:

```ros
[admin@MikroTik] > /system/device-mode/update mode=home email=yes fetch=yes
[admin@MikroTik] > /system/device-mode/print config
   mode: home
  fetch: yes
  email: yes
[admin@MikroTik] > /system/device-mode/update mode=advanced sniffer=no
-- reboot --
[admin@MikroTik] > /system/device-mode/print config
     mode: advanced
  sniffer: no

```

We see that `fetch` = yes and `email` = yes are missing, as they were overridden with the mode change. However, specifying only per-feature settings will change only those:

```ros
[admin@MikroTik] > /system/device-mode/update hotspot=no
-- reboot --
[admin@MikroTik] > /system/device-mode/print config
     mode: advanced
  sniffer: no
  hotspot: no
```

If the feature is disabled, an error message is displayed for interactive commands:

```ros
[admin@MikroTik] > /system/device-mode/print config
     mode: advanced
  sniffer: no
  hotspot: no
[admin@MikroTik] > /tool/sniffer/quick 
failure: not allowed by device-mode
```

However, it is possible to add configuration to a disabled feature, but there will be a comment showing the disabled feature in the device-mode:

```ros
[admin@MikroTik] > /ip/hotspot/add interface=ether1 
[admin@MikroTik] > /ip/hotspot/print 
Flags: X, S - HTTPS
Columns: NAME, INTERFACE, PROFILE, IDLE-TIMEOUT
#   NAME      INTERFACE  PROFILE  IDLE-TIMEOUT
;;; inactivated, not allowed by device-mode
0 X hotspot1  ether1     default  5m          
```

## Changing device-mode settings using Netinstall or FlashFig

Starting from RouterOS 7.22, it is possible to configure **device-mode** and **protected-routerboot** and other settings.

For more information, see the [Netinstall](../getting-started/installation-and-upgrade/netinstall/index.md) and [FlashFig](../management-tools/flashfig.md) documentation.

## Available device-mode modes

There are four device modes available for configuration (*advanced* is the default), each mode has a subset of features that are not allowed when it is used. No mode has all features enabled — certain features need to be enabled even when you have *advanced* mode enabled. ROSE device-mode is very similar to advanced mode, but it is made for RDS and similar devices with a wider option to use disks, supporting container installations from the factory. See the table below for more details about what each feature controls. As the table below shows, **traffic-gen**, **container**, **partitions**, and **routerboard** features are always disabled, unless specifically enabled by the admin user.

| Feature / Property | Actions/unavailable menus | Home | Basic | Advanced | ROSE |
| :-- | :-- | :-- | :-- | :-- | :-- |
| [**Bandwidth Test**](../diagnostics-monitoring-and-troubleshooting/bandwidth-test.md) | `/tool/bandwidth-test`, `/tool/bandwidth-server`, `/tool/speed-test` | No | No | Yes | Yes |
| [**Containers**](../containers/index.md) | All container functionality. | No | No | No | Yes |
| [**Email**](./e-mail.md) | `/tool/e-mail` | No | Yes | Yes | Yes |
| [**Fetch**](./fetch.md) | `/tool/fetch` | No | Yes | Yes | Yes |
| [**Hotspot**](../authentication-authorization-accounting/hotspot-captive-portal/index.md) | `/ip/hotspot` | No | No | Yes | Yes |
| **Install Any Version** | RouterOS will no longer allow installation of versions below the **allowed-versions** list. | No | No | No | No |
| [**IPsec**](../virtual-private-networks/ipsec/index.md) | `/ip/ipsec` | Yes | Yes | Yes | Yes |
| [**L2TP**](../virtual-private-networks/l2tp/index.md) | `/interface/l2tp-server`, `/interface/l2tp-client` | Yes | Yes | Yes | Yes |
| [**Partitions**](./partitions.md) | `/partitions` — does not allow changing the count of partitions. If your router is unable to boot, it will still be able to boot into your other partitions. No restriction for crash recovery. | No | No | No | No |
| [**PPTP**](../virtual-private-networks/pptp.md) | `/interface/pptp-server`, `/interface/pptp-client` | Yes | Yes | Yes | Yes |
| [**Proxy**](../network-management/proxy/web-proxy) | `/ip/proxy` | No | No | Yes | Yes |
| [**RoMon**](../management-tools/romon.md) | `/tool/romon` | No | Yes | Yes | Yes |
| [**Routerboard Settings**](../hardware/routerboard.md) | `/system/routerboard/settings` (except auto-upgrade option) | No | No | No | No |
| [**Scheduler**](./scheduler.md) | `/system/scheduler` | No | Yes | Yes | Yes |
| [**SMB**](../storage/smb.md) | `/ip/smb` | Yes | Yes | Yes | Yes |
| [**Sniffer**](../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) | `/tool/sniffer` | No | Yes | Yes | Yes |
| [**SOCKS Proxy**](../network-management/socks/index.md) | `/ip/socks` | No | No | Yes | Yes |
| [**Traffic Generator**](../diagnostics-monitoring-and-troubleshooting/traffic-generator.md) | `/tool/traffic-generator`, `/tool/flood-ping`, `/tool/ping-speed` | No | No | No | No |
| [**ZeroTier**](../virtual-private-networks/zerotier.md) | `/zerotier` | No | No | Yes | Yes |

More specific control over the available features is possible. Each of the features controlled by device-mode can be specifically turned on or off.

For instance, **scheduler** won't allow performing any action in `/system/scheduler`. The used device-mode disables all listed features, for instance, if **mode**=home is used, but **zerotier** is required for your setup, a device-mode update `/system/device-mode/update` zerotier=yes will be required with physical access to the device to push the button or cut the power.

## Allowed versions

Device mode lists in its parameters an argument called **allowed-versions**. This is a list of versions which MikroTik considers as secure and which do not include any serious vulnerabilities that an attacker could exploit.

This setting does not depend on the installed RouterOS version and works as a separate protection layer, to prevent an attacker from downgrading the version step-by-step to reach a known vulnerable RouterOS release. When you upgrade RouterOS to a release where a newer **allowed-versions** list is available, the oldest list will be overwritten. If you downgrade RouterOS, the **allowed-versions** list will not change and will remain updated to the latest list. The list is ignored if device-mode **install-any-version** is enabled.

## Flagged status

Along with the device-mode feature, RouterOS can analyze the whole configuration at system startup, to determine if there are any signs of unauthorized access to your router. If suspicious configuration is detected, it will be disabled and the **flagged** parameter will be set to *yes*. The device now has a flagged state and enforces certain limitations.

```ros
[admin@MikroTik] > /system/device-mode/print 
     mode: advanced
  flagged: yes
...
```

If the system has this flagged status, the current configuration works, but it is not possible to perform the following actions:

- bandwidth-test, traffic-generator, and sniffer
- Configuration actions that enable or create new entries (it will still be possible to disable or delete them) for: system scheduler, SOCKS proxy, PPTP, L2TP, IPsec, proxy, and SMB.

When performing the aforementioned actions while the router has the flagged state, you will receive an error message:

```ros
[admin@MikroTik] > /tool/sniffer/quick 
failure: configuration flagged, check all router configuration for unauthorized changes and update device-mode
[admin@MikroTik] > /int l2tp-client/add connect-to=1.1.1.1 user=user
failure: configuration flagged, check all router configuration for unauthorized changes and update device-mode
```

To exit the flagged state, you must perform the command `/system/device-mode/update flagged=no`. The system will ask you to either press a button, or issue a hard reboot (cut power physically or do a hard reboot of the virtual machine).

**Important!** Although the system has disabled any malicious-looking rules that triggered the flagged state, it is crucial to inspect all of your configuration for other unknown things before exiting the flagged state. If your system has been flagged, assume that your system has been compromised and do a full audit of all settings before re-enabling the system for use. After completing the audit, change all the system passwords and upgrade to the latest RouterOS version.

:::warning
Starting from RouterOS version 7.17, device-mode restricts SwOS/RouterOS transition for dual-boot devices. To enable it: `/system/device-mode/update` routerboard=yes
:::
