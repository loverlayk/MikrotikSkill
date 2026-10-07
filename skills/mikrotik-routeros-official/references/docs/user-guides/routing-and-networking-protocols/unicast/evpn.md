# EVPN

> This page introduces EVPN technology for Layer 2 and 3 VPN services, detailing BGP control planes, MPLS/VXLAN encapsulations, and EVPN route types (Type-1 to Type-5). It explains NVO terminology like NVE, VNI, and...

# EVPN

Ethernet Virtual Private Network (EVPN) is a technology that extends Layer 2 and Layer 3 connectivity between different network segments. MPLS or VXLAN encapsulations transfer Ethernet frames over MPLS or IP‑based networks.

BGP EVPN is used as the control plane for multiple data‑plane encapsulations (both Layer 2 and Layer 3 VPN services). MP‑BGP carries MAC addresses, MAC/IP bindings, and IP prefixes.

RFC7432 is the initial EVPN standard that defines BGP as the control plane for an MPLS data plane. RFC8365 extends support for additional data planes (VXLAN, NVGRE, and MPLS over GRE) and defines EVPN as a Network Virtualization Overlay (NVO).

## Terminology

- NVO: Network Virtualization Overlay used to deliver Layer2 and Layer 3 VPN services.
- NVE: Network Virtualization Endpoint is Provider Edge (PE) node within the NVO environment. It is responsible for encapsulation/decapsulation of VPN traffic. In case of VXLAN this defines VTEP (Virtual Tunnel End Point).
- VNI: Virtual Network Identifier
- EVI: EVPN Instance
- RD: [Route Distinguisher](../route-distinguisher-and-route-target.md#route-distinguisher) is a 64-bit prefix appended to IP prefix to make it unique, multiple tenants can use overlapping IP range.
- RT: [Route Target](../route-distinguisher-and-route-target.md#route-targets) is BGP extended community used to control import and export of routes. Typically, RT is based on the AS number and the VNI of the MAC-VRF
- MAC-VRF: [VRF](../vrf.md) table for MAC addresses on a PE (VTEP). Requires RD and RT.
- BUM:  Broadcast, unknown Unicast and Multicast traffic is a multi-destination layer2 traffic in vxlan networks.
- Ingress replication: unicast approach to handle BUM traffic. It uses IMET routes to auto-discover remote peers.  Ingress device replicates BUM traffic to all the VTEPS associated with the Layer-2 VNI.
- ESI - Ethernet Segment Identifier

For MP-BGP to carry EVPN, new AFI/SAFI was defined 25(L2 VPN)/70(EVPN). Next-hop address within the NLRI is an IP address of the VTEP advertising the EVPN route.

There are five EVPN route types:

- Type‑1: (Ethernet A‑D) announces reachability of a multi‑homed Ethernet segment.
- Type‑2: (MAC advertisement / MACIP) advertises the MAC address of a MAC/IP binding learned by a specific EVI.
- Type‑3: (Inclusive multicast IMET) advertises membership of a Layer 2 domain, allowing auto discovery of VTEPs.
- Type‑4: (Ethernet segment) is used to discover VTEPs attached to the same shared Ethernet segment for the EVPN multi‑homing model (active‑active or active‑standby forwarding).
- Type‑5: (IP prefix) advertising an IP prefix into the EVPN domain allows creation of a classic Layer 3 VPN (see [`/routing/bgp/vpn`](../../../cli-reference/routing/bgp/vpn.md)).

Data plane encapsulation is defined with encapsulation extended community value:

- 8 - VXLAN (currently only one supported by ROS)
- 9 - NVGRE
- 10 - MPLS
- 11 - MPLSoGRE

There are two methods for supporting inter-subnet routing with EVPN: symmetric and asymmetric integrated routing and bridging (IRB). The main difference between the two methods is that the symmetric method supports both routing and bridged on both the ingress and egress VTEPs, where the asymmetric method supports routing on the ingress, but only bridging on the egress. Symmetric IRB requires a [VRF](../vrf.md) instance for the L3VNI.

## Route list

RouterOS will show local and received EVPN routes in the [`/routing/route`](../../../cli-reference/routing/route.md) list

Locally generated routes will have the **e-evpn** flag. For example:

```routeros
[admin@ros_leaf_3] /routing/route> print where evpn
Flags: e - EVPN
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE
  DST-ADDRESS                                     GATEWAY        AFI   DISTANCE  SCOPE  TARGET-SCOPE
e [10.155.101.133:1010]macip:0|0C:50:85:84:00:01  203.0.255.133  evpn       200     40            10
e [10.155.101.133:1010]imet:0|203.0.255.133       203.0.255.133  evpn       200     40            10
e [203.0.255.133:4]imet:0|203.0.255.133           203.0.255.133  evpn       200     40            10

```

EVPN data is encoded in `dst-address` parameter:

```
    Dst [rd]type:x|y
         ^  ^    ^
         |  |    + - where x - tag or ESI; y - type specific data (can show mac addresses, ip addresses, ethernet segments etc.)
         |  +------- name of the EVPN route type (macip, imet, es, ad, prefix)
         +---------- route distinguisher in square brackets

```

## Configuration Examples

### Basic Configuration Example

Basic Layer2 EVPN Vxlan configuration:

```routeros
/interface/bridge
add name=bridge1 vlan-filtering=yes pvid=40
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus3 pvid=40

/ip/address
add address=203.0.113.1 interface=lo

/interface/vxlan
add bridge=bridge1 bridge-pvid=40 local-address=203.0.113.1 name=vxlan1 vni=100040 learning=no

/routing/bgp/instance
add as=65000 name=evpn-inst

/routing/bgp/connection
add afi=evpn instance=evpn-inst local.address=203.0.113.1 .role=ebgp multihop=yes name=to-leaf-lo remote.address=203.0.113.2 .as=65001

/routing/bgp/evpn
add instance=evpn-inst name=bgp-evpn-1o vni=100040
```

For simple setups with only one VNI, there is no need to set a route distinguisher or [`import.route-targets`](../../../cli-reference/routing/bgp/evpn.md#import.route-targets)/[`export.route-targets`](../../../cli-reference/routing/bgp/evpn.md#export.route-targets).

:::info
When [RTs](../route-distinguisher-and-route-target.md#route-targets) or [RD](../route-distinguisher-and-route-target.md#route-distinguisher) are not specified, values are derived automatically. Route targets are set to `<PE ASN>:<VNI>`, route distinguishers `<PE address>:<num derived from config id>`).
:::

EVPN configuration is directly mapped to VXLAN configurations with matching VNIs

### Bridged EVPN VXLAN Overlay with Arista's Eos and ROS

#### Topology

For this example we will use the following topology:

![](img/evpn_eos_ros.jpg#gh-light-mode-only)
![](img/evpn_eos_ros_dark.png#gh-dark-mode-only)

- 203.0.255.0/24 address range is used for loopback addresses
- Subnets from the 172.16.0.0/16 range are used for underlay connectivity of leaf and spine routers
- Subnets from the 192.168.0.0/16 range are used for host addressing on VLANs.

#### Underlay Configuration

Underlay connectivity depends on the existing network; it can use eBGP, [OSPF](./ospf/areas-and-virtual-links.md), ISIS, or even static routing. In this example we use OSPF as the underlay routing protocol to advertise routes for loopback interface addresses.

**Ros\_Spine**

```routeros
/ip/address
add address=203.0.255.138 interface=lo
add address=172.16.1.1/30 interface=ether3
add address=172.16.2.1/30 interface=ether4
add address=172.16.3.1/30 interface=ether5
add address=172.16.4.1/30 interface=ether6
add address=172.16.5.1/30 interface=ether7

/routing/ospf/instance
add name=evpn_underlay
/routing/ospf/area
add disabled=no instance=evpn_underlay name=evpn-underlay-bb
/routing/ospf/interface-template
add area=evpn-underlay-bb disabled=no networks=172.16.0.0/16
add area=evpn-underlay-bb disabled=no interfaces=lo passive
```

**Ros\_Leaf\_3**

```routeros
/ip/address
add address=203.0.255.133 interface=lo
add address=172.16.3.2/30 interface=ether10

/routing/ospf/instance
add name=evpn_underlay
/routing/ospf/area
add disabled=no instance=evpn_underlay name=evpn-underlay-bb
/routing/ospf/interface-template
add area=evpn-underlay-bb disabled=no networks=172.16.0.0/16
add area=evpn-underlay-bb disabled=no interfaces=lo passive
```

**Eos\_Leaf**

```
interface Ethernet1
   no switchport
   ip address 172.16.5.2/30
!
interface Loopback0
   ip address 203.0.255.128/32
!
ip routing
!
router ospf 100
   router-id 203.0.255.135
   redistribute connected
   network 172.16.1.0/30 area 0.0.0.0
!

```

#### BGP EVPN Overlay

For the [BGP](./bgp/understanding-bgp.md) overlay we use [`multihop`](../../../cli-reference/routing/bgp/connection.md#multihop) eBGP with loopback addresses.

To simplify configuration, use a BGP [`/routing/bgp/template`](../../../cli-reference/routing/bgp/template.md) to set common parameters and configure the [`/routing/bgp/connection`](../../../cli-reference/routing/bgp/connection.md) to listen on the entire loopback address range. This approach scales well: adding more leaf routers requires no changes on the spine routers.

Also it is recommended to set [`nexthop-choice`](../../../cli-reference/routing/bgp/connection.md#nexthop-choice) to propagate especially if there is more than one spine. In case if iBGP is used as overlay then spines should be route reflectors and nexthop propagation is happening by default.

**Ros\_Spine** — [`/routing/bgp/instance`](../../../cli-reference/routing/bgp/instance.md)

```routeros
/routing/bgp/instance
add as=65000 name=bgp-instance-1
/routing/bgp/template
set default afi=evpn multihop=yes nexthop-choice=propagate
/routing/bgp/connection
add instance=bgp-instance-1 local.address=203.0.255.138 .role=ebgp name=evpn_leafs remote.address=\
    203.0.255.0/24 templates=default
```

**Ros\_Leaf\_3** — [`/routing/bgp/instance`](../../../cli-reference/routing/bgp/instance.md), [`/routing/bgp/connection`](../../../cli-reference/routing/bgp/connection.md)

```routeros
/routing/bgp/instance
add as=65003 disabled=no name=bgp-instance-1
/routing/bgp/connection
add afi=evpn instance=bgp-instance-1 local.address=203.0.255.133 .role=ebgp multihop=yes name=to_spine remote.address=\
    203.0.255.138
```

**Eos\_Leaf**

```
service routing protocols model multi-agent
!
router bgp 65005
   neighbor SPINE_EVPN peer group
   neighbor SPINE_EVPN remote-as 65000
   neighbor SPINE_EVPN update-source Loopback0
   neighbor SPINE_EVPN ebgp-multihop 10
   neighbor SPINE_EVPN send-community extended
   neighbor 203.0.255.138 peer group SPINE_EVPN
   !
   address-family evpn
      neighbor SPINE_EVPN activate
!
```

##### Verify BGP Connectivity

Check the [`/routing/bgp/session`](../../../cli-reference/routing/bgp/session/session.md) to verify the BGP peering status.

**Eos\_Leaf**

```
localhost#show bgp summary
BGP summary information for VRF default
Router identifier 203.0.255.128, local AS number 65005
Neighbor               AS Session State AFI/SAFI                AFI/SAFI State   NLRI Rcd   NLRI Acc
------------- ----------- ------------- ----------------------- -------------- ---------- ----------
203.0.255.138       65000 Established   IPv4 Unicast            Advertised              0          0
203.0.255.138       65000 Established   L2VPN EVPN              Negotiated              6          6
```

**Ros\_Leaf\_3**

```routeros
[admin@ros_leaf_3] /routing/bgp/session> print
Flags: E - established
 0 E name="to_spine-1" instance=bgp-instance-1
     remote.address=203.0.255.138 .as=65000 .id=203.0.255.138 .capabilities=mp,rr,gr,as4 .afi=evpn .messages=7 .bytes=682 .eor=""
     local.address=203.0.255.133 .as=65003 .id=203.0.255.133 .cluster-id=203.0.255.133 .capabilities=mp,rr,gr,as4 .afi=evpn .messages=7
     .bytes=698 .eor=""
     output.procid=20
     input.procid=20 ebgp
     multihop=yes hold-time=3m keepalive-time=1m uptime=1s620ms last-started=2025-05-29 11:01:38 prefix-count=0
```

#### VXLAN and EVPN configuration

**Ros\_Leaf\_3**

Just for demonstration purposes, on RouterOS leaf we will be sending vlan tagged traffic to the host.

VXLAN learning should be disabled as we are using [BGP EVPN](../../../cli-reference/routing/bgp/evpn.md) for discovery. The EVPN configuration is done under [`/routing/bgp/evpn`](../../../cli-reference/routing/bgp/evpn.md) menu.

```routeros
/interface/bridge
add name=bridge1 pvid=10 vlan-filtering=yes
/interface/vxlan
add bridge=bridge1 bridge-pvid=10 learning=no local-address=203.0.255.133 mac-address=C2:16:F6:B2:CC:D3 name=vxlan1 vni=1010
/interface/bridge/port
add bridge=bridge1 interface=ether11 pvid=10
/ip/address
add address=192.168.10.133/24 interface=bridge1
/routing/bgp/evpn
add disabled=no export.route-targets=1010:1010 import.route-targets=1010:1010 instance=bgp-instance-1 name=bgp-evpn-1 vni=1010
```

**Eos\_Leaf**

On the Arista router we are setting vlan trunk, untagged traffic will be sent to the host

```
vlan 10
!
interface Ethernet2
   switchport trunk allowed vlan 10
   switchport mode trunk
!
interface Vlan10
   ip address 192.168.10.128/24
!
interface Vxlan1
   vxlan source-interface Loopback0
   vxlan vlan 10 vni 1010
!
router bgp 65501
   vlan 10
      rd 203.0.255.128:1010
      route-target both 1010:1010
      redistribute learned
```

**Host\_1**

```routeros
/ip/address
add address=192.168.10.132/24 interface=ether2
```

**Host\_3**

```routeros
/interface/vlan
add interface=ether2 name=vlan10 vlan-id=10
/ip/address
add address=192.168.10.129/24 interface=vlan10
```

#### Validate L2VPN Service

Let's verify that **IMET** routes are present on the leaf routers and that **VTEPs** are discovered.

```routeros
[admin@ros_leaf_3] /routing/route> print where dst-address~"imet"
Flags: A - ACTIVE; b - BGP, e - EVPN
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
   DST-ADDRESS                               GATEWAY        AFI   DISTANCE  SCOPE  TARGET-SCOPE  IMMEDIATE-GW
Ab [203.0.255.128:1010]imet:0|203.0.255.128  203.0.255.128  evpn        20     40            30  172.16.3.1%ether10
 e [203.0.255.133:256]imet:0|203.0.255.133   203.0.255.133  evpn       200     40            10

[admin@ros_leaf_3] /interface/vxlan/vteps> print
Flags: D - DYNAMIC
Columns: INTERFACE, REMOTE-IP
#   INTERFACE  REMOTE-IP
0 D vxlan1     203.0.255.128
```

On Arista:

```
localhost#show bgp evpn route-type imet
BGP routing table information for VRF default
Router identifier 203.0.255.135, local AS number 65501
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending BGP convergence
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >      RD: 203.0.255.128:1010 imet 203.0.255.128
                                 -                     -       -       0       i
 * >      RD: 203.0.255.133:256 imet 203.0.255.133
                                 203.0.255.133         -       100     0       65000 65003 i

localhost#show interfaces vxlan1
Vxlan1 is up, line protocol is up (connected)
  Hardware is Vxlan
  Source interface is Loopback0 and is active with 203.0.255.128
  Listening on UDP port 4789
  Replication/Flood Mode is headend with Flood List Source: EVPN
  Remote MAC learning via EVPN
  VNI mapping to VLANs
  Static VLAN to VNI mapping is
    [10, 1010]
  Note: All Dynamic VLANs used by VCS are internal VLANs.
        Use 'show vxlan vni' for details.
  Static VRF to VNI mapping is not configured
  Headend replication flood vtep list is:
    10 203.0.255.133
  Shared Router MAC is 0000.0000.0000

localhost#show vxlan flood vtep vlan 10
          VXLAN Flood VTEP Table
--------------------------------------------------------------------------------

VLANS                            Ip Address
-----------------------------   ------------------------------------------------
10                              203.0.255.133

```

At this point we can try to ping **host\_3** from **host\_1**:

```routeros
[admin@host_1] /interface> print
...
1 R ether2  ether           1500  0C:50:85:84:00:01

[admin@host_1] /ip/address> /ping 192.168.10.129
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 192.168.10.129                             56  64 17ms26us
    1 192.168.10.129                             56  64 13ms119us
    2 192.168.10.129                             56  64 17ms192us
```

**host-3**

```routeros
[admin@host_1] /interface> print
...
1 R ether2  ether           1500  0C:74:39:88:00:01
```

Now we should be able to see that EVPN is used to learn remote MAC addresses by looking at MACIP routes.

If we look at routes on **ros\_leaf**, we can see that router 203.0.255.128 sent the macip route for 0C:74:39:88:00:01 mac address which is the **host\_1** mac address located behind **eos\_leaf**.

Eos also sends MAC/IP binding which is used for arp/nd suppression. Unfortunately at the time of writing this article RouterOS does not have this functionality.

```routeros
[admin@ros_leaf_3] /routing/route> print where dst-address~"macip"
Flags: A - ACTIVE; b - BGP, e - EVPN
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
   DST-ADDRESS                                                   GATEWAY        AFI   DISTANCE  SCOPE  TARGET-SCOPE  IMMEDIATE-GW
Ab [203.0.255.128:1010]macip:0|0C:74:39:88:00:01                 203.0.255.128  evpn        20     40            30  172.16.3.1%ether10
 e [203.0.255.133:256]macip:0|0C:50:85:84:00:01                  203.0.255.133  evpn       200     40            10
Ab [203.0.255.128:1010]macip:0|0C:74:39:88:00:01|192.168.10.129  203.0.255.128  evpn        20     40            30  172.16.3.1%ether10
```

Arista allows additionally to see remotely learned mac addresses in "vxlan mac table" and "vlan mac-address table" includes local mac addresses as well:

```
localhost#show bgp evpn route-type mac-ip detail
BGP routing table information for VRF default
Router identifier 203.0.255.128, local AS number 65005
BGP routing table entry for mac-ip 0c50.8584.0001, Route Distinguisher: 203.0.255.133:256
 Paths: 1 available
  65000 65003
    203.0.255.133 from 203.0.255.138 (203.0.255.138)
      Origin IGP, metric -, localpref 100, weight 0, tag 0, valid, external, best
      Extended Community: Route-Target-AS:1010:1010 TunnelEncap:tunnelTypeVxlan
      VNI: 0 ESI: 0000:0000:0000:0000:0000
BGP routing table entry for mac-ip 0c74.3988.0001, Route Distinguisher: 203.0.255.128:1010
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, tag 0, valid, local, best
      Extended Community: Route-Target-AS:1010:1010 TunnelEncap:tunnelTypeVxlan
      VNI: 1010 ESI: 0000:0000:0000:0000:0000
BGP routing table entry for mac-ip 0c74.3988.0001 192.168.10.129, Route Distinguisher: 203.0.255.128:1010
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, tag 0, valid, local, best
      Extended Community: Route-Target-AS:1010:1010 TunnelEncap:tunnelTypeVxlan
      VNI: 1010 ESI: 0000:0000:0000:0000:0000

localhost#show vxlan address-table vlan 10
          Vxlan Mac Address Table
----------------------------------------------------------------------

VLAN  Mac Address     Type      Prt  VTEP             Moves   Last Move
----  -----------     ----      ---  ----             -----   ---------
  10  0c50.8584.0001  EVPN      Vx1  203.0.255.133    1       1:30:49 ago
Total Remote Mac Addresses for this criterion: 1

localhost#show mac address-table vlan 10
          Mac Address Table
------------------------------------------------------------------

Vlan    Mac Address       Type        Ports      Moves   Last Move
----    -----------       ----        -----      -----   ---------
  10    0c50.8584.0001    DYNAMIC     Vx1        1       1:31:17 ago
  10    0c74.3988.0001    DYNAMIC     Et2        1       1 day, 23:45:18 ago
Total Mac Addresses for this criterion: 2

          Multicast Mac Address Table
------------------------------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       ----        -----
Total Mac Addresses for this criterion: 0
```

### Bridged EVPN Overlay with Arista ESI LAG

**ESI-LAG** (Ethernet Segment Identifier - Link Aggregation) or **EVPN-LAG**  is a networking concept that enables multihoming using **EVPN** (Ethernet Virtual Private Network) technology, where client devices (like access switches) can connect to core devices (like distribution switches) through multiple links, forming a logical **LAG** interface.

#### Topology

Let's extend the topology from the previous example. **Host\_2** is a RouterOS device with **LACP** enabled on links connecting to two Arista leafs, forming an active‑active multihoming setup.

![](img/evpn_eos_ros_2.jpg#gh-light-mode-only)
![](img/evpn_eos_ros_2_dark.png#gh-dark-mode-only)

#### Configuration Prerequisities

For details on setting up the underlay and EVPN overlay, refer to the example above. This section focuses on ESI LAG configuration and validation.

#### Port Channel configuration

Assuming that the underlay and overlay are configured and running, proceed to port‑channel configuration on the Arista switches:

**leaf\_2** and **leaf\_4** config is exactly the same

```
interface Port-Channel3
   switchport access vlan 10
   switchport trunk allowed vlan 10
   switchport mode trunk
   !
   evpn ethernet-segment
      identifier 0000:0000:0000:0333:3333
      route-target import 00:00:03:33:33:33
   lacp system-id 0000.0333.3333
!
interface Ethernet2
   channel-group 3 mode active
```

**ros\_host\_2**

```routeros
/interface/bonding
add mode=802.3ad name=bond1 slaves=ether2,ether3
/interface/vlan
add interface=bond1 mtu=1496 name=vlan10 vlan-id=10
/ip/address
add address=192.168.10.130/24 interface=vlan10
```

#### Validate setup

Now if we look at evpn routes we should see some new route types. Both Arista switches are advertising Type-1 AD routes and Type-4 Ethernet Segment (ES) routes to discover multihoming VTEPs

```routeros
[admin@gns3_spine1_ros] /routing/route>  print where afi=evpn dst-address~"(ad|es)"
Flags: A - ACTIVE; b - BGP
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE
   DST-ADDRESS                                                      GATEWAY        AFI   DISTANCE  SCOPE  TA
Ab [203.0.255.127:1]ad:4294967295|00:00:00:00:00:00:03:33:33:33     203.0.255.127  evpn        20     40  30
Ab [203.0.255.127:1]es:00:00:00:00:00:00:03:33:33:33|203.0.255.127  203.0.255.127  evpn        20     40  30
Ab [203.0.255.127:1010]ad:0|00:00:00:00:00:00:03:33:33:33           203.0.255.127  evpn        20     40  30

Ab [203.0.255.134:1]ad:4294967295|00:00:00:00:00:00:03:33:33:33     203.0.255.134  evpn        20     40  30
Ab [203.0.255.134:1]es:00:00:00:00:00:00:03:33:33:33|203.0.255.134  203.0.255.134  evpn        20     40  30
Ab [203.0.255.134:1010]ad:0|00:00:00:00:00:00:03:33:33:33           203.0.255.134  evpn        20     40  30

```

If we check both Eos leafs, we will see that designated forwarder 203.0.255.127 (**eos\_leaf\_4**) is selected:

```
eos_leaf_2#show bgp evpn instance vlan 10
EVPN instance: VLAN 10
  Route distinguisher: 203.0.255.134:1010
  Route target import: Route-Target-AS:1010:1010
  Route target export: Route-Target-AS:1010:1010
  Service interface: VLAN-based
  Local VXLAN IP address: 203.0.255.134
  VXLAN: enabled
  MPLS: disabled
  Local ethernet segment:
    ESI: 0000:0000:0000:0333:3333
      Type: 0 (administratively configured)
      Interface: Port-Channel3
      Mode: all-active
      State: up
      ES-Import RT: 00:00:03:33:33:33
      DF election algorithm: modulus
      Designated forwarder: 203.0.255.127
      Non-Designated forwarder: 203.0.255.134

```

Let's suspend the link from **host2** to **eos\_leaf\_4** and observe the result:

```
eos_leaf_2#show bgp evpn instance vlan 10
EVPN instance: VLAN 10
  Route distinguisher: 203.0.255.134:1010
  Route target import: Route-Target-AS:1010:1010
  Route target export: Route-Target-AS:1010:1010
  Service interface: VLAN-based
  Local VXLAN IP address: 203.0.255.134
  VXLAN: enabled
  MPLS: disabled
  Local ethernet segment:
    ESI: 0000:0000:0000:0333:3333
      Type: 0 (administratively configured)
      Interface: Port-Channel3
      Mode: all-active
      State: up
      ES-Import RT: 00:00:03:33:33:33
      DF election algorithm: modulus
      Designated forwarder: 203.0.255.134

[admin@spine1_ros] /routing/route>  print interval=1 where dst-address~"ad|es"
Flags: A - ACTIVE; b - BGP
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE
   DST-ADDRESS                                                      GATEWAY        AFI   DISTANCE  SCOPE  TA
Ab [203.0.255.134:1]ad:4294967295|00:00:00:00:00:00:03:33:33:33     203.0.255.134  evpn        20     40  30
Ab [203.0.255.134:1]es:00:00:00:00:00:00:03:33:33:33|203.0.255.134  203.0.255.134  evpn        20     40  30
Ab [203.0.255.134:1010]ad:0|00:00:00:00:00:00:03:33:33:33           203.0.255.134  evpn        20     40  30

[admin@host_2] /interface/bonding> /ping 192.168.10.132 interval=500ms
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 192.168.10.132                             56  64 2ms90us
    1 192.168.10.132                             56  64 2ms172us
    2 192.168.10.132                             56  64 2ms503us
    3 192.168.10.132                                               timeout
    4 192.168.10.132                                               timeout
    5 192.168.10.132                                               timeout
    6 192.168.10.132                             56  64 2ms191us
    7 192.168.10.132                             56  64 2ms31us
```

**eos\_leaf\_2** became forwarder, **eos\_leaf\_4** withdraw  ES and AD routes and traffic switched to other LACP link.
