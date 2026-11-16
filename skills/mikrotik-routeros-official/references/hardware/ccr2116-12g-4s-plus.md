# CCR2116-12G-4S+

> Forget about CPU limitations in 10G setups with this powerful 16-core ARM CPU based CCR. Double the performance of our previous 36- core CCR, 6x faster BGP performance. Includes an M.2 PCIe slot. See the...

![](./img/api_ccr2116-12g-4s_.jpg)

## [CCR2116-12G-4S+](https://mikrotik.com/product/ccr2116_12g_4splus)

Forget about CPU limitations in 10G setups with this powerful 16-core ARM CPU based CCR. Double the performance of our previous 36- core CCR, 6x faster BGP performance. Includes an M.2 PCIe slot. See the [CCR2116-12G-4S+ product page](https://mikrotik.com/product/ccr2116_12g_4splus) for full specifications and brochures.

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
- It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik devices must be professionally installed.

:::danger[Power down before opening the chassis]
Before opening the chassis or installing/replacing any internal components, such as an M.2 SSD, power down the system completely and disconnect the power cord from the AC power supply. After unplugging, wait at least 10 seconds to allow any residual power in the motherboard to fully dissipate.
:::

## Specifications

| Parameter | Value |
| --- | --- |
| Product code | CCR2116-12G-4S+ |
| Architecture | ARM 64bit |
| CPU | AL73400 |
| CPU core count | 16 |
| CPU nominal frequency | 2000 MHz |
| CPU Threads count | 16 |
| Switch chip model | 98DX3255 |
| Dimensions | 443 x 199 x 44 mm |
| RouterOS license | 6 |
| Operating System | RouterOS v7 |
| Size of RAM | 16 GB |
| Storage size | 128 MB |
| Storage type | NAND |
| MTBF | Approximately 200'000 hours at 25C |
| Tested ambient temperature | -20°C to 60°C |
| **Powering** | |
| Number of AC inputs | 2 |
| AC input range | 100-240 |
| Number of PSU slots | 2 |
| Frequency (Hz) | 47-63 |
| Max power consumption | 83 W |
| Max power consumption without attachments | 60 W |
| Cooling type | 4 fans |
| **Ethernet** | |
| 10/100/1000 Ethernet ports | 13 |
| **Fiber** | |
| SFP+ ports | 4 |
| **Peripherals** | |
| Serial console port | RJ45 |
| Number of M.2 slots | 1 |
| **Other** | |
| CPU temperature monitor | Yes |
| PCB temperature monitor | Yes |
| Voltage Monitor | Yes |
| Mode button | Yes |
| **Certification & Approvals** | |
| Certification | CE, EAC, ROHS |

## Quickstart

- Connect your PC to the **ETH/BOOT** labeled port or the first Ethernet port;
- Connect the device to a power source;
- Configure the IP settings of your network card to `192.168.88.2/24`;
- Configuration should be made using **WebFig** in a web browser or the **WinBox** configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility;**
- Open `192.168.88.1` in a web browser to start setup. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device. Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

## Powering

The device accepts powering from two redundant power supplies, each accepts 100-240 V AC power. You can use either, or both at the same time. Up to 60 W power consumption.

## Extension slots and ports

- 13x 10/100/1000 Ethernet ports.
- 4x 10G SFP+ ports.
- One M.2 slot, type PCIe x4.
- RJ45 console port.
The CCR2116-12G-4S+ has PCIe Gen 3.0 x4 connection to the M.2 slot.
Recommended are NVMe M.2 2280mm M key SSD disks with no capacity limitations.

## Mounting

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

![](../img/worddavdcbcfbfbb5384f30180de01126c4ad1d.webp)

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown in the picture.
- Place the device in a rackmount enclosure and align with the holes so that the device fits conveniently.
- Tighten screws to secure it in place.
*The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.* *We recommend shielded Cat5/6 cables for our devices.* *The mounting and configuration of this device should be done by a qualified person.*

## Configuration

Full documentation for RouterOS is available at: https://mt.lv/help You can configure the device using **WebFig** in a web browser or the "**WinBox**" configuration tool https://mt.lv/winbox. **Multiple configuration methods are available to ensure accessibility.**
To start setup, open `192.168.88.1` in a web browser to start setup. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device. Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker).
The device is equipped with an RS-232 serial port, set by default to 115200 bit/s, 8 data bits, 1 stop bit, no parity. For recovery purposes, it is possible to reinstall the device from the network, see the [Reset button](#buttons-and-jumpers).

## Buttons and jumpers

**Reset button**:

- Hold this button during boot time until the USER LED light starts flashing, release the button to reset RouterOS configuration.
- Hold the Reset button and power on your device (wait until the "USER" LED is blinking then stable "On", and when the "USER" LED is "Off" - release the Reset button) - the device is booting in BOOTP mode to reinstall RouterOS using [Netinstall](../../docs/getting-started/installation-and-upgrade/netinstall). **The MGMT/BOOT Ethernet port is used for the Netinstall process.** See RouterOS documentation about using the Netinstall recovery utility.

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Release the button before LED begins to flash, to only load backup RouterBOOT without resetting. This is useful for RouterBOOT debugging and recovery.

The Mode button is not functional by default but can be assigned any script in the menu /system routerboard mode-button

## LEDs

The device has four LED lights. PWR1/2 indicates which power supply is being used. FAULT indicates a problem with the cooling fans. USER can be configured in software.

## Accessories

- PLUG1, PLUG2_EU/US power cord, D03+QT3 H05VV-F 3x0.75mm2 1.83m RoHS
- CASE3, CASE4_ 1U rackmount bracket white
- SET1_Fastening set K-57r1v1

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.
