# MQS

> The MQS – Mobile Quick Setup is a tiny wireless device made to simplify MikroTik device configuration in the field.

The MQS – Mobile Quick Setup is a tiny wireless device made to simplify MikroTik device configuration in the field.

## Safety Warnings

Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
Ultimate disposal of this product should be handled according to all national laws and regulations.
The Installation of the equipment must comply with local and national electrical codes.
This unit is intended to be installed in the rackmount. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware or to follow the correct procedures could result in a hazardous situation to people and damage to the system.
This product is intended to be installed indoors. Keep this product away from water, fire, humidity or hot environments.
Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
Read the installation instructions before connecting the system to the power source.
We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

## Quickstart

- Power the device with USB, for example, from your laptop or a power bank.
- From your laptop or smartphone, connect to the MQS wireless network which starts with "RBMQS".
- The MQS by default has a DHCP server enabled on the wireless interface.
- The Management interface has an IP address 192.168.88.3. To avoid conflicts with other MikroTik devices.
- Open https://192.168.88.3 in your web browser to start configuration, there is no password and user name: admin (or, for some models, check user and wireless passwords on the sticker).
- The MQS does not have RouterOS software, its configuration possibilities are limited.

## LED indicators

![](./img/api_rbmqs.webp)

- The LED displays active POE.
- Displays an active connection of the Ethernet port.
- Displays the access point mode.
- Displays the station mode.
- User LED indicates that the device is currently in factory firmware, after the update it will no longer be active, to bring the device in factory firmware, hold reset button when booting and LED will light up again.
- The power LED indicates that the unit is receiving power.

## Mounting

If desired, the device can be mounted to with a zip tie through the opening on it's back, or with provided strap or with wall mounting bracket. The IP rating scale for this device is IPX0. To comply with health regulations, install and use this device at least 20cm away from your body.

## Powering

- MicroUSB port accepts 5 V powering.
- Ethernet port accepts passive Power over Ethernet 12-28 V DC (compensate for the loss on cable, so more than 12 V recommended).
The power consumption under maximum load can reach up to 7 W, without attachments 1 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the POE+DATA port of the POE adapter.
- Connect an Ethernet cable from your local network (LAN) to the POE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Configuration

We suggest starting here to get yourself accustomed to the possibilities: https://mt.lv/help WinBox and MikroTik mobile app can be used to configure other devices through MQS. MQS itself can be configured only in the web interface.

## Extension slots and ports

- Built-in 2 GHz wireless access point module, AP/station/bridge/p2p modes are supported. Onboard PIF antennas built-in.
- One 10/100 Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices. The Ethernet port accepts 12-28 V DC powering and is also capable of POE output.
- One micro-USB 2.0 port for powering only.

## Buttons and jumpers

### Reset button

Hold this button during boot time, to reset software and firmware to factory settings.

### Mode button

By default, MQS will boot as an AP if you hold this button during boot time the MQS will boot into station mode. These modes can be adjusted through the quick-set menu.

## Accessories

Package includes the following accessories that come with the device:

- USB A Male Straight to Micro USB male flat cable L=100 mm w/o data pins.
- Velcro strap 16x300 mm, (with rubber back).
- Plastic tie strap 4.8 mm (W), 157 mm (L), nylon, BLACK.
- K-33 fastening set.
- MQS mounting bracket.

## Specifications

For more information about this product, specification and pictures please visit our web page: https://mikrotik.com/product/mqs

## Upgrading

To keep your device up to date, please visit our MQS product Support & Download section and check for the latest software version:

- Visit https://mikrotik.com/product/mqs#fndtn-downloads
- Download firmware "MQS current release";
- Connect to the MQS using a web browser;
- Choose the Upgrade tab;
- Click on the "Choose File" button and browse to downloaded file;
- Hit the Upgrade button and wait for the setup to finish.

## Federal Communication Commission Interference Statement

| Model | FCCID |
| --- | --- |
| RBMQS | TV7MQS |

This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation.

![](../img/fcc.badge.webp)

This equipment generates, uses and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and receiver.
- Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help.
**FCC Caution:** Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate this equipment.
This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation. This device and its antenna must not be co-located or operation in conjunction with any other antenna or transmitter.

**IMPORTANT: Exposure to Radio Frequency Radiation.**
This equipment complies with the FCC RF radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 20 cm between the radiator and any part of your body.

## Innovation, Science and Economic Development Canada

| Model | IC |
| --- | --- |
| RBMQS | 7442A-MQS |

This device complies with Industry Canada licence-exempt RSS standard(s). Operation is subject to the following two conditions: (1) this device may not cause interference, and (2) this device must accept any interference, including interference that may cause undesired operation of the device.
Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

**IMPORTANT: Exposure to Radio Frequency Radiation.**
This equipment complies with the IC radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 20 cm between the radiator and any part of your body.
Cet équipement est conforme aux limites d'exposition au rayonnement IC définies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé à une distance minimale de 20 cm entre le radiateur et toute partie de votre corps.

## UKCA marking

![](../img/ukca.badge.webp)

## Eurasian Conformity Mark

| Частотный диапазон | Мощность передатчика |
| --- | --- |
| 2400-2483.5 МГц | ≤100 мВт |

*Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: MikroTikls SIA, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. Cм. на упаковке.

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу. Информация об импортерах продукции MikroTik в Российскую Федерацию: https://mikrotik.com/buy/europe/russia

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

![](../img/eac.badge.webp)

## Norma Oficial Mexicana

Rango de frecuencia (potencia de salida máxima): 2400-2483.5 MHz (30 dBm). Los canales de frecuencia disponibles pueden variar según el modelo y la certificación del producto.

EFICIENCIA ENERGETICA CUMPLE CON LA NOM-029-ENER-2017.

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.
Fabricante: MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## The National Commission for the State Regulation of Communications and Informatization by Ukraine

Виробник: MikroTikls SIA, Brivibas gatve 214i Рига, Латвія, LV1039.

Робоча частота (Максимальна вихідна потужність): 2400-2483.5 МГц (20 дБм).

Справжнім MikroTikls SIA заявляє, що маршрутизатор відповідає основним вимогам та іншим відповідним положенням директиви 2014/53/EC, а також суттєвим вимогам Технічного регламенту радіообладнання, затвердженого постановою Кабінету Міністрів України від 24 травня 2017 року № 355.

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE Declaration of Conformity

Manufacturer: MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

Hereby, Mikrotīkls SIA declares that the RBMQS is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: https://mikrotik.com/products

### Frequency bands terms of use

| Frequency range (for applicable models) | Channels used | Maximum Output Power (EIRP) | Restriction |
| --- | --- | --- | --- |
| 2400-2483.5 MHz | 1 - 13 | 20 dBm | Without any restriction to use in all EU Member States |

** It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed!*
