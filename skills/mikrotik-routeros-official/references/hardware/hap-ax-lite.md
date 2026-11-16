# hAP ax lite

> Gen6 wireless on a budget – tiny, fast, and strong enough to harvest the power of RouterOS v7! See the hAP ax lite product page for full specifications and brochures.

![](./img/api_l41g-2axd.jpg)

## [hAP ax lite](https://mikrotik.com/product/hap_ax_lite) (L41G-2axD)

Gen6 wireless on a budget – tiny, fast, and strong enough to harvest the power of RouterOS v7! See the [hAP ax lite product page](https://mikrotik.com/product/hap_ax_lite) for full specifications and brochures.

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
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

## Setup

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

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

![](../img/worddav90b536202301fa410028bd0e2ac949b9.badge.webp)

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Click Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Powering

The device accepts power in the following ways:

- USB type C accepts 5 V DC⎓.
The power consumption under maximum load can reach 8 W.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: https://mt.lv/help In case IP connection is not available, the WinBox tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see the [Reset button](#reset-button).

## Mounting

The device is designed to be used indoors and placed on a flat surface with all needed cables connecting to the front of the unit.
The IP rating scale of this device is IPX0. We recommend using Cat6 shielded cables.
Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.

## Extension slots and ports

- Product code: L41G-2axD.
- CPU: Dual-Core IPQ-5010 1 GHz.
- CPU architecture: ARM.
- Size of RAM: 256 MB.
- Storage: 128 MB, NAND.
- Number of 1G Ethernet ports: 4.
- Switch chip model: MT7531BE.
- Wireless band: 2.4 GHz.
- Wireless interface model: IPQ-5010.
- Wireless 802.11b/g/n/ax: dual-chain.
- Wireless antenna max gain: 4.3 dBi.
- Dimensions: 124 x 100 x 54 mm.
- Operating system: RouterOS v7, License level 4.
- Operating temperature: -40°C to +70°C.

## Reset button

The reset button has three functions:

- Hold this button during boot time until the green LED light starts flashing, release the button to reset RouterOS configuration.
- Keep holding the reset button until the LED turns solid, then release it to enable CAP mode. The device will then start searching for a CAPsMAN server.
- To reinstall RouterOS using the [Netinstall](../docs/tags/netinstall) utility, enter the device into BOOTP mode. Two booter options are available: the **Regular Booter** and the **Backup Booter**. It is recommended to verify both options in case one does not work.
  - **Regular Booter:** To enter etherboot mode, press the **Reset** button after powering on the device and waiting 1–2 seconds.
  - **Backup Booter:** Power off the device. Press and hold the **Reset** button, then power on the device. Wait for the **LED** sequence (blinking → steady → off), then release the button. The device will boot into **BOOTP** mode, ready for RouterOS reinstallation via **Netinstall**. Depending on the model, this may be indicated by the **USR, USER, System**, or **ACT** LED, or by the SFP port LED.

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

- 5V 2.4A 12W USB power adapter

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.
