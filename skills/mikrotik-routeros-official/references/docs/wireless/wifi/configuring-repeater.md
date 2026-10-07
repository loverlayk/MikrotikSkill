# Configuring a wireless repeater

> This guide explains how to configure a wireless repeater using MikroTik RouterOS's wifi-qcom package, detailing setup steps for dual-band interfaces (2.4 GHz and 5 GHz), SSID management, security settings, and...

# Configuring a wireless repeater

**Package:** `wifi-qcom`

:::info
This guide is meant for 802.11 AX devices running `wifi-qcom` package/drivers.
:::

WiFi range is limited. APs (devices that broadcast Wi-Fi networks) run on 2.4 and/or 5 GHz frequency. 5 GHz networks enable much better throughput, but with reduced range. 2.4 GHz networks ensure better coverage, but with less throughput.

Indoor APs are, usually, equipped with omnidirectional antennas (which allow broadcasting the signal in a "donut" shape around the AP, 360°). For indoor and short distance outdoor installations, it is a perfect antenna to use. Using a simple home AP with omnidirectional antennas, you can achieve a distance of up to ±100 meters in an "ideal" interference-free line of sight setup, which is reduced much further inside buildings. Concrete, pipes, metal, water...and all kinds of other different materials affect WiFi indoors. Some items can absorb, some deflect, some diffract and some can scatter the signal.

With that in mind, it is not always possible to cover the required range with a single AP/router, and additional APs need to be installed.

For the best possible throughput, each AP should be connected to the main network via an ethernet cable. However! It is not always possible to pass the cable from the AP to the main router for whatever reason...most likely, aesthetics.

This is where "**repeaters**" or "**extenders**" can help.

The Extender's/Repeater's job is to establish a Wi-Fi connection with your main router as a "client" or a "station", use this connection as an uplink connection, and also broadcast the extender's own WiFi network at the same time.

:::info
**Throughput!**

When a device is used as an extender, the throughput you get from it is reduced, at least, by half.

Half of the resources are allocated to keep an ongoing connection with the router, while you are left with the other half for retransmission. It doubles the overall air time.

Also! Since you are installing the extender at a distance from the main router... with distance, WiFi throughput is reduced further.
:::

:::info
**Roaming!**

If you copy the SSID name from your router settings and configure the extender to broadcast the same SSID name →  roaming will be purely client dependent.

Roaming is when your client device transitions between different APs which use the same WiFi name. There are standards that can help "accelerate" and "smoothen" the transition (like 802.11 r/k/v) but, unfortunately, they can not be used in this setup and so, the decision, "to roam" or "not to roam" is up to the client fully. Different vendors have different algorithms implemented that decide how and when your client device should switch.

Keep that in mind! Some devices, which have a good algorithm (decision-making), will roam properly, while others might stick to the furthest AP with a poor signal.
:::

## Repeater setup

:::info
**Which frequency to use?**

Dual-band routers and access points, from the get-go, should have two Wi-Fi interfaces → wifi1 and wifi2, each representing a certain frequency, 5 and 2.4 GHz respectively. For repeater setup, one of the interfaces needs to be turned into a **station** interface (which will act as a client to another network), while, the other, should be set in **ap** mode (which will allow the device to broadcast its own network).

If we use 2.4 GHz as a **station** interface, it would increase the distance at which we can install the repeater, but it would also reduce the throughput we can get from it. If we use 5 GHz as a **station** interface, we reduce the range but increase the throughput.
:::

:::warning
Because we will be changing Wi-Fi and port-related configurations, it is advised to connect to the device's settings via Ethernet port/cable, using the MAC address. You can use the [Winbox](../../management-tools/winbox.md) "Neighbors" tab and double-click on the MAC address of the device in the list. This way, you will not lose access later on when changing interface-related settings.
:::

In our example, we want to use wifi2 (2.4 GHz) as a "station" interface, while having wifi1 (5 GHz) broadcast repeater's own SSID (and also, potentially re-broadcast router's SSID over 2.4 GHz as well):

![](./img/configuring-repeater-01.webp)

Overall configuration:

```ros
/interface/wifi
set [ find default-name=wifi2 ] configuration.mode=station-bridge configuration.country=Latvia .ssid=router.ssid.2 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
set [ find default-name=wifi1 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.5 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
add configuration.mode=ap .ssid=router.ssid.2 disabled=no master-interface=wifi2 name=wifi3 security.authentication-types=wpa2-psk .passphrase=router.password
/interface/list
add comment=defconf name=WAN
add comment=defconf name=LAN
/interface/bridge
add auto-mac=no comment=defconf name=bridge
/interface/bridge/port
add interface=all bridge=bridge 
/interface/list/member
add comment=defconf interface=bridge list=LAN
/ip/dhcp-client
add interface=bridge
```

### 2.4 GHz interface configuration

```ros
/interface/wifi
set [ find default-name=wifi2 ] configuration.mode=station-bridge .ssid=router.ssid.2 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
```

- `configuration.mode=station-bridge` → selects the [station mode](../user-guides/wireless-station-modes.md).

:::info
**Which station mode to use?**

