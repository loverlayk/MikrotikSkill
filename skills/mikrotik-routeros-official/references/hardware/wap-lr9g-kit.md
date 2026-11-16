# wAP LR9G kit

> The wAP is a small weatherproof device with an integrated LR9 card for UDP packet forwarding to the chosen server.

![](./img/api_rbwapr-2nd_r11e-lr9g.jpg)

### [wAP LR9G kit](https://mikrotik.com/product/wap_lr9g_kit) (RBwAPR-2nD&R11e-LR9G)

The wAP is a small weatherproof device with an integrated LR9 card for UDP packet forwarding to the chosen server.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- All installation methods for mounting an access point on any wall surface is subject to the acceptance of local jurisdiction.
- The Installation of the equipment must comply with local and national electrical codes.
- This product is intended to be mounted outdoors on a pole but can also be installed indoors. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation to people and damage to the system.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.
- This is a class A device. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

## Quickstart

- Make sure your ISP is allowing hardware change and will issue an automatic IP address;
- Open the bottom lid;
- Connect an external antenna to the SMA connector;
- Connect the device to the power source;
- Connect your ISP cable to the Ethernet port;
- Navigate to the network connections section on your computer and locate the wireless network named *"MikroTik-..."*. Proceed to connect to it (check the wireless passwords on the sticker);
- Configure via a wireless network using a mobile app. Alternatively, use a web browser through **WebFig** or the **WinBox** configuration tool https://mt.lv/winbox. Download and open **WinBox**, and choose the **Neighbors** tab to find the device;
- The default IP address is `192.168.88.1`. Click on the IP address. If the IP is not available, use **WinBox** and connect using the MAC address. The username is "**admin**" and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the *"QuickSet"* menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field;
- Find *LR Gateway ID* on the label within the product and register it in your Network Server.

![](../img/image2020-2-28_11-58-38.webp)

## Extension slots and ports

![](../img/worddavce41d1c1b9075684fc0706decb6269dd.webp)

- 10/100 Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices.
- External SMA antenna connector already connected to the LR9G card that is used for LoRa frequencies.
- External SMA antenna connector already connected to the LR9G card that is used for GPS reception.
- LED indicating the power state of the device.
- LED Indicating the activity of the Wireless network.
- Automotive connector. Pinout: A - reserved for future use (orange), B - reserved for future use (blue), C - ground (black), D – power in (red).
- MiniPCIe slot with an integrated LR9G card.
- Integrated Wireless module operating at 2.4 GHz, 802.11b/g/n protocol.
- SIM Slot.

## Powering

The device accepts power in the following ways:

- The Ethernet port accepts passive PoE 9-28 V DC ⎓.
- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin-positive plug) accepts 9-28 V DC⎓.
- Automotive connector 12-30 V DC⎓.
The power consumption under maximum load can reach 7 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Mounting

The device can be mounted in several ways: pole, wall, ceiling or it can be placed in a specially designed MikroTik holder which comes with the package. The package also includes a drill hole template with detailed mounting instructions, to help you with the Ethernet cable installation and attachment to a ceiling or a wall. Steel bracket to put on the other side of a dropdown ceiling tile and two screws and wall anchors. Zip ties or steel clamps for mounting on the pole.

The IP rating scale for this device is IP54. When mounting outdoors, please ensure that any cable openings are directed downwards. We recommend using the POE injector and proper grounding with Cat6 shielded cable. When using and installing this device please pay attention to Maximum Permissible Exposure (MPE) safety distance with a minimum of 20 cm between the radiator and your body.

Mounting on the mast or pole:

It's recommended to use electrical tape to increase friction between materials.

![](../img/worddavfeab95dc2851e833db4e23ae758a6c1d.webp)

- Mount plastic tie straps to steel bracket guiding them through holes.
- Mount the bracket to the device.
- Secure them with a screw.
- Mount and align the device on the pole or mast.
- Guide the Ethernet cable through the opening and connect it to the Ethernet port.
- Close the bottom latch and secure it with a screw.

It's recommended to secure the Ethernet cable to the pole using zip ties. The distance from the device is approximately 30 cm.

Mounting unit on the wall:

![](../img/worddav69823f128bad2ec6044a62c61dae8828.webp)

- Use included a template to mark spots for drilling holes. And if needed for Ethernet cable. Align accordingly, it will depend on how the device will be mounted finally.
- Insert dowels if needed, depending on the wall structure and material.
- Place included a steel bracket on the wall.
- Use screws to secure it in place.
- Extend your Ethernet cable through the opening and connect to the Ethernet port.
- Mount the device on the steel bracket
- Secure it in place with the screw.
- Close the bottom latch.

