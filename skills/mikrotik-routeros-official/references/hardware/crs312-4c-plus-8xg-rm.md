# CRS312-4C+8XG-RM

> CRS312-4C+8XG is an 8-port Gigabit Ethernet switch with four 10g Ethernet / SFP+, combo ports. Includes all basic functionality for a managed switch and more. See the CRS312-4C+8XG-RM product page for full...

![](./img/api_crs312-4c_8xg-rm.jpg)

## [CRS312-4C+8XG-RM](https://mikrotik.com/product/crs312_4c_8xg_rm)

CRS312-4C+8XG is an 8-port Gigabit Ethernet switch with four 10g Ethernet / SFP+, combo ports. Includes all basic functionality for a managed switch and more. See the [CRS312-4C+8XG-RM product page](https://mikrotik.com/product/crs312_4c_8xg_rm) for full specifications and brochures.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- The Installation of the equipment must comply with local and national electrical codes.
- This unit is intended to be installed in the rackmount. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware or to follow the correct procedures could result in a hazardous situation to people and damage to the system.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity or hot environments.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik devices must be professionally installed.

## Quickstart

- Connect with your PC to any Ethernet port;
- Connect the device to a power source;
- Configure the IP settings of your network card to 192.168.88.2/24;
- Use WebFig in a web browser or the "WinBox" configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Open `http://192.168.88.1` in a web browser to start setup. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device. Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

## Mounting

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Please attach rubber pegs on the bottom of the router if the desired placement is on the flat surface or use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown in the picture.
- Place the device in a rackmount enclosure and align with the holes so that the device fits conveniently.
- Tighten screws to secure it in place.
![](../img/worddavdcbcfbfbb5384f30180de01126c4ad1d.webp)

The IP rating scale for this device is IPX0. The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment. We recommend shielded Cat5/6 cables for our devices. *Mounting and configuration of this device should be done by a qualified person.*

## Configuration

Full documentation for both RouterOS and SwOS is available at [https://mt.lv/help](https://mt.lv/help). The device can be configured using **WebFig** in a web browser or the **WinBox** configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility.**

Open `http://192.168.88.1` in a web browser to start setup. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device. Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker).

The device is equipped with an RJ45 serial port, set by default to 115200 bit/s, 8 data bits, 1 stop bit, no parity. For recovery purposes, it is possible to reinstall the device from the network, see the [Reset button](#reset-button).

The Marvell Prestera switch chip features are described in the [Marvell Prestera switch chip features](/docs/bridging-and-switching/marvell-prestera-switch-chip-features) manual.

The device supports booting either RouterOS (for full routing and switching functionality) or SwOS (for switch-only operation). By default, the device boots into RouterOS, but you can switch to the other operating system as follows:

- From SwOS: go to the **System** menu and click the "**Boot RouterOS**" button at the bottom of the page.
- From RouterOS: open **System → RouterBOARD → Settings** and select **Boot OS**.

It is also possible to choose the operating system and configure other boot options using the serial console menu.

## Powering

The device accepts power from two alternative current inputs at range AC ⏦ 100-240 V. Dual power supplies for redundancy with IEC power connectors.
The power consumption under maximum load can reach 60 W.

## Specifications

| **Product Code** | CRS312‑4C+8XG‑RM |
| --- | --- |
| **CPU** | QCA9531, 650 MHz |
| **CPU Architecture** | MIPSBE |
| **CPU Core Count** | 1 |
| **Switch Chip Model** | 98DX8212 |
| **RAM** | 64 MB |
| **Storage** | 16 MB Flash |
| **10/100 Ethernet (RJ45)** | 1 |
| **1G/2.5G/5G/10G Ethernet (RJ45)** | 8 |
| **10G Combo (RJ45/SFP+) Ports** | 4 |
| **USB Type‑A Port** | 1 |
| **Serial Console (RJ45)** | 1 |
| **Operating System** | RouterOS v7 / SwOS (License 5) |
| **Operating Temperature** | ‑30 °C to +70 °C |
| **Case Dimensions** | 443 × 183 × 44 mm |

## Combo interface

The four combo interfaces each have two physical connectors of which the only one can be used at the same time. The ports will be automatically represented as combo 1-4 in RouterOS. It is possible to select which physical port will be used in the RouterOS software ethernet menu. If left to default "auto", and both F/T have cables plugged in, SFP will take priority. For example, if you have plugged an Ethernet cable into the 1T port and an SFP module in the 1F port, you will have to choose in RouterOS which one to use. Double click the respective combo interface in RouterOS GUI to see which socket is used.

## Reset button

- To reset the configuration, unplug the device from power, press and hold the Reset button, and release it when the USER (USR) LED starts flashing.
- To load the backup bootloader, press and hold the Reset button before applying power, then release it after three seconds.
- To initiate the Netinstall process (booting the device in BOOTP mode to reinstall RouterOS), press and hold the Reset button, power on the device, and wait for the USER (USR) LED to flash, then become stable. When the USR LED turns off, release the Reset button.

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

- Fastening set for rackmount case K-57.
- AC ⏦ EU/US power cord, D03+QT3 H05VV-F 3x0.75 mm2 1.83 m RoHS.
- Mounting kit 1U rackmount bracket white, 2 pcs.
Please visit the wiki pages for the MikroTik SFP module compatibility table: MikroTik wired interface compatibility.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.
