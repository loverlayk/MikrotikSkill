# Queue types

> Queue types in RouterOS are named sets of settings for a queuing algorithm: FIFO, RED, SFQ, PCQ, CoDel, FQ-CoDel or CAKE. Create a queue type in /queue/type and assign it to a simple queue, a queue tree or an...

# Queue types

A queue type is a named set of settings for one queuing algorithm. The algorithm is the `kind` of the queue type. It decides which packet a queue sends next, how many packets the queue holds and which packets it drops.

Queue types are in `/queue/type`. A queue type processes no traffic until a queue uses it. Three places use queue types:

- A [simple queue](../simple-queue): the `queue` property takes two types, for upload and for download.
- A [queue tree](../queue-tree): the `queue` property takes one type.
- An [interface queue](../#interface-queue): the `queue` property of `/queue/interface` takes one type for the packets that the interface transmits.

## Kinds

| Kind | How it queues packets | Page |
| :-- | :-- | :-- |
| `pfifo`, `bfifo` | One queue, first in, first out. The size is in packets or in bytes. | [FIFO queue types](./pfifo-bfifo) |
| `mq-pfifo` | One `pfifo` queue for each transmit queue of the interface. | [FIFO queue types](./pfifo-bfifo) |
| `none` | No software queue. | [FIFO queue types](./pfifo-bfifo) |
| `red` | One queue that drops packets at random before it is full. | [RED](./red) |
| `sfq` | A separate queue for each flow. The flows take turns. | [SFQ](./sfq) |
| `pcq` | A separate queue and a separate rate limit for each address or port. | [PCQ](./pcq) |
| `codel` | One queue that drops packets when they wait too long. | [CoDel and FQ-CoDel](./codel-fq-codel) |
| `fq-codel` | A separate CoDel queue for each flow. | [CoDel and FQ-CoDel](./codel-fq-codel) |
| `cake` | A separate queue for each flow and each host, with its own shaper. | [CAKE](./cake) |

## Default queue types

RouterOS has ten default queue types. You can change their settings, but you cannot remove them.

```ros
/queue/type/print
Flags: * - DEFAULT
0  * name="default" kind=pfifo pfifo-limit=50
 
1  * name="ethernet-default" kind=pfifo pfifo-limit=50
 
2  * name="wireless-default" kind=sfq sfq-perturb=5 sfq-allot=1514
 
3  * name="synchronous-default" kind=red red-limit=60 red-min-threshold=10
     red-max-threshold=50 red-burst=20 red-avg-packet=1000
 
4  * name="hotspot-default" kind=sfq sfq-perturb=5 sfq-allot=1514
 
5  * name="pcq-upload-default" kind=pcq pcq-rate=0 pcq-limit=50KiB
     pcq-classifier=src-address pcq-total-limit=2000KiB pcq-burst-rate=0
     pcq-burst-threshold=0 pcq-burst-time=10s pcq-src-address-mask=32
     pcq-dst-address-mask=32 pcq-src-address6-mask=128
     pcq-dst-address6-mask=128
 
6  * name="pcq-download-default" kind=pcq pcq-rate=0 pcq-limit=50KiB
     pcq-classifier=dst-address pcq-total-limit=2000KiB pcq-burst-rate=0
     pcq-burst-threshold=0 pcq-burst-time=10s pcq-src-address-mask=32
     pcq-dst-address-mask=32 pcq-src-address6-mask=128
     pcq-dst-address6-mask=128
 
7  * name="only-hardware-queue" kind=none
 
8  * name="multi-queue-ethernet-default" kind=mq-pfifo mq-pfifo-limit=50
 
9  * name="default-small" kind=pfifo pfifo-limit=10
```

A simple queue or a queue tree that you create without the `queue` property uses `default-small`.

## Create a queue type and use it

This example creates an FQ-CoDel queue type with the default settings and uses it for both directions of a simple queue.

Simple queues do not limit FastTracked connections, and the default configuration has a FastTrack rule for established connections. The first two lines of the example disable this rule. See [Simple queue](../simple-queue) for other ways to take traffic off FastTrack.

```ros
/ip/firewall/filter
disable [find action=fasttrack-connection]
/queue/type
add name=fq-codel-default kind=fq-codel
/queue/simple
add name=lan target=192.168.88.0/24 max-limit=20M/100M \
    queue=fq-codel-default/fq-codel-default
```

In `queue` and in `max-limit`, the first value is for upload and the second value is for download.

Check that the queue uses the type:

```ros
/queue/simple/print where name=lan
0  name="lan" target=192.168.88.0/24 parent=none packet-marks="" priority=8/8
   queue=fq-codel-default/fq-codel-default limit-at=0/0 max-limit=20M/100M
   burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s bucket-size=0.1/0.1
```

## How the kinds differ under load

When one transfer fills a rate limit, a FIFO queue holds the packets of every device in the same line. A packet from another device waits until the queue sends all packets in front of it. A longer queue means a longer wait.

PCQ, FQ-CoDel and CAKE keep separate queues. A packet from another device does not wait behind the transfer.

The delay of a FIFO queue follows from its size: 50 packets of 1500 bytes at 20 Mbps take 30 ms to send. In a test with one TCP transfer at a 20 Mbps limit, a ping from another device took about that long through a FIFO queue of 50 packets, and about 1 ms, the same as with no transfer, through PCQ, FQ-CoDel and CAKE.

When the router translates the addresses of the devices with NAT, PCQ still classifies by the address of the device. CAKE does the same when `cake-nat=yes` is set.

For the properties of each kind, see the [`/queue/type` CLI reference](../../../cli-reference/queue/type).

## Related topics

<DocCardList />
