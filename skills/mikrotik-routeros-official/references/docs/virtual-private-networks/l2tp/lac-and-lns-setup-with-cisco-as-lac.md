# LAC and LNS setup with Cisco as LAC

> This page explains how to configure a MikroTik RouterOS device as an L2TP Network Server (LNS) to establish VPDN connections with a Cisco router acting as an LAC. It includes basic configuration examples for PPPoE...

# LAC and LNS setup with Cisco as LAC

LAC/LNS setup, otherwise known as Virtual Private DialUp Network (VPDN), allows long-distance point-to-point connection between remote dial-up users and private networks.

A Dial-up client uses PPPOE to connect to a L2TP access concentrator (LAC), LAC determines that the session should be forwarded through an IP network to the L2TP Network Server (LNS), creates L2TP tunnel and forwards PPP frames to the server where the client is authenticated and the session is established (see diagram below).

![](./img/lac-and-lns-setup-with-cisco-as-lac-01.svg)

At the time of writing this article RouterOS cannot be used in the LAC role. For this reason, the article will demonstrate how to set up a very basic network with RouterOS as an LNS and a Cisco router as a LAC.

## Configuration

We will be using a simple configuration to demonstrate the very basics of VPDN setup. Let's assume that LAC will forward to the LNS clients with FQDN name containing the [mt.lv](https://mt.lv) domain.

### Client

For the sake of simplicity let's assume that the client is a RouterOS router:

```ros
/interface/pppoe-client/add interface=ether1 user=good_worker@mt.lv password=strongpass
```

### LAC

Let's assume that the client is connected to the GigabitEthernet1 port and the IP address of the LNS server is 10.155.101.231

```text
aaa new-model
!
aaa authentication ppp default local
!
vpdn enable
vpdn aaa attribute nas-ip-address vpdn-nas
vpdn search-order domain dnis 
!
vpdn-group LAC
 request-dialin
  protocol l2tp
  domain mt.lv
 initiate-to ip 10.155.101.231
 source-ip 10.155.101.216
 local name LAC
 l2tp tunnel password 0 tunnelpass
!
bba-group pppoe MAIN-BBA
 virtual-template 1
!
interface GigabitEthernet1
 pppoe enable group MAIN-BBA
!
interface Virtual-Template1
 description pppoe MAIN-BBA
 no ip address
 no peer default ip address
 ppp mtu adaptive
 ppp authentication chap
!

```

Note that this setup does not authenticate the client either locally or via RADIUS, does not actually check the domain name, does not control L2 access for the sake of simplicity. If you want to use those features, refer to Cisco configuration manuals.

### LNS

On the LNS we need to enable L2TP server and set up a method to authenticate the L2TP connection from the LAC.

```ros
/interface/l2tp-server/server
set enabled=yes
/ppp/l2tp-secret
add address=10.155.101.216/32 secret=tunnelpass
```

Now the actual user authentication. In this case we will be using a local authentication method for the sake of simplicity.

```ros
/ip/pool
add name=pool0 ranges=192.168.99.2-192.168.99.99
/ppp/profile
set default local-address=192.168.99.1 remote-address=pool0
/ppp/secret
add name=good_worker@mt.lv password=strongpass
```

## Status Check

On the LNS you can see all successfully connected clients by checking l2tp server interfaces or checking active ppp connections:

```text
[admin@CHR_v6_bgp] /interface/l2tp-server> print
Flags: X - disabled, D - dynamic, R - running
# NAME USER MTU CLIENT-ADDRESS UPTIME ENCODING
0 DR <l2tp-... good_worker@mt.lv 1450 10.155.101.216 6h13m49s

[admin@CHR_v6_bgp] /ppp/active> print
Flags: R - radius
# NAME SERVICE CALLER-ID ADDRESS UPTIME ENCODING
0 good_worker@mt.lv l2tp 10.155.101.216 192.168.99.2 6h15m57s 

```

On the LAC we can also see active client sessions and an active L2TP tunnel between LAC and LNS:

```text
csrLAC#show vpdn

L2TP Tunnel and Session Information Total tunnels 1 sessions 1

LocTunID RemTunID Remote Name State Remote Address Sessn L2TP Class/
Count VPDN Group
26090 11 CHR_v6_bgp est 10.155.101.231 1 LAC

LocID RemID TunID Username, Intf/ State Last Chg Uniq ID
Vcid, Circuit
18521 16 26090 good_worker@mt.lv, Gi1 est 06:17:07 571

```

## Session Establishment

Let's look closely at how client sessions get authenticated and established over the LAC.

![](./img/lac-and-lns-setup-with-cisco-as-lac-02.svg)

- Client initiates PPPoE call.
- LAC and Client begin LCP negotiation.
- After CHAP has been negotiated, LAC sends CHAP challenge.
- Client sends CHAP response.
- LAC checks whether client session should be forwarded to the LNS based on received domain name. The check can be done locally or using a RADIUS server. Client also can be authenticated here before forwarding session.
- LAC brings up an L2TP tunnel.
- LNS checks if the LAC is allowed to open a tunnel and run the authentication process. The Tunnel is up and ready to forward VPDN sessions.
- LAC forwards LCP options negotiated with the client, username and password to the LNS.
- LNS authenticates the client locally or using RADIUS and sends a CHAP Success or CHAP Failure message.
- IP Control Protocol (IPCP) phase is performed, IP addresses and routes are installed. At this point the session is considered established.
