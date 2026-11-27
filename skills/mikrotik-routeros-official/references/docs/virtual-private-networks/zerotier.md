# ZeroTier

> ZeroTier is a network virtualization engine for MikroTik RouterOS that enables secure, cross-network device connectivity via Ethernet virtualization and cryptographic peer-to-peer networks. It supports gaming, LAN...

# ZeroTier

The [ZeroTier](https://docs.zerotier.com/) network hypervisor is a self-contained network virtualization engine that implements an Ethernet virtualization layer similar to VXLAN built atop a cryptographically secure global peer-to-peer network. It provides advanced network virtualization and management capabilities on par with an enterprise SDN switch, but across both local and wide area networks and connecting almost any kind of app or device.

MikroTik has added ZeroTier to RouterOS v7.1rc2 as a separate package for the **ARM/ARM64** architecture.

## Use cases

- Hosting a game server at home (suited for LAN-only games) or creating a LAN party with friends.
- Accessing LAN devices behind NAT directly.
- Accessing LAN devices with SSH without opening a port to the Internet.
- Using your local Pi-Hole setup from anywhere over the Internet.

:::info
ZeroTier functionality can be blocked by `device-mode`. Before configuring ZeroTier, make sure it is enabled in `system/device-mode`. ([more info](../system-information-and-utilities/device-mode.md))
:::

## Video tutorial

- [ZeroTier](https://youtu.be/60uIlyF8Z5s)

## Required Network Configuration

### What ports does ZeroTier use?

It listens on 3 UDP ports:

- 9993 - The default
- A random, high-numbered port derived from your ZeroTier address
- A random, high-numbered port for use with UPnP/NAT-PMP mappings

That means your *peers* could be listening on any port. To talk with them directly, you need to be able to send to them on any port.

### Recommended Local Network and Internet Gateway Configuration

These ZeroTier recommended guidelines are consistent with the vast majority of typical deployments with commodity gateways and access points:

- Don't restrict outbound UDP traffic.
- Supporting either UPnP or NAT-PMP on your network can greatly improve performance by allowing ZeroTier endpoints to map external ports and avoid NAT traversal entirely.
- IPv6 is recommended and can greatly improve direct connection reliability if supported on both ends of a direct link. If present, implement it without NAT (NAT is unnecessary with IPv6 and adds complexity) and with a stateful firewall that permits bidirectional UDP conversations.
- Do not use "symmetric" NAT. Use "full cone" or "port restricted cone" NAT. Symmetric NAT is extremely hostile to peer-to-peer traffic and degrades VoIP, video chat, games, WebRTC, and many other protocols as well as ZeroTier.
- No more than one layer of NAT should be present between ZeroTier endpoints and the Internet. Multiple layers introduce connection instability from chaotic interactions between states and behaviors at different levels. Do not use double NAT.
- NAT devices should have a port mapping or connection timeout no shorter than 60 seconds.
- Place no more than 16,000 devices behind each NAT-managed external IP address to ensure each device can map a sufficient number of ports.
- Switches and wireless access points should allow direct local traffic between local devices. Turn off any "local isolation" features. If switches allow finer-grained control, allow local UDP traffic to/from port 9993.

## Configuration example

![A RouterOS router and a mobile phone connect over the internet with UDP hole punching; both reach the ZeroTier planet servers](./img/zerotier-01.webp)

ZeroTier is designed to be zero-configuration — you can start a new node without writing configuration files or providing the IP addresses of other nodes. Any two devices in the world can locate each other and communicate almost instantly. The following example enables ZeroTier on a RouterOS device and connects one mobile phone with the ZeroTier application.

1. Register on [my.zerotier.com](https://my.zerotier.com/) and **Create A Network**, obtain the *Network ID*, in this example: *1d71939404912b40*.  
   ![ZeroTier Central network list with the Create A Network button and the network ID 1d71939404912b40](./img/zerotier-02.webp)
2. [Download](https://mikrotik.com/download) and install the ZeroTier NPK package. You can find it under "Extra packages". Upload the package to the device and reboot.
3. Enable the default (official) ZeroTier instance:

   ```ros
   [admin@MikroTik] > /zerotier/enable zt1
   ```

4. Add a new network, specifying the network ID you created in the ZeroTier cloud console:

   ```ros
   [admin@mikrotik] /zerotier/interface/add network=1d71939404912b40 instance=zt1
   ```

5. Verify ZeroTier configuration:

   ```ros
   [admin@MikroTik] > /zerotier/interface/print
   Flags: R - RUNNING
   Columns: NAME, MAC-ADDRESS, NETWORK, NETWORK-NAME, STATUS
   #   NAME       MAC-ADDRESS        NETWORK           NETWORK-NAME     STATUS
   0 R zerotier1  42:AC:0D:0F:C6:F6  1d71939404912b40  modest_metcalfe  OK   
   ```

6. You may need to allow connections from the ZeroTier interface to your router, and optionally, to your other LAN interfaces:

   ```ros
   /ip/firewall/filter/add action=accept chain=forward in-interface=zerotier1 place-before=0
   /ip/firewall/filter/add action=accept chain=input in-interface=zerotier1 place-before=0
   ```

7. Install a ZeroTier client on your smartphone or computer. Follow the ZeroTier manual to connect to the same network.
8. If **"Access Control"** is set to **"Private"**, you must authorize nodes before they become members:  
   ![ZeroTier Central member list with the Auth? check boxes of two members marked](./img/zerotier-03.webp)

9. ```ros
   [admin@MikroTik] > `/ip/address/print` where interface~"zero"
   Flags: D - DYNAMIC
   Columns: ADDRESS, NETWORK, INTERFACE
   #   ADDRESS             NETWORK        INTERFACE
   3 D 192.168.192.105/24  192.168.192.0  zerotier1

   [admin@MikroTik] > ping 192.168.192.252 count=3
   SEQ HOST                                     SIZE TTL TIME       STATUS                                                                                                                                           
   0 192.168.192.252                            56  64 407us     
   1 192.168.192.252                            56  64 452us     
   2 192.168.192.252                            56  64 451us     
   sent=3 received=3 packet-loss=0% min-rtt=407us avg-rtt=436us max-rtt=452us 
   ```

:::tip
You should specify routes to specific internal subnets in the [ZeroTier cloud console](https://my.zerotier.com/) to ensure you can access those networks when connecting from other devices.
:::

## Self-hosted controller

A RouterOS router can host a ZeroTier network itself: the controller of the `zerotier` package admits the members and gives them their addresses and routes, without ZeroTier Central. The members still reach the controller through ZeroTier's root servers, so they need internet access. For a configuration example, see [Self-hosted ZeroTier controller on a hAP ax³](zerotier-controller).
