# L2TP

> L2TP in RouterOS: set up an L2TP server and client, protect the tunnel with IPsec, open the firewall for it, carry large packets and bridge Ethernet over the PPP link, use L2TPv3, and connect two sites at layer 2...

# L2TP

The Layer Two Tunneling Protocol (L2TP, [RFC 2661](https://tools.ietf.org/html/rfc2661)) carries a PPP link over an IP network. RouterOS uses it in two ways:

- An L2TP server gives remote users and remote routers a PPP connection into the network. The users and their settings are in the PPP user database or on a RADIUS server: see [PPP AAA](../../authentication-authorization-accounting/ppp-aaa).
- L2TP Ether connects two sites at layer 2: it carries Ethernet frames with L2TPv3 ([RFC 3931](https://tools.ietf.org/html/rfc3931)).

L2TP runs over IPv4 and IPv6. It uses UDP port 1701 for both the control and the data packets, so it passes most firewalls and NAT.

:::warning
L2TP does not encrypt the traffic. Use it with IPsec when the tunnel crosses a network that you do not trust.
:::

![An L2TP client connects to an L2TP server over the internet](./img/l2tp-01.webp)

## Set up a server and a client

On the server, add a pool, a profile and a user, and enable the L2TP server. The router gets the address 10.0.0.1 inside the tunnels:

```ros
/ip/pool/add name=vpn-pool ranges=10.0.0.10-10.0.0.100
/ppp/profile/add name=vpn local-address=10.0.0.1 \
    remote-address=vpn-pool
/ppp/secret/add name=alice password=Example-pass-1 profile=vpn \
    service=l2tp
/interface/l2tp-server/server/set enabled=yes default-profile=vpn
```

On the client, a RouterOS router in this example, add an L2TP client with the address of the server:

```ros
/interface/l2tp-client/add name=l2tp-office connect-to=203.0.113.1 \
    user=alice password=Example-pass-1 disabled=no
```

The client shows the state and the addresses of the link:

```ros
[admin@Client] > /interface/l2tp-client/monitor l2tp-office once
               status: connected           
               uptime: 10s                 
             encoding:                     
                  mtu: 1450                
                  mru: 1450                
        local-address: 10.0.0.100          
       remote-address: 10.0.0.1            
   local-ipv6-address: fe80::978e:f47e:0:5 
  remote-ipv6-address: fe80::2562:b1b9:f0:0
```

The server adds a dynamic interface for the user and lists the user in `/ppp/active`:

```ros
[admin@Server] > /interface/l2tp-server/print detail
Flags: D - DYNAMIC; R - RUNNING
0 DR name="<l2tp-alice>" user="alice" mtu=1450 mru=1450
     client-address="203.0.113.2" uptime=10s encoding=""
```

- An empty `encoding` means that the link is not encrypted.
- To send the traffic for the office network through the tunnel, add a route on the client with the client interface as the gateway, or set `add-default-route=yes` to send all traffic through it.
- The client and the server both use UDP port 1701. With `random-source-port=yes` the client uses a random source port.

## Protect the tunnel with IPsec

With `use-ipsec`, the server and the client add the IPsec configuration for the tunnel themselves. Both sides need the same `ipsec-secret`:

```ros
/interface/l2tp-server/server/set use-ipsec=required \
    ipsec-secret=Example-ipsec-secret-1
```

```ros
/interface/l2tp-client/set l2tp-office use-ipsec=yes \
    ipsec-secret=Example-ipsec-secret-1
```

- `use-ipsec=yes` on the server accepts clients with and without IPsec. `use-ipsec=required` refuses a client without IPsec, and the log of the server has `L2TP connection rejected no IPsec encryption while it was required`.
- The server adds a dynamic IPsec peer `l2tp-in-server` and, for each client, a dynamic policy for UDP port 1701 in transport mode. The client adds a dynamic peer and policy with the name of its interface.
- Several clients behind the same NAT address cannot use L2TP with IPsec at the same time in this mode.
- Microsoft Windows uses L2TP with IPsec by default.
- Take care if the router also has static IPsec peers: the dynamic peer of the L2TP server listens for all addresses.

When IPsec protects the link, `encoding` shows the algorithms:

```ros
[admin@Server] > /interface/l2tp-server/print detail
Flags: D - DYNAMIC; R - RUNNING
0 DR name="<l2tp-alice>" user="alice" mtu=1450 mru=1450
     client-address="203.0.113.2" uptime=25s encoding="cbc(aes) + hmac(sha1)"
```

## Allow L2TP in the firewall

The default firewall drops connections that come from the internet. For L2TP with IPsec, accept IKE, IPsec ESP, and UDP port 1701 only when IPsec protects it. Put the rules before the default drop rule:

```ros
/ip/firewall/filter
add chain=input action=accept protocol=udp dst-port=500,4500 \
    in-interface-list=WAN comment="accept IKE" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=accept protocol=ipsec-esp \
    in-interface-list=WAN comment="accept IPsec ESP" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=accept protocol=udp dst-port=1701 \
    ipsec-policy=in,ipsec in-interface-list=WAN \
    comment="accept L2TP over IPsec" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

All three rules are needed: the client connects only when the last one is in place. UDP port 4500 is used when there is NAT between the client and the server.

For L2TP without IPsec, one rule accepts UDP port 1701, without `ipsec-policy`.

A connected user can reach the devices of the LAN, but not the services of the router. [PPP AAA](../../authentication-authorization-accounting/ppp-aaa) shows how to limit what the users reach.

## Connect a branch office

An L2TP client on a branch router connects the branch network to the office. The tunnel is a routed link, so each side needs a route to the network of the other side. In this example the office LAN is 192.168.88.0/24 and the branch LAN is 192.168.2.0/24.

On the office router, give the branch a fixed address and a route to its LAN in the user entry. The router adds the route when the branch connects:

```ros
/ppp/secret/add name=branch1 password=Example-pass-2 profile=vpn \
    service=l2tp remote-address=10.0.0.5 \
    routes="192.168.2.0/24 10.0.0.5 1"
```

On the branch router, add the client and a route to the office LAN through it:

```ros
/interface/l2tp-client/add name=l2tp-office connect-to=203.0.113.1 \
    user=branch1 password=Example-pass-2 use-ipsec=yes \
    ipsec-secret=Example-ipsec-secret-1 disabled=no
/ip/route/add dst-address=192.168.88.0/24 gateway=l2tp-office
```

- The two LANs must use different networks.
- For a tunnel between two routers with static addresses, [IPsec](../ipsec/site-to-site) or [WireGuard](../wireguard) needs no PPP users.

## Send large packets and bridge Ethernet

The MTU of an L2TP link is 1450 bytes by default, so a 1500-byte packet that must not be fragmented does not pass. Multilink PPP splits such packets and joins them on the other side. Set `mrru` on the server and on the client:

```ros
/interface/l2tp-server/server/set mrru=1600
```

```ros
/interface/l2tp-client/set l2tp-office mrru=1600
```

A PPP link can also carry Ethernet frames, with the Bridge Control Protocol (BCP). Name a bridge in the PPP profile on both sides, and the router adds the link to the bridge as a dynamic port when the user connects:

```ros
/ppp/profile/set vpn bridge=bridge
```

- Set `mrru` as well, so that full-size Ethernet frames pass.
- A PPP link has no MAC address. The bridge needs an Ethernet-like port or a MAC address that you set (`admin-mac`).
- To connect two sites at layer 2 only, L2TP Ether is simpler.

## Use L2TPv3

The client uses L2TP version 2 by default. `l2tp-proto-version` selects version 3 over UDP (`l2tpv3-udp`) or directly over IP (`l2tpv3-ip`, IP protocol 115). Version 3 needs a circuit ID on the client:

```ros
/interface/l2tp-client/set l2tp-office \
    l2tp-proto-version=l2tpv3-udp l2tpv3-circuit-id=office
```

The server accepts both versions by default. `accept-proto-version` of the server limits it to one, and `accept-pseudowire-type` limits it to PPP sessions (`ppp`) or to Ethernet sessions (`ether`).

## Connect two sites at layer 2 with L2TP Ether

An L2TP Ether tunnel carries Ethernet frames between two routers. One router connects to the other:

- The active side has an `/interface/l2tp-ether` entry with the address of the other router in `connect-to`.
- The passive side has the L2TP server enabled.

On the passive side, enable the server and add an interface for the tunnel. `connect-to=0.0.0.0` makes it wait for the connection, and `circuit-id` names the tunnel:

```ros
/interface/l2tp-server/server/set enabled=yes
/interface/l2tp-ether/add name=l2tp-site1 connect-to=0.0.0.0 \
    circuit-id=site1
```

On the active side, use the same circuit ID:

```ros
/interface/l2tp-ether/add name=l2tp-ether1 connect-to=203.0.113.1 \
    circuit-id=site1
```

Add the interface to the LAN bridge on each side (`l2tp-ether1` on the active side), and the two networks are one layer 2 network. Both sides then share one network: use one DHCP server and different addresses for the two routers.

```ros
/interface/bridge/port/add bridge=bridge interface=l2tp-site1
```

`monitor` shows the state of the tunnel:

```ros
[admin@Client] > /interface/l2tp-ether/monitor l2tp-ether1 once
           status: link up    
       circuit-id: site1      
    cookie-length: 0          
    header-format: L2TPv3 UDP 
      l2-sublayer: no         
   remote-sess-id: 33         
    local-sess-id: 125        
  control-conn-id: 104        
     peer-address: 203.0.113.1
           uptime: 17s        
```

- The MTU of the interface is 1450 bytes. Check that the bridge and the devices behind it can work with this MTU.
- `l2tp-proto-version=l2tpv3-ip` on the active side carries the tunnel directly over IP and not over UDP.
- `use-ipsec` and `ipsec-secret` protect the tunnel in the same way as for an L2TP client, and the firewall rules for L2TP with IPsec apply. On the passive side, these settings and the cookie and digest settings are in `/interface/l2tp-server/server`, not in the interface.
- A static tunnel without a control connection is also possible: `unmanaged-mode` with the tunnel IDs, session IDs and cookies set by hand. See the [CLI reference](../../cli-reference/interface/l2tp-ether/).

### Dynamic interfaces on the passive side

When the active side has no circuit ID, the passive side does not need an interface: the server adds a dynamic one for each tunnel.

```ros
[admin@Server] > /interface/l2tp-ether/print detail
Flags: D - DYNAMIC; R - RUNNING
0 DR name="<l2eth-23>" mtu=auto actual-mtu=1450 connect-to=0.0.0.0
     mac-address=FE:36:0B:1B:B5:5E use-ipsec=no allow-fast-path=no
     l2tp-proto-version=l2tpv3-udp circuit-id="<l2eth-23>" cookie-length=0
     digest-hash=md5 use-l2-specific-sublayer=no
```

A dynamic interface gets a new name with each connection. To use it in a bridge, set `l2tpv3-ether-interface-list` of the server: the server adds each dynamic interface to this interface list, and a bridge port can be an interface list.

```ros
/interface/list/add name=l2tp-ether-ports
/interface/l2tp-server/server/set \
    l2tpv3-ether-interface-list=l2tp-ether-ports
/interface/bridge/port/add bridge=bridge interface=l2tp-ether-ports
```

### Troubleshoot L2TP Ether

Log the `l2tp` topic on the passive side to see why a tunnel does not come up:

```ros
/system/logging/add topics=l2tp,debug action=memory
```

| What you see | What to check |
| :-- | :-- |
| The active side shows `status: link down`. The log of the passive side has `has reached maximum session count, disconnecting`, and the server answers with CDN and `Result-Code=4`. | The server found no interface for the session. If the active side has a `circuit-id`, the passive side needs an `l2tp-ether` interface with `connect-to=0.0.0.0` and the same `circuit-id`. Also check `max-sessions` of the server. |
| The tunnel does not come up at all. | `accept-proto-version` of the server must allow `l2tpv3`, and `accept-pseudowire-type` must allow `ether`. In a firewall, accept UDP port 1701, or IP protocol 115 for `l2tpv3-ip`. |
| The tunnel does not come up after a change of `digest-hash`. | With `digest-hash=none` on one side and a hash on the other, the tunnel stays down. Use the same value on the active side and in `l2tpv3-digest-hash` of the server. |

## Read more

- [`/interface/l2tp-server/server`](../../cli-reference/interface/l2tp-server/server), [`/interface/l2tp-server`](../../cli-reference/interface/l2tp-server/), [`/interface/l2tp-client`](../../cli-reference/interface/l2tp-client/), [`/interface/l2tp-ether`](../../cli-reference/interface/l2tp-ether/)
- [PPP AAA](../../authentication-authorization-accounting/ppp-aaa)
- [IPsec](../ipsec/)
- [LAC and LNS setup with Cisco as LAC](lac-and-lns-setup-with-cisco-as-lac)
