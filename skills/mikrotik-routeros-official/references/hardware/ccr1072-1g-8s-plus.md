# CCR1072-1G-8S+

> The CCR1072-1G-8S+ is a high-performance multicore router with eight SFP+ cages. Ports are directly connected to a Tilera 72 core CPU and assisted by 16 GB of built-in ECC RAM. See the CCR1072-1G-8S+ product page for...

![](./img/api_ccr1072-1g-8s_.webp)

## [CCR1072-1G-8S+](https://mikrotik.com/product/CCR1072-1G-8Splus)

The CCR1072-1G-8S+ is a high-performance multicore router with eight SFP+ cages. Ports are directly connected to a Tilera 72 core CPU and assisted by 16 GB of built-in ECC RAM. See the [CCR1072-1G-8S+ product page](https://mikrotik.com/product/CCR1072-1G-8Splus) for full specifications and brochures.

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
- It is the customer's responsibility to follow local country regulations. All MikroTik devices must be professionally installed.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures.

## Quickstart

- Connect your PC to the **MGMT/BOOT** labeled port or the first Ethernet port;
- Connect the device to a power source;
- Configure the IP settings of your network card to `192.168.88.2/24`;
- Configuration should be made using **WebFig** in a web browser or the **WinBox** configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Open `192.168.88.1` in a web browser to start setup. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device. Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

## Mounting

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown on the picture to the right;
- Place the device in rackmount enclosure and align with the holes so that the device fits conveniently;
- Tighten screws to secure it in place.

![](../img/worddavdcbcfbfbb5384f30180de01126c4ad1d.webp)

The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment. We recommend Cat6 cables for our devices.
*Mounting and configuration of this device should be done by a qualified person.*

## Powering

The device has dual removable (hot-swap compatible) power supply units AC **⏦** 110-240V (2.5 A) with standard IEC compatible sockets with Maximum power consumption of 125 W.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: https://mt.lv/help In case IP connection is not available, the WinBox tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see the [Reset button](#reset-button).

## Extension slots and ports

- 2x M.2 slots, which accept 80mm Key-M x4 PCIe 2.0 modules. M.2 slots are located on the PCB board inside the device. In order to access them remove screws on the back of the router for upper cover and while lifting up and pulling towards the cover slides off.
- microSD card slot.
- Smart Card slot for private key storage.
- 1 Gigabit Ethernet port.
- 8 SFP+ ports for 10 Gigabit connectivity.
- USB slot type A.
- microUSB slot type AB.
- Automatic fan speed control.The CCR1072 has PCIe Gen 2.0 x4 connections to the two M.2 slots.Recommended are NVMe M.2 2280mm M key SSD disks with a capacity of up to 1TB.

## Reset button

**Reset button**:

- Hold this button during boot time until the USER LED light starts flashing, release the button to reset RouterOS configuration.
- Hold the Reset button and power on your device (wait until the "USER" LED is blinking then stable "On", and when the "USER" LED is "Off" - release the Reset button) - the device is booting in BOOTP mode to reinstall RouterOS using [Netinstall](../../docs/getting-started/installation-and-upgrade/netinstall). **The MGMT/BOOT Ethernet port is used for the Netinstall process.** See RouterOS documentation about using the Netinstall recovery utility.

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Release the button before LED begins to flash, to only load backup RouterBOOT without resetting. This is useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

- EU/US AC **⏦** power cord, D03+QT3 H05VV-F 3x0.75 mm 2 1.83 m RoHS.
- Fastening set for rackmount case K-10 R2.
- Rackmount Case x72 Side Bracket.
Please see the [MikroTik SFP module compatibility table](/docs/wired-connections/mikrotik-wired-interface-compatibility).

## Specifications

For more information about this product, specification and pictures please visit our web page: https://mikrotik.com/product/CCR1072-1G-8Splus

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

![](../img/worddav8aafa0dcbb3328dd9f53f471f1e60640.badge.webp)

Safety Notice
Electric shock hazard. This equipment is to be serviced by trained personnel only. This is a class A device, operating it near residential radio equipment could cause radio interference.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

![](./img/image2020-3-2_15-27-11.webp)

## UKCA marking

![](../img/ukca.badge.webp)

## Eurasian Conformity Mark

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: MikroTikls SIA, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. Cм. на упаковке.

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

![](../img/eac.badge.webp)

## Norma Oficial Mexicana

EFICIENCIA ENERGETICA CUMPLE CON LA NOM-029-ENER-2017.

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.
Fabricante: MikroTikls SIA, Unijas iela 2, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## CE Declaration of Conformity

Manufacturer: MikroTikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

The full text of the EU Declaration of Conformity is available at the following internet address: https://mikrotik.com/products
