# GPeRx4

> Effortlessly split a single high-power PoE port into multiple standard PoE connections with the compact and durable GPeR14i. Expand, extend, and power your network with ease!

![](./img/api_gper14i.jpg)

Effortlessly split a single high-power PoE port into multiple standard PoE connections with the compact and durable GPeR14i. Expand, extend, and power your network with ease!

## Safety Warnings

Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
This product is intended for outdoors. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.

## Connecting

- Unlock the enclosure by simultaneously pressing the buttons located on both sides of the lower case, and then proceed to remove the cover from the device;
- Thread the cables through the rubber seal located on the underside of the case;
- Connect your desired network cable with power to the PoE in the Ethernet port, and extend it through the PoE out ports;
- Connect the cable to the next device or another GPER14i unit;

## Powering

This device offers two distinct power supply options:

- The First Ethernet port is a PoE-in that supports 802.3bt and accepts DC voltage in the range of 48 to 57V⎓.
- The two-pin connector is compatible with DC voltage in the range of 24 to 57V⎓.
- You can power up an additional GPER14i unit using the two-pin connector. To achieve this, connect the device to the two-pin connectors of another GPER14i unit, and ensure that the SwOS Lite System's "Power I/O" option is configured as "Output." To enable this operation, the device itself must be powered via PoE-in.
Outgoing power WarningPlease ensure that the device's power consumption does not exceed the incoming power capacity of the power-feeding device, taking into account its current load.

Max power consumption: 115W. It is important to note that all other ports are limited to 30W power consumption

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.
Connecting the two-pin connector:

- Attach the positive wire to the + slot.
- Attach the negative wire to the - slot.

## Grounding

The grounding wire should be connected to the RouterBOARD grounding wire attachment point. This wire should then be connected to the base of the installation location, ensuring the connection meets grounding standards. The grounding screws M4 are not included.

## Mounting

The device is designed for use outdoors, the IP rating scale for this device is IP68. It is possible to attach the device on the pole, using the provided screw hole on the mounting bracket of the unit.

Recommended using Cat5/6 cable.
*Mounting and configuration of this device should be done by a qualified person.*

## Extension slots and ports

- 1 PoE-in 802.3bt Gigabit Ethernet port.
- 3 PoE-out 802.3af/at Gigabit Ethernet ports.
- 1 two-pin connector DC power voltage slot in the range of 24 to 57V⎓.

## LED status

The device's LED indication can only be seen with an open case.

- DC-in status LED.
- DC-out status LED.
- The Ethernet port active status LED.
- The PoE-out status LED

## The Reset button

The reset button is located on the plate, and can be used with an opened case. Hold this button until DC-in LED light starts flashing, release the button to reset configuration to default.

## Accessories

The package includes the following accessories that come with the device:

- Mounting bracket with screw and dowel.

## Specifications

Dimensions: H x W x D, mm: 280 x 75 x 70 mm

![](./img/sliding_enclosure-01.webp)

![](./img/sliding_enclosure-03.webp)

![](./img/sliding_enclosure-02.webp)

For more information about this product, specification, and pictures, please visit our web page: https://mikrotik.com/product/gper

## Configuration

This device operates on the SwOS Lite operating system.

- Set your IP for PC to 192.168.88.2/24;
- Connect your PC to any unused Ethernet port;
- Open your web browser, the default IP management address is 192.168.88.1, with username: **admin** and no password (or, for some models, check user and wireless passwords on the sticker);
- Download the latest version of SwitchOS Lite software from https://mikrotik.com/download;
- Upload a file with the web browser in the Upgrade tab, the device will reboot after the upgrade;
- Set up your password to secure the device.

## Federal Communication Commission Interference Statement

This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation.

![](../img/fcc.badge.webp)

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and receiver.
- Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help.
FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

## Innovation, Science and Economic Development Canada

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

## UKCA marking

![](../img/ukca.badge.webp)

## Eurasian Conformity Mark

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: MikroTikls SIA, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. Cм. на упаковке.

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

![](../img/eac.badge.webp)

## Norma Oficial Mexicana

EFICIENCIA ENERGETICA CUMPLE CON LA NOM-029-ENER-2017.

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.
Fabricante: MikroTikls SIA, Unijas iela 2, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## CE Declaration of Conformity

Manufacturer: MikroTikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

The full text of the EU declaration of conformity is available at the following internet address: https://mikrotik.com/products
