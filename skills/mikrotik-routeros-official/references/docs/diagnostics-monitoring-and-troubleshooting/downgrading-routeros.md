# Downgrading RouterOS

> Learn how to downgrade RouterOS to a previous version, including pre-downgrade checks, architecture verification, and step-by-step instructions.

You can downgrade RouterOS **only as far as the minimum version supported by your hardware**. Check it with the following command:

```ros
/system/resource/print
                   uptime: 2m18s
                  version: 7.26beta1
               build-time: 2026-10-01 13:29:47
          minimum-version: 7.0.9
              free-memory: 681.8MiB
             total-memory: 1024.0MiB
                      cpu: ARM64
                cpu-count: 4
            cpu-frequency: 864MHz
                 cpu-load: 3%
           free-hdd-space: 91.8MiB
          total-hdd-space: 128.0MiB
  write-sect-since-reboot: 64
         write-sect-total: 266154
               bad-blocks: 0%
        architecture-name: arm64
               board-name: hAP ax^2
                 platform: MikroTik
```

The `minimum-version` field is the oldest RouterOS release supported by your hardware's bootloader. The exact value depends on the device. In earlier RouterOS versions the same value was shown as `factory-software` — treat that field identically if your version still prints it.

:::warning
Attempting to install a version older than `minimum-version` can cause severe system instability or brick the device.
:::

## Before you start

- **Back up everything.** Configuration syntax changes between major versions. A direct downgrade can corrupt settings. Generate a [binary backup (`.backup`)](../getting-started/configuration-management/backup.md) and an [export file (`.rsc`)](../getting-started/configuration-management/#configuration-export) before proceeding.
- **Security and stability.** Keep in mind that reverting to legacy versions exposes your router to older software bugs and patched security vulnerabilities.

## Downgrade procedure

1. **Verify the architecture.** Check the `architecture-name` field of `/system/resource/print` (for example `arm64`, `arm`, `mipsbe`, `mmips`, `x86`).
2. **Download the packages.** From the [MikroTik download page](https://mikrotik.com/download), download the **main bundle** for that architecture and your targeted older version — it contains the `routeros-<version>-<architecture>.npk` system package. Check `/system/package/print` for the other packages installed on the router and download each of them in the same target version from the "Extra packages" bundle. On a device with WiFi, this includes the wireless driver package (`wifi-qcom`, `wifi-qcom-ac` or `wireless`, depending on the device); other common extra packages are container, calea and cmr.
3. **Upload the files.** Connect to your router via WinBox, WebFig, or an FTP client, open the Files menu, and upload the `.npk` files: the main `routeros` package and every extra package from step 2.
4. **Run the downgrade.** Execute the command and confirm the prompt:

   ```ros
   /system/package/downgrade
   ```

   The router prompts for a reboot. During the reboot it checks the uploaded packages and downgrades RouterOS to the version they contain.
5. **Wait for the reboot.** The router restarts, unpacks the older version, and comes back online with the downgrade complete.

After the reboot, verify the new version with `/system/resource/print` and confirm that the `version` field shows the expected downgrade target.
