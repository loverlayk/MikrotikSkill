# CAKE

> CAKE (Common Applications Kept Enhanced) is an advanced queue management algorithm for RouterOS that optimizes network traffic handling through bandwidth shaping, flow isolation, and RTT-based congestion control. It...

CAKE (Common Applications Kept Enhanced) is a shaping-capable queue discipline that combines COBALT active queue management, a deficit-mode shaper, DRR++ flow isolation, simplified DiffServ handling, and link-layer overhead compensation.

CAKE is designed to maintain fairness and minimize bufferbloat with practical defaults and little tuning.

## When to use CAKE

Use CAKE on a shared bottleneck where bulk transfers increase latency or one host can dominate the available capacity. Typical examples include an Internet connection shared by several clients, a slow uplink, or an asymmetric connection.

CAKE can:

- Keep latency low while the link is busy.
- Share capacity between hosts and between their individual connections.
- Shape for link-layer overhead.
- Apply a simple DiffServ policy.
- Filter redundant TCP acknowledgments on highly asymmetric links.

CAKE can control only traffic that passes through its queue. It cannot correct Wi-Fi interference, insufficient router CPU, or a queue elsewhere in the network unless its shaper is configured below that bottleneck's rate.

Use FQ-CoDel when you require per-flow fairness and active queue management with lower CPU use. Use CAKE when you also require per-host fairness, an integrated shaper with link-layer compensation, DiffServ handling, or ACK filtering.

## Basic configuration

CAKE is a queue type, not a complete traffic-matching rule. Creating a CAKE entry under `/queue/type` defines a reusable queue profile but does not process any traffic by itself. Assign that profile to a Simple Queue, Queue Tree, or Interface Queue. See the generated [`/queue/type` CLI reference](../../../cli-reference/queue/type) for the complete list of properties and accepted values.

The following example applies the same CAKE profile to both directions of a Simple Queue. HTB supplies the upload and download limits, so CAKE's internal shaper remains unlimited:

```ros
/queue/type
add name=cake-default kind=cake cake-bandwidth=0 cake-nat=yes

/queue/simple
add name=internet-cake target=192.168.88.0/24 max-limit=20M/100M queue=cake-default/cake-default
```

In `max-limit=20M/100M` and `queue=cake-default/cake-default`, the first value is upload and the second is download. Replace the target and rates with values appropriate for the network. FastTracked traffic bypasses this Simple Queue, so disable FastTrack for the traffic the queue must process.

:::note
Set `cake-bandwidth` only on queue types where `kind=cake`. It controls the shaper built into the CAKE qdisc.

Simple Queue and Queue Tree entries use HTB. Their `limit-at` (CIR) and `max-limit` (MIR) parameters control the rate at the HTB level. When you assign a CAKE queue type to one of these entries, CAKE operates as a leaf qdisc under HTB.

Leave `cake-bandwidth=0` when HTB should control the traffic rate. This value leaves CAKE's shaper unlimited, but CAKE continues to provide active queue management, flow isolation, and DiffServ handling. Set `cake-bandwidth` when CAKE should also shape the traffic. If you configure both `cake-bandwidth` and an HTB rate limit, traffic passes through both shapers.
:::

## Recommended starting points

| Use case | Recommended starting configuration |
| :-- | :-- |
| Simple Queue or Queue Tree provides the rate limit | Leave `cake-bandwidth=0` and set the HTB `max-limit`. CAKE provides active queue management and fairness without adding a second shaper. |
| CAKE provides the rate limit | Set `cake-bandwidth` below the real bottleneck rate and configure the correct link-layer overhead. Avoid a second HTB rate limit unless both shaping layers are intentional. |
| Router performs NAT | Set `cake-nat=yes` and keep the default `triple-isolate` flow mode. This lets one CAKE instance balance traffic between internal hosts and between their flows. |
| Download/upload ratio is greater than approximately 10:1 | Set `cake-ack-filter=filter` only on the transmit queue for the slower direction. |
| Ingress DSCP markings are not trusted | Set `cake-diffserv=besteffort` to ignore them, or set `cake-wash=yes` to clear them after CAKE applies its priority decision. |

