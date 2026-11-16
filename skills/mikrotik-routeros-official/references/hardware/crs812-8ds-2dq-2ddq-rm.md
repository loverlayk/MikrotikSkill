# CRS812-8DS-2DQ-2DDQ-RM

> This switch is your next leap forward – a powerful, efficient, and cost-effective way to bring 50G, 200G, and 400G into your rack. Quad-core 2 GHz ARM CPU, dual-redundant power supplies and 4x hot-swap cooling fans,...

![](./img/api_crs812-8ds-2dq-2ddq-rm.jpg)

This switch is your next leap forward – a powerful, efficient, and cost-effective way to bring 50G, 200G, and 400G into your rack. Quad-core 2 GHz ARM CPU, dual-redundant power supplies and 4x hot-swap cooling fans, 2x 10G Ethernet, 8x 50G SFP56, 2x 200G QSFP56, and 2x 400G QSFP56-DD ports. See the [CRS812 DDQ product page](https://mikrotik.com/product/crs812_ddq) for full specifications and brochures.

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

The device is designed for indoor use and can be either mounted in a rack enclosure using the provided rackmount brackets or simply placed on a desktop. Please attach rubber pegs on the bottom of the router if the desired placement is on the flat surface or use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

- Attach the Rackmount ears to the front sides of the device.

![](./img/image-2025-9-25_15-0-43.webp)

![](./img/image-2025-9-25_15-1-1.webp)

![](./img/image-2025-9-25_15-2-13.webp)

![](./img/image-2025-9-25_15-2-33.webp)

1. Attach the small rear Rackmount support ears to both sides of the device.

![](../img/02_r1_left_2.webp)

![](../img/03_r1_left_2_assey.webp)

1. Attach the long rear Rackmount support ears to the rack’s rear side.

![](../img/gdss_assey_r1_3.webp)

1. Install the device in the rack, ensuring that the case support ears are securely fixed to the long support ears.

The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
We recommend Cat6 cables for our devices.
Mounting and configuration of this device should be done by a qualified person.

## Powering

The unit is equipped with two Hot Swap IEC type AC power supplies, 250 W, which accepts 100-240 V ⏦ (~ 50/60 Hz 7 A max).
The maximum power consumption without attachments is 81 W, and under maximum load, it can reach 134 W.

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

- Product code: **CRS812-8DS-2DQ-2DDQ-RM**.
- CPU: Quad-Core AL52400 2000 MHz.
- CPU architecture: ARM 64bit.
- Size of RAM: 4 GB.
- RAM type: DDR4.
- Storage: 512 MB, NAND.
- A number of 1G/2.5G/5G/10G Ethernet ports 2 (supported: 10M/100M/1G/10G).
- A number of 50G SFP56 ports: 8.
- A number of 200G QSFP56 ports: 2.
- A number of 400G QSFP56-DD ports: 2.
- 1x RJ45 console port (set at 115200bits/s, 8 data bits, 1 stop bit no parity).
- Switch chip model: 98DX7335.
- Dimensions: 443 x 156 x 44 mm.
- Operating system RouterOS: v7, License level 6.
- Hot-swap cooling fans: Four.
- Operating temperature: -10°C to +50°C.
- IP: 20.
See the [MikroTik wired interface compatibility](/docs/wired-connections/mikrotik-wired-interface-compatibility) table for supported SFP modules.

## LED indicators

- The POWER1 and POWER2 LEDs light up when the router is powered on with an appropriate power supply.
- USER LED indicates the device's state while powering it up into different modes, such as resetting the configuration or booting device for theNetinstall utility.
- The FAULT LED indicates a problem with any of the cooling fans.
- 50G SFP56 cage outer LED arrows indicate link activity and inner indicate 50G link speed.
- 200G QSFP56 port LEDs indicate each interface four channel activity.
- 400G QSFP56-DD port LEDs indicate each interface first four channel activity.

## Accessories

Package includes the following accessories that come with the device:

![](./img/image-2025-9-30_14-53-22.webp)

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.
