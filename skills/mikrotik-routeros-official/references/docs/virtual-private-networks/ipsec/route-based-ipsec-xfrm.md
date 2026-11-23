# Route-based IPsec with XFRM

> Route-based IPsec in RouterOS with XFRM interfaces: bind a policy group to an interface, route traffic into the tunnel, and run OSPF over it.

# Route-based IPsec with XFRM

Policy-based IPsec selects traffic by the source and destination addresses of the policies. An XFRM interface adds a route-based mode: a policy group is bound to a virtual interface, and the traffic that is routed into this interface uses the policies of the group. The routing table then decides which traffic enters the tunnel, and dynamic routing protocols can run over it.

An XFRM interface behaves like other interfaces: it has an IP address, an MTU and a running state. It is configured in [`/interface/xfrm`](../../cli-reference/interface/xfrm).

Use it for:

- **Dynamic routing over IPsec.** A branch office has several networks and gets new ones over time. With policy-based IPsec, each pair of local and remote networks needs a policy. With an XFRM interface, the branch runs OSPF over the tunnel, and new networks are reachable without new policies.
- **Several WAN links and policy routing.** The tunnel is a route, so routing marks or a VRF can send selected traffic into it, and the tunnel can move between WAN links without a change of the policies.

In the example, R1 has the public address 203.0.113.1, the LAN 192.168.51.0/28 and the XFRM address 192.168.50.1/24. R2 has 203.0.113.2, the LAN 192.168.52.0/28 and 192.168.50.2/24. R1 starts the connection and R2 answers.

## R1

Add the LAN bridge, the XFRM interface and their addresses:

```ros
/interface/bridge/add name=lan
/interface/xfrm/add name=xfrm1
/ip/address/add address=192.168.51.1/28 interface=lan
/ip/address/add address=192.168.50.1/24 interface=xfrm1
```

Add the profile and the proposal. They must be the same on both routers:

```ros
/ip/ipsec/profile/add name=xfrm-example hash-algorithm=sha256 \
    enc-algorithm=aes-256 dh-group=modp2048
/ip/ipsec/proposal/add name=xfrm-example auth-algorithms=sha256 \
    enc-algorithms=aes-256-cbc pfs-group=none
```

Add a policy group and bind it to the interface. A group of its own keeps these policies apart from the other IPsec policies of the router:

```ros
/ip/ipsec/policy/group/add name=xfrm1-group interface=xfrm1
```

Add the peer and the identity. The identity must have the same group in `policy-template-group`:

```ros
/ip/ipsec/peer/add name=xfrm-example address=203.0.113.2/32 \
    local-address=203.0.113.1 exchange-mode=ike2 \
    profile=xfrm-example
/ip/ipsec/identity/add peer=xfrm-example \
    auth-method=pre-shared-key secret=Example-psk-1 \
    generate-policy=port-strict policy-template-group=xfrm1-group
```

Add the policy for the traffic between the LANs, and route the remote LAN through the interface:

```ros
/ip/ipsec/policy/add peer=xfrm-example group=xfrm1-group \
    tunnel=yes src-address=192.168.51.0/28 \
    dst-address=192.168.52.0/28 proposal=xfrm-example
/ip/route/add dst-address=192.168.52.0/28 gateway=xfrm1
```

## R2

R2 has the same configuration with the addresses changed, and its peer has `passive=yes`:

```ros
/interface/bridge/add name=lan
/interface/xfrm/add name=xfrm1
/ip/address/add address=192.168.52.1/28 interface=lan
/ip/address/add address=192.168.50.2/24 interface=xfrm1
/ip/ipsec/profile/add name=xfrm-example hash-algorithm=sha256 \
    enc-algorithm=aes-256 dh-group=modp2048
/ip/ipsec/proposal/add name=xfrm-example auth-algorithms=sha256 \
    enc-algorithms=aes-256-cbc pfs-group=none
/ip/ipsec/policy/group/add name=xfrm1-group interface=xfrm1
/ip/ipsec/peer/add name=xfrm-example address=203.0.113.1/32 \
    local-address=203.0.113.2 exchange-mode=ike2 passive=yes \
    profile=xfrm-example
/ip/ipsec/identity/add peer=xfrm-example \
    auth-method=pre-shared-key secret=Example-psk-1 \
    generate-policy=port-strict policy-template-group=xfrm1-group
/ip/ipsec/policy/add peer=xfrm-example group=xfrm1-group \
    tunnel=yes src-address=192.168.52.0/28 \
    dst-address=192.168.51.0/28 proposal=xfrm-example
/ip/route/add dst-address=192.168.51.0/28 gateway=xfrm1
```

