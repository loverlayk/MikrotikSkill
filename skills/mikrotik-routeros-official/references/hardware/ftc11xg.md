# FTC11XG

> The FTC11XG is a weatherproof IP55 Fiber-to-Copper converter to transform your 10 Gigabit SFP+ fiber connections into RJ45 10 Gigabit Ethernet. It runs a full version of SwOS Lite and has its own switch-chip!. See...

![](./img/api_ftc11xg.jpg)

The FTC11XG is a weatherproof IP55 Fiber-to-Copper converter to transform your 10 Gigabit SFP+ fiber connections into RJ45 10 Gigabit Ethernet. It runs a full version of SwOS Lite and has its own switch-chip!. See the [FTC11XG product page](https://mikrotik.com/product/ftc11xg) for full specifications and brochures.

## Safety Warnings
Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
Use only accessories approved by the manufacturer, and which can be found in the original packaging of this product.
This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
This product is intended to be mounted indoor or outdoors on a pole. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
We highly recommend to use AC/DC power supply only for indoor use cases.
The socket-outlet shall be installed near the equipment and shall be easily accessible.
We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.

## First steps:
- Use a screwdriver to unscrew the central screw and remove the plastic cover;
- Underneath the cover, there are Ethernet and SFP output ports;
- Set your IP for PC to 192.168.88.2/24;
- Connect your devices;
- Choose your powering solution (see "");
- Open http://192.168.88.1 in your web browser to start configuration, user name: admin and there is no password by default;
- Download the latest version of SwitchOS Lite software from https://mikrotik.com/download;
- Upload a file with the web browser in the Upgrade tab, the device will reboot after the upgrade;
- Set up your password to secure the device.
- If needed, the device can be mounted on the wall;
- The screws with dowels are included in the package.

## Mounting
The device can be mounted in several ways: on a wall, pole, or mast using a specially designed MikroTik holder that comes with the package. The unit can be attached to the pole using zip ties or a steel clamp (not included).
To prevent the bottom lid from opening, use the included M4x14 PH2 security screw.
The IP rating for this device is IP55.
When mounting outdoors, please ensure that any cable openings are directed downwards. Recommended using Cat5/6 cable. Use the proper case grounding.

### Mounting on the mast or pole:

![](../img/image-2024-5-24_12-13-23.webp)

![](../img/image-2024-5-24_12-10-15.webp)
- Mount the included bracket to the pole or mast using steel hose clamp (not included), guiding it through the hole.
- Mount and align the device on the previously installed bracket on the pole or mast.
- Unscrew the bottom lid screw and open the lid.
- Guide the cables through the opening and connect them to the appropriate ports.
- Close the bottom lid and secure it with a screw.
It's recommended to secure Ethernet cable to the pole using zip ties. With the distance from the device approximately 30 cm.

### Mounting unit on the wall:

![](../img/image-2024-5-24_12-2-14.webp)

![](../img/image-2024-5-24_12-10-15.webp)

- Place the bracket at the location where you plan to install the device and mark spots for drilling holes and, if needed, for cables. Align accordingly, depending on the final mounting position of the device.
- Drill the holes.
- Insert included dowels if needed, depending on the wall structure and material.
- Screw the included bracket onto the wall or ceiling.
- Mount and align the device on the previously installed bracket.
- Unscrew the bottom lid screw and open the lid.
- Guide the cables through the opening and connect them to the appropriate ports.
- Close the bottom lid and secure it with a screw.
Avoid mounting the device on the low ground spot, as you won't be able to attach and close the bottom latch.

## Bottom Lid
- The bottom lid is secured in place with the screw.
- Use the Philips PH2 screwdriver to unscrew it.

![](../img/image-2024-5-24_12-16-1.webp)

- Pull the lid in the opposite direction from the device to remove it.

![](../img/image-2024-5-24_12-16-18.webp)

- Reassemble.

![](../img/image-2024-5-24_12-16-39.webp)

## Powering
The device accepts power from the power jack or from the Ethernet port:

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 18-57 V ⎓ DC;
- Ethernet1 port accepts 802.3 bt PoE.
The maximum power consumption without attachments is 9W, and under maximum load, it can reach 10W.

### Connecting to a PoE Adapter:

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter;
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter;
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.
The product should be properly grounded.

## Extension slots and ports
- One 10/100/1000 Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices.
- One 1G/2.5G/5G/10G Ethernet port.
- One 10G SFP+ port.

## Configuration and operating system support
This FTC11XG has built-in backup SwOS firmware which can be loaded in case standard firmware breaks or an upgrade fails:

- Holding the reset button for a few seconds while the device is powered and booting will reset the configuration and load the backup firmware. The reset button is located under the bottom lid.
- After loading backup firmware, it is possible to connect to 192.168.88.1 (or leased address from a DHCP server) using a web browser and install new SwOS firmware.

## LED indicators
This device features LED indicators, including PWR LED (Power), ETH activity, and SFP activity LEDs.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.
