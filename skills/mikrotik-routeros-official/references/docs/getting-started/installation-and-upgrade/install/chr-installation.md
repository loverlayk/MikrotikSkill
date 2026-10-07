# CHR: Installation

> This page provides an overview of installing and configuring Cloud Hosted Router (CHR) on virtual environments, covering system requirements, RAM calculations, disk image formats, download instructions, VM setup, and...

# CHR: Installation

## Overview and System Requirements

Cloud Hosted Router (CHR) is a virtualized edition of RouterOS designed to run on x86_64 virtual environments. It provides the same core routing, firewall, VPN, and management features available on MikroTik hardware devices.

## Host System Requirements

- **CPU**: 64-bit processor with virtualization support
- **RAM**: 256 MB or more
- **Disk**: 128 MB or more

## Capacity Limits

### RouterOS Version 6

- Maximum CHR virtual hard drive size: 16 GB

### RouterOS Version 7

- Maximum RAM and disk space are limited by the Linux kernel 5.6.3 and depend on the specific hardware.

## Calculating Minimum RAM Requirements

The minimum required RAM depends on your CPU count and interface count. Use the appropriate formula below to calculate an approximate value:

- **RouterOS v6**:
  
  `RAM = 128 + [ 8 × (CPU_COUNT) × (INTERFACE_COUNT - 1) ]`

- **RouterOS v7**:
  
  `RAM = 512 + [ 8 × (CPU_COUNT) × (INTERFACE_COUNT - 1) ]`

**Recommendation**: For CHR instances, allocate at least 1024 MiB of RAM.

## Software Requirements

- **Package version**: RouterOS v6.34 or newer

## Available Disk Image Formats

- **RAW disk image**: `.img` file
- **VirtualBox disk image**: `.vdi` file
- **VMware disk image**: `.vmdk` file
- **Hyper-V disk image**: `.vhdx` file
- **OVA appliance**: `.ova` file

:::warning
These are disk images only and must be attached to a virtual machine.
:::

## Download the CHR Image

1. Go to the [MikroTik download page](https://mikrotik.com/download/chr) Cloud Hosted Router section.
2. Select the image format for your platform.
3. Download the file.

## Create and Configure a Virtual Machine

1. Create a new VM in your hypervisor.
2. Attach the CHR disk image as the system disk.
3. Boot the VM.

### Virtual Network Adapters

:::info
**Fast Path Support**

- RouterOS v7: Fast Path is supported with **vmxnet3** and **virtio-net** interfaces.
- RouterOS v6: Fast Path is not supported.

:::

## Access CHR

- Username: `admin`
- Password: none (you should set a strong password immediately after first login)

After first boot, CHR runs on a Free license by default. To activate a trial or upgrade, use `/system/license/renew`.

## Platform-specific guides

### Supported Virtualization Platforms

- [VMware ESXi](./esxi.md)
- VMware Fusion
- [Proxmox VE (KVM/QEMU)](./proxmox.md)
- [Hyper-V](./hyperv.md)
- [VirtualBox](./virtualbox.md)
- Xen Server

:::warning
CHR cannot run on the **bhyve** hypervisor. CHR does not support para-virtualized platforms.
:::

> **Note:** Only Generation 1 virtual machines are supported when using Hyper-V.

> **Important:** Paravirtualization is not supported on any hypervisor.

### Supported Cloud Platforms

- Amazon Web Services (AWS)
- Google Cloud Platform (GCP)
- [Hetzner Cloud](./hetzner.md)
- Linode
- Microsoft Azure
- [Vultr](./vultr.md)
