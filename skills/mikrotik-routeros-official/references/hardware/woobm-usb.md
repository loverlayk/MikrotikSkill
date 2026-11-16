# Woobm-USB

> The Woobm is a WiFi-to-serial bridge. This device enables wireless access to RouterBOARD devices which have a USB port but do not have wireless interfaces. The device operates in 2GHz 802.11b/g/n wireless mode and...

![](./img/api_woobm-usb.webp)

The Woobm is a WiFi-to-serial bridge. This device enables wireless access to RouterBOARD devices which have a USB port but do not have wireless interfaces. The device operates in 2GHz 802.11b/g/n wireless mode and supports both client and access point modes, which can be protected with a WPA wireless password (for some models, check user and wireless passwords on the sticker). See the [Woobm-USB product page](https://mikrotik.com/product/woobm) for full specifications and brochures.

## Powering

The device accepts power from the USB port of the RouterBOARD device.

## First startup

Connect your Woobm-USB to the USB port, open a wireless network with SSID: WoobmAP will be created. Connect to device and open device IP address in a web browser.

Default Woobm-USB IP is **192.168.4.1**

A device running RouterOS will automatically mount as a serial USB device and provide access after successful login.

## WEB interface

WEB interface allows access to the serial port from devices equipped with an 802.11b/g/n 2.4GHz wireless module.

![](./img/799px-woobm2.webp)

Web interface default page is "Home" From the home page, it is possible to connect and configure RouterOS neighbor devices (MikroTik devices in the same network) Press on a device IP address to establish a connection:

![](./img/woobm3.webp)

By opening the Terminal tab, Woobm-USB will try to emulate the USB serial interface. On a successful attempt "Connection successful! " message will appear above the terminal window. You can enter commands from the keyboard or use key buttons to send out commands through the USB serial interface.

Show keyboard will bring up the keyboard on mobile devices. Extra buttons provide missing keyboard keys for mobile devices.

By opening the Terminal tab, Woobm-USB will try to emulate the USB serial interface. On a successful attempt "Connection successful! " message will appear above the terminal window. You can enter commands from the keyboard or use key buttons to send out commands through the USB serial interface.

Show keyboard will bring up the keyboard on mobile devices. Extra buttons provide missing keyboard keys for mobile devices.

## Settings

Settings tab provides basic configuration for Woobm-USB device. The **basic settings** part provide serial port, button, LED, and wireless general settings

![](./img/woobm10.webp)

### Properties

| Property | Description |
| --- | --- |
| **Identity** (*string*; Default: **MikroTik**) | Device identity is used for the DHCP client as the 'hostname' parameter when reporting it to the DHCP server and for neighbor discovery. |
| **Telnet port** (*integer*; Default: **23**) | Port used for incoming telnet requests |
| **Baud-rate** (*integer*; Default: **115200**) | Baud rate used for serial communication. Should match a host device. |
| **Data bits** (; Default:**8**) | |
| **Parity** (; Default:**None bits**) | |
| **Stopbits** (*integer*; Default: **1**) | |
| **Web conn. timeout** (*integer*; Default: **2400**) | |
| **WPS enabled** (*On/off*; Default: **On**) | |
| **Set the default settings with a button** (*On/off*; Default: **On**) | |
| **Device greeting** (*On/off*; Default: **On**) | |
| **Force echo** (*On/off*; Default: **On**) | |
| **Ignore telnet commands** (*On/off*; Default: **On**) | |
| **Status LEDs enabled** (*On/off*; Default: **On**) | |
| **802.11 mode** (; Default:**default**) | |

**WiFi Station** settings part provides settings wireless for Woobm-USB in client mode.

![](./img/woobm11.webp)

| Property | Description |
| --- | --- |
| **SSID** (*string*; Default: ) | Provide SSID of nearby Access Point, or use scan function. |
| **Password** (*string*; Default: ) | WPA-PSK and WPA2-PSK |
| **SSID MAC** (*MAC*; Default: ) | |
| **Station MAC** (*MAC*; Default: ) | |
| **IP address** (*IP*; Default: ) | |
| **Gateway** (*IP*; Default: ) | |
| **Netmask** (*IP*; Default: ) | |

**WiFi AP** settings part provides wireless settings for Woobm-USB in Access Point mode.

![](./img/woobm12.webp)

| Property | Description |
| --- | --- |
| **SSID** (*string*; Default: ) | SSID of Woobm-USB Access Point |
| **Password** (*string*; Default: ) | WPA-PSK and WPA2-PSK |
| **Channel** (; Default:**6**) | Wireless channel used for AP |
| **Auth. mode** (; Default: ) | |
| **Hidden** (*On/Off*; Default: **Off**) | |
| **Max conn** (*1 to 4*; Default: **4**) | Maximum allowed clients to Access Point. |
| **Beacon interval** (*100 to 60000*; Default: **100**) | How often Access point broadcasts AP information. |
| **IP address** (*IP*; Default: **192.168.4.1**) | |
| **Gateway** (*IP*; Default: ) | |
| **Netmask** (*IP*; Default: ) | |
| **AP MAC** (*MAC*; Default: ) | |
| **DHCP Enabled** (*On/Off*; Default: **On**) | Enable/disable DHCP server |
| **IP range start** (*IP*; Default: **192.168.4.2**) | |
| **IP range end** (*IP*; Default: **192.168.4.5**) | |
| **IP lease time** (; Default:**120**) | |

## Upgrade firmware

Use the upgrade firmware tab for manual firmware upgrade. Firmware is available in the Product Support & Download section on our web page.

## Telnet access

It's possible to use Telnet clients to access the serial port. For Telnet access open Woobm-USB address in telnet client. Woobm-USB forwards serial port to telnet client.

Only one instance of the serial port bridge may be emulated.

## Button functionality

Button provides functionality for enabling WPS, reset configuration and send out a neighbor message (MNDP).

### WPS mode

If a button is pressed for less than 5 seconds - WPS mode is enabled. If a connection is made to the Access point - the Woobm station configuration is saved and old data is overwritten.

### Reset configuration

To reset configuration:

1) Woobm should be unplugged (removed from the USB port);

