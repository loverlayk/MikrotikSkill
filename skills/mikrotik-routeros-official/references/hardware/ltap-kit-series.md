# LtAP kit-series

> The LtAP kit is a wireless access point with three SIM card slots for cellular data modems.

:::info[This article covers]

- **LtAP LTE kit**
- **LtAP 4G kit**
- **LtAP LTE6 kit**

:::

The LtAP kit is a wireless access point with three SIM card slots for cellular data modems.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- All installation methods for mounting an access point on any wall surface is subject to the acceptance of local jurisdiction.
- The Installation of the equipment must comply with local and national electrical codes.
- This product is intended to be mounted outdoors on a pole but can also be installed indoors. Read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation to people and damage to the system.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Use this product with care and operate at your own risk!
- In the case of device failure, disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.
- To avoid pollution of the environment, separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

## Quickstart

follow these quick steps to set up your device:

- Unscrew two screws and remove doors to access all ports. See the section.
- Connect your Internet cable to the Ethernet port (this is optional if using LTE as the primary connection);
- Install your modem using miniPCIe slot (optional);
- Insert the SIM card into the SIM 2 slot (middle).
- Connect GPS antenna (optional), (see ).
- Mount unit in your desired place (see ).
- Choose your powering solution (see ).
- Navigate to the network connections section on your computer and locate the wireless network named "*MikroTik-....*". Proceed to connect to it (ensure to check the wireless passwords on the sticker);
- Establish a connection using a mobile application. Alternatively, use WebFig in a web browser or the "WinBox" configuration tool at https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Start configuration within the chosen tool, using the default IP address 192.168.88.1. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device;
- Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Update the device by selecting the "Check for updates" button to the latest RouterOS software for this to work the device needs to have an active Internet connection;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the "QuickSet" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

## Extension slots and ports

![](./img/api_ltap-2hnd_r11e-lte7.jpg)

- Built-in 2 GHz wireless access point module, AP/station/bridge/p2p modes are supported. Onboard PIF antennas built-in, as well as MMCX connectors for external antennas (software selectable).
- Two miniPCIe slots and three SIM slots.
- Built-in GPS module with an external SMA connector.
- Gigabit Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices. The Ethernet port accepts 12-30 V DC powering from a passive PoE injector.
- One DB9 RS232 serial port for serial console access. Configured as 115200 bit/s, 8 data bits, 1 stop bit, no parity.
- One USB 2.0 port for storage devices or cellular modems.

## Mounting

- It is possible to attach the device to a wall, using the provided four screws and designed four holes on the unit.
- The ports are protected with a small door, that is held in place with two screws. Remove to access Ethernet ports, antenna connector, SIM slots, etc.
- The door has cut-out places for all available ports, so you can guide through all necessary cables, but only break out the openings that you will use.
- Several places for external antennas are provided on the case, use an appropriate size drill, to make them available. Be careful and measure the chosen antenna, so that it does not touch the internal PCB board when installed.

![](../img/worddavea859ff4c106ecf91e733a39269a8237.webp)

The device can be used both indoors and outdoors. The IP rating scale of IP54.

If you intend to mount outdoors, ensure that any cable openings are directed downwards. The Mounting direction is indicated on the device with an arrow pointing up. Use POE injector and proper grounding. Recommended using Cat6 shielded cable.
Warning! This equipment should be installed and operated with a minimum distance of 30 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.
The device enclosure has places where you can drill openings for external LTE and GPS antennas. Use a drill to make holes that are appropriate for the antenna cable used.

## Configuration

You should select the "Check for updates" button and update your RouterOS software to the latest version to ensure the best performance and stability. RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: https://mt.lv/help In case IP connection is not available, the WinBox tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default). For recovery purposes, it is possible to boot the device from a network, see the section .

## GPS

The built-in GPS module requires an external antenna to be used (SMA connector is already mounted behind the unit door). See the section on how to remove the door.
**Attention** the GPS uses an active antenna, only connect and disconnect the antenna, when the device is turned off!

**Supports - GPS, GLONASS, BeiDou, Galileo).**
Make sure that the GPS package is installed on your device. Check by following command /system package print. If not installed download extra packages at our download page accordingly to your RouterOS version and install the GPS package by dragging it to the Files menu. Enable GPS and start working:

