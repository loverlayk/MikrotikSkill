# RouterBOARD

> This page documents the /system/routerboard menu in MikroTik RouterOS, providing hardware and firmware information such as model, serial number, and current/upgrade firmware versions. It includes upgrade instructions...

# RouterBOARD

On RouterBOARD devices, you can view basic hardware and firmware information from the `/system/routerboard` menu.

To display this information, run the following command:

```ros
[admin@demo.mt.lv] /system/routerboard/print 
       routerboard: yes                                                      
             model: CCR2116-12G-4S+                                                                                                
     serial-number: MT123456789                                              
     firmware-type: al64v3                                                   
  minimum-firmware: 7.8                                                      
  current-firmware: 7.22.2
  upgrade-firmware: 7.22.2                          
```

Detailed description of each parameter can be found in [CLI reference](../cli-reference/system/routerboard/routerboard.md).

## Upgrading RouterBOOT

RouterBOOT upgrades typically include minor improvements to overall RouterBOARD operation. You should keep the firmware up to date.

To check whether an upgrade is available, compare the **current-firmware** and **upgrade-firmware** values under `/system/routerboard`. If **upgrade-firmware** shows a higher version than **current-firmware**, a newer version is ready to be applied.

### Upgrade Steps

1. Run the upgrade command:

   ```ros
   [admin@mikrotik] /system/routerboard> upgrade
   Do you really want to upgrade firmware? [y/n]
   y
   echo: system,info,critical Firmware upgraded successfully, please reboot for changes to take effect!
   ```

2. When prompted, enter **y** to confirm.

3. Reboot the device to apply the changes:

   ```ros
   /system/reboot
   ```

After the reboot, verify that **current-firmware** matches **upgrade-firmware**. Matching values confirm the upgrade applied successfully.

## Preboot Etherboot

Preboot etherboot instructs a RouterOS device to search for a Netinstall server on every boot for a specified amount of time, before starting the regular boot process (for example, RouterOS).

