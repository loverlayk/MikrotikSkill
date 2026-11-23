# Site-to-site tunnel

> Site-to-site IPsec in RouterOS: connect the networks of two offices with an IKEv2 tunnel, keep NAT and FastTrack away from the tunnel traffic, open the firewall, and carry a GRE tunnel over IPsec when one office has...

# Site-to-site tunnel

A site-to-site tunnel connects the local networks of two offices over the internet. Each router encrypts the traffic for the other network and sends it to the other router. This page shows a tunnel between two routers with static public addresses, and a GRE tunnel over IPsec for an office without a static address.

![Two office routers connected through the internet, each with its own local network](./img/ipsec-04.webp)

In the examples, Office 1 has the public address 203.0.113.1 and the network 10.1.202.0/24. Office 2 has 203.0.113.2 and 10.1.101.0/24. The two offices must have different networks: if both use 192.168.88.0/24, change one of them first.

## Connect two offices

### Office 1

Add a phase 1 profile and a phase 2 proposal. The algorithms must be the same on both routers. Use separate entries for each tunnel, so that you can change one tunnel later without an effect on the others:

```ros
/ip/ipsec/profile/add name=office2 hash-algorithm=sha256 \
    enc-algorithm=aes-256 dh-group=ecp256
/ip/ipsec/proposal/add name=office2 auth-algorithms=sha256 \
    enc-algorithms=aes-256-cbc pfs-group=ecp256
```

Add the peer with the address of the other router, and an identity with the pre-shared key:

```ros
/ip/ipsec/peer/add name=office2 address=203.0.113.2/32 \
    exchange-mode=ike2 profile=office2
/ip/ipsec/identity/add peer=office2 secret=Example-psk-1
```

Add a policy for the traffic between the two networks:

```ros
/ip/ipsec/policy/add peer=office2 tunnel=yes \
    src-address=10.1.202.0/24 dst-address=10.1.101.0/24 \
    proposal=office2
```

### Office 2

The configuration is the same with the addresses changed:

```ros
/ip/ipsec/profile/add name=office1 hash-algorithm=sha256 \
    enc-algorithm=aes-256 dh-group=ecp256
/ip/ipsec/proposal/add name=office1 auth-algorithms=sha256 \
    enc-algorithms=aes-256-cbc pfs-group=ecp256
/ip/ipsec/peer/add name=office1 address=203.0.113.1/32 \
    exchange-mode=ike2 profile=office1
/ip/ipsec/identity/add peer=office1 secret=Example-psk-1
/ip/ipsec/policy/add peer=office1 tunnel=yes \
    src-address=10.1.101.0/24 dst-address=10.1.202.0/24 \
    proposal=office1
```

:::warning
A pre-shared key is only as strong as the key itself. Use a long random key. For better security, use certificates (`auth-method=digital-signature`).
:::

### Check the tunnel

The peer is `established`, and there is one security association (SA) for each direction:

```ros
[admin@Office1] > /ip/ipsec/active-peers/print
Columns: ID, STATE, UPTIME, PH2-TOTAL, REMOTE-ADDRESS
# ID           STATE        UPTIME  PH2-TOTAL  REMOTE-ADDRESS
0 203.0.113.2  established  15s             1  203.0.113.2   

[admin@Office1] > /ip/ipsec/installed-sa/print
Flags: S - SEEN-TRAFFIC; E - ESP
Columns: SPI, STATE, SRC-ADDRESS, DST-ADDRESS, AUTH-ALGORITHM, ENC-ALGORITHM, 
         ENC-KEY-SIZE
#    SPI         STATE   SRC-ADDRESS  DST-ADDRESS  AUTH-A  ENC-ALGORITHM  ENC
0 SE 0xAAD44FE4  mature  203.0.113.2  203.0.113.1  sha256  aes-cbc        256
1 SE 0x990D4C75  mature  203.0.113.1  203.0.113.2  sha256  aes-cbc        256
```

If the peer does not become `established`, the firewall of the router that answers can be the reason: see "Allow IPsec in the firewall" on this page. The flag `S` shows that the SA has carried traffic. To test from a router, ping an address of the other network from an address of the local network: `/ping 10.1.101.1 src-address=10.1.202.1`. A ping without `src-address` leaves from the public address and does not match the policy.

