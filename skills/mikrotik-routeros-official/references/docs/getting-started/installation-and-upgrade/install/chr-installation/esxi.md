# CHR: VMWare ESXi Installation

> This page documents the installation and configuration of MikroTik CHR on VMware ESXi, covering supported network interfaces (vmxnet3, E1000) and disk controllers (IDE, VMware Paravirtual SCSI), along with...

# CHR: VMWare ESXi Installation

## Supported Network and Disk Interfaces

### VMware ESXi

**Network adapters:**

- vmxnet3
- E1000

**Disk controller:**

- IDE
- VMware Paravirtual SCSI
- LSI Logic SAS
- LSI Logic Parallel

#### ESXi

Enable Promiscuous mode in the port group or virtual switch that you will use for the VM.

**ESXi documentation:**

- https://kb.vmware.com/kb/1004099

### Running on VMware ESXi

#### Changing MTU

VMware ESXi supports MTU values up to 9000 bytes. To take advantage of jumbo frames, adjust your ESXi installation to allow a higher MTU.

**Important:** A virtual Ethernet interface added **after** the MTU change will properly support jumbo frames. However, interfaces added **before** the MTU change will be limited to the original MTU value. If you have interfaces configured before changing the MTU, you must remove and re-add them to the virtual guest.

**Example:** Two interfaces added to the ESXi guest show different MTU values based on when they were added:

```
[admin@chr-vm] > interface ethernet print 
Flags: X - disabled, R - running, S - slave 
 #    NAME           MTU MAC-ADDRESS       ARP       
 0 R  ether1        9000 00:0C:29:35:37:5C enabled   
 1 R  ether2        1500 00:0C:29:35:37:66 enabled
```
