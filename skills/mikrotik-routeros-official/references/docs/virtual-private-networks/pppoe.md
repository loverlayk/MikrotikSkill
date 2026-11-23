# PPPoE

> PPPoE in RouterOS: connect a router to an internet provider with a PPPoE client, run a PPPoE server (access concentrator) for subscribers, choose service names, handle the 1492-byte MTU, and how the PPPoE discovery...

# PPPoE

Point-to-Point Protocol over Ethernet (PPPoE, [RFC 2516](https://tools.ietf.org/html/rfc2516)) carries PPP links over an Ethernet network. Internet providers use it to give each subscriber a connection with a user name and a password, in place of a static address or DHCP. RouterOS has both sides:

- The PPPoE client connects a router to any PPPoE server, for example to an internet provider.
- The PPPoE server, also called the access concentrator, serves many PPPoE clients. Clients exist for almost all operating systems and routers.

Both work on any layer 2 interface: Ethernet, wireless, VLAN, EoIP and others. The users of a PPPoE server and their settings are in the PPP user database or on a RADIUS server: see [PPP AAA](../../authentication-authorization-accounting/ppp-aaa).

![A PPPoE client connects to a PPPoE server over an Ethernet network](./img/pppoe-network-topology.jpg)

## Connect to an internet provider

Add a PPPoE client on the interface that is connected to the provider, with the user name and the password that the provider gave you:

```ros
/interface/pppoe-client/add name=pppoe-out1 interface=ether1 \
    user=alice password=Example-pass-1 add-default-route=yes \
    use-peer-dns=yes disabled=no
```

- `add-default-route=yes` adds a default route through the connection.
- `use-peer-dns=yes` uses the DNS servers that the provider sends.
- With the default configuration, the firewall and NAT use the interface list `WAN`. Add the PPPoE client interface to this list: `/interface/list/member/add list=WAN interface=pppoe-out1`.

`monitor` shows the state of the connection, the server and the addresses:

```ros
[admin@Client] > /interface/pppoe-client/monitor pppoe-out1 once
               status: connected            
               uptime: 12s                  
         active-links: 1                    
             encoding:                      
         service-name: internet             
              ac-name: Server               
               ac-mac: 52:54:0B:80:03:01    
                  mtu: 1492                 
                  mru: 1492                 
        local-address: 10.0.0.94            
       remote-address: 10.0.0.1             
   local-ipv6-address: fe80::7fe3:8e52:0:b  
  remote-ipv6-address: fe80::13af:5abb:f0:ae
```

`scan` lists the PPPoE servers that answer on an interface, with their service names:

```ros
[admin@Client] > /interface/pppoe-client/scan ether1 duration=5
Columns: SERVICE, MAC-ADDRESS, AC-NAME
SERVICE   MAC-ADDRESS        AC-NAME
          52:54:0B:80:03:01  Server 
internet  52:54:0B:80:03:01  Server 
```

- With an empty `service-name`, the client connects to any service. With a name, it connects only to a server that has this service.
- `ac-name` limits the client to the access concentrator with this name.
- Do not use a large number of PPPoE clients on one device.

## Run a PPPoE server

Add a pool, a profile and a user, and then a server on the interface where the clients are:

```ros
/ip/pool/add name=pppoe-pool ranges=10.0.0.10-10.0.0.100
/ppp/profile/add name=subscribers local-address=10.0.0.1 \
    remote-address=pppoe-pool
/ppp/secret/add name=alice password=Example-pass-1 \
    profile=subscribers service=pppoe
/interface/pppoe-server/server/add service-name=internet \
    interface=ether3 default-profile=subscribers disabled=no
```

For each connected user the server adds a dynamic interface, and `/ppp/active` lists the user with the MAC address of the client:

```ros
[admin@Server] > /interface/pppoe-server/print detail
Flags: D - DYNAMIC; R - RUNNING
0 DR name="<pppoe-alice>" user="alice" service="internet" mtu=1492 mru=1492
     remote-address="52:54:0B:81:03:01" encoding="" uptime=13s interface=ether3
```

- An interface can have several servers with different service names. The clients select the server by the service name and by the name of the access concentrator.
- The name of the access concentrator is the [identity](../../system-information-and-utilities/identity) of the router.
- Do not use static addresses or DHCP for the clients on an interface that has a PPPoE server, and do not give that interface an IP address: a device could then use the network without a PPPoE login.
- The server checks that a client is still there with echo requests. With `keepalive-timeout=10` (the default) it closes a session that does not answer. With 0, a session stays until the client logs out or the router restarts; `one-session-per-host=yes` helps in that case.
- Some instructions for Windows give the "phone number" as `MikroTik_AC\mt1`: the name of the access concentrator and then the service name.

## Send full-size packets

An Ethernet frame carries 1500 bytes. PPPoE uses 6 of them and PPP 2, so a PPPoE link has an MTU of 1492 bytes: a 1492-byte packet passes, and a 1500-byte packet that must not be fragmented does not.

TCP connections normally find the lower MTU with path MTU discovery, but this fails where routers or firewalls drop the ICMP messages that it needs. There are two ways to help:

- Lower the MSS of the TCP connections that pass the PPPoE link: see [Change MSS](../../firewall-and-quality-of-service/firewall/mangle). The built-in PPP profiles do this with `change-tcp-mss=yes`.
- Use Multilink PPP on the link. With `mrru` on the server and on the client, large packets are split and joined again, and 1500-byte packets pass: see [MLPPP over single and multiple links](mlppp-over-single-and-multiple-links).

## Serve VLANs with one server

`pppoe-over-vlan-range` makes one server accept clients in a range of VLANs on its interface. `accept-untagged=no` then refuses clients without a VLAN tag.

Do not use this setting together with a VLAN interface whose VLAN ID is in the range:

```ros
/interface/vlan
add interface=ether2 name=vlan15 vlan-id=15
/interface/pppoe-server/server
add disabled=no interface=ether2 pppoe-over-vlan-range=10-20
```

If you need both, take the VLAN ID out of the range and add a second server on the VLAN interface:

```ros
/interface/vlan
add interface=ether2 name=vlan15 vlan-id=15
/interface/pppoe-server/server
add disabled=no interface=ether2 pppoe-over-vlan-range=10-14,16-20
add disabled=no interface=vlan15
```

## How PPPoE works

PPPoE has two phases: discovery and session.

### Discovery

In the discovery phase the client finds a server. After four packets, both sides know the session ID and the MAC address of the other side, which together identify the session:

1. **PADI (Active Discovery Initiation).** The client sends a PADI packet to the broadcast address. The packet has the service name, if one is set on the client.
2. **PADO (Active Discovery Offer).** A server that has the requested service answers with a PADO packet to the address of the client. If the PADI has no service name, the PADO lists the services of the server.
3. **PADR (Active Discovery Request).** The client answers the first valid PADO with a PADR packet to the address of the server. If the PADI had no service name, the PADR has the first service name of the PADO.
4. **PADS (Active Discovery Session-confirmation).** The server makes a session ID and sends it to the client in a PADS packet.

Either side can end the session at any time with a **PADT (Active Discovery Terminate)** packet.

### Session

In the session phase, PPP frames travel in Ethernet frames of the type 0x8864. PPP starts with these steps:

1. LCP negotiates the link.
2. The client authenticates (PAP, CHAP or MS-CHAP).
3. IPCP gives the client an IP address.

If a step fails, the LCP negotiation starts again.

## Troubleshoot

| What you see | What to check |
| :-- | :-- |
| The client stays `disconnected`. | Run `scan` on the interface. If no server is listed, check the cable, the interface and the VLAN. If a server is listed, compare `service-name` and `ac-name` of the client with the list. |
| Web pages open slowly or not at all, while ping works. | The MTU: see "Send full-size packets" on this page. |

## Read more

- [`/interface/pppoe-client`](../../cli-reference/interface/pppoe-client/), [`/interface/pppoe-server/server`](../../cli-reference/interface/pppoe-server/server), [`/interface/pppoe-server`](../../cli-reference/interface/pppoe-server/)
- [PPP AAA](../../authentication-authorization-accounting/ppp-aaa)
- [IPv6 PD over PPP](ipv6-pd-over-ppp)
- [MLPPP over single and multiple links](mlppp-over-single-and-multiple-links)
