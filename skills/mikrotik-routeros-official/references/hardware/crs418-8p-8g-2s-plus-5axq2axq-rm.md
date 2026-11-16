# CRS418-8P-8G-2S+5axQ2axQ-RM

> The Wi-Fi version of CRS418... with our strongest 4x4 MIMO Wi-Fi 6! L3 HW offloading, quad-core 2.2 GHz ARM CPU, 16x Gigabit Ethernet ports + a Gigabit management port with a direct CPU line, 2x 10G SFP+ ports,...

![](./img/api_crs418-8p-8g-2s_5axq2axq-rm.jpg)

The Wi-Fi version of CRS418... with our strongest 4x4 MIMO Wi-Fi 6! L3 HW offloading, quad-core 2.2 GHz ARM CPU, 16x Gigabit Ethernet ports + a Gigabit management port with a direct CPU line, 2x 10G SFP+ ports, PoE-out. See the [CRS418-8P-8G-2S+5axQ2axQ-RM product page](https://mikrotik.com/product/crs418_8p_8g_2s_wifi) for full specifications and brochures.

## Safety Warnings

Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
Ultimate disposal of this product should be handled according to all national laws and regulations.
The Installation of the equipment must comply with local and national electrical codes.
This unit is intended to be installed in the rackmount. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware or to follow the correct procedures could result in a hazardous situation to people and damage to the system.
This product is intended to be installed indoors. Keep this product away from water, fire, humidity or hot environments.
Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
The socket-outlet shall be installed near the equipment and shall be easily accessible.
Read the installation instructions before connecting the system to the power source.
We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
It is the customer's responsibility to follow local country regulations. All MikroTik devices must be professionally installed.
This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures

## Quickstart

- Ensure your Internet Service Provider (ISP) allows hardware changes and automatically assigns an IP address;
- Connect the ISP cable to the Ethernet1 port;
- Connect the device to the power source;
- Connect to the device through any of the ports, excluding Ethernet1, or the wireless network "MikroTik-..." (ensure to check the wireless passwords on the sticker);
- Establish a connection using a mobile application. Alternatively, use WebFig in a web browser or the "WinBox" configuration tool at https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Start configuration within the chosen tool, using the default IP address 192.168.88.1. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device;
- Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the "QuickSet" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

## Mounting

The device is designed for indoor use and can be mounted in a rack enclosure using the provided rackmount brackets or placed on a desktop.

If installing the device in a rack, ensure there is enough space for the antennas and that they can be positioned freely without obstruction.For desktop placement, attach the rubber feet to the bottom of the router.

For rack installation, use a Phillips screwdriver to attach the rackmount ears on both sides of the device:

- Attach the rackmount ears and the rear support ears to both sides of the device and tighten the four screws to secure them, as shown in the picture.
![](../img/worddavea344d21c67b194482b683cafba1a738.webp)
- Place the device in the rackmount enclosure and align it with the mounting holes.
- Tighten the screws to secure the device in place.
The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
We recommend Cat6 cables for our devices.
Mounting and configuration of this device should be done by a qualified person.

## Powering

The unit is equipped with two power supplies, 250 W, which accepts 100-240 V ⏦ (~ 50/60 Hz 4.5 A max).
The maximum power consumption without attachments is 43 W, and under maximum load, it can reach 227 W.

## Configuration

Full documentation for RouterOS is available at: https://mt.lv/help You can configure the device using WebFig in a web browser or the "WinBox" configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility.**
**To start setup, open http://192.168.88.1 in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker).
The device is equipped with an RJ45 serial port, set by default to 115200 bit/s, 8 data bits, 1 stop bit, no parity. For recovery purposes, it is possible to reinstall the device from the network, see the Reset button.

Marvell Prestera switch chip features user manual

## Buttons

**Reset button**:

- Hold this button during boot time until the USER LED light starts flashing, release the button to reset RouterOS configuration.
- Hold the Reset button and power on your device (wait until the "USER" led is blinking then stable "On", and when the "USER" LED is "Off" - release the Reset button) - the device is booting in BOOTP mode to reinstall RouterOS using Netinstall. **The MGMT/BOOT Ethernet port is used for the Netinstall process.** See RouterOS documentation about using the Netinstall recovery utility.
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Release the button before LED begins to flash, to only load backup RouterBOOT without resetting. This is useful for RouterBOOT debugging and recovery.

## Extension slots and ports

- Product code: **CRS418-8P-8G-2S+RM**.
- Size of RAM: 1 GB.
- RAM type: DDR3.
- Storage: 128 MB, NAND.
- Number of 1G Ethernet ports: 17.
- Number of 10G SFP+ Ethernet ports: 2.
- Number of 1G Ethernet ports with PoE-out: 8.
- PoE-out ports: Ether9-Ether16, 802.3af/at, Total output power 150 W.
- 1x RJ45 console port (set at 115200bits/s, 8 data bits, 1 stop bit no parity).
- USB: 1 USB 3.0 type A.
- Switch chip model: 98DX226S.
- Wireless interface model: QCN-5024 (2.4 GHz), QCN-5054 (5 GHz), Wi-Fi 6.
- Wireless: 2.4 GHz 802.11b/g/n/ax quad-chain, 5 GHz 802.11a/n/ac/ax quad-chain.
- MIMO DL: 4x4.
- MIMO UL: 1x1 (5G SA MIMO UL 2x2).
- Dimensions: 443 x 156 x 44 mm.
- Operating system RouterOS: v7, License level 5.
- Operating temperature: -20°C to +70°C.
Please visit help pages for MikroTik SFP module compatibility and configuration table: MikroTik wired interface compatibility

## LED indicators

- PWR LED is lit when the router is powered on.
- USER LED indicates the device's state while powering it up into different modes, such as resetting the configuration or booting device for the Netinstall utility.
- The FAULT LED indicates a problem with any of the cooling fans.
- The triangle LEDs (top row) indicate PoE out status. Green LED indicates that the respective port uses low voltage, a red LED indicates high voltage. Flashing single green LED: problem to start a low voltage device. Flashing single red LED: problem with high voltage device.
- The SFP+ port green LEDs indicate individual SFP+ port activity.

## Accessories

Package includes the following accessories that come with the device:

![](./img/image-2025-11-17_16-19-9.webp)

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.
