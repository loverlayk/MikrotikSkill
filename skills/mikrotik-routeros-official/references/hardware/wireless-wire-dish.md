# Wireless Wire Dish

> The Wireless Wire Dish is a set of two LHG 60G devices that work in the 60 GHz wireless spectrum. Factory configured in pairs for an easy first start.

![](./img/api_rblhgg-60adkit.jpg)

## [Wireless Wire Dish](https://mikrotik.com/product/wireless_wire_dish) (RBLHGG-60adkit)

The Wireless Wire Dish is a set of two LHG 60G devices that work in the 60 GHz wireless spectrum. Factory configured in pairs for an easy first start.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- The Installation of the equipment must comply with local and national electrical codes.
- This unit is intended to be installed in the rackmount. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware or to follow the correct procedures could result in a hazardous situation to people and damage to the system.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity or hot environments.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.
- This is a class A device. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 51 centimeters from your body, occupational user, or the general public.

## Quickstart

- Assemble unit;
- Open the Ethernet door to connect an Ethernet cable to the Ethernet port, connect the other end of the Ethernet cable to the included PoE injector;
- Plug the PoE injector into your network switch;
- Plug the included power supply into the PoE injector to start up the device;
- Mount the devices on the mast or pole;
- Align both units;
- Download WinBox configuration tool https://mt.lv/winbox Default IP for the master unit: `192.168.88.2`, slave unit: `192.168.88.3`, user name: **admin** and password is printed on the label, that can be found inside the device cover;
- In case the IP connection is not available, please use the Neighbors tab and connect through MAC address;
- For LHG 60G models, the default IP: `192.168.88.1`, and there is no password;
- Once connected configure the device, so it has an active Internet connection https://mt.lv/configuration;
- Upgrade the RouterOS software to the latest version https://mt.lv/upgrade;
- Choose your country, to apply country regulation settings.

## Assembly

- Attach the two legs to the LHG case.
- Snap the assembled LHG unit to the grid in the appropriate locations.
- Fix the legs in place with two self thread screws (Use Phillips screwdriver PH2).

![](./img/worddavc893c24e5100f2845980f2d3e5241b28.webp)

## Mounting

![](./img/worddav40164c36a87ed55c59220370705742ba.webp)

- Attach the mounting assembly to the back of the device with four provided screws.
- Mount the assembled unit to the pole using the provided U bolt clamp. The clamping diameter with the provided steel clamp is 35 – 70 mm.

![](./img/worddavceb76a886f913df623cb750087a845c7.webp)