2) Press and hold the button;

3) Attach Woobm to the USB port while holding the button;

4) Wait till the red LED light starts blinking;

5) Release button;

The device will reset be reset to the default configuration.

#### Neighbor message

The neighbor message is sent out automatically every minute. To send a message out manually hold the button for at least 5 seconds until the LED light stops blinking.

## Operating system support

 The device supports Woobm software only. It can be updated, by uploading a newer.BIN file through the web configuration page.

## Federal Communication Commission Interference Statement

| Model | FCCID |
| --- | --- |
| Woobm-USB | TV7WBM |

This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation.

![](../img/fcc.badge.webp)

This equipment generates, uses and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and receiver.
- Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help.
**FCC Caution:** Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate this equipment.
This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation. This device and its antenna must not be co-located or operation in conjunction with any other antenna or transmitter.
This device is acting as slave/MASTER and operating in the 2.4 GHz (2412 ~2472 MHz) band.
**RF Exposure Information:** The EUT is compliance with SAR for general population/uncontrolled exposure limits in IC RSS-102 and had been tested in accordance with the measurement methods and procedures specified in IEEE 1528. This equipment should be installed and operated with minimum distance 20 cm between the radiator and your body.

## Innovation, Science and Economic Development Canada

| Model | IC |
| --- | --- |
| Woobm-USB | 7442A-WBM |

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
| 2412-2472 МГц | ≤100 мВт |

*Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: MikroTikls SIA, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. Cм. на упаковке.

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу. Информация об импортерах продукции MikroTik в Российскую Федерацию: https://mikrotik.com/buy/europe/russia

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

![](../img/eac.badge.webp)

## Norma Oficial Mexicana

Rango de frecuencia (potencia de salida máxima): 2412-2472 MHz (30 dBm). Los canales de frecuencia disponibles pueden variar según el modelo y la certificación del producto.

EFICIENCIA ENERGETICA CUMPLE CON LA NOM-029-ENER-2017.

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.
Fabricante: MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## The National Commission for the State Regulation of Communications and Informatization by Ukraine

Виробник: MikroTikls SIA, Brivibas gatve 214i Рига, Латвія, LV1039.

Робоча частота (Максимальна вихідна потужність): 2412-2472 МГц (20 дБм).

Справжнім MikroTikls SIA заявляє, що маршрутизатор відповідає основним вимогам та іншим відповідним положенням директиви 2014/53/EC, а також суттєвим вимогам Технічного регламенту радіообладнання, затвердженого постановою Кабінету Міністрів України від 24 травня 2017 року № 355.

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE Declaration of Conformity

![](./img/worddav426ecf203ac703c225f5aebc506dc498.badge.webp)

Manufacturer: MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

Hereby, Mikrotīkls SIA declares that the Woobm-USB is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: https://mikrotik.com/products

### Frequency bands terms of use

| **Frequency range (for applicable models)** | **Channels used** | **Maximum Output Power (EIRP)** | **Restriction** |
| --- | --- | --- | --- |
| 2412 - 2472 MHz | 1 - 13 | 20 dBm | Without any restriction to use in all EU Member States |

** It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed!*
