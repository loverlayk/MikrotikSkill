# Simple queue

> A simple queue in RouterOS limits the upload and download rate of a target: an address, a network or an interface. This page shows how to limit a device or a network, order queues, guarantee a rate, limit by time of...

# Simple queue

A simple queue limits the traffic of a target in both directions with one entry. The target is an IP address, a network or an interface. Simple queues are in `/queue/simple`.

Upload and download are seen from the target: upload is the traffic that the target sends, and download is the traffic that it receives. Properties with two values, such as `max-limit=5M/25M`, take the upload value first and the download value second.

The router checks the simple queues in order, from the top of the list. A packet goes to the first queue whose target matches it and skips all following queues.

:::warning
A simple queue must match a packet either by its source or by its destination, not by both. If both the source and the destination of a connection are inside the target, the queue counts and limits all packets of the connection as download, and the upload limit has no effect. Do not put both ends of the traffic into the target of one queue.
:::

## Before you start: FastTrack

The default configuration has a FastTrack rule for established connections, and simple queues do not limit FastTracked connections. Without this step, the examples on this page do not limit established TCP and UDP connections.

Disable the FastTrack rule:

```ros
/ip/firewall/filter
disable [find action=fasttrack-connection]
```

Check that the rule is disabled. The command counts the disabled FastTrack rules:

```ros
/ip/firewall/filter/print count-only \
    where action=fasttrack-connection and disabled
1
```

FastTrack makes forwarding faster, so without it the router needs more processor time for the same traffic. There are two other ways:

