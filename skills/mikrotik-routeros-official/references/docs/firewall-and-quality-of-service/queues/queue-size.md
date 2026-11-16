# Queue size

> This page explains how to configure queue size limits in MikroTik RouterOS, detailing the impact of setting maximum packet counts on traffic shaping and scheduling. It includes examples comparing 100% shapers,...

# Queue size

The maximum permissible queue size could be specified as a maximum memory limit, but a lot of algorithms simplify it to a maximum number of packets, so the actual memory used varies depending on the size of the packets.

The queue size is a property of the [queue type](./queue-types). The `pfifo`, `mq-pfifo` and `red` kinds count packets (`pfifo-limit`, `mq-pfifo-limit`, `red-limit`). The `bfifo` and `pcq` kinds count bytes (`bfifo-limit`, `pcq-limit`). The smallest value is 1 for `pfifo-limit` and `pcq-limit`, and 1000 for `bfifo-limit`.

The rest of this page shows the effect of the queue size with a queue that counts packets.

CAKE is different: it controls its memory use with [`cake-memlimit`](./queue-types/cake#memory-limit) on the CAKE queue type, not with the packet-count queue size settings described on this page.

## Example

This example was created to highlight the queue size impact on traffic that was queued by a specific queue.

For a simplified visualization, let's assume we are processing data in steps and we know exactly how many packets will be received/transited in every step and there will be no dropped packet retransmission taking place.

![Timeline of 25 steps with 1610 incoming packets](./img/queue-size-01.webp)

As you can see in the picture above there are **25 steps** and there are a total of **1610 incoming packets** over this time frame.

### 100% Shaper

A queue is a 100% shaper when every packet that is over the allowed limits will be dropped immediately. This way all packets that are not dropped will be sent out without any delay.

Let's apply a **max-limit=100 packets per step** limitation to our example:

![100% shaper drops packets above 100 packets per step](./img/queue-size-02.webp)

With this type of limitation, only 1250 out of 1610 packets were able to pass the queue (**22,4% packet drop**), but all packets arrived without delay.

### 100% Scheduler

A queue is 100% Scheduler when there are no packet drops at all, all packets are queued and will be sent out at the first possible moment.

In each step, the queue must send out queued packets from previous steps first and only then send out packets from this step; this way it is possible to keep the right sequence of packets.

We will again use the same limit (**100 packets per step**).

![100% scheduler delays packets above 100 packets per step](./img/queue-size-03.webp)

There was no packet loss, but 630 **(39,1%) packets had 1-step delay**, and the other 170 **(10,6%) packets had 2-step delay**. (delay = latency)

### Default-small queue type

It is also possible to choose the middle way when the queue uses both of these queuing aspects (shaping and scheduling). By default, most of the queues in RouterOS have a queue size of 10.

![Default-small queue type drops some packets and delays others](./img/queue-size-04.webp)

There were 320 **(19,9%) packets dropped** and 80 **(5,0%) packets had 1 step delay**.

### Default queue type

Another popular queue size in RouterOS is 50.

![Default queue type drops fewer packets and delays more of them](./img/queue-size-05.webp)

There were 190 **(11.8%) packets dropped** and 400 **(24.8%) packets had a 1 step delay**.
