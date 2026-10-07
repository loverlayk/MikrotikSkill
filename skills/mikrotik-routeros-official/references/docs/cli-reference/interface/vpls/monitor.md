# monitor

> Command displays the current VPLS interface status.

-----------

## interface/vpls/monitor 
**Conditions:** !smips
**Type:** Command

Command displays the current VPLS interface status.

For example:

```ros
[admin@10.0.11.23] /interface/vpls> monitor vpls2
remote-label: 800000
local-label: 43
remote-status: 
transport: 10.255.11.201/32
transport-nexthop: 10.0.11.201
imposed-labels: 800000
```

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="remote-label" typ="num">MPLS label assigned by the remote peer for this pseudowire (RFC 4447 Section 5.1).</ArgTableRow>
<ArgTableRow arg="local-label" typ="num">MPLS label assigned locally for this pseudowire (RFC 4447 Section 5.1).</ArgTableRow>
<ArgTableRow arg="remote-status" typ="ubit (not-forwarding, attachment-circuit-rx-fault, attachment-circuit-tx-fault, pw-rx-fault, pw-tx-fault)">Pseudowire status received from the remote peer via LDP status signaling (RFC 4447 Section 5.4).</ArgTableRow>
<ArgTableRow arg="remote-group" typ="num">Group ID of the remote peer, used for LDP status withdrawal aggregation (RFC 4447 Section 5.3).</ArgTableRow>
<ArgTableRow arg="te-tunnel" typ="enum">Name of the transport interface. Shown when VPLS is running over a [Traffic Engineering](../../../user-guides/routing-and-networking-protocols/mpls/traffic-eng.md) tunnel.</ArgTableRow>
<ArgTableRow arg="nexthops" typ="object { label: enum (expl-null | alert | expl-null6 | impl-null) { expl-null:0, alert:1, expl-null6:2, impl-null:3 }
, nh: address
, interface: iface_enum
 }">Transport nexthops in use.</ArgTableRow>
</ArgTable>
