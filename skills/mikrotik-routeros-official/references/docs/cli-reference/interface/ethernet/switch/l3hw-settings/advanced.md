# advanced

> This menu allows tweaking l3hw settings for specific use cases.

-----------

## interface/ethernet/switch/l3hw-settings/advanced 
**Syscap:** rbswitch and crs_prestera
**Type:** Settings Directory

This menu allows tweaking l3hw settings for specific use cases.

It is NOT recommended to change the advanced L3HW settings unless instructed by MikroTik Support or a MikroTik Certified Routing Engineer. Applying incorrect settings may break the L3HW operation.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="route-queue-limit-high" typ="num" syscap="!prestera-cpss">The switch driver stops route indexing when [`route-queue-size`](../monitor#route-queue-size) exceeds this value. Lowering this value leads to faster route processing but increases the lag between a route's appearance in RouterOS and hardware memory. Setting **0** disables route indexing when there are any routes in the processing queue - the most efficient CPU usage but the longest delay before hardware offloading. Useful when there are static routes only. Not recommended together with routing protocols (such as BGP or OSPF) when there are frequent routing table changes.</ArgTableRow>
<ArgTableRow arg="route-queue-limit-low" typ="num" syscap="!prestera-cpss">Re-enable route indexing when [`route-queue-size`](../monitor#route-queue-size) drops down to this value. Must not exceed the high limit. Setting **0** tells the switch driver to process all pending routes before the next hw-offloading attempt. While this is the desired behavior, it may completely block the hw-offloading under a constant BGP feed.</ArgTableRow>
<ArgTableRow arg="shwp-reset-counter" typ="num">
Reset the Shortest HW Prefix (SHWP) and try the full route table offloading after this number of changes in the routing table.  
At a partial offload, when the entire routing table does not fit into the hardware memory and shorter prefixes are redirected to the CPU, there is no need to try offloading route prefixes shorter than SHWP since those will get redirected to the CPU anyway, theoretically. However, significant changes to the routing table may lead to a different index layout and, therefore, a different number of routes that can be hw-offloaded. That's why it is recommended to do the full table re-indexing occasionally.
Lowering this value may allow more routes to be hw-offloaded but increases CPU usage and vice-versa. Setting `shwp-reset-counter=0` always does full re-indexing after each routing table change.
This setting is used only during Partial Offloading and has no effect when [`ipv4-shortest-hw-prefix`](./monitor#ipv4-shortest-hw-prefix)=0 (and ipv6, respectively).
</ArgTableRow>
<ArgTableRow arg="partial-offload-chunk" typ="num" syscap="prestera-bc2">
The minimum number of routes for incremental adding in Partial Offloading.  
Depending on the switch chip model, routes are offloaded either as-is (each routing entry in RouterOS corresponds to an entry in the hardware memory) or get indexed, and the index entries are the ones that are written into the hardware memory. This setting is used only for the latter during Partial Offloading.
Depending on index fragmentation, a single IPv4 route addition can occupy from -3 to +6 LPM blocks of HW memory (some route additions may lower the amount of required HW memory thanks to index defragmentation). Hence, it is impossible to predict the exact number of routes that may fit in the hardware memory. The switch driver uses a binary split algorithm to find the maximum number of routes that fit in the hardware.  
Let's imagine 128k routes, all of them not fitting into the hardware memory. The algorithm halves the number and tries offloading 64k routes. Let's say offloading succeeded. In the next iteration, the algorithm picks 96k, let's say it fails; then 80k - fails again, 72k - succeeds, 76k, etc. until the difference between succeeded and failed numbers drops below the partial-offload-chunk value.
Lowering the partial-offload-chunk value increases the number of hw-offloaded routes but also raises CPU usage and vice-versa.
</ArgTableRow>
<ArgTableRow arg="route-index-delay-min" typ="time" syscap="!prestera-cpss">
The minimum delay between route processing and its offloading. The delay allows processing more routes together and offloading them at once, saving CPU usage.  
It also makes offloading the entire routing table faster by reducing the per-route processing work. On the other hand, it slows down the offloading of an individual route.  
If an additional route is received during the delay, the latter resets to the `route-index-delay-min` value. Adding more and more routes within the delay keeps resetting the timer until the `route-index-delay-max` is reached.
</ArgTableRow>
<ArgTableRow arg="route-index-delay-max" typ="time">The maximum delay between route processing and its offloading. When the maximum delay is reached, the processed routes get offloaded despite more routes pending. However, `route-queue-limit-high` has higher priority than this, meaning that the indexing/offloading gets paused anyway when a certain queue size is reached.</ArgTableRow>
<ArgTableRow arg="neigh-keepalive-interval" typ="time" syscap="!prestera-cpss">Neighbor (host) keepalive interval. When a host gets hw-offloaded, all traffic from/to it is routed by the switch chip, and RouterOS may think the neighbor is inactive and delete it. To prevent that, the switch driver must keep the offloaded neighbors alive by sending periodic refreshes to RouterOS.</ArgTableRow>
<ArgTableRow arg="neigh-discovery-interval" typ="time" syscap="!prestera-cpss">
The interval between sending ARP (IPv4) or Neighbor Discovery (IPv6) requests to check if the offloaded host is still active.  
Unfortunately, switch chips do not provide per-neighbor stats. Hence, the only way to check if the offloaded host is still active is by sending occasional ARP (IPv4) / Neighbor Discovery (IPv6) requests to the connected network.  
Neighbor discovery is triggered within the neighbor keepalive work. Hence, the discovery time is rounded up to the next keepalive session. Choose a value for `neigh-discovery-interval` not divisible by `neigh-keepalive-interval` to send ARP/ND requests in various sessions, preventing broadcast bursts.
</ArgTableRow>
<ArgTableRow arg="neigh-discovery-burst-limit" typ="num" syscap="!prestera-cpss">The maximum number of ARP/ND requests that can be sent at once.</ArgTableRow>
<ArgTableRow arg="neigh-discovery-burst-delay" typ="time" syscap="!prestera-cpss">The delay between ARP/ND subsequent bursts if the number of requests exceeds `neigh-discovery-burst-limit`.</ArgTableRow>
<ArgTableRow arg="neigh-dump-retries" typ="num" syscap="!prestera-cpss">The maximum retry count to offload a neighbor table in case of failure.</ArgTableRow>
</ArgTable>
