# RB1100-series

> The RB1100 is a rack-mountable Ethernet router with 13 Gigabit Ethernet ports. Two of the ports provide bypass functionality.

:::info[This article covers]

- **[RB1100AHx4](https://mikrotik.com/product/rb1100ahx4)**
- **[RB1100AHx4 Dude Edition](https://mikrotik.com/product/RB1100Dx4)**

:::

![](./img/api_rb1100dx4.jpg) ![](./img/image2020-3-2_14-2-29.webp)

The RB1100 is a rack-mountable Ethernet router with 13 Gigabit Ethernet ports. Two of the ports provide bypass functionality.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- The Installation of the equipment must comply with local and national electrical codes.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity or hot environments.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik devices must be professionally installed.

## Quickstart

- Connect your ISP cable to the Ethernet1 port, and local network computers to the other ports;
- Connect the device to a power source;
- Configure your network card with an address from the `192.168.88.0/24` network, because the device does not have a DHCP server enabled by default;
- Configuration should be made using **WebFig** in a web browser or the **WinBox** configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Open `http://192.168.88.1` in a web browser to start setup. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device. Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- Set up your router password.

## Powering

The device accepts powering from the dual/failover IEC power connectors on the back of the case. You can use either of them separately or both connectors at the same time, for failover purposes. The device also accepts 12-57V passive or 802.3af/at PoE on Ethernet port 13. The device also has a terminal block for Telecom -48V DC supply or any other DC supply in the 24-57 V range.

## Configuration

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting with the [RouterOS documentation](https://mt.lv/help) to get accustomed to the possibilities. In case an IP connection is not available, the **WinBox** tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default). For recovery purposes, it is possible to boot the device from the network, see the [Reset button](#reset-button).

## Booting process

First, the RouterBOOT loader is started. It displays boot information on the onboard RS232C asynchronous serial port. The serial port is set by default to 115200 bit/s, 8 data bits, 1 stop bit, no parity.

The RouterOS system will then load. It will also be indicated by two beeps.

You can connect to the device with SSH, **WinBox**, or the web interface by plugging your computer into port Ether1 and connecting to `192.168.88.1` with the username "**admin**" and no password (or, for some models, check user and wireless passwords on the sticker). The device doesn't have a DHCP server enabled by default, your PC should be configured with an address from this network.

More information on connecting to the device: https://mt.lv/help

## Extension slots and ports

- 13x Gigabit Ethernet ports, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices. ETH13 port accepts PoE power, and can be used to boot the device from the network for reinstalling with the Netinstall utility (see documentation)
- DB9 RS232C asynchronous serial port
- microSD slot
- 2x M.2 slots, accepting SATA type M.2 SSD disks in 2280 form factor (only Dx4 model)
- 2x 2.5 inch SATA connectors, accepting standard 2.5" SATA HDD disks (only Dx4 model)

Recommended are SATA3 M.2 2242mm/2260mm/2280mm B+M key SSD disks with no capacity limitations.

## Reset button

The reset button has the following functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration.
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers.

The bypass switch allows binding ports 11 and 12 together in bypass mode, which means that if the device loses power, the ports will be connected together, allowing data to pass from one port to the other, as if the device were not there.

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Specifications

For more information about this product, specification and pictures please visit our web page: https://mikrotik.com/product/rb1100ahx4

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

![](../img/worddavf8766f69b74dff1d087a9fa824cd1a00.badge.webp)

## Safety notice

Electric shock hazard. This equipment is to be serviced by trained personnel only.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Federal Communication Commission Interference Statement

![](../img/fcc.badge.webp)

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation.

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense.

FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate this equipment.
This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.
Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

## Innovation, Science and Economic Development Canada

This device complies with Industry Canada's license-exempt RSS standard(s). Operation is subject to the following two conditions: (1) this device may not cause interference, and (2) this device must accept any interference, including interference that may cause undesired operation of the device.
Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

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

## CE Declaration of Conformity

Manufacturer: MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

The full text of the EU Declaration of Conformity is available at the following internet address: https://mikrotik.com/products
