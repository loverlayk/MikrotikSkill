# settings

> This sub-menu configures RouterBOOT firmware settings. These settings control how the device starts and operates at the hardware level.

-----------

## system/routerboard/settings 
**Conditions:** !i386
**Type:** Settings Directory

This sub-menu configures RouterBOOT firmware settings. These settings control how the device starts and operates at the hardware level.

```ros
[admin@MikroTik] /system/routerboard/settings> print 
              auto-upgrade: no
                 baud-rate: 115200
                boot-delay: 2s
            enter-setup-on: any-key
               boot-device: nand-if-fail-then-ethernet
         preboot-etherboot: disabled
             cpu-frequency: 1200MHz
          memory-frequency: 1066DDR
             boot-protocol: bootp
       enable-jumper-reset: yes
       force-backup-booter: no
               silent-boot: yes
      protected-routerboot: disabled
      reformat-hold-button: 20s
  reformat-hold-button-max: 10m
```

:::info
The device-mode setting restricts SwOS/RouterOS transitions for dual-boot devices. To enable it, run:
`/system/device-mode/update routerboard=yes`
:::

:::danger
Overclocking the CPU or memory is not covered by warranty. If you suspect overclocking causes performance issues, return both frequencies to their nominal values before contacting support.
:::

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="auto-upgrade" typ="bool">Whether to upgrade firmware automatically after a RouterOS upgrade. The latest firmware will be applied after an additional reboot.</ArgTableRow>
<ArgTableRow arg="baud-rate" typ="enum (115200 | 57600 | 38400 | 19200 | 9600 | 4800 | 2400 | 1200) { 115200:0, 57600:1, 38400:2, 19200:3, 9600:4, 4800:5, 2400:6, 1200:7 }">Choose the onboard RS232 speed in bits per second, if installed. The **off** option disables the serial interface.</ArgTableRow>
<ArgTableRow arg="boot-delay" typ="time">How much time to wait for a keystroke while booting.</ArgTableRow>
<ArgTableRow arg="init-delay" typ="time">Used only for mPCIe modems on RB9xx series devices. If your modem is not recognized after a soft reboot, set a delay before the USB port is initialized.</ArgTableRow>
<ArgTableRow arg="enter-setup-on" typ="enum (any-key | delete-key) { any-key:0, delete-key:1 }">Specifies which key causes the BIOS to enter configuration mode during the boot delay. Useful when the serial console prints symbols during the boot process and enters the RouterBOOT menu by itself. In some serial terminal programs, you cannot use the <kbd>Delete</kbd> key to enter the setup. In this case, use the <kbd>Backspace</kbd> key instead.</ArgTableRow>
<ArgTableRow arg="boot-device" typ="enum">
Choose how RouterBOOT loads the operating system:
- **ethernet** — boot the device in Etherboot mode.
- **flash-boot** — enable Flashfig mode on startup. This setting reverts to NAND after a successful configuration change, or when a user logs into the board.
- **flash-boot-once-then-nand** — enable Flashfig mode on startup for a single boot only. After that, the setting resets to `nand-if-fail-then-ethernet`.
- **nand-if-fail-then-ethernet** — boot RouterOS from the NAND. If RouterOS does not boot, the device goes to Etherboot automatically. This is the default mode for devices straight out of the box.
- **nand-only** — boot RouterOS from the NAND.
- **try-ethernet-once-then-nand** — boot the device in Etherboot mode once. If no server is available, the device boots directly from the NAND or the storage type the device uses.

Etherboot mode is a special state for a MikroTik device. You can use it to reinstall the device with Netinstall.  
You can put the device into Etherboot mode in several ways, depending on the device you use:
1. Press the Reset button and power on the device. Wait until the USR LED blinks, then stays on, and then turns off. Release the Reset button. The device boots in bootp mode to reinstall RouterOS with Netinstall.
2. Use the serial console. When the device boots, press and hold <kbd>Control</kbd>+<kbd>E</kbd> until the device shows that it is trying the bootp protocol.
3. Use the serial console. Press any key while the device boots, and then press <kbd>O</kbd>, <kbd>1</kbd>, and <kbd>X</kbd>.
</ArgTableRow>
<ArgTableRow arg="preboot-etherboot" typ="alt { symbolic-names: enum (disabled) { disabled:0 }
, timeout: time [1 .. 30]
 }">Enables preboot-etherboot, which runs before the regular boot device. It works the same as `boot-device=etherboot`, but has an additional timeout value. If an IP address is not received from the Netinstall server before the timeout expires, the regular boot process starts.The preboot-etherboot configuration is stored in the BIOS, so downgrading RouterOS to an earlier version does not disable it. You can disable it from the RouterOS menu or by resetting the BIOS.Because etherboot accepts IP addresses from any BOOTP/DHCP server, use preboot-etherboot-server to start etherboot only when the address is received from the specified Netinstall server.</ArgTableRow>
<ArgTableRow arg="preboot-etherboot-server" typ="alt { symbolic-names: enum (any) { any:0 }
, ip: ipAddr
 }">Sets preboot-etherboot to accept an IP address only from the specified Netinstall server. This setting prevents unintentional etherboot from other BOOTP/DHCP servers.</ArgTableRow>
