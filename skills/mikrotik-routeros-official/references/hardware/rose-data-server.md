# ROSE Data Server

> RDS is a high-performance, all-in-one storage, 100G networking, and container platform designed for enterprise environments. Featuring 20 U.2 storage slots and a special RouterOS Edition for Storage & Compute (ROSE)....

![](./img/api_rds2216-2xg-4s_4xs-2xq.jpg)

## [ROSE Data Server](https://mikrotik.com/product/rds2216) (RDS2216-2XG-4S+4XS-2XQ)

RDS is a high-performance, all-in-one storage, 100G networking, and container platform designed for enterprise environments. Featuring 20 U.2 storage slots and a special RouterOS Edition for Storage & Compute (ROSE). See the [ROSE Data Server product page](https://mikrotik.com/product/rds2216) for full specifications and brochures.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- The Installation of the equipment must comply with local and national electrical codes.
- This unit is intended to be installed in the rackmount. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity or hot environments.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- The socket-outlet shall be installed near the equipment and shall be easily accessible.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik devices must be professionally installed.

## Quickstart

Set up RouterOS before connecting disks:

- Connect your PC to the **MGMT/BOOT** labeled port or the first Ethernet port;
- Connect the device to a power source;
- Configure the IP settings of your network card to `192.168.88.2/24`;
- Configuration should be made using **WebFig** in a web browser or the **WinBox** configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Open `http://192.168.88.1` in a web browser to start setup. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device. Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- Set up your router password.

## Install disks

To install disks:

1. Open the tray by pressing the button on the right side and pulling it out.

   

   ![](./img/tray_disasembly_arrow.webp)

   ![](./img/tray_disasembly_2_arrow.webp)

   ![](./img/tray_close1_arrow.webp)

   ![](./img/tray_open3_arrow.webp)

   

2. Mount the disk inside the bracket (optionally securing it with screws).

   

   ![](./img/disc_assey4.webp)

   ![](./img/disc_assey_bottom1.webp)

   

3. Insert the tray back into its slot, pushing forward until it locks.

   

   ![](./img/disk_assey1_arrow.webp)

   ![](./img/disk_assey2_arrow.webp)

   ![](./img/disk_assey3_outlines_arrows.webp)

   ![](./img/disk_assey1_outlines_arrows.webp)

   

4. Disk trays are numbered from the upper left (starting at 1) to the last tray at the bottom right.

   

   ![](./img/rds_3_stickers.webp)

   

[Download the tray sticker set (PDF)](./img/rds-tray-sticker-set.pdf) to label the disk trays.

:::warning
Forced removal is possible on the RDS2216-2XG-4S+4XS-2XQ, but use `/disk/eject` before physically removing any drives. The U.2 drive trays are hot-swappable.
:::

## Mounting

The device is designed for indoor use and can be either mounted in a rack using the provided rack mount ears or placed on a desktop. The included rack mount ear set is recommended for racks up to 600 mm deep. For rackmount installation, follow these steps using a Phillips screwdriver:

1. Attach the rackmount ears to the front sides of the device.

   ![](./img/04_r1_left_1.webp)

   ![](./img/05_r1_left_1_assey.webp)

   ![](./img/06_r1_right_1_assey.webp)

   ![](./img/04_r1_right_1.webp)

2. Attach the small rear rackmount support ears to both sides of the device.

   ![](../img/02_r1_left_2.webp)

   ![](../img/03_r1_left_2_assey.webp)

   ![](./img/03_r1_right_2.webp)

   ![](./img/05_r1_right_2_assey.webp)

3. Attach the long rear rackmount support ears to the rack's rear side.

   ![](../img/gdss_assey_r1_3.webp)

4. Install the device in the rack, ensuring that the case support ears are securely fixed to the long support ears.

   ![](./img/06_r1_in_rack_4.webp)

   ![](./img/07_r1_in_rack_3.webp)

   ![](./img/08_r1_in_rack_2.webp)

   ![](./img/09_r1_in_rack_1.webp)

   ![](./img/gdss_assey_r1_2.webp)

   ![](./img/gdss_assey_r1.webp)

Place the device in a dry and ventilated environment. The device has an IP20 rating.

## Configuration

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting with the [RouterOS documentation](https://mt.lv/help) to get accustomed to the possibilities. In case an IP connection is not available, the **WinBox** tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side. For recovery purposes, it is possible to boot the device from the network, see the [Reset button](#buttons-and-jumpers).

The device is equipped with an RJ45 serial console port, set by default to 115200 bit/s, 8 data bits, 1 stop bit, no parity.

## Powering

The unit is equipped with two hot-swap IEC type AC power supplies, 550 W, which accept 100-240 V ⏦ (~50/60 Hz, 7 A max).

The maximum power consumption without attachments is 105 W, and under maximum load, it can reach 286 W.

## Extension slots and ports

The device has two M.2 slots with SATA3 connections. Recommended are SATA3 M.2 2280 mm B+M key SSD disks with no capacity limitations.

The SFP ports support the following speeds:

- 100G QSFP28 supported speeds: 1x 100G; 1x 40G; 4x 25G; 4x 10G; 4x 1G. Not supported: 2x 50G; 1x 50G; 2x 40G.
- 25G SFP28 supported speeds: 1x 25G; 1x 10G; 1x 2.5G; 1x 1G. Not supported: 1x 5G.

See the [MikroTik wired interface compatibility](../../docs/wired-connections/mikrotik-wired-interface-compatibility) table for supported SFP modules.

## Specifications

| Parameter | Specification |
| --- | --- |
| **Product code** | RDS2216-2XG-4S+4XS-2XQ |
| **Architecture** | ARM 64bit |
| **CPU** | AL73400, 2000 MHz |
| **CPU core count** | 16 |
| **CPU threads count** | 16 |
| **Switch chip model** | 98DX4310 |
| **Switch connection to CPU** | 4x 25 Gbps |
| **Size of RAM** | 32 GB DDR4 |
| **Storage** | 32 MB flash, 128 MB NAND |
| **M.2 slots** | 2 (SATA3) |
| **2.5" disk trays** | 20 (U.2, maximum height 7 mm) |
| **10/100/1000 Ethernet ports** | 1 |
| **1G/2.5G/5G/10G Ethernet ports** | 2 |
| **10G SFP+ ports** | 4 |
| **25G SFP28 ports** | 4 |
| **100G QSFP28 ports** | 2 |
| **Serial console port** | RJ45 |
| **USB ports** | 2 (USB 3.0 Type A and USB 2.0 Type A) |
| **Max USB current** | 1 A |
| **USB Power Reset** | Yes |
| **Number of AC inputs** | 2 |
| **AC input range** | 100-240 V |
| **AC frequency** | 50-60 Hz |
| **Max power consumption** | 286 W |
| **Max power consumption without attachments** | 105 W |
| **Cooling** | 10 fans |
| **Dimensions** | 476 x 443 x 44 mm |
| **Operating temperature** | -20°C to +50°C |
| **Operating system** | RouterOS v7 (Special ROSE edition) |
| **RouterOS license** | 6 |
| **MTBF** | Approximately 200,000 hours at 25 °C |
| **CPU temperature monitor** | Yes |
| **PCB temperature monitor** | Yes |
| **Voltage monitor** | Yes |
| **Mode button** | Yes |
| **Certification** | CE, EAC, ROHS |
| **IP rating** | IP20 |

For more information about this product, specification and pictures please visit our web page: https://mikrotik.com/product/rds2216

## Buttons and jumpers

**Reset button**:

- Hold this button during boot time until the USER LED light starts flashing, release the button to reset RouterOS configuration.
- Hold the Reset button and power on your device (wait until the "USER" LED is blinking then stable "On", and when the "USER" LED is "Off" - release the Reset button) - the device is booting in BOOTP mode to reinstall RouterOS using [Netinstall](../../docs/getting-started/installation-and-upgrade/netinstall). **The MGMT/BOOT Ethernet port is used for the Netinstall process.** See RouterOS documentation about using the Netinstall recovery utility.

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Release the button before LED begins to flash, to only load backup RouterBOOT without resetting. This is useful for RouterBOOT debugging and recovery.

The Mode button is not functional by default but can be assigned any script in the menu `/system routerboard mode-button`.

## LEDs

### Back panel

- The PWR1/2 LED lights up when the router is powered on and connected to an appropriate power unit.
- The USER LED indicates the device's state during different boot modes, such as resetting the configuration or booting the device for the Netinstall utility.
- The FAULT LED lights up if there is an issue with any of the cooling fans.
- The square orange and green Ethernet port LEDs indicate individual 10G Ethernet port activity.
- The triangle 25G SFP28 and SFP+ port green LEDs indicate individual 25G SFP28 and SFP+ port activity.
- The circled 100G QSFP28 port green LEDs indicate individual lane activity for the 100G QSFP28 ports.

### Front panel

- The USER LED indicates the device's state during different boot modes, such as resetting the configuration or booting the device for the Netinstall utility.
- The FAULT LED lights up if there is an issue with any of the cooling fans.
- The POWER LED turns on when the router is powered up.
- The 2.5" disk tray LEDs (green and blue) indicate whether a disk is installed in the corresponding tray.

## Accessories

The package includes the following accessories that come with the device:

- IEC power cord, 2 pcs.
- Rackmount ear (ROSE).
- Small rear support ears (ROSE).
- Long rear rackmount support ears (ROSE).
- K-90 fastening set.

![](./img/rds-included-parts.png)

:::warning
The included rack mount ear set is recommended for racks up to 600 mm deep.
:::

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Safety notice

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.
