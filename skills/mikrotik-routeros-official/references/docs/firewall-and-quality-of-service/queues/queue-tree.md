# Queue tree

> A queue tree in RouterOS limits traffic in one direction, selected by packet mark, on an interface or globally. This page shows how to limit an Internet connection without mangle rules, give priority to voice traffic...

# Queue tree

A queue tree entry limits traffic in one direction. It selects packets by their packet mark, not by address. Queue trees are in `/queue/tree`.

Two properties define what a queue limits:

- `parent` is where the queue is attached. With an interface as the parent, the queue limits the traffic that leaves the router through this interface. With `parent=global`, the queue limits marked traffic in all directions. With another queue as the parent, the queue is a child of that queue.
- `packet-mark` selects the packets. `no-mark` selects the packets that have no packet mark. A queue with children needs no packet mark: it gets the traffic of its children. A queue without children and without a packet mark gets no traffic.

Packet marks come from [mangle](../firewall/mangle) rules. Queue trees have no order: each packet goes to the queue with its packet mark.

## Limit an Internet connection

Upload leaves the router through the WAN interface, and download leaves through the LAN interface. One queue on each interface with `packet-mark=no-mark` limits all traffic, and no mangle rules are necessary. Queues with an interface as the parent also limit FastTracked traffic, so the FastTrack rule of the default configuration stays as it is. In the default configuration, the WAN interface is `ether1` and the LAN interface is `bridge`:

```ros
/queue/tree
add name=upload parent=ether1 packet-mark=no-mark max-limit=20M
add name=download parent=bridge packet-mark=no-mark max-limit=100M
```

The `download` queue limits all packets that leave through `bridge`, also the packets that the router itself sends to the LAN. It does not limit traffic that the bridge forwards between its own ports.

Check that both queues count traffic:

```ros
/queue/tree/print stats
0  name="upload" parent=ether1 packet-mark=no-mark rate=244112 packet-rate=30
   queued-bytes=0 queued-packets=0 bytes=201486 packets=203 dropped=0
1  name="download" parent=bridge packet-mark=no-mark rate=241416 packet-rate=30
   queued-bytes=0 queued-packets=0 bytes=200814 packets=199 dropped=0
```

To keep the delay low while the connection is full, add a queue type such as [FQ-CoDel](./queue-types/codel-fq-codel) or [CAKE](./queue-types/cake) to both queues.

## Packet marks and FastTrack

The default configuration has a FastTrack rule for established connections. FastTracked packets skip the mangle rules, so they get no packet mark, and they skip queues with `parent=global`. A queue tree that works with packet marks needs the connections of its traffic outside FastTrack.

The following examples do this with a connection mark. They change the FastTrack rule so that it takes only connections without a connection mark, and they mark the connections that the queues handle:

```ros
/ip/firewall/filter
set [find action=fasttrack-connection] connection-mark=no-mark
```

All other connections stay FastTracked.

## Give priority to voice traffic

Child queues with different priorities share the rate of their parent. `priority=1` is the highest and `priority=8` is the lowest. When the connection is full, each child first gets its `limit-at`, and then the queue with the higher priority gets the rest first.

This example gives upload priority to calls. IP phones and voice applications send their voice packets with DSCP 46. The first mangle rule marks the connections that carry such packets, which also keeps them out of FastTrack. The second rule marks the packets of these connections that leave through the WAN interface. All other packets have no packet mark and go to the `upload-other` queue:

```ros
/ip/firewall/filter
set [find action=fasttrack-connection] connection-mark=no-mark
/ip/firewall/mangle
add chain=forward dscp=46 connection-mark=no-mark \
    action=mark-connection new-connection-mark=voice
add chain=postrouting out-interface-list=WAN connection-mark=voice \
    action=mark-packet new-packet-mark=voice passthrough=no
/queue/tree
add name=upload parent=ether1 max-limit=20M
add name=upload-voice parent=upload packet-mark=voice priority=1 \
    limit-at=2M max-limit=20M
add name=upload-other parent=upload packet-mark=no-mark priority=8 \
    limit-at=18M max-limit=20M
```

Check that the voice queue counts the marked packets and the parent queue counts all upload:

```ros
/queue/tree/print stats
0  name="upload" parent=ether1 packet-mark="" rate=464496 packet-rate=57
   queued-bytes=0 queued-packets=0 bytes=436062 packets=431 dropped=0
1  name="upload-voice" parent=upload packet-mark=voice rate=239304
   packet-rate=29 queued-bytes=0 queued-packets=0 bytes=218010 packets=215
   dropped=0
2  name="upload-other" parent=upload packet-mark=no-mark rate=239384
   packet-rate=29 queued-bytes=0 queued-packets=0 bytes=218052 packets=216
   dropped=0
```

See [HTB](./htb-hierarchical-token-bucket) for how `limit-at`, `max-limit` and `priority` work between parent and child queues.

## Limit marked traffic in both directions

With `parent=global`, a queue limits its packet mark wherever the packets go. This example limits the devices of the address list `limited` to 2 Mbps upload and 10 Mbps download. The first two mangle rules mark the connections from and to these devices, which keeps them out of FastTrack. The other two rules mark the packets of these connections by direction:

```ros
/ip/firewall/address-list
add list=limited address=192.168.88.10
/ip/firewall/filter
set [find action=fasttrack-connection] connection-mark=no-mark
/ip/firewall/mangle
add chain=forward src-address-list=limited connection-mark=no-mark \
    action=mark-connection new-connection-mark=limited
add chain=forward dst-address-list=limited connection-mark=no-mark \
    action=mark-connection new-connection-mark=limited
add chain=forward connection-mark=limited src-address-list=limited \
    action=mark-packet new-packet-mark=limited-up passthrough=no
add chain=forward connection-mark=limited dst-address-list=limited \
    action=mark-packet new-packet-mark=limited-down passthrough=no
/queue/tree
add name=limited-up parent=global packet-mark=limited-up max-limit=2M
add name=limited-down parent=global packet-mark=limited-down \
    max-limit=10M
```

Check that both queues count traffic. The traffic of devices that are not in the address list does not go to these queues:

```ros
/queue/tree/print stats
0  name="limited-up" parent=global packet-mark=limited-up rate=232000
   packet-rate=29 queued-bytes=0 queued-packets=0 bytes=222000 packets=222
   dropped=0
1  name="limited-down" parent=global packet-mark=limited-down rate=232000
   packet-rate=29 queued-bytes=0 queued-packets=0 bytes=222000 packets=222
   dropped=0
```

## More properties

- `queue` selects the [queue type](./queue-types). A new queue uses `default-small`.
- `burst-limit`, `burst-threshold` and `burst-time` allow a higher rate for a short time. See [Queue Burst](./queue-burst).
- `bucket-size` controls how much traffic a queue can send in one burst after an idle time. See [HTB](./htb-hierarchical-token-bucket).

When a queue tree has an interface as its parent, `/queue/interface` shows `queue-tree` as the active queue of this interface.

## Read more

- [Simple queue](./simple-queue) - limits by address, network or interface without packet marks.
- [Queue types](./queue-types) - the queuing algorithms and their examples.
- [Packet flow](../packet-flow-in-routeros) - where the queues are in the path of a packet.
- [`/queue/tree` CLI reference](../../cli-reference/queue/tree) - all properties.
