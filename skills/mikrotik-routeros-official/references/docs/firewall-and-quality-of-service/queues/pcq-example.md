# PCQ example

> Per Connection Queue (PCQ) is a RouterOS queuing method for equalizing bandwidth among users, with examples showing how to set download/upload limits using Queue Tree and Simple Queues.

# PCQ example

Per Connection Queue (PCQ) gives every device on a network its own speed limit with one queue, instead of one queue for each device. PCQ sorts the traffic into sub-streams with its classifier, for example one sub-stream for each destination address, and limits each sub-stream to `pcq-rate`.

## Limit every device on a LAN

This example limits every device on the LAN 192.168.88.0/24 to 10 Mbit/s download and 5 Mbit/s upload.

### Step 1: add PCQ in Queue Types

Add one queue type for download and one for upload. `pcq-classifier=dst-address` gives every device its own sub-stream for download traffic, and `src-address` for upload traffic. `pcq-rate` is the limit for each sub-stream, so for each device, in bits per second; the `k` and `M` suffixes work:

```ros
/queue/type/add name="PCQ_download" kind=pcq pcq-rate=10M pcq-classifier=dst-address
/queue/type/add name="PCQ_upload" kind=pcq pcq-rate=5M pcq-classifier=src-address
```

`pcq-limit` is not a speed: it is the queue size of each sub-stream, in KiB (`50KiB` by default).

### Step 2: deploy the PCQ

#### Simple Queues option

One simple queue for the whole LAN applies both types. `queue` takes the upload type first, then the download type:

```ros
/queue/simple/add target=192.168.88.0/24 queue=PCQ_upload/PCQ_download
```

`/queue/simple/print stats` shows in `pcq-queues` how many sub-streams, here devices, the queue has.

#### Queue Tree option

Mark all packets with packet-marks upload/download (in this example, ether1-WAN is the public interface to the internet and ether2-LAN is the local interface where clients are connected):

```ros
/ip/firewall/mangle/add chain=prerouting action=mark-packet \
   in-interface=ether2-LAN new-packet-mark=client_upload
/ip/firewall/mangle/add chain=prerouting action=mark-packet \
   in-interface=ether1-WAN new-packet-mark=client_download
```

Then, add two queues, one for download and one for upload:

```ros
/queue/tree/add parent=global queue=PCQ_download packet-mark=client_download
/queue/tree/add parent=global queue=PCQ_upload packet-mark=client_upload
```

:::warning
Queues do not apply to FastTracked traffic, and the default configuration FastTracks established connections. Make sure the firewall does not FastTrack the traffic you want to limit, for example by disabling the FastTrack rule in `/ip/firewall/filter`.
:::
