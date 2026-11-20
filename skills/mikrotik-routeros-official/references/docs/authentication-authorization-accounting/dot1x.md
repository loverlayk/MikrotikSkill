# Dot1X

> Dot1X is the IEEE 802.1X implementation of RouterOS: authenticate the devices on Ethernet ports with RADIUS, assign VLANs, use guest, reject and server-fail VLANs, authenticate by MAC address, add dynamic switch...

# Dot1X

Dot1X is the RouterOS implementation of IEEE 802.1X, port-based network access control. A device must authenticate before the Ethernet port that it is connected to passes its traffic. The authentication uses EAP over LAN (EAPOL). 802.1X has three roles:

- The supplicant is the device that connects, the client. RouterOS can be a supplicant: `/interface/dot1x/client`.
- The authenticator is the switch or router with the port. RouterOS can be an authenticator: `/interface/dot1x/server`.
- The authentication server is a [RADIUS](radius) server that checks the credentials. RouterOS can be one with the [User Manager](user-manager) package.

![A supplicant connects to a port of the authenticator, and the authenticator asks the RADIUS server](./img/dot1x-01.webp)

:::note
Dot1X is not available on SMIPS devices (hAP lite, hAP lite TC and hAP mini).
:::

## Authenticate the devices on a port

Add the RADIUS server for the `dot1x` service, and add the port to the Dot1X server:

```ros
/radius/add address=10.1.2.3 secret=Radius-Secret-1 service=dot1x
/interface/dot1x/server/add interface=ether2
```

- The RADIUS server does not have to be in the same network as the authenticator, but the authenticator must reach it. When the path to the server is not trusted, use RadSec: see [RADIUS](radius).
- `interface` is an Ethernet interface or an interface list. For many ports, use a list (the example follows).
- From now on the port passes only EAPOL frames until a device authenticates. Do not add the port that you manage the router through.

One server entry with an interface list covers several ports:

```ros
/interface/list/add name=dot1x-ports
/interface/list/member/add list=dot1x-ports interface=ether3
/interface/list/member/add list=dot1x-ports interface=ether4
/interface/dot1x/server/add interface=dot1x-ports
```

`/interface/dot1x/server/state` shows the state of each port:

```ros
[admin@MikroTik] > /interface/dot1x/server/state/print
Columns: INTERFACE, STATUS
#  INTERFACE  STATUS       
0  ether2     un-authorized
```

When a device authenticates, the state changes to `authorized` and the device is listed in `/interface/dot1x/server/active`:

```ros
[admin@MikroTik] > /interface/dot1x/server/active/print detail
0  interface=ether2 username="tst" client-mac=52:54:0B:7D:02:01
   session-id="00002086" auth-info="dot1x"
```

| State | Meaning |
| :-- | :-- |
| `authorized` | The port passes traffic. |
| `un-authorized` | No device is authenticated. The port passes only EAPOL frames. |
| `rejected-holding` | The RADIUS server rejected the device. |
| `iface-down` | The interface is not running. |

An authorized port accepts all traffic that it receives. If the port is connected to a shared medium with several devices, all of them have access after one of them authenticates. Dynamic switch rules can limit the port to the MAC address of the authenticated device.

## Assign a VLAN from RADIUS

The RADIUS server can put the port of a device into a VLAN. The port must be in a bridge with VLAN filtering. On a router that already has a bridge, read [Bridge VLAN table](../bridging-and-switching/user-guides/bridge-vlan-table) before you turn VLAN filtering on: a wrong order of the steps can cut your access to the router.

```ros
/interface/bridge/add name=bridge1 vlan-filtering=yes
/interface/bridge/port/add bridge=bridge1 interface=ether1
/interface/bridge/port/add bridge=bridge1 interface=ether2
/interface/bridge/vlan/add bridge=bridge1 tagged=ether1 vlan-ids=12
```

`ether1` is the uplink and carries VLAN 12 tagged.

The server sends the VLAN in three attributes of the Access-Accept. In the `users` file of FreeRADIUS:

```text
vlanuser  Cleartext-Password := "Example-pass-1"
          Tunnel-Type = VLAN,
          Tunnel-Medium-Type = IEEE-802,
          Tunnel-Private-Group-Id = "12"
```

With the `radius,debug` [log](../diagnostics-monitoring-and-troubleshooting/log/) topics, the attributes are in the log of the authenticator:

