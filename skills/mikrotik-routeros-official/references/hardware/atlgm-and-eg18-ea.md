# ATLGM&EG18-EA

> An advanced technology level (ATL) LTE solution with wide range MIMO 4x4 antennas for fast and stable connectivity in rural and urban areas. Make the most of your mobile coverage! See the ATL LTE18 kit product page...

![](./img/api_atlgm_eg18-ea.jpg)

## [ATL LTE18 kit](https://mikrotik.com/product/atl18) (ATLGM&EG18-EA)

An advanced technology level (ATL) LTE solution with wide range MIMO 4x4 antennas for fast and stable connectivity in rural and urban areas. Make the most of your mobile coverage! See the [ATL LTE18 kit product page](https://mikrotik.com/product/atl18) for full specifications and brochures.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- All installation methods for mounting an access point on any wall surface are subject to the acceptance of local jurisdiction.
- The Installation of the equipment must comply with local and national electrical codes.
- This product is intended to be mounted outdoors on a pole. Read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Use this product with care and operate at your own risk!
- In the case of device failure, disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.
- This is a class A device. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

## Quickstart

- Open the Ethernet port door;
- Insert the SIM card into the slot, with the chip facing UP;
- Connect the device to the included PoE injector with an Ethernet cable to the data+power end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Configure your device using a web browser through **WebFig** or the **WinBox** tool at https://mt.lv/winbox Access **WebFig** by opening http://192.168.188.1, and for **WinBox**, download the tool, navigate to the **Neighbors** tab, and select the MAC address. The username is "**admin**" with no password (or, for some models, check user and wireless passwords on the sticker);
- Enter the PIN code, if required by your mobile network operator;
- Select the "Check for updates" button and update RouterOS to the latest version. Must have a valid SIM card inserted and active Internet connection;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- The device will reboot;
- Connect again and in the **QuickSet** menu set a strong password.

![](./img/image-2022-11-10_9-39-16.webp)

## Powering

- Number of DC inputs 1
- DC input type PoE-in (12-57)
- Power adapter nominal voltage 24 V
- Power adapter nominal current 0.8 A
- Max power consumption without attachments 8 W
- Max power consumption 8 W

## Mounting

- Slide the included metallic mounting rings into the two slots on the back of the antenna dish.
- Attach the unit to a pole, with the Ethernet port pointing downward.
- Use a PH2 screwdriver to tighten the rings.
- Fix the Ethernet cable to the pole using zip ties, less than one meter from the unit, to avoid the cable being pulled out of the port.
- Check mounting angle and positioning.
 When mounting outdoors, ensure that any cable openings are directed downwards. Use a POE injector and proper grounding, this device has a specially-designed grounding connector under the port cover. Recommended using shielded Cat5/6 cable. The IP rating scale for this device is IP54.

## Configuration

Once logged in, you should select the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, make sure you have selected the country where the device will be used, to conform to local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: https://mt.lv/help In case an IP connection is not available, the WinBox tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see the section .

## Accessories

The package includes the following accessories that come with the device:

![](../img/image-2022-10-4_11-52-31.webp)

## Extension slots and ports

- Product code ATLGM&EG18-EA
- CPU Dual-core 88F3720 1.2 GHz
- CPU architecture ARM 64bit
- Size of RAM 256 MB
- RAM type DDR3L
- Storage 16 MB, Flash
- Number of 1G Ethernet ports 1
- LTE modem R11mL-EG18-EA
- TAC 86981604
- LTE Category 18 (1.2Gbps Downlink, 150Mbps Uplink)
- LTE bands 1 (2100MHz) / 3 (1800MHz) / 5 (850MHz) / 7 (2600MHz) / 8 (900 MHz) / 20 (800MHz) / 28 (700MHz) / 38 (2600MHz) / 40 (2300MHz) / 41 (2500MHz)
- 3G Category R8 (42.2Mbps Downlink, 11.2Mbps Uplink)
- 3G Bands 1 (2100MHz) / 3 (1800MHz) / 5 (850MHz) / 8 (900MHz)
- Dimensions 315 mm diameter x 170 mm depth
- Operating system RouterOS, License level 3
- Operating temperature -40°C to +70°C

## SIM slot usage

![](../img/worddav1617cee4086cb64136be15fb67b20679.webp)

SIM card slot is designed to be used with Micro SIM cards.
Nano SIM cards have different thicknesses and usage with an adapter is not recommended.

## Reset button

The reset button has three functions:

- Hold this button during boot time until the LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds);
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total of 10 seconds);
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total of 15 seconds);
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, separate the device from household waste and dispose of it in a safe manner, such as at designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

### CE Declaration of Conformity

