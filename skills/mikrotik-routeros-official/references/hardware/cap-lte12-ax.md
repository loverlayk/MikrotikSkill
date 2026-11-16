# cAP LTE12 ax

> A powerful ceiling access point that offers true Wi-Fi 6 mobility for your pop-up business - now with a CAT12 LTE modem! See the cAP LTE12 ax product page for full specifications and brochures.

![](./img/api_capgi-5haxd2haxd_eg12-ea.jpg)

## [cAP LTE12 ax](https://mikrotik.com/product/cap_lte12_ax) (cAPGi-5HaxD2HaxD&EG12-EA)

A powerful ceiling access point that offers true Wi-Fi 6 mobility for your pop-up business - now with a CAT12 LTE modem! See the [cAP LTE12 ax product page](https://mikrotik.com/product/cap_lte12_ax) for full specifications and brochures.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- The Installation of the equipment must comply with local and national electrical codes.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity or hot environments.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Use this product with care and operate at your own risk!
- In the case of device failure, disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 30 centimeters from your body, occupational user, or the general public.

## Quickstart

follow these quick steps to set up your device:

- Insert the micro SIM card into the slot;
- The IMEI number can be found on the case and packaging labels;
- Connect the device to the included PoE injector with an Ethernet cable to the *"data+power"* end;
- Connect to the device through either one of the Ethernet ports or the wireless network "MikroTik-..." (ensure to check the wireless passwords on the sticker);
- Establish a connection using a mobile application. Alternatively, use WebFig in a web browser or the "WinBox" configuration tool at https://mt.lv/winbox Start configuration within the chosen tool, using the default IP address 192.168.88.1. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device;
- Proceed to connect using the MAC address. The username is "admin," and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Select the "Check for updates" button and update RouterOS to the latest version. Must have a valid SIM card inserted and active Internet connection;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the "QuickSet" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

## Powering

- Number of DC inputs: 2 (DC jack, PoE-IN);
- Supported input voltage 18-57 V (DC jack) 18-57 (PoE-In)
- PoE-in 802.3af/at: Ether1;
- PoE-Out Passive PoE up to 57V (&lt;30v DC jack must be used, >30V PoE-In and DC jack can be used)
- PoE-Out port: Ether2, max out per port output (input &lt; 30 V): 0.6 A, max out per port output (input > 30 V): 0.4 A. Over 0.3 A current, use a DC jack for powering the device.
- Max power consumption (without attachments) 13 W
- Max power consumption 34 W

## Mounting

It is possible to attach the device to a wall or ceiling, using the provided mounting bracket on the back of the unit:

- Attach the mounting bracket to the wall or ceiling with provided screws;
- Use drill bit if necessary with provided dowels;
- Connect needed cables to the device;
- Attach the device to the mounting bracket by sliding.
![](./img/image-2024-12-27_14-55-37.webp)

*Mounting and configuration of this device should be done by a qualified person.*
Warning! This equipment should be installed and operated with a minimum distance of 30 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.

## Configuration

By default, the device is configured as a wireless access point, with the LTE interface as WAN, Ether1, Ether2 interfaces are bridged together with the wireless interface. A DHCP server is configured on the bridge interface.
Once logged in, you should select the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, make sure you have selected the country where the device will be used, to conform with local regulations. Must have a valid SIM card inserted and active Internet connection.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: https://mt.lv/help If an IP connection is unavailable, the WinBox tool (https://mt.lv/winbox) can be used to connect to the device's MAC address from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see the section .

## Extension slots and ports

- Product code: cAPGi-5HaxD2HaxD&EG12-EA
- CPU: Quad core IPQ-6010 1.8 GHz
- Size of RAM: 1 GB
- RAM type: DDR3L
- Storage: 128 MB, NAND
- Number of 1G Ethernet ports: 2
- Switch chip model: IPQ-6010
- Wireless interface model: QCN-5022 (2.4 GHz), QCN-5052 (5 GHz)
- Wireless 2.4 GHz 802.11b/g/n/ax dual-chain, 5 GHz 802.11a/n/ac/ax dual-chain
- Antenna gain: 5.5 dBi
- 3G Category: R8 (42.2Mbps Downlink, 11.2Mbps Uplink)
- 3G Bands: 1 (2100MHz) / 3 (1800MHz) / 5 (850MHz) / 8 (900MHz)
- LTE category: 12 (600Mbps Downlink, 150Mbps Uplink)
- LTE modem: EG12-EA
- LTE FDD bands: 1 (2100MHz) / 3 (1800MHz) / 5 (850MHz) / 7 (2600MHz) / 8 (900 MHz) / 20 (800MHz) / 28 (700MHz)
- LTE TDD bands: 38 (2600MHz) / 40 (2300MHz) / 41 (2500MHz)
- TAC: 86056104
- Number of SIM slots: 1 Modem (Micro SIM)
- Operating system: RouterOS v7, License level 4
- Dimensions: 228 x 48 mm
- IP: 20
- Operating temperature: -40°C to +70°C tested

## Buttons and jumpers

## Reset button

The reset button has three functions:

- Hold this button during boot time until the LED light starts flashing, and release the button to reset the RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, the LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until the LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Mode button

![](../img/image-2023-4-4_15-1.webp)

The action of the mode buttons can be configured from RouterOS software to execute any user-supplied RouterOS script. You can also disable this button. By default, the buttons will enable "dark mode", which disables LED lights. The mode button can be configured in the RouterOS menu /system routerboard mode-button.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

![](../img/worddav90b536202301fa410028bd0e2ac949b9.badge.webp)

- Scan the QR code and choose your preferred OS.
- Install and open the application.
- By default, the IP address and user name will be already entered.
- Select Connect to establish a connection to your device through a wireless network.
- Choose Quick Setup and the application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Accessories

The package includes the following accessories that come with the device:

![](./img/image-2024-12-27_15-14-33.webp)

To avoid pollution of the environment, separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.
