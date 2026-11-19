# PCQ example

> Per Connection Queue (PCQ) is a RouterOS queuing method for equalizing bandwidth among users, with examples showing how to set download/upload limits using Queue Tree and Simple Queues.

# PCQ example

Per Connection Queue (PCQ) gives every device on a network its own speed limit with one queue, instead of one queue for each device. PCQ sorts the traffic into sub-streams with its classifier, for example one sub-stream for each destination address, and limits each sub-stream to `pcq-rate`.

## Limit every device on a LAN

This example limits every device on the LAN 192.168.88.0/24 to 10 Mbit/s download and 5 Mbit/s upload.

:::warning
The queues of this example do not apply to FastTracked traffic, and the default configuration FastTracks established connections. Disable the FastTrack rule first, see [Before you start: FastTrack](./simple-queue#before-you-start-fasttrack).
:::

### Step 1: add PCQ in Queue Types

Add one queue type for download and one for upload. `pcq-classifier=dst-address` gives every device its own sub-stream for download traffic, and `src-address` for upload traffic. `pcq-rate` is the limit for each sub-stream, so for each device, in bits per second; the `k` and `M` suffixes work:

```ros
/queue/type
add name=PCQ_download kind=pcq pcq-rate=10M \
    pcq-classifier=dst-address
add name=PCQ_upload kind=pcq pcq-rate=5M pcq-classifier=src-address
```

`pcq-limit` is not a speed: it is the queue size of each sub-stream, in KiB (`50KiB` by default).

### Step 2: deploy the PCQ

#### Simple Queues option

One simple queue for the whole LAN applies both types. `queue` takes the upload type first, then the download type:

```ros
/queue/simple
add name=lan-pcq target=192.168.88.0/24 \
    queue=PCQ_upload/PCQ_download
```

`/queue/simple/print stats` shows in `pcq-queues` how many sub-streams, here devices, the queue has. In this output three devices upload at the same time. Each of them gets 5 Mbit/s, and the `rate` of the queue is the sum:

```ros
[admin@MikroTik] > /queue/simple/print stats
0  name="lan-pcq" target=192.168.88.0/24 rate=14.9Mbps/2.4kbps total-rate=0bps
   packet-rate=1254/5 total-packet-rate=0 queued-bytes=150000/0
   total-queued-bytes=0 queued-packets=100/0 total-queued-packets=0
   bytes=38369640/26830 total-bytes=0 packets=25695/166 total-packets=0
   dropped=24029/0 total-dropped=0 pcq-queues=3/3
```

#### Queue Tree option

Use the queue tree instead of the simple queue, not together with it. If you added the simple queue, remove it first with `/queue/simple/remove lan-pcq`. Mark the packets by the interface list they arrive from. In the default configuration, the `LAN` list has the interfaces where the clients are connected, and the `WAN` list has the interface to the Internet:

```ros
/ip/firewall/mangle
add chain=prerouting action=mark-packet \
    new-packet-mark=client_upload in-interface-list=LAN
add chain=prerouting action=mark-packet \
    new-packet-mark=client_download in-interface-list=WAN
```

Then, add two queues, one for download and one for upload:

```ros
/queue/tree
add name=pcq-download parent=global queue=PCQ_download \
    packet-mark=client_download
add name=pcq-upload parent=global queue=PCQ_upload \
    packet-mark=client_upload
```

`/queue/tree/print stats` shows `pcq-queues` for each queue in the same way.
