# CRS317-1G-16S+RM

> Smart Switch, 1 x Gigabit LAN, 16 x SFP+ cages, Dual Core 800MHz CPU, 1GB RAM, 1U rackmount passive cooling case, Dual Power Supplies. See the CRS317-1G-16S+RM product page for full specifications and brochures.

![](./img/api_crs317-1g-16s_rm.jpg)

## [CRS317-1G-16S+RM](https://mikrotik.com/product/crs317_1g_16s_rm)

Smart Switch, 1 x Gigabit LAN, 16 x SFP+ cages, Dual Core 800MHz CPU, 1GB RAM, 1U rackmount passive cooling case, Dual Power Supplies. See the [CRS317-1G-16S+RM product page](https://mikrotik.com/product/crs317_1g_16s_rm) for full specifications and brochures.

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
- Place the device in the rackmount enclosure and align with the holes so that the device fits conveniently.
![](../img/worddavea344d21c67b194482b683cafba1a738.webp)
- Tighten screws to secure it in place.

The IP rating scale for this device is IP0. The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
We recommend Cat6 cables for our devices.
The mounting and configuration of this device should be done by a qualified person.

## Powering

The device accepts powering through two IEC C14 standard connectors and supports both AC 110/240 V ⏦. Only one PSU is active at the time, the second one is used for redundancy.
The PoE injector is not included. The power consumption of this device under maximum load is up to 44W.

The device is fitted with passive cooling heatsinks and under normal load will operate silently, but in emergencies, two redundant fans will automatically switch on to keep the device cool, if ambient temperatures are above normal. The device has been tested to operate in ambient temperatures from -20 ℃ to +60 ℃.

## Configuration

Full documentation for both RouterOS and SwOS is available at [https://mt.lv/help](https://mt.lv/help). The device can be configured using **WebFig** in a web browser or the **WinBox** configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility.**

Open `http://192.168.88.1` in a web browser to start setup. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device. Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker).

The device is equipped with an RJ45 serial port, set by default to 115200 bit/s, 8 data bits, 1 stop bit, no parity. For recovery purposes, it is possible to reinstall the device from the network, see the [Reset button](#reset-button).

The Marvell Prestera switch chip features are described in the [Marvell Prestera switch chip features](/docs/bridging-and-switching/marvell-prestera-switch-chip-features) manual.

The device supports booting either RouterOS (for full routing and switching functionality) or SwOS (for switch-only operation). By default, the device boots into RouterOS, but you can switch to the other operating system as follows:

- From SwOS: go to the **System** menu and click the "**Boot RouterOS**" button at the bottom of the page.
- From RouterOS: open **System → RouterBOARD → Settings** and select **Boot OS**.

It is also possible to choose the operating system and configure other boot options using the serial console menu.

## Specifications

| **Product Code** | CRS317‑1G‑16S+RM |
| --- | --- |
| **CPU** | 98DX8216, 800 MHz |
| **CPU Architecture** | ARM 32bit |
| **CPU Core Count** | 2 |
| **Switch Chip Model** | 98DX8216 |
| **RAM** | 1 GB |
| **Storage** | 16 MB Flash |
| **1G Ethernet (RJ45)** | 1 |
| **10G SFP+ Ports** | 16 |
| **Serial Console (RJ45)** | 1 |
| **Operating System** | RouterOS (license level 6) / SwOS (dual boot) |
| **Operating Temperature** | ‑20 °C to +60 °C |
| **Case Dimensions** | 443 × 224 × 44 mm |

## Reset button

- To reset the configuration, unplug the device from power, press and hold the Reset button, and release it when the USER (USR) LED starts flashing.
- To load the backup bootloader, press and hold the Reset button before applying power, then release it after three seconds.
- To initiate the Netinstall process (booting the device in BOOTP mode to reinstall RouterOS), press and hold the Reset button, power on the device, and wait for the USER (USR) LED to flash, then become stable. When the USR LED turns off, release the Reset button.

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## SwOS Reset and Reinstall

CRS317-1G-16S+ has built-in backup SwOS firmware which can be loaded in case standard firmware breaks or upgrade fails:

- Holding the Reset button for a few seconds while CRS317-1G-16S+ is booting resets the configuration and loads the backup SwOS firmware.
- After loading the backup SwOS firmware, it is possible to connect to `192.168.88.1` using a web browser and install new SwOS firmware.

## Accessories

Package includes the following accessories that come with the device:

![](./img/image2020-2-24_14-33-13.webp)

Please visit the wiki pages for the MikroTik SFP module compatibility table: MikroTik wired interface compatibility.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.