```ros
/system/logging/add topics=radius,debug action=memory
```

```text
09:51:45 radius,debug,packet received Access-Accept with id 64 from 10.1.2.3:1812
09:51:45 radius,debug,packet     Tunnel-Type = 13 
09:51:45 radius,debug,packet     Tunnel-Medium-Type = 6 
09:51:45 radius,debug,packet     Tunnel-Private-Group-ID = "12" 
(..)
09:51:45 radius,debug,packet     User-Name = "dot1x-user" 
```

After the authentication the session has the VLAN ID:

```ros
[admin@MikroTik] > /interface/dot1x/server/active/print detail
0  interface=ether2 username="vlanuser" client-mac=52:54:0B:7D:02:01
   session-id="0f002086" vlan-id=12 auth-info="dot1x"
```

The bridge adds the port to VLAN 12 as an untagged port. `/interface/bridge/vlan/print` shows this in a dynamic entry with the comment `added by pvid`.

- Only devices with hardware offloaded VLAN filtering do this in the switch chip.
- A server that authenticates with EAP-PEAP or EAP-TTLS must send the attributes in the outer reply. In FreeRADIUS this is `use_tunneled_reply = yes`.

## Put devices that fail into a VLAN

A port can get a VLAN when the authentication does not succeed. A typical use is a guest network. All three settings need a bridge with VLAN filtering, and all are off by default.

```ros
/interface/dot1x/server/set [find interface=ether2] \
    guest-vlan-id=50 reject-vlan-id=30 server-fail-vlan-id=40
```

| Setting | The port gets the VLAN when | `auth-info` of the session |
| :-- | :-- | :-- |
| `guest-vlan-id` | The device does not answer EAP requests, because it has no supplicant. The VLAN is set after three `retrans-timeout` periods. | `dot1x (guest vlan)` |
| `reject-vlan-id` | The RADIUS server answers with Access-Reject. | `dot1x (reject vlan)` |
| `server-fail-vlan-id` | The RADIUS server does not answer. | `dot1x (server fail vlan)` |

In each case the state of the port is `authorized` and the session shows the VLAN:

```ros
[admin@MikroTik] > /interface/dot1x/server/active/print detail
0  interface=ether2 username="vlanuser" client-mac=52:54:0B:7D:02:01
   session-id="11002086" vlan-id=30 auth-info="dot1x (reject vlan)"
```

- With the default `retrans-timeout` of 30 seconds, a device without a supplicant gets the guest VLAN after 90 seconds.
- A device of a visitor that has a supplicant gets an Access-Reject and not the guest VLAN. To give all visitors the same network, set `reject-vlan-id` to the same VLAN as `guest-vlan-id`.
- Add the VLANs to the uplink port as tagged in the VLAN table of the bridge.
- When a supplicant starts on a port in the guest VLAN and authenticates, the port leaves the guest VLAN.
- `reject-vlan-id` is not used when the RADIUS server does not answer. Without `server-fail-vlan-id`, the authentication then times out and the port stays closed.

## Authenticate devices by MAC address

Printers, cameras and other devices without a supplicant can be authenticated by their MAC address. The authenticator asks the RADIUS server with the MAC address of the device as the user name:

```ros
/interface/dot1x/server/set [find interface=ether2] \
    auth-types=mac-auth
```

In the `users` file of FreeRADIUS, an entry for a device with the default settings accepts the MAC address without a password:

```text
52:54:0B:7D:02:01  Auth-Type := Accept
```

- The authenticator learns the MAC address from a frame that the device sends. A device that sends nothing is not authenticated.
- With `mac-auth-mode=mac-as-username` (the default) the password of the request is empty. With `mac-as-username-and-password` the MAC address is also the password.
- `radius-mac-format` sets how the MAC address is written. The default is `XX:XX:XX:XX:XX:XX`.
- The RADIUS server can send a VLAN in the same way as for a Dot1X device.

The session has `auth-info="mac-auth"`:

```ros
[admin@MikroTik] > /interface/dot1x/server/active/print detail
0  interface=ether2 username="52:54:0B:7D:02:01" client-mac=52:54:0B:7D:02:01
   session-id="17002086" vlan-id=12 auth-info="mac-auth"
```

With both types, the authenticator tries Dot1X first. If the device does not answer in three `retrans-timeout` periods, it tries the MAC address:

