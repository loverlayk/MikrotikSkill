# HTB (Hierarchical Token Bucket)

> HTB (Hierarchical Token Bucket) is a queuing discipline in RouterOS for rate limiting and burst handling, using a token bucket algorithm to manage data rates with configurable capacity and limits.

# HTB (Hierarchical Token Bucket)

HTB (Hierarchical Token Bucket) is a classful queuing discipline for rate limiting and burst handling. RouterOS uses a modified version of HTB in [Simple queues](./simple-queue) and [Queue trees](./queue-tree). This page describes HTB as RouterOS implements it: the token bucket of a queue, the two rate limits, priority, and how a queue structure shares a rate.

## How a queue passes packets

![HTB diagram with the token bucket, the packet queue and the token rate selection](./img/htb-hierarchical-token-bucket-01.webp)

### Token bucket (red part of the diagram)

The token bucket algorithm is based on an analogy to a bucket where tokens, represented in bytes, are added at a specific rate. The bucket itself has a specified capacity. If the bucket fills to capacity, newly arriving tokens are dropped.

**Bucket capacity = bucket-size \* max-limit**

`bucket-size` is a number from 0 to 10. The default value is `0.1`.

Before a packet passes through the queue, the queue bucket is inspected to see if it contains sufficient tokens at that moment.

If yes, the appropriate number of tokens is removed ("cashed in") and the packet passes through the queue.

If not, the packet stays at the start of the packet queue until the appropriate amount of tokens is available.

In a multi-level queue structure, tokens used in a child queue are also charged to its parent queues. In other words, child queues borrow tokens from their parent queues.

### Packet queue (blue part of the diagram)

The size of the packet queue, the sequence in which packets are added to it, and when packets are discarded are determined by:

- the queue type that the queue uses (`queue`) - see [Queue types](./queue-types)
- the queue size of that queue type - see [Queue size](./queue-size)

### Token rate selection (black part of the diagram)

The maximal token rate at any given time is equal to the highest active value of these:

- `limit-at`: guaranteed data rate of the queue.
- `max-limit`: maximal data rate of the queue.
- `burst-limit`: maximal data rate of the queue while the burst is active.

`burst-limit` is active only when the burst is in the allowed state, see [Queue Burst](./queue-burst).

When `limit-at` is the highest value, extra tokens are issued to compensate for all the tokens that were not borrowed from the parent queue.

## Bucket size in action

The examples in this section limit all traffic from and to one address, 192.168.88.101. The mangle rules mark its packets. `bridge` is the LAN interface and `ether1` is the WAN interface, as in the default configuration:

```ros
/ip/firewall/mangle
add chain=forward action=mark-connection \
    new-connection-mark=pc1_conn connection-mark=no-mark \
    src-address=192.168.88.101
add chain=forward action=mark-connection \
    new-connection-mark=pc1_conn connection-mark=no-mark \
    dst-address=192.168.88.101
add chain=forward action=mark-packet new-packet-mark=pc1_traffic \
    connection-mark=pc1_conn
```

