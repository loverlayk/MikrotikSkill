# CRS518-16XS-2XQ-RM

> A 100 Gigabit switch for enterprise networks and data centers. Hot-swappable parts and insane port density with 1.2 Tbps switching capacity! See the CRS518-16XS-2XQ-RM product page for full specifications and brochures.

![](./img/api_crs518-16xs-2xq-rm.jpg)

A 100 Gigabit switch for enterprise networks and data centers. Hot-swappable parts and insane port density with 1.2 Tbps switching capacity! See the [CRS518-16XS-2XQ-RM product page](https://mikrotik.com/product/crs518_16xs_2xq) for full specifications and brochures.

### CRS518-16XS-2XQ

## Safety Warnings

Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
Ultimate disposal of this product should be handled according to all national laws and regulations.
The Installation of the equipment must comply with local and national electrical codes.
This unit is intended to be installed in the rackmount. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
This product is intended to be installed indoors. Keep this product away from water, fire, humidity, or hot environments.
Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
Read the installation instructions before connecting the system to the power source.
We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik devices must be professionally installed.

## Quickstart

- Connect with your PC to any Ethernet port;
- Connect the device to a power source;
- Configure the IP settings of your network card to 192.168.88.2/24;
- Use WebFig in a web browser or the "WinBox" configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Open http://192.168.88.1 in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

## Mounting

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Please attach rubber pegs on the bottom of the router if the desired placement is on the flat surface or use a Phillips screwdriver to attach rackmount ears on both sides of the device if the designated use is for rackmount enclosure:

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown in the picture.
- Place the device in a rackmount enclosure and align with the holes so that the device fits conveniently.
- Tighten screws to secure it in place.
![](../img/worddavdcbcfbfbb5384f30180de01126c4ad1d.webp)

The IP rating scale for this device is IPX0. The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment. We recommend shielded Cat5/6 cables for our devices. The mounting*and configuration of this device should be done by a qualified person.*

## Configuration

Full documentation for RouterOS is available at: https://mt.lv/help You can configure the device using WebFig in a web browser or the "WinBox" configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility.**
**To start setup, open http://192.168.88.1 in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker).
The device is equipped with an RJ45 serial port, set by default to 115200 bit/s, 8 data bits, 1 stop bit, no parity. For recovery purposes, it is possible to reinstall the device from the network, see the Reset button.

Marvell Prestera switch chip features user manual

## Powering

- A number of AC inputs 2.
- Nominal voltage 12 V.
- Nominal current 12.5 A.
- AC input range 100-240 V.
- Max power consumption (without attachments) 45 W.
- Max power consumption 77 W.

## Extension slots and ports

- Product code CRS518-16XS-2XQ-RM.
- Switch chip model 98DX8525.
- CPU QCA9531 650 MHz.
- CPU architecture MIPSBE.
- CPU core count 1.
- Size of RAM 64 MB.
- RAM type DDR2.
- Storage 16 MB, Flash.
- A number of 100M Ethernet ports 1.
- A number of 25G SFP28 ports 16.
- A number of 100G QSFP28 ports 2.
- USB port 1 (type A).
- Operating system Only v7 RouterOS.
- Dimensions 443 x 265 x 44.5 mm.
- Operating temperature -40°C to +70°C.
- 100G QSFP28 supported speeds: 1x 100G; 2x 50G; 1x 50G; 1x 40G; 4x 25G; 4x 10G; 4x 1G. Not supported: 2x 40G
- 25G SFP28 supported speeds: 1x 25G; 1x 10G; 1x 2.5G; 1x 1G. Not supported: 1x 5G

## Reset button

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

![](./img/image-2026-2-23_16-8-26.webp)

Please visit help pages for MikroTik SFP module compatibility and configuration table: MikroTik wired interface compatibility

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.
