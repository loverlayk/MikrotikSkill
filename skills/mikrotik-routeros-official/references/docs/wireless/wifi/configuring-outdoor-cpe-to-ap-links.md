# Configuring outdoor CPE to AP links

> Guide for configuring outdoor CPE-to-AP Wi-Fi links using MikroTik RouterOS's wifi-qcom package, covering frequency selection, country regulations, AP mode setup, security, and distance considerations for long-range...

# Configuring outdoor CPE to AP links

**Package:** `wifi-qcom`

It is no secret that Wi-Fi range for indoor access points is limited. It is affected, mostly, by local regulations, which restrict the device's output power (depending on which frequency channel is used). A typical indoor Wi-Fi connection is established between an AP (access point) and a client (station) device (smartphone, laptop, etc.).

Indoor APs are, usually, equipped with omnidirectional antennas (which allow broadcasting the signal in a "donut" shape around the AP), which have a relatively low antenna gain. For indoor and short distance outdoor installations, it is a perfect antenna to use. Using a simple home AP with omnidirectional antennas, you can achieve a distance of up to ±100 meters in the "ideal" interference-free line of sight setup, which is reduced much further inside buildings.

However! If you were to increase the antenna gain of the AP and "direct" the signal at a smaller angle towards a specific destination (instead of broadcasting the signal in 360°), you could achieve a much longer distance connection (if the station device is positioned within the directed angle). This is where outdoor long-range APs and CPEs come into play. They allow establishing Wi-Fi connections over multiple kilometer distances.

Long distance connections require you to have a device running in "AP" mode and a client-side device, running in "station" mode. Multiple stations can be connected to a single AP.

:::info
This guide is meant for 802.11 AX devices running `wifi-qcom` package/drivers.
:::

## AP setup

### Frequency selection

As mentioned in the introduction, local authorities regulate Wi-Fi devices' output powers. Different frequency ranges in different countries can have different allowed powers. You can check which limitations apply to your country profile using the command:

```ros
/interface/wifi/radio/reg-info country=Latvia 0           
  ranges: 2402-2482/20dBm/40MHz            
          5170-5250/23dBm/160MHz/indoor    
          5250-5330/23dBm/160MHz/indoor/dfs
          5490-5730/30dBm/160MHz/dfs       
          5735-5875/14dBm/80MHz 
```

As per the table, we can see that the most power (using the "Latvia" country profile) we can get is `30 dBm` on channels `5490-5730`.

"dBm" shown in this table represents "allowed EIRP" (EIRP=Tx power + antenna gain). Not to break any regulations and "laws", the more antenna gain the device has, the lower Tx power is set (if the device has a built-in antenna, it will happen **automatically**), to match the allowed "EIRP" value.

Also note that it could be that the highest "EIRP" channels are "DFS" channels (meaning that if a radar is detected on the channel, the broadcasting stops). This is something to keep in mind!

With this information, per the table, we can see that it would be wise to avoid using the `5735-5875` range, as it only allows `14 dBm`.

The more "EIRP" is allowed on the channel = the more output power will be available = the stronger the signal will be = the bigger distance you can get.

:::note
Please note that there is a country profile called "Superchannel". In this profile, there are no software limitations applied to output powers. This mode should only be used in controlled environments, or if you have special permission to use it in your region. You can combine it with "reducing" the Tx power value directly in the settings to get "custom" power output.
:::

Frequency-wise, additionally, remember that the lower the channel width is, the less interference and the bigger the distance you can get. Meaning, for longer distances, use 20 MHz.

### WiFi interface configuration

To configure AP mode, run the command:

```ros
/interface/wifi
set [ find default-name=wifi1 ] channel.frequency=5500 configuration.country=Latvia .mode=ap .ssid=input_your_SSID_here security.authentication-types=wpa2-psk .passphrase=input_your_password_here channel.width=20mhz
```

- `channel.frequency` → selects a frequency channel on which to run the AP. You can skip this, if you want to use "automatic" channel selection.
- `configuration.country` → applies the country profile, so that the device follows output power regulations.
- `.mode=ap` → sets the WiFi interface to operate in "access point" mode.
- `.ssid=input_your_SSID_here` → configures the SSID name the AP is going to broadcast.
- `security.authentication-types=wpa2-psk` → specifies which authentication types to support.
- `.passphrase=input_your_password_here` → sets the password for the SSID.

:::warning
There is a "distance" parameter that you have to configure additionally if your link is longer than 2km. This setting does not work for `wifi-qcom-ac` drivers.
:::

- `configuration.distance=distance_in_km` → sets maximum link distance in kilometers. The value should reflect the distance to the AP or station that is furthest from the device. The unconfigured value allows usage of 2 km links.
- `channel.width=20mhz` → sets channel width. The lower the width of the channel, the longer the distance (less interference).

### Other settings to consider

#### Scenario #1

In case you already have a DHCP-server in the topology that is responsible for providing IP addresses to the network, and you want to install the AP behind it:

![](./img/configuring-outdoor-cpe-to-ap-links-01.webp)

