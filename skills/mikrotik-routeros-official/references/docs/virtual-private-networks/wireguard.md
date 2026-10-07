# WireGuard

> WireGuard is a modern VPN solution offering fast, secure encryption across platforms with detailed configuration options including private/public keys, VRF routing, and peer management for establishing encrypted...

WireGuard is a simple, fast, and modern VPN that uses state-of-the-art cryptography. It aims to be faster, simpler, and leaner than IPsec, and considerably more performant than OpenVPN. WireGuard is a general-purpose VPN designed for embedded interfaces and supercomputers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform (Windows, macOS, BSD, iOS, Android) and widely deployable.

## Importing and Exporting WireGuard

Configuration can be done in various ways. An example file is available for download: [wireguard1.conf](pathname:///assets/wireguard1.conf). Replace its example keys and endpoint before use.

### Importing a WireGuard configuration

[`/interface/wireguard/wg-import`](../cli-reference/interface/wireguard/wg-import) accepts configurations in the standard WireGuard format (`[Interface]` / `[Peer]` sections). A minimal working file:

```ini
[Interface]  
Address =192.168.88.3/24  
ListenPort = 13533  
PrivateKey = UBLqJEFZZf9wszZSUF2BPWa9dsMX99RbEcxlNfxWffk=
```

Save the file to the device (for example, via the WebFig/WinBox Files menu) and import it with:

```ros
/interface/wireguard/wg-import config-file=wireguard1.conf
```

The same configuration can be imported directly, without a file, using the `config-string` parameter:

```ros
/interface/wireguard/wg-import config-string="
[Interface]
Address = 192.168.88.3/24
ListenPort = 13533
PrivateKey = UBLqJEFZZf9wszZSUF2BPWa9dsMX99RbEcxlNfxWffk=

[Peer]
PublicKey = EoF7HlFu3fbOnuYbyGqLMJkPZgQk9n3WwONZuJZ6qWc=
Endpoint = 192.0.2.10:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25"
```

### Exporting client configurations

Client-side configurations (for phones, laptops and other peer devices) are generated per peer with [`/interface/wireguard/peers/show-client-config`](../cli-reference/interface/wireguard/peers/show-client-config) — either as text (`conf` output, or saved to a file with the `file` argument), or as a QR code (`qr` output) that a WireGuard client application can scan.

The generated configuration is built from the peer's `client-*` properties (see [`/interface/wireguard/peers`](../cli-reference/interface/wireguard/peers/)). If the peer's `client-address` is left empty, the default address `192.168.177.2/24` is used in the generated configuration.

:::note
The "**AllowedIPs**" value in the generated client configuration is `0.0.0.0/0, ::/0`. Since RouterOS 7.21 it can be adjusted with the peer's `client-allowed-address` property; on older versions the value is fixed and can only be changed in the remote peer software.
:::

### Exporting a WireGuard interface

[`/interface/wireguard/wg-export`](../cli-reference/interface/wireguard/wg-export) writes the selected interface and its peers in standard WireGuard configuration format:

```ros
/interface/wireguard/wg-export [find name=wireguard1] \
    file=wireguard1.conf
```

Import this file with `wg-import`. The export contains `[Interface]` and `[Peer]` sections, but does not include the interface's IP addresses or RouterOS routes and firewall rules. Configure those separately on the destination router.

For a RouterOS configuration script, use the regular `/interface/wireguard/export` command instead. Treat exports and generated client configurations containing private keys as secrets.

:::note
When you encounter issues with reply traffic having the wrong source address, translating packet source addresses to your loopback interface with NAT is a common workaround. This approach helps ensure the source address is consistent and correct when packets are routed back through the network.
:::

## Application examples

### Site to Site WireGuard tunnel

Consider the setup illustrated below. Two remote office routers are connected to the internet and office workstations are behind NAT. Each office has its own local subnet, 10.1.202.0/24 for Office1 and 10.1.101.0/24 for Office2. Both remote offices need secure tunnels to local networks behind routers.

![Two office LANs connected through a WireGuard tunnel between their routers](./img/wireguard-01.webp)

#### WireGuard interface configuration

First, configure WireGuard interfaces on both sites to allow automatic private and public key generation. The command is the same for both routers:

```ros
/interface/wireguard
add listen-port=13231 name=wireguard1
```

Read the public key on each router and exchange only the public keys.

:::warning
A private key is never needed on the remote side device — hence the name private.
:::

**Office1**

```ros
:put [/interface/wireguard/get [find name=wireguard1] public-key]
```

**Office2**

```ros
:put [/interface/wireguard/get [find name=wireguard1] public-key]
```

#### Peer configuration

Peer configuration defines who can use the WireGuard interface and what kind of traffic can be sent over it. To identify the remote peer, its public key must be specified together with the created WireGuard interface. Replace `<Office2-public-key>` on Office1 with the key read on Office2, and `<Office1-public-key>` on Office2 with the key read on Office1.

**Office1**

```ros
/interface/wireguard/peers
add allowed-address=10.1.101.0/24,10.255.255.2/32 \
    endpoint-address=192.168.80.1 endpoint-port=13231 \
    interface=wireguard1 \
    public-key="<Office2-public-key>"
```

**Office2**

```ros
/interface/wireguard/peers
add allowed-address=10.1.202.0/24,10.255.255.1/32 \
    endpoint-address=192.168.90.1 endpoint-port=13231 \
    interface=wireguard1 \
    public-key="<Office1-public-key>"
```

#### IP and routing configuration

Lastly, IP and routing information must be configured to allow traffic to be sent over the tunnel.

**Office1**

```ros
/ip/address
add address=10.255.255.1/30 interface=wireguard1
/ip/route
add dst-address=10.1.101.0/24 gateway=wireguard1
```

**Office2**

```ros
/ip/address
add address=10.255.255.2/30 interface=wireguard1
/ip/route
add dst-address=10.1.202.0/24 gateway=wireguard1
```

#### Firewall considerations

The default RouterOS firewall blocks the tunnel from establishing properly. The traffic must be accepted in the `input` chain before any drop rules on both sites. These commands insert rules before the first existing rule in the corresponding chain. If a chain is empty, omit `place-before`.

**Office1**

```ros
/ip/firewall/filter
add chain=input action=accept \
    dst-port=13231 protocol=udp src-address=192.168.80.1 \
    place-before=([find chain=input]->0)
```

**Office2**

```ros
/ip/firewall/filter
add chain=input action=accept \
    dst-port=13231 protocol=udp src-address=192.168.90.1 \
    place-before=([find chain=input]->0)
```

The "forward" chain can also restrict communication between the subnets, so such traffic should also be accepted before any drop rules.

**Office1**

```ros
/ip/firewall/filter
add chain=forward action=accept \
    dst-address=10.1.202.0/24 src-address=10.1.101.0/24 \
    place-before=([find chain=forward]->0)
add chain=forward action=accept \
    dst-address=10.1.101.0/24 src-address=10.1.202.0/24 \
    place-before=([find chain=forward]->0)
```

**Office2**

```ros
/ip/firewall/filter
add chain=forward action=accept \
    dst-address=10.1.101.0/24 src-address=10.1.202.0/24 \
    place-before=([find chain=forward]->0)
add chain=forward action=accept \
    dst-address=10.1.202.0/24 src-address=10.1.101.0/24 \
    place-before=([find chain=forward]->0)
```

## RoadWarrior WireGuard tunnel

### RouterOS configuration

Add a new WireGuard interface and assign an IP address to it.

```ros
/interface/wireguard
add listen-port=13231 name=wireguard1
/ip/address
add address=192.168.100.1/24 interface=wireguard1
```

Adding a new WireGuard interface automatically generates a pair of private and public keys. Configure the public key on your remote devices. To obtain the public key value, run:

```ros
:put [/interface/wireguard/get [find name=wireguard1] public-key]
```

For the next steps, obtain the public key of the remote device. Once you have it, add a new peer by specifying the public key of the remote device and allowed addresses that will be allowed over the WireGuard tunnel.

```ros
/interface/wireguard/peers
add allowed-address=192.168.100.2/32 interface=wireguard1 \
    public-key="<paste public key from remote device here>"
```

### Firewall considerations

If you have a default or strict firewall configured, you need to allow a remote device to establish the WireGuard connection to your device.

```ros
/ip/firewall/filter
add chain=input action=accept \
    comment="allow WireGuard" dst-port=13231 protocol=udp \
    place-before=([find chain=input]->0)
```

To allow remote devices to connect to the RouterOS services (e.g. request DNS), allow the WireGuard subnet in the input chain.

```ros
/ip/firewall/filter
add chain=input action=accept \
    comment="allow WireGuard traffic" in-interface=wireguard1 \
    src-address=192.168.100.0/24 \
    place-before=([find chain=input]->0)
```

Alternatively, add the WireGuard interface to the `LAN` interface list. This gives VPN peers the access granted to your LAN by rules that match this list; use separate firewall rules when VPN peers should have less access.

```ros
/interface/list/member
add interface=wireguard1 list=LAN
```

### iOS configuration

Download the WireGuard application from the App Store. Open it up and create a new configuration from scratch.

![WireGuard on iOS with the Create from scratch option selected](./img/wireguard-02.webp)

First, give your connection a `Name` and choose `Generate a keypair`. The generated `Public key` is necessary for the peer configuration on the RouterOS side.

![New iOS WireGuard configuration with keypair, address and DNS fields](./img/wireguard-03.webp)

Specify an IP address in the `Addresses` field that is in the same subnet as configured on the RouterOS side. This address is used for communication. For this example, the RouterOS side uses `192.168.100.1/24`. You can use `192.168.100.2/24` here.

If necessary, configure the `DNS servers`. If `allow-remote-requests` is set to `yes` under `/ip/dns` on the RouterOS side, you can specify the remote WireGuard IP address here.

![iOS WireGuard address 192.168.100.2 and DNS server 192.168.100.1](./img/wireguard-04.webp)

Select `Add peer` to reveal more parameters.

The `Public key` value is the public key value that is generated on the WireGuard interface on the RouterOS side.

`Endpoint` is the IP or DNS with a port number of the RouterOS device that the iOS device can communicate with over the Internet.

`Allowed IPs` are set to `0.0.0.0/0` to allow all traffic to be sent over the WireGuard tunnel.

![iOS peer settings with the router endpoint and Allowed IPs set to 0.0.0.0/0](./img/wireguard-05.webp)

If the RouterOS device is behind another NAT router, configure port forwarding on that upstream router to forward the WireGuard UDP port to the RouterOS device. If the upstream router is running RouterOS:

```ros
/ip/firewall/nat
add chain=dstnat action=dst-nat \
    protocol=udp dst-port=13231 in-interface=WAN \
    to-addresses=192.168.1.2 to-ports=13231
```

Replace `WAN`, `192.168.1.2` and `13231` with the appropriate upstream interface name, the RouterOS device's IP address on the upstream network, and the WireGuard listen port.

### Windows configuration

Download the WireGuard installer from [WireGuard](https://www.wireguard.com/install/) and run it as Administrator.

Press <kbd>Control</kbd>+<kbd>N</kbd> to add a new empty tunnel. Add a name for the interface — the public key should be auto-generated. Copy it to the RouterOS peer configuration.  
Add it to the server configuration. The full configuration should look like this (keep your auto-generated `PrivateKey` in the `[Interface]` section):

```ini
[Interface]
PrivateKey = your_autogenerated_private_key=
Address = 192.168.100.2/24
DNS = 192.168.100.1

[Peer]
PublicKey = your_MikroTik_public_KEY=
AllowedIPs = 0.0.0.0/0
Endpoint = example.com:13231
```

Save the configuration and select `Activate`.

## The vrf parameter in the WireGuard context

The `vrf` parameter does **not** apply to the WireGuard interface itself (e.g., `wg0`, `wg1`), but rather to the **UDP socket** used for transporting encrypted packets.

There are two distinct layers in WireGuard operation:

1. **WireGuard interface** — a virtual network device that handles plain (unencrypted) IP packets. Outgoing packets entering the interface are encrypted by WireGuard and sent through a UDP socket; incoming encrypted UDP packets are decrypted by WireGuard and delivered as plain IP packets through the interface.
2. **UDP socket** — handles encrypted WireGuard traffic, receiving encrypted packets from the network and sending encrypted packets to the network.

The `vrf` parameter is relevant to **the UDP socket layer** (case 2). It specifies **which routing table (VRF)** the socket should use to determine how encrypted packets are sent or received.  
This ensures that encrypted traffic follows the correct routing path and uses the proper source IP, preventing issues where packets might otherwise go out through the wrong interface or route.  

### Example

> Suppose interface `eth1` belongs to VRF `foo`.  
> If you want WireGuard to send and receive encrypted packets through `eth1`, configure WireGuard with `vrf=foo`.  
> It is normal for the WireGuard interface (`wg0`) itself to be in a different VRF than the one specified by the `vrf` parameter used by the internal UDP socket.

## Multi-WAN setup

For WireGuard there is no inherent server-client relationship. Both ends can serve as an endpoint and both ends stream UDP handshake messages to each other if they have endpoints defined in their configurations. You can enable the "responder" option in the peer settings to emulate server-client behavior, where the "server" peer only replies to handshake messages from "client" peers and does not stream handshake messages by itself.  
Because of this tunnel establishment behavior, handshake messages from different endpoints of the WireGuard tunnel are treated as two separate connections.  
You need to account for this in setups with multiple paths to the "client" peer, as this can cause the "server" to reply to the "client" through a different route instead of the incoming route.  
Below is a configuration example that addresses this behavior and ensures the "server" uses the incoming route to reply to the "client".

### Configuration example

This example does not include WireGuard interface configuration as it is applicable to both [RoadWarrior](./wireguard#roadwarrior-wireguard-tunnel) and [Site to Site](./wireguard#site-to-site-wireguard-tunnel) setups with two WAN connections such as [PCC](../high-availability-solutions/load-balancing/per-connection-classifier) setup.
The `wan2` and `wan3` routing tables must already exist, each with a route to the peer through its corresponding WAN. Replace the interface and table names to match your configuration. The output rules match the local WireGuard source port, because a remote peer can use a different port.

For these rules to work as intended, you need to enable the "responder" option in WireGuard peer settings, as the "server" could send handshakes via the incorrect interface because routing was not marked.

```ros
/ip/firewall/mangle
add chain=prerouting action=add-src-to-address-list \
    address-list=WAN2_WireGuard_clients address-list-timeout=1m \
    dst-port=13231 in-interface=ether2 protocol=udp \
    comment="Track WireGuard peers on WAN2"
add chain=output action=mark-connection \
    dst-address-list=WAN2_WireGuard_clients src-port=13231 \
    new-connection-mark=wan2 protocol=udp \
    comment="Mark WireGuard replies"
add chain=output action=mark-routing \
    connection-mark=wan2 src-port=13231 new-routing-mark=wan2 \
    protocol=udp \
    comment="Route WireGuard replies through WAN2"
add chain=prerouting action=add-src-to-address-list \
    address-list=WAN3_WireGuard_clients address-list-timeout=1m \
    dst-port=13231 in-interface=ether3 protocol=udp \
    comment="Track WireGuard peers on WAN3"
add chain=output action=mark-connection \
    dst-address-list=WAN3_WireGuard_clients src-port=13231 \
    new-connection-mark=wan3 protocol=udp \
    comment="Mark WireGuard replies"
add chain=output action=mark-routing \
    connection-mark=wan3 src-port=13231 new-routing-mark=wan3 \
    protocol=udp \
    comment="Route WireGuard replies through WAN3"
 
/ip/firewall/nat
add chain=srcnat action=masquerade \
    protocol=udp src-port=13231 out-interface=ether2 \
    comment="Use the WAN2 source address"
add chain=srcnat action=masquerade \
    protocol=udp src-port=13231 out-interface=ether3 \
    comment="Use the WAN3 source address"
```

The first mangle rule catches the source IP address by matching the destination port of the incoming WireGuard handshake and adds it to the list, which is later used to mark the outgoing WireGuard handshake. The timeout ensures that the same source IP address can later establish a WireGuard tunnel through a different WAN interface.  
The second mangle rule marks connections that are used for routing marks and ensures the mark stays on the connection after the IP address is gone from the address list and the tunnel is established.  
The third mangle rule forces the packet to use the correct routing table for the second WAN interface.  
The last NAT rule ensures the packet is sent out with the correct source IP, as it is not adjusted by the mangle rules. Without this rule, the packet could have a different source IP depending on the setup.
The rules are duplicated for WAN3 to ensure the WAN3 interface is also usable with WireGuard.  

This rule set ensures the WireGuard tunnel is established on the interface that received the incoming handshake.

## 2FA setup

[HotSpot](../authentication-authorization-accounting/hotspot-captive-portal/) services can be bound to WireGuard interfaces in RouterOS v7. This allows administrators to combine WireGuard's high-performance encryption with the HotSpot's captive portal features, supporting additional user-level authentication through a local database, User Manager, or RADIUS. The OTP feature strengthens security further.

### Configuration example

Make sure the WireGuard interface `wg1` is configured on your device.

Set up HotSpot on the WireGuard interface:

```ros
/ip/hotspot/setup
```

Select `wg1` when prompted for the HotSpot interface. To create the server without the interactive setup, configure a HotSpot profile and use:

```ros
/ip/hotspot/add interface=wg1
```

After HotSpot setup, once a WireGuard peer is connected, an additional login to the portal is required to proceed. Regular HotSpot username/password authorization can be used. For better security, configure `otp-secret` in `/ip/hotspot/user` or `/user-manager/user`. Generate a unique Base32 secret for each user and add it to the authenticator app. Replace the example secret before use:

```ros
/ip/hotspot/user/add name=peer1 \
    otp-secret=HVR4CFHAFOWFGGFAGSA5JVTIMMPG6GMT
```

You can find multiple open-source totp generator tools that can provide you with an appropriate key and necessary options to import it into your "authenticator" app.

After setup is complete, launch WireGuard on your device. Open the HotSpot login page through the tunnel and enter the HotSpot username and the six-digit time-based one-time password (TOTP) from the authenticator app. WireGuard authenticates the peer key; the HotSpot login authorizes user traffic separately.

You should use an HTTPS login page for HotSpot and make sure the WireGuard peer can verify the login page certificate.
