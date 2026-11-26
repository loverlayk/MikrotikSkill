# Queue Burst

> Queue Burst feature allows temporary bandwidth bursts beyond configured limits when average traffic stays below a threshold, using burst-limit and burst-time parameters to control the burst duration and size.

# Queue Burst

Burst is a feature that allows satisfying queue requirements for additional bandwidth even if the required rate is bigger than **MIR** (**max-limit**) for a limited period of time.

Burst can occur only if the average rate of the queue for the last **burst-time** seconds is smaller than **burst-threshold**. Burst will stop if the average rate of the queue for the last **burst-time** seconds is bigger than or equal to **burst-threshold**.

The burst mechanism is simple - if a burst is allowed, the **max-limit** value is replaced by the **burst-limit** value. When the burst is disallowed, the **max-limit** value remains unchanged.

- `burst-limit`: maximal upload/download data rate which can be reached while the burst is allowed.
- `burst-time`: period of time, in seconds, over which the average data rate is calculated. This is not the time of the actual burst.
- `burst-threshold`: the value of the burst on/off switch.

[Simple queues](./simple-queue) and [queue trees](./queue-tree) have these properties. The [bucket size](./htb-hierarchical-token-bucket#bucket-size-in-action) of a queue also lets traffic pass above `max-limit` for a short time. The examples on this page also use two values that are not properties of a queue:

- average rate - every 1/16 part of the **burst-time**, the router calculates the average data rate of each class over the last **burst-time** seconds. The queue statistics do not show this value.
- actual rate - the actual traffic transfer rate of the queue. The queue statistics show it as `rate`.

## Example

Values: **limit-at=1M**, **max-limit=2M**, **burst-threshold=1500k**, **burst-limit=4M**

A simple queue with these values and `burst-time=16s` for one client:

```ros
/queue/simple
add name=burst target=192.168.88.101/32 limit-at=1M/1M \
    max-limit=2M/2M burst-limit=4M/4M \
    burst-threshold=1500k/1500k burst-time=16s/16s
```

Simple queues do not limit FastTracked connections, and a queue matches only the traffic that no earlier queue has matched. See [Simple queue](./simple-queue) for both.

The client will try to download two 4MB (32Mb) blocks of data, the first download will start at zero seconds, and the second download will start at the 17th second. There was no traffic during the last minute.

### Burst-time=16s

The chart is drawn from the values in the table below.

![Actual rate and average rate of both downloads with burst-time=16s: 4 Mbit/s until second 6 and 2 Mbit/s until second 10, then 2 Mbit/s from second 17, 4 Mbit/s from second 19 to 22 and 2 Mbit/s until second 28. The average rate rises to 2 Mbit/s and falls below the 1500 kbit/s threshold at second 19.](./img/queue-burst-16s.svg)

As we can see as soon as the client requested bandwidth it was able to get 4Mbps burst for 6 seconds. This is the longest possible burst with given values *(longest-burst-time = burst-threshold \* burst-time / burst-limit)*. As soon as the burst runs out, the rest of the data will be downloaded with 2Mbps. This way, a block of data was downloaded in 10 seconds - without burst, it would take 16 seconds. Burst has 7 seconds to recharge before the next download will start.

Note that burst is still disallowed when the download started and it kicks in only afterward - in the middle of a download. So with this example, we proved that a burst may happen in the middle of a download. The burst was ~4 seconds long and the second block was downloaded 4 seconds faster than without burst.

The average rate is calculated every 1/16 of burst time so in this case 1s.

| Time | average rate | burst | actual rate |
| --: | :-- | :-- | :-- |
| 0 | (0+0+0+0+0+0+0+0+0+0+0+0+0+0+0+0)/16=0Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps |
| 1 | (0+0+0+0+0+0+0+0+0+0+0+0+0+0+0+4)/16=250Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps |
| 2 | (0+0+0+0+0+0+0+0+0+0+0+0+0+0+4+4)/16=500Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps |
| 3 | (0+0+0+0+0+0+0+0+0+0+0+0+0+4+4+4)/16=750Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps |
| 4 | (0+0+0+0+0+0+0+0+0+0+0+0+4+4+4+4)/16=1000Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps |
| 5 | (0+0+0+0+0+0+0+0+0+0+0+4+4+4+4+4)/16=1250Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps |
| 6 | (0+0+0+0+0+0+0+0+0+0+4+4+4+4+4+4)/16=1500Kbps | average rate = burst-threshold â†’ Burst is **not** allowed | **2Mbps** |
| 7 | (0+0+0+0+0+0+0+0+0+4+4+4+4+4+4+2)/16=1625Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps |
| 8 | (0+0+0+0+0+0+0+0+4+4+4+4+4+4+2+2)/16=1750Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps |
| 9 | (0+0+0+0+0+0+0+4+4+4+4+4+4+2+2+2)/16=1875Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps |
| 10 | (0+0+0+0+0+0+4+4+4+4+4+4+2+2+2+2)/16=2Mbps | average rate > burst-threshold â†’ Burst is not allowed | **0Mbps** |
| 11 | (0+0+0+0+0+4+4+4+4+4+4+2+2+2+2+0)/16=2Mbps | average rate > burst-threshold â†’ Burst is not allowed | 0Mbps |
| 12 | (0+0+0+0+4+4+4+4+4+4+2+2+2+2+0+0)/16=2Mbps | average rate > burst-threshold â†’ Burst is not allowed | 0Mbps |
| 13 | (0+0+0+4+4+4+4+4+4+2+2+2+2+0+0+0)/16=2Mbps | average rate > burst-threshold â†’ Burst is not allowed | 0Mbps |
| 14 | (0+0+4+4+4+4+4+4+2+2+2+2+0+0+0+0)/16=2Mbps | average rate > burst-threshold â†’ Burst is not allowed | 0Mbps |
| 15 | (0+4+4+4+4+4+4+2+2+2+2+0+0+0+0+0)/16=2Mbps | average rate > burst-threshold â†’ Burst is not allowed | 0Mbps |
| 16 | (4+4+4+4+4+4+2+2+2+2+0+0+0+0+0+0)/16=2Mbps | average rate > burst-threshold â†’ Burst is not allowed | 0Mbps |
| 17 | (4+4+4+4+4+2+2+2+2+0+0+0+0+0+0+0)/16=1750Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps |
| 18 | (4+4+4+4+2+2+2+2+0+0+0+0+0+0+0+2)/16=1500Kbps | average rate = burst-threshold â†’ Burst is not allowed | 2Mbps |
| 19 | (4+4+4+2+2+2+2+0+0+0+0+0+0+0+2+2)/16=1375Kbps | average rate < burst-threshold â†’ Burst **is** allowed | 4Mbps |
| 20 | (4+4+2+2+2+2+0+0+0+0+0+0+0+2+2+4)/16=1375Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps |
| 21 | (4+2+2+2+2+0+0+0+0+0+0+0+2+2+4+4)/16=1375Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps |
| 22 | (2+2+2+2+0+0+0+0+0+0+0+2+2+4+4+4)/16=1375Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps |
| 23 | (2+2+2+0+0+0+0+0+0+0+2+2+4+4+4+4)/16=1500Kbps | average rate = burst-threshold â†’ Burst is **not** allowed | 2Mbps |
| 24 | (2+2+0+0+0+0+0+0+0+2+2+4+4+4+4+2)/16=1500Kbps | average rate = burst-threshold â†’ Burst is not allowed | 2Mbps |
| 25 | (2+0+0+0+0+0+0+0+2+2+4+4+4+4+2+2)/16=1500Kbps | average rate = burst-threshold â†’ Burst is not allowed | 2Mbps |
| 26 | (0+0+0+0+0+0+0+2+2+4+4+4+4+2+2+2)/16=1500Kbps | average rate = burst-threshold â†’ Burst is not allowed | 2Mbps |
| 27 | (0+0+0+0+0+0+2+2+4+4+4+4+2+2+2+2)/16=1625Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps |
| 28 | (0+0+0+0+0+2+2+4+4+4+4+2+2+2+2+2)/16=1750Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps |
| 29 | (0+0+0+0+2+2+4+4+4+4+2+2+2+2+2+2)/16=1875Kbps | average rate > burst-threshold â†’ Burst is not allowed | 0Mbps |
| 30 | (0+0+0+2+2+4+4+4+4+2+2+2+2+2+2+0)/16=1875Kbps | average rate > burst-threshold â†’ Burst is not allowed | 0Mbps |
| 31 | (0+0+2+2+4+4+4+4+2+2+2+2+2+2+0+0)/16=1875Kbps | average rate > burst-threshold â†’ Burst is not allowed | 0Mbps |

### Burst-time=8s

The chart is drawn from the values in the table below.

![Actual rate and average rate of both downloads with burst-time=8s: 4 Mbit/s for the first 3 seconds of the first download and from second 17.5 to 19 of the second download, 2 Mbit/s for the rest of each download](./img/queue-burst-8s.svg)

If we decrease burst-time to 8 seconds - we are able to see that in this case, bursts are only at the beginning of downloads. The average rate is calculated every 1/16th of burst time, so in this case every 0.5 seconds.

| Time | average rate | burst | actual rate |
| --: | :-- | :-- | :-- |
| 0 | (0+0+0+0+0+0+0+0+0+0+0+0+0+0+0+0)/8=0Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps (2Mb per 0.5s) |
| 0.5 | (0+0+0+0+0+0+0+0+0+0+0+0+0+0+0+2)/8=250Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps (2Mb per 0.5s) |
| 1 | (0+0+0+0+0+0+0+0+0+0+0+0+0+0+2+2)/8=500Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps (2Mb per 0.5s) |
| 1.5 | (0+0+0+0+0+0+0+0+0+0+0+0+0+2+2+2)/8=750Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps (2Mb per 0.5s) |
| 2 | (0+0+0+0+0+0+0+0+0+0+0+0+2+2+2+2)/8=1000Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps (2Mb per 0.5s) |
| 2.5 | (0+0+0+0+0+0+0+0+0+0+0+2+2+2+2+2)/8=1250Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps (2Mb per 0.5s) |
| 3 | (0+0+0+0+0+0+0+0+0+0+2+2+2+2+2+2)/8=1500Kbps | average rate = burst-threshold â†’ Burst is **not** allowed | **2Mbps** (1Mb per 0.5s) |
| 3.5 | (0+0+0+0+0+0+0+0+0+2+2+2+2+2+2+1)/8=1625Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 4 | (0+0+0+0+0+0+0+0+2+2+2+2+2+2+1+1)/8=1750Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 4.5 | (0+0+0+0+0+0+0+2+2+2+2+2+2+1+1+1)/8=1875Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 5 | (0+0+0+0+0+0+2+2+2+2+2+2+1+1+1+1)/8=2000Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 5.5 | (0+0+0+0+0+2+2+2+2+2+2+1+1+1+1+1)/8=2125Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 6 | (0+0+0+0+2+2+2+2+2+2+1+1+1+1+1+1)/8=2250Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 6.5 | (0+0+0+2+2+2+2+2+2+1+1+1+1+1+1+1)/8=2375Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 7 | (0+0+2+2+2+2+2+2+1+1+1+1+1+1+1+1)/8=2500Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 7.5 | (0+2+2+2+2+2+2+1+1+1+1+1+1+1+1+1)/8=2625Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 8 | (2+2+2+2+2+2+1+1+1+1+1+1+1+1+1+1)/8=2750Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 8.5 | (2+2+2+2+2+1+1+1+1+1+1+1+1+1+1+1)/8=2625Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 9 | (2+2+2+2+1+1+1+1+1+1+1+1+1+1+1+1)/8=2500Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 9.5 | (2+2+2+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2375Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 10 | (2+2+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2250Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 10.5 | (2+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2125Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 11 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 11.5 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 12 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 12.5 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 13 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average rate > burst-threshold â†’ Burst is not allowed | **0Mbps** (0Mb per 0.5s) |
| 13.5 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+0)/8=1875Kbps | average rate > burst-threshold â†’ Burst is not allowed | 0Mbps (0Mb per 0.5s) |
| 14 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+0+0)/8=1750Kbps | average rate > burst-threshold â†’ Burst is not allowed | 0Mbps (0Mb per 0.5s) |
| 14.5 | (1+1+1+1+1+1+1+1+1+1+1+1+1+0+0+0)/8=1625Kbps | average rate > burst-threshold â†’ Burst is not allowed | 0Mbps (0Mb per 0.5s) |
| 15 | (1+1+1+1+1+1+1+1+1+1+1+1+0+0+0+0)/8=1500Kbps | average rate > burst-threshold â†’ Burst is not allowed | 0Mbps (0Mb per 0.5s) |
| 15.5 | (1+1+1+1+1+1+1+1+1+1+1+0+0+0+0+0)/8=1375Kbps | average rate < burst-threshold â†’ Burst **is** allowed | 0Mbps (0Mb per 0.5s) |
| 16 | (1+1+1+1+1+1+1+1+1+1+0+0+0+0+0+0)/8=1250Kbps | average rate < burst-threshold â†’ Burst is allowed | 0Mbps (0Mb per 0.5s) |
| 16.5 | (1+1+1+1+1+1+1+1+1+0+0+0+0+0+0+0)/8=1125Kbps | average rate < burst-threshold â†’ Burst is allowed | 0Mbps (0Mb per 0.5s) |
| 17 | (1+1+1+1+1+1+1+1+0+0+0+0+0+0+0+0)/8=1000Kbps | average rate < burst-threshold â†’ Burst is allowed | **2Mbps** (1Mb per 0.5s) |
| 17.5 | (1+1+1+1+1+1+1+0+0+0+0+0+0+0+0+1)/8=1000Kbps | average rate < burst-threshold â†’ Burst is allowed | **4Mbps** (2Mb per 0.5s) |
| 18 | (1+1+1+1+1+1+0+0+0+0+0+0+0+0+1+2)/8=1125Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps (2Mb per 0.5s) |
| 18.5 | (1+1+1+1+1+0+0+0+0+0+0+0+0+1+2+2)/8=1250Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps (2Mb per 0.5s) |
| 19 | (1+1+1+1+0+0+0+0+0+0+0+0+1+2+2+2)/8=1375Kbps | average rate < burst-threshold â†’ Burst is allowed | 4Mbps (2Mb per 0.5s) |
| 19.5 | (1+1+1+0+0+0+0+0+0+0+0+1+2+2+2+2)/8=1500Kbps | average rate = burst-threshold â†’ Burst is **not** allowed | 2Mbps (1Mb per 0.5s) |
| 20 | (1+1+0+0+0+0+0+0+0+0+1+2+2+2+2+1)/8=1500Kbps | average rate = burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 20.5 | (1+0+0+0+0+0+0+0+0+1+2+2+2+2+1+1)/8=1500Kbps | average rate = burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 21 | (0+0+0+0+0+0+0+0+1+2+2+2+2+1+1+1)/8=1500Kbps | average rate = burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 21.5 | (0+0+0+0+0+0+0+1+2+2+2+2+1+1+1+1)/8=1625Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 22 | (0+0+0+0+0+0+1+2+2+2+2+1+1+1+1+1)/8=1750Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 22.5 | (0+0+0+0+0+1+2+2+2+2+1+1+1+1+1+1)/8=1875Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 23 | (0+0+0+0+1+2+2+2+2+1+1+1+1+1+1+1)/8=2000Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 23.5 | (0+0+0+1+2+2+2+2+1+1+1+1+1+1+1+1)/8=2125Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 24 | (0+0+1+2+2+2+2+1+1+1+1+1+1+1+1+1)/8=2250Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 24.5 | (0+1+2+2+2+2+1+1+1+1+1+1+1+1+1+1)/8=2375Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 25 | (1+2+2+2+2+1+1+1+1+1+1+1+1+1+1+1)/8=2500Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 25.5 | (2+2+2+2+1+1+1+1+1+1+1+1+1+1+1+1)/8=2500Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 26 | (2+2+2+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2375Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 26.5 | (2+2+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2250Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 27 | (2+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2125Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 27.5 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 28 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 28.5 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 29 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 29.5 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 30 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average rate > burst-threshold â†’ Burst is not allowed | 2Mbps (1Mb per 0.5s) |
| 30.5 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average rate > burst-threshold â†’ Burst is not allowed | 0Mbps (0Mb per 0.5s) |
| 31 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+0)/8=1875Kbps | average rate > burst-threshold â†’ Burst is not allowed | 0Mbps (0Mb per 0.5s) |
