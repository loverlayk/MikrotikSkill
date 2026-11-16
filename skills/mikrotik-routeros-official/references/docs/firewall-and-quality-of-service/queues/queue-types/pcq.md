# PCQ

> Per Connection Queue (PCQ) is a RouterOS queue type that gives each address or port its own queue and rate limit. This page shows how to share a rate equally between devices and how to limit networks instead of...

# PCQ

Per Connection Queue (PCQ) sorts traffic into sub-streams and gives each sub-stream its own FIFO queue. One queue with a PCQ type replaces a separate queue for each device.

Two properties define how PCQ works:

- `pcq-classifier` selects what one sub-stream is: `src-address`, `dst-address`, `src-port`, `dst-port` or a combination. With `src-address`, each sending device is one sub-stream. With `dst-address`, each receiving device is one sub-stream.
- `pcq-rate` is the rate limit of each sub-stream. With `pcq-rate=0`, the sub-streams have no limit of their own, and every active sub-stream sends the same number of packets.

![PCQ operation: a classifier groups the incoming packets into the FIFO queues 1 to n, each with the size of the PCQ limit, and one total FIFO queue with the size of the PCQ total limit sends them out.](../img/queues-04.webp)

For traffic of the LAN, use `src-address` for upload and `dst-address` for download. PCQ classifies by the address of the device also when the router translates this address with NAT.

The default queue types `pcq-upload-default` and `pcq-download-default` use these two classifiers with `pcq-rate=0`.

## Share a rate equally between devices

This example limits the LAN to 20 Mbps upload and 100 Mbps download. The devices that are active at the same time share the rate. A device that is alone gets the whole rate.

PCQ shares by packets, not by bytes: every active device sends the same number of packets. Devices that send packets of the same size get the same rate. A device that sends larger packets gets a larger part of the rate.

Simple queues do not limit FastTracked connections, and the default configuration has a FastTrack rule for established connections. The first two lines of the example disable this rule. See [Simple queue](../simple-queue) for other ways to take traffic off FastTrack.

```ros
/ip/firewall/filter
disable [find action=fasttrack-connection]
/queue/simple
add name=lan target=192.168.88.0/24 max-limit=20M/100M \
    queue=pcq-upload-default/pcq-download-default
```

Check the queue. `pcq-queues` shows the number of sub-streams for upload and for download. In this output, three devices are active:

```ros
/queue/simple/print stats where name=lan
0  name="lan" target=192.168.88.0/24 rate=650.0kbps/626.0kbps total-rate=0bps
   packet-rate=81/78 total-packet-rate=0 queued-bytes=0/0 total-queued-bytes=0
   queued-packets=0/0 total-queued-packets=0 bytes=611000/611000 total-bytes=0
   packets=611/611 total-packets=0 dropped=0/0 total-dropped=0 pcq-queues=3/3
```

## Limit each device to a fixed rate

Set `pcq-rate` to give each device its own rate limit. See [PCQ example](../pcq-example) for the complete configuration with a simple queue and with a queue tree.

## Limit networks instead of addresses

The address masks make one sub-stream from a whole network. `pcq-src-address-mask` and `pcq-dst-address-mask` are for IPv4. `pcq-src-address6-mask` and `pcq-dst-address6-mask` are for IPv6. The default masks are 32 and 128: one sub-stream for each address.

In this example, each customer has a /30 network inside 192.168.88.0/24. Each customer gets 5 Mbps upload and 10 Mbps download for all addresses of the network together:

```ros
/ip/firewall/filter
disable [find action=fasttrack-connection]
/queue/type
add name=pcq-up-net kind=pcq pcq-classifier=src-address \
    pcq-rate=5M pcq-src-address-mask=30
add name=pcq-down-net kind=pcq pcq-classifier=dst-address \
    pcq-rate=10M pcq-dst-address-mask=30
/queue/simple
add name=customers target=192.168.88.0/24 \
    queue=pcq-up-net/pcq-down-net
```

Check the queue. In this output, three devices from two /30 networks are active, and the queue has two sub-streams:

```ros
/queue/simple/print stats where name=customers
0  name="customers" target=192.168.88.0/24 rate=610.0kbps/610.0kbps
   total-rate=0bps packet-rate=76/76 total-packet-rate=0 queued-bytes=0/0
   total-queued-bytes=0 queued-packets=0/0 total-queued-packets=0
   bytes=597000/597000 total-bytes=0 packets=597/597 total-packets=0
   dropped=0/0 total-dropped=0 pcq-queues=2/2
```

## Queue sizes

`pcq-limit` is the queue size of one sub-stream. `pcq-total-limit` is the queue size of all sub-streams together. Both count bytes, not packets, and are set in kilobytes: the default `pcq-limit` holds about 50 kilobytes of packets for one sub-stream. They are not rate limits.

## Read more

- [PCQ example](../pcq-example) - a fixed rate limit for each device.
- [Queue Burst](../queue-burst) - how burst works. PCQ has the same burst settings for each sub-stream: `pcq-burst-rate`, `pcq-burst-threshold` and `pcq-burst-time`.
- [Queue types](./) - all kinds and the default queue types.
- [`/queue/type` CLI reference](../../../cli-reference/queue/type) - all properties.