| *BG* | С настоящото Mikrotīkls SIA декларира, че този тип радиосъоръжение ATLGM&EG18-EA е в съответствие с Директива 2014/53/ЕС. Цялостният текст на ЕС декларацията за съответствие може да се намери на следния интернет адрес: https://mikrotik.com/products |
| --- | --- |
| CS | Tímto Mikrotīkls SIA prohlašuje, že typ rádiového zařízení ATLGM&EG18-EA je v souladu se směrnicí 2014/53/EU. Úplné znění EU prohlášení o shodě je k dispozici na této internetové adrese: https://mikrotik.com/products |
| DA | Hermed erklærer Mikrotīkls SIA, at radioudstyrstypen ATLGM&EG18-EA er i overensstemmelse med direktiv 2014/53/EU. EU-overensstemmelseserklæringens fulde tekst kan findes på følgende internetadresse: https://mikrotik.com/products |
| DE | Hiermit erklärt Mikrotīkls SIA, dass der Funkanlagentyp ATLGM&EG18-EA der Richtlinie 2014/53/EU entspricht. Der vollständige Text der EU-Konformitätserklärung ist unter der folgenden Internetadresse verfügbar: https://mikrotik.com/products |
| EL | Με την παρούσα ο/η Mikrotīkls SIA, δηλώνει ότι ο ραδιοεξοπλισμός ATLGM&EG18-EA πληροί την οδηγία 2014/53/ΕΕ. Το πλήρες κείμενο της δήλωσης συμμόρφωσης ΕΕ διατίθεται στην ακόλουθη ιστοσελίδα στο διαδίκτυο: https://mikrotik.com/products |
| EN | Hereby, Mikrotīkls SIA declares that the radio equipment type ATLGM&EG18-EA is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: https://mikrotik.com/products |
| ES | Por la presente, Mikrotīkls SIA declara que el tipo de equipo radioeléctrico ATLGM&EG18-EA es conforme con la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la dirección Internet siguiente: https://mikrotik.com/products |
| ET | Käesolevaga deklareerib Mikrotīkls SIA, et käesolev raadioseadme tüüp ATLGM&EG18-EA vastab direktiivi 2014/53/EL nõuetele. ELi vastavusdeklaratsiooni täielik tekst on kättesaadav järgmisel internetiaadressil: https://mikrotik.com/products |
| FI | Mikrotīkls SIA vakuuttaa, että radiolaitetyyppi ATLGM&EG18-EA on direktiivin 2014/53/EU mukainen. EU-vaatimustenmukaisuusvakuutuksen täysimittainen teksti on saatavilla seuraavassa internetosoitteessa: https://mikrotik.com/products |
| FR | Le soussigné, Mikrotīkls SIA, déclare que l'équipement radioélectrique du type ATLGM&EG18-EA est conforme à la directive 2014/53/UE. Le texte complet de la déclaration UE de conformité est disponible à l'adresse internet suivante: https://mikrotik.com/products |
| HR | Mikrotīkls SIA ovime izjavljuje da je radijska oprema tipa ATLGM&EG18-EA u skladu s Direktivom 2014/53/EU. Cjeloviti tekst EU izjave o sukladnosti dostupan je na sljedećoj internetskoj adresi: https://mikrotik.com/products |
| HU | Mikrotīkls SIA igazolja, hogy a ATLGM&EG18-EA típusú rádióberendezés megfelel a 2014/53/EU irányelvnek. Az EU-megfelelőségi nyilatkozat teljes szövege elérhető a következő internetes címen: https://mikrotik.com/products |
| IT | Il fabbricante, Mikrotīkls SIA, dichiara che il tipo di apparecchiatura radio ATLGM&EG18-EA è conforme alla direttiva 2014/53/UE. Il testo completo della dichiarazione di conformità UE è disponibile al seguente indirizzo Internet: https://mikrotik.com/products |
| IS | Hér með lýsir Mikrotīkls SIA því yfir að ATLGM&EG18-EA er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU. Fullur texti ESB samræmisyfirlýsingar er að finna á eftirfarandi veffangi: https://mikrotik.com/products |
| LT | Aš, Mikrotīkls SIA, patvirtinu, kad radijo įrenginių tipas ATLGM&EG18-EA atitinka Direktyvą 2014/53/ES. Visas ES atitikties deklaracijos tekstas prieinamas šiuo interneto adresu: https://mikrotik.com/products |
| LV | Ar šo Mikrotīkls SIA deklarē, ka radioiekārta ATLGM&EG18-EA atbilst Direktīvai 2014/53/ES. Pilns ES atbilstības deklarācijas teksts ir pieejams šādā interneta vietnē: https://mikrotik.com/products |
| MT | B'dan, Mikrotīkls SIA, niddikjara li dan it-tip ta' tagħmir tar-radju ATLGM&EG18-EA huwa konformi mad-Direttiva 2014/53/UE. It-test kollu tad-dikjarazzjoni ta' konformità tal-UE huwa disponibbli f'dan l-indirizz tal-Internet li ġej: https://mikrotik.com/products |
| NL | Hierbij verklaar ik, Mikrotīkls SIA, dat het type radioapparatuur ATLGM&EG18-EA conform is met Richtlijn 2014/53/EU. De volledige tekst van de EU-conformiteitsverklaring kan worden geraadpleegd op het volgende internetadres: https://mikrotik.com/products |
| NO | Mikrotīkls SIA erklærer herved at utstyret ATLGM&EG18-EA er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU. Den fulle teksten til EU-samsvarserklæringen er tilgjengelig på følgende internettadresse: https://mikrotik.com/products |
| PL | Mikrotīkls SIA niniejszym oświadcza, że typ urządzenia radiowego ATLGM&EG18-EA jest zgodny z dyrektywą 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: https://mikrotik.com/products |
| PT | O(a) abaixo assinado(a) Mikrotīkls SIA declara que o presente tipo de equipamento de rádio ATLGM&EG18-EA está em conformidade com a Diretiva 2014/53/UE. O texto integral da declaração de conformidade está disponível no seguinte endereço de Internet: https://mikrotik.com/products |
| RO | Prin prezenta, Mikrotīkls SIA declară că tipul de echipamente radio ATLGM&EG18-EA este în conformitate cu Directiva 2014/53/UE. Textul integral al declarației UE de conformitate este disponibil la următoarea adresă internet: https://mikrotik.com/products |
| SK | Mikrotīkls SIA týmto vyhlasuje, že rádiové zariadenie typu ATLGM&EG18-EA je v súlade so smernicou 2014/53/EÚ. Úplné EÚ vyhlásenie o zhode je k dispozícii na tejto internetovej adrese: https://mikrotik.com/products |
| SL | Mikrotīkls SIA potrjuje, da je tip radijske opreme ATLGM&EG18-EA skladen z Direktivo 2014/53/EU. Celotno besedilo izjave EU o skladnosti je na voljo na naslednjem spletnem naslovu: https://mikrotik.com/products |
| SV | Härmed försäkrar Mikrotīkls SIA att denna typ av radioutrustning ATLGM&EG18-EA överensstämmer med direktiv 2014/53/EU. Den fullständiga texten till EU-försäkran om överensstämmelse finns på följande webbadress: https://mikrotik.com/products |

