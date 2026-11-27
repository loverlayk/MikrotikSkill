# Steering clients between access points

> Steer Wi-Fi clients from a weak access point to a better one: a CAPsMAN configuration with a steering profile for several access points, how the access points build the neighbor list, when they send 802.11v BSS...

# Steering clients between access points

**Packages:** `wifi-qcom`, `wifi-qcom-ac`

A phone or laptop that joins one access point often stays with it after its owner walks to the other end of the office, even when another access point is much closer. Steering lets the access points help such a client move. Each access point knows the other access points of the same network, its neighbor group, and suggests a move to a client whose signal has stayed weak. The suggestion is an 802.11v BSS transition management request.

The client makes the decision. It can follow the suggestion, roam later on its own, or ignore it. For clients that ignore it, the access point can disconnect them after a time limit.

This guide sets up steering on a [CAPsMAN](./capsman) network: a router runs CAPsMAN, and the access points are CAPs that it manages.

## Before you begin

- The router that runs CAPsMAN has the address `192.168.99.1` on its LAN bridge `bridge`.
- Each access point has an address in the same network, from DHCP or set by hand, and its LAN port in a bridge. The examples use the bridge name `bridge`; use the name of the bridge on your access points.
- All access points use the same SSID and the same security settings. The interfaces with the same SSID and security settings form one neighbor group. This guide uses a pre-shared key. For networks with 802.1X/EAP authentication, read the neighbor group description in [Steering properties](./#steering-properties).

The example uses cAP ax access points with the `wifi-qcom` package. An access point with the `wifi-qcom-ac` package installed, for example the hAP ac<sup>3</sup>, joins the same network with the same CAP configuration.

## Configure CAPsMAN with a steering profile

On the CAPsMAN router, create the channels, the security profile, the steering profile and one configuration for each band. Then add a provisioning rule for each kind of radio, and enable CAPsMAN on the LAN bridge.

```ros
/interface/wifi/channel
add name=ch-5g frequency=5180,5220 width=20/40mhz
add name=ch-2g frequency=2412,2437,2462 width=20mhz
/interface/wifi/security
add name=sec-office authentication-types=wpa2-psk,wpa3-psk \
    passphrase="change-this-passphrase" ft=yes
/interface/wifi/steering
add name=steer-office transition-threshold=-65
/interface/wifi/configuration
add name=cfg-5g ssid=Office country=Latvia security=sec-office \
    channel=ch-5g steering=steer-office
add name=cfg-2g ssid=Office country=Latvia security=sec-office \
    channel=ch-2g steering=steer-office
/interface/wifi/provisioning
add action=create-dynamic-enabled supported-bands=5ghz-ax \
    master-configuration=cfg-5g name-format=%I-5g
add action=create-dynamic-enabled supported-bands=5ghz-ac \
    master-configuration=cfg-5g name-format=%I-5g
add action=create-dynamic-enabled supported-bands=2ghz-ax \
    master-configuration=cfg-2g name-format=%I-2g
add action=create-dynamic-enabled supported-bands=2ghz-n \
    master-configuration=cfg-2g name-format=%I-2g
/interface/wifi/capsman
set enabled=yes interfaces=bridge
```

What the settings do:

- `country` sets the regulatory rules for the radios. Set it to the country where the access points are installed.
- The channel profiles list the channels the access points can use: 5180 and 5220 MHz (channels 36 and 44) and the 2.4 GHz channels 1, 6 and 11. Each access point uses one channel from the list.
- `transition-threshold=-65` sets the signal level, in dBm, below which an access point starts to suggest a move. An access point measures the signal it receives from the client, the value in the `SIGNAL` column of the registration table. The transmit power of the access point does not change this value. To choose the threshold, look at the signal of clients in the places where they should change to the next access point.
- The request timing stays at the defaults: when the signal of a client stays below the threshold for 10 seconds, the access point sends the first request, then two more 30 seconds apart.
- `ft=yes` turns on 802.11r fast roaming, so a client moves between access points of the network without a full login. It is not needed for steering.
- `name-format=%I-5g` names each interface after the identity of its access point, so the registration table and the log show which access point a client is on.
- A provisioning rule with several values in `supported-bands` matches only radios that support all of them. The example has one rule for each band and Wi-Fi generation, so Wi-Fi 6 and Wi-Fi 5 radios get the same configuration. For Wi-Fi 7 radios, see [CAPsMAN](./capsman).

The steering properties are described in the [WiFi](./#steering-properties) page and in the [CLI reference](../../cli-reference/interface/wifi/steering/).

## Configure the access points

On each access point, set a name that tells where it is, create a datapath that adds the Wi-Fi interfaces to the bridge, turn on the CAP service and hand the radios to CAPsMAN.

```ros
/system/identity
set name=ap-reception
/interface/wifi/datapath
add name=capdp bridge=bridge
/interface/wifi/cap
set enabled=yes caps-man-addresses=192.168.99.1 \
    discovery-interfaces=none
/interface/wifi
set [find] configuration.manager=capsman datapath=capdp
```

Use a different name on each access point, for example `ap-meeting` for the access point in the meeting room.

With `discovery-interfaces=none` the access point connects only to the CAPsMAN at the address in `caps-man-addresses`, and not to another CAPsMAN that it finds on the LAN.

## Check that it works

Each radio of each access point has a dynamic interface with the configuration from the provisioning rules:

```ros
/interface/wifi/print
```

```text
Flags: M - MASTER; D - DYNAMIC; B - BOUND
Columns: NAME, CONFIGURATION.SSID, CHANNEL.FREQUENCY, CHANNEL.WIDTH
#     NAME             CONFIGURATION.SSID  CHANNEL.FREQUENCY  CHANNEL.WIDTH
;;; operated by CAP 192.168.99.7, traffic processing on CAP
0 MDB ap-meeting-2g    Office                           2412  20mhz        
                                                        2437               
                                                        2462               
;;; operated by CAP 192.168.99.7, traffic processing on CAP
1 MDB ap-meeting-5g    Office                           5180  20/40mhz     
                                                        5220               
;;; operated by CAP 192.168.99.8, traffic processing on CAP
2 MDB ap-reception-2g  Office                           2412  20mhz        
                                                        2437               
                                                        2462               
;;; operated by CAP 192.168.99.8, traffic processing on CAP
3 MDB ap-reception-5g  Office                           5180  20/40mhz     
                                                        5220
```

The registration table shows which access point each client is on, and the signal the access point receives from it:

```ros
/interface/wifi/registration-table/print
```

```text
Flags: A - AUTHORIZED
Columns: INTERFACE, SSID, MAC-ADDRESS, UPTIME, LAST-ACTIVITY, SIGNAL, 
         AUTH-TYPE
#   INTERFACE        SSID    MAC-ADDRESS        UPT  LAS  SIG  AUTH-TYPE  
0 A ap-meeting-5g    Office  48:A9:8A:E0:2C:A8  40s  0ms  -34  ft-wpa3-psk
1 A ap-reception-5g  Office  0C:85:E1:1D:D6:AF  32s  0ms  -63  ft-wpa3-psk
```

The access points of the SSID form a dynamic neighbor group. It lists the BSSID of every interface that broadcasts the SSID, on both bands:

```ros
/interface/wifi/steering/neighbor-group/print detail
```

```text
0  name="dynamic-Office-e0f80598"
   bssids=48:8F:5A:A4:65:F5,48:A9:8A:E0:2C:00,48:8F:5A:A4:65:F4,
      48:A9:8A:E0:2C:01
```

The CAPsMAN router logs the roams. To see the steering requests too, turn on debug logging for Wi-Fi, and print the roams and the requests:

```ros
/system/logging/add topics=wireless,debug
/log/print where message~"transition requests|roamed to"
```

```text
 2026-11-26 12:47:18 wireless,info 0C:85:E1:1D:D6:AF@ap-reception-5g(Office) roamed to 0C:85:E1:1D:D6:AF@ap-meeting-5g(Office), signal strength -53, channel 5220/ax/Ce/I
 2026-11-26 12:47:46 wireless,info 0C:85:E1:1D:D6:AF@ap-reception-5g(Office) roamed to 0C:85:E1:1D:D6:AF@ap-meeting-5g(Office), signal strength -57, channel 5220/ax/Ce/I
```

In this output a client has roamed twice from the access point at the reception to the one in the meeting room. When a client stays after all requests, the log shows the line `all 3 transition requests sent` for it. Some moves appear as a disconnect from one interface and a connect to another, and not as `roamed to`.

The debug messages fill the log. Remove the logging rule when you are done:

```ros
/system/logging/remove [find topics=wireless,debug]
```

## Disconnect clients that do not move

Some clients ignore the requests. `transition-time` sets how long a client can stay a transition candidate before the access point disconnects it:

```ros
/interface/wifi/steering
set steer-office transition-time=40s
```

The access point disconnects a client that is still below the threshold 40 seconds after it became a candidate, and logs the reason:

```ros
/log/print where message~"better AP"
```

```text
 2026-11-26 12:53:50 wireless,info 0C:85:E1:1D:D6:AF@ap-reception-5g(Office) disconnected, didn't switch to better AP in time (steering), signal strength -76, channel 5220/ac/Ce/I
 2026-11-26 12:54:05 wireless,info 48:A9:8A:E0:2C:A8@ap-reception-5g(Office) disconnected, didn't switch to better AP in time (steering), signal strength -78, channel 5220/ac/Ce/I
 2026-11-26 12:54:40 wireless,info 0C:85:E1:1D:D6:AF@ap-reception-5g(Office) disconnected, didn't switch to better AP in time (steering), signal strength -72, channel 5220/ac/Ce/I
```

The client then connects again and chooses the access point itself. When the access point that disconnected it is still the best one the client hears, the client connects to it again.

## How steering behaves

- The access point compares the signal it receives from the client with `transition-threshold`. When the signal stays below the threshold for `transition-threshold-time`, the client becomes a transition candidate. The access point sends the first request immediately and then one every `transition-request-period`, `transition-request-count` requests in total.
- The client decides whether to move. A client that hears no access point that is clearly better can stay where it is.
- A client that roams with 802.11r is logged on the CAPsMAN router as `roamed to` with the new interface.
