# hAP ax³

> Our top-of-the-line AX home access point. With all the processing power and speed your household might ever need. Gen 6 wireless, 2.5 Gigabit Ethernet, PoE, WPA3, and more! See the hAP ax³ product page for full...

![](./img/api_c53uig_5hpaxd2hpaxd.jpg)

## [hAP ax³](https://mikrotik.com/product/hap_ax3) (C53UiG+5HPaxD2HPaxD)

Our top-of-the-line AX home access point. With all the processing power and speed your household might ever need. Gen 6 wireless, 2.5 Gigabit Ethernet, PoE, WPA3, and more! See the [hAP ax³ product page](https://mikrotik.com/product/hap_ax3) for full specifications and brochures.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- The Installation of the equipment must comply with local and national electrical codes.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity, or hot environments.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 37 centimeters from your body, occupational user, or the general public.

## Setup

- Attach the provided antennas to the device before connecting it to the power source;
- Ensure your Internet Service Provider (ISP) allows hardware changes and automatically assigns an IP address;
- Connect the ISP cable to the Ethernet1 port;
- Connect the device to the power source;
- Connect to the device through any of the ports, excluding Ethernet1, or the wireless network "MikroTik-..." (ensure to check the wireless passwords on the sticker);
- Establish a connection using a mobile application. Alternatively, use WebFig in a web browser or the "WinBox" configuration tool at https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Start configuration within the chosen tool, using the default IP address 192.168.88.1. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device;
- Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the "QuickSet" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

To reach the **password**, pull out the card placeholder near the product information.

![](./img/image-2023-1-11_16-12-5.webp)

## Powering

- Number of DC inputs 2 (PoE-in, DC jack)
- PoE-in input Voltage 18-28 V
- DC jack input Voltage 12-28 V
- PoE-out Passive PoE Ether1, max out per port output (input &lt; 30 V): 0.625 A
- PoE-out total output power 15 W
- Power adapter nominal voltage 24 V
- Power adapter nominal current 1.5 A
- Max power consumption (without attachments) 15 W
- Max power consumption 38 W

## Configuration

We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability. RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: https://mt.lv/help In case an IP connection is not available, the WinBox tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default). For recovery purposes, it is possible to boot the device from the network, see the [Buttons and jumpers](#buttons-and-jumpers).

## Extension slots and ports

- Product code C53UiG+5HPaxD2HPaxD
- CPU Quad-Core IPQ-6010 1.8 GHz
- CPU architecture ARM 64bit
- Size of RAM 1 GB
- Storage 128 MB, NAND
- Number of 1G Ethernet ports 4
- Number of 2.5G Ethernet ports 1 (supports PoE-in/out)
- USB 1 USB 3 type A
- Switch chip model IPQ-6010
- Wireless interface model QCN-5022 (2.4 GHz), QCN-5052 (5 GHz)
- Wireless 2.4 GHz 802.11b/g/n/ax dual-chain, 5 GHz 802.11a/n/ac/ax dual-chain
- Wireless antenna max gain 2.4 GHz (3.3 dBi), 5 GHz (5.5 dBi)
- Dimensions 251 x 130 x 39 mm
- Operating system RouterOS, License level 6
- Operating temperature -40°C to +70°C

## Buttons and jumpers

The reset button has three functions:

- Hold this button during boot time until the green LED light starts flashing, release the button to reset RouterOS configuration.
- Keep holding the reset button until the LED turns solid, then release it to enable CAP mode. The device will then start searching for a CAPsMAN server.
- To reinstall RouterOS using the [Netinstall](../docs/tags/netinstall) utility, enter the device into BOOTP mode. Two booter options are available: the **Regular Booter** and the **Backup Booter**. It is recommended to verify both options in case one does not work.
  - **Regular Booter:** To enter etherboot mode, press the **Reset** button after powering on the device and waiting 1–2 seconds.
  - **Backup Booter:** Power off the device. Press and hold the **Reset** button, then power on the device. Wait for the **LED** sequence (blinking → steady → off), then release the button. The device will boot into **BOOTP** mode, ready for RouterOS reinstallation via **Netinstall**. Depending on the model, this may be indicated by the **USR, USER, System**, or **ACT** LED, or by the SFP port LED.

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Accessories

![](./img/image-2022-10-4_11-38-44.webp)

## Notice

- Datasheet for any device is available on the official manufacturer website.
- The Frequency band 5.470-5.725 GHz isn’t allowed for commercial use.
- Please make sure the device has a locking package (firmware version from the manufacturer) which is required to be applied to the end-user equipment to prevent the end-user from reconfiguration. The product will be marked with country code “-EG” - C53UiG+5HPaxD2HPaxD-EG.
- For Outdoor Usage: End-user requires approval/license from the NTRA.
- Firmware for Egypt Regulatory have their wireless frequency range limited to 2.400 – 2.4835 GHz, the TX power is limited to 20dBm (EIRP).
- Firmware for Egypt Regulatory have their wireless frequency range limited to 5.150 – 5.250 GHz, the TX power is limited to 23dBm (EIRP).
- Firmware for Egypt Regulatory have their wireless frequency range limited to 5.250 – 5.350 GHz, the TX power is limited to 20dBm (EIRP).
This device needs to be upgraded to the latest version to ensure compliance with local authority regulations! It is the end users responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements.
All MikroTik radio devices must be professionally installed.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as at designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

### Federal Communication Commission Interference Statement

| | |
| --- | --- |
| C53UiG+5HPaxD2HPaxD-US | TV7C53-5AXD2AXD |

![](../img/fcc.badge.webp)

This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation.

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and the receiver.
- Connect the equipment to an outlet on a circuit different from that to which the receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help.
FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

APPROVED 2.4 GHz ANTENNA:

- 3.36 dBi Omni-directional (HGO-antenna-IN)
APPROVED 5 GHz ANTENNA:

- 6.01 dBi Omni-directional (HGO-antenna-IN)
**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 37 centimeters from your body, occupational user, or the general public.

### Innovation, Science and Economic Development Canada

| | |
| --- | --- |
| C53UiG+5HPaxD2HPaxD-US | 7442A-C53AX |

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

The device for operation in the band 5150–5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems.

Les dispositifs fonctionnant dans la bande de 5 150 à 5 250 MHz sont réservés uniquement pour une utilisation à l'intérieur afin de réduire les risques de brouillage préjudiciable aux systèmes de satellites mobiles utilisant les mêmes canaux.

APPROVED 2.4 GHz ANTENNA:

- 3.36 dBi Omni-directional (HGO-antenna-IN)
APPROVED 5 GHz ANTENNA:

- 6.01 dBi Omni-directional (HGO-antenna-IN)
**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the IC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 37 centimeters from your body, occupational user, or the general public.

Cet équipement est conforme aux limites d'exposition aux rayonnements IC établies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé avec un minimum de 37cm de distance entre la source de rayonnement et votre corps.

### UKCA marking

![](../img/ukca.badge.gif)

### CE Declaration of Conformity

| *BG* | С настоящото Mikrotīkls SIA декларира, че този тип радиосъоръжение C53UiG+5HPaxD2HPaxD е в съответствие с Директива 2014/53/ЕС. Цялостният текст на ЕС декларацията за съответствие може да се намери на следния интернет адрес: https://mikrotik.com/products |
| --- | --- |
| CS | Tímto Mikrotīkls SIA prohlašuje, že typ rádiového zařízení C53UiG+5HPaxD2HPaxD je v souladu se směrnicí 2014/53/EU. Úplné znění EU prohlášení o shodě je k dispozici na této internetové adrese: https://mikrotik.com/products |
| DA | Hermed erklærer Mikrotīkls SIA, at radioudstyrstypen C53UiG+5HPaxD2HPaxD er i overensstemmelse med direktiv 2014/53/EU. EU-overensstemmelseserklæringens fulde tekst kan findes på følgende internetadresse: https://mikrotik.com/products |
| DE | Hiermit erklärt Mikrotīkls SIA, dass der Funkanlagentyp C53UiG+5HPaxD2HPaxD der Richtlinie 2014/53/EU entspricht. Der vollständige Text der EU-Konformitätserklärung ist unter der folgenden Internetadresse verfügbar: https://mikrotik.com/products |
| EL | Με την παρούσα ο/η Mikrotīkls SIA, δηλώνει ότι ο ραδιοεξοπλισμός C53UiG+5HPaxD2HPaxD πληροί την οδηγία 2014/53/ΕΕ. Το πλήρες κείμενο της δήλωσης συμμόρφωσης ΕΕ διατίθεται στην ακόλουθη ιστοσελίδα στο διαδίκτυο: https://mikrotik.com/products |
| EN | Hereby, Mikrotīkls SIA declares that the radio equipment type C53UiG+5HPaxD2HPaxD is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: https://mikrotik.com/products |
| ES | Por la presente, Mikrotīkls SIA declara que el tipo de equipo radioeléctrico C53UiG+5HPaxD2HPaxD es conforme con la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la dirección Internet siguiente: https://mikrotik.com/products |
| ET | Käesolevaga deklareerib Mikrotīkls SIA, et käesolev raadioseadme tüüp C53UiG+5HPaxD2HPaxD vastab direktiivi 2014/53/EL nõuetele. ELi vastavusdeklaratsiooni täielik tekst on kättesaadav järgmisel internetiaadressil: https://mikrotik.com/products |
| FI | Mikrotīkls SIA vakuuttaa, että radiolaitetyyppi C53UiG+5HPaxD2HPaxD on direktiivin 2014/53/EU mukainen. EU-vaatimustenmukaisuusvakuutuksen täysimittainen teksti on saatavilla seuraavassa internetosoitteessa: https://mikrotik.com/products |
| FR | Le soussigné, Mikrotīkls SIA, déclare que l'équipement radioélectrique du type C53UiG+5HPaxD2HPaxD est conforme à la directive 2014/53/UE. Le texte complet de la déclaration UE de conformité est disponible à l'adresse internet suivante: https://mikrotik.com/products |
| HR | Mikrotīkls SIA ovime izjavljuje da je radijska oprema tipa C53UiG+5HPaxD2HPaxD u skladu s Direktivom 2014/53/EU. Cjeloviti tekst EU izjave o sukladnosti dostupan je na sljedećoj internetskoj adresi: https://mikrotik.com/products |
| HU | Mikrotīkls SIA igazolja, hogy a C53UiG+5HPaxD2HPaxD típusú rádióberendezés megfelel a 2014/53/EU irányelvnek. Az EU-megfelelőségi nyilatkozat teljes szövege elérhető a következő internetes címen: https://mikrotik.com/products |
| IT | Il fabbricante, Mikrotīkls SIA, dichiara che il tipo di apparecchiatura radio C53UiG+5HPaxD2HPaxD è conforme alla direttiva 2014/53/UE. Il testo completo della dichiarazione di conformità UE è disponibile al seguente indirizzo Internet: https://mikrotik.com/products |
| IS | Hér með lýsir Mikrotīkls SIA því yfir að C53UiG+5HPaxD2HPaxD er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU. Fullur texti ESB samræmisyfirlýsingar er að finna á eftirfarandi veffangi: https://mikrotik.com/products |
| LT | Aš, Mikrotīkls SIA, patvirtinu, kad radijo įrenginių tipas C53UiG+5HPaxD2HPaxD atitinka Direktyvą 2014/53/ES. Visas ES atitikties deklaracijos tekstas prieinamas šiuo interneto adresu: https://mikrotik.com/products |
| LV | Ar šo Mikrotīkls SIA deklarē, ka radioiekārta C53UiG+5HPaxD2HPaxD atbilst Direktīvai 2014/53/ES. Pilns ES atbilstības deklarācijas teksts ir pieejams šādā interneta vietnē: https://mikrotik.com/products |
| MT | B'dan, Mikrotīkls SIA, niddikjara li dan it-tip ta' tagħmir tar-radju C53UiG+5HPaxD2HPaxD huwa konformi mad-Direttiva 2014/53/UE. It-test kollu tad-dikjarazzjoni ta' konformità tal-UE huwa disponibbli f'dan l-indirizz tal-Internet li ġej: https://mikrotik.com/products |
| NL | Hierbij verklaar ik, Mikrotīkls SIA, dat het type radioapparatuur C53UiG+5HPaxD2HPaxD conform is met Richtlijn 2014/53/EU. De volledige tekst van de EU-conformiteitsverklaring kan worden geraadpleegd op het volgende internetadres: https://mikrotik.com/products |
| NO | Mikrotīkls SIA erklærer herved at utstyret C53UiG+5HPaxD2HPaxD er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU. Den fulle teksten til EU-samsvarserklæringen er tilgjengelig på følgende internettadresse: https://mikrotik.com/products |
| PL | Mikrotīkls SIA niniejszym oświadcza, że typ urządzenia radiowego C53UiG+5HPaxD2HPaxD jest zgodny z dyrektywą 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: https://mikrotik.com/products |
| PT | O(a) abaixo assinado(a) Mikrotīkls SIA declara que o presente tipo de equipamento de rádio C53UiG+5HPaxD2HPaxD está em conformidade com a Diretiva 2014/53/UE. O texto integral da declaração de conformidade está disponível no seguinte endereço de Internet: https://mikrotik.com/products |
| RO | Prin prezenta, Mikrotīkls SIA declară că tipul de echipamente radio C53UiG+5HPaxD2HPaxD este în conformitate cu Directiva 2014/53/UE. Textul integral al declarației UE de conformitate este disponibil la următoarea adresă internet: https://mikrotik.com/products |
| SK | Mikrotīkls SIA týmto vyhlasuje, že rádiové zariadenie typu C53UiG+5HPaxD2HPaxD je v súlade so smernicou 2014/53/EÚ. Úplné EÚ vyhlásenie o zhode je k dispozícii na tejto internetovej adrese: https://mikrotik.com/products |
| SL | Mikrotīkls SIA potrjuje, da je tip radijske opreme C53UiG+5HPaxD2HPaxD skladen z Direktivo 2014/53/EU. Celotno besedilo izjave EU o skladnosti je na voljo na naslednjem spletnem naslovu: https://mikrotik.com/products |
| SV | Härmed försäkrar Mikrotīkls SIA att denna typ av radioutrustning C53UiG+5HPaxD2HPaxD överensstämmer med direktiv 2014/53/EU. Den fullständiga texten till EU-försäkran om överensstämmelse finns på följande webbadress: https://mikrotik.com/products |

***WLAN***

| Operating Frequency / Maximum output power Betriebsfrequenz / maximale Ausgangsleistung Fréquence de fonctionnement / puissance de sortie maximale Frequenza operativa / massima potenza di uscita Frecuencia de funcionamiento / potencia de salida máxima Рабочая частота / максимальная выходная мощность | WLAN 2.4 GHz | 2400-2483.5 MHz / 20 dBm |
| --- | --- | --- |
| WLAN 5 GHz | 5150-5250 MHz / 23 dBm | |
| WLAN 5 GHz | 5250-5350 MHz / 20 dBm | |
| WLAN 5 GHz | 5470-5725 MHz / 27 dBm | |
| WLAN 5 GHz | 5725-5850 MHz / 14 dBm | |
| WLAN 5 GHz | 5850-5895 MHz / 14 dBm | |

This MikroTik device meets Maximum transmit power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.

The WLAN function for this device is restricted to indoor use only when operating in the 5150 to 5350 MHz frequency range. / Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.

![](./img/inkedpicto_li.webp)

| **(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:** | | | | |
| --- | --- | --- | --- | --- |
| (EN) Product Power Input Options (DE) Produkt Stromquellen Optionen (FR) Options d'entrée d'alimentation du produit (IT) Opzioni di ingresso alimentazione del prodotto (ES) Opciones de entrada de energía del producto (RU) Параметры входной мощности продукта | (EN) DC Adapter Output Specification(DE) Ausgangsspezifikationen des Gleichstromadapters(FR) Spécifications de sortie de l'adaptateur de courant continu(IT) Specifiche di uscita dell'adattatore di corrente continua(ES) Especificaciones de salida del adaptador de corriente continua(RU) Выходные характеристики адаптера постоянного тока | (EN) IP class of the enclosure (DE) IP-Klasse des Gehäuses (FR) Classe IP du boîtier (IT) Classe IP della custodia (ES) Clase de IP del recinto (RU) Класс защиты корпуса IP | (EN) Operating Temperature (DE)Betriebstemperatur (FR) température de fonctionnement (IT) temperatura di esercizio (ES) Temperatura de funcionamiento (RU) Рабочая Температура | |
| Voltage, V | Current, A | | | |
| DC Jack (12 - 28 V DC) PoE in Ethernet port (18 - 28 V DC) | 24 | 1.5 | IP20 | ±0° .. +70°C |