By default, Etherboot accepts addresses from any BOOTP/DHCP server, but it is possible to lock preboot-etherboot process to aspecific Netinstall server with a specific IP address with [`preboot-etherboot-server`](../cli-reference/system/routerboard/settings/settings.md#preboot-etherboot-server) parameter.

When both options are enabled, you can reinstall the device remotely without accessing RouterOS or pressing the reset button.

For example:
1. Power cycle the RouterOS device (for example, with a PoE switch or power controller).
2. The device attempts Etherboot and connects to the Netinstall server.
3. After installation, disable the Netinstall server.
4. Power cycle the device again to complete the process.

Run:

```ros
/system/routerboard/settings/set preboot-etherboot=9s preboot-etherboot-server=10.10.10.100
```

On every reboot or power cycle, the device attempts to receive an IP address from the Netinstall server with the IP address **10.10.10.100** for **9 seconds**. If no such server is available, the device continues with the normal boot process.

:::warning
If `preboot-etherboot-server` is not specified, the device accepts an IP address from any Netinstall server and enters Etherboot mode, waiting for a reinstall process. DHCP servers are used only if the RouterBOOT `boot-protocol` is set to **dhcp** (the default is **bootp**).
:::

RouterOS reinstallation does not affect BIOS settings. If preboot-etherboot is enabled, the device continues to attempt Etherboot on every boot.

To prevent unintended Etherboot activation without accessing RouterOS, disable any attached Netinstall or DHCP server.

## Protected RouterBOOT

The Protected RouterBOOT setting protects a RouterOS device from physical access by disabling Etherboot and restricting access to the bootloader.

You can enable or disable this setting only from within RouterOS after login. No RouterBOOT setting controls it directly. These additional options appear only under certain conditions.

:::warning
If you forget the RouterOS admin password while Protected RouterBOOT is enabled, the device cannot be recovered without performing a complete reformat.
:::

### Behavior When Enabled

When this setting is active:

- The reset button and reset pin-hole are disabled.
- The RouterBOOT menu is inaccessible via serial console.
- Etherboot (Netinstall) is disabled.
- You can access the device only through RouterOS with a valid admin password.
- You can enable or disable this setting only from within RouterOS. No RouterBOOT-level option exists.

:::warning
If you enable Protected RouterBOOT and forget your RouterOS password, **the device cannot be recovered** through normal means.
:::

### Enabling or Disabling

Starting from RouterOS v7, enabling or modifying this setting requires confirmation by pressing the reset or mode button.

You have **60 seconds** to confirm the change.

#### Enable (Example)

```ros
[admin@450] > /system/routerboard/settings/set protected-routerboot=enabled
[admin@450] > /system/routerboard/settings/print
                        ;;; press button within 60 seconds to confirm
                            protected routerboot enable
              auto-upgrade: no
                 baud-rate: 115200
                boot-delay: 2s
            enter-setup-on: any-key
               boot-device: nand-if-fail-then-ethernet
             cpu-frequency: auto
             boot-protocol: bootp
       enable-jumper-reset: yes
       force-backup-booter: no
               silent-boot: yes
      protected-routerboot: enabled
      reformat-hold-button: 20s
  reformat-hold-button-max: 10m
```

#### Disable (Example)

```ros
/system/routerboard/settings/set protected-routerboot=disabled
```

:::warning
If the button is not pressed within the timeout, the change is not applied.
:::

### Emergency Reformat (Recovery Method)

As an emergency recovery option, you can reset the device by holding the reset button during power-on for longer than `reformat-hold-button`, but shorter than `reformat-hold-button-max`.

:::danger
EXTREMELY DANGEROUS. Use this only if you have lost all access to the device.
:::

When triggered, the following actions are performed:

- RouterOS, all files, and configuration are completely and irreversibly erased (NAND reformat).
- All RouterBOOT settings are reset to defaults.
- The device reboots.
- Because boot from NAND fails, the device enters Etherboot mode automatically. Netinstall is required to reinstall RouterOS.

:::note
Reformat on some RouterBOARD devices can take more than 5 minutes.
:::

### LED Indicator

When Protected RouterBOOT is enabled, the LED blinks every second to assist with timing:

- LED off for one second.
- LED on for one second.

### Support on Older MikroTik Hardware

:::warning
This section applies only to older devices that display the specific error message described in the following text. Do not modify the bootloader unless that message instructs you to do so.
:::

The Protected RouterBOOT setting is supported on all modern MikroTik devices. However, if you are using an older device whose minimum firmware version is earlier than **7.19.3**, you might see the following message when you attempt to enable it:

> *"The 'protected routerboot' feature requires a backup-routerboot upgrade"*

If you see this message, follow the steps for your RouterOS version.

#### RouterOS v7 — Upgrade Steps

1. [Upgrade or downgrade](../getting-started/installation-and-upgrade/upgrade.md#manual-upgrade) your device to RouterOS **7.19.3** specifically. You can find this release on the [MikroTik download page](https://mikrotik.com/download).

2. Upgrade the RouterBOOT firmware by running `/system/routerboard/upgrade`, then reboot the device. After rebooting, verify that the **current-firmware** value shown in `/system/routerboard/print` matches the installed RouterOS version shown in `/system/resource/print` — both should be **7.19.3**.

3. Upload the [v7 universal package (all architectures)](https://box.mikrotik.com/f/991c3e94984c4e18b8d6/?dl=1) to the device and reboot again. This updates the **minimum-firmware** version to **7.19.3**, which is required to enable the Protected RouterBOOT setting.

4. When the previous steps are complete, you can upgrade the device to a later RouterOS release.

#### RouterOS v6 — Upgrade Steps

If your device is running RouterOS **v6** and you encounter the same message, follow the steps in the previous section, with these differences:

- Target version: **6.49.7** (instead of 7.19.3)
- Use the [v6 universal package (all architectures)](https://box.mikrotik.com/f/b062a26b4bd34c55aa52/?dl=1) (instead of the v7 package)

## Mode and Reset Buttons

All MikroTik devices running RouterOS support additional options for the **Reset** button. Select RouterBOARD devices also include a **Mode** button, which you can configure to run a custom script when pressed.

---

### Supported Devices (Mode Button)

The following devices support the Mode button:

- RBcAP-2nD (cAP)
- RBcAPGi-5acD2nD (cAP ac)
- RBwsAP5Hac2nD (wsAP ac lite)
- RB750Gr3 (hEX)
- RB760iGS (hEX S)
- RB912R-2nD (LtAP mini, LtAP mini LTE/4G kit)
- RBD52G-5HacD2HnD (hAP ac²)
- RBLHGR (LHG LTE/4G kit)
- RBSXTR (SXT LTE/4G kit)
- CRS328-4C-20S-4S+RM
- CRS328-24P-4S+RM
- CCR1016-12G r2
- CCR1016-12S-1S+ r2
- CCR1036-12G-4S r2
- CCR1036-8G-2S+ r2
- RBD53G-5HacD2HnD (Chateau)
- RBD53GR-5HacD2HnD (hAP ac³)
- E50UG (hEX)
- L41G-2axD (hAP ax lite)
- L009UiGS-RM, L009UiGS-2HaxD-IN
- cAPGi-5HaxD2HaxD (cAP ax)
- C53UiG+5HPaxD2HPaxD (hAP ax³)
- S53UG+5HaxD2HaxD (Chateau ax)
- H53UiG-5HaxQ2HaxQ (Chateau PRO ax)
- CCR2116-12G-4S+
- RDS2216-2XG-4S+4XS-2XQ

---

### Basic Mode Button Example

The following example creates a script and assigns it to the Mode button. When the button is pressed, a message is written to the system log.

```ros
/system/script/add name=test-mode-button source={:log info message=("mode button pressed");}
/system/routerboard/mode-button/set on-event=test-mode-button enabled=yes
```

---

### Hold-Time Option

You can configure the button to trigger only when held for a specific duration. The following example activates the script when the Mode button is held for 3 to 5 seconds:

```ros
/system/script/add name=test-mode-button source={:log info message=("mode button pressed");}
/system/routerboard/mode-button/set on-event=test-mode-button hold-time=3..5 enabled=yes
```

The Reset button is configured in the same way as the Mode button, but uses a different menu path: `/system/routerboard/reset-button`.

```ros
/system/script/add name=test-reset-button source={:log info message=("reset button pressed");}
/system/routerboard/reset-button/set on-event=test-reset-button hold-time=0..10 enabled=yes
```

---

### Example: Toggle LED Dark Mode with the Mode Button

The following script toggles [LED dark mode](./leds.md#led-settings) on and off each time the Mode button is pressed:

```ros
/system/script/add name=dark-mode source={
   :if ([system leds settings get all-leds-off] = "never") do={
      /system/leds/settings/set all-leds-off=immediate
   } else={
      /system/leds/settings/set all-leds-off=never
   }
}
/system/routerboard/mode-button/set enabled=yes on-event=dark-mode
```

---

### WPS Button (D53, C53, S53, and H53 Series)

RouterBOARD devices in the D53, C53, S53, and H53 series include a configurable **WPS button**. It works the same way as the Mode and Reset buttons: it executes a script when pressed.

#### Basic WPS Button Example

```ros
/system/script/add name=test-wps-button source={:log info message=("wps button pressed");}
/system/routerboard/wps-button/set on-event=test-wps-button hold-time=0..10 enabled=yes
```

#### Trigger WPS Pairing with the WPS Button or Mode Button

The following script initiates WPS push-button pairing on all active Wi-Fi access point interfaces. You can assign it to the WPS button, the Mode button, or both.

```ros
/system/script/add name=wps-accept source={
    :foreach iface in=[/interface/wifi/find where (configuration.mode="ap" && disabled=no)] do={
        /interface/wifi/wps-push-button $iface;
    }
}

/system/routerboard/wps-button/set enabled=yes on-event=wps-accept
/system/routerboard/mode-button/set enabled=yes on-event=wps-accept
```