```ros
/interface/dot1x/server/set [find interface=ether2] \
    auth-types=dot1x,mac-auth
```

A MAC address is easy to copy from another device. Give MAC-authenticated devices only the access that they need, for example their own VLAN.

## Re-authenticate and send accounting

- `reauth-period` makes the authenticator authenticate each device again after this time. A Dot1X device gets a new EAP request, and a MAC-authenticated device is checked with the RADIUS server again. By default devices are not authenticated again.
- `accounting=yes` (the default) sends the start and the end of each session to the RADIUS server. `interim-update` also sends an update at this interval.

```ros
/interface/dot1x/server/set [find interface=ether2] \
    reauth-period=1h interim-update=5m
```

## Add switch rules for a device

The RADIUS server can limit what an authenticated device can reach. It sends rules in the Mikrotik-Switching-Filter attribute, and the authenticator adds them as dynamic [switch rules](../bridging-and-switching/switch-chip-features) on the port of the device. The rules exist while the session is active and the interface is running.

:::warning
Dynamic switch rules need a switch chip with rule support: MikroTik devices with a Marvell Prestera switch chip, and the QCA8337, Atheros8327 and Atheros8316 switch chips. CRS1xx and CRS2xx series switches do not support them. Each device has a maximum number of rules: see [MikroTik devices with Marvell Prestera switch](../bridging-and-switching/marvell-prestera-switch-chip-features) and the [switch chip table](../bridging-and-switching/switch-chip-features).
:::

The format of the attribute:

- The conditions are `mac-protocol`, `src-mac-address`, `src-address` (IPv4 address and mask), `dst-address` (IPv4 address and mask), `protocol` (IPv4), `src-port` and `dst-port`.
- `mac-protocol` and `protocol` take a decimal or a hexadecimal number, for example `protocol 17` or `protocol 0x11`.
- `src-port` and `dst-port` take one port or a range, for example `src-port 10` or `src-port 10-20`.
- `src-mac-address` takes the format `xx:xx:xx:xx:xx:xx` or `xxxxxxxxxxxx`. The word `none` makes a rule without a source MAC address: `src-mac-address none`.
- The authenticator sets `switch` and `ports` of each rule. It also sets `src-mac-address` to the address of the device, unless the attribute sets it.
- A rule ends with `action drop` or `action allow`. Without an action, the rule allows.
- Several rules are separated with commas.

Drop ARP frames (EtherType 0x0806, decimal 2054):

```text
Mikrotik-Switching-Filter = "mac-protocol 2054 action drop"
```

```ros
/interface/ethernet/switch/rule/print
Flags: X - disabled, I - invalid, D - dynamic 
 0  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF mac-protocol=arp copy-to-cpu=no redirect-to-cpu=no mirror=no new-dst-ports=""
```

Allow UDP (IP protocol 17) to the destination port 100 and drop everything else:

```text
Mikrotik-Switching-Filter = "protocol 17 dst-port 100 action allow, action drop"
```

```ros
/interface/ethernet/switch/rule/print
Flags: X - disabled, I - invalid, D - dynamic 
 0  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF protocol=udp dst-port=100 copy-to-cpu=no redirect-to-cpu=no mirror=no 

 1  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF copy-to-cpu=no redirect-to-cpu=no mirror=no new-dst-ports=""
```

Allow only the MAC address of the authenticated device and drop all other source addresses:

```text
Mikrotik-Switching-Filter = "action allow, src-mac-address none action drop"
```

```ros
/interface/ethernet/switch/rule/print 
Flags: X - disabled, I - invalid; D - dynamic 
 0  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 src-mac-address=CC:2D:E0:01:6D:EB/FF:FF:FF:FF:FF:FF copy-to-cpu=no redirect-to-cpu=no mirror=no 

 1  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 copy-to-cpu=no redirect-to-cpu=no mirror=no new-dst-ports="" 
```

### Example

The device on `ether2` can reach only the network 192.168.50.0/24 on the UDP port 50. The switch rules work on hardware offloaded bridge ports, so check the `H` flag first:

```ros
/interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE                   BRIDGE                   HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0   H ether1                      bridge1                  yes    1     0x80         10                 10       none
 1   H ether2                      bridge1                  yes    1     0x80         10                 10       none
 2   H ether12                     bridge1                  yes    1     0x80         10                 10       none
```

The RADIUS server sends the attribute in the Access-Accept:

