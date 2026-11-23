# Failover (WAN Backup)

> WAN failover in RouterOS: use a second internet link when the first one fails, check the link with check-gateway, detect a failure behind the provider's gateway with recursive routes, and see which link is in use.

# Failover (WAN Backup)

A router with two internet links can use the second link when the first one fails. This page shows two ways to do it with routes only:

- Check the gateway of each provider. This is simple, but it does not see a failure inside the network of the provider.
- Check hosts on the internet through each link, with recursive routes. This also sees a failure behind the gateway.

![A router with a LAN and two links to two internet providers](./img/failover-wan-backup-01.webp)

In the examples, the first provider (ISP1) is on `ether1` with the gateway 10.111.0.1, and the second (ISP2) is on `ether2` with the gateway 10.112.0.1. ISP1 is the main link.

## Prepare NAT

The devices of the LAN must reach the internet through both links, so each WAN interface needs a masquerade rule:

```ros
/ip/firewall/nat
add chain=srcnat action=masquerade out-interface=ether1
add chain=srcnat action=masquerade out-interface=ether2
```

With the default configuration, the masquerade rule uses the interface list `WAN`, and the two rules are not needed. Take the second WAN port out of the LAN bridge and add it to the list. The default firewall then also protects it. Without this, the traffic through the second link is not translated and gets no answers:

```ros
/interface/bridge/port/remove [find interface=ether2]
/interface/list/member/add list=WAN interface=ether2
```

The routes of this page are static and need the address of each gateway. If a link gets its settings from a DHCP or PPPoE client, set `add-default-route=no` in the client, so that its own default route does not compete with the routes of this page.

## Check the gateways

Add a default route for each link. The route with the lower `distance` is used while it is active:

```ros
/ip/route
add distance=1 gateway=10.111.0.1 check-gateway=ping
add distance=2 gateway=10.112.0.1 check-gateway=ping
```

With `check-gateway=ping`, the router pings the gateway of the route. When the gateway does not answer, the route becomes inactive, and the route with the next distance takes over. When the gateway answers again, the first route becomes active again. [Routing decision](../../user-guides/routing-and-networking-protocols/routing-decision) describes the timing of the check.

In `/ip/route/print`, the route of ISP1 has the flag `A` (active). After the gateway of ISP1 stops answering, this route gets the flag `I` (inactive) and the route of ISP2 becomes active. This takes about 20 seconds with the default timing of the check.

An answer from the gateway shows only that the link between the router and the gateway works. The gateway can answer while the provider has no connection to the internet, and then the router keeps using a link that does not work.

## Check hosts on the internet

To check the path to the internet, ping a host on the internet through each link. Choose two reliable hosts that answer pings, one for each link. This example uses the public DNS servers 8.8.8.8 and 8.8.4.4.

First add a route to each host through its link. Then add the default routes with the hosts as gateways:

```ros
/ip/route
add dst-address=8.8.8.8 scope=10 gateway=10.111.0.1
add dst-address=8.8.4.4 scope=10 gateway=10.112.0.1
add distance=1 gateway=8.8.8.8 target-scope=11 check-gateway=ping
add distance=2 gateway=8.8.4.4 target-scope=11 check-gateway=ping
```

These are recursive routes: the gateway of a default route is not directly connected, and the router finds the way to it through another route. `scope` and `target-scope` control which routes can be used for this: a route can resolve its gateway through routes whose `scope` is not greater than its `target-scope`. The host routes have `scope=10`, and the default routes have `target-scope=11`.

The detail output shows the real next hop of each default route in `immediate-gw`:

```ros
[admin@Router] > /ip/route/print detail where dst-address=0.0.0.0/0
Flags: A - ACTIVE; s - STATIC
2 As dst-address=0.0.0.0/0 routing-table=main gateway=198.51.100.1
     immediate-gw=10.111.0.1%ether2 check-gateway=ping distance=1 scope=30
     target-scope=11
 
3  s dst-address=0.0.0.0/0 routing-table=main gateway=198.51.100.2
     immediate-gw=10.112.0.1%ether3 check-gateway=ping distance=2 scope=30
     target-scope=11
```

This output is from a test network, where the hosts are 198.51.100.1 and 198.51.100.2 and the WAN interfaces are `ether2` and `ether3`.

- When the host of ISP1 stops answering, the first default route becomes inactive within about half a minute and the traffic uses ISP2, also when the gateway of ISP1 still answers. When the host answers again, the route becomes active again.
- The host routes are necessary. Without them, both default routes are inactive.
- Each host is reachable only through its own link. Do not use an address that your network needs through the other link, for example the DNS server that the LAN uses.

## Check two hosts for each link

With one host for each link, a failure of that host alone switches the traffic to the backup link. To avoid this, add a second host for each link, here 208.67.222.222 and 208.67.220.220:

```ros
/ip/route
add dst-address=208.67.222.222 scope=10 gateway=10.111.0.1
add dst-address=208.67.220.220 scope=10 gateway=10.112.0.1
add distance=1 gateway=208.67.222.222 target-scope=11 \
    check-gateway=ping
add distance=2 gateway=208.67.220.220 target-scope=11 \
    check-gateway=ping
```

ISP1 now has two default routes with the distance 1. While both hosts answer, the two routes are one ECMP route (flag `+`). When one host stops answering, the other route of ISP1 stays active. The traffic moves to ISP2 only when both hosts of ISP1 do not answer.

## What happens to open connections

A connection that is open when the route changes can break. The devices open it again. New connections use the link of the active route.

To use both links at the same time, see [Per connection classifier](per-connection-classifier).

## Read more

- [`/ip/route`](../../cli-reference/ip/route)
- [Routing decision](../../user-guides/routing-and-networking-protocols/routing-decision)
- [Load Balancing](./)
- [Per connection classifier](per-connection-classifier)
