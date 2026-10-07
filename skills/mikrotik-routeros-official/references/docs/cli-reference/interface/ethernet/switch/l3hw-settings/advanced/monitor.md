# monitor

> An enhanced version of Monitor with extra telemetry data for advanced users. Advanced Monitor contains all data from the basic monitor as well.

-----------

## interface/ethernet/switch/l3hw-settings/advanced/monitor 
**Syscap:** rbswitch and crs_prestera
**Type:** Command

An enhanced version of [Monitor](../monitor.md) with extra telemetry data for advanced users. Advanced Monitor contains all data from the basic monitor as well.

```ros
/interface/ethernet/switch/l3hw-settings/advanced> monitor once
        ipv4-routes-total: 29968
           ipv4-routes-hw: 29957
          ipv4-routes-cpu: 11
  ipv4-shortest-hw-prefix: 0
               ipv4-hosts: 3
        ipv6-routes-total: 4
           ipv6-routes-hw: 0
          ipv6-routes-cpu: 4
  ipv6-shortest-hw-prefix: 0
               ipv6-hosts: 0
         route-queue-size: 0
         route-queue-rate: 0
       route-process-rate: 0
     fasttrack-ipv4-conns: 0
     fasttrack-queue-size: 0
     fasttrack-queue-rate: 0
   fasttrack-process-rate: 0
   fasttrack-hw-min-speed: 0
   fasttrack-hw-offloaded: 0
    fasttrack-hw-unloaded: 0
                  lpm-cap: 54560
                lpm-usage: 31931
             lpm-bank-cap: 2728
           lpm-bank-usage: 46,0,0,0,2589,2591,1983,0,2728,2728,2728,2728,2728,2728,2728,2728,2728,170,0,0
                  pbr-cap: 8192
                pbr-usage: 0
             pbr-lpm-bank: 3
                nat-usage: 0
              nexthop-cap: 8192
            nexthop-usage: 85
```

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="error-code" typ="num">Error code when L3HW driver is in a failure state.</ArgTableRow>
<ArgTableRow arg="state" typ="enum (ok | stopping | starting | fib-failure | net-failure | switch-failure | fasttrack-failure | out-of-memory) { ok:0, stopping:1, starting:2, fib-failure:3, net-failure:4, switch-failure:5, fasttrack-failure:6, out-of-memory:0xFFFFFFF4 }">Current state of the L3HW driver.</ArgTableRow>
<ArgTableRow arg="ipv4-routes-total" typ="num">The total number of IPv4 routes handled by the switch driver.</ArgTableRow>
<ArgTableRow arg="ipv4-routes-hw" typ="num">The number of hardware-offloaded IPv4 routes (a.k.a. hardware routes).</ArgTableRow>
<ArgTableRow arg="ipv4-routes-cpu" typ="num">The number of IPv4 routes redirected to the CPU (a.k.a. software routes).</ArgTableRow>
<ArgTableRow arg="ipv4-shortest-hw-prefix" typ="num">**Shortest Hardware Prefix (SHWP)** for IPv4. If the entire IPv4 routing table does not fit into the hardware memory, **partial offloading** is applied, where the longest prefixes are hw-offloaded while the shorter ones are redirected to the CPU. This field shows the shortest route prefix (/x) that is offloaded to the hardware memory. All prefixes shorter than this are processed by the CPU. `ipv4-shortest-hw-prefix=0` means the entire IPv4 routing table is offloaded to the hardware memory.</ArgTableRow>
<ArgTableRow arg="ipv4-hosts" typ="num">The number of hardware-offloaded IPv4 hosts (/32 routes).</ArgTableRow>
<ArgTableRow arg="ipv6-routes-total" typ="num">The total number of IPv6 routes handled by the switch driver.</ArgTableRow>
<ArgTableRow arg="ipv6-routes-hw" typ="num">The number of hardware-offloaded IPv6 routes (a.k.a. hardware routes). Shown only when IPv6 hardware routing is enabled (`ipv6-hw=yes`).</ArgTableRow>
<ArgTableRow arg="ipv6-routes-cpu" typ="num">The number of IPv6 routes redirected to the CPU (a.k.a. software routes). Shown only when IPv6 hardware routing is enabled (`ipv6-hw=yes`).</ArgTableRow>
<ArgTableRow arg="ipv6-shortest-hw-prefix" typ="num">**Shortest Hardware Prefix (SHWP)** for IPv6. If the entire IPv6 routing table does not fit into the hardware memory, **partial offloading** is applied, where the longest prefixes are hw-offloaded while the shorter ones are redirected to the CPU. This field shows the shortest route prefix (/x) that is offloaded to the hardware memory. All prefixes shorter than this are processed by the CPU. `ipv6-shortest-hw-prefix=0` means the entire IPv6 routing table is offloaded to the hardware memory. Shown only when IPv6 hardware routing is enabled (`ipv6-hw=yes`).</ArgTableRow>
<ArgTableRow arg="ipv6-hosts" typ="num">The number of hardware-offloaded IPv6 hosts (/128 routes). Shown only when IPv6 hardware routing is enabled (`ipv6-hw=yes`).</ArgTableRow>
<ArgTableRow arg="route-queue-size" typ="num" syscap="!prestera-cpss">The number of routes in the queue for processing by the switch chip driver. Under normal working conditions, this field is 0, meaning that all routes are processed by the driver.</ArgTableRow>
<ArgTableRow arg="route-queue-rate" typ="num" syscap="!prestera-cpss">The rate at which routes are added to the queue for processing by the switch driver (growth rate of `route-queue-size` routes per second).</ArgTableRow>
<ArgTableRow arg="route-process-rate" typ="num" syscap="!prestera-cpss">The rate at which previously queued routes are processed by the switch driver (shrink rate of `route-queue-size` routes per second)..</ArgTableRow>
<ArgTableRow arg="nexthop-cap" typ="num">The nexthop capacity.</ArgTableRow>
<ArgTableRow arg="nexthop-usage" typ="num">The number of currently used nexthops.</ArgTableRow>
<ArgTableRow arg="vxlan-mtu-packet-drop" typ="num" syscap="prestera-bc2">The number of dropped VXLAN packets due to exceeded interface MTU settings.</ArgTableRow>
<ArgTableRow arg="fasttrack-ipv4-conns" typ="num" syscap="prestera-bc2">The number of hardware-offloaded FastTrack connections. Parammeter appear only when hardware offloading of FastTrack connections is enabled.</ArgTableRow>
<ArgTableRow arg="fasttrack-queue-size" typ="num" syscap="prestera-bc2">The number of FastTrack connections in the queue for processing by the switch chip driver.</ArgTableRow>
<ArgTableRow arg="fasttrack-queue-rate" typ="num" syscap="prestera-bc2">The rate at which FastTrack connections are added to the queue for processing by the switch driver (growth rate of `fasttrack-queue-size` connections per second).</ArgTableRow>
<ArgTableRow arg="fasttrack-process-rate" typ="num" syscap="prestera-bc2">The rate at which previously queued FastTrack connections are processed by the switch driver (shrink rate of `fasttrack-queue-size` connections per second).</ArgTableRow>
<ArgTableRow arg="fasttrack-hw-min-speed" typ="num" syscap="prestera-bc2">When the hardware memory for storing FastTrack is full, this field shows the minimum speed (in bytes per second) of a hw-offloaded FastTrack connection. Parammeter appear only when hardware offloading of FastTrack connections is enabled.</ArgTableRow>
<ArgTableRow arg="fasttrack-hw-offloaded" typ="num" syscap="prestera-bc2">The number of FastTrack connections offloaded to the hardware. The counter resets every second.</ArgTableRow>
<ArgTableRow arg="fasttrack-hw-unloaded" typ="num" syscap="prestera-bc2">The number of FastTrack connections unloaded from the hardware (redirected to software routing). The counter resets every second.</ArgTableRow>
<ArgTableRow arg="lpm-cap" typ="num" syscap="!prestera-ac3">The size of the LPM hardware table (LPM = Longest Prefix Match). LPM stores route indexes for hardware routing. Not every switch chip model uses LPM. Others use TCAM.</ArgTableRow>
<ArgTableRow arg="lpm-usage" typ="num" syscap="!prestera-ac3">The number of used LPM blocks.</ArgTableRow>
<ArgTableRow arg="lpm-bank-cap" typ="num" syscap="!prestera-ac3">LPM memory is organized in banks. This value shows the size of a single bank (in LPM blocks). The bank size depends on the switch chip model. lpm-cap / lpm-bank-cap = the number of banks.</ArgTableRow>
<ArgTableRow arg="lpm-bank-usage" typ="multi { array-id, lpm-bank: num
 }" syscap="!prestera-ac3">Per-bank LPM usage (in LPM blocks).</ArgTableRow>
<ArgTableRow arg="pbr-cap" typ="num" syscap="prestera-bc2">The size of the Policy-Based Routing (PBR) hardware table. PBR is used for NAT offloading of FastTrack connections.</ArgTableRow>
<ArgTableRow arg="pbr-usage" typ="num" syscap="prestera-bc2">The number of used PBR entries.</ArgTableRow>
<ArgTableRow arg="pbr-lpm-bank" typ="num" syscap="prestera-bc2">PBR shares LPM memory banks with routing tables. This value shows the LPM bank index shared with PBR (0 = the first bank).</ArgTableRow>
<ArgTableRow arg="nat-usage" typ="num" syscap="prestera-bc2">The number of used NAT hardware entries (for FastTrack connections).</ArgTableRow>
</ArgTable>
