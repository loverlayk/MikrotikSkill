# LHG R

> LHG R without factory installed modem, you can choose your own solution.

## [LHG R](https://mikrotik.com/product/rblhgr) (RBLHGR)

![](./img/api_rblhgr.webp)

LHG R without factory installed modem, you can choose your own solution.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- All installation methods for mounting an access point on any wall surface is subject to the acceptance of local jurisdiction.
- The Installation of the equipment must comply with local and national electrical codes.
- This product is intended to be mounted outdoors on a pole. Read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Use this product with care and operate at your own risk!
- In the case of device failure, disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 120 centimeters from your body, occupational user, or the general public.

## Quickstart

- While holding the unit by its central column, apply force to the tab, which holds the latch closed, until the latch pops open.
- Insert the SIM card into the slot, with chips facing UP.
- Install your desired modem.
- Assemble case by attaching legs to the base of the unit, see Case assembly paragraph.
- Mount unit in your desired place, see Mounting paragraph.
- Connect an Ethernet cable to the Ethernet port, connect the other end of the Ethernet cable to the included PoE injector.
- Plug the PoE injector into your PC.
- Plug the included power supply into the PoE injector to start up the device. See the powering paragraph.
- Set LAN computer IP configuration to *automatic* (DHCP).
- Open http://192.168.88.1 in your web browser to start the configuration.
- User name: a*dmin* and there is no password by default you will be logged in automatically to the Quick Set screen (or, for some models, check user and wireless passwords on the sticker).
- Update the device by selecting the "Check for updates" button on the right side and updating your RouterOS software to the latest version to ensure the best performance and stability. Must have a valid SIM card inserted.
- To manually update the device, go https://mikrotik.com/download
- Choose MIPSBE packages for this device and download it to your PC.
- Upload downloaded packages to the WebFig "Files" menu and reboot the device. Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates.

## Extension slots and ports