- Use the Aim tool to adjust your device. See the [Wireless Wire Dish product page](https://mikrotik.com/product/wireless_wire_dish) for mounting instructions.

![](./img/worddav5e6fe1d4900e51d20aa24c5099f03b9a.webp)

The device includes a grounding connection (marked ⏚) which you should connect to the grounding installation of the tower or building where the device will be used. This is to substantially reduce the risk of ESD and lightning damage. Grounding connector included in the package.

Warning! This equipment should be installed and operated with a minimum distance of 95 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.
The IP rating scale for this device is IP54.
*Mounting and configuration of this device should be done by a qualified person.*

## Extension slots and ports

- One Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- WiGig, 802.11ad.

## Powering

The devices accept powering from the Ethernet port. The Ethernet port accepts PoE input 12-57 V DC (passive and 802.3af/at). A power adapter and a passive PoE injector are included in the box. When using the PoE injector, make sure to use the "Power + Data" connector to connect to the device, and the "Data" connector to your PC, router, or switch.
**Connecting to a POE Adapter:**

- Connect the Ethernet cable from the device to the POE+DATA port of the POE adapter.
- Connect an Ethernet cable from your local network (LAN) to the POE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.
Maximum power consumption 5 W.

## Configuration

Full RouterOS documentation is located here: https://mt.lv/help Devices included in the Wireless Wire dish kit have been preconfigured with 60GHz and Ethernet interfaces in bridge mode. Another configuration has to be applied according to the documentation manual linked above.
Connect each of the Wireless Wire dish devices to your network using an Ethernet cable. To be able to communicate between these networks, devices have to be pointed at each other and be in direct line of sight. Once connected the devices will automatically bridge both networks.
Please get yourself familiar with additional information on the [W60G interface](/docs/wireless/w60g/).
Access devices by Ethernet cable, using the MikroTik WinBox utility. WinBox should be used to connect to the default IP address of 192.168.88.2 for the master device and 192.168.88.3 for the slave device. Username for login is admin and password is printed on the label that can be found inside the device cover.
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Buttons and jumpers

The routerBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when the green LED starts flashing, resets to password-protected state (~5 seconds)
- Release the button when the LED turns solid green to clear all configuration (~10 seconds)
- Release the button after LED is no longer lit (~20 seconds) to cause the device to look for Netinstall servers (required for reinstalling RouterOS over the network).
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## LED status

The device includes precise alignment guides using LEDs. The lights indicate with arrows direction to turn the dish if looking from behind the dish to the other end of the link. When alignment LEDs turn off, leaving only the "link established" LED, it means alignment is complete. The LED lights are:

![](../img/worddav18a753f3644737867efd8a4db9fa3be9.badge.webp)

- Tilt-up.
- Tilt down.
- Rotate to right.
- Rotate to left.
- LED on when the link established.
- LED on when Ethernet connected.
- User-configurable LED.
- Power state on.

## Accessories

The package includes the following accessories that come with the device:

- K-LHG screw set/fastening set.
- Gigabit POE injector.
- LHG-5G-390 mm Dish (mesh size 0.5 t x1.0 wx1.4 mm ).
- EU/US Switching Power Supply 24 V ⎓, 0.38 A, 9 W, Level VI, cable:1.5 m.
- Hose Clamp SUS304 (Philips type; clamping diameter range 35-70 mm).
- BRAC1_ LHG montage element.
- DynaDish U-Bolt M8 (A2 Stainless Steel).
- QuickMount AIM.

## Specifications

For more information about LHG products, specifications and pictures please visit our web page: https://mikrotik.com/product/wireless_wire_dish

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point. Scan QR code and choose your preferred OS.

![](../img/worddav90b536202301fa410028bd0e2ac949b9.badge.webp)

![](../img/worddavea6671dfbffe714b2f3abe6d04e7ad04.badge.webp)

This device meets the Maximum TX power limit per ETSI regulations. An Operational mode in the 60 GHz band:58.32 GHz, 60.48 GHz, 62.64 GHz. This device is certified for outdoor use in Point-to-multipoint applications. In the following countries, fixed service is allowed only in part of the band:

![](../img/tab.webp)

## Federal Communication Commission Interference Statement

FCC ID: TV7LHGG60AD

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation.

![](../img/fcc.badge.webp)

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense.

**FCC Caution:** Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

This device is not to be operated on aircraft except for the conditions listed on FCC CFR §15.255 (b)

**IMPORTANT NOTE. FCC Radiation Exposure Statement:**
This equipment complies with FCC radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 51cm between the radiator & your body.

## Innovation, Science and Economic Development Canada

IC: 7442A-LHGG60AD

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes : 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

This device is not to be operated on aircraft except for the conditions listed on ISED RSS-210 Annex J.1.

Cet appareil ne doit pas être utilisé sur un avion, sauf dans les conditions énumérées ISED RSS-210 Annex J.1.

**IMPORTANT NOTE. IC Radiation Exposure Statement:**
This equipment complies with IC RSS-102 radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance 51cm between the radiator & your body.
Cet équipement est conforme aux limites d'exposition aux rayonnements IC établies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé avec un minimum de 51cm de distance entre la source de rayonnement et votre corps.

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

Hereby, Mikrotīkls SIA declares that the radio equipment type RBLHGG-60adkit is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: https://mikrotik.com/products

### WiGig

| Operational channels / Maximum output power Betriebskanäle / maximale Ausgangsleistung Canaux opérationnels / puissance de sortie maximale Canali operativi / massima potenza di uscita Canales operacionales / potencia de salida máxima Операционные каналы / максимальная выходная мощность | 58.32 GHz / 40 dBm |
| --- | --- |
| 60.48 GHz / 40 dBm | |
| 62.64 GHz / 40 dBm | |
