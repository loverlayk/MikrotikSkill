# Traffic Eng

> This page documents MikroTik RouterOS Traffic Engineering (TE) tunnel functionality, covering monitoring commands like monitor to track TE tunnel status and paths, along with reoptimization techniques using...

# Traffic Eng

### Monitoring

To verify the TE tunnel's status, the **`monitor`** command can be used.

```ros
/interface/traffic-eng/monitor 0 
tunnel-id: 12 
primary-path-state: on-hold 
secondary-path-state: established 
secondary-path: static 
active-path: static 
active-lspid: 3 
active-label: 66 
explicit-route: "S:192.168.55.10/32,L:192.168.55.13/32,L:192.168.55.17/32" 
recorded-route: "192.168.55.13[66],192.168.55.17[59],192.168.55.18[3]" 
reserved-bandwidth: 5.0Mbps
```

### Reoptimization

The path can be re-optimized manually by entering the command `/interface/traffic-eng/reoptimize [id]` (where [id] is an item number or interface name). It allows network administrators to reoptimize the LSPs that have been established based on changes in bandwidth, traffic, management policy, or other factors.

Let's say a TE tunnel chose another path after a link failure on the best path. You can verify optimization by looking at **`explicit-route`** or **`recorded-route`** values if the `record-route` parameter is enabled.

```ros
/interface/traffic-eng/monitor 0 
tunnel-id: 12 
primary-path-state: established 
primary-path: dyn 
secondary-path-state: not-necessary 
active-path: dyn
active-lspid: 1
active-label: 67 
explicit-route: "S:192.168.55.10/32,S:192.168.55.13/32,S:192.168.55.14/32, 
S:192.168.55.17/32,S:192.168.55.18/32" 
recorded-route: "192.168.55.13[67],192.168.55.17[60],192.168.55.18[3]" 
reserved-bandwidth: 5.0Mbps
```

Whenever the link comes back, the TE tunnel will use the same path even if it is not the best path (unless `reoptimize-interval` is configured). To fix it we can manually reoptimize the tunnel path.

```ros
/interface/traffic-eng/reoptimize 0
```

```ros
/interface/traffic-eng/monitor 0 
tunnel-id: 12 
primary-path-state: established 
primary-path: dyn 
secondary-path-state: not-necessary 
active-path: dyn
active-lspid: 2
active-label: 81 
explicit-route: "S:192.168.55.5/32,S:192.168.55.2/32,S:192.168.55.1/32" 
recorded-route: "192.168.55.2[81],192.168.55.1[3]" 
reserved-bandwidth: 5.0Mbps
```

Notice how explicit-route and recorded-route changed to a shorter path.
