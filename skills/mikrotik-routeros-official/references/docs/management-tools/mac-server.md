# MAC server

> The RouterOS MAC server lets you reach a router by its MAC address on the same layer-2 segment, without IP configuration: connect with MAC Telnet, find routers with MAC scan, limit MAC Telnet and MAC WinBox to...

# MAC server

The MAC server lets you reach a router by its MAC address from a device on the same layer-2 segment, without any IP configuration on either side. It serves three things:

- MAC Telnet - A console session, like Telnet over IP. The RouterOS client is `/tool/mac-telnet`.
- MAC WinBox - [WinBox](winbox) connects to the router by its MAC address.
- MAC ping - Answers pings sent to the router's MAC address.

Use MAC access to recover a router whose IP settings are wrong or missing, and for the first setup of a new router. The default configuration allows MAC Telnet and MAC WinBox only on the interfaces in the `LAN` interface list, which holds the LAN bridge: on most routers every port except the WAN port `ether1`, and the Wi-Fi interfaces. Without the default configuration, they are allowed on all interfaces. The MAC ping server is on by default. In production networks, you should turn MAC access off or limit it to trusted interfaces; see [Securing your router](../getting-started/securing-your-router#routeros-mac-access). To reach routers beyond one layer-2 segment by MAC address, use [RoMON](romon).

## Connect with MAC Telnet

From a computer, use [WinBox](winbox#device-list-section): the **Neighbors** tab lists the routers on the network, and selecting the MAC address connects by MAC WinBox. WinBox also has a terminal. From another RouterOS device, find the MAC address of the router with MAC scan or in the [neighbor list](../system-information-and-utilities/neighbor-discovery), then connect with MAC Telnet:

```ros
/tool/mac-telnet FE:F1:E6:82:D5:B6
```

```text
Login: admin
Password:
Trying FE:F1:E6:82:D5:B6...
Connected to FE:F1:E6:82:D5:B6

  MMM      MMM       KKK                          TTTTTTTTTTT      KKK
  MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK
  MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK  KKK
  MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK
  MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK
  MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK

  MikroTik RouterOS 7.25beta5 (c) 1999-2026       https://www.mikrotik.com/

Press F1 for help

[admin@Test2] >
```

MAC Telnet logs in with a user name and password; SSH keys do not apply. The user's group needs the `telnet` policy. After you log in, correct the IP settings, for example in [`/ip/address`](../cli-reference/ip/address). When the target does not answer or refuses the connection, for example because MAC Telnet is not allowed on the interface the request arrives on, the client prints `Trying ...` and returns to the local prompt without an error message.

Without `interface`, the client sends its connection attempts out of every interface of the router. To send them out of one interface only:

```ros
/tool/mac-telnet FE:F1:E6:82:D5:B6 interface=ether1
```

The router you connect to lists the open MAC Telnet sessions, with the interface the session arrived on and the MAC address of the client:

```ros
/tool/mac-server/sessions/print
```

```text
Columns: INTERFACE, SRC-ADDRESS, UPTIME
#  INTERFACE  SRC-ADDRESS        UPTIME
0  ether2     DC:2C:6E:E7:10:6A  2s
```

The list shows MAC Telnet sessions only, not MAC WinBox connections. The sessions also appear in `/user/active` with `mac-telnet` in the `VIA` column.

## Find routers with MAC scan

MAC scan lists the devices that send MikroTik Neighbor Discovery (MNDP) announcements on an interface, with their MAC address and IPv4 address:

```ros
/tool/mac-scan interface=ether2 duration=8s
```

```text
Columns: MAC-ADDRESS, ADDRESS, AGE
MAC-ADDRESS        ADDRESS      AGE
FE:F1:E6:82:D5:B6  203.0.113.1   17
```

`AGE` is the time in seconds since the device's last announcement. The list comes from [neighbor discovery](../system-information-and-utilities/neighbor-discovery), not from the MAC server: a device appears whatever its MAC server settings are, and a device whose neighbor discovery is off on that interface does not appear. The list includes devices heard before the scan started, so `AGE` can be longer than `duration`; devices announce themselves every 30 seconds by default. `/ip/neighbor/print` shows the same devices with more details, such as the identity and RouterOS version.

On a bridge, scan one of its ports or `interface=all`: the bridge interface itself shows no devices. Without `duration`, the scan runs until you stop it with <kbd>Control</kbd>+<kbd>C</kbd>. MAC scan is not available on devices with the SMIPS architecture.

## Allow MAC access only on trusted interfaces

MAC Telnet and MAC WinBox each have their own `allowed-interface-list` setting: `/tool/mac-server` for MAC Telnet and `/tool/mac-server/mac-winbox` for MAC WinBox. Each takes an [interface list](../cli-reference/interface/list/).

To allow MAC Telnet and MAC WinBox only on the LAN:

```ros
/tool/mac-server/set allowed-interface-list=LAN
/tool/mac-server/mac-winbox/set allowed-interface-list=LAN
```

The default configuration already has the `LAN` list, with the LAN bridge in it. On a router without it, create the list first:

```ros
/interface/list/add name=LAN
/interface/list/member/add list=LAN interface=bridge
```

Check the current settings with `/tool/mac-server/print` and `/tool/mac-server/mac-winbox/print`.

Put the bridge in the list, not its ports: a bridge in the list allows connections that arrive through any of its ports, and a bridge port alone in the list does not allow them. A change applies to the next connection immediately; sessions that are already open stay open.

To keep one port of the bridge out, for example the port of a guest Wi-Fi network, drop MAC access on it with a bridge filter rule, or put the guests on their own bridge:

```ros
/interface/bridge/filter/add chain=input in-interface=wifi2 \
    mac-protocol=ip ip-protocol=udp dst-port=20561 action=drop
```

To turn MAC Telnet and MAC WinBox off, set the lists to `none`:

```ros
/tool/mac-server/set allowed-interface-list=none
/tool/mac-server/mac-winbox/set allowed-interface-list=none
```

An interface list you create without members blocks MAC access in the same way.

:::note
The IP firewall does not protect MAC access: an IP filter rule that drops UDP port 20561 does not block MAC Telnet or MAC ping. Limit MAC access with `allowed-interface-list`, or with a bridge filter rule on a bridge port. For the other ports RouterOS uses, see [Services](../system-information-and-utilities/services).
:::

## MAC ping

The MAC ping server (`/tool/mac-server/ping`) answers pings sent to the router's MAC address. It is enabled by default. To ping a MAC address, see [Ping a MAC address](../diagnostics-monitoring-and-troubleshooting/ping#ping-a-mac-address).

To turn the MAC ping server off:

```ros
/tool/mac-server/ping/set enabled=no
```

With the server off, the router no longer answers MAC pings, and it cannot send MAC pings either: its own MAC pings fail with the status `unknown interface`. ARP ping works in both directions regardless of this setting.

## Technical details

### Transport

MAC Telnet, MAC WinBox and MAC ping use UDP port 20561 inside Ethernet frames addressed to the MAC address of the target. The IP header carries the addresses 0.0.0.0 and 255.255.255.255, so the packets do not depend on IP configuration. The MAC server takes them directly from the interface, so IP firewall rules do not stop them.

### Security

MAC Telnet is not encrypted. The commands you type and the router's output cross the link in clear text. The password is not sent in clear: the login uses a challenge and response. Use MAC Telnet on trusted links, for example to recover a router, and use SSH for regular access.

A MAC login has no IP address, so the `address` setting of a user in `/user` does not apply to it: a user restricted to certain IP addresses can still log in with MAC Telnet. The group policies do apply.

For all parameters, see [`/tool/mac-server`](../cli-reference/tool/mac-server/), [`/tool/mac-telnet`](../cli-reference/tool/mac-telnet) and [`/tool/mac-scan`](../cli-reference/tool/mac-scan) in the CLI reference.
