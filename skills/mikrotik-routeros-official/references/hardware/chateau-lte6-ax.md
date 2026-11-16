# Chateau LTE6 ax

> The Chateau is a home router to be used with a cellular network provider sim card. See the Chateau LTE6 ax product page for full specifications and brochures.

![](./img/api_s53ug_5haxd2haxd-tc_fg621-ea.webp)

## [Chateau LTE6 ax](https://mikrotik.com/product/chateau_lte6_ax) (S53UG+5HaxD2HaxD-TC&FG621-EA)

The Chateau is a home router to be used with a cellular network provider sim card. See the [Chateau LTE6 ax product page](https://mikrotik.com/product/chateau_lte6_ax) for full specifications and brochures.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- The Installation of the equipment must comply with local and national electrical codes.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity, or hot environments.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Use this product with care and operate at your own risk!
- In the case of device failure, disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

## Quickstart

follow these quick steps to set up your device:

![](../img/worddav7baaa636a1fa9d377c8759957ef10026.webp)

- Connect your computer to one of the Ethernet ports;
- Optional - Connect external antennas to the SMA connector (The antennas are not provided in the package, see "");
- Insert a micro SIM card into the slot located under the device;

![](../img/worddav3516d54390ed95be0ac48ad263d97ab1.webp)

- Connect the power adapter to the DC jack;
- Once the device is powered on and the PC is connected to the device, open http://192.168.88.1 in your web browser to start the configuration;
- User name: a*dmin* and there is no password by default you will be logged in automatically to the Quick Set screen (or, for some models, check user and wireless passwords on the sticker);
- Update the device by selecting the (*Check_for_updates*) on the right side and updating your RouterOS software to the latest version. Must have a valid SIM card inserted;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the (**WebFig**) (**Files**) menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- To personalize your wireless network, SSID can be changed in the fields "Network Name";
- In the (**QuickSet**) menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the field "WiFi Password" the password must be at least eight symbols;
- Set up your router password in the bottom field "Password" to the right and repeat it in the field "Confirm Password", it will be used to log in next time;
- Select the "Apply Configuration" to save changes.

## Connecting with a mobile app

Use your smartphone to access your router through WiFi.

![](../img/worddav90b536202301fa410028bd0e2ac949b9.badge.webp)

- Insert the SIM card and power on the device.
- Scan the QR code with your smartphone and choose your preferred OS.
- Connect to the wireless network. SSID starts with MikroTik and has the last digits of the device's MAC address.
- Open application.
- By default, the IP address and user name will be already entered.
- Select Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and the application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Specifications

- Product code S53UG+5HaxD2HaxD-TC&FG621-EA
- CPU Quad-Core IPQ-6010 1.8 GHz
- CPU architecture ARM 64bit
- CPU core count 4
- Size of RAM 1 GB
- RAM type DDR3L
- Storage 128 MB, NAND
- Number of 1G Ethernet ports 4
- Number of 2.5G Ethernet ports 1
- USB 1 USB 2.0 port type A
- Switch chip model IPQ-6010
- Wireless 2.4 GHz 802.11b/g/n/ax dual-chain, 5 GHz 802.11a/n/ac/ax dual-chain
- Wireless antenna max gain 2.4 GHz - 2 dBi, 5 GHz - 4 dBi
- Antenna beam width 360°
- LTE category 6 (300Mbit/s Downlink, 50Mbit/s Uplink)
- LTE modem FG621-EA
- TAC 86335904
- MIMO DL 2x2
- MIMO UL 1x1
- LTE FDD bands 1 (2100MHz) / 3 (1800MHz) / 5 (850MHz) / 7 (2600MHz) / 8 (900 MHz) / 20 (800MHz) / 28 (700MHz)
- 3G Category R8 (42.2Mbps Downlink, 11.2Mbps Uplink)
- 3G Bands 1 (2100MHz) / 3 (1800MHz) / 5 (850MHz) / 8 (900MHz)
- Dimensions 240 x 156 x 44 mm
- Operating system RouterOS v7, License level 4
- Operating temperature -40°C to +70°C

## Mounting

The device is designed to be used indoors, by placing it on the desktop.

You should use CAT5 shielded cable. When using and installing this device pay attention to the Maximum Permissible Exposure (MPE) safety distance with a minimum of 20 cm between the radiator and your body.

## Powering

The device accepts power from an adapter:

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) 12-28 V DC⎓.
The power consumption under maximum load can reach 13 W, with attachments 17 W.

## Configuration

You should check for updates frequently to receive the latest updates for your RouterOS software to ensure the best performance and stability.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: https://mt.lv/help In case IP connection is not available, the WinBox tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see the section .

## Mode button

The Mode button is located on the back of the unit, to the right side (see "")
The Default configuration for the Mode button is dark mode - to turn off all LEDs. The button can be configured in RouterOS to run any user-specified scripts.

## Sync button

The Sync button is located on the top of the unit. The WPS Sync button, if configured on the wireless interface, can be used to connect new clients.

![](../img/worddav5849550989789eb95a4b8e4d12bd44b3.badge.webp)

- Press and hold the WPS button for 1 – 5 seconds to enable WPS for wireless interfaces.

## Front LED status

![](../img/image2022-6-13_14-45.webp)

- Wireless network activity.
- Ethernet port activity.
- System LED.
- Signal strength.
Cellular connection technology based on the System LED color:
Red: GSM
Yellow: 3G
Blue: LTE
Green: 5G NSA
Violet: 5G SA

When LTE is not connected to the network, the system LED will blink red to indicate that there is some issue with the LTE connection. If the LTE interface is intentionally disabled (not being used), the system LED will glow blue.

## SIM slot usage

![](../img/worddav1617cee4086cb64136be15fb67b20679.webp)

SIM card slot is designed to be used with Micro SIM cards.
Nano SIM cards have different thicknesses and usage with an adapter is not recommended.

## Reset button

The reset button has three functions:

- Hold this button during boot time until the green LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total of 10 seconds).
- To reinstall RouterOS using the Netinstall utility, enter the device into BOOTP mode. There are two types of booters available: the regular booter and the backup booter.Regular booter - Power on the device, wait 1-2 seconds, then press and hold the Reset button. Wait until the System LED is blinking green, then turns solid "On". When the green LED turns "Off", release the Reset button - the device will enter BOOTP mode.
- Backup booter – Power off the device, press and hold the Reset button, then power it on. Wait until the System LED is blinking green, then solid "On". When the green LED turns "Off", release the Reset button - the device will enter BOOTP mode using the backup booter.
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

NetinstallWhen performing Netinstall, make sure to use the latest v7 version of both RouterOS. Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates.

## Accessories

The package includes the following accessories that come with the device:

- EU/US Switching Power Supply 24 V ⎓, 1.2 A.
- CAT5E UTP Flat Cable, 8P8C, AWG32, 1.5m, Black color

## Antenna usage

SMA connectors are for LTE antennas.

External antenna sockets are located on the back of the device. Device comes with connected wireless antennas, LTE antennas are not provided within the package.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, separate the device from household waste and dispose of it in a safe manner, such as at designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.
