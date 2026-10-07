# PPPoE

> PPPoE enables IPv6 prefix delegation over PPP and MLPPP across Ethernet links, supporting both client-to-server and server-to-client configurations. It operates in discovery and session phases, with LCP/CHAP...

# PPPoE

This section covers PPPoE examples. Use it to configure IPv6 prefix delegation over PPP and MLPPP over one or more links.

Point-to-Point over Ethernet (PPPoE) is a method of encapsulating PPP packets into Ethernet frames. PPPoE is an extension of the standard Point to Point Protocol (PPP) and it is the successor of PPPoA. The PPPoE standard is defined in [RFC 2516](https://tools.ietf.org/html/rfc2516). The PPPoE client and server work over any Layer 2 Ethernet level interface on the router — for example, Wireless, Ethernet, EoIP, etc. PPPoE is used to hand out IP addresses to clients based on authentication by username (and also if required, by workstation) as opposed to workstation-only authentication where static IP addresses or DHCP are used. Do not use static IP addresses or DHCP on the same interfaces as PPPoE for security reasons.

## Introduction

PPPoE provides the ability to connect a network of hosts over a simple bridging access device to a remote Access Concentrator.

Supported connections:

- MikroTik RouterOS PPPoE client to any PPPoE server.
- MikroTik RouterOS server (access concentrator) to multiple PPPoE clients (clients are available for almost all operating systems and most routers).

## PPPoE Operation

PPPoE has two distinct stages (phases):

1. Discovery phase.
2. Session phase.

### Discovery phase

The Discovery stage has four steps. When it completes, both peers know the PPPoE *SESSION\_ID* and the peer's Ethernet address, which together define the PPPoE session uniquely:

1. **PPPoE Active Discovery Initialization (PADI) —** The PPPoE client sends out a *PADI* packet to the broadcast address. This packet can also populate the "service-name" field if a service name has been entered in the dial-up networking properties of the PPPoE client. If a service name has not been entered, this field is not populated.
2. **PPPoE Active Discovery Offer (PADO) —** The PPPoE server, or Access Concentrator, should respond to the *PADI* with a *PADO* if the Access Concentrator is able to service the "service-name" field that had been listed in the *PADI* packet. If no "service-name" field had been listed, the Access Concentrator responds with a *PADO* packet that has the "service-name" field populated with the service names that the Access Concentrator can service. The *PADO* packet is sent to the unicast address of the PPPoE client.
3. **PPPoE Active Discovery Request (PADR) —** When a *PADO* packet is received, the PPPoE client responds with a *PADR* packet. This packet is sent to the unicast address of the Access Concentrator. The client may receive multiple *PADO* packets, but the client responds to the first valid *PADO* that the client receives. If the initial *PADI* packet had a blank "service-name" field, the client populates the "service-name" field of the *PADR* packet with the first service name that had been returned in the *PADO* packet.
4. **PPPoE Active Discovery Session Confirmation (PADS) —** When the *PADR* is received, the Access Concentrator generates a unique session identification (ID) for the Point-to-Point Protocol (PPP) session and returns this ID to the PPPoE client in the *PADS* packet. This packet is sent to the unicast address of the client.

### PPPoE session termination

- **PPPoE Active Discovery Terminate (PADT) —** Can be sent at any time after a session is established to indicate that a PPPoE session has been terminated. It can be sent by either server or client.

### Session phase

When the discovery stage is completed, both peers know the *PPPoE Session ID* and the other peer's *Ethernet (MAC) address* which together define the PPPoE session. PPP frames are encapsulated in PPPoE session frames, which have Ethernet frame type **0x8864**.
When the server sends confirmation and the client receives it, the PPP session starts with the following stages:

1. **LCP negotiation** stage.
2. **Authentication (CHAP/PAP)** stage.
3. **IPCP negotiation** stage — where the client is assigned an IP address.

:::warning
If any process fails, the LCP negotiation establishment phase is started again.
:::

The PPPoE server sends *Echo-Request* packets to the client to determine the state of the session. Otherwise, the server cannot determine that the session is terminated if a client terminates the session without sending a *Terminate-Request* packet.

## MTU

Typically, the largest Ethernet frame that can be transmitted without fragmentation is 1500 bytes. PPPoE adds another 6 bytes of overhead and the PPP field adds two more bytes, leaving 1492 bytes for an IP datagram. Therefore, the maximum PPPoE MRU and MTU values must not be larger than 1492.

TCP stacks try to avoid fragmentation, so they use an MSS (Maximum Segment Size). By default, MSS is chosen as the MTU of the outgoing interface minus the usual size of the TCP and IP headers (40 bytes), which results in 1460 bytes for an Ethernet interface. Intermediate links with lower MTU can cause fragmentation. In such a case the TCP stack performs path MTU discovery. Routers that cannot forward the datagram without fragmentation are supposed to drop the packet and send *ICMP-Fragmentation-Required* to the originating host. When a host receives such an ICMP packet, it tries to lower the MTU. This should work in the ideal world; however, in the real world many routers do not generate fragmentation-required datagrams, and many firewalls drop all ICMP datagrams.

The workaround for this problem is to [adjust MSS](../../firewall-and-quality-of-service/firewall/mangle.md#change-mss) if it is too big.

## MRRU

Specifying MRRU means enabling MP (Multilink PPP) over a single link. This protocol is used to split big packets into smaller ones. The MRRU is hardcoded to 1614. This setting helps overcome PathMTU discovery failures. The MP setting should be enabled on both peers.  
On Windows, it can be enabled in the Networking tab, Settings button, "Negotiate multi-link for single link connections".

## Access concentrator

The PPPoE server (access concentrator) supports multiple servers for each interface — with differing service names. The access concentrator name and PPPoE service name are used by clients to identify the access concentrator to register with. The access concentrator name is the same as the identity of the router displayed before the command prompt. The identity is set within the *`/system/identity`* submenu.

Access concentrator is configured in [`/interface/pppoe-server/server`](../../cli-reference/interface/pppoe-server/server.md) menu.

:::tip
Do not assign an IP address to the interface you receive PPPoE requests on.
:::

:::warning
The default `keepalive-timeout` value of 10s is OK in most cases. If you set it to 0, the router does not disconnect clients until they explicitly log out or the router is restarted. To resolve this problem, the `one-session-per-host` property can be used.
:::

## Quick Example

![](./img/pppoe-network-topology.jpg)

### PPPoE Client

To configure MikroTik RouterOS to be a PPPoE client, add a PPPoE-client with the following parameters:

```ros
[admin@MikroTik] > interface pppoe-client add interface=ether2 password=StrongPass service-name=pppoeservice name=PPPoE-Out disabled=no user=MT-User
[admin@MikroTik] > interface pppoe-client print
Flags: X - disabled, I - invalid, R - running 
 0  R name="PPPoE-Out" max-mtu=auto max-mru=auto mrru=disabled interface=ether2 user="MT-User" 
      password="StrongPass" profile=default keepalive-timeout=10 service-name="pppoeservice" ac-name="" 
      add-default-route=no dial-on-demand=no use-peer-dns=no allow=pap,chap,mschap1,mschap2
```

### PPPoE Server

To configure MikroTik RouterOS to be an Access Concentrator (PPPoE Server):

- add an IP address pool for the clients from 10.0.0.2-10.0.0.5.
- add a PPP profile.
- add a PPP secret (username/password).
- add the PPPoE server itself.

:::warning
For Windows, some connection instructions may use the form where the "phone number", such as "MikroTik\_AC\mt1", is specified to indicate that "MikroTik\_AC" is the access concentrator name and "mt1" is the service name.
:::

```ros
[admin@MikroTik] > /ip/pool
add name=pppoe-pool ranges=10.0.0.2-10.0.0.5
[admin@MikroTik] > /ppp/profile
add local-address=10.0.0.1 name=for-pppoe remote-address=pppoe-pool
[admin@MikroTik] > /ppp/secret
add name=MT-User password=StrongPass profile=for-pppoe service=pppoe
[admin@MikroTik] > /interface/pppoe-server/server
add default-profile=for-pppoe disabled=no interface=ether3 service-name=pppoeservice
```

## PPPoE Over VLAN Range

Avoid configuring a server with `pppoe-over-vlan-range` on an interface while also creating a VLAN interface using a VLAN ID that falls within that range.  
For example:
```
/interface/vlan
add interface=ether2 name=vlan15 vlan-id=15
/interface/pppoe-server/server
add disabled=no interface=ether2 pppoe-over-vlan-range=10-20
```
If you need this type of setup, remove the overlapping VLAN ID from `pppoe-over-vlan-range` and create a separate PPPoE server instance directly on the VLAN interface, like this:
```
/interface/vlan
add interface=ether2 name=vlan15 vlan-id=15
/interface/pppoe-server/server
add disabled=no interface=ether2 pppoe-over-vlan-range=10-14,16-20
add disabled=no interface=vlan15
```

## Notes

Do not use a large number of PPPoE clients on one device.
