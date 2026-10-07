# Queue size

> This page explains how to configure queue size limits in MikroTik RouterOS, detailing the impact of setting maximum packet counts on traffic shaping and scheduling. It includes examples comparing 100% shapers,...

# Queue size

The maximum permissible queue size could be specified as a maximum memory limit, but a lot of algorithms simplify it to a maximum number of packets, so the actual memory used varies depending on the size of the packets.

The rest of this page demonstrates how this works with queue types like PFIFO, BFIFO, PCQ and RED, that deal with packet count.

## Example

This example was created to highlight the queue size impact on traffic that was queued by a specific queue.

For a simplified visualization, let's assume we are processing data in steps and we know exactly how many packets will be received/transited in every step and there will be no dropped packet retransmission taking place.

![](./img/queue-size-01.webp)

As you can see in the picture above there are **25 steps** and there are a total of **1610 incoming packets** over this time frame.

### 100% Shaper

A queue is a 100% shaper when every packet that is over the allowed limits will be dropped immediately. This way all packets that are not dropped will be sent out without any delay.

Let's apply a **max-limit=100 packets per step** limitation to our example:

![](./img/queue-size-02.webp)

With this type of limitation, only 1250 out of 1610 packets were able to pass the queue (**22,4% packet drop**), but all packets arrived without delay.

### 100% Scheduler

A queue is 100% Scheduler when there are no packet drops at all, all packets are queued and will be sent out at the first possible moment.

In each step, the queue must send out queued packets from previous steps first and only then send out packets from this step; this way it is possible to keep the right sequence of packets.

We will again use the same limit (**100 packets per step**).

![](./img/queue-size-03.webp)

There was no packet loss, but 630 **(39,1%) packets had 1-step delay**, and the other 170 **(10,6%) packets had 2-step delay**. (delay = latency)

### Default-small queue type

It is also possible to choose the middle way when the queue uses both of these queuing aspects (shaping and scheduling). By default, most of the queues in RouterOS have a queue size of 10.

![](./img/queue-size-04.webp)

There were 320 **(19,9%) packets dropped** and 80 **(5,0%) packets had 1 step delay**.

### Default queue type

Another popular queue size in RouterOS is 50.

![](./img/queue-size-05.webp)

There were 190 **(11.8%) packets dropped** and 400 **(24.8%) packets had a 1 step delay**.