### Direction and queue placement

A CAKE instance processes only the packets that pass through the queue where it is attached. It does not automatically process traffic in the reverse direction.

- **Interface Queue:** An interface queue processes packets transmitted by that interface. For forwarded client traffic, CAKE on the WAN-facing transmit interface processes uploads, while CAKE on the LAN-facing transmit interface processes downloads. These are two separate CAKE instances. An interface queue does not process packets received by that interface.
- **Simple Queue:** RouterOS determines upload and download relative to the configured target. The `queue` property selects the upload and download queue types in that order. Assign a CAKE queue type to both positions to process both directions.
- **Queue Tree:** Each Queue Tree is one-directional. Its parent and packet selection determine which traffic passes through its CAKE leaf queue.

Configure a separate CAKE queue type for each direction when the upload and download rates or options differ. If the LAN uses several outgoing interfaces, an Interface Queue attached to only one of them does not process traffic transmitted by the others. A single CAKE instance can balance many hosts and flows that pass through it. Create separate per-client queues only when you require explicit per-client rate limits or HTB guarantees.

The `cake-autorate-ingress` name refers to CAKE's capacity-estimation mode. It does not make an Interface Queue process packets received by the interface or create a reverse-direction queue. Linux examples that redirect WAN ingress to an Intermediate Functional Block (IFB) create a separate transmit queueing point; they are not RouterOS Interface Queue configuration instructions.

### Select the shaping rate

The shaper must become the bottleneck to control queue delay. Start below the stable measured throughput, not at the advertised service rate. Ingress shaping usually requires more headroom because the upstream sender and ISP queue are outside the router's control. With correct overhead compensation, egress shaping can operate closer to the measured link rate.

Validate the rate under simultaneous upload and download load while you measure latency. A throughput-only speed test does not show whether interactive traffic, voice, or other hosts remain responsive. Reduced throughput for one flow can be the expected result when CAKE shares capacity between hosts and flows.

:::warning
A shaped CAKE instance does not divide its packet processing across multiple CPU cores. CPU exhaustion can reduce throughput and increase latency even when other cores are idle. Test the required shaping rate on the target device. Unlimited CAKE requires substantially less processing than shaped CAKE.
:::

