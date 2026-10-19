# GRE

> Generic Routing Encapsulation (GRE) is a tunneling protocol that encapsulates IP over IP as a virtual point-to-point link in RouterOS, with keepalive monitoring, MTU and MSS handling, DSCP settings and an optional...

# GRE

Generic Routing Encapsulation (GRE) is a tunneling protocol originally developed by Cisco to encapsulate a wide variety of network layer protocols over an IP network. It creates a virtual point-to-point link between tunnel endpoints, allowing different protocol traffic to be carried across routed infrastructure.

In RouterOS, GRE is implemented as virtual interfaces in the [`/interface/gre`](../cli-reference/interface/gre) (over IPv4) and [`/interface/gre6`](../cli-reference/interface/gre6) (over IPv6) menus. The interfaces are routed (Layer 3) tunnels: a GRE tunnel carries only IP and IPv6 packets between the two endpoints. For Layer 2 connectivity over an IP network (bridging Ethernet frames), use [EoIP](./eoip) instead.

## How the tunnel works

GRE is a stateless tunnel, similar in behavior to [IPIP](./ipip) and EoIP. No session state is maintained between the endpoints: the router keeps forwarding packets toward the remote endpoint even if it becomes unreachable, and the tunneled traffic is dropped until connectivity is restored or the tunnel is reconfigured.

The router considers the tunnel **running** (the `R` flag) after the remote end has responded at least once. Keepalive monitors the remote end from then on: the router sends GRE echo probes to the remote-address every keepalive interval and answers the remote end's probes while the tunnel is up. Keepalive is enabled by default (`10s,10` — interval 10 seconds, 10 retries) and the interval can be as short as 1 second for faster detection (a 0-second setting is rejected). On current RouterOS the running flag is kept while the tunnel is enabled — a tunnel whose remote end is unreachable stays running and the tunneled traffic is dropped until the remote end answers again. If an automated failover must react to a dead tunnel, add a reachability check (for example a script that pings the remote end and adjusts the routes) instead of relying on the running flag.

:::tip
A GRE tunnel adds per-packet overhead: over IPv4 24 bytes (4-byte GRE header + 20-byte IP header), over IPv6 44 bytes (4-byte GRE header + 40-byte IPv6 header). With the default `mtu=auto` the router sets the tunnel MTU accordingly — `actual-mtu` is 1476 on a 1500-byte interface for GRE over IPv4 and 1456 for GRE over IPv6. The tunnel carries only IP and IPv6 packets (EtherType 0x0800 and 0x86DD). Do not use the "Check gateway" option `arp` when a GRE tunnel is used as a route gateway.
:::

All GRE properties are described in the [`/interface/gre`](../cli-reference/interface/gre) and [`/interface/gre6`](../cli-reference/interface/gre6) CLI references.

## Example: connect two sites

The example connects two sites over the internet with a GRE tunnel and gives each site Layer 3 access to the other site's local network.

![GRE tunnel between two sites](./img/gre-01.webp)

**Site1** has the local network **10.1.101.0/24**, **Site2** the local network **10.1.202.0/24**. The tunnel endpoints are the routers' public addresses, here **192.168.80.1** (Site1) and **192.168.90.1** (Site2) — substitute your routers' own internet addresses.

Create the tunnel on the Site1 router:

```ros
/interface/gre/add name=myGre \
    remote-address=192.168.90.1 local-address=192.168.80.1
```

And on the Site2 router:

```ros
/interface/gre/add name=myGre \
    remote-address=192.168.80.1 local-address=192.168.90.1
```

:::note
The example leaves keepalive at its default (`10s,10`). The tunnel shows the running flag after the remote end has answered. GRE is stateless: if one end becomes unreachable, the running flag stays and traffic into the tunnel is dropped until the remote end is reachable again.
:::

Both ends now have a tunnel, but need addresses to route over it. Give the tunnel ends addresses from a private range, and add routes to the remote site's local network. On the Site1 router:

```ros
/ip/address/add address=172.16.1.1/30 interface=myGre
/ip/route/add dst-address=10.1.202.0/24 gateway=172.16.1.2
```

On the Site2 router:

```ros
/ip/address/add address=172.16.1.2/30 interface=myGre
/ip/route/add dst-address=10.1.101.0/24 gateway=172.16.1.1
```

At this point both sites have Layer 3 connectivity over the GRE tunnel. Verify it end to end — the ping to the far tunnel address must be answered and the tunnel must show the `R` flag on both sites:

```ros
/ping 172.16.1.2
/interface/gre/print where name=myGre
```

## Troubleshooting

- **The tunnel has no running flag.** The remote end has not answered yet. Check with `/ping <remote-address>` that the tunnel endpoint is reachable, that the remote router has a matching tunnel with `remote-address` pointing back, and that the tunnel has `local-address` set correctly. The running flag appears only after the remote end responds.
- **Traffic through the tunnel is lost.** GRE is stateless: when the remote end is unreachable, the router keeps sending tunneled traffic into the tunnel and it is dropped. Check the reachability of `remote-address`, and compare the tunnel's `actual-mtu` against the path MTU between the sites (an MTU mismatch drops oversized packets).
- **The tunnel is up but no traffic passes between the sites.** The WAN firewalls between the sites must allow GRE (IP protocol 47) between the two tunnel endpoints — and the IPsec ports if the tunnel has an `ipsec-secret` — and the tunneled traffic must not be NATed.
- **The remote end's address changed.** `remote-address` takes an IP address, not a hostname; if a site's public address changes, update the tunnel on the other end or use an endpoint with a stable address.
- **Non-IP traffic does not go through.** GRE is a routed tunnel and carries only IP and IPv6 packets. To bridge Ethernet frames over an IP network, use [EoIP](./eoip).
