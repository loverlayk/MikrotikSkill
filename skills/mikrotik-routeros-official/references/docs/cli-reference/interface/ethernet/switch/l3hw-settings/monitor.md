# monitor

> This command allows monitoring switch chip and L3HW related driver stats.

-----------

## interface/ethernet/switch/l3hw-settings/monitor 
**Syscap:** rbswitch and crs_prestera
**Type:** Command

This command allows monitoring switch chip and L3HW related driver stats.

```ros
/interface/ethernet/switch/l3hw-settings/monitor
        ipv4-routes-total: 99363
           ipv4-routes-hw: 61250
          ipv4-routes-cpu: 38112
  ipv4-shortest-hw-prefix: 24
               ipv4-hosts: 87
        ipv6-routes-total: 15
           ipv6-routes-hw: 11
          ipv6-routes-cpu: 4
  ipv6-shortest-hw-prefix: 0
               ipv6-hosts: 7
         route-queue-size: 118
     fasttrack-ipv4-conns: 2031
   fasttrack-hw-min-speed: 0
              nexthop-cap: 8192
            nexthop-usage: 93
    vxlan-mtu-packet-drop: 0
```

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="state" typ="enum (ok | stopping | starting | fib-failure | net-failure | switch-failure | fasttrack-failure | out-of-memory) { ok:0, stopping:1, starting:2, fib-failure:3, net-failure:4, switch-failure:5, fasttrack-failure:6, out-of-memory:0xFFFFFFF4 }">Current state of the L3HW driver.</ArgTableRow>
<ArgTableRow arg="ipv4-routes-total" typ="num">The total number of IPv4 routes handled by the switch driver.</ArgTableRow>
<ArgTableRow arg="ipv4-routes-hw" typ="num">The number of hardware-offloaded IPv4 routes.</ArgTableRow>
<ArgTableRow arg="ipv4-routes-cpu" typ="num">The number of IPv4 routes redirected to the CPU.</ArgTableRow>
<ArgTableRow arg="ipv4-shortest-hw-prefix" typ="num">**Shortest Hardware Prefix (SHWP)** for IPv4. If the entire IPv4 routing table does not fit into the hardware memory, **partial offloading** is applied, where the longest prefixes are hw-offloaded while the shorter ones are redirected to the CPU. This field shows the shortest route prefix (/x) that is offloaded to the hardware memory. All prefixes shorter than this are processed by the CPU. `ipv4-shortest-hw-prefix=0` means the entire IPv4 routing table is offloaded to the hardware memory.</ArgTableRow>
<ArgTableRow arg="ipv4-hosts" typ="num">The number of hardware-offloaded IPv4 hosts (/32 routes).</ArgTableRow>
<ArgTableRow arg="ipv6-routes-total" typ="num">The total number of IPv6 routes handled by the switch driver.</ArgTableRow>
<ArgTableRow arg="ipv6-routes-hw" typ="num">The number of hardware-offloaded IPv6 routes (a.k.a. hardware routes). Shown only when IPv6 hardware routing is enabled (`ipv6-hw=yes`).</ArgTableRow>
<ArgTableRow arg="ipv6-routes-cpu" typ="num">The number of IPv6 routes redirected to the CPU (a.k.a. software routes). Shown only when IPv6 hardware routing is enabled (`ipv6-hw=yes`).</ArgTableRow>
<ArgTableRow arg="ipv6-shortest-hw-prefix" typ="num">**Shortest Hardware Prefix (SHWP)** for IPv6. If the entire IPv6 routing table does not fit into the hardware memory, **partial offloading** is applied, where the longest prefixes are hw-offloaded while the shorter ones are redirected to the CPU. This field shows the shortest route prefix (/x) that is offloaded to the hardware memory. All prefixes shorter than this are processed by the CPU. `ipv6-shortest-hw-prefix=0` means the entire IPv6 routing table is offloaded to the hardware memory. Shown only when IPv6 hardware routing is enabled (`ipv6-hw=yes`).</ArgTableRow>
<ArgTableRow arg="ipv6-hosts" typ="num">The number of hardware-offloaded IPv6 hosts (/128 routes).</ArgTableRow>
<ArgTableRow arg="route-queue-size" typ="num" syscap="!prestera-cpss">The number of routes in the queue for processing by the switch chip driver. Under normal working conditions, this field is 0, meaning that all routes are processed by the driver.</ArgTableRow>
<ArgTableRow arg="nexthop-cap" typ="num">The nexthop capacity.</ArgTableRow>
<ArgTableRow arg="nexthop-usage" typ="num">The number of currently used nexthops.</ArgTableRow>
<ArgTableRow arg="vxlan-mtu-packet-drop" typ="num" syscap="prestera-bc2">The number of dropped VXLAN packets due to exceeded interface MTU settings.</ArgTableRow>
<ArgTableRow arg="fasttrack-ipv4-conns" typ="num" syscap="prestera-bc2">The number of hardware-offloaded FastTrack connections. Parammeter appear only when hardware offloading of FastTrack connections is enabled.</ArgTableRow>
<ArgTableRow arg="fasttrack-hw-min-speed" typ="num" syscap="prestera-bc2">When the hardware memory for storing FastTrack is full, this field shows the minimum speed (in bytes per second) of a hw-offloaded FastTrack connection. Parammeter appear only when hardware offloading of FastTrack connections is enabled.</ArgTableRow>
</ArgTable>
