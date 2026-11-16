# Intercell

> Set up, power, configure, and mount the Intercell 10 B38+B39 LTE base station, with downloadable configuration and maintenance examples.

![Intercell 10 B38+B39 outdoor LTE base station.](./img/api_p02003-b38b39-10w.jpg)

The Intercell 10 B38+B39 is an outdoor dual-carrier time-division duplex LTE (TDD-LTE) base station. Each carrier supports 2×2 MIMO with 10 W output power per radio frequency (RF) channel, for a total output power of 40 W across four RF channels.

## Quick start 

1. Connect the external antennas and Ethernet cable to the connectors described in **Expansion slots and ports**.
2. Connect a 48 V DC power supply as described in **Powering**.
3. Connect your laptop to the device for configuration. The device supports DHCP and static IP address assignment.
4. For access through the default maintenance IP address, set your laptop's IP address to `192.168.200.100/24` and open `https://192.168.200.200` in a web browser.
5. Sign in with username `admin` and password `MikroTik`.
6. Configure the network, backhaul, and radio parameters as described in **Configuration**.

## Powering

The power connector accepts **48 V DC**. The package includes a power cable and connector, but **does not include a power supply**. Power consumption can reach **200 W** under maximum load.

1. Connect the supplied cable to your 48 V DC power source.
2. Connect the cable connector to the device.

Use the supplied RBGESP surge protector with the Ethernet connection.

## Configuration

Configure the device through its web interface. Installation and configuration must be performed by a qualified person.

### Network architecture

![Small-cell network architecture with an LTE base station, management system, HeNB gateway, and EPC.](./img/image2020-2-26_10-47-59.webp)

The network components have the following roles:

- **Home eNodeB (HeNB):** The LTE base station provides service to user equipment (UE).
- **Network management system (NMS) / HeNB management system (HeMS):** The management system provides small-cell lifecycle management and supports the TR-181 and TR-196 data models.
- **HeNB-GW:** The gateway between the HeNB and the Mobility Management Entity (MME) aggregates control and user-plane traffic and provides S1/X2 proxy functions.

### Configuration flow

Configure network access first, followed by the backhaul and radio parameters. Enable RF transmission after completing the configuration.

![Configuration sequence: sign in to the web interface, configure backhaul parameters, then configure radio parameters.](./img/image2020-2-26_10-38-5.webp)

The **WAN** interface is the SFP port, identified as **ID1** in the network configuration. The **LAN** interface is the Ethernet port, identified as **ID2**. If the device receives an IP address through DHCP, use a MAC scan to find it.

For static IP address assignment:

1. Set your computer's IP address to `192.168.200.100/24`.
2. Connect directly to the HeNB WAN interface and open `https://192.168.200.200`. Sign in with username `admin` and password `MikroTik`.
3. In the network configuration, set **Address Type** to **Static**, then enter the **IPv4 address** and **Mask** for your network.

   ![Network configuration with static IPv4 address and mask fields.](./img/image2020-2-26_10-44-47.webp)

4. Check the configured interfaces and IP addresses.

   ![IP interface list showing DHCP and static address assignments.](./img/image2020-2-26_10-44-28.webp)

5. Select **Submit**. The HeNB reboots to apply the configuration.
6. Reconnect the HeNB WAN interface to your network and sign in through HTTPS at its configured IP address.

### Backhaul parameters 

Open **Management → Cell** and set **S1SigLinkServer** to the IP address of your MME or HeNB gateway.

![Cell configuration with the S1SigLinkServer backhaul address highlighted.](./img/image2020-2-26_10-29-32.webp)

### Radio parameters 

The values in this section are examples. Set the network identifiers and radio parameters to match your LTE network.

#### Calculate transmit power 

Calculate the transmit power from **ReferenceSignalPower** and the bandwidth-dependent base value:

- **Per antenna:** `ReferenceSignalPower + Base`, in dBm.
- **Two antennas combined:** `ReferenceSignalPower + Base + 3`, in dBm.

