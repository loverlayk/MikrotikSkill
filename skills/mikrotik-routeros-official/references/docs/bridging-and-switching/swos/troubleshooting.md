# Cannot upgrade SwOS

> MikroTik switches that support SwOS store two separate firmware images in flash memory: a primary (active) image and a backup image. Under normal operation, the device boots from the primary image. When a firmware...

# Cannot upgrade SwOS

---

## Overview

MikroTik switches that support SwOS store two separate firmware images in flash memory: a **primary** (active) image and a **backup** image. Under normal operation, the device boots from the primary image. When a firmware upgrade is initiated — either automatically via the web interface or manually via file upload — the device writes the new image to the primary slot and reboots into it.

Upgrade failures typically occur due to one of the following:

- Incorrect firmware file selected (wrong model or firmware branch)
- Interrupted write operation leaving the primary image corrupted
- Network connectivity issue preventing the automatic download from reaching MikroTik servers
- On dual-boot devices: device-mode policy restricting OS transitions (RouterOS 7.17+)

SwOS-only devices and dual-boot devices require different recovery procedures, described separately below.

---

## Before You Begin

> **Warning:** The reset button procedure described in this article will erase the active configuration and load factory defaults. Export a configuration backup from the **System** tab before proceeding.

Confirm which firmware file you need before attempting a manual upgrade. Each switch series uses a dedicated firmware binary — cross-series firmware files are not interchangeable and will be rejected or cause a boot failure. The correct file for your device can be found at:

[mikrotik.com Software download centre](https://mikrotik.com/download)

---

## Resolution

### SwOS-only Devices (CSS series)

These devices do not run RouterOS and have no serial console boot menu. Recovery relies on the hardware backup firmware stored in a protected flash partition.

**Step 1 — Attempt manual firmware upload**

Navigate to the **Upgrade** tab in the SwOS web interface, select the correct `.swos` firmware file for your device model, and click **Upgrade**. Do not interrupt power during the write process. After the upload completes, the device will reboot automatically. Reload the web interface and verify the firmware version shown in the **System** tab.

**Step 2 — Boot into backup firmware via hardware reset**

If the manual upload fails or the device becomes unreachable after the upgrade attempt, the backup (primary) firmware can be force-loaded using the reset button:

1. Disconnect power from the device.
2. Hold the **Reset** button and reapply power.
3. Continue holding the button for approximately 5 seconds until the device completes its boot sequence.
4. Release the button.

The device will load the backup firmware and apply the factory default configuration. It will be accessible at **192.168.88.1** or at a DHCP-assigned address.

**Step 3 — Reattempt manual firmware upload**

Once the device is accessible on the backup firmware, repeat the manual upgrade procedure from Step 1. The backup firmware environment provides a clean state from which the upgrade is more likely to succeed.

---

### Dual-Boot Devices (CRS series)

Dual-boot devices store both SwOS and RouterOS and can boot into either operating system. This provides additional recovery paths, including upgrade via the RouterOS CLI.

**Step 1 — Attempt manual firmware upload**

As with SwOS-only devices, first attempt a manual upgrade via the **Upgrade** tab in the SwOS web interface using the correct firmware file for your device.

**Step 2 — Boot into backup SwOS via serial console**

If the manual upload fails, connect to the device using a serial console cable with the following parameters:

| Parameter | Value |
| --- | --- |
| Baud rate | 115200 |
| Data bits | 8 |
| Stop bits | 1 |
| Parity | None |
| Flow control | None |

At the boot menu prompt, select:

```
p - boot primary SwOS
```

This loads the factory backup SwOS image. Once the device is accessible, reattempt the manual firmware upload as described in Step 1.

**Step 3 — Boot into RouterOS via reset button (no console access)**

If no serial console port is available or no cable is at hand, the device can be forced into RouterOS using the reset button:

1. With the device powered on, press and hold the **Reset** button.
2. Hold until the user LED begins to flash (approximately 5 seconds).
3. Release the button.

The device will reset the RouterOS configuration to factory defaults and boot into RouterOS.

> **Warning:** This procedure resets the RouterOS configuration. Ensure a RouterOS configuration backup exists before proceeding if the device was previously running RouterOS.

**Step 4 — Upgrade SwOS from RouterOS CLI**

Once booted into RouterOS, SwOS can be upgraded directly without using the web interface. The following command fetches and installs the latest available SwOS firmware for the device:

```
/system swos upgrade
```

Internet access is required for this command to resolve and download the correct firmware package from MikroTik's update servers. Verify connectivity before executing.

**Step 5 — Device-mode restriction (RouterOS 7.17 and later)**

Starting with RouterOS **v7.17**, the `device-mode` policy restricts OS transitions between SwOS and RouterOS on dual-boot hardware. If the upgrade command fails or OS switching is blocked, explicitly permit the transition with:

```
/system/device-mode/update routerboard=yes
```

This command must be executed in RouterOS before re-attempting the SwOS upgrade or switching back to SwOS.

**Step 6 — Return to SwOS**

After the SwOS firmware has been successfully updated from RouterOS, set the default boot target back to SwOS and reboot the device:

```
/system routerboard settings set boot-os=swos
/system reboot
```

The device will restart and load the newly installed SwOS firmware.
