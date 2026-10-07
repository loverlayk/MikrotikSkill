# Detect Internet

> Detect Internet gives each watched interface a state (lan, wan, internet and others) from its link, its routes and MikroTik cloud reachability, and keeps interface lists up to date with the result.

# Detect Internet

Detect Internet watches the interfaces in `detect-interface-list` and gives each one a state: whether it has a link, whether the router's route to the internet goes through it, and whether MikroTik's cloud server answers through it. It adds each interface to the LAN, WAN or internet interface list you name, so settings and scripts that use those lists follow the current state of the interfaces.

Detect Internet is off by default (`detect-interface-list=none`), and the hAP ax² default configuration does not turn it on. While it runs, the router contacts `cloud.mikrotik.com` on UDP port 30000 to check the internet state, see [Communication with MikroTik Cloud Services](../network-management/cloud/communication-mikrotik-cloud-servers).

:::note
Detect Internet changes the members of the interface lists by itself. Rules and settings that use these lists change their effect whenever an interface changes its state.
:::

## See which interface has internet

Create a list for the interfaces with internet, and watch all interfaces:

```ros
/interface/list/add name=internet
/interface/detect-internet/set detect-interface-list=all \
    internet-interface-list=internet
```

The state of each interface shows in the `state` menu:

```ros
[admin@MikroTik] > /interface/detect-internet/state/print
Columns: NAME, STATE, STATE-CHANGE-TIME, CLOUD-RTT
#  NAME    STATE     STATE-CHANGE-TIME    CLOUD-RTT
0  lo      lan       2026-10-01 13:48:56
1  ether1  no-link   2026-10-01 13:48:56
2  ether2  slave     2026-10-01 13:48:56
3  ether3  slave     2026-10-01 13:48:56
4  ether4  slave     2026-10-01 13:48:56
5  ether5  slave     2026-10-01 13:48:56
6  wifi1   slave     2026-10-01 13:48:56
7  wifi2   slave     2026-10-01 13:48:56
8  bridge  internet  2026-10-01 13:49:02  12ms
```

This router gets its internet from another router on its LAN, so its `bridge` has the internet state. On a typical home router, the internet state goes to the interface with the default route, for example `ether1`. Ports of the bridge show as `slave`, and `ether1` has no cable here (`no-link`). `lo` is the router's loopback interface, shown as `lan`.

The interface with the internet state is a dynamic member of the `internet` list:

```ros
[admin@MikroTik] > /interface/list/member/print where list=internet
Flags: D - DYNAMIC
Columns: LIST, INTERFACE
#   LIST      INTERFACE
;;; INTERNET detected
0 D internet  bridge
```

## Use the lists with care

The lists change on their own: an interface leaves the `internet` or `wan` list when its state changes, and every interface is `lan` again after a link change. Do not use these lists for trust decisions, for example in firewall rules that accept traffic, and do not set them to the `LAN` and `WAN` lists of the default configuration. They fit informational use, for example in scripts that report which line has the internet.

Set `lan-interface-list` and `wan-interface-list` to fill lists for the other states in the same way.

## How the states work

| State | Meaning |
| :-- | :-- |
| `no-link` | The interface has no link. |
| `slave` | The interface is a port of a bridge or another interface, for example a bridge port or a Wi-Fi interface in a bridge. |
| `lan` | The start state of layer 2 interfaces, and the state again after a link change. |
| `unknown` | The router is checking the interface. It lasts about 6 seconds. |
| `wan` | The router's active route to 8.8.8.8 goes through the interface. Layer 3 tunnels, such as IPIP, become `wan` when their link comes up. |
| `internet` | A `wan` interface through which the router reaches `cloud.mikrotik.com` on UDP port 30000. The router's route to the cloud server must go through this interface. |

The router checks an interface again after a link change, a route change or a change of the Detect Internet settings. These rules decide what can change:

- An interface that has stayed `lan` for an hour is locked. It changes only after a link change, also when a route to 8.8.8.8 goes through it later.
- A `wan` interface goes back to `lan` only after a link change.
- An `internet` interface falls back to `wan` when the cloud server stops answering (after about 4 minutes with the default `request-interval`), or when the route to the cloud server no longer goes through the interface. When the server answers again, the interface gets the `internet` state back.
- With two equal-cost routes to 8.8.8.8 through different interfaces, neither interface becomes `wan`.

A link change means that the link of the interface goes down and comes up again, for example when a cable is unplugged and plugged in, or when the interface is disabled and enabled.

:::note
Detect Internet shows which interface the router's active route uses, not the health of every line. A backup line whose route is not active stays `lan`, and after an hour it is locked, so Detect Internet is not a health check for failover. A /32 route to 8.8.8.8 through one line, which some failover setups use, keeps the `wan` state on that line. To check backup lines, use routes with `check-gateway` (see [Failover (WAN backup)](../high-availability-solutions/load-balancing/failover-wan-backup)) or [Netwatch](netwatch).
:::

Each state change is logged with the topic `interface`, for example `ether1 detect WAN`.

## Troubleshoot

When every interface stays `lan`:

- Check that the router's active route to the internet goes through the interface:

  ```ros
  /ip/route/print where active and dst-address=0.0.0.0/0
  ```

- An interface that stayed `lan` for an hour is locked. Disable and enable it, or unplug and plug in its cable, so that the router checks it again.
- With two equal-cost routes to 8.8.8.8 through different interfaces, neither becomes `wan`.

When an interface is `wan` but never `internet`, check that the router's route to `cloud.mikrotik.com` goes through that interface, and that UDP port 30000 to the cloud server is not blocked on the way.

## Technical details

### Cloud check

For a `wan` interface, the router sends a 32-byte UDP message to `cloud.mikrotik.com` port 30000, and the server sends it back. The router sends the message at half of `request-interval`, so about every minute with the default of 2 minutes. `request-interval` takes values from 1 minute to 1 day. `CLOUD-RTT` in the `state` menu shows the round-trip time of the last answer.

### Dynamic list members

Each dynamic member of a list gets a comment with the state that added it: `LAN detected`, `WAN detected` or `INTERNET detected`.

### Settings changes

A change of the Detect Internet settings checks all watched interfaces again. Each interface shows `unknown` for a few seconds and then its state.

## Turn it off

Stop watching the interfaces:

```ros
/interface/detect-internet/set detect-interface-list=none
```

This also removes the dynamic members from the lists. With no interfaces to watch, Detect Internet no longer contacts the cloud server.

For all parameters, see the CLI reference for [`/interface/detect-internet`](../cli-reference/interface/detect-internet/) and [`/interface/detect-internet/state`](../cli-reference/interface/detect-internet/state).