## Keep NAT away from the tunnel traffic

A source NAT rule changes the source address of the packets before IPsec sees them. They then no longer match the policy and are not encrypted: the tunnel is up, but no traffic passes.

The masquerade rule of the default configuration has `ipsec-policy=out,none`, so it leaves the traffic of IPsec policies alone and nothing more is needed. A masquerade rule without this matcher, for example `chain=srcnat action=masquerade out-interface=ether1`, needs a rule before it that accepts the traffic between the two networks. On the Office 1 router:

```ros
/ip/firewall/nat/add chain=srcnat action=accept place-before=0 \
    src-address=10.1.202.0/24 dst-address=10.1.101.0/24
```

On the Office 2 router:

```ros
/ip/firewall/nat/add chain=srcnat action=accept place-before=0 \
    src-address=10.1.101.0/24 dst-address=10.1.202.0/24
```

- The rule must be before all other source NAT rules.
- Connections that were tried before the rule was added keep their NAT. Remove them with `/ip/firewall/connection/remove [find dst-address~"10.1.101."]` (on Office 1), or restart both routers.

## Keep FastTrack away from the tunnel traffic

FastTracked packets do not pass the IPsec policies, so connections over the tunnel are slow or lose packets when FastTrack takes them.

The default configuration is safe: it has two rules that accept forwarded traffic of IPsec policies (`ipsec-policy=in,ipsec` and `ipsec-policy=out,ipsec`) before its FastTrack rule, so the connections of the tunnel are not FastTracked. A firewall that has a FastTrack rule without these two rules before it needs one of the following.

Accept the established connections of the tunnel before the FastTrack rule, on both routers:

```ros
/ip/firewall/filter
add chain=forward action=accept connection-state=established,related \
    src-address=10.1.101.0/24 dst-address=10.1.202.0/24 \
    place-before=[find action=fasttrack-connection]
add chain=forward action=accept connection-state=established,related \
    src-address=10.1.202.0/24 dst-address=10.1.101.0/24 \
    place-before=[find action=fasttrack-connection]
```

With many tunnels and much traffic, these rules add load to the CPU. The other way is to leave the tunnel traffic out of connection tracking. Then the filter rules are not needed, and the CPU load is about 30% lower:

```ros
/ip/firewall/raw
add chain=prerouting action=notrack \
    src-address=10.1.101.0/24 dst-address=10.1.202.0/24
add chain=prerouting action=notrack \
    src-address=10.1.202.0/24 dst-address=10.1.101.0/24
```

## Allow IPsec in the firewall

The default firewall drops connections that come from the internet. A router that starts the IKE connection gets the answers, but a router that waits for it does not get the first packet. Accept IKE (UDP port 500, and 4500 when there is NAT between the routers) and ESP from the other router, before the default drop rule, on both routers:

```ros
/ip/firewall/filter
add chain=input action=accept protocol=udp dst-port=500,4500 \
    src-address=203.0.113.2 comment="accept IKE" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=accept protocol=ipsec-esp \
    src-address=203.0.113.2 comment="accept IPsec ESP" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

The default configuration already accepts forwarded traffic that comes out of or goes into an IPsec tunnel (the rules with `ipsec-policy`).

## GRE tunnel over IPsec for an office without a static address

A GRE tunnel over IPsec gives each router an interface for the other office. You can then use routes, and the traffic of the tunnel needs no IPsec policy for each pair of networks. In this example only the server office needs an address that the other one can find: a static address, or a DNS name such as the one of [IP Cloud](../../network-management/cloud/).

![Two routers with a GRE tunnel between loopback addresses, protected by IPsec](./img/ipsec-05.webp)

The server gives the client the address 192.168.99.2 with mode config. The GRE tunnel runs between this address and the address 192.168.99.1 of the server, and IPsec protects exactly this pair of addresses.

:::tip
When both offices have static addresses, `ipsec-secret` of the GRE interface is a shorter way to protect a GRE tunnel with IPsec: see [GRE](../gre) and its [reference](../../cli-reference/interface/gre).
:::

### Server

Add a bridge without ports as a loopback interface, with the address for the GRE tunnel:

```ros
/interface/bridge/add name=loopback
/ip/address/add address=192.168.99.1 interface=loopback
```

Add the profile and the proposal. The peer of this example listens for all IKEv2 connections, so other IKEv2 setups on the router, for example road warriors, use the same profile:

```ros
/ip/ipsec/profile/add name=ike2 dh-group=ecp256,modp2048 \
    enc-algorithm=aes-256,aes-192,aes-128
