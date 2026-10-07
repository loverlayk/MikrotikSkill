# RIP

> MikroTik RouterOS supports RIP version 2 for exchanging routing information within autonomous systems, selecting optimal paths based on hop count. Configuration is available under /routing/rip.

# RIP

MikroTik RouterOS implements RIP version 2 (RFC 2453). Version 1 (RFC 1058) is not supported.

RIP enables routers in an autonomous system to exchange routing information. It always uses the best path (the path with the fewest number of hops (i.e. routers)) available. Configuration is available under [`/routing/rip`](../../../cli-reference/routing/rip/instance.md).
