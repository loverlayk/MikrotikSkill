# LHG-series

> Exposure to Radio Frequency Radiation: This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be...

:::info[This article covers]

- **[LHG 2](https://mikrotik.com/product/lhg_2)** (RBLHG-2nD)
- **[LHG 5](https://mikrotik.com/product/RBLHG-5nD)** (RBLHG-5nD)
- **[LHG HP5](https://mikrotik.com/product/RBLHG-5HPnD)** (RBLHG-5HPnD)
- **[LHG 5 ac](https://mikrotik.com/product/lhg_5_ac)** (RBLHGG-5acD)

:::

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- All installation methods for mounting an access point on any wall surface is subject to the acceptance of local jurisdiction.
- The Installation of the equipment must comply with local and national electrical codes.
- This product is intended to be mounted outdoors on a pole. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

- The LHG is an outdoor wireless router with a built-in directional antenna. It can be used as a CPE or for point-to-point links (use RouterOS wireless mode "bridge" to work as a single-client AP for point-to-point scenarios).

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 40 centimeters from your body, occupational user, or the general public.

## Quickstart

- Open the Ethernet door to connect an Ethernet cable to the Ethernet port, connect the other end of the Ethernet cable to the included PoE injector.
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

## Assembly and Mounting

- Attach the two legs to the LHG case.

![](./img/api_rblhg-5nd.jpg)

## [LHG 5](https://mikrotik.com/product/RBLHG-5nD) (RBLHG-5nD)

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

![](./img/image2021-7-22_11-10-57.webp)

solidMOUNT

![](./img/image2021-7-22_11-11-40.webp)

## Powering

The device accepts powering only from Passive PoE injectors.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the POE port of the POE adapter.
- Connect an Ethernet cable from your LAN to the LAN port of the POE adapter, please mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: https://mt.lv/help In case an IP connection is not available, the WinBox tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section .

## Extension slots and ports

- One Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- One Integrated 2x2 MIMO wireless device with a built-in grid antenna.
LHG 2 Dual chain 18 dBi, 2.4GHz, 802.11b/g/n. Maximum power consumption 5 W.
LHG 5 Dual chain 24.5 dBi, 5GHz, 802.11 a/n. Maximum power consumption 6 W.
LHG HP5 Dual chain 24dBi, 5GHz, 802.11 a/n. Maximum power consumption 7 W.
LHG 5 ac Dual chain 24.5dBi, 5GHz, 802.11 a/n/ac. Maximum power consumption 8 W.

## Reset button

The reset button has three functions:

- Hold this button during boot time until the LED light starts flashing, release the button to reset the RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAPs mode (total 10 seconds).
- Or keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

The package includes the following accessories that come with the device:

- Mounting set for LHG-5.
- POE Injector/Gigabit POE injector(For LHGG-5acD).
- LHG-5G-390 mm Dish 3,0x2.5x0,5 mm.
- DC ⎓ EU/US Switching Power Supply 24 V, 0.38 A, 9 W, Level VI, cable:1.5 m).
- Hose Clamp SUS304 (philips type ; clamping diameter range 35-70 mm).

## Specifications

For more information about LHG products, specifications and pictures please visit our web page: https://mikrotik.com/product/lhg_2
https://mikrotik.com/product/RBLHG-5nD
https://mikrotik.com/product/RBLHG-5HPnD
https://mikrotik.com/product/lhg_5_ac

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

![](../img/worddavea6671dfbffe714b2f3abe6d04e7ad04.badge.webp)

![](../img/worddavec48bf5aa3b860afa9fcb97cf4aca652.webp)

![](../img/worddave70ad1e3c5acf51ccbd4a9d382cadd85.webp)

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Federal Communication Commission Interference Statement

| Model | FCC ID |
| --- | --- |
| LHG 2 | TV7LHG2ND |
| LHG 5 | TV7LHG5NDM |
| LHG 5 ac | TV7LHG5ACD |
| LHG HP5 | TV7LHG5HPND |

![](../img/fcc.badge.webp)

**LHG 5** and **LHG 5 ac** has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation.

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense.

**LHG 2** and **LHG HP5** has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation.
This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and receiver.
- Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help.
FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate this equipment.
This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation. This device and its antenna must not be co-located or operation in conjunction with any other antenna or transmitter.
**IMPORTANT: Exposure to Radio Frequency Radiation.**
This equipment complies with the FCC RF radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 40 cm between the radiator and any part of your body.

## Innovation, Science and Economic Development Canada

| Model | FCC ID |
| --- | --- |
| LHG 2 | 7442A-LHG2ND |
| LHG 5 | 7442A-LHG5NDM |
| LHG 5 ac | 7442A-LHG5ACD |
| LHG HP5 | 7442A-LHG5HPND |

This device complies with Industry Canada's license-exempt RSS standard(s). Operation is subject to the following two conditions: (1) this device may not cause interference, and (2) this device must accept any interference, including interference that may cause undesired operation of the device.
Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.
**IMPORTANT: Exposure to Radio Frequency Radiation.**
This equipment complies with the IC radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 40 cm between the radiator and any part of your body.
**IMPORTANTE:** Cet équipement est conforme aux limites d'exposition au rayonnement IC définies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé à une distance minimale de 40 cm entre le radiateur et toute partie de votre corps.

**LHG 5** and **LHG 5 ac**. This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

**LHG 2** and **LHG HP5**. This class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

The device for operation in the band 5150–5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems.
Les dispositifs fonctionnant dans la bande de 5 150 a 5 250 MHz sont reserves uniquement pour une utilisation a l'interieur afin de reduire les risques de brouillage prejudiciable aux systemes de satellites mobiles utilisant les memes canaux.

## UKCA Marking

![](../img/ukca.badge.webp)

## Eurasian Conformity Mark

| Частотный каналы | Мощность передатчика |
| --- | --- |
| 2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц | ≤10 Вт |

*Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: MikroTikls SIA, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. Cм. на упаковке.

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

![](../img/eac.badge.webp)

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

## Norma Oficial Mexicana

Rango de frecuencia (potencia de salida máxima): 2400-2483.5 MHz (30 dBm), 5725-5850 MHz (30 dBm). Los canales de frecuencia disponibles pueden variar según el modelo y la certificación del producto.

EFICIENCIA ENERGETICA CUMPLE CON LA NOM-029-ENER-2017.

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.

Fabricante: MikroTikls SIA, Unijas iela 2, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## The National Commission for the State Regulation of Communications and Informatization by Ukraine

Виробник: MikroTikls SIA, Unijas iela 2, Рига, Латвія, LV1039.

Робоча частота (Максимальна вихідна потужність): 2400-2483.5 МГц (30 дБм), 5150-5250 МГц (23 дБм), 5250-5350 МГц (20 дБм), 5470-5725 МГц (27 дБм).

Справжнім MikroTikls SIA заявляє, що маршрутизатор відповідає основним вимогам та іншим відповідним положенням директиви 2014/53/EC, а також суттєвим вимогам Технічного регламенту радіообладнання, затвердженого постановою Кабінету Міністрів України від 24 травня 2017 року № 355.

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE Declaration of Conformity

Manufacturer: MikroTikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

Hereby, Mikrotīkls SIA declares that the radio equipment type RouterBOARD is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: https://mikrotik.com/products

### Frequency bands terms of use

| **Frequency range (for applicable models)** | **Channels used** | **Maximum Output Power (EIRP)** | **Restriction** |
| --- | --- | --- | --- |
| 2400-2483.5 MHz (only LHG 2) | 1 - 13 | 20 dBm | Without any restriction to use in all EU Member States |
| 5150-5250 MHz | 26 - 48 | 23 dBm | Restricted to indoor use only* |
| 5250-5350 MHz | 52 - 64 | 20 dBm | Restricted to indoor use only* |
| 5470-5725 MHz | 100 - 140 | 27 dBm | Without any restriction to use in all EU Member States |

**It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed!**

This MikroTik device meets Maximum TX power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

![](../img/image2020-2-6_16-24-10.badge.webp)

The WLAN function for this device is restricted to indoor use only when operating in the 5150 to 5350 MHz frequency range. / Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.
