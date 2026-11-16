# QRT 2

> The QRT is an outdoor CPE unit with the following hardware specifications:

The QRT is an outdoor CPE unit with the following hardware specifications:

![](./img/api_rbqrtg-2shpnd.webp)

## [QRT 2](https://mikrotik.com/product/RBQRTG-2SHPnDr2) (RBQRTG-2SHPnD)

## Quickstart

Please follow these quick steps to set up your device:

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
- Mount the unit in your desired place, please see (link)

## Extension slots and ports

Gigabit Ethernet port, passive PoE on Ethernet port.

- 2.4 GHz wireless, supported protocol 802.11b/g/n, antenna gain 17 (dBi).

## Opening latch

To access the Ethernet port and reset button, please open latch:

![](../img/worddav867a92adb22e5da4d72329c0496a5cf3.webp)

- Pull the latch out downwards from the device.
- Lift the latch, but do not remove them completely.

![](../img/worddav179b848077c3b85403ff218083268b5b.webp)

## Front status LED behavior

RouterOS allows configuring each LED's activity the way that the user wishes. It is possible to configure the LEDs to display wireless strength, blink the LEDs on interface traffic activity, and many other options. For further information please visit the [LEDs](/docs/hardware/leds) manual page.
Default factory configuration for this device:

![](../img/worddav8166c6239ffec9eae13bd85db72a8eb4.webp)

- Solid Blue – The device is powered on.
- Solid Green – Connected Ethernet port.
- Solid Green – User-defined LED.
- Solid Green – The set of five green LEDs, shows the signal strength.

## Mounting

The device is designed to be used outdoors and mounted on the mast with all needed cables connecting through the latch of the unit.

*Mounting and configuration of this device should be done by a qualified person.*

When mounting on the mast, please ensure that the cable feed is pointing downwards.
The IP rating scale of this device is IP54. We recommend using Cat5/6 shielded cables.
Warning! This equipment should be installed and operated with a minimum distance of 30 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference. The QRT box contains several parts that need to be assembled. Please follow this process:

- Attach the two brackets (A) to the swivel adjuster (B), by using the four provided screws (use a PH1 screwdriver).

![](../img/worddav5a0d40904ad5b4f0eee9b7042b44b745.webp)

- Place the two U-bolts (C) around the mast or pole, and guide them through the holes on the swivel adjuster (D). Then, tighten the U-bolts, each with one regular washer, one spring washer, and one nut, as shown in the image to the right. All nuts need to be tightened using a size 10 (3/8 in) wrench. Maximum diameter of the pole can be up to 70 mm.

![](../img/worddavb8f7a36cd37a414342a63357cd872cbf.webp)

- Use the mounting bracket (E), and put it on to the back of the antenna. Install with one rubber ring, one washer, and one nut for each of the built-in bolts (in that order).

![](../img/worddav4e759eb7208e49d33b06e83b683878f6.webp)

- Attach the swivel adjuster to the mounting bracket. Use the long bolt in the position (F). Put one regular washer, and one spring washer onto the shorter screws, then put them in positions (G). Do not tighten too much, as you need to adjust the antenna now.

![](../img/worddav46d7954f63a07f3fabe91584db433b7c.webp)

- Once antenna level and angle are adjusted according to the wireless signal in software, tighten all nuts. Note the degrees of angle for future reference.
Wind load16 kg @ 40m/s, 9kg @ 30 m/s;

## Grounding

The installation infrastructure (towers and masts), as well as the router itself, must be properly grounded. The device includes a grounding wire attachment screw on the backside of the unit. Attach your grounding wire to the grounding screw, then attach the other end of the grounding wire to the grounded mast, please see the picture:

![](../img/worddav4b300042fc6267d7fa146c1b3b3bc3f4.webp)

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes accessories that come with the device:

- Montage elements: QRT U Bolt, Steel - Zinc plated, DIA 6 mm, U mast clamp, antenna mount.
- EU Switching Power Supply 24 V, 0.8 A, 19.2 W, DC ⎓, 85.3 %, VI, cable:150 cm Hor CMC.
- K-QRT_Fastening set for QRT.
- ZCPOEC006-R2_Gigabit POE injector cable with shielded connector.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Specifications

For more information about this product, specifications, pictures, downloads, and test results please visit our web page: https://mikrotik.com/product/RBQRTG-2SHPnDr2

## MikroTik mobile app

![](../img/worddave70ad1e3c5acf51ccbd4a9d382cadd85.webp)

![](../img/worddavec48bf5aa3b860afa9fcb97cf4aca652.webp)

![](../img/worddavea6671dfbffe714b2f3abe6d04e7ad04.badge.webp)

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

## Federal Communication Commission Interference Statement

FCC ID: TV7RBQRTG2SHPND

![](../img/fcc.badge.webp)

This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation.
This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and receiver.
- Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help.
FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate this equipment.
This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation. This device and its antenna must not be co-located or operation in conjunction with any other antenna or transmitter.
IMPORTANT: Exposure to Radio Frequency Radiation.
This equipment complies with the FCC RF radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 30 cm between the radiator and any part of your body.
**Antenna Installation. WARNING:** It is the installer's responsibility to ensure that when using the authorized antennas in the United States (or where FCC rules apply); only those antennas certified with the product are used. The use of any antenna other than those certified with the product is expressly forbidden in accordance to FCC rules CFR47 part 15.204. The installer should configure the output power level of antennas, according to country regulations and per antenna type. Professional installation is required of equipment with connectors to ensure compliance with health and safety issues.

## Innovation, Science and Economic Development Canada

IC:7442A-QRTG2SHPND
This device complies with Industry Canada's licence-exempt RSS standard(s). Operation is subject to the following two conditions: (1) this device may not cause interference, and (2) this device must accept any interference, including interference that may cause undesired operation of the device.
Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.
IMPORTANT: Exposure to Radio Frequency Radiation.
This equipment complies with the IC radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 30 cm between the radiator and any part of your body.
Cet équipement est conforme aux limites d'exposition au rayonnement IC définies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé à une distance minimale de 30 cm entre le radiateur et toute partie de votre corps.
CAN ICES-3 (B)/NMB-3(B)FCC

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

Робоча частота (Максимальна вихідна потужність): 2480-2483.5 МГц (20 дБм).

Справжнім MikroTikls SIA заявляє, що маршрутизатор відповідає основним вимогам та іншим відповідним положенням директиви 2014/53/EC, а також суттєвим вимогам Технічного регламенту радіообладнання, затвердженого постановою Кабінету Міністрів України від 24 травня 2017 року № 355.

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE Declaration of Conformity

Manufacturer: MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

Hereby, Mikrotīkls SIA declares that the radio equipment type RBQRTG-2SHPnD is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: https://mikrotik.com/products

### Frequency bands terms of use

| **Frequency range (for applicable models)** | **Channels used** | **Maximum Output Power (EIRP)** | **Restriction** |
| --- | --- | --- | --- |
| 2412-2472 MHz | 1 - 13 | 20 dBm | Without any restriction to use in all EU Member States |

**It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed!**
