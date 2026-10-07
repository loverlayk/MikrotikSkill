# CHR: Hetzner Cloud Installation

> This page provides an overview for deploying MikroTik RouterOS Cloud Hosted Router (CHR) on Hetzner Cloud, detailing the installation process including server creation, rescue system activation, CHR image deployment...

# CHR: Hetzner Cloud Installation

## Overview

**[Hetzner Cloud](https://www.hetzner.com/cloud)** is a cloud computing platform that provides scalable virtual machine infrastructure and a range of pre-configured Linux distributions. For users requiring advanced networking features, Hetzner Cloud is also a suitable platform for deploying **RouterOS Cloud Hosted Router (CHR)**.

Cloud Hosted Router (CHR) is a MikroTik RouterOS edition designed to run in x86_64 virtualized environments. It provides the same core routing, firewall, VPN, and management features as MikroTik hardware devices, making it suitable for cloud-based networking, VPN services, and general network management.

When deployed on Hetzner Cloud, CHR benefits from scalable virtual infrastructure while maintaining full RouterOS functionality, allowing users to build flexible and powerful network solutions.

## Create a CHR Virtual Machine

1. **Create a Hetzner Cloud Server**  
   Start creating a new server on Hetzner Cloud. Any of the available server options will work.
2. **Activate Rescue System**
   - In the Hetzner Cloud admin interface, activate the **Enable Rescue** system by selecting **ENABLE RESCUE & POWER CYCLE**.
   - Choose `linux64` as the Rescue OS.
   - The system will display a username and password. Use these credentials to log into the rescue system via SSH.
3. **Install Cloud Hosted Router (CHR)**
   - After you log in to the rescue system, download the CHR **RAW** disk image and write it over the system disk of the cloud server with the following command:

   ```bash
   curl -L https://download.mikrotik.com/routeros/7.21.4/chr-7.21.4.img.zip | funzip | dd of=/dev/sda bs=1M
   ```

   >`/dev/sda` Device name may vary depending on the cloud provider configuration.

:::warning
Replace the URL with the link to the latest CHR version available on the MikroTik [download page](https://mikrotik.com/download).
:::

## Reboot the Server

After the installation is complete, reboot the server by issuing the `reboot` command.
:::warning
It is crucial to [secure your RouterOS](../../../securing-your-router.md) installation immediately!
:::

Make sure to keep your RouterOS updated and follow best security practices to maintain the safety and performance of your server.
