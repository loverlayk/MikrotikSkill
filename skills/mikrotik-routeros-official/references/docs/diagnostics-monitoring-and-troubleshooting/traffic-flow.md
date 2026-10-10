# Traffic Flow

> Traffic-Flow exports statistics about the flows of packets passing through the router in Cisco NetFlow (v1/v5/v9) or IPFIX formats to a collector: enable the service, pick interfaces and timeouts, add targets, verify...

# Traffic Flow

MikroTik Traffic-Flow provides statistical information about packets that pass through the router. Besides network monitoring and accounting, system administrators can identify various problems that occur in the network, and analyze and optimize overall network performance. Traffic-Flow is compatible with Cisco NetFlow, so utilities designed for NetFlow work with it.

Traffic Flow only processes traffic that passes through the router's CPU. HW-offloaded traffic (for example, HW-offloaded bridged traffic between switch-chip ports) never shows up in Traffic Flow.

Supported export formats:

- **version 1** - The original NetFlow format. Basic information about IP packets flowing through a router, lacking support for different types of protocols and Type of Service (ToS).
- **version 5** - An enhancement over version 1, supporting Type of Service (ToS), TCP flags and autonomous-system information. RouterOS does not fill BGP AS numbers.
- **version 9** - Template-based export format with support for new record types; exports IPv4 and IPv6 flow information.
- **IPFIX** - The IETF-standardized protocol based on NetFlow version 9, with more customizable flow records; supports newer fields like multicast.

## Enable Traffic Flow and choose interfaces

Enable the service in [`/ip/traffic-flow`](../../cli-reference/ip/traffic-flow):

```ros
[admin@MikroTik] > /ip/traffic-flow/set enabled=yes
[admin@MikroTik] > /ip/traffic-flow/print
                enabled: yes
             interfaces: all
          cache-entries: 256k
    active-flow-timeout: 30m
  inactive-flow-timeout: 15s
        packet-sampling: no
      sampling-interval: 0
         sampling-space: 0
```

The `cache-entries` default depends on the device's memory (256k on larger boards, 4k on the smallest). `active-flow-timeout` and `inactive-flow-timeout` decide when a flow is expired and exported (see the [parameter descriptions](../../cli-reference/ip/traffic-flow)).

### Packet sampling

Packet sampling only accounts for a selection of packets:

```ros
/ip/traffic-flow/set packet-sampling=yes sampling-interval=2222 \
    sampling-space=1111
```

2222 consecutive packets are sampled, then 1111 are omitted, and the cycle repeats.

## Add export targets

Add the hosts that receive flow data in [`/ip/traffic-flow/target`](../../cli-reference/ip/traffic-flow/target):

```ros
[admin@MikroTik] > /ip/traffic-flow/target/add dst-address=192.168.0.2 \
    port=2055 version=9
[admin@MikroTik] > /ip/traffic-flow/target/print
Columns: SRC-ADDRESS, DST-ADDRESS, PORT, VERSION
# SRC-ADDRESS  DST-ADDRESS  PORT  VERSION
0 0.0.0.0      192.168.0.2  2055  9
```

`src-address=0.0.0.0` means the router picks the source address of the outgoing interface automatically. The export goes out over UDP (default port 2055) in the chosen format, for example NetFlow version 9 here.

## Watch the flow counters

The `/ip/traffic-flow/monitor` command shows the state of the flow cache (live-updating; stops after `duration`):

```ros
[admin@MikroTik] > /ip/traffic-flow/monitor duration=3
    finished-flows: 0
      active-flows: 8
  unmanaged-packets: 0
    unmanaged-bytes: 0
```

If the collector receives nothing, check that the flows appear here: `active-flows` climbs as the router routes traffic, and `finished-flows` starts climbing once the flows expire and get exported (default `inactive-flow-timeout` is 15s after the last packet of the flow). Check the target entry and that the traffic you watch is actually CPU-routed (not hardware-offloaded).

## Choose exported fields for IPFIX

The [`/ip/traffic-flow/ipfix`](../../cli-reference/ip/traffic-flow/ipfix) menu selects which fields appear in IPFIX flow records: addresses, ports, protocols, flags, interfaces, timing (for example `sys-init-time`, `first-forwarded`, `last-forwarded`), NAT addresses and ports and more — all rows listed in the [CLI reference](../../cli-reference/ip/traffic-flow/ipfix).

All fields are on by default; drop the ones you do not want with `set`:

```ros
[admin@MikroTik] > /ip/traffic-flow/ipfix/set gateway=no tcp-flags=no
```

## Notes

Traffic flow records flows at the end of the input, forward and output chain stacks of the [packet flow](../../firewall-and-quality-of-service/packet-flow-in-routeros) diagram, so only traffic that reaches one of those chains is counted.

Because of that, a mirror port on a switch connected to the router cannot be used to count mirrored packets: mirrored frames are dropped before they reach the input chain.

Other interfaces appear in the report if traffic passes through them and the monitoring interface.

## Minimal end-to-end example

A setup from scratch on one router, exporting NetFlow v9 to a collector on 192.168.0.2:

```ros
/ip/traffic-flow/set enabled=yes
/ip/traffic-flow/target/add dst-address=192.168.0.2 port=2055 version=9
```

The router starts sending export packets with the flow information; watch with `/ip/traffic-flow/monitor`.

:::info
To use ntop-ng with MikroTik you need to use Nprobe, which is paid software.
:::

### See more

- [NetFlow Fundamentals](https://etutorials.org/Networking/network+management/Part+II+Implementations+on+the+Cisco+Devices/Chapter+7.+NetFlow/Fundamentals+of+NetFlow/)
- [Traffic flow with Ntop on MikroTik](https://github.com/ntop/ntopng/issues/1575)

## Related topics

<DocCardList />