## Check

The interface has the flag `R` after an SA that uses it is made. Until then, an IP address on the interface is shown as invalid.

```ros
[admin@R1] > /interface/xfrm/print detail
Flags: R - RUNNING
0  R name="xfrm1" mtu=1400
```

The policy is active and shows the interface:

```ros
[admin@R1] > /ip/ipsec/policy/print detail where peer=xfrm-example
Flags: A - ACTIVE
0 A peer=xfrm-example tunnel=yes group=xfrm1-group src-address=192.168.51.0/28
    src-port=any dst-address=192.168.52.0/28 dst-port=any protocol=all
    action=encrypt level=require ipsec-protocols=esp sa-src-address=203.0.113.1
    sa-dst-address=203.0.113.2 proposal=xfrm-example active-interface=xfrm1
    ph2-count=1 ph2-state=established
```

Test the tunnel from the address of one LAN to the other: `/ping 192.168.52.1 src-address=192.168.51.1`.

:::warning
If the SA is made but the interface does not get the flag `R` and no traffic passes, re-create the interface or restart the router.
:::

- A policy group can be bound to one XFRM interface only.
- `mtu` is the layer 3 MTU of the interface. The default of 1400 bytes leaves room for the ESP overhead. A change of `mtu` applies at once, and `actual-mtu` in `/interface/print detail` shows the value in use. If `actual-mtu` is not the configured value, set `mtu` again.
- The example uses a pre-shared key. Use certificates in production.
- With the default firewall, the XFRM interface is not in the `LAN` interface list, so the router drops what arrives through it for the router itself, for example OSPF packets. Add the interface to the list or add accept rules for it.

## OSPF over XFRM

OSPF can run over the XFRM interface, and its routes replace the static routes of the first example. The policy must then match the OSPF packets too, also the multicast hello packets, so replace the LAN-to-LAN policy with a policy for all addresses in the XFRM group. The policy applies only to the traffic that is routed into the interface.

On R1:

```ros
/ip/route/remove [find gateway=xfrm1]
/ip/ipsec/policy/remove [find peer=xfrm-example]
/ip/ipsec/policy/add peer=xfrm-example group=xfrm1-group \
    tunnel=yes src-address=0.0.0.0/0 dst-address=0.0.0.0/0 \
    proposal=xfrm-example
/routing/ospf/instance/add name=xfrm-ospf version=2 \
    router-id=192.168.50.1
/routing/ospf/area/add name=backbone instance=xfrm-ospf \
    area-id=0.0.0.0
/routing/ospf/interface-template
add interfaces=xfrm1 area=backbone type=ptp
add networks=192.168.51.0/28 area=backbone
```

On R2, the same with its router ID and LAN:

```ros
/ip/route/remove [find gateway=xfrm1]
/ip/ipsec/policy/remove [find peer=xfrm-example]
/ip/ipsec/policy/add peer=xfrm-example group=xfrm1-group \
    tunnel=yes src-address=0.0.0.0/0 dst-address=0.0.0.0/0 \
    proposal=xfrm-example
/routing/ospf/instance/add name=xfrm-ospf version=2 \
    router-id=192.168.50.2
/routing/ospf/area/add name=backbone instance=xfrm-ospf \
    area-id=0.0.0.0
/routing/ospf/interface-template
add interfaces=xfrm1 area=backbone type=ptp
add networks=192.168.52.0/28 area=backbone
```

The neighbor reaches the state `Full`, and each router learns the LAN of the other one as an OSPF route (`/ip/route/print where ospf`):

```ros
[admin@R1] > /routing/ospf/neighbor/print
Flags: D - DYNAMIC
0 D instance=xfrm-ospf area=backbone interface=xfrm1 address=192.168.50.2
    router-id=192.168.50.2 state="Full" state-changes=5 adjacency=45s
    timeout=35s
```

Both routers must have the same MTU on the XFRM interface. With different values the OSPF neighbor stays in `ExStart`. Check `actual-mtu` with `/interface/print detail` on both routers.

## Read more

- [IPsec](./): how IKE works, the menus, the algorithms
- [Site-to-site tunnel](site-to-site)
- [OSPF](../../user-guides/routing-and-networking-protocols/unicast/ospf/)
- [Troubleshooting](troubleshooting)
