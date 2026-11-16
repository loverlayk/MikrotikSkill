# netPower 16P

> The netPower is a weatherproof switch with the capability of delivering PoE to your connected devices. See the netPower 16P product page for full specifications and brochures.

![](./img/api_crs318-16p-2s_out.jpg)

### netPower 16P (CRS318-16P-2S+OUT)

The netPower is a weatherproof switch with the capability of delivering PoE to your connected devices. See the [netPower 16P product page](https://mikrotik.com/product/netpower_16p) for full specifications and brochures.

## Safety Warnings

Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
Ultimate disposal of this product should be handled according to all national laws and regulations.
The Installation of the equipment must comply with local and national electrical codes.
This product is intended to be mounted outdoors on a pole. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
Read the installation instructions before connecting the system to the power source.
We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik devices must be professionally installed.

## Quickstart

- Connect with your PC to any Ethernet port;
- Connect the device to a power source;
- Configure the IP settings of your network card to 192.168.88.2/24;
- Use WebFig in a web browser or the "WinBox" configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Open http://192.168.88.1 in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

## Extension slots and ports

![](./img/worddav158230ba80223c20f0fbc6e91631ee5d.webp)

- DC power connector 48 – 57 V.
- DC power connector 18 – 30 V.
- LED indicating a power state of the device.
- Reset button.
- Gigabit Ethernet, 8 - ports, delivering PoE out.
- Gigabit Ethernet, 8 - ports, delivering PoE out.
- Two - 10G SFP+ ports.
- LED Indicating the activity of SFP port.
- LED Indicating the speed of SFP port.

## Configuration

Full documentation for both RouterOS and SwOS is available at: https://mt.lv/help You can configure the device using WebFig in a web browser or the "WinBox" configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility.**
**To start setup, open http://192.168.88.1 in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker).
The device is equipped with an RS-232 serial port, set by default to 115200 bit/s, 8 data bits, 1 stop bit, no parity. For recovery purposes, it is possible to reinstall the device from the network, see the Reset button.

Marvell Prestera switch chip features user manual

The device supports booting either RouterOS (for full routing and switching functionality) or SwOS (for switch-only operation). By default, the device boots into RouterOS, but you can switch to the other operating system as follows:

- From SwOS: Go to the System menu and click the Boot RouterOS button at the bottom of the page.
- From RouterOS: Open System → RouterBOARD → Settings and select Boot OS.
It is also possible to choose the operating system and configure other boot options using the serial console menu.

## Powering

The device accepts power in the two ways following ways:

- Direct-input power jack 1, (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 18-30 V DC⎓.
- Direct-input power jack 2, 48-57 V DC ⎓.
Use included DC plug to connect with your power source:

![](./img/worddavad63d423800bf0910af086bfe88dc615.webp)

- DC plug 2.1x5.5x12 mm to Screw Terminal 2pin.
- Connect your power source cables to the two pins and secure them in place by tightening screws.
- Connect DC plug to the device.
The power consumption under maximum load can reach 21 W, with attachments 325 W.

## Power output

The device supports 802.3af/at PoE from Ethernet 1 - 16. You can power MikroTik devices which supports powering through Ethernet. The power delivered through the PoE port will depend on the incoming to the device.

- Max PoE-out on low (&lt;30 V) voltage 5.6 A (2.8 A per 8port group, max 1.1 A per port).
- Max PoE-out on high (>30 V) voltage 2.8 A (1.4 A per 8port group, max 0.6 A per port).
When using both the high and low Voltage adapters, the netPower will automatically choose the correct PoE standard and Voltage, based on the devices you connect to each port. This can also be specified manually.

### Connecting to a PoE Adapter, only to deliver power to other devices

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Bottom Lid

- Bottom lid is secured in place with the captive screw, it can be unscrewed by hand, but do not remove the screw completely.
- Pull the cover towards.
![](../img/worddav2075f2108eadfabe02671bc5d7327b4b.webp)
- Lift to access Ethernet ports.

## Mounting

The device can be mounted in several ways: pole, wall, or ceiling. The package also includes a drill hole template with detailed mounting instructions, to help you with the drill hole marking. The device has eight mounting points for versatility use zip ties or steel clamps for mounting on the pole.

The IP rating scale for this device is IP54. When mounting outdoors, please ensure that any cable openings are directed downwards.

![](../img/worddav781d05276d2263b81e8698dae35b0e23.webp)

 **Mounting points:**

- There are eight mounting points on the back of this device. Choose the most relevant ones.
- Middle points are designed for mounting on the mast, there are curves on the case for slim fitment.
It's recommended to secure Ethernet cable to the pole using zip ties. With the distance from the device approximately 30 cm.

The device must be mounted by UP arrow facing upwards.

The installation infrastructure (towers and masts), as well as the router itself, must be properly grounded. The device includes a grounding wire attachment screw on the backside.

- Attach your grounding wire to the grounding screw.
- Attach the other end of the grounding wire to the grounded mast.
Mounting and configuration of this device should be performed by a qualified person. **Mounting on the mast or pole:**

![](../img/worddavd92f2926c9db0a96115f5eeeebb17d8a.webp)

- Insert provided steel clamps into mounting spots.
- Attach the unit to the mast.
- Align the device and secure it by tightening steel clamps with a PH2 screwdriver.
- Guide Ethernet cables through the opening and connect to the Ethernet ports.
- Close bottom latch and secure with a screw.
**A – Always make sure to place the unit in an upwards position.** ***B - It's recommended to use electrical tape to increase friction between materials.*** **Mounting unit on the wall:**

- Use included a template to mark spots for drilling holes. Align accordingly, it will depend on how the device will be mounted finally.
![](../img/worddav3763ee5bb6a9fea332248fa396547e3a.webp)
- Insert dowels if needed, depends on wall structure and material.
- Insert screws and screw them by leaving approximately 1 cm out.
- Attach the unit to the position.
- Use screw holes under the bottom cover and tighten to secure in place. Extend your Ethernet cables through the openings and connect to Ethernet ports.
- Close bottom latch.
Carefully check the wall for electric cables before drilling mounting holes.

## Buttons and jumpers

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when a green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and bridge all interfaces.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

- DC plug 2.1x5.5x12 mm to Screw Terminal 2pin AWG14-20 Adapter.
- Hose Clamp SUS304.
- K-66 fastening set.
- OED-drill-template, paper brochure.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Federal Communication Commission Interference Statement

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation.

![](../img/fcc.badge.webp)

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense.

FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate this equipment.
This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.
Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

## Innovation, Science and Economic Development Canada

This device complies with Industry Canada's license-exempt RSS standard(s). Operation is subject to the following two conditions: (1) this device may not cause interference, and (2) this device must accept any interference, including interference that may cause undesired operation of the device.
Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

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
