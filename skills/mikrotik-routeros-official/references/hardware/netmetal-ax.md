# NetMetal ax

> The Mars rover of networking. Our toughest long-range outdoor access point – now with Wi-Fi 6! See the NetMetal ax product page for full specifications and brochures.

![](./img/api_l23ugsr-5haxd2haxd-nm.jpg)

## [NetMetal ax](https://mikrotik.com/product/netmetal_ax) (L23UGSR-5HaxD2HaxD-NM)

The Mars rover of networking. Our toughest long-range outdoor access point – now with Wi-Fi 6! See the [NetMetal ax product page](https://mikrotik.com/product/netmetal_ax) for full specifications and brochures.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- All installation methods for mounting an access point on any wall surface is subject to the acceptance of local jurisdiction.
- The Installation of the equipment must comply with local and national electrical codes.
- This product is intended to be mounted outdoors on a pole. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.
- This is a class A device. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

## Quickstart

The configuration is the same as PTP Bridge in AP mode, wireless mode is set to AP for PTMP setups as well. The router can be accessed directly using the address. If the device is connected to the network with enabled DHCP server, configured DHCP client on the bridge interface will get the IP address, that can be used to access the router.

Please follow these quick steps to set up your device:

- Open the upper cover (see [Removing upper and bottom covers](#removing-upper-and-bottom-covers));
- Connect an external antenna to the SMA connector (see [Antenna usage](#antenna-usage));
- Open the bottom cover (see [Removing upper and bottom covers](#removing-upper-and-bottom-covers));
- Connect your ISP cable to the device, make sure the ISP is allowing hardware change and will issue an automatic IP address;
- Connect the device to the power source (see [Powering](#powering));
- Navigate to the network connections section on your computer and locate the wireless network named "*MikroTik-...*". Proceed to connect to it (check the wireless passwords on the sticker);
- Configuration should be made via a wireless network using a mobile application or you can use the **WinBox** configuration tool [https://mt.lv/winbox](https://mt.lv/winbox);
- Download and open **WinBox**, and choose the **Neighbors** tab to find the device;
- Click on the MAC address. The username is "**admin**" and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WinBox** "**Files**" menu and reboot the device. By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the wifi-interface menu set up the following: Choose your country, to apply country regulation settings; SSID; mode; See the manual page: [WiFi](/docs/wireless/wifi)
- Set up your wireless network security profile;
- If you need to use a SIM card, open the case and install your desired modem into miniPCIe slot;
- Insert a Nano SIM card into the slot.

## Powering

The device accepts power in the following ways:

- Ethernet port accepts passive PoE, input voltage 18-28 V DC;
- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 12-28 V DC.

The maximum power consumption without attachments is 12 W, and under maximum load it can reach 25 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter;
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter;
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

![](../img/worddav90b536202301fa410028bd0e2ac949b9.badge.webp)

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Click Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Removing upper and bottom covers

- To remove the upper cover, unscrew two captive screws and slide it off the main body. Do not remove screws completely, when assembling tightening torque 0.2 Nm.
- To remove the bottom cover, release clips for both fasteners and cover will be free to open.

![](./img/worddavc9c6877f91a28badac2e83fffdf112fc.webp)

## Mounting

The NetMetal ax is designed to be used outdoors and mounted on pole or DIN rail.

When mounting, please ensure that cable feed is pointing downwards.
The IP rating scale of this device is IP66. We recommend using Cat6 shielded cables.
Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference. Mounting and configuration of this device should be done by a qualified person. The mounting hose clamp is provided with the package.

![](../img/worddav3ec521bfbc324e6d0ab5f0edb062be26.webp)

- Guide hose clamp through the opening on the back of the device.
- Attach to the pole or mast.
- Align and secure by hose clamp screw using PH2 screwdriver.
- The device should be always placed by TOP cover facing upwards.

![](../img/worddavda4208862be213501829bfab8cb074be.webp)

- When mounting on DIN rail, please find a special bracket in the package and secure it with four screws to the back of the unit.

![](../img/worddav3d7e2b3fdb928200b1ee79547d0ae2a1.webp)

- With the attached mounting bracket you will be able to slide the device on the DIN rail.

## Grounding

The installation infrastructure (towers and masts), as well as the router itself, must be properly grounded. The device includes a grounding wire attachment screw. Attach your grounding wire to the grounding screw, then attach the other end of the grounding wire to the grounded mast.

![](./img/worddav250d75b2c9c0210376e71a4ac45dc34e.webp)

Please secure all loose Ethernet cables and antenna cables to the pole or mast approximately 30cm from the device, so that the cable weight is not pulling the ports and connectors.

## Front status LED behavior

RouterOS allows configuring each LED's activity the way that the user wishes. It is possible to configure the LEDs to display wireless strength, blink the LEDs on interface traffic activity and many other options. See the [LEDs](/docs/hardware/leds) page for further information.
Default factory configuration for this device:

![](./img/worddavb6ef4379c1aa857f7a702dee1e69aa7f.webp)

- Solid Blue – The device is powered on.
- Solid Green – Active SFP port.
- Solid Green – Active Ethernet port.
- Solid Green – The set of five green LEDs, shows the signal strength.

## Configuration

The device is configured as a wireless access point, with the Ethernet port configured as a DHCP client, for connecting to your ISP router or switch. A DHCP server is configured on the wireless interface.
We recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: https://mt.lv/help In case IP connection is not available, the WinBox tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see a section [Reset button](#reset-button).

## Extension slots and ports

- Gigabit Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices.
- SFP port (2.5G supported).
- External SMA antenna connectors.
- MiniPCIe slot.
- Integrated Wireless module operating at 2.4 GHz, 802.11b/g/n/ax protocol.
- Integrated Wireless module operating at 5 GHz, 802.11a/n/ac/ax protocol.
- USB type-A.
- Nano SIM slot.

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

- EU Switching Power Supply 24 V ⎓ 1,2 A.
- Gigabit PoE injector.
- K-27 DIN rail bracket mounting set.
- Hose clamp 40/60 w2 A2 9 mm.
See the [MikroTik wired interface compatibility](/docs/wired-connections/mikrotik-wired-interface-compatibility) table for supported SFP modules.

## MiniPCIe slot usage

This NetMetal ax version does not have a modem installed. To install the module you will need to remove the upper cover and open bottom cover (see [Removing upper and bottom covers](#removing-upper-and-bottom-covers)). Installing a miniPCIe module should be done by a qualified person, please follow safety precautions when handling electrical equipment:

- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage.
- Use a screwdriver to remove the four screws.

![](../img/worddav1df83a206909e5f05e7831eb898fefda.webp)

- Remove the top cover by lifting it.
- Locate the miniPCIe slot on the PCB and remove two factory attached screws.

![](../img/worddav77de0b747bcb46617a85b764f359e306.webp)

- Attach provided a thick thermal pad to the card, and install the card into miniPCIe slot so that the thermal pad is between PCB and card.
- Secure the card in place using previously removed two screws.
- Attach the grey uFL connector to the MAIN antenna connector of the modem, attach the black cable to the secondary (or AUX) connector.
- Attach a thinner thermal pad to the top of the card.

![](../img/image_15.webp)

- Drill holes for SMA connectors.
- Guide through the card cables.
- Reassemble.

When assembling make sure the rubber sealing is placed firmly around the case for equal spread to prevent water contamination. Case screw torque 2,5 Nm.
When mounting the antenna for the installed card, please make sure to keep them separate at a good distance from Wireless antennas.

## Antenna usage

Antenna Installation. WARNING: It is the installer's responsibility to ensure that when using the authorized antennas in the United States (or where FCC rules apply); only those antennas certified with the product are used. The use of any antenna other than those certified with the product is expressly forbidden in accordance with FCC rules CFR47 part 15.204. The installer should configure the output power level of antennas, according to country regulations and per antenna type. Professional installation is required for equipment with connectors to ensure compliance with health and safety issues.
LIST OF APPROVED 2GHz ANTENNAS:

- 5 dBi Dipole ACOMNIRPSMA
LIST OF APPROVED 5GHz ANTENNAS:

- 30 dBi Parabolic dish MTAD-5G-30D3
- 19 dBi Sector MTAS-5G-19D120
Antennas of the same type and lower gain than those listed above may be used in compliance with certification.
More information on the WiFi interface: [WiFi](/docs/wireless/wifi)

## Specifications

| Parameters | Description |
| --- | --- |
| **Product Code** | L23UGSR-5HaxD2HaxD-NM |
| **Architecture** | ARM 32-bit |
| **CPU** | IPQ-5010, 2 core, 800 MHz |
| **RAM** | 256 MB |
| **Storage** | 128 MB, NAND |
| **Operating System** | RouterOS v7 (license level 4) |
| **Wireless 2.4 GHz** | 802.11b/g/n/ax, 2 chains, 574 Mbit/s |
| **Wireless 5 GHz** | 802.11a/n/ac/ax, 2 chains, 2400 Mbit/s |
| **Antenna** | 2 × RP-SMA female, antennas not included |
| **10/100/1000 Ethernet ports** | 1 |
| **SFP ports** | 1 (2.5G supported) |
| **USB port** | 1 × USB type-A |
| **SIM slots** | 1 × Nano SIM |
| **miniPCIe slots** | 1 |
| **Number of DC inputs** | 2 (DC jack, PoE-in) |
| **PoE-in** | Passive PoE, 18-28 V |
| **DC jack input voltage** | 12-28 V |
| **Max power consumption** | 25 W |
| **Max power consumption without attachments** | 12 W |
| **Cooling type** | Passive |
| **Dimensions** | 143 × 247 × 48 mm |
| **Operating temperature** | -40 °C to +70 °C |
| **MTBF** | Approximately 200,000 hours at 25 °C |
| **Certification** | CE, FCC, IC, EAC, ROHS |
| **IP rating** | IP66 |

For more information about this product, specifications, pictures, downloads and test results please visit our web page: https://mikrotik.com/product/netmetal_ax

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.