| Bandwidth | Base (dB) |
| --- | --- |
| 1 MHz | 19 |
| 3 MHz | 23 |
| 5 MHz | 25 |
| 10 MHz | 28 |
| 15 MHz | 30 |
| 20 MHz | 31 |

:::warning
Do not exceed **40 dBm per antenna**. Calculate the transmit power before enabling RF transmission; excessive power can damage the power amplifier.
:::

At 20 MHz, **ReferenceSignalPower** of `-14` gives `-14 + 31 = 17 dBm` per antenna. A value of `9` gives `9 + 31 = 40 dBm`, the maximum for this product.

In **Management → Cell**, configure the common parameters:

| Parameter | Example value |
| --- | --- |
| Duplex Mode | `TDD` |
| TAC | `10` |
| PLMNID | `00666` |

![Common cell configuration with duplex mode, TAC, and PLMNID.](./img/image2020-2-26_10-30-36.webp)

#### Configure Cell 1 radio parameters

Open the **Cell1** tab and configure the following example values:

| Parameter | Example value |
| --- | --- |
| CellIdentity | `257` |
| CandidateARFCNList | `38400` |
| CandidatePCIList | `0..503` |
| FreqBandIndicator | `39` |
| DL Bandwidth | `100` |
| UL Bandwidth | `100` |
| ReferenceSignalPower | `-14` |

![Cell1 radio parameters for LTE band 39.](./img/image2020-2-26_10-31-38.webp)

**CandidateARFCNList** specifies the downlink E-UTRA absolute radio frequency channel number (EARFCN); the HeNB configures the uplink EARFCN automatically. The HeNB selects a physical cell identifier (PCI) from **CandidatePCIList**, in the range `0..503`.

The bandwidth fields use resource-block values: **20 MHz → 100**, **15 MHz → 75**, **10 MHz → 50**, and **5 MHz → 25**. Set **UL Bandwidth** equal to **DL Bandwidth**.

#### Configure Cell 2 radio parameters

Open the **Cell2** tab and configure the following example values. The EARFCN, PCI, and bandwidth conventions are the same as for Cell1.

| Parameter | Example value |
| --- | --- |
| CellIdentity | `258` |
| CandidateARFCNList | `37900` |
| CandidatePCIList | `0..503` |
| FreqBandIndicator | `38` |
| DL Bandwidth | `100` |
| UL Bandwidth | `100` |
| ReferenceSignalPower | `-14` |

![Cell2 radio parameters for LTE band 38.](./img/image2020-2-26_10-35-35.webp)

After configuring both cells and checking the transmit power, enable **AdminState** to turn on RF transmission. Select **Submit**; the HeNB reboots to apply the configuration.

#### Checking the RF status

Open **Management → Cell** and check **OpState** on both the **Cell1** and **Cell2** tabs. A value of **True** indicates the radio cell has been established successfully.

![Cell status showing OpState and the radio parameters in use.](./img/image2020-2-26_10-36-17.webp)

## Mounting

The device is designed for outdoor use and has an **IP66** rating. Mount it with the cable feed pointing downwards and use shielded Cat6 cables. The supplied mounting hardware supports wall mounting or pole mounting with a pole diameter of **50–120 mm**.

:::warning
The device weighs **25 kg**. Installation must be performed by a qualified person.
:::

1. Unpack the mounting frame and accessories.

   ![Intercell chassis and separate mounting frame.](./img/image2020-2-26_10-53-10.webp "Mounting illustration")

2. For pole mounting, attach the frame with the four fixing plates, four M12 bolts, and four M12 nuts. Pass each bolt through the mounting frame, fixing plate, and cradle, then secure it.

   ![Mounting frame attached to a pole with fixing plates and M12 bolts.](./img/image2020-2-26_10-53-39.webp "Mounting illustration")

3. Leave a **3 mm** gap under the four fixing screws near the lower side of the chassis so they can engage the mounting frame.

   ![Chassis fixing screws with a 3 mm gap for the mounting frame.](./img/image2020-2-26_10-55-3.webp "Mounting illustration")

4. Position the chassis on the frame so the screws on both sides engage the fixing holes.

   ![Intercell chassis seated in the mounting frame.](./img/image2020-2-26_10-56-11.webp "Mounting illustration")