- Enabling - /system gps set enable=yes;
- Setting antenna to external - /system gps set gps-antenna-select=external;
- Checking configuration - /system gps print.
Configuration information - [GPS manual, basic examples](/docs/mobile-networking/gps/#basic-examples)

## Powering

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 12-30 V DC ⎓ with provided 24 V, 1.2 A adapter.
- Ethernet port accepts passive Power over Ethernet 12-30 V DC ⎓ (compensate for the loss on cable, so more than 12 V recommended).
- The automotive connector can be used to power the device from regular 12/24 V ⎓ connections in automobiles and buses. The plug has four pins: bottom left (black) is the ground, bottom right is power in (red). The upper two (AUX) are reserved for future use.
The power consumption under maximum load can reach 12 W without attachments. Attach ground (earth) wire to the screw under the door.

### Connecting to a PoE Adapter: (Not included)

- Connect the Ethernet cable from the device to the POE out port of the POE adapter.
- Connect an Ethernet cable from your LAN to the POE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Front status LED behavior

- Solid Blue – the device is powered on.
- Solid Green – user-defined LED, can be configured in system settings.
- Solid Green – state of GPS module.
- Solid Green– the set of five green LED, shows the signal strength of the cellular network.

![](../img/worddav4493bb2b243dca45caaf926c70f8b5b6.webp)

## miniPCIe slot

### SIM card connectivity

- MiniPCIe 1 (top slot) supports PCIe and USB 2.0 cards but is shared with the USB 2.0 type A port (can use either the USB port or miniPCIe slot at the same time). It can be used only for SIM slot #1.
- MiniPCIe 2 (bottom slot) supports only USB (2.0 and 3.0) miniPCIe modems (no PCIe support). Uses SIM slot #2 and SIM slot #3. By default uses SIM slot #2.
- USB 2.0 type A port (can only be used if miniPCIe 1 is not used).
- To use the top miniPCIe slot with a USB type miniPCIe card, switch the USB connections to the miniPCIe slot: /system routerboard usb set type=mini-PCIe This will disable the USB 2.0 port on the front of the unit.
- Insert the SIM card into the top slot by a chip on the SIM card facing down. Bottom slots – with the chip facing up.
check if you are using the correct SIM slot. For the modem inserted in the bottom mini-pcie slot, you need to use either sim slot 2 or sim slot 3. And the used sim slot needs to be selected in RouterOS.
CLI command to select the sim slot: */system routerboard modem set sim-slot=2*

### Modem installation

This LtAP version is with the modem installed in the bottom slot. When installing an additional modem use the upper slot. In this case, an internal antenna is connected to the bottom modem.
Installing a miniPCIe module should be done by a qualified person, follow safety precautions when handling electrical equipment:

- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage;
- Remove six screws on the bottom of the case and lift off the top part of the case. Note that antenna cables are connected to the bottom modem;
- Locate the miniPCIe slot and remove two factory attached screws;
- Attach provided a thick thermal pad to the card, and install the card into miniPCIe slot so that thermal pad is between PCB and card;
- The secure card in place using previously removed two screws;
- Guide your antenna cables through openings near the GPS connector and connect to your modem. Recommended using silicone rubber to secure connectors in place.
- Attach a thinner thermal pad to the top of the card;
- When using external antennas, connectors can be attached on the case sides, to make openings use a 6.5 mm drill bit, see section part 4;
- see picture below for reference on how to place rubber seals for best water protection;
- Reassembly in backorder. Tightening torque for PCB screws 0.3 Nm, case cover/enclosure screws 0.5 Nm.

![](../img/worddavec21901c2798bd037d088efaaed068d8.webp)

After you have reinserted the device into the case and secured it with the screws that were removed earlier, slide in the SIM cards from your mobile operator into the SIM slots, with the chips facing as shown on the port label. The slot accepts miniSIM (2FF). SIM slots 2 and 3 apply to the bottom miniPCIe slot and can be switched in RouterOS "/system routerboard sim" menu.

## Reset button

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes accessories that come with the device:

- K-67 fastening set. Includes four screws 4x25 mm, four dowels 6x30 mm.
- Cable DC ⎓ (H4130-04PDB000R 3 mm 2x2P Housing) to (StripJacket 5 cm+WireEnd Strip/Tin 1 cm) 24 AWG (Black/Red/Blue/Orange) 0.35 m.
- EU/US Switching Power Supply 24 V, 1.2 A, 28.8 W, 86.8%, VI, DC ⎓ cable: 220 cm RA DC plug mod Hor CMC shorter plug.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

![](../img/worddav90b536202301fa410028bd0e2ac949b9.badge.webp)

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Select Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.

## Notice

- The Frequency band 5.470-5.725 GHz isn’t allowed for commercial use.
- In case WLAN devices work with different ranges than the above regulations, then a customized firmware version from the manufacturer/supplier is required to be applied to the end-user equipment and also prevent the end-user from reconfiguration.
- For Outdoor Usage: End-user requires approval/license from the NTRA.
- Datasheet for any device is available on the official manufacturer website.
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 2.400 – 2.4835 GHz, the TX power is limited to 20dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.150 – 5.250 GHz, the TX power is limited to 23dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.250 – 5.350 GHz, the TX power is limited to 20dBm (EIRP).

make sure the device has a lock package (firmware version from the manufacturer) which is required to be applied to the end-user equipment to prevent the end-user from reconfiguration. The product will be marked with country code “-EG”. This device needs to be upgraded to the latest version to ensure compliance with local authority regulations! It is the end users responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.