Avoid mounting the device on the low ground spot, as you won't be able to attach and close the bottom latch.

Mounting on the ceiling:

![](../img/worddave5c1e23fd8f38eb305de915ea3609bb1.webp)

A Special bracket is included in the package to mount on the drop ceiling. As it consists of two parts, to be attached on both sides of the ceiling tile.

- Use the template to mark spots for holes.
- Place both mounting brackets on the spot.
- Secure them together using screws.
- Continue assembling in the same manner if mounting on the wall.

- Extend your Ethernet cable through the opening and connect to the Ethernet port.
- Mount the device on the steel bracket.
- Secure it in place with the screw.
- Close the bottom latch.

## Bottom Lid

- The bottom lid is secured in place with the captive screw.

![](../img/worddavf9d64e5d4da7d1db76c0a479e1959fd3.webp)

- Use a Torx T20 screwdriver to unscrew it, but do not remove the screw completely.

![](../img/worddav808b8a4013f2b26d3a99b4b85417f536.webp)

- Pull the cover in the opposite direction from the device to remove it.

![](../img/worddava4a960260b39a8f742893b001ac9fb6e.webp)

- Reassemble.

## Configuration

To set the configuration for LR please connect to the device and log in with your web browser or use a mobile application. Two easy steps to follow:
**First step:**

- Once logged in, Quick Set will be selected, please switch to WebFig on the right side of the screen. If the configuration is done through a mobile application then click on the gear symbol on the right side of the screen to open up an advanced menu.
- On the left side menu please find and select the section "Lora".
- On the newly opened window select the Servers tab.
- Click + to add a new server configuration.
- A new window will appear and you will have to enter:
Name: (Server name)
Address: (Server address)
Up port: (Usually it's 1700)
Down port: (Usually it's 1700)

- Click OK to save.
**Second step:**

- Select the Device tab on the previous window.
- Double-click or tap on the line to configure.
- Choose the previously entered network on the drop-down menu.
- Click on the button Enable to enable the gateway.
- Click OK to save.
- The configuration is done.
For more detailed information on LoRa settings, check the guide over here.

The configuration example, for both UDP and LNS scenarios with The Things Stack server, can be found here.

We recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: https://mt.lv/help In case IP connection is not available, the WinBox tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

![](../img/worddav90b536202301fa410028bd0e2ac949b9.badge.webp)

- Scan the QR code and choose your preferred OS.
- Install and open the application.
- By default, the IP address and user name will be already entered.
- Click Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and the application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Antenna usage

We recommend using an external antenna, which can be obtained separately, like our "LoRa omni antenna". The antenna has a pole mount and cable ready to use with LR cards - https://mikrotik.com/product/915_omni_antenna
The SMA connector located under the bottom door is already connected to the LR card and ready to be used. Please see the section on how to remove the door.

Please connect and disconnect the antenna, when the device is turned off!

**Internal antenna** 2 dBi can be used for setups where the distance to the gateway is closer than 1km. By default, the antenna is not connected to the card! To use an internal antenna:

- Open the bottom door (see "").

![](../img/worddavf67a4b9754755d04092c86219cdb377a.webp)

- Use the PH2 screwdriver to remove the screw.
- Disassemble the upper case from the bottom by sliding them to opposite sides.

![](../img/worddav8f16e9c2ada96b6e6050e385c459f37d.webp)

- Locate the internal antenna cable and attach it to the LR card (connector labeled "RFIO"):

![](../img/image-2025-5-27_16-0-54.webp)

- The other connector (labeled "GPS"), is used for connecting GPS antennas.
- Reassembly.

## Buttons and jumpers

The reset button has three functions:

- Hold this button during boot time until the LED light starts flashing, and release the button to reset the RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total of 10 seconds).
- Or Keep holding the button for 5 more seconds until the LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

The package includes the following accessories that come with the device:

- EU/US Switching Power Supply 24 V ⎓, 0.8 A, 19.2 W, 85.3 %, VI, cable:150 cm Hor CMC.
- WAP desk bracket.
- WAP outdoor case bracket AL, white.
- POE Injector cable.
- Cable (H4130-04PDB000R 3 mm 2x2P Housing) to (StripJacket 5 cm+WireEnd Strip/Tin 1 cm) 24 AWG.
- Hose Clamp, 35-70 mm, W4.
- K-52 fastening set.
- WAP-drill-template, paper brochure.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.
RouterOS LR support is limited to MikroTik LR cards, it does not support 3rd party Lora cards.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.