- Leave the rule enabled and keep only the connections that the queues limit out of FastTrack. See the example in [FastTrack](../packet-flow-in-routeros#fasttrack).
- Use a [queue tree](./queue-tree) with an interface as the parent. It limits FastTracked traffic too.

## Limit one device

This example limits the device 192.168.88.10 to 5 Mbps upload and 25 Mbps download:

```ros
/queue/simple
add name=tv target=192.168.88.10/32 max-limit=5M/25M
```

Check that the queue counts the traffic of the device. The counters grow while the device sends and receives:

```ros
/queue/simple/print bytes where name=tv
Columns: NAME, TARGET, BYTES, TOTAL-BYTES
# NAME  TARGET            BYTES          TOTAL-BYTES
0 tv    192.168.88.10/32  185000/185000            0
```

## Limit a network

With a network as the target, all devices of the network share one limit. This example limits the whole LAN to 20 Mbps upload and 100 Mbps download:

```ros
/queue/simple
add name=lan target=192.168.88.0/24 max-limit=20M/100M
```

Check that the queue counts the traffic of the LAN:

```ros
/queue/simple/print bytes where name=lan
Columns: NAME, TARGET, BYTES, TOTAL-BYTES
# NAME  TARGET           BYTES          TOTAL-BYTES
0 lan   192.168.88.0/24  189000/189000            0
```

The target can also be an interface, for example `target=bridge`. The queue then limits the traffic of all devices behind this interface.

To give each device of the network its own limit with one queue, or to share the rate equally between the devices, use a [PCQ](./queue-types/pcq) queue type.

## Give one device a different limit

Because a packet goes to the first queue that matches, a queue for one device must be before the queue for its network. `place-before` adds a queue before another queue. This example limits the LAN and gives the server 192.168.88.10 its own, higher limit:

```ros
/queue/simple
add name=lan target=192.168.88.0/24 max-limit=20M/100M
add name=server target=192.168.88.10/32 max-limit=50M/50M \
    place-before=lan
```

Check the order and the counters. The `server` queue is first and counts the traffic of the server, and the `lan` queue counts the traffic of the other devices:

```ros
/queue/simple/print bytes
Columns: NAME, TARGET, BYTES, TOTAL-BYTES
# NAME    TARGET            BYTES          TOTAL-BYTES
0 server  192.168.88.10/32  210000/210000            0
1 lan     192.168.88.0/24   208000/208000            0
```

## Guarantee a rate for one device

`limit-at` is the rate that a queue gets when the devices together ask for more than the limit of the parent queue. `limit-at` has an effect only between queues with the same parent.

In this example, the LAN has 20 Mbps upload and 100 Mbps download. The server always gets at least 5 Mbps upload and 20 Mbps download. Each child queue can use the whole rate when the other does not use it:

```ros
/queue/simple
add name=lan target=192.168.88.0/24 max-limit=20M/100M
add name=server parent=lan target=192.168.88.10/32 \
    limit-at=5M/20M max-limit=20M/100M
add name=others parent=lan target=192.168.88.0/24 \
    limit-at=15M/80M max-limit=20M/100M
```

The `limit-at` values of the child queues together must not be more than the `max-limit` of the parent queue.

Check that each queue counts its traffic. The parent queue counts the traffic of both child queues:

```ros
/queue/simple/print bytes
Columns: NAME, TARGET, BYTES, TOTAL-BYTES
# NAME    TARGET            BYTES          TOTAL-BYTES
0 lan     192.168.88.0/24   421000/421000            0
1 server  192.168.88.10/32  210000/210000            0
2 others  192.168.88.0/24   211000/211000            0
```

See [HTB](./htb-hierarchical-token-bucket) for how `limit-at`, `max-limit` and `priority` work between parent and child queues.

## Limit at certain hours

`time` makes a queue active only in a time range and on the selected days. The router uses its own clock, so check that the time and the time zone in `/system/clock` are correct. This example limits the LAN on working days from 8:00 to 18:00:

```ros
/queue/simple
add name=work-hours target=192.168.88.0/24 max-limit=10M/50M \
    time=8h-18h,mon,tue,wed,thu,fri
```

Check the queue. This output is from inside the time range. Outside the time range, the flag `I` is in front of the name, and the queue limits no traffic:

```ros
/queue/simple/print where name=work-hours
0  name="work-hours" target=192.168.88.0/24 parent=none packet-marks=""
   priority=8/8 queue=default-small/default-small limit-at=0/0
   max-limit=10M/50M burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s
   bucket-size=0.1/0.1 time=8h-18h,mon,tue,wed,thu,fri
```

## Limit the traffic to one destination

`dst` limits the queue to the traffic between the target and one destination address or network. Other traffic of the target does not go to this queue. This example limits the traffic between the device 192.168.88.10 and a backup server at 203.0.113.10 to 5 Mbps:

```ros
/queue/simple
add name=backup target=192.168.88.10/32 dst=203.0.113.10/32 \
    max-limit=5M/5M
```

Check that the queue counts the traffic to the backup server:

```ros
/queue/simple/print bytes where name=backup
Columns: NAME, TARGET, BYTES, TOTAL-BYTES
# NAME    TARGET            BYTES          TOTAL-BYTES
0 backup  192.168.88.10/32  215000/215000            0
```

## Limit upload and download together

The `total-` properties set one limit for upload and download together. This example limits the LAN to 50 Mbps for the sum of both directions:

```ros
/queue/simple
add name=lan target=192.168.88.0/24 total-max-limit=50M
```

Check the queue. With a total limit, the `total-` counters count the traffic:

```ros
/queue/simple/print stats where name=lan
0  name="lan" target=192.168.88.0/24 rate=0bps/0bps total-rate=472.0kbps
   packet-rate=0/0 total-packet-rate=59 queued-bytes=0/0 total-queued-bytes=0
   queued-packets=0/0 total-queued-packets=0 bytes=0/0 total-bytes=390000
   packets=0/0 total-packets=390 dropped=0/0 total-dropped=0
```

## More properties

- `queue` selects the [queue type](./queue-types) for upload and for download. A new simple queue uses `default-small`.
- `burst-limit`, `burst-threshold` and `burst-time` allow a higher rate for a short time. See [Queue Burst](./queue-burst).
- `packet-marks` limits the queue to packets that have one of the listed packet marks. Mark the packets in the `prerouting` or `forward` chain of [mangle](../firewall/mangle).
- `priority` and `bucket-size` control how child queues share the rate of their parent. See [HTB](./htb-hierarchical-token-bucket).

:::note
A CAKE queue type can buffer more traffic in a simple queue than in an equivalent queue tree. Set [`cake-memlimit`](./queue-types/cake#memory-limit) on the CAKE queue type to bound its memory use.
:::

## Read more

- [Queue tree](./queue-tree) - limits by packet mark and by interface.
- [Queue types](./queue-types) - the queuing algorithms and their examples.
- [`/queue/simple` CLI reference](../../cli-reference/queue/simple) - all properties.