```text
02:35:38 radius,debug,packet received Access-Accept with id 121 from 10.1.2.3:1812 
(..)
02:35:38 radius,debug,packet     MT-Switching-Filter = "mac-protocol 2048 dst-address 192.168.50.0/24 dst-port 50 protocol 17 action allow,action drop"
```

The authenticator adds two rules:

```ros
/interface/ethernet/switch/rule/print 
Flags: X - disabled, I - invalid; D - dynamic 
 0  D ;;; dot1x dynamic
      switch=switch1 ports=ether2 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF mac-protocol=ip dst-address=192.168.50.0/24 protocol=udp dst-port=50 copy-to-cpu=no redirect-to-cpu=no mirror=no 

 1  D ;;; dot1x dynamic
      switch=switch1 ports=ether2 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF copy-to-cpu=no redirect-to-cpu=no mirror=no new-dst-ports="" 
```

## Connect a RouterOS port as a supplicant

A router or switch can authenticate its own port to an 802.1X network. The methods are EAP-MSCHAPv2, EAP-PEAP (PEAPv0 with EAP-MSCHAPv2), EAP-TTLS and EAP-TLS.

With a name and a password:

```ros
/interface/dot1x/client/add interface=ether2 \
    eap-methods=eap-peap identity=tst password=Example-pass-1
```

- EAP-PEAP, EAP-TTLS and EAP-TLS check the certificate of the RADIUS server. Import the certificate authority that signed it as a trusted [certificate](certificates) first. Without it the client stays in `authenticating`, and the log has `no trusted CA certificate found`.
- EAP-MSCHAPv2 needs no certificate, but it does not check the server.
- `anon-identity` is the name that EAP-PEAP and EAP-TTLS show outside the encrypted tunnel. Without it, `identity` is used. With it, the authenticator lists the session with the outer name.
- `eap-methods` can list several methods.

EAP-TLS uses a client certificate in place of the password. Import the certificate with its private key, and name it in `certificate`:

```ros
/interface/dot1x/client/add interface=ether2 eap-methods=eap-tls \
    identity=tst certificate=dot1x-client
```

```ros
[admin@MikroTik] > /interface/dot1x/client/print detail
0  ;;; d1x
   interface=ether2 eap-methods=eap-tls identity="tst" anon-identity=""
   certificate=dot1x-client status="authenticated"
```

| Status | Meaning |
| :-- | :-- |
| `authenticated` | The authentication succeeded. |
| `authenticating` | The client reached the authenticator and the authentication is in progress. |
| `rejected` | The server refused the client. |
| `disabled` | The client is disabled. |
| `interface is down` | The interface is not running. |
| `error` | An internal error. |

## Check and troubleshoot

| What you see | What to check |
| :-- | :-- |
| The port stays `un-authorized`. | The device has no supplicant. For such devices, use `guest-vlan-id` or `auth-types=dot1x,mac-auth`. |
| The port is `rejected-holding`, the client is `rejected`. | The RADIUS server refused the name, the password or the certificate. Check the log of the server. |
| The client stays `authenticating`, and its log has `no trusted CA certificate found`. | Import the certificate authority of the RADIUS server on the client as a trusted certificate. |
| The client stays `authenticating` and the RADIUS server gets no request. | The authenticator cannot reach the server. Check the `/radius` entry: it needs `service=dot1x`, the address and the secret. See [RADIUS](radius). |
| The device is authenticated but not in the VLAN. | The bridge needs `vlan-filtering=yes`, and the Access-Accept must have the three tunnel attributes. Check them with the `radius,debug` log topics. |

Keep RSTP or MSTP enabled on a bridge that has Dot1X ports: without a spanning tree protocol, EAP packets from the device may not be accepted. A bridge has `protocol-mode=rstp` by default. For a port that must not send BPDUs or must ignore received BPDUs, set `edge=yes` on the bridge port.

## Read more

- [`/interface/dot1x/server`](../cli-reference/interface/dot1x/server/), [`/interface/dot1x/server/active`](../cli-reference/interface/dot1x/server/active), [`/interface/dot1x/server/state`](../cli-reference/interface/dot1x/server/state), [`/interface/dot1x/client`](../cli-reference/interface/dot1x/client)
- [RADIUS](radius)
- [User Manager](user-manager)
- [Certificates](certificates)
- [Switch chip features](../bridging-and-switching/switch-chip-features)
