# ZeroTier

> ZeroTier is a network virtualization engine for MikroTik RouterOS that enables secure, cross-network device connectivity via Ethernet virtualization and cryptographic peer-to-peer networks. It supports gaming, LAN...

# ZeroTier

The [ZeroTier](https://docs.zerotier.com/) network hypervisor is a self-contained network virtualization engine that implements an Ethernet virtualization layer similar to VXLAN built atop a cryptographically secure global peer-to-peer network. It provides advanced network virtualization and management capabilities on par with an enterprise SDN switch, but across both local and wide area networks and connecting almost any kind of app or device.

MikroTik has added ZeroTier to RouterOS v7.1rc2 as a separate package for the **ARM/ARM64** architecture.

### Use cases

- Hosting a game server at home (suited for LAN-only games) or creating a LAN party with friends.
- Accessing LAN devices behind NAT directly.
- Accessing LAN devices with SSH without opening a port to the Internet.
- Using your local Pi-Hole setup from anywhere over the Internet.

:::info
ZeroTier functionality can be blocked by `device-mode`. Before configuring ZeroTier, make sure it is enabled in `system/device-mode`. ([more info](../system-information-and-utilities/device-mode.md))
:::

### Video tutorial

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

![](./img/zerotier-01.webp)

ZeroTier is designed to be zero-configuration — you can start a new node without writing configuration files or providing the IP addresses of other nodes. Any two devices in the world can locate each other and communicate almost instantly. The following example enables ZeroTier on a RouterOS device and connects one mobile phone with the ZeroTier application.

1. Register on [my.zerotier.com](https://my.zerotier.com/) and **Create A Network**, obtain the *Network ID*, in this example: *1d71939404912b40*.  
   ![](./img/zerotier-02.webp)
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
   ![](./img/zerotier-03.webp)

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

# Controller

RouterOS implements ZeroTier functionality in the role of a node where most of the network configuration must be done on the ZeroTier webpage dashboard. However, in situations where you would prefer to do all the configuration on your own device, RouterOS offers to host your own controller.

A common misunderstanding is to conflate network controllers with root servers (planet and moons). Root servers are connection facilitators that operate at the **[VL1 level](https://docs.zerotier.com/zerotier/manual/#2networkhypervisoroverviewaname2a)**. Network controllers are configuration managers and certificate authorities that belong to the **[VL2 level](https://docs.zerotier.com/zerotier/manual/#22vl2theethernetvirtualizationlayeraname2_2a).** Generally, root servers don’t join or control virtual networks and network controllers are not root servers, though it is possible to have a node do both.

Every ZeroTier instance has a self-hosting network controller that can be used to host virtual networks. A controller is responsible for admitting members to the network and issuing default configuration information including certificates. Controllers can in theory host up to 2^24 networks and serve many millions of devices, but you should spread large numbers of networks across many controllers for load balancing and fault tolerance.

Controller is configured in [`/zerotier/controller`](../cli-reference/zerotier/controller/controller.md) menu.

## Configuration example

This example uses the RouterOS built-in ZeroTier controller to send the new network hosts appropriate certificates, credentials, and configuration information. The controller operates from the "RouterOS Home" device and joins 3 units to the network: a mobile phone, a laptop, and a RouterOS Office device. You can join up to 100 devices in one network.

![](./img/zerotier-04.webp)

### RouterOS Home

First, enable the default instance which operates at the **VL1** level:

```ros
[admin@Home] /zerotier> print
Columns: NAME, PORT, IDENTITY.PUBLIC
# NAME  PORT  IDENTITY.PUBLIC
;;; ZeroTier Central controller - https://my.zerotier.com/
0 zt1   9993  879c0b5265:0:d5fd2d17805e011d9b93ce8779385e427c8f405e520eea9284809d8444de0335a817xxb21aa4ba153bfbc229ca34d94e08de96d925a4aaa19b252da546693a28
```

Now, create a new network through the controller section which operates at the **VL2** level. Each network has its own controller and each network ID is generated from the controller address and controller ID combination.

Use the ***private=yes*** option for a more secure network:

```ros
[admin@Home] /zerotier> controller/add name=ZT-private instance=zt1 ip-range=172.27.27.10-172.27.27.20 private=yes routes=172.27.27.0/24
[admin@Home] /zerotier> controller/print
Columns: INSTANCE, NAME, NETWORK, PRIVATE
# INSTANCE  NAME        NETWORK           PRIVATE
0 zt1       ZT-private  879c0b5265a99e4b  yes
```

Add the new network under the interface section:

```ros
[admin@Home] /zerotier> interface/add network=879c0b5265a99e4b name=myZeroTier instance=zt1 
[admin@Home] /zerotier> interface/print interval=1
Columns: NAME, MAC-ADDRESS, NETWORK, STATUS
# NAME        MAC-ADDRESS        NETWORK           STATUS
0 myZeroTier  4A:19:35:6E:00:6E  879c0b5265a99e4b  ACCESS_DENIED
```

Each new peer asks the controller to join the network. In this case, the status is *ACCESS\_DENIED* and the peer must be authorized, because the **private=yes** option was used.

After authorization, each member in the network receives information from the controller about new peers and approval to exchange packets with them:

```ros
[admin@Home] /zerotier> controller/member/print
Columns: NETWORK, ZT-ADDRESS
# NETWORK     ZT-ADDRESS
0  ZT-private  879a0b5265
[admin@Home] /zerotier> controller/member/set 0 authorized=yes
```

## Verify newly configured IP address and route

```ros
[admin@Home] /zerotier> `/ip/address/print` where interface~"Zero"
Flags: D - DYNAMIC
Columns: ADDRESS, NETWORK, INTERFACE
# ADDRESS          NETWORK      INTERFACE
4 D 172.27.27.15/24  172.27.27.0  myZeroTier

[admin@Home] /zerotier> `/ip/route/pr` where gateway~"Zero"
Flags: D - DYNAMIC; A - ACTIVE; c, y - COPY
Columns: DST-ADDRESS, GATEWAY, DISTANCE
    DST-ADDRESS     GATEWAY     DISTANCE
DAc 172.27.27.0/24  myZeroTier         0
```

### RouterOS Office

Configuration on the Office device. Enable the default instance and ask the controller to join the *879c0b5265a99e4b* network:

```ros
[admin@office] /zerotier> interface/add network=879c0b5265a99e4b instance=zt1 name=ZT-interface 
[admin@office] /zerotier> interface/print interval=1
Columns: NAME, MAC-ADDRESS, NETWORK, STATUS
# NAME          MAC-ADDRESS        NETWORK           STATUS
0 ZT-interface  4A:40:1C:38:97:BA  879c0b5265a99e4b  ACCESS_DENIED
```

As before, because the network is private, the new peer must be authorized on the "RouterOS Home" device. After that, verify the IP address and route received from the controller:

```ros
[admin@Home] /zerotier> controller/member/print
Flags: A - AUTHORIZED
Columns: NETWORK, ZT-ADDRESS, IP-ADDRESS, LAST-SEEN
# NETWORK     ZT-ADDRESS  IP-ADDRESS    LAST-SEEN
0 A  ZT-private  879a0b5265  172.27.27.15           
1 A  ZT-private  554a914c7f  172.27.27.17           
2 A  ZT-private  a83ac6032a  172.27.27.10           
3    ZT-private  deba5dc5b1  172.27.27.13  3s348ms  
[admin@Home] /zerotier> controller/member/set 3 authorized=yes
[admin@Home] /zerotier> controller/member/print               
Flags: A - AUTHORIZED
Columns: NETWORK, ZT-ADDRESS, IP-ADDRESS, LAST-SEEN
# NETWORK     ZT-ADDRESS  IP-ADDRESS    LAST-SEEN
0 A  ZT-private  879a0b5265  172.27.27.15           
1 A  ZT-private  554a914c7f  172.27.27.17           
2 A  ZT-private  a83ac6032a  172.27.27.10           
3 A  ZT-private  deba5dc5b1  172.27.27.13  4s55ms 
```

Verify the IP address and route obtained through ZeroTier:

```ros
[admin@office] /zerotier> `/ip/address/print` where interface~"ZT"
Flags: D - DYNAMIC
Columns: ADDRESS, NETWORK, INTERFACE
# ADDRESS          NETWORK      INTERFACE
0 D 172.27.27.13/24  172.27.27.0  ZT-interface

[admin@office] /zerotier> `/ip/route/print` where gateway~"ZT"
Flags: D - DYNAMIC; A - ACTIVE; c, y - COPY
Columns: DST-ADDRESS, GATEWAY, DISTANCE
    DST-ADDRESS     GATEWAY       DISTANCE
DAc 172.27.27.0/24  ZT-interface         0
```

### Other devices

[Download the ZeroTier app](https://www.zerotier.com/download/) for your mobile phone or computer and join your newly created network:

1. From the laptop ZeroTier application, join the *879c0b5265a99e4b* network.
2. Use the ZeroTier mobile app to join the *879c0b5265a99e4b* network.

:::warning
All other new hosts must also be authorized in the `/zerotier/controller/member/` section.
:::

![](./img/zerotier-05.webp)

![](./img/zerotier-network-config.png)
