# Configuring standalone access point

> This guide provides instructions for configuring standalone access points (APs) using MikroTik RouterOS's wifi-qcom package, detailing setup steps for 2.4/5 GHz networks, antenna selection, and bridge configurations...

# Configuring standalone access point

**Package:** `wifi-qcom`

:::info
This guide is meant for 802.11 AX devices running `wifi-qcom` package/drivers.
:::

Wi-Fi devices can play different roles. The most common device that almost every household has is called a Wi-Fi router. A typical Wi-Fi router, usually, has a WAN port (for ISP connection), LAN ports (for local PCs, wired printers etc) and a WLAN network (Wi-Fi network). Routers are also called "gateways" and "firewalls" because they act as a "doorway" for your local network clients into the Internet (those devices "hide" LAN-connected clients behind them and protect them).

:::info
The router is a firewall/gateway device, which has an ISP cable connected to it, and is [firewall protected](../../firewall-and-quality-of-service/firewall/index.md) and has [DHCP-server](../../network-management/dhcp/server) functionality enabled (which provides an IP address to the connected, both wirelessly and via a wire, LAN clients).
:::

Another role for a Wi-Fi device is called an "access point" or an "AP" for short. Those devices, typically, are connected to the main "router/gateway/firewall" via an ethernet connection (to the router's LAN port); they are not firewall protected, and do not have DHCP-server functionality enabled (they do not provide IP addresses). APs have all their Wi-Fi and LAN interfaces/ports bridged, and thus, APs "take" IP addresses from the router connection, and "pass" them down to AP-connected clients (acting as a "layer2" bridge/switch).

:::info
Access points are "bridge" devices, which are connected to the router using an Ethernet cable; they are not [firewall protected](../../firewall-and-quality-of-service/firewall/index.md), and they have [DHCP-server](../../network-management/dhcp/server) functionality disabled (they "bridge" DHCP requests from the router to AP's clients).
:::

In other words, a **Wi-Fi router** **is** **an AP with additional functionality**.

APs (devices that broadcast Wi-Fi networks) run on 2.4 and/or 5 GHz frequency. 5 GHz networks enable much better throughput, but with reduced range. 2.4 GHz networks ensure better coverage, but with less throughput.

Indoor APs are, usually, equipped with omnidirectional antennas (which allow broadcasting the signal in a "donut" shape around the AP, 360°). For indoor and short distance outdoor installations, it is a perfect antenna to use. Using a simple home AP with omnidirectional antennas, you can achieve a distance of up to ±100 meters in an "ideal" interference-free line of sight setup, which is reduced much further inside buildings. Concrete, pipes, metal, water...and all kinds of other different materials affect WiFi indoors. Some items can absorb, some deflect, some diffract and some can scatter the signal.

With that in mind, it is not always possible to cover the required range with a single AP/router, and additional APs need to be installed, meaning that if you have a problematic spot in your home, where Wi-Fi signal is poor or non-existent, consider installing a new AP closer to the problematic spot.

:::warning
**This guide is meant for** a "basic" or a so-called **"standalone" AP setup**. You can use it, if you have a 3rd-party vendor Wi-Fi router (non-MikroTik), if you have a legacy Wi-Fi 5 (AC) MikroTik router, or if your previous setup did not have any Wi-Fi APs at all.

**For setups that consist of `wifi-qcom` package/driver APs, use [CAPSMAN management](./capsman.md)**, as it enables 802.11 r/k/v roaming standards, which smooth the client's transition.
:::

:::note
**Non-802.11 r/k/v roaming!**

In "standalone" AP setups, if you simply copy the SSID name from your router settings and configure the AP to broadcast the same SSID name →  roaming will be purely client dependent.

Roaming is when your client device transitions between different APs which use the same WiFi name. There are standards that can help "accelerate" and "smoothen" the transition (like 802.11 r/k/v) but, unfortunately, they cannot be used in this setup (because there is no "manager" device) and so, the decision, "to roam" or "not to roam" is up to the client fully. Different vendors have different algorithms implemented that decide how and when your client device should switch.

Keep that in mind! Some devices that have a good algorithm (decision-making), will roam properly, while others might stick to a poor signal (furthest) AP.
:::

Most, if not all, of our MikroTik Wi-Fi devices come pre-configured in the ["router" role](../../getting-started/first-time-configuration.md). This guide will show you how to turn them into standalone AP role devices (layer2 bridged APs).

## Access point setup

:::warning
Because we will be changing Wi-Fi and port-related configurations, it is advised to connect to the device's settings via an Ethernet port/cable, using the MAC-address. You can use the [Winbox](../../management-tools/winbox.md) "Neighbors" tab and double-click on the MAC-address of the device in the list. This way, you will not lose access later on when changing interface-related settings.
:::

Overall configuration:

```ros
/interface/wifi
set [ find default-name=wifi2 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.2 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
set [ find default-name=wifi1 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.5 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
add configuration.mode=ap .ssid=guest.ssid.2 disabled=no master-interface=wifi2 name=wifi3 security.authentication-types=wpa2-psk .passphrase=guest.password
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
set [ find default-name=wifi2 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.2 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
```

- `configuration.mode=ap` → configures the interface to work in "access point" mode.
- `configuration.country=Latvia` → selects your actual country, so that you do not break any regulations (your country "laws"). Different country profiles have different allowed output powers per different frequency ranges.
- `ssid=router.ssid.2` → configures the wireless network name (SSID), which the AP needs to broadcast. It can be the same network name as the main router uses, or it can be a different name. For testing, it is better to use a "unique" name so you can differentiate networks. For "client roaming" to happen, use the exact same WiFi name from the router settings.
- `security.authentication-types=wpa2-psk` → selects which authentication types to use. For "client roaming" to happen, use the exact same authentication type from the router settings.
- `passphrase=router.password` → sets the password from the AP's WiFi network. For "client roaming" to happen, use the exact same password from the router settings.

### 5 GHz interface configuration

```ros
/interface/wifi
set [ find default-name=wifi1 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.5 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
```

- `configuration.mode=ap` → Configures the interface to work in "access point" mode.
- `configuration.country=Latvia` → Select your actual country, so that you do not break any regulations (your country's "laws"). Different country profiles have different allowed output powers per different frequency ranges.
- `ssid=router.ssid.5` → Configures the wireless network name (SSID), which the AP needs to broadcast. It can be the same network name as the main router uses, or it can be a different name. For testing, it is better to use a "unique" name so you can differentiate networks. For "client roaming" to happen, use the exact same WiFi name from the router settings.
- `security.authentication-types=wpa2-psk` → Select which authentication types to use. For "client roaming" to happen, use the exact same authentication type from the router settings.
- `passphrase=router.password` → Sets the password from the AP's WiFi network. For "client roaming" to happen, use the exact same password from the router settings.

#### **Increasing 5 GHz range**

Local authorities regulate Wi-Fi devices' output powers. Different frequency ranges in different countries can have different allowed powers. You can check which limitations apply to your country profile using the command:

```ros
/interface/wifi/radio/reg-info country=Latvia 0      
  ranges: 2402-2482/20dBm/40MHz   
          5170-5250/23dBm/160MHz/indoor    
          5250-5330/23dBm/160MHz/indoor/dfs
          5490-5730/30dBm/160MHz/dfs     
          5735-5875/14dBm/80MHz 
```

As per the table, we can see that the most power (using the "Latvia" country profile) we can get is `30 dBm` on channels `5490-5730`.

"dBm" shown in this table represents "allowed EIRP" (EIRP=Tx power + antenna gain). In order not to break any regulations and "laws", the more antenna gain the device has, the lower Tx power is set (if the device has a built-in antenna, it will happen **automatically**), to match the allowed "EIRP" value.

Also note that it could be that the highest "EIRP" channels are "DFS" channels (meaning that if a radar is detected on the channel, the broadcasting stops). This is something to keep in mind!

With this information, per the table, we can see that it would be wise to avoid using the `5735-5875` range, as it only allows `14 dBm`.

The more "EIRP" is allowed on the channel = the more output power will be available = the stronger the signal will be = the bigger the distance you can get.

:::info
Please note that there is a country profile called `Superchannel`. In this profile, there are no software limitations applied to output power. This mode should only be used in controlled environments, or if you have special permission to use it in your region. You can combine it with "reducing" Tx power value directly in the settings to get "custom" power output.
:::

To set a channel or a range, run the command:

```ros
/interface/wifi
set [ find default-name=wifi1 ] channel.frequency=5490-5730
```

### Optional step - adding virtual interface

In case you want to create an additional network (an additional SSID name), you can create a `virtual` interface on top of another interface:

```ros
/interface/wifi
add configuration.mode=ap .ssid=guest.ssid.2 disabled=no master-interface=wifi2 name=wifi3 security.authentication-types=wpa2-psk .passphrase=guest.password
```

- `configuration.mode=ap` → Ensures that it will act as an "access point" interface.
- `ssid=guest.ssid.2` → Configures the wireless network name (SSID), which the AP needs to broadcast. For "client roaming" to happen, use the exact same WiFi name from the router settings.
- `master-interface=wifi2` → Specify which interface to "base" the "virtual" interface on (specify on top of which interface to create it).
- `name=wifi3` → Name the virtual interface.
- `security.authentication-types=wpa2-psk` → Select which authentication types to use. For "client roaming" to happen, use the exact same authentication type from the router settings.
- `passphrase=guest.password` → Sets the password from the AP's WiFi network. For "client roaming" to happen, use the exact same password from the router settings.

:::info
The virtual interface will use the exact same frequency channel, which is used by the `master` interface. The Wi-Fi frequency channel for this interface can not be changed.
:::

### Bridging and listing

[Bridge all ports](../../bridging-and-switching/index.md#example-1):

```ros
/interface/bridge
add auto-mac=no comment=defconf name=bridge
/interface/bridge/port
add interface=all bridge=bridge 
```

And ensure that the bridge is listed as a "LAN" interface (`/interface list member add comment=defconf interface=bridge list=LAN`), so that the firewall rules do not block access to the AP's management:

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

Apply [DHCP-client](../../network-management/dhcp/client#configuration-examples) on top of the bridge interface, so that the AP itself and all its connected clients get IP addresses from the main router.

Disable [DHCP-server](../../network-management/dhcp/server) functionality.

### Address

Remove/disable the default configuration bridge-assigned [IP Address](../../getting-started/networking-fundamentals/index.md#address-configuration), in case your router's network uses the same subnet, so that it does not "conflict" with the gateway IP.
