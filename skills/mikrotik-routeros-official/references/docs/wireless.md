# Wireless

> This section introduces MikroTik RouterOS wireless configuration, covering package selection for different CPU types and frequency bands (2.4GHz, 5GHz, 60GHz), use cases for home access points and industrial links,...

# Wireless

This section will describe the configuration of 802.11 wireless protocols and best use examples.

Wireless capabilities of a router can greatly enhance the usability of your home or office network or provide a solution for industrial structures. Choosing the right device for setup can be a puzzle to inexperienced users. This guide intends to explain different parameters and suggest a thought process to not get lost in the vast selection of MikroTik routers.

### Which section is for my device?

MikroTik wireless devices fall into product families, each configured through a specific RouterOS menu. Find yours below, then jump to its section:

| Product family | RouterOS menu | Driver package |
| :-- | :-- | :-- |
| [Wi-Fi 6 / 7 (802.11 ax/be)](./wifi/index.md) | `/interface/wifi` | `wifi-qcom`, `wifi-qcom-be`, `wifi-mediatek` |
| [Wi-Fi 5 (802.11ac)](./wifi-ac/index.md) | `/interface/wifi` *or* `/interface/wireless` | `wifi-qcom-ac` *or* `wireless` |
| [802.11 a/b/g/n](./abgn/index.md) | `/interface/wireless` | `wireless` |
| [60 GHz (W60G)](./w60g/index.md) | `/interface/w60g` *or* `/interface/wifi` | `wireless` |

802.11ac devices are the only ones with a choice of menu — the [Wi-Fi 5 (802.11ac)](./wifi-ac/index.md) section explains how to pick. The package tables below cover that choice in more detail.

:::tip[Not sure which family your device belongs to?]
The wireless standard is usually encoded in the model name. For example, **wAP ax** and **hAP ax³** are 802.11ax (Wi-Fi 6), **hAP be lite** is 802.11be (Wi-Fi 7), **hAP ac²** and **wAP ac** are 802.11ac (Wi-Fi 5), and a Cube **60Pro** is a 60 GHz (W60G) device.
:::

### RouterOS package type

Some MikroTik devices can choose between two types of Wireless NPK packages (i.e. wireless drivers), depending on the required features and the device type. More details can be found in the respective documentation sections. CAPsMAN functionality is included in the routeros bundle package, regardless of CPU architecture and independent of wireless drivers, i.e. you can run CAPsMAN on any model.

In short:

- CAPsMAN can run anywhere, on any MikroTik device. You can run both new and old CAPsMAN at the same time in most cases (when running both on an AX router, built in cards can't be used).
- MIPS type devices have no choice of driver, only legacy drivers are supported.
- ARM CPU 802.11AC wireless devices have a choice of wireless driver: wireless.npk or wifi-qcom-ac.npk.

The table below helps you choose in this case:

#### Old 802.11ac ARM CPU devices\*

| **Feature** | **Needed packages** | **Notes** |
| :-- | :-- | :-- |
| New drivers (WPA3, Fast Roaming) | routeros + wifi-qcom-ac |  |
| Legacy drivers (Nstreme, Nv2) | routeros + wireless |  |
|  |  |  |
| New Capsman and own real interfaces | routeros + wifi-qcom-ac | *Built-in cards work with new drivers* |
| New Capsman only controller | routeros | *Built-in cards are not used at all* |
| Old Capsman | routeros + wireless | *Actually old = dual. Built-in cards will work with legacy drivers* |
| Running both Capsmans at the same time | routeros + wireless | *Built-in cards can only work with legacy drivers* |

***\* wifi-qcom-ac**: Audience, Audience LTE kit, Chateau (all variants of D53), hAP ac<sup>2</sup>, hAP ac<sup>3</sup>, cAP ac, cAP XL ac, LDF 5 ac, LHG XL 5 ac, LHG XL 52 ac, NetMetal ac<sup>2</sup>, mANTBox 52 15s, wAP ac (RBwAPG-5HacD2HnD), SXTsq 5 ac*

#### New 802.11ax devices

| **Feature** | **Needed packages** | **Notes** |
| :-- | :-- | :-- |
| New drivers (WPA3, Fast Roaming) | routeros + wifi-qcom |  |
| Legacy drivers (Nstreme, Nv2) | - | *Not possible* |
|  |  |  |
| New Capsman and own real interfaces | routeros + wifi-qcom | *Built-in cards work with new drivers* |
| New Capsman only controller | routeros | *Built-in cards are not used at all* |
| Old Capsman | routeros + wireless | *Actually, old = dual. Loses built-in cards* |
| Running both capsmans at the same time | routeros + wireless | *Loses built-in cards* |

### Frequencies

MikroTik provides routers with interfaces in 3 frequency bands - 2.4GHz, 5GHz, and 60GHz. Each frequency band has its own advantages and use cases.

#### 2.4GHz

Nowadays considered legacy because of overuse, it is still the most widely supported band. If you have a wireless client like a phone, laptop or another device, it will most probably support this band. Even IoT devices often support the 2.4GHz band. Because of the lower frequency, the 2.4GHz band can better overcome obstacles, so consequently it has a bigger range than a 5GHz device, but it also usually has smaller throughput (internet speed). Also, it can severely suffer from interference (noise) from other 2.4GHz wireless devices, because almost every home access point supports the 2.4GHz band and it performs well through walls and over large distances also, there are fewer frequencies to choose from (3 non-overlapping). If you have many close neighbors (apartments, shared office building), chances are the 2.4GHz band will be saturated and performance will be lower. This band can also be used for industrial links.

#### 5GHz

Usually, new phones and laptops also support the 5GHz band. If your client device and router support 802.11ac (sometimes referred to as just "ac") it will be faster than the 2.4GHz band. The 5GHz band has more frequencies to choose from, but also usually has a lower range than the 2.4GHz band. If you have new client devices, your network will benefit from an ac router. The 5GHz band is also often used for industrial links, because of the big frequency range.

#### 60GHz

Currently, there are very few client devices (phones, laptops) that support the 60GHz band. However, it offers cutting-edge solutions for industrial links. For example, if you have 2 points that must be connected at distances up to 1500 meters you will get a 1 Gbps duplex link. For example, one of the MikroTik products is called the *Wireless Wire* because it provides the same speed as a 1Gbps wired connection, but you will need a clear line of sight to establish the link.

---

### Use case

RouterOS software on MikroTik devices provides broad and coherent configuration possibilities. RouterOS software allows you to use MikroTik devices in many ways, for example, if needed, a "home access point" device can be easily reconfigured to act as a client or form a point-to-point link, if needed. The "home AP" is simply the default configuration, but it can be changed to whatever configuration you wish. That being said, it is best to use hardware for its intended purpose.

#### Home AP for phones and laptops

Before you determine the most optimal choice for your setup, you should answer questions like how many clients you want to connect, what range you should cover and what speeds you want to get.

#### Client count

More connected clients mean higher latency and smaller throughput. We recommend 20-50 clients per interface to reach the peak performance, depending on conditions, the number of clients can go up to 100 and still work stably. If clients need high throughput or data traffic is time sensitive it is advised to plan fewer clients per access point. Often it is beneficial to choose simpler access points but place them more densely.

#### Range

The range of wireless connections depends on many conditions. Some of those are antenna gain, transmit power of the router and the client device, interference from other devices, obstacles (walls, metal objects), router placement. An important factor to note is that all involved devices affect the achievable distance, meaning that no matter how strong and sensitive your AP is, a small phone will be limited by its own transmit power and sensitivity. One device is unable to cover large areas if the client devices are mobile phones. Usually, only a few hundred meters can be achieved and more AP devices are required to cover bigger areas.

- **Antenna gain** is measured in dBi and determines how narrow the beam is. The radiation pattern of 0 dBi (practically impossible) is of the shape of a sphere, 1.5 dBi - 5 dBi radiates to all directions almost equally but has some dents and sides where the signal will be stronger. > 9 dBi has an obvious directional radiation pattern. Antennas with higher antenna gain if properly positioned will reach further in the necessary direction.
- **Transmit power** measured in dBm or mW determines signal strength that is coming out of a wireless interface. Mobile devices usually have low transmit power to save battery power. Even if, for example, the phone reports an OK received signal strength, the router may receive a weak signal from the phone.

- **Interference** from other devices increases the noise floor and it gets harder for the router to distinguish signal from noise, therefore, the signal must be stronger and the client closer to the access point. Access points in the same frequency occupy the same air time decreasing throughput and increasing latency.

- Some **objects** decrease (attenuate) signal strength while others reflect the signal. Usually, in buildings, you have to keep in mind walls and their thickness, floor, and ceiling, metallic objects. Glass and wood also attenuate the signal.

- **Placement** of access point also affects range. The access point shouldn't be covered by metallic objects or surfaces so the signal can have space to spread.

#### Speed

If speed is important, then you should choose a 5GHz wireless router with 802.11 ac support.

### For other wireless antennas to connect (CPE to AP)

Often it is necessary to connect two or more points, such as connecting buildings on campus or connecting client homes to the network, or establishing a long link. MikroTik provides solutions in these situations too. In order to choose, you must know the distance, whether you have to connect two points (point to point - PtP) or multiple points (point to multipoint - PtMP) and what speeds you need.

#### Distance

Because in these situations we are dealing with directional antennas and big distances, you must keep in mind that alignment and line of sight are crucial. For small distances up to 1500 meters, we advise using 60 GHz devices which will provide stability and great speed. Also, in small distances, 2.4 GHz or 5 GHz devices with small antenna gain will do just fine, although you won't get such speeds as with 60 GHz devices. For longer links antenna gain and transmit power should be taken into consideration. Higher signal strength will allow higher data rates which mean higher throughput. Choose your frequency wisely to escape interference with other wireless links. Keep in mind that in cities even above the roof there often is interference from neighboring 2.4 GHz and 5 GHz links.

#### PtP or PtMP

PtP and PtMP links differ in some areas. For PtMP you most probably will want an antenna with a wider beam also called - a sector antenna. Such an antenna covers a wider angle but also has less gain, therefore, less distance. Also in PtMP the access point must have at least level 4 RouterOS software license. Clients or devices that are connected to the access point and devices in a PtP link can have license level 3 and narrower beamwidth.

#### Speed

For higher speeds in short links, you must choose 60 GHz devices, for longer distances - 5GHz ac devices.

---

#### Note

For controlling large networks of access points you can use CAPsMAN — a controller that provisions many access points from one place. Use the controller that matches your devices' menu: [WiFi CAPsMAN](./wifi/capsman.md) for `/interface/wifi` devices (`wifi-qcom` / `wifi-qcom-ac`), or [CAPsMAN](./abgn/capsman/index.md) for legacy `/interface/wireless` devices. For controlling hundreds of access points, we advise using our CCR series devices. For controlling thousands of access points you might want to try using CHR or an x86 machine.