:::note
Mangle rules do not process [FastTracked](../packet-flow-in-routeros#fasttrack) packets, and the default configuration FastTracks established connections. Keep the connections that the queues have to limit out of FastTrack, see [Packet marks and FastTrack](./queue-tree#packet-marks-and-fasttrack). This applies to all examples on this page.
:::

### Default queue bucket

```ros
/queue/tree
add name=download parent=bridge packet-mark=pc1_traffic max-limit=10M
add name=upload parent=ether1 packet-mark=pc1_traffic max-limit=10M
```

In this case `bucket-size=0.1`, so the bucket capacity is 0.1 x 10M = 1M.

If the bucket is full (that is, the client was not using the full capacity of the queue for some time), the next 1 Mb of traffic passes through the queue at an unrestricted speed. After that, the queue passes 10 Mbit/s.

### Large queue bucket

Set the bucket size of both queues to its maximal value:

```ros
/queue/tree
set download,upload bucket-size=10
```

In this case `bucket-size=10`, so the bucket capacity is 10 x 10M = 100M.

If the bucket is full, the next 100 Mb of traffic passes through the queue at an unrestricted speed, in addition to the 10 Mbit/s of new tokens. So you can have:

- 20 Mbit/s transfer speed for 10 s.
- 30 Mbit/s transfer speed for 5 s.
- 60 Mbit/s transfer burst for 2 s.
- 1 Gbit/s transfer burst for approximately 100 ms.

When the bucket is empty, the rate of the queue returns to 10 Mbit/s.

The bucket permits a type of burstiness of the traffic that passes through the queue. The behavior is similar to the [burst](./queue-burst) feature, but it has no upper limit of the burst rate. A queue structure adds this limit.

### Large child queue bucket, small parent queue bucket

```ros
/queue/tree
remove download,upload
add name=download_parent parent=bridge max-limit=20M
add name=download parent=download_parent packet-mark=pc1_traffic \
    max-limit=10M bucket-size=10
add name=upload_parent parent=ether1 max-limit=20M
add name=upload parent=upload_parent packet-mark=pc1_traffic \
    max-limit=10M bucket-size=10
```

In this case:

- parent queue `bucket-size=0.1`, bucket capacity is 0.1 x 20M = 2M
- child queue `bucket-size=10`, bucket capacity is 10 x 10M = 100M

The parent runs out of tokens much faster than the child queue. The child queue borrows tokens from the parent queue, so the whole system is restricted to the token rate of the parent queue, in this case to `max-limit=20M`. This rate is sustained until the child queue runs out of tokens. Then the child queue is restricted to its own token rate of 10 Mbit/s.

In this way, the queue allows a burst at 20 Mbit/s for up to 10 seconds.

## Queue structure

There are three basic steps to create an HTB structure:

- **Match and mark traffic** – classify traffic for further use. It consists of one or more matching parameters to select packets for the specific class.
- **Create rules (policy) to mark traffic** – put specific traffic classes into specific queues and define the actions that are taken for each class.
- **Attach a policy for a specific interface(-s)** – append the policy to all traffic (`parent=global`), to a specific interface, or to a specific parent queue.

HTB allows the creation of a hierarchical queue structure and determines relations between queues, like "parent-child" or "child-child".

As soon as a queue has at least one child, it becomes an **inner** queue. All queues without children are **leaf** queues. Leaf queues make actual traffic consumption, inner queues are responsible only for traffic distribution. All leaf queues are treated on an equal basis.

In RouterOS, the `parent` property assigns a queue as a child to another queue.

### Dual limitation

Each queue in HTB has two rate limits:

- **CIR** (Committed Information Rate) – `limit-at` in RouterOS. The worst case scenario: the flow gets this amount of traffic no matter what (assuming the interface can actually send so much data).
- **MIR** (Maximal Information Rate) – `max-limit` in RouterOS. The best case scenario: a rate that the flow can get up to if the parent of its queue has spare bandwidth.

In other words, at first the `limit-at` (CIR) of all queues is satisfied. Only then child queues try to borrow the necessary data rate from their parents in order to reach their `max-limit` (MIR).

:::warning
CIR is assigned to the corresponding queue no matter what, even if the `max-limit` of the parent is exceeded. Example 4 on this page shows it.
:::

That is why, to ensure the designed usage of the dual limitation feature, keep to these rules:

- The sum of the committed rates of all children is less than or equal to the amount of traffic that is available to the parent.

  CIR(parent) ≥ CIR(child1) + ... + CIR(childN)

  If the parent is the main parent, CIR(parent) = MIR(parent).

- The maximal rate of any child is less than or equal to the maximal rate of the parent.

  MIR(parent) ≥ MIR(child1) & MIR(parent) ≥ MIR(child2) & ... & MIR(parent) ≥ MIR(childN)

### Priority

The `limit-at` (CIR) of all queues is given out no matter what.

Priority is responsible for the distribution of the remaining traffic of the parent queue to child queues, so that they are able to reach `max-limit`.

The queue with higher priority reaches its `max-limit` before the queue with lower priority. 8 is the lowest priority, and 1 is the highest.

Priority only works:

- For leaf queues. Priority in an inner queue has no meaning.
- If `max-limit` is specified (not 0).

## Examples

The examples in this section use one HTB structure and change the options of its queues. They show how HTB distributes the rate in each case.

### Structure

The HTB structure consists of five queues:

- **Queue01** inner queue with two children - **Queue02** and **Queue03**
- **Queue02** inner queue with two children - **Queue04** and **Queue05**
- **Queue03** leaf queue
- **Queue04** leaf queue
- **Queue05** leaf queue

**Queue03**, **Queue04** and **Queue05** are clients that require 10 Mbit/s all the time. The link behind the outgoing interface is able to handle 10 Mbit/s of traffic.

Remove the mangle rules and the queues of the bucket size examples before you add this structure. The mangle rules mark the packets of the three clients, and the queues are attached to the outgoing interface `ether1`:

```ros
/ip/firewall/mangle
add chain=forward action=mark-packet new-packet-mark=client3 \
    src-address=192.168.88.101 passthrough=no
add chain=forward action=mark-packet new-packet-mark=client4 \
    src-address=192.168.88.102 passthrough=no
add chain=forward action=mark-packet new-packet-mark=client5 \
    src-address=192.168.88.103 passthrough=no
/queue/tree
add name=Queue01 parent=ether1 max-limit=10M
add name=Queue02 parent=Queue01 limit-at=4M max-limit=10M
add name=Queue03 parent=Queue01 packet-mark=client3 \
    limit-at=6M max-limit=10M priority=1
add name=Queue04 parent=Queue02 packet-mark=client4 \
    limit-at=2M max-limit=10M priority=3
add name=Queue05 parent=Queue02 packet-mark=client5 \
    limit-at=2M max-limit=10M priority=5
```

These commands create the queues of Example 1. Each next example changes the queues of the previous one.

### Example 1: Usual case

![Queue structure and rates of example 1](./img/htb-hierarchical-token-bucket-02.webp)

- **Queue01** limit-at=0Mbps max-limit=10Mbps
- **Queue02** limit-at=4Mbps max-limit=10Mbps
- **Queue03** limit-at=6Mbps max-limit=10Mbps priority=1
- **Queue04** limit-at=2Mbps max-limit=10Mbps priority=3
- **Queue05** limit-at=2Mbps max-limit=10Mbps priority=5

Result:

- **Queue03** receives 6 Mbit/s.
- **Queue04** receives 2 Mbit/s.
- **Queue05** receives 2 Mbit/s.

By satisfying all `limit-at` values, the main queue has no throughput left to distribute.

The `rate` of each queue, in bits per second, shows the distribution while the three clients send:

```ros
[admin@MikroTik] > /queue/tree/print stats proplist=name,rate
0  name="Queue01" rate=10004120

1  name="Queue02" rate=4001472

2  name="Queue03" rate=6002648

3  name="Queue04" rate=2001952

4  name="Queue05" rate=1999520
```

### Example 2: Usual case with max-limit

![Queue structure and rates of example 2](./img/htb-hierarchical-token-bucket-03.webp)

- **Queue01** limit-at=0Mbps max-limit=10Mbps
- **Queue02** limit-at=4Mbps max-limit=10Mbps
- **Queue03** limit-at=2Mbps max-limit=10Mbps priority=3
- **Queue04** limit-at=2Mbps max-limit=10Mbps priority=1
- **Queue05** limit-at=2Mbps max-limit=10Mbps priority=5

```ros
/queue/tree
set Queue03 limit-at=2M priority=3
set Queue04 priority=1
```

Result:

- **Queue03** receives 2 Mbit/s.
- **Queue04** receives 6 Mbit/s.
- **Queue05** receives 2 Mbit/s.

After satisfying all `limit-at` values, HTB gives the remaining throughput to the queue with the highest priority.

### Example 3: Inner queue limit-at

![Queue structure and rates of example 3](./img/htb-hierarchical-token-bucket-04.webp)

- **Queue01** limit-at=0Mbps max-limit=10Mbps
- **Queue02** limit-at=8Mbps max-limit=10Mbps
- **Queue03** limit-at=2Mbps max-limit=10Mbps priority=1
- **Queue04** limit-at=2Mbps max-limit=10Mbps priority=3
- **Queue05** limit-at=2Mbps max-limit=10Mbps priority=5

```ros
/queue/tree
set Queue02 limit-at=8M
set Queue03 priority=1
set Queue04 priority=3
```

Result:

- **Queue03** receives 2 Mbit/s.
- **Queue04** receives 6 Mbit/s.
- **Queue05** receives 2 Mbit/s.

After satisfying all `limit-at` values, HTB gives throughput to the queue with the highest priority. But in this case, the inner queue **Queue02** has `limit-at` specified. By doing so, it reserves 8 Mbit/s of throughput for the queues **Queue04** and **Queue05**. Of these two, **Queue04** has the highest priority, which is why it gets the additional throughput.

### Example 4: Leaf queue limit-at

![Queue structure and rates of example 4](./img/htb-hierarchical-token-bucket-05.webp)

- **Queue01** limit-at=0Mbps max-limit=10Mbps
- **Queue02** limit-at=4Mbps max-limit=10Mbps
- **Queue03** limit-at=6Mbps max-limit=10Mbps priority=1
- **Queue04** limit-at=2Mbps max-limit=10Mbps priority=3
- **Queue05** limit-at=12Mbps max-limit=15Mbps priority=5

```ros
/queue/tree
set Queue02 limit-at=4M
set Queue03 limit-at=6M
set Queue05 limit-at=12M max-limit=15M
```

Result, as the clients get it through the 10 Mbit/s link:

- **Queue03** receives ~3 Mbit/s.
- **Queue04** receives ~1 Mbit/s.
- **Queue05** receives ~6 Mbit/s.

To satisfy all `limit-at` values, HTB is forced to allocate 20 Mbit/s: 6 Mbit/s to **Queue03**, 2 Mbit/s to **Queue04**, and 12 Mbit/s to **Queue05**. The queue statistics show these rates, and a rate of 20 Mbit/s for **Queue01**, although its `max-limit` is 10 Mbit/s. The link behind the output interface is able to handle only 10 Mbit/s, so half of this traffic is lost after the queues. As the output interface queue is usually FIFO, the throughput allocation keeps the ratio 6:2:12, or 3:1:6.
