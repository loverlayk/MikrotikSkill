# RBM11G

> OEM board with a Gigabit Ethernet port and a miniPCIe slot for an 802.11 wireless card or a 3G/LTE modem. See the RBM11G product page for full specifications and brochures.

![](./img/api_rbm11g.webp)

## [RBM11G](https://mikrotik.com/product/m11g)

OEM board with a Gigabit Ethernet port and a miniPCIe slot for an 802.11 wireless card or a 3G/LTE modem. See the [RBM11G product page](https://mikrotik.com/product/m11g) for full specifications and brochures.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- All installation methods for mounting an access point on any wall surface is subject to the acceptance of local jurisdiction.
- The Installation of the equipment must comply with local and national electrical codes.
- This product is intended to be mounted outdoors on a pole but can also be installed indoors. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

## First use

- Insert the miniPCIe card (not included).
- (Optional) Install the device in a case.
- Connect antenna cables to the miniPCIe card and an Ethernet cable to the Gigabit Ethernet port.
- Plug in the power cable to turn on the device.
- Connect to the device using WinBox with a default IP address of 192.168.88.1 and the username `admin` and no password (or, for some models, check user and wireless passwords on the sticker).

## Mounting

M11G router for professional use. Each of the devices comes in ESD protective packaging. When handling electrical equipment please observe the following safety precautions:

- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage.
- After unpacking, place the router on the anti-static mat.
- When mounting the unit, make sure there are no objects that can damage or touch the PCB plate.
- Note that the ETH and DC jack are extending over the perimeter of the PCB plate.
The device can be mounted in your desired location using the factory provided four holes in a PCB plate, located on each side of the device.

## MiniPCIe slot

Installing a miniPCIe module should be done by a qualified person, please follow safety precautions when handling electrical equipment:

- Place the device on the anti-static mat.
- Locate the miniPCIe slot and remove the two factory attached screws.
- Attach the provided thick thermal pad to the card, and install the card into the miniPCIe slot so that the thermal pad is between the PCB and the card.
- Secure the card in place using the previously removed two screws.
- Attach the grey uFL connector to the MAIN antenna connector of the modem, attach the black cable to the secondary (or AUX) connector.
- Attach a thinner thermal pad to the top of the card.
- Mount the unit in your desired location.
After you mount the device, slide in the SIM card from your mobile operator into the SIM slot, with the chip facing down. The slot accepts miniSIM (2FF).

## Powering

The device accepts power with the following modes:

- Passive 10-30 V PoE to the Ethernet port. The higher voltage is needed to compensate for power loss on long cables. At least 18 V is suggested.
- Direct input to the power jack 10-30 V.
Maximum power consumption is 11 W.

## Booting process

RouterOS is the operating system of all RouterBOARD routers. Please see documentation here: https://mt.lv/help This device is not preconfigured other than an IP address on the Ethernet port. Another configuration has to be applied according to the documentation manual linked above.
The initial connection has to be done via the Ethernet cable, using the MikroTik WinBox utility. WinBox should be used to connect to the default IP address of 192.168.88.1 with the username `admin` and no password.
In case you wish to boot the device from the network, for example, to use MikroTik Netinstall, hold the reset button of the device when starting it until the LED light turns off, and the device will start to look for Netinstall servers.
In case the IP connection is not available, the WinBox utility can also be used to connect to the MAC address of the device. More information in the documentation.

## Extension slots and ports

- One Gigabit Ethernet port (with Auto MDI/X, so you can use either straight or crossover cables for connecting to other network devices). The Ethernet port accepts 10-30 V DC powering from a passive PoE injector.
- One miniPCIe slot for either an 802.11 wireless card or a 3G/LTE modem. A SIM slot is available for miniPCIe 3G/LTE modems and has no functionality when a modem is not installed.

## Specifications

| Parameters | Description |
| --- | --- |
| **Product Code** | RBM11G |
| **Architecture** | MMIPS |
| **CPU** | MT7621A, 2 core, 880 MHz |
| **RAM** | 256 MB |
| **Storage** | 16 MB, FLASH |
| **Operating System** | RouterOS (license level 4) |
| **10/100/1000 Ethernet ports** | 1 |
| **SIM slots** | 1 × Mini SIM |
| **miniPCIe slots** | 1 |
| **Number of DC inputs** | 2 (DC jack, PoE-in) |
| **PoE-in** | Passive PoE, 10-30 V |
| **DC jack input voltage** | 10-30 V |
| **Max power consumption** | 11 W |
| **Cooling type** | Passive |
| **Dimensions** | 105 × 110 mm |
| **Operating temperature** | -40 °C to +70 °C |
| **MTBF** | Approximately 100,000 hours at 25 °C |
| **Certification** | CE, EAC, ROHS |

For more information about this product, specification and pictures please visit our web page: https://mikrotik.com/product/m11g

## Reset button

The reset button has three functions:

- Hold this button during boot time until the LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode (total 10 seconds).
- Keep holding the button for 5 more seconds until the LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

![](../img/worddavec48bf5aa3b860afa9fcb97cf4aca652.webp)

![](../img/worddavea6671dfbffe714b2f3abe6d04e7ad04.badge.webp)

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Federal Communication Commission Interference Statement

This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation.

![](../img/fcc.badge.webp)

This equipment generates, uses and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and receiver.
- Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help.
**FCC Caution**: Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate this equipment.
This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.
Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

## Innovation, Science and Economic Development Canada

This device complies with Industry Canada licence-exempt RSS standard(s). Operation is subject to the following two conditions: (1) this device may not cause interference, and (2) this device must accept any interference, including interference that may cause undesired operation of the device.
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

Manufacturer: MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV-1039.

The full text of the EU declaration of conformity is available at the following internet address: https://mikrotik.com/products
