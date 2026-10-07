# Downgrading RouterOS

> Learn how to downgrade RouterOS to a previous version, including pre-downgrade checks, architecture verification, and step-by-step instructions.

You can downgrade RouterOS, **but only until the factory-installed version**, which you can check with the following command:

```ros
/system/resource/print

          uptime: 1w1d11h11m1s
         version: 7.23.1 (stable)
      build-time: Jan/01/2026 11:11:11
factory-software: 7.20.8
```

:::warning
The factory-software version is the absolute oldest release supported by your hardware's bootloader. Attempting to install a version older than this can cause severe system instability or brick the device.
:::

## Pre-Downgrade Checklist

- **Back up everything.** Configuration syntax changes between major versions. A direct downgrade can corrupt settings. Always generate a [binary backup (`.backup`)](../getting-started/configuration-management/backup.md) and an [export file (`.rsc`)](../getting-started/configuration-management/#configuration-export) before proceeding.
- **Security and stability.** Keep in mind that reverting to legacy versions exposes your router to older software bugs and patched security vulnerabilities.

## Step-by-Step Downgrade Procedure

1. **Verify architecture.** Check your device's architecture type via `/system/resource/print` (look for the `architecture` field, e.g., `arm64`, `mipsbe`, `mmips`).
2. **Download packages.** Download the "Extra packages" or main bundle zip corresponding to that exact architecture and your targeted older version from the [MikroTik download page](https://mikrotik.com/download).
3. **Upload files.** Connect to your router via WinBox, WebFig, or an FTP client, open the Files menu, and upload all the required `.npk` files.
4. **Execute downgrade.** Run the downgrade sequence from the terminal:

   ```ros
   /system/package/downgrade
   ```

5. **Reboot.** Confirm the action when prompted. Issue `/system/reboot` to restart the router — it will unpack the older version and come back online with the downgrade complete.

After the reboot, verify the new version by running `/system/resource/print` and confirming that the `version` field reflects the expected downgrade target.
