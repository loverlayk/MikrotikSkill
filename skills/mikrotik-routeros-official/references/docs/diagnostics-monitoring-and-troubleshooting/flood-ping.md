# Flood Ping

> Flood ping sends a series of up to 1000 ICMP echo requests in one run and shows only the totals: requests sent, replies received and the shortest, average and longest round-trip time. It needs the traffic-gen...

# Flood Ping

Flood ping sends a series of ICMP echo requests to one host and, instead of a line for every reply as [ping](ping) prints, shows only the totals: how many requests it sent, how many replies came back, and the shortest, average and longest round-trip time. Use it to check a link for packet loss with many requests, for example a wireless link or a VPN tunnel. It works with IPv4 and IPv6 addresses and is not available on devices with the SMIPS architecture.

Flood ping loads the link and the target, so use it only on links and hosts that you manage.

## Enable flood ping

Flood ping belongs to the `traffic-gen` feature of [device mode](../system-information-and-utilities/device-mode), which is off in every device mode. On a router where it is off, the command fails with `failure: not allowed by device-mode`. To turn it on, run the update and confirm it on the router itself within the time the router shows, by pressing the reset or mode button or by turning the power off and on. The router then reboots. The [device mode](../system-information-and-utilities/device-mode) page describes the confirmation and its limits:

```ros
/system/device-mode/update traffic-gen=yes
```

## Test a link for packet loss

To send 1000 requests with `size=1400` to the far end of a link:

```ros
/tool/flood-ping address=10.0.0.2 count=1000 size=1400
```

When the run ends, the router shows the totals: `sent` and `received` requests, and `min-rtt`, `avg-rtt` and `max-rtt`, the round-trip times. A difference between `sent` and `received` is packet loss, on the link or at the target: many hosts limit how many ICMP requests they answer, so test against a device you know does not. To find an MTU problem on the path, use [ping with `do-not-fragment`](ping#find-the-path-mtu) instead: flood ping has no such option.

For an IPv6 host, give the IPv6 address:

```ros
/tool/flood-ping address=2001:db8::2 count=500
```

## Limits

- `count` - Up to 1000 requests per run.
- `size` - Size of each request, 10 to 1500.
- `timeout` - How long to wait for each reply, 10 ms to 5 s.
- `interval` - Time between requests, 20 ms to 5 s.

For more requests, a longer test, or options such as a source address or a VRF, use [ping](ping) with `count` and `interval`.

For all parameters, see the [`/tool/flood-ping` CLI reference](../cli-reference/tool/flood-ping).
