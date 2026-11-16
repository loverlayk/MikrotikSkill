# FIFO queue types

> PFIFO, BFIFO and MQ-PFIFO are the first-in, first-out queue types of RouterOS. This page shows how to set the queue size in packets or in bytes, and describes the default FIFO queue types and only-hardware-queue.

# FIFO queue types

A first-in, first-out (FIFO) queue sends packets in the order in which they arrive. When the queue is full, it drops every new packet until there is space again. A FIFO queue does not separate devices or connections.

RouterOS has three FIFO kinds:

- `pfifo` - the queue size is a number of packets, set with `pfifo-limit`.
- `bfifo` - the queue size is a number of bytes, set with `bfifo-limit`.
- `mq-pfifo` - one `pfifo` queue for each transmit queue of an interface. The size of each queue is set with `mq-pfifo-limit`.

The default queue types `default`, `ethernet-default` and `default-small` are `pfifo` types. `multi-queue-ethernet-default` is an `mq-pfifo` type.

## Set the queue size in packets

A simple queue and a queue tree use `default-small`, which holds 10 packets. This example gives the rate limit of one server a queue of 100 packets.

Simple queues do not limit FastTracked connections, and the default configuration has a FastTrack rule for established connections. The first two lines of the example disable this rule. See [Simple queue](../simple-queue) for other ways to take traffic off FastTrack.

```ros
/ip/firewall/filter
disable [find action=fasttrack-connection]
/queue/type
add name=fifo-100 kind=pfifo pfifo-limit=100
/queue/simple
add name=server target=192.168.88.10/32 max-limit=10M/10M \
    queue=fifo-100/fifo-100
```

Check that the queue counts the traffic of the server:

```ros
/queue/simple/print bytes where name=server
Columns: NAME, TARGET, BYTES, TOTAL-BYTES
# NAME    TARGET            BYTES          TOTAL-BYTES
0 server  192.168.88.10/32  188000/188000            0
```

## Set the queue size in bytes

With `pfifo`, the amount of queued data depends on the packet sizes. With `bfifo`, the limit is the same for small and large packets. This example changes the queue of the server to 150 000 bytes, which is the size of 100 packets of 1500 bytes:

```ros
/queue/type
add name=fifo-150k kind=bfifo bfifo-limit=150000
/queue/simple
set server queue=fifo-150k/fifo-150k
```

Check the queue type of the simple queue:

```ros
/queue/simple/print where name=server
0  name="server" target=192.168.88.10/32 parent=none packet-marks=""
   priority=8/8 queue=fifo-150k/fifo-150k limit-at=0/0 max-limit=10M/10M
   burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s bucket-size=0.1/0.1
```

## Choose the queue size

A full queue adds delay to every packet that passes it. The delay is the queue size divided by the rate of the queue. A queue of 100 packets of 1500 bytes holds 1.2 Mbit of data:

- At 10 Mbps, the last packet in the queue waits 120 ms.
- At 100 Mbps, the last packet in the queue waits 12 ms.

The default type `default-small` holds 10 packets, which is 6 ms at 20 Mbps. The type `default` holds 50 packets, which is 30 ms at 20 Mbps.

A short queue drops more packets when traffic arrives in bursts. A long queue drops fewer packets and delays them longer. See [Queue size](../queue-size) for how the queue size changes the shape of the traffic.

## FIFO types on interfaces

`/queue/interface` shows the queue type of each interface. On Ethernet interfaces, the default is `only-hardware-queue`. Its kind is `none`: the interface has no software queue, and packets go directly to the transmit queue of the hardware.

```ros
/queue/interface/print where interface=ether1
Columns: INTERFACE, QUEUE, ACTIVE-QUEUE
#  INTERFACE  QUEUE                ACTIVE-QUEUE
0  ether1     only-hardware-queue  only-hardware-queue
```

To put a software FIFO queue on an interface, set its queue type:

```ros
/queue/interface
set ether1 queue=ethernet-default
```

Check the active queue of the interface:

```ros
/queue/interface/print where interface=ether1
Columns: INTERFACE, QUEUE, ACTIVE-QUEUE
#  INTERFACE  QUEUE             ACTIVE-QUEUE
0  ether1     ethernet-default  ethernet-default
```

`QUEUE` is the configured type. `ACTIVE-QUEUE` is the type that the interface uses now. When a queue tree has the interface as its parent, `ACTIVE-QUEUE` shows `queue-tree`.

## Read more

- [Queue types](./) - all kinds and the default queue types.
- [Queue size](../queue-size) - the effect of the queue size on a rate limit.
- [`/queue/type` CLI reference](../../../cli-reference/queue/type) - all properties.
