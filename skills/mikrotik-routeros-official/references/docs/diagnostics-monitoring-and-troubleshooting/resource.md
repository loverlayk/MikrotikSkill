# Resource

> The Resource menu in RouterOS provides overview of system statistics including uptime, memory, disk usage, and hardware details like CPU model and frequency. It also offers submenus for detailed per-CPU usage, IRQ,...

# Resource

### General

**Sub-menu:** `/system/resource`

The general resource menu shows overall resource usage and router statistics like uptime, memory usage, disk usage, version, etc.

It also has several sub-menus for more detailed hardware statistics like CPU, IRQ, and Hardware.

```ros
[admin@MikroTik] > /system/resource/print 
                   uptime: 29s
                  version: 7.24rc2
               build-time: 2023-08-31 13:55:47
          minimum-version: 7.6
              free-memory: 94.2MiB
             total-memory: 224.0MiB
                      cpu: ARM
                cpu-count: 2
            cpu-frequency: 800MHz
                 cpu-load: 2%
           free-hdd-space: 93.5MiB
          total-hdd-space: 128.5MiB
  write-sect-since-reboot: 85
         write-sect-total: 222100
               bad-blocks: 0%
        architecture-name: arm
               board-name: hAP ax lite LTE6
                 platform: MikroTik

```

All properties are read-only

| Property | Description |
| :-- | :-- |
| **architecture-name** (*string*) | CPU architecture |
| **bad-blocks** (*percent*) | Shows percentage of bad blocks on the NAND. |
| **board-name** (*string*) | RouterBOARD model name |
| **build-time**(*string*) | Installed RouterOS version build-time |
| **cpu** (*string*) | CPU model that is on the board |
| **cpu-count** (*integer*) | Number of CPUs present on the system. Each core is a separate CPU, Intel HT is also a separate CPU. |
| **cpu-frequency** (*string*) | Current CPU frequency |
| **cpu-load** (*percent*) | Percentage of used CPU resources. Combines all CPUs. Per-core CPU usage can be seen in [CPU submenu](#cpu) |
| **minimum-version**(*string*) | Minimum RouterOS version (was 'factory-software') |
| **free-hdd-space** (*string*) | Free space on hard drive or NAND |
| **free-memory** (*string*) | The unused amount of RAM |
| **platform** (*string*) | Platform name |
| **total-hdd-space** (*string*) | Size of the hard drive or NAND |
| **total-memory** (*string*) | Amount of installed RAM |
| **uptime** (*time*) | Time interval passed since boot-up |
| **version** (*string*) | Installed RouterOS version number |
| **write-sect-since-reboot** (*integer*) | The number of sector writes in HDD or NAND since the router was last rebooted |
| **write-sect-total** (*integer*) | The number of sector writes in total |

### CPU

**Sub-menu:** `/system/resource/cpu`

This submenu shows per-cpu usage, as well as IRQ and Disk usage.

```ros
[admin@RB1100test] /system/resource/cpu> print 
CPU LOAD IRQ DISK 
0 5% 0% 0% 
[admin@RB1100test] /system/resource/cpu> 

```

## Properties

### Read-only properties

| Property | Description |
| :-- | :-- |
| **cpu** (*integer*) | Identification number of the CPU whose usage is shown. |
| **load** (*percent*) | CPU usage in percent |
| **irq** (*percent*) | IRQ usage in percent |
| **disk** (*percent*) | Disk usage in percent |

### IRQ

**Sub-menu:** `/system/resource/irq`

The menu shows all used IRQs on the router. It is possible to set up [IRQ load balancing](#irq) on multicore systems by assigning an IRQ to a specific core. IRQ assignments are done by hardware and cannot be changed from RouterOS. For example, if all Ethernets are assigned to one IRQ, then you have to deal with hardware: upgrade motherboard's BIOS, reassign IRQs manually in BIOS, if none of the above helps then change the hardware.

#### Properties

| Property | Description |
| :-- | :-- |
| **cpu** (*auto \| integer*; Default: ) | Specifies which CPU is assigned to the IRQ.auto - picks a CPU based on the number of interrupts. Uses NAPI to optimize interrupts. |

**Read-only properties**

| Property | Description |
| :-- | :-- |
| **active-cpu** (*integer*) | Shows active CPU in multicore systems. |
| **count** (*integer*) | The number of interrupts. On ethernet interfaces interrupt=packet. |
| **irq** (*integer*) | IRQ identification number |
| **users** (*string*) | Process assigned to IRQ |

### RPS

**Sub-menu:** `/system/resource/irq/rps`

Receive Packet Steering (RPS) is similar to Receive Side Scaling (RSS) in that it is used to direct packets to specific CPUs for processing. However, RPS is implemented at the software level, and helps to prevent the hardware queue of a single network interface card from becoming a bottleneck in network traffic.  
  
RPS is useful when packets require additional processing that uses a relatively large amount of CPU time, such as PPP tunnel termination, VPLS, or firewall processing. The CPU resources spent by RPS on classifying and forwarding packets to another CPU are then outweighed by the additional processing required. Unfortunately, RPS cannot always replace several lines in Ethernet drivers, as forwarding packets to another CPU is expensive in itself.
  
For network devices with multiple queues, there is typically no benefit to configuring both RPS and RSS, as RSS is configured to map a CPU to each receive queue by default. However, RPS may still be beneficial if there are fewer hardware queues than CPUs, depending on the traffic handled by the device.

#### Properties

| Property | Description |
| :-- | :-- |
| **disable***(number)* | Disable RPS for selected entries |
| **edit** *(number)* | Edit properties of an existing entry |
| **enable** *(number)* | Enable RPS for selected entries |
| **reset***(number)* | Reset properties to default values |

### **Hardware**

Shows detected hardware devices connected via PCI, USB, or SCSI buses.

Flags:

```ros
I - inactive   Device is present but not active
```

**Sub-menu:** `/system/resource/hardware`

#### Properties

| Property | Description |
| :-- | :-- |
| **location** (*string*) | Device location in system topology |
| **parent** (*enum*) | Parent bus or controller |
| **type** (usb\|pci\|scsi\|serial) | Bus type of the device |
| **vendor** (*string*) | Device vendor name |
| **name** (*string*) | Device name or model |
| **serial-number** (*string*) | Device serial number |
| **vendor-id**(string) | Vendor identifier (VID) |
| **device-id** (string) | Device identifier (PID / Device ID) |
| **speed** (*string*) | Negotiated device speed |
| **ports***(number)* | Number of ports provided by the device |
| **usb-version** (*string*) | Supported USB version |
| **owner** (*string*) | Subsystem or driver owning the device |
| **device-path** (*string*) | Device path from root bus to endpoint |

**Read-only properties**

| Property | Description |
| :-- | :-- |
| **category** (*string*) | Device category |
| **irq** (*number*) | Assigned interrupt number |

### Device authorization

Controls the authorization state of a hardware device.

**Sub-menu:** `/system/resource/hardware/authorize`

#### Properties

| Property | Description |
| :-- | :-- |
| **allow** (*yes\|no*) | Enable or disable USB device authorization |

### Global USB subsystem settings

**Sub-menu:** `/system/resource/hardware/usb-settings`

#### Properties

| Property | Description |
| :-- | :-- |
| **authorization** (*yes\|no*) | Enable or disable USB device authorization |
| **numbers** (*number*) |  |

**Sub-menu:** `/system/resource/hardware/usb-power-reset`

#### Properties

| Property | Description |
| :-- | :-- |
| **duration** (time) | Power-off duration before re-enabling USB |
| **bus**(number) | USB bus number |
| **slot**(number) | USB port/slot number on the bus |
