# LHG XL 5 ax

> Long-range outdoor CPEs with modern Wi-Fi 6 performance, rugged design, and unbeatable pricing. Available in two models (24.5 or 27 dBi), they’re ideal for point-to-point links over great distances. This is the XL 27...

![](./img/api_lhg-5axd-xl.jpg)

## [LHG XL 5 ax](https://mikrotik.com/product/lhg_5_ax_xl) (LHG-5axD-XL)

Long-range outdoor CPEs with modern Wi-Fi 6 performance, rugged design, and unbeatable pricing. Available in two models (24.5 or 27 dBi), they’re ideal for point-to-point links over great distances. This is the XL 27 dBi version. See the [LHG XL 5 ax product page](https://mikrotik.com/product/lhg_5_ax_xl) for full specifications and brochures.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- The Installation of the equipment must comply with local and national electrical codes.
- This product is intended to be mounted outdoors on a pole. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

- To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Assembly and Mounting

- Attach the two legs to the LHG case.
![](../img/image2021-7-22_10-59-3.webp)
- Snap the assembled LHG unit to the grid in the appropriate locations.
- Fix the legs in place with two self-thread screws (Use Phillips screwdriver PH2).
![](../img/image2021-7-22_11-1-5.webp)

The device is designed to be mounted on the pole using zip ties or steel clamps as shown in the picture. The clamping diameter with provided steel clamps is 35 – 70 mm.

![](../img/image2021-7-22_10-56-42.webp)

- Guide provided steel clamps through the unit.
- Attach the device to the pole.
- Align and tighten the clamps to secure the device.Optional: If required, before mounting the unit, you can insert the included 5-degree adjustment adapter into the top or bottom slot where the mounting ring is inserted. This will create an additional upward or downward angle when the unit is tightened to a vertical pole.

![](../img/worddav0145d1f797f63ac04a8fcff37dee1617.webp)

The device includes a grounding connection (marked ⏚) which you should connect to the grounding installation of the tower or building where the device will be used. This is to substantially reduce the risk of ESD and lightning damage.
Warning! This equipment should be installed and operated with a minimum distance of 40 cm between the device and your body. The operation of this equipment in the residential environment could cause radio interference.

Connect the Ethernet cable to the Ethernet port located under the door and guide through the leg as shown in the picture:

![](../img/image2021-7-22_11-6-14.webp)

Additional mounting brackets can be purchased separately:

LHG mount

![](../img/image-2025-8-11_16-55-42.webp)

solidMOUNT

![](../img/image-2025-8-11_16-56-0.webp)

## Quickstart

- Connect the device to the included PoE injector with an Ethernet cable to the data+power end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Configure your device using a web browser through **WebFig** or the **WinBox** tool at https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Access **WebFig** by opening http://192.168.88.1, and for **WinBox**, download the tool, navigate to the **Neighbors** tab, and click on the MAC address. The username is "**admin**" with no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- In the "Quick Set" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

## Powering

The device accepts powering only from Passive PoE injectors.
PoE in input Voltage: 12-28 V.

## Extension slots and ports

- One Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- One integrated wireless device with a built-in grid antenna.

## Buttons and jumpers

The reset button has three functions:

- Reset RouterOS configuration - Hold the button during boot until the USR LED light starts flashing, then release it to reset the configuration (about 5 seconds).
- Enable CAP mode. Keep holding for 5 more seconds (total 10 seconds) until the USR LED turns solid, then release to turn on CAP mode. The device will now search for a CAPsMAN server.
- Reinstall RouterOS using Netinstall (BOOTP mode). Two types of booters are available:Regular booter - Power on the device, wait 1-2 seconds, then press and hold the Reset button. Wait until the USR LED is blinking and then turns solid ON. When the USR LED turns OFF, release the Reset button - the device will enter BOOTP mode.
- Backup booter - Power off the device, press and hold the Reset button, then power it on. Wait until the USR LED is blinking and then turns solid ON. When the USR LED turns OFF, release the Reset button - the device will enter BOOTP mode using the backup booter.
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.
