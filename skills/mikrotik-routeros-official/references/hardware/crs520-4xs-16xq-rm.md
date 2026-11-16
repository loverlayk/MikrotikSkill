# CRS520-4XS-16XQ-RM

> An ultra-fast enterprise switch with extra processing power due to the CCR series CPU & the best price per 100 Gigabit port on the market! See the CRS520-4XS-16XQ-RM product page for full specifications and brochures.

![](./img/api_crs520-4xs-16xq-rm.jpg)

An ultra-fast enterprise switch with extra processing power due to the CCR series CPU & the best price per 100 Gigabit port on the market! See the [CRS520-4XS-16XQ-RM product page](https://mikrotik.com/product/crs520_4xs_16xq_rm) for full specifications and brochures.

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

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Please attach rubber pegs on the bottom of the router if the desired placement is on the flat surface or use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

- Attach rackmount ears and the rear support ears to both sides of the device and tighten four screws to secure them in place, as shown in the picture.
![](../img/worddavea344d21c67b194482b683cafba1a738.webp)
- Place the device in the rackmount enclosure and align with the holes so that the device fits conveniently.
- Tighten screws to secure it in place.
The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
We recommend Cat6 cables for our devices.
Mounting and configuration of this device should be done by a qualified person.

## Powering

The unit is equipped with two Hot Swap IEC type AC power supply, 150W, which accepts 100-240 V ⏦ (~ 50/60 Hz 12.5 A max).
The maximum power consumption without attachments is 123 W, and under maximum load, it can reach 150W.

## Configuration

Full documentation for both RouterOS and SwOS is available at: https://mt.lv/help You can configure the device using WebFig in a web browser or the "WinBox" configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility.**
**To start setup, open http://192.168.88.1 in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker).
The device is equipped with an RS-232 serial port, set by default to 115200 bit/s, 8 data bits, 1 stop bit, no parity. For recovery purposes, it is possible to reinstall the device from the network, see the Reset button.

Marvell Prestera switch chip features user manual

The device supports booting either RouterOS (for full routing and switching functionality) or SwOS (for switch-only operation). By default, the device boots into RouterOS, but you can switch to the other operating system as follows:

- From SwOS: Go to the System menu and click the Boot RouterOS button at the bottom of the page.
- From RouterOS: Open System → RouterBOARD → Settings and select Boot OS.
It is also possible to choose the operating system and configure other boot options using the serial console menu.

## Cooling

The device is equipped with four MT-HotSwapFan units.

## Buttons

**Reset button**:

- Hold this button during boot time until the USR LED light starts flashing, release the button to reset RouterOS configuration.
- Hold the Reset button and power on your device (wait until the "USR" led is blinking then stable "On", and when the "USR" led is "Off" - release the Reset button) - the device is booting in bootp mode to reinstall RouterOS using Netinstall. **The MGMT/BOOT Ethernet port is used for the Netinstall process.** See RouterOS documentation about using the Netinstall recovery utility.
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Release the button before LED begins to flash, to only load backup RouterBOOT without resetting. This is useful for RouterBOOT debugging and recovery.

## Extension slots and ports

- Sixteen 100G QSFP28 ports.
- Four 25G SFP28 ports.
- Two 1G/10G Ethernet ports for management access.
- 1x RJ45 console port (set at 115200bits/s, 8 data bits, 1 stop bit no parity).
Please visit help pages for MikroTik SFP module compatibility and configuration table: MikroTik wired interface compatibility

## LED indicators

- PWR1, PWR2 LEDs are lit when the router is powered with the PSU in use.
- USER LED indicates the device's state while powering it up into different modes, such as resetting the configuration or booting device for the Netinstall utility.
- FAULT LED indicates a problem with any of the cooling fans.

## Accessories

Package includes the following accessories that come with the device:

![](./img/image-2026-2-23_16-17-10.webp)

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.
