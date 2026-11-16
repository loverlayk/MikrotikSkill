# Queues

> Overview of queues in RouterOS: rate limiting principles, committed and maximum rates, interface queues, and links to the Simple queue, Queue tree, queue type, HTB, burst and queue size pages.

# Queues

This section covers RouterOS queueing and bandwidth management. Use it to configure HTB, PCQ, burst behavior, [queue sizes](./queue-size), and queue types for traffic shaping.

<DocCardList />

## Overview

A queue is a collection of data packets collectively waiting to be transmitted by a network device using a pre-defined structure methodology. Queuing works almost on the same methodology used at banks or supermarkets, where the customer is treated according to their arrival.

Queues are used to:

- Limit data rate for certain IP addresses, subnets, protocols, ports, etc.
- Packet prioritization.
- Configure traffic bursts for traffic acceleration.
- Apply different time-based limits.
- Share available traffic among users equally, or depending on the load of the channel.

Queue implementation in MikroTik RouterOS is based on Hierarchical Token Bucket (HTB). HTB allows the creation of a hierarchical queue structure and determines relations between queues. These hierarchical structures can be attached at two different places. The [Packet Flow diagram](../packet-flow-in-routeros) illustrates both *input* and *postrouting* chains.

There are two different ways to configure queues in RouterOS:

- [Simple queue](./simple-queue) (`/queue/simple`) - limits the upload and download of an address, a network or an interface with one entry.
- [Queue tree](./queue-tree) (`/queue/tree`) - limits traffic in one direction by packet mark, on an interface or globally. Packet marks come from [`/ip/firewall/mangle`](../firewall/mangle).

RouterOS provides a possibility to configure queues in 8 levels -  the first level is an interface queue from the `/queue/interface` menu and the other 7 are lower-level queues that can be created in Queue Simple and/or Queue Tree.

### Rate limitation principles

Rate limiting is used to control the rate of traffic flow sent or received on a network interface. Traffic with a rate that is less than or equal to the specified rate is sent, whereas traffic that exceeds the rate is dropped or delayed.

Rate limiting can be performed in two ways:

1. Discard all packets that exceed the rate limit – ***rate-limiting (dropper or shaper)***.
2. Delay packets that exceed the specific rate limit in the queue and transmit them when it is possible – ***rate equalizing (scheduler)***.

The next figure explains the difference between *rate limiting* and rate *equalizing*:

![Two pairs of traffic graphs. Rate limiting (shaper) cuts the traffic peaks at the rate limit. Rate equalizing (scheduler) also cuts the peaks at the rate limit and sends the delayed traffic afterwards.](./img/queues-01.webp)

As you can see in the first case, all traffic exceeds a specific rate and is dropped. In another case, traffic exceeds a specific rate and is delayed in the queue and transmitted later when it is possible, but note that the packet can be delayed only while the queue is not full. If there is no more space in the queue buffer, packets are dropped.

For each queue we can define two rate limits:

- **CIR** (Committed Information Rate) – (**limit-at** in RouterOS) In a worst-case scenario, the flow will get this amount of traffic rate regardless of other traffic flows. At any given time, the bandwidth should not fall below this committed rate.
- **MIR** (Maximum Information Rate) – (**max-limit** in RouterOS) In a best-case scenario, the maximum available data rate for the flow, if there is any free part of the bandwidth.

## Simple Queue

A simple queue limits the upload and download rate of a target: an address, a network or an interface. It needs no packet marks.

See [Simple queue](./simple-queue) for the examples: a limit for a device or a network, the order of queues, a guaranteed rate, limits by time and by destination.

:::note
A CAKE queue type can buffer more traffic in a simple queue than in an equivalent queue tree. Set [`cake-memlimit`](./queue-types/cake#memory-limit) on the CAKE queue type to bound its memory use.
:::

## Queue Tree

A queue tree limits traffic in one direction, selected by packet mark, on an interface or globally. A queue tree with an interface as the parent also limits FastTracked traffic.

See [Queue tree](./queue-tree) for the examples: a limit for an Internet connection without mangle rules, priority for voice traffic and limits for marked traffic.

## Queue Types

A queue type is a named set of settings for a queuing algorithm, such as FIFO, PCQ, FQ-CoDel or CAKE. Queue types are in `/queue/type`, and simple queues, queue trees and interface queues use them.

See [Queue types](./queue-types) for the kinds, the default queue types and examples for each kind.

## Interface Queue

**Sub-menu:** `/queue/interface`

Before sending data over an interface, it is processed by the queue. An Interface Queue is a transmit (egress) queue; it does not process packets received by that interface.

For forwarded client traffic, the WAN-facing Interface Queue processes uploads, and the LAN-facing Interface Queue processes downloads. Each direction uses a separate queue instance. If traffic can leave through several LAN interfaces, configure every required transmit path or use a Simple Queue or Queue Tree that matches the traffic at a common point.

This sub-menu lists all available interfaces in RouterOS and allows changing the queue type for a particular interface. The list is generated automatically.

```ros
[admin@MikroTik] > /queue/interface/print
Columns: INTERFACE, QUEUE, ACTIVE-QUEUE
# INTERFACE QUEUE ACTIVE-QUEUE
0 ether1 only-hardware-queue only-hardware-queue
1 ether2 only-hardware-queue only-hardware-queue
2 ether3 only-hardware-queue only-hardware-queue
3 ether4 only-hardware-queue only-hardware-queue
4 ether5 only-hardware-queue only-hardware-queue
5 ether6 only-hardware-queue only-hardware-queue
6 ether7 only-hardware-queue only-hardware-queue
7 ether8 only-hardware-queue only-hardware-queue
8 ether9 only-hardware-queue only-hardware-queue
9 ether10 only-hardware-queue only-hardware-queue
10 sfp-sfpplus1 only-hardware-queue only-hardware-queue
11 wlan1 wireless-default wireless-default
12 wlan2 wireless-default wireless-default 
```

## Queue load visualization in GUI

In Winbox and Webfig, a green, yellow, or red icon visualizes each Simple and Tree queue usage based on max-limit.

|  |  |
| :-- | :-- |
| ![Green queue icon](./img/queue-usage-0-50.png)  | Less than 50% of max-limit used |
| ![Yellow queue icon](./img/queue-usage-50-75.png)  | 50% or more, but less than 75% of max-limit used |
| ![Red queue icon](./img/queue-usage-75-100.png)  | 75% or more of max-limit used |
