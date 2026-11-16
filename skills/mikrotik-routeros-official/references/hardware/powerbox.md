# PowerBox

> The PowerBox is an outdoor device with five Ethernet ports. Package includes IEC cord, steel clamp, PoE injector, 24 V power adapter, and DIN mount. See the PowerBox product page for full specifications and brochures.

![](./img/api_rb750p-pbr2.webp)

## [PowerBox](https://mikrotik.com/product/RB750P-PBr2) (RB750P-PBr2)

The PowerBox is an outdoor device with five Ethernet ports. Package includes IEC cord, steel clamp, PoE injector, 24 V power adapter, and DIN mount. See the [PowerBox product page](https://mikrotik.com/product/RB750P-PBr2) for full specifications and brochures.

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

## Mounting

It is possible to attach the device to a DIN rail, using provided DIN rail bracket and screws. Since the device has a weatherproof outdoor case, you can mount it on a pole, with a provided steel clamp.

![](./img/image2020-3-17_15-55-16.webp)

Please make sure to mount the device with the Ethernet ports facing down.

## Powering

The board accepts power from the power jack or from the first Ethernet port (Passive PoE):

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 8-30 V DC,
- The first Ethernet port accepts passive Power over Ethernet accepts 8-30 V DC.

The power consumption of this device is 2 W.

## Power output

This device can supply PoE powering to external devices from its Ethernet ports. This is convenient as you don't need any additional PoE injectors to power other devices. This feature is indicated by the letter "P" in the device model name. The output voltage will be the same as the input voltage, and this feature will have to be enabled on the specific ports in RouterOS software. By default it is disabled. The maximum power output of each Ethernet port in this mode is 1 A (2 A total for all ports). Once Power Output is enabled in RouterOS, the Ethernet LED light shines also in red. Red LED means the port is currently providing PoE power, green means Ethernet has a link, both at the same time means Ethernet is linked and power is being outputted.

## Configuration

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting with the [RouterOS documentation](https://mt.lv/help) to get accustomed to the possibilities. In case an IP connection is not available, the **WinBox** tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default). For recovery purposes, it is possible to boot the device from the network, see the [Reset button](#reset-button).

## Extension slots and ports

- Five individual Ethernet ports, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration.
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers.

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

The package includes the following accessories that come with the device:

- IEC power cord.
- Steel clamp.
- PoE injector.
- 24 V power adapter.
- DIN mount.

## Specifications

For more information about this product, specification and pictures please visit our web page: https://mikrotik.com/product/RB750P-PBr2

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

![](./img/image2020-2-26_11-35-51.webp)

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
