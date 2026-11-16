# R11e-LR9

> R11e-LR9 - LR mPCIe Gateway module. It can be integrated into a RouterBOARD product with mPCIe slot. Requires Lora package installation to configure in RouterOS.

![](./img/api_r11e-lr9.webp)

R11e-LR9 - LR mPCIe Gateway module. It can be integrated into a RouterBOARD product with mPCIe slot. Requires Lora package installation to configure in RouterOS.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- The Installation of the equipment must comply with local and national electrical codes.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 29 centimeters from your body, occupational user, or the general public.

## Specifications

Low power-consuming with mini PCIe interface, for long-distance data, transmit:

- Interface – Mini-PCIe;
- Temperature Operating -40 / +70;
- Supports Class A and C;
- Frequency - 902-928MHz (US);
- RF Output power - 902-928MHz (US) @ 20dBm;
- *Receive max sensitivity - 137 dB @ SF12, Depends on the antenna used;*
- *Maximum power consumption 2 W.*

## Installing the module in your device

R11e-LR9 for professional use. Each of the cards comes in ESD protective packaging. When handling electrical equipment please observe the following safety precautions:

- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage;
- After unpacking please place the card on the anti-static mat;
- When installing make sure there are no objects that can damage or touch the PCB plate;
- The card can be installed in your desired device using the factory provided screw holes in a PCB plate;
*Pictures added for illustration purposes, the device configuration, and the placement of the miniPCIe card may vary.*

- Locate miniPCIe slot on your device;
- Unscrew two factory attached screws;

![](../img/worddav858d70e514f5f460711d36395eb0db47.webp)

![](../img/worddav20cbdaef825269f3f18d531047ca6ce5.webp)

- Optionally you can use the thermal pad by placing it under the card, the thermal pad is not included in the package;
- Install the module to the miniPCIe slot and secure it with previously removed screws. Tightening torque 0,3 Nm.

![](../img/worddav1bf0c4f4ae96a27e4f57fd4fd3359c7a.webp)

## Connecting to the antenna

