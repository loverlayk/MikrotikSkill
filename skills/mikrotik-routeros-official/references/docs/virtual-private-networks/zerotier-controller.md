# Self-hosted ZeroTier controller on a hAP ax³

> Host your own private ZeroTier network on a hAP ax³ with the controller built into RouterOS: turn ZeroTier on in device mode, install the zerotier package, create the network, authorize the hAP and an office router...

# Self-hosted ZeroTier controller on a hAP ax³

**Package:** `zerotier`

A ZeroTier network has a controller. The controller decides which devices may join the network and gives them their addresses and routes. ZeroTier's own service, ZeroTier Central, is one such controller. The `zerotier` package of RouterOS has a controller too, so a router can host the network itself. The network and its members are then part of the router's configuration.

This guide makes a hAP ax³ at home the controller of a private network, `home-net`, and connects an office router to it:

- the hAP ax³ (`home`) gets the address `172.27.27.1`;
- the office router (`office`) gets the address `172.27.27.2`.

Both routers can then reach each other over ZeroTier, and the hAP ax³ decides who else may join.

## Before you begin

- The hAP ax³ has the default configuration: the internet on `ether1` and the default firewall.
- The office router is an ARM or ARM64 router: `/system/resource/print` shows `architecture-name: arm` or `arm64`. The `zerotier` package exists only for these two architectures; the hAP ax³ is ARM64.
- You can reach the office router while you set it up: the device mode change needs someone at the router, and the package install reboots it.
- The office router has the default firewall too. On a router with other firewall rules, put the rule of this guide before the rule that drops input traffic.
- Both routers have internet access. The routers find each other and the controller through ZeroTier's root servers on the internet, also when the controller is your own router.
- The subnet `172.27.27.0/24` is not used in either network.

## Turn on ZeroTier in device mode

Device mode can turn ZeroTier off. On both routers, check it:

```ros
/system/device-mode/print
```

If the output shows `zerotier: no`, run `/system/device-mode/update zerotier=yes` and confirm the change at the router, as described in [Device mode](../system-information-and-utilities/device-mode).

## Install the zerotier package

On both routers, load the list of packages, mark `zerotier` for install, and apply the change. The router downloads the package and reboots:

```ros
/system/package/update/check-for-updates
/system/package/enable zerotier
/system/package/apply-changes
```

To install the package from a file instead, see [Packages](../getting-started/installation-and-upgrade/packages).

## Create the network on the hAP ax³

Turn on the default ZeroTier instance, `zt1`. Its comment names ZeroTier Central, but the same instance hosts your own controller:

```ros
/zerotier/enable zt1
/zerotier/print
```

Wait until the instance has the `R` (online) flag:

```text
Flags: R - ONLINE
Columns: NAME, PORT
#   NAME  PORT
;;; ZeroTier Central controller - https://my.zerotier.com/
0 R zt1   9993
```

The flag shows that the router reaches ZeroTier's root servers. Until the instance runs, a new network gets no network ID, so create the network only after this step.

Create the network and join the hAP ax³ to it:

```ros
/zerotier/controller/add instance=zt1 name=home-net private=yes \
    ip-range=172.27.27.10-172.27.27.20 routes=172.27.27.0/24
/zerotier/interface/add instance=zt1 name=zt-home \
    network=[/zerotier/controller/get [find name=home-net] network]
```

- `private=yes` lets only authorized members into the network. With `private=no`, every device that knows the network ID is authorized when it joins.
- `routes=172.27.27.0/24` gives the members a route to the network's subnet. The members get their addresses only when `routes` has a subnet for them: without it, an authorized member gets no address from `ip-range`.
- `ip-range` is the pool for members that have no fixed address. In this guide both routers get fixed addresses, and the pool serves members you add later.

Check the network, the new interface and the member list:

```ros
/zerotier/controller/print
/zerotier/interface/print
/zerotier/controller/member/print
```

```text
Columns: INSTANCE, NAME, NETWORK, PRIVATE
# INSTANCE  NAME      NETWORK           PRIVATE
0 zt1       home-net  086bc0f47bb51c5e  yes    

Columns: NAME, MAC-ADDRESS, NETWORK, STATUS
# NAME     MAC-ADDRESS        NETWORK           STATUS       
0 zt-home  5E:14:DE:BB:00:BB  086bc0f47bb51c5e  ACCESS_DENIED

Columns: NETWORK, ZT-ADDRESS
#  NETWORK   ZT-ADDRESS
0  home-net  086bc0f47b
```

