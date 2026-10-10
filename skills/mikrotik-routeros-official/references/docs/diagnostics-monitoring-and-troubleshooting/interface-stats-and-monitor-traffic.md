# Interface stats and monitor-traffic

> Interface statistics and real-time traffic monitoring on MikroTik RouterOS: print interface counters (stats, stats-detail), watch per-second rates with monitor-traffic, and run script triggers when a rate crosses a...

# Interface stats and monitor-traffic

Every RouterOS interface contains various counters, for example the number of received and transmitted packets, [Fast Path](../firewall-and-quality-of-service/packet-flow-in-routeros#fast-path) bytes, the number of link downs on the physical side, and packets dropped by the interface queue. These statistics give real-time visibility into network utilization and hardware performance; the `monitor-traffic` command shows a live per-second rate view for verifying throughput and troubleshooting bottlenecks.

## Inspect the counters

Print cumulative counters per interface with `stats` (or `stats-detail` for a per-interface list including link events):

```ros
[admin@MikroTik] > /interface/print stats
Flags: X - DISABLED; R - RUNNING; S - SLAVE
Columns: NAME, RX-BYTE, TX-BYTE, RX-PACKET, TX-PACKET, RX-DROP, TX-DROP,
         TX-QUEUE-DROP, RX-ERROR, TX-ERROR
#     NAME            RX-BYTE    TX-BYTE  RX-PACKET  TX-PACKET  R  T  T  R  T
0   S ether1                0          0          0          0        0
1  RS ether2       28 805 078  8 117 511    221 798     17 287        0
2   S ether3                0          0          0          0        0
3   S ether4                0          0          0          0        0
4   S ether5                0          0          0          0        0
```

The values starting with `fp` are Fast Path counters; `tx-queue-drop` counts the packets dropped by the [interface queue](../firewall-and-quality-of-service/queues/#interface-queue) (a congestion signal). `stats-detail` adds the link-up/down timestamps and the `link-downs` count, which are used to spot a flapping cable (when the number keeps rising, check the cable, SFP, or PoE; the interface-specific error counters live in the [Ethernet statistics](../wired-connections/ethernet#stats) menu):

```ros
[admin@MikroTik] > /interface/print stats-detail
Flags: X - DISABLED; R - RUNNING; S - SLAVE
 0   S name="ether1" link-downs=0 rx-byte=0 tx-byte=0 rx-packet=0 tx-packet=0
       tx-queue-drop=0 fp-rx-byte=0 fp-tx-byte=0 fp-rx-packet=0 fp-tx-packet=0
       fp-rps-drop=0

 1  RS name="ether2" last-link-up-time=2026-10-09 12:41:25 link-downs=0
       rx-byte=28 805 078 tx-byte=8 117 511 rx-packet=221 798 tx-packet=17 287
       tx-queue-drop=0 fp-rx-byte=27 917 886 fp-tx-byte=0 fp-rx-packet=221 798
       fp-tx-packet=0 fp-rps-drop=0
```

## Watch the live rate

`/interface/monitor-traffic` shows per-second rates for the chosen interfaces:

```ros
[admin@MikroTik] > /interface/monitor-traffic ether2 duration=3
                       name:   ether2
      rx-packets-per-second:       26
         rx-bits-per-second: 26.4kbps
   fp-rx-packets-per-second:       26
      fp-rx-bits-per-second: 25.6kbps
      tx-packets-per-second:        2
         tx-bits-per-second: 12.7kbps
   fp-tx-packets-per-second:        0
      fp-tx-bits-per-second:     0bps
  tx-queue-drops-per-second:        0
```

The view refreshes continuously until you stop it; use `duration` to bound it. Use it to verify a newly configured VLAN or bridge member passes traffic or that a WAN port does not pass more than it should. Pass several interfaces to compare them side by side, or `aggregate` to watch the router as a whole. Use [Torch](torch) for a per-connection breakdown when a single interface stays busy.

## Trigger a script on a rate threshold

The [`/tool/traffic-monitor`](../cli-reference/tool/traffic-monitor) menu runs a script when an interface's transmitted or received rate goes `above` a threshold, below it, or every poll (`always`):

```ros
/system/script/add name=rate-alert \
    source=":log info \"ether2 over threshold\""
/tool/traffic-monitor/add name=high-load interface=ether2 \
    traffic=received trigger=above threshold=100000000 \
    on-event=rate-alert
```

## Technical details

- The values starting with `fp` count the traffic that took the Fast Path (the streamlined CPU forwarding path). When regular counters grow much faster than the fp counters, the traffic instead takes the full CPU path (firewall processing and so on) — useful on busy routers.
- Interface drop/error counters (`rx-drop`, `tx-drop`, `rx-error`, `tx-error`) count the problems seen by the driver; `tx-queue-drop` belongs to the queueing system.
- `link-downs` counts only the physical link drops; a rising number with no link-down timestamps on a VLAN member usually points to a physical issue on the member's parent interface.

For all the counters and rate rows, see the [`/interface`](../cli-reference/interface) and [`/interface/monitor-traffic`](../cli-reference/interface/monitor-traffic) CLI references; the [Ethernet statistics](../wired-connections/ethernet#stats) menu adds hardware-level counters.