:::note
FastTracked traffic bypasses Simple Queues and Queue Trees with `parent=global`. Queue Trees parented directly to an interface can process FastTracked traffic. See [FastTrack](../../connection-tracking#fasttrack).
:::

## Overhead compensation

CAKE must know how much time each packet occupies on the bottleneck link. The packet size visible to CAKE might exclude framing, encapsulation, or inter-packet overhead. Without compensation, the configured shaper can send slightly faster than the real link and allow a queue to build elsewhere.

Prefer a `cake-overhead-scheme` that matches the bottleneck technology. A scheme sets the related overhead, minimum packet unit (MPU), and ATM or PTM compensation. Use manual values only when the encapsulation is known and no preset matches it.

| Scheme | Behavior |
| :-- | :-- |
| `raw` | Disables overhead compensation. Use it when the packet size visible to CAKE already represents the unit used by the bottleneck. |
| `convervative` | Deliberately overestimates unknown overhead. It is equivalent to 48 bytes of overhead with ATM compensation. RouterOS uses the spelling `convervative` for this value. |
| `ethernet` | Accounts for the Ethernet preamble, inter-frame gap, and frame check sequence. It is equivalent to 38 bytes of overhead, an MPU of 84 bytes, and no ATM or PTM compensation. |
| `via-ethernet` | Adjusts another scheme when CAKE receives a complete Ethernet frame instead of a raw IP packet. Use it only as a modifier with the applicable base scheme. |
| `ether-vlan` | Adds 4 bytes for an IEEE 802.1Q VLAN header. Combine it with the applicable base scheme. |
| `docsis` | Matches the Ethernet frame size used by DOCSIS head-end shaping and metering. It is equivalent to 18 bytes of overhead, an MPU of 64 bytes, and no ATM or PTM compensation. |
| ADSL schemes | Select `ipoa-vcmux`, `ipoa-llcsnap`, `bridged-vcmux`, `bridged-llcsnap`, `pppoa-vcmux`, `pppoa-llc`, `pppoe-vcmux`, or `pppoe-llcsnap` to match the encapsulation. These schemes include ATM cell compensation. |
| `pppoe-ptm` or `bridged-ptm` | Select the matching VDSL2 encapsulation. These schemes include PTM compensation. |

For manual configuration, `cake-overhead` accepts values from -64 to 256 bytes. `cake-mpu` accepts values from 0 to 256 bytes and cannot be negative. Set `cake-atm=atm` for ATM cell framing or `cake-atm=ptm` for PTM encoding.

## RTT Schemes

The CAKE queue discipline uses the round-trip time (RTT) to tune its active queue management parameters. Keep the default `internet` scheme unless the typical traffic RTT is known. A shorter scheme reacts more quickly, but a value below the actual path RTT can reduce the throughput of long-lived flows, especially on low-rate links. The setting does not need to match every flow exactly; actual RTTs within approximately one order of magnitude generally work well.

Use `metro` rather than `lan` for most local networks. The aggressive time constants of `lan` can signal congestion prematurely, reduce throughput, and leave too little queued traffic for the fairness logic. Reserve it for controlled, pure Ethernet networks; do not use it when shaping an Internet access link.

Here are the RTT settings you can use, what they mean, and when you might use them:

1. `cake-rtt`: Manually specifies the RTT, for example, `cake-rtt=100ms`.
2. `cake-rtt-scheme=datacentre`: Assumes an RTT of 100 microseconds. Use it only for extremely high-performance data-center networks.
3. `cake-rtt-scheme=lan`: Assumes an RTT of 1 millisecond. Use it only for controlled, pure Ethernet networks, not for an Internet access link.
4. `cake-rtt-scheme=metro`: Assumes an RTT of 10 milliseconds. Use it for most local networks or traffic within a single city.
5. `cake-rtt-scheme=regional`: Assumes an RTT of 30 milliseconds. Use it for traffic within a region or country.
6. `cake-rtt-scheme=internet`: Assumes an RTT of 100 milliseconds. This is suitable for typical Internet traffic.
7. `cake-rtt-scheme=oceanic`: Assumes an RTT of 300 milliseconds. Use it for Internet traffic with consistently above-average latency.
8. `cake-rtt-scheme=satellite`: Assumes an RTT of 1000 milliseconds. Use it for geostationary satellite paths.
9. `cake-rtt-scheme=interplanetary`: Assumes an RTT of 3600 seconds and almost completely disables Active Queue Management (AQM) actions. It is not intended for ordinary network configurations.

For satellite and other high-delay links, set the measured RTT when the preset does not match the path. The presets are starting points rather than measurements.

## Flow isolation

CAKE identifies flows by the source and destination addresses, transport protocol, and source and destination ports. It places flows into separate queues and schedules them fairly. Sparse, low-rate flows can then remain responsive when bulk flows use the same link.

- `cake-flowmode=triple-isolate`: Applies fairness between source hosts, destination hosts, and individual flows. This is the default and the recommended starting point for a typical gateway.
- `cake-flowmode=dual-srchost`: Applies fairness between source hosts, then between each host's flows. Use it when the source addresses identify the subscribers or devices to balance.
- `cake-flowmode=dual-dsthost`: Applies fairness between destination hosts, then between each host's flows. Use it when the destination addresses identify the subscribers or devices to balance.
- `cake-flowmode=srchost`: Applies fairness only between source addresses.
- `cake-flowmode=dsthost`: Applies fairness only between destination addresses.
- `cake-flowmode=hosts`: Applies fairness between source and destination host pairs.
- `cake-flowmode=flows`: Applies fairness only between complete five-tuple flows.
- `cake-flowmode=flowblind`: Disables flow isolation and places all traffic for each tin in one queue.

When the router performs NAT, set `cake-nat=yes` so CAKE can isolate the internal addresses and ports. Keep `triple-isolate` unless the topology requires a specific directional mode. The commonly copied combination of `dual-srchost` for upload and `dual-dsthost` for download is mainly useful when CAKE can already see the required host addresses without a NAT lookup. The NAT lookup has no effect when another device performs NAT or when hardware-offloaded traffic bypasses CAKE.

## ACK filter

ACK filtering removes redundant TCP acknowledgment packets before they consume capacity on a narrow transmit link. Start with `cake-ack-filter=filter`; use `cake-ack-filter=aggressive` only after testing shows that the additional filtering does not reduce TCP performance. Set `cake-ack-filter=none` to disable it.

Enable ACK filtering only on the transmit queue for the slower side of a highly asymmetric connection. It becomes relevant when the download/upload ratio exceeds approximately 10:1. Do not enable it on the receive queue: ACK packets normally do not accumulate there, and the filter consumes additional CPU.

ACK filtering cannot inspect ACK packets inside encrypted traffic, such as a WireGuard or IPsec tunnel. Apply it where the plain TCP ACK packets are visible.

## DiffServ

Differentiated Services (DiffServ) classifies packets by their Differentiated Services Code Point (DSCP) and places them into CAKE traffic classes called tins. CAKE applies soft priority between tins: every tin receives service and can borrow unused capacity. The percentage thresholds are not fixed bandwidth limits. For example, Best Effort can use 100% of the link when the other tins are idle.

- `cake-diffserv=diffserv3` (default): Provides Bulk (CS1 and LE), Best Effort (general traffic), and Voice (CS7, CS6, EF, VA, and TOS4) tins. Their thresholds are 6.25%, 100%, and 25%. Voice uses a shorter CoDel interval.
- `cake-diffserv=diffserv4`: Provides Bulk (CS1 and LE), Best Effort (general traffic), Video (AF4x, AF3x, CS3, AF2x, CS2, TOS4, and TOS1), and Voice (CS7, CS6, EF, VA, CS5, and CS4) tins. Their thresholds are 6.25%, 100%, 50%, and 25%.
- `cake-diffserv=diffserv8`: Provides eight tins for networks with a deliberate, detailed DSCP policy.
- `cake-diffserv=besteffort`: Disables priority queuing and places all traffic in one tin. Use this when DSCP markings are absent or must not affect scheduling.
- `cake-diffserv=precedence`: Uses the legacy IP precedence interpretation. Avoid this mode on new configurations.

CAKE does not create trustworthy classifications by itself. Use the DiffServ modes only when you trust the received DSCP markings or set them with a consistent local policy. Incorrect high-priority markings can give traffic unintended service.

## Wash

The `cake-wash=yes` option clears DSCP markings after CAKE uses them for its priority decision. It does not clear Explicit Congestion Notification (ECN) bits.

Enable `cake-wash=yes` at a DiffServ domain boundary when the next network must not inherit the existing DSCP policy. If inbound markings are not trusted and should not affect scheduling, use `cake-diffserv=besteffort`; adding `cake-wash=yes` also clears those markings before forwarding the packets.

## Autorate ingress

The `cake-autorate-ingress` option estimates capacity from the arrival times of ingress packets and adjusts CAKE's internal shaper. An optional `cake-bandwidth` value supplies its initial estimate.

The estimator observes only traffic arriving at this CAKE instance. It cannot measure a bottleneck farther downstream, and it must receive enough traffic before it can increase its estimate. Links with large or rapid capacity changes, such as LTE and 5G, can therefore produce unstable or unexpectedly low rates.

:::warning
Test `cake-autorate-ingress` on the actual link before production use. It is CAKE's built-in estimator and is not the same as external adaptive-rate implementations that continuously measure delay and update the shaper. Use a fixed rate below the reliable link capacity when predictable latency and throughput are more important than following every capacity change.
:::

Do not enable `cake-autorate-ingress` when HTB is intended to control the rate. The option changes CAKE's shaper, not the HTB `max-limit`.
