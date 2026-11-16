# Groove-series

> The RouterBOARD Groove comes preinstalled in an outdoor case, with a built-in wireless interface, an N-Male antenna connector, and one 10/100 Ethernet connector which supports MDI-X auto-detection. The device is...

:::info[This article covers]

- **[Groove 52](https://mikrotik.com/product/RBGroove52HPnr2)**
- **[GrooveA 52](https://mikrotik.com/product/RBGrooveA-52HPnr2)** (RBGrooveA-52HPn)
- **[GrooveA 52 ac](https://mikrotik.com/product/RBGrooveGA-52HPacn)** (RBGrooveGA-52HPacn)

:::

![](./img/api_rbgroovea-52hpn.jpg)

The RouterBOARD Groove comes preinstalled in an outdoor case, with a built-in wireless interface, an
N-Male antenna connector, and one 10/100 Ethernet connector which supports MDI-X auto-detection.
The device is packaged with a 24 V power adapter, a PoE injector, and two mounting loops. Several
models are available (dual-band, single-band, AP, and CPE variants).

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- The Installation of the equipment must comply with local and national electrical codes.
- This product is intended to be mounted outdoors on a pole. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

## Quickstart

The Groove accepts 8-30 V Passive PoE from a PoE injector. The included injector should be connected with the "Data" end into a switch or other router, the "Data + Power" port should be connected to the Groove, by using an Ethernet cable of the desired length (not included).

Please follow these quick steps to set up your device:

- Attach provided antennas to the device, before connecting to the power source;
- Connect the ISP cable to the Ethernet1 port;
- Connect the device to the power source;
- Connect to the device through any of the ports, excluding Ethernet1, or the wireless network "MikroTik-..." (ensure to check the wireless passwords on the sticker); multiple configuration methods are available to ensure accessibility;
- Establish a connection using a mobile application. Alternatively, use **WebFig** in a web browser or the "**WinBox**" configuration tool at https://mt.lv/WinBox;
- Start configuration within the chosen tool, using the default IP address 192.168.88.1. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device;
- Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the "QuickSet" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

## Powering

The device accepts powering from an Ethernet port (Passive PoE). Under maximum load, the power consumption of this device is 4 W.

## Mounting

The device is to be mounted vertically so that the Ethernet cable points downwards.
If you wish to tighten the Groove to a pole, you can do it with the provided mounting loops. The Groove
comes bundled with two mounting loops – guide the loops around the Groove through the provided edge
markings, and around the pole where it will be mounted. You should avoid connecting a loose Ethernet
cable to the Ethernet port, and secure the cable to a wall or the pole, so that the cable weight is not pulling
the port. It is recommended to secure the Ethernet cable less than 2m from the Groove device. This is to
ensure that the cable doesn't damage the port by its weight or doesn't fall out.

## Configuration

The AP model Groove (A) is configured as a wireless access point, with the ethernet port configured as a
DHCP client, for connecting to your ISP router or switch. A DHCP server is configured on the wireless
interface. The CPE model Groove is configured as a client, with the Ethernet port configured as a DHCP
server.
RouterOS includes many configuration options in addition to what is described in this document. We
suggest starting here to get yourself accustomed to the possibilities: https://mt.lv/help In case the IP connection is not available, the WinBox tool (https://mt.lv/winbox) can be used to connect to the
MAC address of the device from the LAN side (all access is blocked from the internet port by default).

## Reset button

The reset button has three functions:
• Hold this button during boot time until LED light starts flashing, release the button to reset
RouterOS configuration (total 5 seconds).
• Keep holding for 5 more seconds, LED turns solid, release now to turn on CAPs mode for
managing the unit from a CAPsMAN server (total 10 seconds).
• Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the
RouterBOARD looks for Netinstall servers (total 15 seconds).

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Federal Communication Commission Interference Statement

| Model | FCC ID |
| --- | --- |
| Groove 52 | TV7GRV-A52HPN |
| GrooveA 52 | TV7GRV-A52HPN |
| GrooveA 52 ac | TV7GRV-A52HPC |

This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation.

However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and the receiver.
- Connect the equipment to an outlet on a circuit different from that to which the receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help
**FCC Caution:** Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

**Antenna Installation WARNING**: It is the installer's responsibility to ensure that when using the authorized antennas in the USA (or where FCC rules apply); only those antennas certified with the product are to be used. The installer should configure the output power level of antennas, according to country regulations and per antenna type. Professional installation is required for equipment with connectors to ensure compliance with health and safety issues.

**LIST OF APPROVED 2.4 GHz ANTENNAS:**

- 15 dBi Omni Directional (Model: WLO-2450-15)
- 13 dBi Omni Directional HP (Model: ODH 24-13)
- 20 dBi Panel (Model: WLP-2450-20)
- 17 dBi Sector (Model: SA 24-90-17-WB)
- 24 dBi Dish (Model: DC 24-HD-PFIP)
**LIST OF APPROVED 5 GHz ANTENNAS:**

- 8.5 dBi Omni Directional (Model: MT-482016/N/A)
- 24 dBi Panel Antenna (Model: PA58-24-ANT)
- 32 dBi Dish Antenna (Model: HDDA5W-32-DP2)
The same type of antenna and lower antenna gain as those listed above may also be used in accordance with certification.

## Innovation, Science, and Economic Development Canada

| Model | IC |
| --- | --- |
| Groove 52 | 7442A-GRVA52HPN |
| GrooveA 52 | 7442A-GRVA52HPN |
| GrooveA 52 ac | 7442A-GRVA52HPC |

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes : 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

The device for operation in the band 5150–5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems.

Les dispositifs fonctionnant dans la bande de 5 150 à 5 250 MHz sont réservés uniquement pour une utilisation à l'intérieur afin de réduire les risques de brouillage préjudiciable aux systèmes de satellites mobiles utilisant les mêmes canaux.

Antenna Installation WARNING: It is the installer's responsibility to ensure that when using the authorized antennas in Canada (or where IC rules apply); only those antennas certified with the product are to be used. The installer should configure the output power level of antennas, according to country regulations and per antenna type. Professional installation is required for equipment with connectors to ensure compliance with health and safety issues.

**LIST OF APPROVED 2.4 GHz ANTENNAS:**

- 15 dBi Omni Directional (Model: WLO-2450-15)
- 13 dBi Omni Directional HP (Model: ODH 24-13)
- 20 dBi Panel (Model: WLP-2450-20)
- 17 dBi Sector (Model: SA 24-90-17-WB)
- 24 dBi Dish (Model: DC 24-HD-PFIP)
**LIST OF APPROVED 5 GHz ANTENNAS:**

- 8.5 dBi Omni Directional (Model: MT-482016/N/A)
- 24 dBi Panel Antenna (Model: PA58-24-ANT)
- 32 dBi Dish Antenna (Model: HDDA5W-32-DP2)
The same type of antenna and lower antenna gain as those listed above may also be used in accordance with certification.

## UKCA Marking

![](../img/ukca.badge.webp)

## Eurasian Conformity Mark

| Частотный диапазон | Мощность передатчика |
| --- | --- |
| 2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц | ≤10 Вт |

*Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: MikroTikls SIA, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. Cм. на упаковке.

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу. Информация об импортерах продукции MikroTik в Российскую Федерацию: https://mikrotik.com/buy/europe/russia

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

![](../img/eac.badge.webp)

## Norma Oficial Mexicana

Rango de frecuencia (potencia de salida máxima): 2400-2483.5 MHz (30 dBm), 5725-5850 MHz (30 dBm). Los canales de frecuencia disponibles pueden variar según el modelo y la certificación del producto.

Número de Certificado de Homologación (IFT): Ver la etiqueta del producto.

EFICIENCIA ENERGETICA CUMPLE CON LA NOM-029-ENER-2017.

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.
Fabricante: MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## The National Commission for the State Regulation of Communications and Informatization by Ukraine

Виробник: MikroTikls SIA, Brivibas gatve 214i Рига, Латвія, LV1039.

Робоча частота (Максимальна вихідна потужність): 2400-2483.5 МГц (20 дБм), 5150-5250 МГц (23 дБм), 5250-5350 МГц (20 дБм), 5470-5725 МГц (27 дБм).

Справжнім MikroTikls SIA заявляє, що маршрутизатор відповідає основним вимогам та іншим відповідним положенням директиви 2014/53/EC, а також суттєвим вимогам Технічного регламенту радіообладнання, затвердженого постановою Кабінету Міністрів України від 24 травня 2017 року № 355.

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE Declaration of Conformity

Manufacturer: MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

Hereby, Mikrotīkls SIA declares that the radio equipment type RouterBOARD is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: https://mikrotik.com/products

### Frequency band's terms of use

| Frequency range (for applicable models) | Channels used | Maximum Output Power (EIRP) | Restriction |
| --- | --- | --- | --- |
| 2412-2472 MHz | 1 - 13 | 20 dBm | Without any restriction to use in all EU Member States |
| 5150-5250 MHz | 26 - 48 | 23 dBm | Restricted to indoor use only* |
| 5250-5350 MHz | 52 - 64 | 20 dBm | Restricted to indoor use only* |
| 5470-5725 MHz | 100 - 140 | 27 dBm | Without any restriction to use in all EU Member States |

**It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed!**

This MikroTik device meets Maximum TX power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

![](../img/image2020-2-6_16-24-10.badge.webp)

The WLAN function for this device is restricted to indoor use only when operating in the 5150 to 5350 MHz frequency range. / Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.