### WLAN/LTE

| Operating Frequency / Maximum output power Betriebsfrequenz / maximale Ausgangsleistung Fréquence de fonctionnement / puissance de sortie maximale Frequenza operativa / massima potenza di uscita Frecuencia de funcionamiento / potencia de salida máxima Рабочая частота / максимальная выходная мощность | WCDMA Band I | 2100 MHz / 24dBm ± 2.7 dB |
| --- | --- | --- |
| WCDMA Band III | 1800 MHz / 24dBm ± 2.7 dB | |
| WCDMA Band V | 850 MHz / 24dBm ± 2.7 dB | |
| WCDMA Band VIII | 900 MHz / 24dBm ± 2.7 dB | |
| LTE Band 1 | 2100 MHz / 23dBm ± 2.7 dB | |
| LTE Band 3 | 1700 MHz / 23dBm ± 2.7 dB | |
| LTE Band 5 | 850 MHz / 23dBm ± 2.7 dB | |
| LTE Band 7 | 2600 MHz / 23dBm ± 2.7 dB | |
| LTE Band 8 | 900 MHz / 23dBm ± 2.7 dB | |
| LTE Band 20 | 800 MHz / 23dBm ± 2.7 dB | |
| LTE Band 28 | 700 MHz / 23dBm ± 2.7 dB | |
| LTE Band 38 | 2600 MHz / 23dBm ± 2.7 dB | |
| LTE Band 40 | 2300 MHz / 23dBm ± 2.7 dB | |

This MikroTik device meets Maximum TX power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

| **(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques /(IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:** | | | | |
| --- | --- | --- | --- | --- |
| (EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Параметры входной мощности продукта | (EN) DC Adapter Output Specification(DE) Ausgangsspezifikationen des Gleichstromadapters(FR) Spécifications de sortie de l'adaptateur de courant continu(IT) Specifiche di uscita dell'adattatore di corrente continua(ES) Especificaciones de salida del adaptador de corriente continua(RU) Выходные характеристики адаптера постоянного тока | (EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP | (EN) Operating Temperature(DE)Betriebstemperatur (FR) température de fonctionnement (IT) temperatura di esercizio (ES) Temperatura de funcionamiento (RU) Рабочая Температура | |
| Voltage, V | Current, A | | | |
| PoE In Ethernet Port (12 - 57 V DC) | 24 | 0.8 | IP54 | -33°..+70°C |
