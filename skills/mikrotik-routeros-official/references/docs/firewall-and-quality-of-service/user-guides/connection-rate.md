# Connection rate

> Connection Rate is a MikroTik RouterOS firewall feature that monitors and filters traffic based on connection speed, using 'connection-bytes' and 'connection-rate' to detect high-speed connections for prioritization...

# Connection rate

Connection rate is a firewall matcher that selects packets by the present speed of their connection. Together with the `connection-bytes` matcher it finds the connections that transfer a lot of data at a high rate, for example to give them a lower priority.

## How it works

Each entry in the [connection tracking](../connection-tracking) table represents bidirectional communication. Every time a packet is associated with an entry, the size of the packet (including the IP header) is added to the byte counter of the entry. The `connection-bytes` matcher compares this counter, so it includes both directions, upload and download.

The `connection-rate` matcher compares the present rate of the connection, in bits per second. It is the rate of both directions together. The connection table shows the rate of each direction as `orig-rate` and `repl-rate` in `/ip/firewall/connection/print detail`.

Both matchers take a range:

- `connection-rate=From-To`, for example `connection-rate=0-100k`. The values are from 0 to 4294967295, and the `k` and `M` suffixes are accepted. `!` before the range inverts the match.
- `connection-bytes=From-To`, for example `connection-bytes=500000-0`.

In both matchers, `0` as the second value means no upper limit.

### Rule example

These rules count the TCP and UDP packets that go through the router and belong to a connection with a rate below 100 kbit/s:

```ros
/ip/firewall/mangle
add chain=forward action=passthrough protocol=tcp \
    connection-rate=0-100k comment="slow TCP"
add chain=forward action=passthrough protocol=udp \
    connection-rate=0-100k comment="slow UDP"
```

`/ip/firewall/mangle/print stats` shows the counters of the rules.

## Application example: traffic prioritization

A common use of the connection rate is to detect heavy connections and give them a lower priority. Heavy connections keep a fast rate for a long time, for example downloads. All other traffic, which usually includes VoIP, web browsing and online gaming, then gets priority.

The method of this example can be used together with other ways to detect and prioritize traffic. `connection-rate` alone also matches a short peak, so the example needs a margin that identifies heavy connections. If a normal web browsing connection is shorter than 500 kB (4 Mb) and VoIP needs no more than 200 kbit/s, then every connection that still has more than 200 kbit/s after its first 500 kB can be assumed to be heavy.

Your network can have other values of `connection-bytes` for web browsing and of `connection-rate` for VoIP. Measure them before you use this example.

The example assumes a 6 Mbit/s upload and download connection to the ISP. For another connection, set `max-limit` of the `upload` and `download` queues to its rate and keep the sum of the two `limit-at` values of each direction within `max-limit`. The rules mark IPv4 traffic. `ether1` is the WAN interface and `bridge` is the LAN interface, as in the default configuration.

:::warning
The queues of this example select traffic by packet marks. Mangle rules do not process FastTracked packets, and the default configuration FastTracks established connections. This example marks every forwarded connection, so disable the FastTrack rule first, see [Before you start: FastTrack](../queues/simple-queue#before-you-start-fasttrack).
:::

### Mark the connections and packets

The mangle rules separate all connections into two groups and then mark the packets of each group. The traffic is client traffic, so the rules are in the forward chain.

When a heavy connection has a lower priority and the queue reaches its `max-limit`, the heavy connection slows down, and its connection rate becomes lower. A rule that looks only at the rate then moves the connection back to the higher priority, the connection gets more traffic for a short while, its rate rises, and the priority changes again. To avoid this, a connection that is detected as heavy keeps its mark.

```ros
/ip/firewall/mangle
add chain=forward action=mark-connection \
    new-connection-mark=all_conn connection-mark=no-mark
add chain=forward action=mark-connection protocol=tcp \
    new-connection-mark=heavy_traffic_conn connection-mark=all_conn \
    connection-bytes=500000-0 connection-rate=200k-0
add chain=forward action=mark-connection protocol=udp \
    new-connection-mark=heavy_traffic_conn connection-mark=all_conn \
    connection-bytes=500000-0 connection-rate=200k-0
add chain=forward action=mark-packet new-packet-mark=heavy_traffic \
    connection-mark=heavy_traffic_conn passthrough=no
add chain=forward action=mark-packet new-packet-mark=other_traffic \
    connection-mark=all_conn passthrough=no
```

- The first rule marks every connection that has no connection mark yet with `all_conn`. A connection that is marked as heavy keeps its mark, because the rule matches only `no-mark`.
- The second and third rules mark the heavy TCP and UDP connections: a connection with the `all_conn` mark that has transferred more than 500 kB and has a rate above 200 kbit/s. Connections of other protocols stay in the `all_conn` group.
- The last two rules mark the packets of the two groups.

### Queue the traffic

The queue tree is attached to the interfaces. The `other` queues have the higher priority and a guaranteed 4 Mbit/s, and the `heavy` queues are guaranteed 2 Mbit/s. See [HTB](../queues/htb-hierarchical-token-bucket) for `limit-at`, `max-limit` and `priority`.

```ros
/queue/tree
add name=upload parent=ether1 max-limit=6M
add name=other_upload parent=upload packet-mark=other_traffic \
    limit-at=4M max-limit=6M priority=1
add name=heavy_upload parent=upload packet-mark=heavy_traffic \
    limit-at=2M max-limit=6M priority=8
add name=download parent=bridge max-limit=6M
add name=other_download parent=download packet-mark=other_traffic \
    limit-at=4M max-limit=6M priority=1
add name=heavy_download parent=download packet-mark=heavy_traffic \
    limit-at=2M max-limit=6M priority=8
```

If the router has more than one WAN or more than one LAN interface, mark upload and download with different packet marks and attach the queues to `parent=global`, see [Queue tree](../queues/queue-tree).

### Check that it works

Start a large upload from a LAN device. After its first 500 kB, the connection has the `heavy_traffic_conn` mark:

```ros
[admin@MikroTik] > /ip/firewall/connection/print where connection-mark=heavy_traffic_conn
Flags: S - SEEN-REPLY; A - ASSURED; C - CONFIRMED; s - SRCNAT
Columns: PROTOCOL, SRC-ADDRESS, SRC-PORT, DST-ADDRESS, DST-PORT, TCP-STATE, 
         TIMEOUT, ORIG-RATE
#      PRO  SRC-ADDRESS     SRC-P  DST-ADDR  DST-  TCP-STATE    TIMEO  ORIG-RA
0 SACs tcp  192.168.88.101  46326  11.0.0.2  2000  established  4m59s  5.8Mbps
```

The queue statistics show the `rate` of each queue in bits per second. The upload goes through `heavy_upload`. Other traffic, in this output a 100 kbit/s stream, goes through `other_upload`:

```ros
[admin@MikroTik] > /queue/tree/print stats proplist=name,rate,dropped
0  name="upload" rate=5629904 dropped=0

1  name="other_upload" rate=101072 dropped=1403

2  name="heavy_upload" rate=5528832 dropped=1922

3  name="download" rate=34576 dropped=0

4  name="other_download" rate=1152 dropped=1354

5  name="heavy_download" rate=36552 dropped=608
```
