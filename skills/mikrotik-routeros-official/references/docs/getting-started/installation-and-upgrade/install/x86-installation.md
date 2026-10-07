# x86 Installation

> This page provides a step-by-step guide for installing RouterOS on x86 hardware using USB or Netinstall, covering Windows/Linux/macOS methods, BIOS settings adjustments, and boot priority configurations for...

# x86 Installation

## USB

### Step-by-step guide

1. Download the x86 CD image file from the download page: https://mikrotik.com/download

    - On Windows systems:

        - Download Rufus: https://github.com/pbatard/rufus/releases (use the latest version)
        - Connect your USB drive and open Rufus
        - Select the downloaded ISO image and click **START**

    - On Linux, FreeBSD, or macOS systems:

        :::danger
        Warning! Double-check the correct device address — `dd` can destroy data irreversibly.
        :::

        - Connect the USB drive and identify its device address

            macOS:

            ```text
            diskutil list
            ```

            Linux / FreeBSD:

            ```text
            fdisk -l
            ```

        - Ensure that the USB drive is formatted and all old data is erased before using the `dd` command

    Write the image to disk using `dd`:

    ```bash
    dd if=<your_downloaded_routeros_ISO> of=<disk_address> bs=1M status=progress
    ```

    macOS:

    ```bash
    dd if=<your_downloaded_routeros_ISO> of=<disk_address> bs=1m status=progress
    ```

    After the process completes, connect the USB drive to your x86 system and boot from it.

    Proceed with the installation by pressing **"i"** on your keyboard.

    After reboot, RouterOS will be installed.

Boot priority should be adjusted in BIOS settings. If RouterOS is installed on an NVMe drive, the USB must be booted in UEFI mode.

Make sure that CSM (Compatibility Support Module) is disabled in the BIOS boot settings.

## Install the x86 system using Netinstall

1. Download the Netinstall utility for your system and run it on your PC
2. Download the x86 CD image file from the download page: https://mikrotik.com/download
3. Set the PC BIOS boot option to PXE
4. Save changes and reboot
5. Proceed following the Netinstall utility steps