5. Tighten and secure all eight screws to complete the installation.

   ![Secured chassis with the mounting screw positions marked.](./img/image2020-2-26_10-56-21.webp "Mounting illustration")

## Grounding

Ground both the installation infrastructure, including towers and masts, and the device. Attach a grounding wire to the device's grounding screw and connect its other end to the grounded mast.

Power-interface lightning protection standards: **GB/T 17626.5** and **IEC 61000-4-5**.

## Expansion slots and ports 

The numbers in the diagram identify the connectors and indicators:

![Intercell connector panel with numbered power, antenna, indicator, Ethernet, and SFP positions.](./img/worddav9d68e8b68243e695a7b0ccf08edcd963.webp)

1. Power supply connector.
2. Antenna connectors.
3. Power indicator LED.
4. Activity indicator LED.
5. GPS antenna connector.
6. SNIFF antenna connector.
7. Ethernet connector.
8. SFP connector.

## Hardware specifications

| Specification | Value |
| --- | --- |
| LTE bands | TDD B38: 2570–2620 MHz. TDD B39: 1880–1920 MHz. |
| Channel bandwidth | 5, 10, 15, or 20 MHz. |
| Peak rate per carrier at 20 MHz | Downlink: 140 Mbps (256QAM, SF2). Uplink: 30 Mbps (64QAM, SF1). |
| Peak rate with carrier aggregation at 20 MHz | Downlink: 280 Mbps (256QAM, SF2). Uplink: 60 Mbps (64QAM, SF1). |
| User capacity | 2 × 196 RRC-connected users and 2 × 96 active users. |
| Synchronization | GPS, IEEE 1588v2, and network listening. |
| Backhaul interfaces | One RJ45 Gigabit Ethernet port and one optical SFP port. |
| RF connectors | Six: four antenna connectors, one sniffer connector, and one GPS/BeiDou connector. |
| Maximum output power | 40 ± 1 dBm per antenna. Configure transmit power to stay within the 40 dBm limit. |

## Accessories

The package includes:

- Power cable with a plug. The power supply is not included.
- [S-31DLC20D SFP module](https://mikrotik.com/product/S-31DLC20D-181).
- [RBGESP Ethernet surge protector](https://mikrotik.com/product/rbgesp).
- N/SMA-JK converter.
- Lightning protection for the GPS and sniffer connectors.
- Installation bracket.
- Large-pole installation accessories.

See the [MikroTik wired interface compatibility table](../docs/wired-connections/mikrotik-wired-interface-compatibility) for SFP module compatibility.

## Upgrade example

[Download the firmware upgrade example (PDF)](./img/intercell-upgrade-example.pdf), with screenshots for checking the firmware version, selecting an image, and verifying the upgrade.

## B38 configuration example 

[Download the B38 configuration example (PDF)](./img/intercell-b38-cfg-example.pdf), with screenshots for adapting the cell configuration to band 38 and rebooting the device.

## Intercell built-in EPC 

[Download the built-in EPC configuration document (PDF)](./img/intercell-built-in-epc.pdf), covering network topology, Evolved Packet Core (EPC) parameters, and subscriber configuration.

## Reset configuration through the serial console 

[Download the serial-console reset instructions (PDF)](./img/intercell-reset-serial-console.pdf), including chassis access, serial connection, and configuration-file removal.

:::warning
The serial-console procedure removes configuration files and restores the default configuration after a reboot.
:::

## Configuration import 

[Download the configuration import example (PDF)](./img/intercell-cfg-import.pdf), covering data-model version matching and import of the Device and Cndata configuration files.

## Monitoring 

[Download the protocol-stack log viewer document (PDF)](./img/intercell-monitoring.pdf), covering the monitoring tool and log analysis.

## Full dual-carrier configuration 

[Download the full dual-carrier configuration document (PDF)](./img/intercell-dual-carrier-configuration.pdf), covering initial setup, network and radio configuration, and maintenance.

## Operating system support

The device runs Intercell HeNB software. RouterOS is not supported.
