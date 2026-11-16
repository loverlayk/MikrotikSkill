# Chateau LTE6

> The Chateau is a home router to be used with a cellular network provider sim card.

![](./img/api_d53g-5hacd2hnd-tc_eg06-a.jpg)

## [Chateau LTE6](https://mikrotik.com/product/chateau_lte6) (D53G-5HacD2HnD-TC&FG621-EA)

The Chateau is a home router to be used with a cellular network provider sim card.

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

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

## Quickstart

follow these quick steps to set up your device:

![](../img/worddav7baaa636a1fa9d377c8759957ef10026.webp)

- Connect your computer to one of the Ethernet ports;
- Optional - Connect an external antenna to the SMA connector (The antennas are not provided in the package, see "(link) for Micro sim card.
- Mode button.
- Cover for external (link)
- WPS (link)
- Integrated Wireless module operating at 2.4 GHz, 802.11b/g/n protocol.
- Integrated Wireless module operating at 5 GHz, 802.11a/n/ac protocol.

## Mounting

The device is designed to be used indoors, by placing it on the desktop.

You should use CAT5 shielded cable. When using and installing this device pay attention to the Maximum Permissible Exposure (MPE) safety distance with a minimum of 20 cm between the radiator and your body.

## Powering

The device accepts power from an adapter:

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin-positive plug) 12-28 V DC⎓.
The power consumption under maximum load can reach 15 W, with attachments 21 W.

## Configuration

You should check for updates frequently to receive the latest updates for your RouterOS software to ensure the best performance and stability.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: https://mt.lv/help In case IP connection is not available, the WinBox tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Mode button

Mode button is located on the back of the unit, to the right side (see "")
The Default configuration for the Mode button is dark mode - to turn off all LEDs. The button can be configured in RouterOS to run any user-specified scripts.

## Sync button

The sync button is located on the top of the unit. The WPS Sync button, if configured on the wireless interface, can be used to connect new clients.

![](../img/worddav5849550989789eb95a4b8e4d12bd44b3.badge.webp)

- Press and hold the WPS button for 1 – 5 seconds to enable WPS for wireless interfaces.

## Front LED status

![](../img/image2022-6-13_14-45.webp)

- Wireless network activity.
- Ethernet port activity.
- System LED with alternate mode for cellular modem status indication.
- Signal strength.

## System LED alternate modem mode indications

When cellular modem interface is enabled, System LED have have alternate indications:

blinking red - SIM card not inserted

yellow - established connection in 3G mode

blue - established connection in LTE mode

blinking - connection establishment in progress, modem registered in cellular network, APN is not activated yet

## SIM slot usage

![](../img/worddav1617cee4086cb64136be15fb67b20679.webp)

SIM card slot is designed to be used with Micro SIM cards.
Nano SIM cards have different thickness, and usage with an adapter are not recommended.

## Reset button

The reset button has three functions:

- Hold this button during boot time until the green LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total of 10 seconds).
- To reinstall RouterOS using the Netinstall utility, enter the device into BOOTP mode. There are two types of booters available: the regular booter and the backup booter.Regular booter - Power on the device, wait 1-2 seconds, then press and hold the Reset button. Wait until the System LED is blinking green, then turns solid "On". When the green LED turns "Off", release the Reset button - the device will enter BOOTP mode.
- Backup booter – Power off the device, press and hold the Reset button, then power it on. Wait until the System LED is blinking green, then solid "On". When the green LED turns "Off", release the Reset button - the device will enter BOOTP mode using the backup booter.
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

NetinstallWhen performing Netinstall, make sure to use the latest v7 version of both ROS files and the Netinstall software.

## Accessories

The package includes the following accessories that come with the device:

- EU/US Switching Power Supply 24 V ⎓, 1.2 A, 28.8 W, 86.8 %, VI, cable:150 cm.
- CAT5E UTP Flat Cable, 8P8C, AWG32, 1.5 m.

## LTE Antenna usage

SMA connectors are for LTE antennas.

The device has two external antenna connectors on the back behind the doors.

- Open doors by pulling them upwards.
- Screw the LTE antenna to the SMA connector located on the left side. The maximum diameter for antenna connectors or any other adapters used is 13 mm.

![](../img/worddavb8b9cee1c814bbd0bf653b6b36b5f0ee.webp)

When using one antenna, connect to the SMA connector on the left side (ANT1).
Only when using two antennas, you can connect to the right SMA connector (ANT4).

![](../img/worddavbe6f007cc2b0928447cca33a7c70953e.webp)

connect and disconnect the antenna, when the device is turned off!
SMA connectors on the device are female.

You should use our antenna https://mikrotik.com/product/mant_lte_5o

## Removing front cover to access PCB

In case there is a need to access PCB, the front cover can be removed.

- Remove center screw;
![](../img/image2021-4-20_14-1-27.webp)
- Use a small screwdriver to pry open cover in marked spots;
- Continue to pry it open by going up;
![](../img/image2021-4-20_14-5-54.webp)
- At the end lift off the whole cover.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, separate the device from household waste and dispose of it in a safe manner, such as at designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.