The network ID (`086bc0f47bb51c5e` here) is what other routers use to join. The hAP ax³ is in its own network as a member, but it is not authorized yet, so its interface shows `ACCESS_DENIED`. The member list shows it by its ZeroTier address, which is also the first ten characters of the network ID. The member list can take a few seconds to show a new member.

## Authorize the hAP ax³

Authorize the hAP ax³ in its own network and give it the address `172.27.27.1`. Use the ZeroTier address from your member list:

```ros
/zerotier/controller/member/set [find zt-address=086bc0f47b] \
    authorized=yes name=home ip-address=172.27.27.1
```

The address does not have to be in `ip-range`. Check that the interface is up and has the address:

```ros
/zerotier/interface/print
/ip/address/print where interface=zt-home
```

```text
Flags: R - RUNNING
Columns: NAME, MAC-ADDRESS, NETWORK, NETWORK-NAME, STATUS
#   NAME     MAC-ADDRESS        NETWORK           NETWORK-NAME  STATUS
0 R zt-home  5E:14:DE:BB:00:BB  086bc0f47bb51c5e  home-net      OK    

Flags: D - DYNAMIC
Columns: ADDRESS, NETWORK, INTERFACE, VRF
#   ADDRESS         NETWORK      INTERFACE  VRF 
0 D 172.27.27.1/24  172.27.27.0  zt-home    main
```

## Join the office router

On the office router, turn on the instance and join the network with the network ID from the hAP ax³. The interface has the same name as on the hAP ax³, so the firewall rule later in this guide is the same on both routers:

```ros
/zerotier/enable zt1
/zerotier/interface/add instance=zt1 name=zt-home \
    network=086bc0f47bb51c5e
```

Check the router's ZeroTier address and the interface:

```ros
/zerotier/print detail
/zerotier/interface/print
```

```text
Flags: R - ONLINE
0  R ;;; ZeroTier Central controller - https://my.zerotier.com/
     name="zt1" disabled=no port=9993 interfaces=all route-distance=1
     backup-priorities=""
     identity.public="daf4d8238e:0:a816684eac8f759140345a147ac0d38ddb76043f2f45
        a97eaee586d20409a8797fb5bc436afbc248f6e16136015ae3005c1a6b9dde20fa620a6
        84cc891adb52d" state="running"

Columns: NAME, MAC-ADDRESS, NETWORK, STATUS
# NAME     MAC-ADDRESS        NETWORK           STATUS                  
0 zt-home  5E:C6:41:A3:D7:4E  086bc0f47bb51c5e  REQUESTING_CONFIGURATION
```

The first ten characters of `identity.public` are the router's ZeroTier address, `daf4d8238e` here. The status is `REQUESTING_CONFIGURATION` while the router looks for the controller, and changes to `ACCESS_DENIED` when the controller has its request.

## Authorize the office router

On the hAP ax³, the office router is now in the member list, without the `A` (authorized) flag:

```ros
/zerotier/controller/member/print
```

```text
Flags: A - AUTHORIZED
Columns: NAME, NETWORK, ZT-ADDRESS, IP-ADDRESS
#   NAME  NETWORK   ZT-ADDRESS  IP-ADDRESS 
0 A home  home-net  086bc0f47b  172.27.27.1
1         home-net  daf4d8238e
```

The hAP ax³ itself has no `LAST-SEEN`. Any ZeroTier device that knows the network ID can ask to join and appears in this list. The list shows only the device's ZeroTier address, so authorize only the addresses you know, for example from the owner of the device. Compare the address with the office router, then authorize it with the address `172.27.27.2`:

```ros
/zerotier/controller/member/set [find zt-address=daf4d8238e] \
    authorized=yes name=office ip-address=172.27.27.2
```

On the office router, the interface changes to `OK` and gets the address:

```ros
/zerotier/interface/print
/ip/address/print where interface=zt-home
```

```text
Flags: R - RUNNING
Columns: NAME, MAC-ADDRESS, NETWORK, NETWORK-NAME, STATUS
#   NAME     MAC-ADDRESS        NETWORK           NETWORK-NAME  STATUS
0 R zt-home  5E:C6:41:A3:D7:4E  086bc0f47bb51c5e  home-net      OK    

Flags: D - DYNAMIC
Columns: ADDRESS, NETWORK, INTERFACE, VRF
#   ADDRESS         NETWORK      INTERFACE  VRF 
3 D 172.27.27.2/24  172.27.27.0  zt-home    main
```

## Let the members reach the routers

