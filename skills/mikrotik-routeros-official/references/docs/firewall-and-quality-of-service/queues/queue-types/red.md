# RED

> Random Early Drop (RED) is a RouterOS queue type that drops packets at random before the queue is full. This page describes the RED settings and shows how to use a RED queue type in a simple queue.

# RED

Random Early Drop (RED) is one queue for all traffic, like a FIFO queue. The difference is in how it drops packets. RED follows the average queue size:

- While the average is less than `red-min-threshold`, RED drops no packets.
- Between `red-min-threshold` and `red-max-threshold`, RED drops packets at random. The more the queue fills, the more packets it drops.
- More than `red-max-threshold`, RED drops every new packet.

![Graph of the RED drop probability against the average queue size: zero up to the minimum threshold, a rising line between the minimum and the maximum threshold, and one from the maximum threshold.](../img/queues-02.webp)

`red-limit` is the hard limit of the queue. The thresholds, `red-limit` and `red-burst` are numbers of packets. `red-avg-packet` is the average packet size in bytes that RED uses in its calculation.

The default queue type `synchronous-default` is a RED type.

## Use RED on a rate limit

This example creates a RED queue type with a queue of 120 packets and uses it for a rate limit on the whole LAN.

Simple queues do not limit FastTracked connections, and the default configuration has a FastTrack rule for established connections. The first two lines of the example disable this rule. See [Simple queue](../simple-queue) for other ways to take traffic off FastTrack.

```ros
/ip/firewall/filter
disable [find action=fasttrack-connection]
/queue/type
add name=red-wan kind=red red-limit=120 red-min-threshold=20 \
    red-max-threshold=100 red-burst=40
/queue/simple
add name=lan target=192.168.88.0/24 max-limit=20M/100M \
    queue=red-wan/red-wan
```

Check that the queue counts the traffic of the LAN:

```ros
/queue/simple/print bytes where name=lan
Columns: NAME, TARGET, BYTES, TOTAL-BYTES
# NAME  TARGET           BYTES          TOTAL-BYTES
0 lan   192.168.88.0/24  719852/717012            0
```

## Read more

- [Queue types](./) - all kinds and the default queue types.
- [`/queue/type` CLI reference](../../../cli-reference/queue/type) - all properties.