/ip/ipsec/proposal/add name=ike2-gre auth-algorithms="" \
    enc-algorithms=aes-128-gcm pfs-group=none
```

An AES-GCM proposal needs `auth-algorithms=""`: the algorithm authenticates the packets itself.

Add a mode config that gives the client its address and the address of the server loopback, a policy group, and a policy template for this pair of addresses:

```ros
/ip/ipsec/mode-config/add name=ike2-gre address=192.168.99.2 \
    address-prefix-length=32 split-include=192.168.99.1/32 \
    system-dns=no
/ip/ipsec/policy/group/add name=ike2-gre
/ip/ipsec/policy/add template=yes group=ike2-gre \
    proposal=ike2-gre src-address=192.168.99.1/32 \
    dst-address=192.168.99.2/32
```

Add the peer that listens for IKEv2 connections (skip this if the router already has one) and the identity. The client has no fixed address, so the firewall rules for IKE and ESP on the server must not have `src-address`:

```ros
/ip/ipsec/peer/add name=ike2 exchange-mode=ike2 passive=yes \
    profile=ike2
/ip/ipsec/identity/add peer=ike2 secret=Example-psk-1 \
    generate-policy=port-strict mode-config=ike2-gre \
    policy-template-group=ike2-gre
```

Add the GRE interface, an address on it, and a route to the network of the other office:

```ros
/interface/gre/add name=gre-tunnel1 local-address=192.168.99.1 \
    remote-address=192.168.99.2
/ip/address/add address=172.16.1.1/30 interface=gre-tunnel1
/ip/route/add dst-address=10.1.101.0/24 gateway=172.16.1.2
```

### Client

The client connects to the server, so its profile can name the exact algorithms. They must be in the list of the server:

```ros
/ip/ipsec/profile/add name=ike2-gre dh-group=ecp256 \
    enc-algorithm=aes-256
/ip/ipsec/proposal/add name=ike2-gre auth-algorithms="" \
    enc-algorithms=aes-128-gcm pfs-group=none
```

Add a mode config that asks the server for the settings, a policy group and a template:

```ros
/ip/ipsec/mode-config/add name=ike2-gre responder=no
/ip/ipsec/policy/group/add name=ike2-gre
/ip/ipsec/policy/add template=yes group=ike2-gre \
    proposal=ike2-gre src-address=192.168.99.2/32 \
    dst-address=192.168.99.1/32
```

Add the peer with the DNS name or the address of the server, and the identity. With a DNS name, `address` is for example `address=example.sn.mynetname.net`:

```ros
/ip/ipsec/peer/add name=office1 address=203.0.113.1 \
    exchange-mode=ike2 profile=ike2-gre
/ip/ipsec/identity/add peer=office1 secret=Example-psk-1 \
    generate-policy=port-strict mode-config=ike2-gre \
    policy-template-group=ike2-gre
```

When the connection is made, the client has the address 192.168.99.2, and `/ip/ipsec/policy/print detail` shows a dynamic policy from 192.168.99.2/32 to 192.168.99.1/32 with `ph2-state=established`.

Add the GRE interface, an address and a route:

```ros
/interface/gre/add name=gre-tunnel1 local-address=192.168.99.2 \
    remote-address=192.168.99.1
/ip/address/add address=172.16.1.2/30 interface=gre-tunnel1
/ip/route/add dst-address=10.1.202.0/24 gateway=172.16.1.1
```

The two offices now reach each other through the GRE tunnel, and IPsec encrypts the GRE packets.

## Read more

- [IPsec](./): how IKE works, the menus, the algorithms
- [Route-based IPsec with XFRM](route-based-ipsec-xfrm)
- [Firewall and routing for IPsec](firewall-and-routing)
- [Troubleshooting](troubleshooting)
- [GRE](../gre)