The default firewall drops traffic to the router from interfaces that are not in the `LAN` list, and the ZeroTier interface is not in it. Ping works, because the default firewall accepts ICMP, but other traffic to the router, such as WebFig, does not. On both routers, accept the traffic from the ZeroTier interface before the default drop rule:

```ros
/ip/firewall/filter/add chain=input action=accept \
    in-interface=zt-home comment="ZeroTier members" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

The rule accepts all traffic to the router from every authorized member of the network, also from the members you authorize later.

## Check the connection

On the office router, ping the hAP ax³ and open its WebFig page:

```ros
/ping 172.27.27.1 count=3
/tool/fetch url="http://172.27.27.1/" output=none
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS      
    0 172.27.27.1                                56  64 41ms358us 
    1 172.27.27.1                                56  64 719us     
    2 172.27.27.1                                56  64 708us     
    sent=3 received=3 packet-loss=0% min-rtt=708us avg-rtt=14ms261us 
   max-rtt=41ms358us 

  status: requesting

      status: finished
        code: 200     
  downloaded: 1KiB    
       total: 1KiB    
    duration: 1s      
```

`status: finished` shows that the firewall rule works. Without the rule, the ping works but the fetch ends with `failure: timeout connecting`. `/tool/fetch` needs `fetch` allowed in [Device mode](../system-information-and-utilities/device-mode).

On the hAP ax³, both members are authorized, and the counter of the new rule grows:

```ros
/zerotier/controller/member/print
/ip/firewall/filter/print stats where comment="ZeroTier members"
```

```text
Flags: A - AUTHORIZED
Columns: NAME, NETWORK, ZT-ADDRESS, IP-ADDRESS, LAST-SEEN
#   NAME    NETWORK   ZT-ADDRESS  IP-ADDRESS   LAST-SEEN
0 A home    home-net  086bc0f47b  172.27.27.1           
1 A office  home-net  daf4d8238e  172.27.27.2  1s740ms  

Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN  ACTION  BYTES  PACKETS
;;; ZeroTier members
1 input  accept     60        1
```

## Remove a router from the network

To take a router out of the network, remove its authorization on the hAP ax³:

```ros
/zerotier/controller/member/set [find name=office] authorized=no
```

Traffic between the routers stops. On the hAP ax³, a ping to the office router fails:

```ros
/ping 172.27.27.2 count=3
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS      
    0 172.27.27.2                                                  timeout     
    1 172.27.27.2                                                  timeout     
    2 172.27.27.2                                                  timeout     
    sent=3 received=0 packet-loss=100% 
```

The interface status on the office router changes to `ACCESS_DENIED` a little later, and the address stays on the interface:

```text
Columns: NAME, MAC-ADDRESS, NETWORK, NETWORK-NAME, STATUS
# NAME     MAC-ADDRESS        NETWORK           NETWORK-NAME  STATUS       
0 zt-home  5E:C6:41:A3:D7:4E  086bc0f47bb51c5e  home-net      ACCESS_DENIED
```

To let the router in again, set `authorized=yes` on the same entry. The office router keeps asking to join: its entry stays in the member list without the `A` flag, and its `LAST-SEEN` keeps changing. If you remove the entry with `/zerotier/controller/member/remove`, the entry comes back, unauthorized and without an address, the next time the router asks. To stop the requests, remove the `zt-home` interface on the office router.

## Technical details

- The first ten hexadecimal digits of a network ID are the ZeroTier address of the controller's instance. Each `/zerotier/controller/add` creates a new network ID. A network that is removed and added again has a different ID, and the members join with the new ID.
- A member reaches the controller through ZeroTier's root servers. Without internet access, a router stays in `REQUESTING_CONFIGURATION` and does not appear in the controller's member list, even when it is in the same LAN as the controller.
- A member without `ip-address` gets an address from `ip-range` when it is authorized. The controller then shows the address in the member list.
- `/zerotier/print detail` shows the public identity. The `identity` property also holds the secret key of the instance: `/export` leaves it out, and `/export show-sensitive` includes it, together with the networks and members of the controller. Keep such exports private.

## Related pages

- [ZeroTier](zerotier): joining a network that ZeroTier Central or another controller manages, and the network requirements of ZeroTier.
- CLI reference: [`/zerotier`](../cli-reference/zerotier/), [`/zerotier/controller`](../cli-reference/zerotier/controller/), [`/zerotier/controller/member`](../cli-reference/zerotier/controller/member), [`/zerotier/interface`](../cli-reference/zerotier/interface).