- One 10/100 Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices. The Ethernet port accepts 9-30 V DC powering from a passive PoE injector.
- MiniPCIe slot and SIM slot (can't be used separately) to be used with a 3G/4G/LTE modem.

## Powering

The device can be powered from 12-57 V 802.3af/at sources and also Passive PoE injectors (one power supply and PoE injector are included).
Maximum power consumption 6 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the POE port of the POE adapter.
- Connect an Ethernet cable from your LAN to the LAN port of the POE adapter, mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Opening the case cover

To access the miniPCIe slot, the opening of the unit's top cover is required. As an opening tool, you can use a large size flat head screwdriver or a small coin. Be extremely cautious when opening, because the incorrect opening of the clip can break it off!
*Mounting and configuration of this device should be done by a qualified person.*
Follow these steps:

![](../img/image2020-2-11_12-52-24.webp)

Additional Caution when lifting up the cover, do not force it with sharp objects.

## miniPCIe slot usage

The device is equipped with a miniPCIe slot to be used with a 3G/4G/LTE modem. One SIM slot is provided for use together with a miniPCIe modem. The SIM slot is not used separately.
In this case, an internal antenna is not connected (located inside the enclosure). Installing a miniPCIe module should be done by a qualified person, follow safety precautions when handling electrical equipment:

- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage.
- Open the upper cover as shown on instruction previously.
- The antenna is located underneath PCB.
- Locate the miniPCIe slot on the PCB and remove two factory attached screws.
- Attach provided a thick thermal pad to the card, and install the card into miniPCIe slot so that the thermal pad is between PCB and card.
![](../img/worddav1e90809e529db3204bdc0723606664be.webp)
- Insert your desired card.
- The secure card in place using previously removed two screws.
- Attach the black uFL connector to the MAIN antenna connector of the modem, attach the gray cable to the DIV connector.
- Attach a thinner thermal pad to the top of the card.
- Reassembly in backorder.
After reassembly, slide in the SIM card from your mobile operator into the SIM slot, with the chips facing up as shown on the port label. The slot accepts MicroSIM (3FF).

## Assembly

- Attach the two legs to the LHG case by sliding them onto the respective sides, legs are different and cannot be exchanged (when looking at the product place it that cover for Ethernet port is in front of you, leg marked R is for the right side, leg marked L is for the left side).
- Snap the assembled LHG unit to the grid in the appropriate central location.
- Fix the two legs in place with included two self thread screws (Phillips screwdriver PH2).
The package also contains a grounding cable connector and a 5-degree angle adapter, for easier up or downward tilt adjustment.

## Mounting

![](../img/worddav1da210ea0b3e561fb1c3ae605bd31feb.webp)

- Slide the included metallic mounting rings into the two slots on the back of the antenna dish.
- Attach the unit to a pole, with the Ethernet port pointing downward.
- Use a PH2 screwdriver to tighten the rings.
- Fix the Ethernet cable to the pole using zip ties, less than one meter from the unit, to avoid the cable being pulled out of the port.
- Check mounting angle and positioning.
- Optional: If required, before mounting the unit, you can insert the included 5-degree adjustment adapter into the top or bottom slot where the mounting ring is inserted. This will create an additional upward or downward angle when the unit is tightened to a vertical pole.
- Insert a 5-degree angle adapter to one of the slots and remount the unit.
When mounting outdoors, ensure that any cable openings are directed downwards. Use POE injector and proper grounding, this device has specially designed grounding connector under the port cover. Recommended using shielded Cat5/6 cable. The IP rating scale for this device is IP54.

## Configuration

Once logged in, you should select the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: https://mt.lv/help In case IP connection is not available, the WinBox tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section .

## Reset button

The reset button has three functions:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.
The device includes a grounding connection behind the Ethernet port door, which you should connect to the grounding installation of the tower or building where the device will be used. This is to substantially reduce the risk of ESD and lightning damage.

## Mode button

The action of the mode buttons can be configured from RouterOS software to execute any user-supplied RouterOS script. You can also disable this button. The mode button can be configured in RouterOS menu /system routerboard mode-button.

## Specifications

For more information about this product, specification and pictures visit our web page: https://mikrotik.com/product/rblhgr

## Accessories

![](../img/image2020-2-11_12-55-40.webp)

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

![](../img/worddavea6671dfbffe714b2f3abe6d04e7ad04.badge.webp)

![](../img/worddavec48bf5aa3b860afa9fcb97cf4aca652.webp)

![](../img/worddave70ad1e3c5acf51ccbd4a9d382cadd85.webp)

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

To avoid pollution of the environment, separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Federal Communication Commission Interference Statement

![](../img/fcc.badge.webp)

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation.

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense

**FCC Caution:** Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate this equipment.
This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation. This device and its antenna must not be co-located or operation in conjunction with any other antenna or transmitter.
Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

## Innovation, Science and Economic Development Canada

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada's license-exempt RSS(s). Operation is subject to the following two conditions:

- This device may not cause interference;
- This device must accept any interference, including interference that may cause undesired operation of the device.
L'émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d'Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes:

- L'appareil ne doit pas produire de brouillage;
- L'appareil doit accepter tout brouillage radioélectrique subi, mźme si le brouillage est.
This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

**IMPORTANT: Exposure to Radio Frequency Radiation.**
This equipment complies with the IC radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 120 cm between the radiator and any part of your body.
Cet equipement est conforme aux limites d'exposition au rayonnement IC definies pour un environnement non controle. Cet equipement doit etre installe et utilise a une distance minimale de 120 cm entre le radiateur et toute partie de votre corps.

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

## The National Commission for the State Regulation of Communications and Informatization by Ukraine

Виробник: MikroTikls SIA, Brivibas gatve 214i Рига, Латвія, LV1039.

Справжнім MikroTikls SIA заявляє, що маршрутизатор відповідає основним вимогам та іншим відповідним положенням директиви 2014/53/EC, а також суттєвим вимогам Технічного регламенту радіообладнання, затвердженого постановою Кабінету Міністрів України від 24 травня 2017 року № 355.

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE Declaration of Conformity

Manufacturer: MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

Hereby, Mikrotīkls SIA declares that the radio equipment type RBLHGR is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: https://mikrotik.com/products

### WCDMA / LTE / 5G

| Operating Frequency / Maximum output power Betriebsfrequenz / maximale Ausgangsleistung Fréquence de fonctionnement / puissance de sortie maximale Frequenza operativa / massima potenza di uscita Frecuencia de funcionamiento / potencia de salida máxima Рабочая частота / максимальная выходная мощность | E-GSM-900 | 900 MHz / 33 dBm |
| --- | --- | --- |
| DCS-1800 | 1800 MHz / 30 dBm | |
| WCDMA Band I | 1922.4 MHz / 24 dBm ± 2.7 dB | |
| WCDMA Band VIII | 882.4 MHz / 24 dBm ± 2.7 dB | |
| LTE Band 1 | 2100 MHz / 23dBm ± 2.7 dB | |
| LTE Band 3 | 1800 MHz / 23dBm ± 2.7 dB | |
| LTE Band 7 | 2600 MHz / 23dBm ± 2.7 dB | |
| LTE Band 8 | 900 MHz / 23dBm ± 2.7 dB | |
| LTE Band 20 | 800 MHz / 23dBm ± 2.7 dB | |
| LTE Band 38 | 2600 MHz / 23dBm ± 2.7 dB | |
| LTE Band 40 | 2300 MHz / 23dBm ± 2.7 dB | |

This MikroTik device meets Maximum WLAN and LTE transmit power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen WLAN- und LTE-Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN et LTE conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN e LTE in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN y LTE de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN и LTE в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.
