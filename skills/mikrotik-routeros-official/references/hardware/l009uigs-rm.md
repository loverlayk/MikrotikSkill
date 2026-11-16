# L009UiGS-RM

> L009 is more than just a router. This product line is up to 4 times faster than RB2011, it has a modern ARM CPU with container support, an innovative enclosure that allows mounting up to four routers in a single 1U...

![](./img/api_l009uigs-rm.jpg)

## [L009UiGS-RM](https://mikrotik.com/product/l009uigs_rm)

L009 is more than just a router. This product line is up to 4 times faster than RB2011, it has a modern ARM CPU with container support, an innovative enclosure that allows mounting up to four routers in a single 1U space, more RAM, PoE, and 2.5G SFP support. This version comes with 1U rackmount accessories. See the [L009UiGS-RM product page](https://mikrotik.com/product/l009uigs_rm) for full specifications and brochures.

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

- Make sure your ISP allows hardware changes and will automatically issue an IP address;
- Connect your ISP cable to the first Ethernet port;
- Connect your PC to any of the Ethernet ports;
- Connect the device to the power source;
- Configure your network card settings to obtain the IP address automatically using DHCP;
- Configuration should be made using **WebFig** in a web browser or the **WinBox** configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Open `http://192.168.88.1` in a web browser to start setup. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device. Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- In the "Quick Set" menu, choose your country to apply country regulation settings;
- Set up your router password.

## Powering

The power consumption under maximum load can reach 40 W. The device accepts power from the power jack or from the first Ethernet port:

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 24-56 V DC.
- The First Ethernet port accepts Power over Ethernet 802.3af/at.
- The 2-pin terminal on the side accepts 24-56 V DC.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE port of the PoE adapter;
- Connect an Ethernet cable from your LAN to the LAN port of the PoE adapter, mind the arrows for data and power flow;
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Configuration

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting with the [RouterOS documentation](https://mt.lv/help) to get accustomed to the possibilities. In case an IP connection is not available, the **WinBox** tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default). For recovery purposes, it is possible to boot the device from the network, see the [Reset button](#reset-button).

## Mounting

The device is designed to use indoors and it can be mounted on the wall, or it can be placed on the desktop.

![](./img/2270_hi_res.webp)

- Find the designed mounting holes on both sides of the device, as shown in the picture;
- Use provided screws to secure the device to the wall;
- Based on the wall material you can use a drill bit and provided dowels.

The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
We recommend Cat6 cables for our devices.
*The mounting and configuration of this device should be done by a qualified person.*

## Rackmount

If desired placement is rackmount, additional brackets can be purchased separately:

### RB5009/L009 rackmount kit K-79

![](../img/image2021-7-28_16-8-26.webp)

## Extension slots and ports

- Eight 10/100/1000 Gigabit Ethernet ports.
- One 2.5G SFP port.
- One USB 3.0 type-A port.
- RJ45 serial console port.
- PoE-in on Ether1 and PoE-out on Ether8.

## Reset button

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when the green LED starts flashing, to reset the RouterOS configuration to defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network using Ether1).

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## LED

- Hidden Green LED behind the Reset button is a USER LED
- Blue LED 1 is the DC1 Power LED
- Blue LED 2 is the DC2 Power LED
- Green SFP LED is an SFP port link and activity LED
- Ethernet RJ45 Green LEDs are Ethernet port link 1Gbps and activity LEDs
- Ethernet RJ45 Port 1 Orange LED is PoE-in status LED
- Ethernet RJ45 Port 2-8 Orange LEDs only - 100Mbps

## Accessories

The package includes the following accessories that come with the device:

- ADAPT1_EU/US Switching Power Supply 24V 1.5A 36W
- SET1_ K-55 fastening set
- PAD1_ 4 pcs Pad D=7; H=1.5 mm, one side adhesive 3M988T

Please see the [MikroTik SFP module compatibility table](/docs/wired-connections/mikrotik-wired-interface-compatibility).

## Specifications

- CPU: IPQ-5018 800 MHz.
- CPU architecture: ARM.
- CPU core count: 2.
- Size of RAM: 512 MB.
- RAM type: DDR3L.
- Storage: 128 MB, NAND.
- Number of 1G Ethernet ports: 8.
- Number of 2.5G SFP ports: 1.
- USB port: 1 (3.0 type A).
- PoE-in: Ether1.
- PoE-out: Ether8.
- Serial console port: RJ45.
- Operating system: RouterOS (License level 5).
- Switch chip model: 88E6190.
- Dimensions: 220 x 125 x 22 mm.
- Operating temperature: -40°C to +70°C.
- IP rating: IP20.

For more information about this product, specification and pictures please visit our web page: https://mikrotik.com/product/l009uigs_rm

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Safety notice

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as at designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.