If your device does not have internal antennas, it is possible to connect to the external antennas by adding cable connectors, product code — [ACSMAUFL](https://mikrotik.com/product/acsmaufl). Please connect and disconnect the antenna, when the device is turned off!

![](./img/worddav85027cfdafde63daba8ed361a5d5b66c.webp)

- Attach antenna cable to the connector on the module:

When installing outdoors please ensure that the device case is waterproof and is designed for outdoor use. The IP rating scale for this device is IP0.
*Mounting and configuration of this device should be done by a qualified person.*

## Configuration for RouterOS

To set the configuration for LR please connect to the device and log in with your web browser, WinBox or mobile application. Two easy steps to follow:
**First step:**

- Once logged in, Quick Set will be selected, please switch to WebFig on the right side of the screen. If the configuration is done through mobile application then click on the gear symbol on the right side of the screen to open up an advanced menu.
- On the left side menu please find and select the ion "Lora".
- On the newly opened window select the ers tab.
- Click + to add a w server configuration.
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

## Specifications

The module can be installed on the miniPCIe to USB adapter and used in any of our devices with a USB slot and installed Lora package.

**To use it in other devices, packet forwarder from Semtech is required:** [packet_forwarder](https://github.com/Lora-net/packet_forwarder)

## Pinout

| Pin # | Value |
| --- | --- |
| 2 | 3V3 |
| 4 | GND |
| 9 | GND |
| 15 | GND |
| 18 | GND |
| 21 | GND |
| 22 | PERST# (not used in RouterOS) |
| 24 | 3V3 |
| 26 | GND |
| 27 | GND |
| 29 | GND |
| 34 | GND |
| 35 | GND |
| 36 | USB_D- |
| 37 | GND |
| 38 | USB_D+ |
| 39 | 3V3 |
| 40 | GND |
| 41 | 3V3 |
| 43 | GND |
| 50 | GND |
| 51 | Reserved |
| 52 | 3V3 |

## Operating system support

The module supports RouterOS software version v6 and v7. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Federal Communication Commission Interference Statement

This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation.

![](../img/fcc.badge.webp)

This equipment generates, uses and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and receiver.
- Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help.
**FCC Caution:** Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate this equipment.
This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.
This device and its antenna must not be co-located or operation in conjunction with any other antenna or transmitter.

**IMPORTANT: Exposure to Radio Frequency Radiation.**

0,29m minimum distance has to be maintained between the antenna and the occupational user and 0,64m to the general public. Under such configuration, the FCC radiation exposure limits set forth for a population/uncontrolled environment can be satisfied.

**Antenna Installation WARNING**

It is the installer's responsibility to ensure that when using the authorized antennas in the United States (or where FCC rules apply); only those antennas certified with the product are used. The use of any antenna other than those certified with the product is expressly forbidden in accordance to FCC rules CFR47 part 15.204. The installer should configure the output power level of antennas, according to country regulations and per antenna type.

## OEM statement

This module is intended for OEM installations only. As such the OEM integrator is responsible for ensuring that the end-user has no manual instructions to remove install or modify the module. This module is limited to installations in mobile or fixed applications. OEM integrators may utilize antennas of like an equal or lesser gain as appearing in the list in this document (reference 47 CFR, paragraph 15.204(c)(4) for further information on this topic. The MikroTik OEM RF Module complies with Part 15 of the FCC rules and regulations.
The Grantee will provide guidance to the Host Manufacturer in ensuring compliance with the Part 15 Subpart B requirements.
OEM Modules have been certified by the FCC for use with other products without any further certification (as per FCC section 2.1091). Separate approval is required for other operating configurations including portable configurations with respect to 47CFR paragraphs 2.1093 and different antenna configurations. The OEM is required to comply with all 47CFR labeling instructions and requirements for the finished products.
Changes or modifications not expressly approved by MikroTik could void the OEM authority to install or operate the equipment. OEMs must test their final product to comply with unintentional radiators (FCC section 15.107 and 15.109) before declaring compliance with their final product to Part 15 of the FCC Rules.
**WARNING:** the OEM must ensure that the FCC labeling requirements are met. This includes a clearly visible label on the outside of the OEM enclosure specifying the appropriate MikroTik OEM RF Module FCC identifier for this product as well as any other required FCC notices as presented below.
This enclosed device complies with 47CFR paragraph 15 C of the FCC rules and regulations. Operation is subject to the following two conditions: (1) this device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.
Labeling and text information should be of a size of type large enough to be readily legible, consistent with the dimensions of the equipment and the label.
**WARNING:** This device has been tested with a MMCX connector and antennas as listed in the table below. When integrated into the OEM products, these fixed antennas require professional installation. Preventing end users from replacing them with non-compliant antennas.
Antennas of same type and lower gain than those listed above may be used in compliance with certification.

## Innovation, Science and Economic Development Canada

This device complies with Industry Canada licence-exempt RSS standard(s). Operation is subject to the following two conditions: (1) this device may not cause interference, and (2) this device must accept any interference, including interference that may cause undesired operation of the device.
Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, mźme si le brouillage est susceptible d'en compromettre le fonctionnement.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

## LE-LAN device restriction

LE-LAN devices are restricted to indoor operation only in the band 5150-5250 MHz. However, original equipment manufacturer (OEM) devices, which are installed in vehicles by vehicles manufacturers, are permitted;
Users should also be advised that high-power radars are allocated as primary users (i.e. priority users) of the bands 5250-5350 MHz and 5650-5850 MHz and that these radars could cause interference and/or damage to LE-LAN devices.
les dispositifs fonctionnant dans la bande de 5 150 ą 5 250 MHz sont réservés uniquement pour une utilisation ą l'intérieur afin de réduire les risques de brouillage préjudiciable aux systčmes de satellites mobiles utilisant les mźmes canaux
Les utilisateurs devraient aussi źtre avisés, d'une part, que les utilisateurs de radars de haute puissance sont désignés utilisateurs principaux (c.-ą-d., qu'ils ont la priorité) des bandes de 5 250 ą 5 350 MHz et de 5 650 ą 5 850 MHz et, d'autre part, que ces radars pourraient causer du brouillage et/ou des dommages aux dispositifs de RL-EL
This radio transmitter (identify the device by certification number or model number if Category II) has been approved by Industry Canada to operate with the antenna types listed below with the maximum permissible gain indicated. Antenna types not included in this list, having a gain greater than the maximum gain indicated for that type, are strictly prohibited for use with this device.
