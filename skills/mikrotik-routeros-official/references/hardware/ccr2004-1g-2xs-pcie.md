# CCR2004-1G-2XS-PCIe

> A smart PCIe network interface card that adds full-fledged router capabilities to your servers. The smart and easy way to create 25 Gigabit networks if you want to save space in your server room! See the...

![](./img/api_ccr2004-1g-2xs-pcie.jpg)

## [CCR2004-1G-2XS-PCIe](https://mikrotik.com/product/ccr2004_1g_2xs_pcie)

A smart PCIe network interface card that adds full-fledged router capabilities to your servers. The smart and easy way to create 25 Gigabit networks if you want to save space in your server room! See the [CCR2004-1G-2XS-PCIe product page](https://mikrotik.com/product/ccr2004_1g_2xs_pcie) for full specifications and brochures.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- The Installation of the equipment must comply with local and national electrical codes.
- This unit is intended to be installed in the rackmount. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity, or hot environments.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations. All MikroTik devices must be professionally installed.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures.

## Quickstart

- Insert the device into the PCIe slot of the computer;
- Turn on the computer;
- Configuration should be made using the WinBox configuration tool https://mt.lv/winbox Open the **Neighbors** tab and connect to the device using the MAC address;
- The user name: **admin**, by default there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

## Powering

The device uses power from PCIe with Maximum power consumption of 29W.

## Configuration

By default, the PCIe interface will show up as four virtual Ethernet interfaces. Two interfaces in passthrough mode to the 25G SFP28 cages. The remaining two virtual Ethernet-PCIe interfaces are bridged with the Gigabit Ethernet port for management access.

## Specifications

- Product code CCR2004-1G-2XS-PCIe
- CPU AL32400 2 GHz
- CPU architecture ARM 64bit
- CPU core count 4
- Size of RAM 4 GB
- RAM type DDR4
- Storage 128 MB, NAND
- Number of 1G Ethernet ports 1
- Number of 25G SFP28 ports 2
- Operating system RouterOS (License level 6)
- Dimensions 170 x 69 x 18 mm
- Operating temperature -20°C to +60°C
- Max power consumption 25 W

## Reset

![](./img/ccr2004_pcie.badge.webp)

To reset this device to factory settings you must turn off your PC.

- Place a metal object into the reset hole so that it makes contact with both metalized sides.
- Turn on the PC and hold the screwdriver until both 25G SFP28 LEDs starts flashing RED and then release it, it will reset the RouterOS configuration.
- If you Keep holding for more than 5 seconds up to 20 seconds until the red LEDs turns off, it to make the RouterBOARD look for Netinstall servers.

## Included Parts

![](./img/image2022-4-4_13-51-27.webp)

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

**The device is supported in Linux (minimum kernel 5.15.25) and RouterOS (minimum version 7.x), but it will not be recognized in Windows.**

https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net.git/commit/?id=bf8e59fd315f

![](../img/worddavf8766f69b74dff1d087a9fa824cd1a00.badge.webp)

 Safety Notice
Electric shock hazard. This equipment is to be serviced by trained personnel only.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as at designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

### Federal Communication Commission Interference Statement

![](../img/fcc.badge.webp)

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation.

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense

FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

### Innovation, Science and Economic Development Canada

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes : 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

### UKCA marking

![](../img/ukca.badge.gif)

## Eurasian Conformity Mark

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: MikroTikls SIA, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. Cм. на упаковке.

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

![](../img/eac.badge.webp)

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

## Norma Oficial Mexicana

EFICIENCIA ENERGETICA CUMPLE CON LA NOM-029-ENER-2017.

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.

Fabricante: MikroTikls SIA, Unijas iela 2, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## CE Declaration of Conformity

Manufacturer: MikroTikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

The full text of the EU Declaration of Conformity is available at the following internet address: https://mikrotik.com/products
