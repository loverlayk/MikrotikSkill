# PowerBox Pro

> The PowerBox Pro is an outdoor device with five Gigabit Ethernet ports and PoE power output on ports 2-5 (1 A maximum per port, 2 A total maximum). See the PowerBox Pro product page for full specifications and brochures.

![](./img/api_rb960pgs-pb.jpg)

## [PowerBox Pro](https://mikrotik.com/product/RB960PGS-PB) (RB960PGS-PB)

The PowerBox Pro is an outdoor device with five Gigabit Ethernet ports and PoE power output on ports 2-5 (1 A maximum per port, 2 A total maximum). See the [PowerBox Pro product page](https://mikrotik.com/product/RB960PGS-PB) for full specifications and brochures.

## Safety Warnings

- Before you work on any equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents.
- Ultimate disposal of this product should be handled according to all national laws and regulations.
- The Installation of the equipment must comply with local and national electrical codes.
- This product is intended to be mounted outdoors on a pole. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- Read the installation instructions before connecting the system to the power source.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik devices must be professionally installed.

## Quickstart

- Connect your WAN cable to port 1, and the other devices to ports 2-5;
- Connect the device to a power source;
- Configure your network card settings to obtain the IP address automatically using DHCP;
- Configuration should be made using **WebFig** in a web browser or the **WinBox** configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Open `http://192.168.88.1` in a web browser to start setup. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device. Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- Set up your router password.

## Powering

The power consumption of this device without attachments is 6 W, Max power consumption is 54 W. The device accepts power from the power jack or from the first Ethernet port (Passive PoE):

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 12-57 V DC.
- The ether1 port accepts Passive PoE input 12-57 V DC.

## Mounting

It is possible to attach the device to a DIN rail, using provided DIN rail bracket and screws. Since the device has a weatherproof outdoor case, you can mount it on a pole, with provided two zip ties or a steel clamp. The ground cable needs to be attached to a specially designed screw on the backside of the unit.

![](./img/image2020-3-17_15-51-2.webp)

Please make sure to mount the device with the Ethernet ports facing down.

## Configuration

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting with the [RouterOS documentation](https://mt.lv/help) to get accustomed to the possibilities. In case an IP connection is not available, the **WinBox** tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default). For recovery purposes, it is possible to boot the device from the network, see the [Reset button](#reset-button).

## Extension slots and ports

- Five 10/100/1000 Gigabit Ethernet ports.
- One SFP port.

## Power output

The device supports passive or standard 802.3at/af PoE input/output. Ethernet ports 2-5 can power other PoE-capable devices with the same voltage as applied to the unit. Fewer power adapters and cables to worry about! It can power af/at mode B (4,5+)(7,8-) compatible devices if 48-57 V input voltage is used. The maximum power output per port is 1 A, and 2 A total using input voltage 12-30 V. Using input voltage 31-57 V power limit per port is 450 mA. Once Power Output is enabled in RouterOS, the Ethernet LED adds red color to it (green means Ethernet link is made, red means power but no link, red and green both means there is link and power).

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration.
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers.

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Specifications

- CPU nominal frequency: 800 MHz.
- Size of RAM: 128 MB.
- Storage: 16 MB.
- 10/100/1000 Ethernet ports: 5.
- SFP ports: 1.
- Switch chip model: QCA8337.
- Dimensions: 125 x 52 x 225 mm.
- Operating temperature: -40°C to +70°C tested.

For more information about this product, specification and pictures please visit our web page: https://mikrotik.com/product/RB960PGS-PB

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

![](./img/image2020-2-26_11-36-24.webp)

## Safety notice

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

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