For **MikroTik Wi-Fi 6 AX** (router that uses `wifi-qcom` package/drivers) to **MikroTik Wi-Fi 6 AX** (repeater/station that uses `wifi-qcom` package/drivers) connection, use **`station-bridge`** mode.

For **3rd-party-vendor** or **MikroTik legacy WiFi 5 AC and below** (router) to **Wi-Fi 6 AX** (repeater) connection, use **`station-pseudobridge`** mode.

`station-pseudobridge` does something similar to "Network Address Translation" but with MAC addresses. With this mode, if you have multiple devices connected to the repeater and they all access the internet, the router would see all those attempts coming from a single MAC address. Basically, all client devices would be hidden behind one MAC address, which could potentially cause networking issues. It is not advised to use this mode, but, in such cases, there are no other options.

Additionally, when using `station-pseudobridge` on legacy MikroTik devices, ensure that the legacy device has disabled [RSTP](../../bridging-and-switching/user-guides/spanning-tree-protocol.md) on its bridge port with the command `/interface/bridge/set protocol-mode=none`. Otherwise, RSTP could result in issues with DHCP-client functionality and issues passing IP addresses through the bridge ports.
:::

- `configuration.country=Latvia` → Select your actual country, so that you do not break any regulations (your country's "laws"). Different country profiles have different allowed output powers per different frequency ranges.
- `ssid=router.ssid.2` → It is the 2.4 GHz SSID network name that the router broadcasts (where the repeater should connect).
- `security.authentication-types=wpa2-psk` → Selects which authentication types the main router uses.
- `passphrase=router.password` → Configures the password from the main router network. It is the password configured in your router's settings.

### 5 GHz interface configuration

```ros
/interface/wifi
set [ find default-name=wifi1 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.5 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
```

- `configuration.mode=ap` → configures interface to work in "access point" mode.
- `configuration.country=Latvia` → selects your actual country, so that you do not break any regulations (your country "laws"). Different country profiles have different allowed output powers per different frequency ranges.
- `ssid=router.ssid.5` → configures wireless network name (SSID), which the repeater needs to re-broadcast. It can be the same network name as the main router uses, or it can be a different name. For testing, better use a "unique" name so you can differentiate networks. For "client roaming" to happen, use the exact same WiFi name from the router settings.
- `security.authentication-types=wpa2-psk` → selects which authentication types to use. For "client roaming" to happen, use the exact same authentication type from the router settings.
- `passphrase=router.password` → sets the password from the repeater's WiFi network. For "client roaming" to happen, use the exact same password from the router settings.

### Optional step - adding virtual interface

In case you want to make the extender re-broadcast wireless networks using both frequencies (e.g. `wifi2` is reserved for `mode=station-bridge`, and you are left only with `wifi1` for `mode=ap`), create a virtual interface on top of the `station` interface:

```ros
/interface/wifi
add configuration.mode=ap .ssid=router.ssid.2 disabled=no master-interface=wifi2 name=wifi3 security.authentication-types=wpa2-psk .passphrase=router.password
```

- `configuration.mode=ap` → Ensures that it will act as an "access point" interface.
- `ssid=router.ssid.2` → Configures the wireless network name (SSID), which the repeater needs to re-broadcast. For "client roaming" to happen, use the exact same WiFi name from the router settings.
- `master-interface=wifi2` → Specify which interface to "base" the "virtual" interface on (specify on-top of which interface to create it). Select the interface, which is used as a `station` interface.
- `name=wifi3` → Name the virtual interface.
- `security.authentication-types=wpa2-psk` → Select which authentication types to use. For "client roaming" to happen, use the exact same authentication type from the router settings.
- `passphrase=router.password` → Sets the password from the repeater's WiFi network. For "client roaming" to happen, use the exact same password from the router settings.

:::info
The virtual interface will use the exact same frequency channel, which is used by the `station` interface to connect to the router. The Wi-Fi frequency channel for this interface can not be changed.
:::

### Bridging and listing

[Bridge all ports](../../bridging-and-switching/index.md#example-1) (Ethernet, Wi-Fi and virtual Wi-Fi interfaces):

```ros
/interface/bridge
add auto-mac=no comment=defconf name=bridge
/interface/bridge/port
add interface=all bridge=bridge 
```

And ensure that the bridge is listed as a "LAN" interface (`/interface list member add comment=defconf interface=bridge list=LAN`), so that the firewall rules do not block access to extender's management:

```ros
/interface/list/member
add comment=defconf interface=bridge list=LAN
```

That is, of course, if you have proper firewall and access restrictions added on the main router. Otherwise, restrict it.

### DHCP

```ros
/ip/dhcp-client
add interface=bridge
```

Apply [DHCP-client](../../network-management/dhcp/client#configuration-examples) on top of the bridge interface, so that the repeater itself and all its connected clients get IP addresses from the main router.

Disable [DHCP-server](../../network-management/dhcp/server) functionality.

### Address

Remove/disable default configuration bridge's assigned [IP Address](../../getting-started/networking-fundamentals/index.md#address-configuration), in case your router's network uses the same subnet, so that it does not "conflict" with the gateway IP.
