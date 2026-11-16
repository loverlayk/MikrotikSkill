# CRS326-24G-2S+RM

> 24 Gigabit port switch with 2 x SFP+ cages in 1U rackmount case, Dual boot (RouterOS or SwOS). See the CRS326-24G-2S+RM product page for full specifications and brochures.

![](./img/api_crs326-24g-2s_rm.jpg)

## [CRS326-24G-2S+RM](https://mikrotik.com/product/CRS326-24G-2SplusRM)

24 Gigabit port switch with 2 x SFP+ cages in 1U rackmount case, Dual boot (RouterOS or SwOS). See the [CRS326-24G-2S+RM product page](https://mikrotik.com/product/CRS326-24G-2SplusRM) for full specifications and brochures.

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

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown in the picture.

![](../img/worddavea344d21c67b194482b683cafba1a738.webp)

- Place the device in a rackmount enclosure and align with the holes so that the device fits conveniently.
- Tighten screws to secure it in place.
The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
We recommend Cat6 cables for our devices.
Mounting and configuration of this device should be done by a qualified person.

## Powering

The device accepts power in the following ways:

- Ethernet port accepts passive PoE 10-30 V DC ⎓.
- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 10-30 V DC⎓.
The device will also work when both input sources are powered at the same time. It will work from the highest voltage source, and if that is removed, will switch to the other one. You can use it for power redundancy. Both power sources have to be within the supported voltage range.

The power consumption under maximum load can reach 24 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter;
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter;
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

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

| **Product Code** | CRS326-24G-2S+RM |
| --- | --- |
| **CPU** | 98DX3236, 800 MHz |
| **CPU Architecture** | ARM 32bit |
| **CPU Core Count** | 2 |
| **Switch Chip Model** | 98DX3236 |
| **RAM** | 512 MB |
| **Storage** | 16 MB Flash |
| **1G Ethernet (RJ45)** | 24 |
| **10G SFP+ Ports** | 2 |
| **Serial Console (RJ45)** | 1 |
| **Operating System** | RouterOS / SwOS (Dual boot) |
| **Operating Temperature** | -40 °C to +60 °C |
| **Case Dimensions** | 443 × 144 × 44 mm |

Please visit wiki pages for MikroTik SFP module compatibility table: MikroTik wired interface compatibility

## Reset button

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

Use Ethernet 1 port when connecting to **Netinstall**.

![](./img/image2020-2-24_13-33-13.webp)

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.
