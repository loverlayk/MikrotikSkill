# PCQ example

> Per Connection Queue (PCQ) is a RouterOS queuing method for equalizing bandwidth among users, with examples showing how to set download/upload limits using Queue Tree and Simple Queues.

# PCQ example

Per Connection Queue (PCQ) is a queuing discipline that can be used to dynamically equalize or shape traffic for multiple users, using little administration. It is possible to divide PCQ scenarios into three major groups: equal bandwidth for a number of users, certain bandwidth equal distribution between users, and unknown bandwidth equal distribution between users.

## Equal Bandwidth for a Number of Users

PCQ type can be used through the Queue Tree and Simple Queues to equalize the bandwidth [and set max limit] for a number of users. We will set the 64kbps download and 32kbps upload limits.

![](./img/pcq-example-01.webp)

### Step 1: add PCQ in Queue Types

Add two new entries - one for download and one for upload. `dst-address` is a classifier for the user's download traffic, and `src-address` for upload traffic:

```ros
/queue/type/add name="PCQ_download" kind=pcq pcq-rate=64000 pcq-classifier=dst-address
/queue/type/add name="PCQ_upload" kind=pcq pcq-rate=32000 pcq-classifier=src-address
 
```

### Step 2: deploy the PCQ

#### Queue Tree option

Mark all packets with packet-marks upload/download: (let's consider that ether1-WAN is the public interface to the Internet and ether2-LAN is a local interface where clients are connected):

```ros
/ip/firewall/mangle/add chain=prerouting action=mark-packet \
   in-interface=ether2-LAN new-packet-mark=client_upload
/ip/firewall/mangle/add chain=prerouting action=mark-packet \
   in-interface=ether1-WAN new-packet-mark=client_download
```

Then, two queue rules are required, one for download and one for upload:

```ros
/queue/tree/add parent=global queue=PCQ_download packet-mark=client_download
/queue/tree/add parent=global queue=PCQ_upload packet-mark=client_upload
```

#### Simple Queues option

Alternatively you can do it with one command like so:

```ros
/queue/simple/add target=192.168.0.0/24 queue=PCQ_upload/PCQ_download
```
