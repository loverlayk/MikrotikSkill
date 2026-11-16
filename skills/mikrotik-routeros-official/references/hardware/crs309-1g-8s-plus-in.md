# CRS309-1G-8S+IN

> This device is a network switch with eight SFP+ ports and one-gigabit port. It is already configured, with all ports switched together. See the CRS309-1G-8S+IN product page for full specifications and brochures.

![](./img/api_crs309-1g-8s_in.jpg)

## [CRS309-1G-8S+IN](https://mikrotik.com/product/crs309_1g_8s_in)

 This device is a network switch with eight SFP+ ports and one-gigabit port. It is already configured, with all ports switched together. See the [CRS309-1G-8S+IN product page](https://mikrotik.com/product/crs309_1g_8s_in) for full specifications and brochures.

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

- Mount the unit or place it on a flat surface, see [Mounting](#mounting);
- Choose your powering solution, see [Powering](#powering);
- Connect your PC to any Ethernet port;
- Connect the device to a power source;
- Configure the IP settings of your network card to 192.168.88.2/24;
- Configuration should be made using **WebFig** in a web browser or the **WinBox** configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Open `http://192.168.88.1` in a web browser to start setup. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device. Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

## Mounting

![](../img/worddavdcbcfbfbb5384f30180de01126c4ad1d.webp)

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Please attach rubber pegs on the bottom of the router if the desired placement is on the flat surface or use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure.

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown on the picture to the right.
- Place the device in a rackmount enclosure and align with the holes so that the device fits conveniently.
- Tighten screws to secure it in place.
The IP rating scale for this device is IPX0. The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
We recommend shielded Cat5/6 cables for our devices.
*Mounting and configuration of this device should be done by a qualified person.*

## Powering

The device accepts 12-57 V DC ⎓ from the direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts. The Ethernet port 1 accepts 802.3af/at and passive PoE power input (18-57 V DC).
The power consumption of this device under maximum load is up to 23 W. It is possible to connect both power inputs at the same time and they will work in fail-over mode (input with higher voltage will work as the main source).
When using 802.3af/at to power this device, we recommend not using grounding for best compatibility.

## Configuration

Full documentation for both RouterOS and SwOS is available at [https://mt.lv/help](https://mt.lv/help). The device can be configured using **WebFig** in a web browser or the **WinBox** configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility.**

Open `http://192.168.88.1` in a web browser to start setup. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device. Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker).

The device is equipped with an RS-232 serial port, set by default to 115200 bit/s, 8 data bits, 1 stop bit, no parity. For recovery purposes, it is possible to reinstall the device from the network, see the [Reset button](#reset-button).

The Marvell Prestera switch chip features are described in the [Marvell Prestera switch chip features](/docs/bridging-and-switching/marvell-prestera-switch-chip-features) manual.

The device supports booting either RouterOS (for full routing and switching functionality) or SwOS (for switch-only operation). By default, the device boots into RouterOS, but you can switch to the other operating system as follows:

- From SwOS: go to the **System** menu and click the "**Boot RouterOS**" button at the bottom of the page.
- From RouterOS: open **System → RouterBOARD → Settings** and select **Boot OS**.

It is also possible to choose the operating system and configure other boot options using the serial console menu.

## Reset button

- To reset the configuration, unplug the device from power, press and hold the Reset button, and release it when the USER (USR) LED starts flashing.
- To load the backup bootloader, press and hold the Reset button before applying power, then release it after three seconds.
- To initiate the Netinstall process (booting the device in BOOTP mode to reinstall RouterOS), press and hold the Reset button, power on the device, and wait for the USER (USR) LED to flash, then become stable. When the USR LED turns off, release the Reset button.

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## LED indicators

- The power LED is lit when the router is powered from the DC jack or PoE.
- The user LED can be configured from RouterOS.
- The port LEDs indicate the individual Ethernet and SFP port activity.

## Specifications

| **Product Code** | CRS309‑1G‑8S+IN |
| --- | --- |
| **CPU** | 98DX8208, 800 MHz |
| **CPU Architecture** | ARM 32bit |
| **CPU Core Count** | 2 |
| **Switch Chip Model** | 98DX8208 |
| **RAM** | 512 MB |
| **Storage** | 16 MB Flash |
| **1G Ethernet (RJ45)** | 1 |
| **10G SFP+ Ports** | 8 |
| **Operating System** | RouterOS / SwOS (Dual boot) |
| **Operating Temperature** | ‑40 °C to +70 °C |
| **Case Dimensions** | 272 × 191 × 44 mm |

## Accessories

Package includes the following accessories that come with the device:

![](../img/image2020-2-24_14-15-21.webp)

See the [MikroTik wired interface compatibility](/docs/wired-connections/mikrotik-wired-interface-compatibility) table for supported SFP modules.

## Operating system support

The device supports dual boot with SwOS version 2.9 and later, as well as RouterOS version 7 or later. The specific factory-installed RouterOS version is indicated in the RouterOS menu under `/system resource`. Other operating systems have not been tested and are not officially supported.
