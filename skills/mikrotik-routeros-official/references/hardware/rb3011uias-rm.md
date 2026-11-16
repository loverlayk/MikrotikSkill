# RB3011UiAS-RM

> RB3011UiAS-RM is a rackmount wired router with ten Gigabit Ethernet ports, an SFP cage, USB 3.0, an LCD panel, and PoE-out on Ether10. See the RB3011UiAS-RM product page for full specifications and brochures.

![](./img/api_rb3011uias-rm.webp)

## [RB3011UiAS-RM](https://mikrotik.com/product/RB3011UiAS-RM)

RB3011UiAS-RM is a rackmount wired router with ten Gigabit Ethernet ports, an SFP cage, USB 3.0, an LCD panel, and PoE-out on Ether10. See the [RB3011UiAS-RM product page](https://mikrotik.com/product/RB3011UiAS-RM) for full specifications and brochures.

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
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik devices must be professionally installed.

## Quickstart

- Connect your Internet cable to port 1, and local network computers to ports 2-10;
- Choose your powering solution, please see [Powering](#powering);
- Connect the device to a power source;
- Configure your network card settings to obtain the IP address automatically using DHCP;
- Configuration should be made using **WebFig** in a web browser or the **WinBox** configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Open `http://192.168.88.1` in a web browser to start setup. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device. Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- Set up your router password.

## Powering

The device accepts powering from either the power jack or from the LAN1 Ethernet port:

- Direct-input power jack (5.5 mm outside and 2 mm inside diameter, female, pin positive plug) accepts 10-30 V DC ⎓ (overvoltage protection starts at 30 V).
- Eth1 port accepts 10-30 V DC ⎓ input (at the board; higher voltage needed to compensate for power loss on long cables) from non-standard (passive) Power over Ethernet injectors. The board does not support IEEE802.3af compliant 48 V power injectors.

The power consumption under maximum load can reach 30 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE port of the PoE adapter;
- Connect an Ethernet cable from your LAN to the LAN port of the PoE adapter, mind the arrows for data and power flow;
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Extension slots and ports

- Ten 10/100/1000 (Gigabit) Ethernet ports (Auto MDI/X).
- USB 3.0 type A.
- LCD panel.
- SFP port for SFP module.
- The Ether10 port supports PoE output with auto-detection, so non-PoE devices can be connected without damage. The PoE-out on Ether10 outputs approximately 2 V below the input voltage and supports up to 0.7 A, so the provided 24 V PSU will provide 22 V at 0.7 A on the Ether10 PoE port.

## Mounting

![](../img/worddavdcbcfbfbb5384f30180de01126c4ad1d.webp)

The device is designed for indoor use and can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Please attach rubber pegs on the bottom of the router if the desired placement is on the flat surface or use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown in the picture to the right;
- Place the device in the rackmount enclosure and align it with the holes so that the device fits conveniently;
- Tighten the screws to secure it in place.

The IP rating scale for this device is IPX0. The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
We recommend Cat5/6 cables for our devices.
*Mounting and configuration of this device should be done by a qualified person.*

Operating humidity can be from 5% to 95% non-condensing.

## Configuration

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting with the [RouterOS documentation](https://mt.lv/help) to get accustomed to the possibilities. In case an IP connection is not available, the **WinBox** tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default). For recovery purposes, it is possible to boot the device from the network, see the [Reset button](#reset-button).

## Reset button

To use the reset button, hold it and then turn on the device, while still holding the button.

- Release the button when the green LED starts flashing, to reset the RouterOS configuration. To not load the backup bootloader, you can start holding the button after power is already applied.
- Release the button after LED is no longer flashing (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network). You can also release the button at the time when the device has appeared on the Netinstall utility device list.

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

The package includes the following accessories that come with the device:

- EU/US Switching Power Supply DC ⎓ 24 V, 1.2 A, 28.8 W, 86.8%, VI, cable:220 cm.
- 1U rackmount bracket black.
- Fastening set for RB2011 rackmount case K-19 v3.

![](./img/image2020-3-2_13-53-56.webp)

Please see the [MikroTik SFP module compatibility table](/docs/wired-connections/mikrotik-wired-interface-compatibility).

## Specifications

For more information about this product, specifications and pictures please visit our web page: https://mikrotik.com/product/RB3011UiAS-RM

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Safety notice

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Federal Communication Commission Interference Statement

![](../img/fcc.badge.webp)

This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation.

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and receiver.
- Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help.

FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate this equipment.
This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.
Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

## Innovation, Science and Economic Development Canada

This device complies with Industry Canada's license-exempt RSS standard(s). Operation is subject to the following two conditions: (1) this device may not cause interference, and (2) this device must accept any interference, including interference that may cause undesired operation of the device.
Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

## UKCA marking

![](../img/ukca.badge.webp)

## Eurasian Conformity Mark

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: MikroTikls SIA, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. Cм. на упаковке.

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу. Информация об импортерах продукции MikroTik в Российскую Федерацию: https://mikrotik.com/buy/europe/russia

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

![](../img/eac.badge.webp)

## Norma Oficial Mexicana

EFICIENCIA ENERGETICA CUMPLE CON LA NOM-029-ENER-2017.

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.

Fabricante: MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## CE Declaration of Conformity

Manufacturer: MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

The full text of the EU Declaration of Conformity is available at the following internet address: https://mikrotik.com/products