1. Ensure that the AP has a [bridge interface](../../bridging-and-switching/index.md#example) added and that all Ethernet and WiFi ports [are a part of it](../../bridging-and-switching/index.md#example-1).
2. Set up [DHCP-client](../../network-management/dhcp/client) on that bridge or, statically, add an [IP address](../../getting-started/networking-fundamentals/index.md#address-configuration) and a [default route](../../user-guides/routing-and-networking-protocols/routing-decision.md#default-route), instead.
3. Change [interface list members](../../cli-reference/interface/list/member) roles if required.

#### Scenario #2

In case you want to have the AP itself act as a DHCP-server for stations:

![](./img/configuring-outdoor-cpe-to-ap-links-02.webp)

1. Configure an ethernet port as an uplink/WAN port, i.e. set up a [DHCP-client](../../network-management/dhcp/client) or [static IP](../../getting-started/networking-fundamentals/index.md#address-configuration) for the ethernet interface, set up a default [route](../../user-guides/routing-and-networking-protocols/routing-decision.md) and categorize the port as a "WAN" port in the [interface list](../../cli-reference/interface/list) settings.
2. Set up a [DHCP-server](../../network-management/dhcp/server) on top of the WiFi interface (or on top of the bridge, which WiFi port is a part of) and add a respective  [IP address](../../getting-started/networking-fundamentals/index.md#address-configuration) to that interface.

## Station setup

### WiFi interface configuration

To configure station mode, run the command:

```ros
/interface/wifi
set [ find default-name=wifi1 ] channel.frequency=5500 configuration.country=Latvia .mode=station .ssid=input_your_SSID_here security.authentication-types=wpa2-psk .passphrase=input_your_password_here
```

- `channel.frequency` → selects a frequency channel, which the AP uses. You can skip this if you want to use "automatic" channel selection.
- `configuration.country` → applies the country profile, so that the device follows output power regulations.
- `.mode=station` → sets the WiFi interface to operate in "station" mode.
- `.ssid=input_your_SSID_here` → input the SSID name that the AP is broadcasting.
- `security.authentication-types=wpa2-psk` → specifies which authentication types to support.
- `.passphrase=input_your_password_here` → set the password which the AP expects.

:::warning
There is a "distance" parameter that you have to configure additionally if your link is longer than 2km. This parameter does not work for `wifi-qcom-ac` drivers.
:::

- `configuration.distance=distance_in_km` → Sets maximum link distance in kilometers. The value should reflect the distance to the AP or station that is furthest from the device. An unconfigured value allows usage of 2 km links.

### Other settings to consider

#### Scenario #1

Scenario where station's WiFi interface is categorized as a "WAN" interface, which allows station's clients to stay hidden behind [NAT](../../firewall-and-quality-of-service/firewall/nat.md). This is a factory configuration applied to most CPE devices.

An example of such a topology:

![](./img/configuring-outdoor-cpe-to-ap-links-03.webp)

This type of setup requires the CPE to have:

1. The WiFi interface categorized as "WAN" port in the [interface list members](../../cli-reference/interface/list/member) menu.
2. a [DHCP-server](../../network-management/dhcp/server) running on the "other/ethernet" interfaces (it is suggested to ensure that AP's DHCP server and Station's DHCP server networks do not use the same subnet, as it can lead to layer3/routing issues).
3. a [DHCP-client](../../network-management/dhcp/client) or a [static IP](../../getting-started/networking-fundamentals/index.md#address-configuration) applied to the WiFi interface and a [default route](../../user-guides/routing-and-networking-protocols/routing-decision.md) configured.
4. [`mode=station`](../user-guides/wireless-station-modes.md#mode-station) configured in the WiFi settings.

#### Scenario #2

Scenario where you can bridge station's ports, so that the CPE itself and all CPE's clients obtain DHCP addresses from the AP.

An example of such a topology:

![](./img/configuring-outdoor-cpe-to-ap-links-04.webp)

This type of setup requires the CPE to have:

1. All ports (WiFi and Ethernet) are added into the same [bridge interface](../../bridging-and-switching/index.md#example).
2. The bridge is categorized as a "LAN" interface in the [interface list members](../../cli-reference/interface/list/member) menu.
3. A [DHCP-server](../../network-management/dhcp/server) is disabled.
4. A [DHCP-client](../../network-management/dhcp/client) or a [static IP](../../getting-started/networking-fundamentals/index.md#address-configuration) is applied to the bridge interface.
5. [`mode=station-bridge`](../user-guides/wireless-station-modes.md#mode-station-bridge) is configured in the WiFi settings:

```ros
/interface/wifi
set [ find default-name=wifi1 ] configuration.mode=station-bridge
```

## Verification

On a successful connection, both the AP and the Station should display a new entry in the "Registration" table:

```ros
/interface/wifi/registration-table/print
Flags: A - AUTHORIZED
Columns: INTERFACE, SSID, MAC-ADDRESS, UPTIME, LAST-ACTIVITY, SIGNAL, AUTH-TYPE, BAND
#   INTERFACE  SSID        MAC-ADDRESS        UPTIME    LAST-ACTIVITY  SIGNAL  AUTH-TYPE  BAND   
0 A wifi1      input_SSID  XX:YY:ZZ:AA:30:6E  6h24m21s  0ms            -72     wpa2-psk   5ghz-ax
```

You can also check, via the CPE, whether it properly sees/recognizes the AP using the "scan" command:

```ros
/interface/wifi/scan [find where name=wifi1]
Flags: A - ACTIVE
Columns: ADDRESS, SSID, CHANNEL, SECURITY, SIGNAL, STA-COUNT
  ADDRESS            SSID               CHANNEL           SECURITY                              SIGNAL  STA-COUNT
A XX:YY:ZZ:AA:F4:28  SSID_Y             5620/ax           WPA2-PSK/WPA3-PSK                     -60             0
A XX:YY:ZZ:BB:0B:DA  SSID_X             5745/ax/Ce        WPA3-PSK                              -68             0
A XX:YY:ZZ:CC:0B:DA  input_SSID         5745/ax/Ce        WPA2-PSK                              -68             0
A XX:YY:ZZ:DD:0B:DA                     5745/ax/Ce        WPA2-PSK                              -68             0
```
