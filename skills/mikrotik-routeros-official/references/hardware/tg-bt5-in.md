# TG-BT5-IN

> TG-BT5-IN is ready to use Bluetooth Tag with a preinstalled battery. The software manual you can find under each product in the Support and Downloads sections https://mikrotik.com/products. See the TG-BT5-IN product...

![](./img/api_tg-bt5-in.jpg)

TG-BT5-IN is ready to use Bluetooth Tag with a preinstalled battery. The software manual you can find under each product in the Support and Downloads sections https://mikrotik.com/products. See the [TG-BT5-IN product page](https://mikrotik.com/product/tg_bt5_in) for full specifications and brochures.

## Software-related links

You can find the guide on how to configure the tag using the Android app following the link:

MikroTik Beacon Manager for Android devices

You can find the guide on how to configure the tag using the iOS app following the link:

MikroTik Beacon Manager for iOS devices

You can find more information about the tag's advertisement formats following the link:

MikroTik Tag advertisement formats

## Indoor slim rectangular shape - TG-BT5-IN

![](./img/image2021-9-9_8-56-45.badge.webp)

- Temperature range -20..+60°C.
- Built-in accelerometer.
- Magnet activation.
- Dimensions 35x22x7mm.
- BLE 5.2 with Silabs BG22.
- Weatherproof (sealed) version with a built-in non-replaceable LiMnO2 CR2032 (220mAh) battery.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- The Installation of the equipment must comply with local and national electrical codes.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity or hot environments.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

## Overview

TG-BT5-IN is a new addition to our MikroTik equipment. It is a Bluetooth tag (a very small gadget) that can be attached to other equipment or other belonging. Bluetooth tags play a big role in IoT topologies, where Bluetooth is used to broadcast the data over short distances. Once installed and configured, the tag will broadcast advertising packets in iBeacon, Eddystone, or MikroTik telemetry (default packet format) to the gateway (for example, KNOT). Gateway, on the other hand, pushes the advertising packet payload to the remote server utilizing MQTT or HTTP protocols.

## Tag modes

When the product arrives from manufacturing it is set into factory sleep mode. In this mode, all components are shut-down as much as possible and MCU is put into the deepest sleep state. The current draw is reduced to a minimum, so this is the preferred mode to use when the tag is stored and/or not in use. To exit this mode put a magnet to the tag's edge (where the "Magnetic switch" is) and hold it for 3-10 seconds until LED turns off. After that, the tags exits sleep mode and enters advertising mode.

In the Advertising mode, the tag will broadcast Bluetooth advertising packets. By default, MikroTik's advertisement packets are sent once every 5 seconds. This can be changed in the Configuration mode.

Configuration mode can be entered only from advertising mode by applying a magnet to the magnetic switch as in the exiting factory sleep procedure. After applying a magnet for 5-10 seconds LED will turn off and the tag enters configuration mode. If you apply a magnet for longer than 15 seconds or won't connect to the tag with the configuration app, it will go back into advertising mode.

When the device wakes from the factory sleep for the first time, it has this default configuration:

| Configuration parameter | Setting/value |
| --- | --- |
| Advertising packet format | MikroTik |
| Advertising interval | 5.0 seconds |
| Angle Threshold/Tilt trigger | 60° |
| Freefall Threshold/Accelerometer trigger | 156.25 mg |
| Wakeup Threshold/Wakeup trigger | 1.0 mg |
| Bandwith Filter | 0.8 Hz |
| Low noise filter | disabled |
| Tx Power | 0 dBm |

The magnet is used on the reed switch to change the tag's operating modes as described above. As soon as the magnet is detected (the reed switch is activated), the LED will start flashing for the next 5 seconds (first 5 seconds) and, then, stop. It can help you identify that 5 seconds have passed and that you can remove the magnet to enter configuration mode.

![](./img/image2021-3-9_11-7-7.webp)

## Initial steps

Install the "MikroTik Beacon Manager" application and run the app.

For Android devices, you can find it following the link.

- Upon the first login, you will see the list of the nearby devices (devices in either advertising mode or configuration mode):

![](../img/image2021-3-9_11-13-41.webp)

To "wake up" the tag from the factory sleep mode, the reed switch should be activated for 3-10 seconds.

- As soon as the device "wakes up", it will show up in the "MikroTik Beacon Manager" list. Select the tag and you can begin configuring it by pressing the "CONFIG ONLY" button:

![](../img/image2021-6-8_14-35-17.webp)

![](../img/image2021-6-8_14-35-39.webp)

- Right after that, you will need to put a magnet over the device for 10 seconds (this is the step where the device is set to the configuration mode):

![](../img/image2021-3-9_11-22-47.webp)

- After a short wind up time, the device should be ready to be configured:

![](../img/image2021-3-9_11-32-30.webp)

The app will show general information about the tag in the "Status" tab and will allow you to alter the tag's setting using the "Settings" tab (as shown in the screenshot above).

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Federal Communication Commission Interference Statement

| Model | FCC ID |
| --- | --- |
| TG-BT5-IN | TV7-TB5I |

This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation.

![](../img/fcc.badge.webp)

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and receiver.
- Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help.
**FCC Caution:** Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

## Innovation, Science and Economic Development Canada

| Model | IC |
| --- | --- |
| TG-BT5-IN | 7442A-TB5I |

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

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

Hereby, Mikrotīkls SIA declares that the radio equipment type TG-BT5-IN is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: https://mikrotik.com/products

### Bluetooth

| (EN) Operating Frequency / Maximum output power (DE) Betriebsfrequenz / maximale Ausgangsleistung (FR) Fréquence de fonctionnement / puissance de sortie maximale (IT) Frequenza operativa / massima potenza di uscita (ES) Frecuencia de funcionamiento / potencia de salida máxima (RU) Рабочая частота / максимальная выходная мощность | Bluetooth | 2400-2483.5 MHz / 3.5 dBm |
| --- | --- | --- |

**Bluetooth Qualified Product

![](../img/bluetooth-logo.webp)

This product has successfully completed Bluetooth Qualification Process. For more information on Bluetooth Qualified products please use the following link: https://launchstudio.bluetooth.com/Listings/Search