<ArgTableRow arg="etherboot-port" typ="enum (ether1 | ether2) { ether1:0, ether2:1 }">Selects the Etherboot/Netinstall interface. Applies only to CRS520, CRS804, and CRS812. The default port depends on the model.</ArgTableRow>
<ArgTableRow arg="boot-os" typ="enum (router-os | swos) { router-os:0, swos:1 }">Changes the boot operating system for CRS3xx series switches.</ArgTableRow>
<ArgTableRow arg="regulatory-domain-ce" typ="bool">Enables extra-low TX power for high antenna gain devices (requires a reboot).</ArgTableRow>
<ArgTableRow arg="cpu-mode" typ="enum (power-save | regular) { power-save:0, regular:1 }">Whether the CPU enters suspend mode on the HLT instruction. Most operating systems use the HLT instruction during the CPU idle cycle. When the CPU is in suspend mode, it consumes less power. In low-temperature conditions, you should choose the regular mode, so the overall system temperature is higher.</ArgTableRow>
<ArgTableRow arg="cpu-frequency" typ="enum">Use this option to change the CPU frequency of the device. Values depend on the model. To see the available options, press <kbd>?</kbd> in RouterOS version 6 or <kbd>F1</kbd> in RouterOS version 7 at this prompt.</ArgTableRow>
<ArgTableRow arg="memory-frequency" typ="enum">Use this option to change the memory frequency of the device. Values depend on the model. To see the available options, press <kbd>?</kbd> in RouterOS version 6 or <kbd>F1</kbd> in RouterOS version 7 at this prompt.</ArgTableRow>
<ArgTableRow arg="memory-data-rate" typ="enum">Use this option to change the memory data rate of the device. Values depend on the model. To see the available options, press <kbd>?</kbd> in RouterOS version 6 or <kbd>F1</kbd> in RouterOS version 7 at this prompt.</ArgTableRow>
<ArgTableRow arg="preferred-architecture" typ="enum (arm32 | arm64) { arm32:0, arm64:1 }">Specific setting for L009 devices. Updates the device to use the ARM64 architecture.</ArgTableRow>
<ArgTableRow arg="boot-protocol" typ="enum (bootp | dhcp) { bootp:0, dhcp:1 }">The boot protocol to use:- **bootp** — the default option for booting RouterOS.- **dhcp** — used for OpenWrt and possibly other operating systems.</ArgTableRow>
<ArgTableRow arg="enable-jumper-reset" typ="bool">Disable this option to prevent an accidental settings reset through the onboard jumper.</ArgTableRow>
<ArgTableRow arg="force-backup-booter" typ="bool">Whether to use the backup RouterBOOT. This setting is useful only if the main loader is corrupted and cannot be fixed. Instead of booting the device with a pressed reset button (which loads the backup loader), you can use this setting to load it on every boot.</ArgTableRow>
<ArgTableRow arg="silent-boot" typ="bool">This option disables beeping sounds during boot (does not disable the RouterOS `beep` command).</ArgTableRow>
<ArgTableRow arg="disable-pci" typ="bool">Specific setting for devices with the MT7621 chip. Disables PCI.</ArgTableRow>
<ArgTableRow arg="gpio-function" typ="ubit (serial1)">Specific setting for M33 devices. By default, pins 12, 13, 15, and 16 are configured for use of the second `serial1` port. You can reassign them for GPIO use in the `/iot/gpio/digital` menu.</ArgTableRow>
<ArgTableRow arg="protected-routerboot" typ="enum (disabled | enabled)">
Disables access to the RouterBOOT configuration over the serial console and prevents the reset button from changing boot mode (Netinstall is disabled). You can access RouterOS only with a known RouterOS user account with administrative privileges. You can disable this setting only from within RouterOS. If you lose the RouterOS password, recovery requires a full device reformat with the reset button timing procedure.
- **enabled** — secure mode. RouterOS is accessible only with a valid admin-level account. Serial input is ignored, Etherboot is disabled, and RouterBOOT settings cannot be changed.
- **disabled** — normal operation. RouterBOOT settings are accessible through the serial console, and the reset button can be used to enter Netinstall mode.
</ArgTableRow>
<ArgTableRow arg="reformat-hold-button" typ="time">
Defines the minimum time the reset button must be held at power-on to trigger a full device reformat. The hold time must be longer than this value, but shorter than `reformat-hold-button-max`. When triggered, the device performs a complete reset operation:
- RouterOS, all files, and configuration are permanently erased (NAND reformat).
- All RouterBOOT settings are reset to defaults.
- The device reboots.
- Because NAND boot fails, the device enters Etherboot automatically.
- Netinstall is required to reinstall RouterOS.

This operation is extremely dangerous. Use it only when all other access methods are unavailable. On some RouterBOARD devices, the reformat process can take more than 5 minutes. The device is ready for Netinstall after the reformat completes.
</ArgTableRow>
<ArgTableRow arg="reformat-hold-button-max" typ="time">
Defines the maximum time the reset button can be held during a reformat trigger. Works together with `reformat-hold-button` to create a precise time window.  
For example, setting `reformat-hold-button=60s` and `reformat-hold-button-max=65s` requires the button to be held strictly between 60 and 65 seconds. This increases security by making accidental or guessed resets practically impossible. Introduced in RouterBOOT 3.38.3.
</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="safe-cpu-frequency" typ="enum"></ArgTableRow>
</ArgTable>
