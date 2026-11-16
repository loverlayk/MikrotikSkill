# Wireless Wire Cube Pro, Cube 60Pro ac

> It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements....

![](./img/api_cubeg-5ac60aypair.jpg) ![](./img/image2022-4-4_15-5-46.webp)

:::info[This article covers]

- **[Wireless Wire Cube Pro](https://mikrotik.com/product/wireless_wire_cube_pro)** (CubeG-5ac60aypair)
- **[Cube 60Pro ac](https://mikrotik.com/product/cube_60pro_ac)** (CubeG-5ac60ay)

:::

It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- The Installation of the equipment must comply with local and national electrical codes.
- This unit is intended to be installed in the rackmount. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware or to follow the correct procedures could result in a hazardous situation to people and damage to the system.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity, or hot environments.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.
- This is a class A device. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 21 centimeters from your body, occupational user, or the general public.

## Quickstart

- Connect the device to the included PoE injector with Ethernet cable;
- Connect the PoE injector into the PC or to the network switch;
- Connect the power adapter to the PoE injector;
- Download the WinBox configuration tool https://mt.lv/winbox Open WinBox and connect to the device;
- Default IP: `192.168.88.2`/`192.168.88.3`, user name: **admin**, please find the password on the sticker;
- Download the latest RouterOS software from https://mikrotik.com/download;
- Choose ARM packages, and save them to your PC;
- Open WinBox and upload downloaded packages, drag and drop into any windows;
- Restart the device;
- Connect again and select your Region in the Wireless menu, W60G tab, and in the **QuickSet** menu set your Country, to apply country regulation settings.
*If the device RX blocking condition has happened device will restore its signal after a few seconds.*

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform to local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: https://mt.lv/help In case an IP connection is not available, the WinBox tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network (see ).
If the device loses connection, wait for a few seconds and then the device will recover connection automatically.

## Assembly and mounting

The device can be mounted on a vertical or horizontal pole. The maximum pole diameter is 51 mm.

Mounting and configuration of this device should be done by a certified person.

Choose your desired position, the device will require precise adjustment for best performance.

- Attach provided mount to the mast and secure with a screwdriver.
- Attach the device to the mounting bracket and secure using provided tool.

![](./img/image_pasted_at_2022-4-4_14-53.webp)

Even though the IP rating scale for this device is IP66, but when mounting outdoors, please ensure that any cable openings are directed downwards. We recommend using the POE injector and proper grounding with a Cat6 shielded cable. When using and installing this device please pay attention to the Maximum Permissible Exposure (MPE) safety distance with a minimum of 20 cm between the radiator and your body.

## Powering

The device accepts DC ⎓ power from Passive PoE injectors (one power supply and PoE injector are included) and accepts 18-48 V DC ⎓ consuming at a maximum load of 13 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Extension slots and ports

- Product code CubeG-5ac60ay / CubeG-5ac60ay-SA
- CPU 4 core IPQ-4019 716 MHz
- Size of RAM 256 MB
- Storage 64 MB flash
- Number of 1G Ethernet ports 1
- Wireless 5 GHz 802.11a/n/ac
- Wireless Chains 1
- Antenna gain (dBi) 11.5 5 GHz
- Antenna beamwidth 35° 5 GHz
- Antenna beamwidth at 60 GHz 11° (CubeG-5ac60ay); 60° (CubeG-5ac60ay-SA)
- GPS MT3337V
- WiGig chipset QCA6438
- WiGig antenna module SWL-QD46
- Supported protocol MikroTik 802.11ad / 802.11ay
- Max EIRP (dBm) 40
- Dimensions 115 x 95 x 82 mm (CubeG-5ac60ay) 115 x 211 x 90 mm (Cube G-5ac60ay-SA)
- Operating temperature -40°C to +70°C
- Operating system RouterOS, License level 4

## Reset button

![](./img/cubeg-5ac60aypair_reset.webp)

The routerBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause the device to look for Netinstall servers (required for reinstalling RouterOS over the network).
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

The package includes the following accessories that come with the device:

![](./img/image2022-4-4_15-2-42.webp)

## Operating system support

The device supports RouterOS software version *v6.49.5.* The specific factory-installed version number is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

### Federal Communication Commission Interference Statement

![](../img/fcc.badge.webp)

FCC ID: TV7CB5A60Y

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation.

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense.

FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

This device is not to be operated on aircraft except for the conditions listed on FCC CFR §15.255 (b)

IMPORTANT NOTE:
FCC Radiation Exposure Statement:
This equipment complies with FCC radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 20cm between the radiator & your body.
All cables used to connect peripherals must be shielded and grounded. Operation with cables connected to peripherals that are not shielded and grounded may result in interference to radio and television reception.

### Innovation, Science and Economic Development Canada

IC: 7442A-CB5A60Y

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes : 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

The device for operation in the band 5150–5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems.

Les dispositifs fonctionnant dans la bande de 5 150 à 5 250 MHz sont réservés uniquement pour une utilisation à l'intérieur afin de réduire les risques de brouillage préjudiciable aux systèmes de satellites mobiles utilisant les mêmes canaux.

This device is not to be operated on aircraft except for the conditions listed on ISED RSS-210 Annex J.1.

Cet appareil ne doit pas être utilisé sur un avion, sauf dans les conditions énumérées ISED RSS-210 Annex J.1.

IMPORTANT NOTE:
IC Radiation Exposure Statement:
This equipment complies with IC RSS-102 radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 20cm between the radiator & your body.
Cet équipement est conforme aux limites d'exposition aux rayonnements IC établies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé avec un minimum de 20cm de distance entre la source de rayonnement et votre corps.

### UKCA marking

![](../img/ukca.badge.gif)

### CE Declaration of Conformity

| *BG* | С настоящото Mikrotīkls SIA декларира, че този тип радиосъоръжение CubeG-5ac60ay, CubeG-5ac60ay-SA е в съответствие с Директива 2014/53/ЕС. Цялостният текст на ЕС декларацията за съответствие може да се намери на следния интернет адрес: https://mikrotik.com/products |
| --- | --- |
| CS | Tímto Mikrotīkls SIA prohlašuje, že typ rádiového zařízení CubeG-5ac60ay, CubeG-5ac60ay-SA je v souladu se směrnicí 2014/53/EU. Úplné znění EU prohlášení o shodě je k dispozici na této internetové adrese: https://mikrotik.com/products |
| DA | Hermed erklærer Mikrotīkls SIA , at radioudstyrstypen CubeG-5ac60ay, CubeG-5ac60ay-SA er i overensstemmelse med direktiv 2014/53/EU. EU-overensstemmelseserklæringens fulde tekst kan findes på følgende internetadresse: https://mikrotik.com/products |
| DE | Hiermit erklärt Mikrotīkls SIA , dass der Funkanlagentyp CubeG-5ac60ay, CubeG-5ac60ay-SA der Richtlinie 2014/53/EU entspricht. Der vollständige Text der EU-Konformitätserklärung ist unter der folgenden Internetadresse verfügbar: https://mikrotik.com/products |
| EL | Με την παρούσα ο/η Mikrotīkls SIA , δηλώνει ότι ο ραδιοεξοπλισμός CubeG-5ac60ay, CubeG-5ac60ay-SA πληροί την οδηγία 2014/53/ΕΕ. Το πλήρες κείμενο της δήλωσης συμμόρφωσης ΕΕ διατίθεται στην ακόλουθη ιστοσελίδα στο διαδίκτυο: https://mikrotik.com/products |
| EN | Hereby, Mikrotīkls SIA declares that the radio equipment type CubeG-5ac60ay, CubeG-5ac60ay-SA is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: https://mikrotik.com/products |
| ES | Por la presente, Mikrotīkls SIA declara que el tipo de equipo radioeléctrico CubeG-5ac60ay, CubeG-5ac60ay-SA es conforme con la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la dirección Internet siguiente: https://mikrotik.com/products |
| ET | Käesolevaga deklareerib Mikrotīkls SIA , et käesolev raadioseadme tüüp CubeG-5ac60ay, CubeG-5ac60ay-SA vastab direktiivi 2014/53/EL nõuetele. ELi vastavusdeklaratsiooni täielik tekst on kättesaadav järgmisel internetiaadressil: https://mikrotik.com/products |
| FI | Mikrotīkls SIA vakuuttaa, että radiolaitetyyppi CubeG-5ac60ay, CubeG-5ac60ay-SA on direktiivin 2014/53/EU mukainen. EU-vaatimustenmukaisuusvakuutuksen täysimittainen teksti on saatavilla seuraavassa internetosoitteessa: https://mikrotik.com/products |
| FR | Le soussigné, Mikrotīkls SIA , déclare que l'équipement radioélectrique du type CubeG-5ac60ay, CubeG-5ac60ay-SA est conforme à la directive 2014/53/UE. Le texte complet de la déclaration UE de conformité est disponible à l'adresse internet suivante: https://mikrotik.com/products |
| HR | Mikrotīkls SIA ovime izjavljuje da je radijska oprema tipa CubeG-5ac60ay, CubeG-5ac60ay-SA u skladu s Direktivom 2014/53/EU. Cjeloviti tekst EU izjave o sukladnosti dostupan je na sljedećoj internetskoj adresi: https://mikrotik.com/products |
| HU | Mikrotīkls SIA igazolja, hogy a CubeG-5ac60ay, CubeG-5ac60ay-SA típusú rádióberendezés megfelel a 2014/53/EU irányelvnek. Az EU-megfelelőségi nyilatkozat teljes szövege elérhető a következő internetes címen: https://mikrotik.com/products |
| IT | Il fabbricante, Mikrotīkls SIA , dichiara che il tipo di apparecchiatura radio CubeG-5ac60ay, CubeG-5ac60ay-SA è conforme alla direttiva 2014/53/UE. Il testo completo della dichiarazione di conformità UE è disponibile al seguente indirizzo Internet: https://mikrotik.com/products |
| IS | Hér með lýsir Mikrotīkls SIA því yfir að CubeG-5ac60ay, CubeG-5ac60ay-SA er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU. Fullur texti ESB samræmisyfirlýsingar er að finna á eftirfarandi veffangi: https://mikrotik.com/products |
| LT | Aš, Mikrotīkls SIA , patvirtinu, kad radijo įrenginių tipas CubeG-5ac60ay, CubeG-5ac60ay-SA atitinka Direktyvą 2014/53/ES. Visas ES atitikties deklaracijos tekstas prieinamas šiuo interneto adresu: https://mikrotik.com/products |
| LV | Ar šo Mikrotīkls SIA deklarē, ka radioiekārta CubeG-5ac60ay, CubeG-5ac60ay-SA atbilst Direktīvai 2014/53/ES. Pilns ES atbilstības deklarācijas teksts ir pieejams šādā interneta vietnē: https://mikrotik.com/products |
| MT | B'dan, Mikrotīkls SIA , niddikjara li dan it-tip ta' tagħmir tar-radju CubeG-5ac60ay, CubeG-5ac60ay-SA huwa konformi mad-Direttiva 2014/53/UE. It-test kollu tad-dikjarazzjoni ta' konformità tal-UE huwa disponibbli f'dan l-indirizz tal-Internet li ġej: https://mikrotik.com/products |
| NL | Hierbij verklaar ik, Mikrotīkls SIA , dat het type radioapparatuur CubeG-5ac60ay, CubeG-5ac60ay-SA conform is met Richtlijn 2014/53/EU. De volledige tekst van de EU-conformiteitsverklaring kan worden geraadpleegd op het volgende internetadres: https://mikrotik.com/products |
| NO | Mikrotīkls SIA erklærer herved at utstyret CubeG-5ac60ay, CubeG-5ac60ay-SA er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU. Den fulle teksten til EU-samsvarserklæringen er tilgjengelig på følgende internettadresse: https://mikrotik.com/products |
| PL | Mikrotīkls SIA niniejszym oświadcza, że typ urządzenia radiowego CubeG-5ac60ay, CubeG-5ac60ay-SA jest zgodny z dyrektywą 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: https://mikrotik.com/products |
| PT | O(a) abaixo assinado(a) Mikrotīkls SIA declara que o presente tipo de equipamento de rádio CubeG-5ac60ay, CubeG-5ac60ay-SA está em conformidade com a Diretiva 2014/53/UE. O texto integral da declaração de conformidade está disponível no seguinte endereço de Internet: https://mikrotik.com/products |
| RO | Prin prezenta, Mikrotīkls SIA declară că tipul de echipamente radio CubeG-5ac60ay, CubeG-5ac60ay-SA este în conformitate cu Directiva 2014/53/UE. Textul integral al declarației UE de conformitate este disponibil la următoarea adresă internet: https://mikrotik.com/products |
| SK | Mikrotīkls SIA týmto vyhlasuje, že rádiové zariadenie typu CubeG-5ac60ay, CubeG-5ac60ay-SA je v súlade so smernicou 2014/53/EÚ. Úplné EÚ vyhlásenie o zhode je k dispozícii na tejto internetovej adrese: https://mikrotik.com/products |
| SL | Mikrotīkls SIA potrjuje, da je tip radijske opreme CubeG-5ac60ay, CubeG-5ac60ay-SA skladen z Direktivo 2014/53/EU. Celotno besedilo izjave EU o skladnosti je na voljo na naslednjem spletnem naslovu: https://mikrotik.com/products |
| SV | Härmed försäkrar Mikrotīkls SIA att denna typ av radioutrustning CubeG-5ac60ay, CubeG-5ac60ay-SA överensstämmer med direktiv 2014/53/EU. Den fullständiga texten till EU-försäkran om överensstämmelse finns på följande webbadress: https://mikrotik.com/products |

This device meets the Maximum TX power limit per ETSI regulations. The frequency is 5470-5725MHz and the maximum transmitted power is less than 27dBm. The frequency and the maximum transmitted power in the EU are listed below: 57 - 66 GHz: 34.02 dBm. An Operational mode in the 60 GHz band: 58.32 GHz, 60.48 GHz, 62.64 GHz. This device is certified for outdoor use in Point to Multipoint applications. In the following countries this device cannot be used in Fixed Point-to-Point applications:

![](../img/tab.webp)

### WiGig

| Operational channels / Maximum output power Betriebskanäle / maximale Ausgangsleistung Canaux opérationnels / puissance de sortie maximale Canali operativi / massima potenza di uscita Canales operacionales / potencia de salida máxima Операционные каналы / максимальная выходная мощность | 58.32 GHz / &lt;40 dBm |
| --- | --- |
| 60.48 GHz / &lt;40 dBm | |
| 62.64 GHz / &lt;40 dBm | |

### WLAN

| Operating Frequency / Maximum output power Betriebsfrequenz / maximale Ausgangsleistung Fréquence de fonctionnement / puissance de sortie maximale Frequenza operativa / massima potenza di uscita Frecuencia de funcionamiento / potencia de salida máxima Рабочая частота / максимальная выходная мощность | 5470-5725 MHz / 27 dBm |
| --- | --- |

| **(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:** | | | | |
| --- | --- | --- | --- | --- |
| (EN) Product Power Input Options (DE) Produkt Stromquellen Optionen (FR) Options d'entrée d'alimentation du produit (IT) Opzioni di ingresso alimentazione del prodotto (ES) Opciones de entrada de energía del producto (RU) Варианты входной мощности продукта | (EN) DC Adapter Output Specification (DE) Ausgangsspezifikationen des Gleichstromadapters (FR) Spécifications de sortie de l'adaptateur de courant continu (IT) Specifiche di uscita dell'adattatore di corrente continua (ES) Especificaciones de salida del adaptador de corriente continua (RU) Выходные характеристики адаптера постоянного тока | (EN) IP class of the enclosure (DE) IP-Klasse des Gehäuses (FR) Classe IP du boîtier (IT) Classe IP della custodia (ES) Clase de IP del recinto (RU) Класс защиты корпуса IP | (EN) Operating Temperature (DE)Betriebstemperatur (FR) température de fonctionnement (IT) temperatura di esercizio (ES) Temperatura de funcionamiento (RU) Рабочая Температура | |
| Voltage, V | Current, A | | | |
| PoE In Ethernet Port (18 - 48 V DC) | 24 | 0.8 | IP54 | -33°..+70°C |
