# CCR2004-16G-2S+

> This powerful and affordable router crushes all previous CCR models in single-core performance. 16x Gigabit Ethernet ports, USB, 2x10G SFP+ cages, active cooling and the best single-core performance per watt & best...

![](./img/api_ccr2004-16g-2s_.jpg)

## [CCR2004-16G-2S+](https://mikrotik.com/product/ccr2004_16g_2splus)

This powerful and affordable router crushes all previous CCR models in single-core performance. 16x Gigabit Ethernet ports, USB, 2x10G SFP+ cages, active cooling and the best single-core performance per watt & best overall performance per watt among all the CCR devices. See the [CCR2004-16G-2S+ product page](https://mikrotik.com/product/ccr2004_16g_2splus) for full specifications and brochures.

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

- Connect your PC to the **MGMT/BOOT** labeled port or the first Ethernet port;
- Connect the device to a power source;
- Configure the IP settings of your network card to `192.168.88.2/24`;
- Configuration should be made using **WebFig** in a web browser or the **WinBox** configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Open `192.168.88.1` in a web browser to start setup. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device. Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

## Powering

![](./img/image2021-7-28_15-49-48.webp)

The device has dual integrated power supply units AC **⏦** 100-240V with standard IEC compatible sockets with Maximum power consumption of 48 W.

## Specifications

- Product code CCR2004-16G-2S+
- CPU AL32400 1.7 GHz
- CPU architecture ARM 64bit
- CPU core count 4
- Size of RAM 4 GB
- RAM type DDR4
- Storage 128 MB, NAND
- Number of 1G Ethernet ports 16
- Number of 10G SFP+ ports 2
- Operating system RouterOS (License level 6)
- Switch chip model 88E6191X, 88E619X
- Dimensions 443 x 210 x 44 mm
- Operating temperature -20°C to +60°C

## Reset button

**Reset button**:

- Hold this button during boot time until the USER LED light starts flashing, release the button to reset RouterOS configuration.
- Hold the Reset button and power on your device (wait until the "USER" LED is blinking then stable "On", and when the "USER" LED is "Off" - release the Reset button) - the device is booting in BOOTP mode to reinstall RouterOS using [Netinstall](../../docs/getting-started/installation-and-upgrade/netinstall). **The MGMT/BOOT Ethernet port is used for the Netinstall process.** See RouterOS documentation about using the Netinstall recovery utility.

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Release the button before LED begins to flash, to only load backup RouterBOOT without resetting. This is useful for RouterBOOT debugging and recovery.

## Mounting

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

![](../img/worddavdcbcfbfbb5384f30180de01126c4ad1d.webp)

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown on the picture to the right;
- Place the device in rackmount enclosure and align with the holes so that the device fits conveniently;
- Tighten screws to secure it in place.
The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment. We recommend Cat6 cables for our devices.

## Included Parts

![](./img/image2021-7-28_15-45-35.webp)

- PLUG1-2_ EU/US power cord, JL3-JL38C (D03+QT3) H05VV-F 3x0.75mm2 1.83m
- SET1_ Fastening set K-57
- CASE3-4_ 1U rackmount bracket white

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.
