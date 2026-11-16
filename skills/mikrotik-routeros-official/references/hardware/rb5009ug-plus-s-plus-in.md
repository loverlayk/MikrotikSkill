# RB5009UG+S+IN

> The ultimate heavy-duty home lab router with USB 3.0, 1G and 2.5G Ethernet and a 10G SFP+ cage. You can mount four of these new routers in a single 1U rackmount space! Unprecedented processing power in such a small...

![](./img/api_rb5009ug_s_in.jpg)

## [RB5009UG+S+IN](https://mikrotik.com/product/rb5009ug_s_in)

The ultimate heavy-duty home lab router with USB 3.0, 1G and 2.5G Ethernet and a 10G SFP+ cage. You can mount four of these new routers in a single 1U rackmount space! Unprecedented processing power in such a small form factor. See the [RB5009UG+S+IN product page](https://mikrotik.com/product/rb5009ug_s_in) for full specifications and brochures.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- The Installation of the equipment must comply with local and national electrical codes.
- This unit is intended to be installed in the rackmount. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity, or hot environments.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik devices must be professionally installed.

## Quickstart

- Make sure your ISP is accepting hardware changes and will automatically assign an IP address;
- Connect the ISP cable to the Ethernet1 port;
- Connect the PC to any port except Ethernet1;
- Connect the device to a power source;
- Configure your network card settings to obtain the IP address automatically using DHCP;
- Configuration should be made using **WebFig** in a web browser or the **WinBox** configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Open `http://192.168.88.1` in a web browser to start setup. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device. Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- Set up your router password.

## Powering

The power consumption under maximum load can reach 20 W. The device accepts power from the power jack or from the first Ethernet port:

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 24-57 V DC.
- The first Ethernet port accepts Power over Ethernet 24-57 V DC.
- The 2-pin terminal on the side accepts 24-57 V DC.
- 2-pin terminal: Connector Plug P=5.08 mm 1x2pin RA TH, tin plated, 300 V 10 A.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE port of the PoE adapter;
- Connect an Ethernet cable from your LAN to the LAN port of the PoE adapter, mind the arrows for data and power flow;
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Configuration

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting with the [RouterOS documentation](https://mt.lv/help) to get accustomed to the possibilities. In case an IP connection is not available, the **WinBox** tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default). For recovery purposes, it is possible to boot the device from the network, see the [Reset button](#reset-button).

## Mounting

The device is designed to use indoors and it can be mounted on the wall, or it can be placed on the desktop.

![](../img/image2021-7-28_16-1-26.webp)

- Find the designed mounting holes on both sides of the device, as shown in the picture;
- Use provided screws to secure the device to the wall;
- Based on the wall material you can use a drill bit and provided dowels.

The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
We recommend Cat6 cables for our devices.
*The mounting and configuration of this device should be done by a qualified person.*

## Rackmount

If desired placement is rackmount, additional brackets can be purchased separately:

### RB5009 rackmount kit K-79

![](../img/image2021-7-28_16-8-26.webp)

## Extension slots and ports

- Seven 10/100/1000 Gigabit Ethernet ports.
- One 2.5G Ethernet port.
- One 10G SFP+ port.
- One USB 3.0 type-A port.

## Reset button

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when the green LED starts flashing, to reset the RouterOS configuration to defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## LED

- Hidden Green LED behind the Reset button is a USER LED
- Blue LED 1 is the DC1 Power LED
- Blue LED 2 is the DC2 Power LED
- Green SFP+ LED is an SFP+ port link and activity LED
- Ethernet RJ45 Green LEDs are Ethernet port link and activity LEDs
- Ethernet RJ45 Port 1 Orange LED is PoE-in status LED
- Ethernet RJ45 Port 2-8 Orange LEDs are unused on this model

## Accessories

The package includes the following accessories that come with the device:

- ADAPT1_EU/US Switching Power Supply 24V 1.5A 36W
- SET1_ K-55 fastening set
- PAD1_ 4 pcs Pad D=7; H=1.5 mm, black, one side adhesive 3M988T

See the [MikroTik wired interface compatibility](/docs/wired-connections/mikrotik-wired-interface-compatibility) table for supported SFP modules.

## Specifications

- CPU: 88F7040 1.4 GHz.
- CPU architecture: ARM 64-bit.
- CPU core count: 4.
- Size of RAM: 1 GB.
- RAM type: DDR4.
- Storage: 1 GB, NAND.
- Number of 1G Ethernet ports: 7.
- Number of 2.5G Ethernet ports: 1.
- Number of 10G SFP+ ports: 1.
- USB port: 1 (3.0 type A).
- Operating system: RouterOS (License level 5).
- Switch chip model: 88E6393.
- Dimensions: 220 x 125 x 22 mm.
- Operating temperature: -40°C to +60°C.

For more information about this product, specification and pictures please visit our web page: https://mikrotik.com/product/rb5009ug_s_in

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Safety notice

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as at designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.
