# CoDel and FQ-CoDel

> CoDel and FQ-CoDel are RouterOS queue types that control how long packets wait in a queue. This page shows how to use FQ-CoDel on a rate-limited Internet connection with a simple queue or a queue tree, and CoDel on...

# CoDel and FQ-CoDel

Controlled Delay (CoDel) controls the time that packets wait in the queue, not the number of packets in it. When packets wait longer than the target time for a whole interval, CoDel starts to drop packets. The senders then slow down and the queue gets shorter.

RouterOS has two kinds:

- `codel` - one CoDel queue for all traffic. The packets of all devices wait in the same queue.
- `fq-codel` - Fair Queuing CoDel. It sorts packets into flows, gives each flow its own CoDel queue and lets the flows take turns.

Both kinds have no rate limit of their own. They work under the rate limit of a simple queue or a queue tree, where the queue builds up.

The two main settings have the same meaning in both kinds:

- `codel-target`, `fq-codel-target` - the waiting time that the queue accepts. The default is 5 ms.
- `codel-interval`, `fq-codel-interval` - the time over which the queue checks the waiting time. Set it to about the round-trip time of the connections. The default is 100 ms.

## Limit an Internet connection with FQ-CoDel

On an Internet connection that several devices share, one upload or download fills the queue of a FIFO rate limit, and the packets of all other devices wait behind it. With FQ-CoDel, the other flows have their own queues and do not wait behind the transfer. Use `fq-codel`, not `codel`, on a connection that several devices share.

This example limits the LAN to 20 Mbps upload and 100 Mbps download. Set the limits a little less than the real rates of the Internet connection, so that the queue builds up in the router.

Simple queues do not limit FastTracked connections, and the default configuration has a FastTrack rule for established connections. The first two lines of the example disable this rule. See [Simple queue](../simple-queue) for other ways to take traffic off FastTrack.

```ros
/ip/firewall/filter
disable [find action=fasttrack-connection]
/queue/type
add name=fq-codel-wan kind=fq-codel
/queue/simple
add name=lan target=192.168.88.0/24 max-limit=20M/100M \
    queue=fq-codel-wan/fq-codel-wan
```

Check that the queue counts the traffic of the LAN:

```ros
/queue/simple/print bytes where name=lan
Columns: NAME, TARGET, BYTES, TOTAL-BYTES
# NAME  TARGET           BYTES          TOTAL-BYTES
0 lan   192.168.88.0/24  710027/696920            0
```

## Limit an Internet connection with a queue tree

A queue tree with an interface as its parent limits the traffic that leaves the router through this interface. Upload leaves through the WAN interface, and download leaves through the LAN interface. `packet-mark=no-mark` matches the packets that have no packet mark, so this example needs no mangle rules. A queue tree with an interface as the parent also limits FastTracked traffic, so the FastTrack rule stays as it is.

In the default configuration, the WAN interface is `ether1` and the LAN interface is `bridge`:

```ros
/queue/type
add name=fq-codel-wan kind=fq-codel
/queue/tree
add name=upload parent=ether1 packet-mark=no-mark max-limit=20M \
    queue=fq-codel-wan
add name=download parent=bridge packet-mark=no-mark max-limit=100M \
    queue=fq-codel-wan
```

The `download` queue limits all packets that leave through `bridge`, also the packets that the router itself sends to the LAN. It does not limit traffic that the bridge forwards between its own ports.

Check that both queues count traffic:

```ros
/queue/tree/print stats
0  name="upload" parent=ether1 packet-mark=no-mark rate=891472 packet-rate=102
   queued-bytes=0 queued-packets=0 bytes=710418 packets=605 dropped=0
1  name="download" parent=bridge packet-mark=no-mark rate=947032
   packet-rate=106 queued-bytes=0 queued-packets=0 bytes=717584 packets=608
   dropped=0
```

Use either the simple queue or the queue tree, not both for the same traffic.

## Use CoDel on a rate limit

`codel` controls the waiting time in one queue for all traffic. This example uses it for the rate limit of one server. As in the first example, the first two lines disable the FastTrack rule:

```ros
/ip/firewall/filter
disable [find action=fasttrack-connection]
/queue/type
add name=codel-server kind=codel
/queue/simple
add name=server target=192.168.88.10/32 max-limit=10M/10M \
    queue=codel-server/codel-server
```

Check that the queue counts the traffic of the server:

```ros
/queue/simple/print bytes where name=server
Columns: NAME, TARGET, BYTES, TOTAL-BYTES
# NAME    TARGET            BYTES          TOTAL-BYTES
0 server  192.168.88.10/32  178000/178000            0
```

## Read more

- [CAKE](./cake) - flow and host fairness with a built-in shaper.
- [Queue types](./) - all kinds and the default queue types.
- [`/queue/type` CLI reference](../../../cli-reference/queue/type) - all properties.
