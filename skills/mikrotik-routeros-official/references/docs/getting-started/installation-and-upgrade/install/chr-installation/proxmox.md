# CHR: Proxmox VE Installation

> This page provides an overview and detailed installation steps for deploying MikroTik Cloud Hosted Router (CHR) on Proxmox VE virtual environments, covering VM creation, image handling, and configuration methods.

# CHR: Proxmox VE Installation

## Overview

Cloud Hosted Router (CHR) is a MikroTik RouterOS edition designed to run on x86_64 virtualized environments. It provides full routing, firewall, VPN, and management functionality, making it suitable for both on-premise and cloud-based virtual infrastructure such as Proxmox VE.

Proxmox VE (KVM/QEMU) allows flexible deployment of CHR using raw or qcow2 disk images and provides multiple storage backends and network adapter options.

## Installation Steps

### Step 1: Create a Virtual Machine

- Create a new VM in Proxmox VE using the web interface.
- Assign CPU, memory, and network interfaces as required.
- Do not install an operating system (CHR disk will be attached manually).

### Step 2: Download and Extract CHR Image

Download the latest CHR image from the MikroTik download page: https://mikrotik.com/download to the Proxmox host:

```bash
wget https://download.mikrotik.com/routeros/7.21.4/chr-7.21.4.img.zip
```

:::warning
Replace the URL with the latest CHR version available on the MikroTik [download page](https://mikrotik.com/download).
:::

Unpack the image:

```bash
unzip chr-7.21.4.img.zip
```

This will produce a `.img` file used for installation.

### Step 3: Move the Image to VM Storage

Default Proxmox local storage location:

```bash
/var/lib/vz/images/<VM_ID>/
```

Create directory if needed:

```bash
mkdir -p /var/lib/vz/images/<VM_ID>
```

Move the image:

```bash
mv chr-7.21.4.img /var/lib/vz/images/<VM_ID>/
```

### Step 4: Convert Image to QCOW2

Convert the raw CHR image to qcow2 format:

```bash
qemu-img convert -f raw -O qcow2 /var/lib/vz/images/<VM_ID>/chr-7.21.4.img /var/lib/vz/images/<VM_ID>/vm-<VM_ID>-disk-1.qcow2
```

### Step 5: Attach Disk to VM

VM configuration file location:

```bash
/etc/pve/qemu-server/<VM_ID>.conf
```

Attach the disk manually through the VM configuration file or by using the Proxmox web interface.

:::tip
Use a test VM first to validate correct configuration syntax.
:::

## Alternative GUI-Based Method

1. Create a basic VM via Proxmox web interface.
2. Ensure storage is set to local storage.
3. Upload CHR image to: `/var/lib/vz/images/<VM_ID>/`
4. Convert image to qcow2:

```bash
qemu-img convert -f raw -O qcow2 chr.img vm-<VM_ID>-disk-1.qcow2
```

1. Attach disk via Proxmox GUI or `.conf` file.

## Automated Installation Script

CHR can also be deployed using a Bash script on the Proxmox host.

**What the script does:**

- Creates temp directory (/root/temp).
- Downloads CHR image.
- Extracts and converts it.
- Creates VM and attaches disk.

```bash
#!/bin/bash

version="nil"
vmID="nil"

echo "############## Start of Script ##############"

if [ ! -d /root/temp ]; then
    mkdir /root/temp
fi

read -p "Enter CHR version (e.g. 7.21.4): " version

cd /root/temp

wget https://download.mikrotik.com/routeros/$version/chr-$version.img.zip
unzip chr-$version.img.zip

read -p "Enter VM ID: " vmID

mkdir -p /var/lib/vz/images/$vmID

qemu-img convert -f raw -O qcow2 \
chr-$version.img \
/var/lib/vz/images/$vmID/vm-$vmID-disk-1.qcow2

qm create $vmID \
  --name chr-$version \
  --net0 virtio,bridge=vmbr0 \
  --bootdisk virtio0 \
  --ostype l26 \
  --memory 512 \
  --sockets 1 \
  --cores 1 \
  --virtio0 local:$vmID/vm-$vmID-disk-1.qcow2

echo "############## End of Script ##############"
```

### Utility Tip

Fix Windows line endings in scripts:

```bash
sed -i -e 's/\r$//' *.sh
```

## Supported Network and Disk Interfaces

### Proxmox VE (KVM/QEMU)

**Network adapters:**

- Virtio (paravirtual)
- E1000

**Disk controllers:**

- IDE
- SATA
- Virtio (paravirtual)
