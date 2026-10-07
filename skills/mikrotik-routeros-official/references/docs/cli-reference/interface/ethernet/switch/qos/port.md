# port

> This sub-menu configures QoS settings for individual switch ports. It allows you to assign a QoS profile to ingress packets arriving on a specific port. If the port is configured as trusted, the assigned profile can...

-----------

## interface/ethernet/switch/qos/port 
**Syscap:** rbswitch and crs_prestera
**Type:** Directory

This sub-menu configures QoS settings for individual switch ports. It allows you to assign a QoS profile to ingress packets arriving on a specific port. If the port is configured as trusted, the assigned profile can be overridden by match rules based on packet header values.

By default, all ports are untrusted and receive the default QoS profile (Best-Effort, PCP=0, DSCP=0). In this default state, priority fields are cleared from egress packets.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="profile" typ="enum" syscap="crs_prestera">QoS profile to assign to ingress packets by default.</ArgTableRow>
<ArgTableRow arg="map" typ="enum" syscap="crs_prestera">QoS Packet-to-Profile mapping.</ArgTableRow>
<ArgTableRow arg="trust-l2" typ="enum (ignore | trust | keep) { ignore:0, trust:1, keep:2 }" syscap="crs_prestera">Trust Layer 2 header (PCP) for QoS mapping.</ArgTableRow>
<ArgTableRow arg="trust-l3" typ="enum (ignore | trust | keep) { ignore:0, trust:1, keep:2 }" syscap="crs_prestera">Trust Layer 3 header (DSCP) for QoS mapping.</ArgTableRow>
<ArgTableRow arg="tx-manager" typ="enum" syscap="crs_prestera">QoS Tx Manager for egress traffic on this port.</ArgTableRow>
<ArgTableRow arg="pfc" typ="enum" syscap="!prestera-ac3">Priority Flow Control profile for ingress traffic on this port.</ArgTableRow>
<ArgTableRow arg="egress-rate-queue0" typ="num" syscap="switch-rate">Egress rate limit for queue 0.</ArgTableRow>
<ArgTableRow arg="egress-rate-queue1" typ="num" syscap="switch-rate">Egress rate limit for queue 1.</ArgTableRow>
<ArgTableRow arg="egress-rate-queue2" typ="num" syscap="switch-rate">Egress rate limit for queue 2.</ArgTableRow>
<ArgTableRow arg="egress-rate-queue3" typ="num" syscap="switch-rate">Egress rate limit for queue 3.</ArgTableRow>
<ArgTableRow arg="egress-rate-queue4" typ="num" syscap="switch-rate">Egress rate limit for queue 4.</ArgTableRow>
<ArgTableRow arg="egress-rate-queue5" typ="num" syscap="switch-rate">Egress rate limit for queue 5.</ArgTableRow>
<ArgTableRow arg="egress-rate-queue6" typ="num" syscap="switch-rate">Egress rate limit for queue 6.</ArgTableRow>
<ArgTableRow arg="egress-rate-queue7" typ="num" syscap="switch-rate">Egress rate limit for queue 7.</ArgTableRow>
</ArgTable>
**Port Stats**

```ros
[admin@Mikrotik] /interface/ethernet/switch/qos/port> print stats where name=ether2
                  name:     ether2
             tx-packet:      2 887
               tx-byte:  3 938 897
           drop-packet:      1 799
             drop-byte:  2 526 144
      tx-queue0-packet:         50
      tx-queue1-packet:      1 871
      tx-queue3-packet:        774
      tx-queue5-packet:        192
        tx-queue0-byte:      3 924
        tx-queue1-byte:  2 468 585
        tx-queue3-byte:  1 174 932
        tx-queue5-byte:    291 456
    drop-queue1-packet:      1 799
      drop-queue1-byte:  2 526 144
```

**Port Resources/Usage**

:::danger
Due to hardware limitations, some switch chip models may break traffic flow while accessing QoS port `usage` data. Use port `usage` for diagnostics/troubleshooting only. For monitoring, use QoS `monitor` or Port `stats` instead.
:::

```ros
[admin@crs326] /interface/ethernet/switch/qos/port> print usage where name=ether2
                 name:  ether2
           packet-cap:     136
           packet-use:       5
             byte-cap:  35 840
             byte-use:   9 472
    queue0-packet-cap:     130
    queue0-packet-use:       1
    queue1-packet-cap:       5
    queue1-packet-use:       4
    queue3-packet-cap:      65
    queue3-packet-use:       2
      queue0-byte-cap:  24 576
      queue0-byte-use:     256
      queue1-byte-cap:   7 680
      queue1-byte-use:   6 144
      queue3-byte-cap:  14 080
      queue3-byte-use:   3 072
```

**Port PFC Stats (Previous Generations)**
```ros
[admin@crs317] /interface/ethernet/switch/qos/port> print pfc interval=1 where running
                 name:  sfp-sfpplus1 sfp-sfpplus2   ether1
                  pfc:          roce     disabled disabled
               pfc-tx:            46            
        pfc-paused-tc:             3            
 pfc3-pause-threshold:     1 048 576            
pfc3-resume-threshold:        10 240            
             pfc3-use:     1 075 200
```

**Port PFC Stats (New Generations)**
```routeros
[admin@crs812] /interface/ethernet/switch/qos/port> print pfc interval=1 where pfc=roce
                 name:       sfp56-5 
                  pfc:          roce
             rx-pause:           287              
             tx-pause:            46             
             pfc3-use:     2 184 200 
```

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Port name.</ArgTableRow>
<ArgTableRow arg="switch" typ="enum">Switch chip name.</ArgTableRow>
<ArgTableRow arg="tx-packet" typ="multi { counter: num
 }">The total number of packets transmitted via this port.</ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="multi { counter: num
 }">The total number of bytes transmitted via this port.</ArgTableRow>
<ArgTableRow arg="packet-use" typ="num" syscap="!prestera-cpss">Port's packet usage. The number of packets currently enqueued in all port's queues.</ArgTableRow>
<ArgTableRow arg="byte-use" typ="num">Port's byte usage. The size of hardware buffers (in bytes) that are currently allocated for the enqueued packets. Since the buffers are allocated by blocks (usually - 256B each), the allocated buffer size can be bigger than the actual payload.</ArgTableRow>
<ArgTableRow arg="queue0-shared-packet-cap" typ="num" syscap="prestera-bc2">Shared queue capacity (individual queue capacity + shared buffers) for queue 0.</ArgTableRow>
<ArgTableRow arg="queue1-shared-packet-cap" typ="num" syscap="prestera-bc2">Shared queue capacity (individual queue capacity + shared buffers) for queue 1.</ArgTableRow>
<ArgTableRow arg="queue2-shared-packet-cap" typ="num" syscap="prestera-bc2">Shared queue capacity (individual queue capacity + shared buffers) for queue 2.</ArgTableRow>
<ArgTableRow arg="queue3-shared-packet-cap" typ="num" syscap="prestera-bc2">Shared queue capacity (individual queue capacity + shared buffers) for queue 3.</ArgTableRow>
<ArgTableRow arg="queue4-shared-packet-cap" typ="num" syscap="prestera-bc2">Shared queue capacity (individual queue capacity + shared buffers) for queue 4.</ArgTableRow>
<ArgTableRow arg="queue5-shared-packet-cap" typ="num" syscap="prestera-bc2">Shared queue capacity (individual queue capacity + shared buffers) for queue 5.</ArgTableRow>
<ArgTableRow arg="queue6-shared-packet-cap" typ="num" syscap="prestera-bc2">Shared queue capacity (individual queue capacity + shared buffers) for queue 6.</ArgTableRow>
<ArgTableRow arg="queue7-shared-packet-cap" typ="num" syscap="prestera-bc2">Shared queue capacity (individual queue capacity + shared buffers) for queue 7.</ArgTableRow>
<ArgTableRow arg="queue0-shared-byte-cap" typ="num" syscap="!prestera-ac3">Shared queue capacity (individual queue capacity + shared buffers) for queue 0.</ArgTableRow>
<ArgTableRow arg="queue1-shared-byte-cap" typ="num" syscap="!prestera-ac3">Shared queue capacity (individual queue capacity + shared buffers) for queue 1.</ArgTableRow>
<ArgTableRow arg="queue2-shared-byte-cap" typ="num" syscap="!prestera-ac3">Shared queue capacity (individual queue capacity + shared buffers) for queue 2.</ArgTableRow>
<ArgTableRow arg="queue3-shared-byte-cap" typ="num" syscap="!prestera-ac3">Shared queue capacity (individual queue capacity + shared buffers) for queue 3.</ArgTableRow>
<ArgTableRow arg="queue4-shared-byte-cap" typ="num" syscap="!prestera-ac3">Shared queue capacity (individual queue capacity + shared buffers) for queue 4.</ArgTableRow>
<ArgTableRow arg="queue5-shared-byte-cap" typ="num" syscap="!prestera-ac3">Shared queue capacity (individual queue capacity + shared buffers) for queue 5.</ArgTableRow>
<ArgTableRow arg="queue6-shared-byte-cap" typ="num" syscap="!prestera-ac3">Shared queue capacity (individual queue capacity + shared buffers) for queue 6.</ArgTableRow>
<ArgTableRow arg="queue7-shared-byte-cap" typ="num" syscap="!prestera-ac3">Shared queue capacity (individual queue capacity + shared buffers) for queue 7.</ArgTableRow>
<ArgTableRow arg="queue0-packet-cap" typ="num" syscap="!prestera-cpss">Individual queue capacity. The maximum number of packets that can be enqueued in queue 0.</ArgTableRow>
<ArgTableRow arg="queue1-packet-cap" typ="num" syscap="!prestera-cpss">Individual queue capacity. The maximum number of packets that can be enqueued in queue 1.</ArgTableRow>
<ArgTableRow arg="queue2-packet-cap" typ="num" syscap="!prestera-cpss">Individual queue capacity. The maximum number of packets that can be enqueued in queue 2.</ArgTableRow>
<ArgTableRow arg="queue3-packet-cap" typ="num" syscap="!prestera-cpss">Individual queue capacity. The maximum number of packets that can be enqueued in queue 3.</ArgTableRow>
<ArgTableRow arg="queue4-packet-cap" typ="num" syscap="!prestera-cpss">Individual queue capacity. The maximum number of packets that can be enqueued in queue 4.</ArgTableRow>
<ArgTableRow arg="queue5-packet-cap" typ="num" syscap="!prestera-cpss">Individual queue capacity. The maximum number of packets that can be enqueued in queue 5.</ArgTableRow>
<ArgTableRow arg="queue6-packet-cap" typ="num" syscap="!prestera-cpss">Individual queue capacity. The maximum number of packets that can be enqueued in queue 6.</ArgTableRow>
<ArgTableRow arg="queue7-packet-cap" typ="num" syscap="!prestera-cpss">Individual queue capacity. The maximum number of packets that can be enqueued in queue 7.</ArgTableRow>
<ArgTableRow arg="queue0-byte-cap" typ="num" syscap="!prestera-cpss">Individual queue capacity. The maximum number of bytes that can be enqueued in queue 0.</ArgTableRow>
<ArgTableRow arg="queue1-byte-cap" typ="num" syscap="!prestera-cpss">Individual queue capacity. The maximum number of bytes that can be enqueued in queue 1.</ArgTableRow>
<ArgTableRow arg="queue2-byte-cap" typ="num" syscap="!prestera-cpss">Individual queue capacity. The maximum number of bytes that can be enqueued in queue 2.</ArgTableRow>
<ArgTableRow arg="queue3-byte-cap" typ="num" syscap="!prestera-cpss">Individual queue capacity. The maximum number of bytes that can be enqueued in queue 3.</ArgTableRow>
<ArgTableRow arg="queue4-byte-cap" typ="num" syscap="!prestera-cpss">Individual queue capacity. The maximum number of bytes that can be enqueued in queue 4.</ArgTableRow>
<ArgTableRow arg="queue5-byte-cap" typ="num" syscap="!prestera-cpss">Individual queue capacity. The maximum number of bytes that can be enqueued in queue 5.</ArgTableRow>
<ArgTableRow arg="queue6-byte-cap" typ="num" syscap="!prestera-cpss">Individual queue capacity. The maximum number of bytes that can be enqueued in queue 6.</ArgTableRow>
<ArgTableRow arg="queue7-byte-cap" typ="num" syscap="!prestera-cpss">Individual queue capacity. The maximum number of bytes that can be enqueued in queue 7.</ArgTableRow>
<ArgTableRow arg="queue0-packet-use" typ="num" syscap="!prestera-cpss">Queue packet usage. The number of enqueued packets in queue 0.</ArgTableRow>
<ArgTableRow arg="queue1-packet-use" typ="num" syscap="!prestera-cpss">Queue packet usage. The number of enqueued packets in queue 1.</ArgTableRow>
<ArgTableRow arg="queue2-packet-use" typ="num" syscap="!prestera-cpss">Queue packet usage. The number of enqueued packets in queue 2.</ArgTableRow>
<ArgTableRow arg="queue3-packet-use" typ="num" syscap="!prestera-cpss">Queue packet usage. The number of enqueued packets in queue 3.</ArgTableRow>
<ArgTableRow arg="queue4-packet-use" typ="num" syscap="!prestera-cpss">Queue packet usage. The number of enqueued packets in queue 4.</ArgTableRow>
<ArgTableRow arg="queue5-packet-use" typ="num" syscap="!prestera-cpss">Queue packet usage. The number of enqueued packets in queue 5.</ArgTableRow>
<ArgTableRow arg="queue6-packet-use" typ="num" syscap="!prestera-cpss">Queue packet usage. The number of enqueued packets in queue 6.</ArgTableRow>
<ArgTableRow arg="queue7-packet-use" typ="num" syscap="!prestera-cpss">Queue packet usage. The number of enqueued packets in queue 7.</ArgTableRow>
<ArgTableRow arg="queue0-byte-use" typ="num">Queue buffer usage (in bytes) for queue 0.</ArgTableRow>
<ArgTableRow arg="queue1-byte-use" typ="num">Queue buffer usage (in bytes) for queue 1.</ArgTableRow>
<ArgTableRow arg="queue2-byte-use" typ="num">Queue buffer usage (in bytes) for queue 2.</ArgTableRow>
<ArgTableRow arg="queue3-byte-use" typ="num">Queue buffer usage (in bytes) for queue 3.</ArgTableRow>
<ArgTableRow arg="queue4-byte-use" typ="num">Queue buffer usage (in bytes) for queue 4.</ArgTableRow>
<ArgTableRow arg="queue5-byte-use" typ="num">Queue buffer usage (in bytes) for queue 5.</ArgTableRow>
<ArgTableRow arg="queue6-byte-use" typ="num">Queue buffer usage (in bytes) for queue 6.</ArgTableRow>
<ArgTableRow arg="queue7-byte-use" typ="num">Queue buffer usage (in bytes) for queue 7.</ArgTableRow>
<ArgTableRow arg="byte-max" typ="num" syscap="prestera-bc2">Maximum port buffer fill level (in bytes). Use the reset-counters command to reset values.</ArgTableRow>
<ArgTableRow arg="queue0-byte-max" typ="num" syscap="!prestera-ac3">Maximum queue buffer fill level (in bytes) for queue 0.</ArgTableRow>
<ArgTableRow arg="queue1-byte-max" typ="num" syscap="!prestera-ac3">Maximum queue buffer fill level (in bytes) for queue 1.</ArgTableRow>
<ArgTableRow arg="queue2-byte-max" typ="num" syscap="!prestera-ac3">Maximum queue buffer fill level (in bytes) for queue 2.</ArgTableRow>
<ArgTableRow arg="queue3-byte-max" typ="num" syscap="!prestera-ac3">Maximum queue buffer fill level (in bytes) for queue 3.</ArgTableRow>
<ArgTableRow arg="queue4-byte-max" typ="num" syscap="!prestera-ac3">Maximum queue buffer fill level (in bytes) for queue 4.</ArgTableRow>
<ArgTableRow arg="queue5-byte-max" typ="num" syscap="!prestera-ac3">Maximum queue buffer fill level (in bytes) for queue 5.</ArgTableRow>
<ArgTableRow arg="queue6-byte-max" typ="num" syscap="!prestera-ac3">Maximum queue buffer fill level (in bytes) for queue 6.</ArgTableRow>
<ArgTableRow arg="queue7-byte-max" typ="num" syscap="!prestera-ac3">Maximum queue buffer fill level (in bytes) for queue 7.</ArgTableRow>
<ArgTableRow arg="pfc0-pause-threshold" typ="num" syscap="prestera-bc2">Pause threshold of traffic class 0.</ArgTableRow>
<ArgTableRow arg="pfc1-pause-threshold" typ="num" syscap="prestera-bc2">Pause threshold of traffic class 1.</ArgTableRow>
<ArgTableRow arg="pfc2-pause-threshold" typ="num" syscap="prestera-bc2">Pause threshold of traffic class 2.</ArgTableRow>
<ArgTableRow arg="pfc3-pause-threshold" typ="num" syscap="prestera-bc2">Pause threshold of traffic class 3.</ArgTableRow>
<ArgTableRow arg="pfc4-pause-threshold" typ="num" syscap="prestera-bc2">Pause threshold of traffic class 4.</ArgTableRow>
<ArgTableRow arg="pfc5-pause-threshold" typ="num" syscap="prestera-bc2">Pause threshold of traffic class 5.</ArgTableRow>
<ArgTableRow arg="pfc6-pause-threshold" typ="num" syscap="prestera-bc2">Pause threshold of traffic class 6.</ArgTableRow>
<ArgTableRow arg="pfc7-pause-threshold" typ="num" syscap="prestera-bc2">Pause threshold of traffic class 7.</ArgTableRow>
<ArgTableRow arg="pfc0-resume-threshold" typ="num" syscap="prestera-bc2">Resume threshold of traffic class 0.</ArgTableRow>
<ArgTableRow arg="pfc1-resume-threshold" typ="num" syscap="prestera-bc2">Resume threshold of traffic class 1.</ArgTableRow>
<ArgTableRow arg="pfc2-resume-threshold" typ="num" syscap="prestera-bc2">Resume threshold of traffic class 2.</ArgTableRow>
<ArgTableRow arg="pfc3-resume-threshold" typ="num" syscap="prestera-bc2">Resume threshold of traffic class 3.</ArgTableRow>
<ArgTableRow arg="pfc4-resume-threshold" typ="num" syscap="prestera-bc2">Resume threshold of traffic class 4.</ArgTableRow>
<ArgTableRow arg="pfc5-resume-threshold" typ="num" syscap="prestera-bc2">Resume threshold of traffic class 5.</ArgTableRow>
<ArgTableRow arg="pfc6-resume-threshold" typ="num" syscap="prestera-bc2">Resume threshold of traffic class 6.</ArgTableRow>
<ArgTableRow arg="pfc7-resume-threshold" typ="num" syscap="prestera-bc2">Resume threshold of traffic class 7.</ArgTableRow>
<ArgTableRow arg="pfc0-use" typ="num" syscap="!prestera-ac3">Current buffer usage of traffic class 0 (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.</ArgTableRow>
<ArgTableRow arg="pfc1-use" typ="num" syscap="!prestera-ac3">Current buffer usage of traffic class 1 (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.</ArgTableRow>
<ArgTableRow arg="pfc2-use" typ="num" syscap="!prestera-ac3">Current buffer usage of traffic class 2 (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.</ArgTableRow>
<ArgTableRow arg="pfc3-use" typ="num" syscap="!prestera-ac3">Current buffer usage of traffic class 3 (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.</ArgTableRow>
<ArgTableRow arg="pfc4-use" typ="num" syscap="!prestera-ac3">Current buffer usage of traffic class 4 (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.</ArgTableRow>
<ArgTableRow arg="pfc5-use" typ="num" syscap="!prestera-ac3">Current buffer usage of traffic class 5 (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.</ArgTableRow>
<ArgTableRow arg="pfc6-use" typ="num" syscap="!prestera-ac3">Current buffer usage of traffic class 6 (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.</ArgTableRow>
<ArgTableRow arg="pfc7-use" typ="num" syscap="!prestera-ac3">Current buffer usage of traffic class 7 (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.</ArgTableRow>
<ArgTableRow arg="pfc-paused-tc" typ="multi { array-id, tc: num
 }" syscap="prestera-bc2">The list of traffic classes that should be paused. PFC pause frames (XOFF) are periodically sent with the listed timers set from this port.</ArgTableRow>
<ArgTableRow arg="pfc-unknown" typ="multi { counter: num
 }" syscap="prestera-bc2">Unknown PFC frame count.</ArgTableRow>
<ArgTableRow arg="pfc-rx" typ="multi { counter: num
 }" syscap="prestera-bc2">Received PFC frame count.</ArgTableRow>
<ArgTableRow arg="pfc-tx" typ="num" syscap="prestera-bc2">Transmitted PFC frame count.</ArgTableRow>
<ArgTableRow arg="rx-pause" typ="multi { counter: num
 }" syscap="prestera-cpss">Received pause frame count.</ArgTableRow>
<ArgTableRow arg="tx-pause" typ="multi { counter: num
 }" syscap="prestera-cpss">Transmitted pause frame count.</ArgTableRow>
<ArgTableRow arg="tx-queue0-packet" typ="multi { counter: num
 }">The number of packets transmitted via this port from queue 0.</ArgTableRow>
<ArgTableRow arg="tx-queue0-byte" typ="multi { counter: num
 }">The number of bytes transmitted via this port from queue 0.</ArgTableRow>
<ArgTableRow arg="tx-queue1-packet" typ="multi { counter: num
 }">The number of packets transmitted via this port from queue 1.</ArgTableRow>
<ArgTableRow arg="tx-queue1-byte" typ="multi { counter: num
 }">The number of bytes transmitted via this port from queue 1.</ArgTableRow>
<ArgTableRow arg="tx-queue2-packet" typ="multi { counter: num
 }">The number of packets transmitted via this port from queue 2.</ArgTableRow>
<ArgTableRow arg="tx-queue2-byte" typ="multi { counter: num
 }">The number of bytes transmitted via this port from queue 2.</ArgTableRow>
<ArgTableRow arg="tx-queue3-packet" typ="multi { counter: num
 }">The number of packets transmitted via this port from queue 3.</ArgTableRow>
<ArgTableRow arg="tx-queue3-byte" typ="multi { counter: num
 }">The number of bytes transmitted via this port from queue 3.</ArgTableRow>
<ArgTableRow arg="tx-queue4-packet" typ="multi { counter: num
 }">The number of packets transmitted via this port from queue 4.</ArgTableRow>
<ArgTableRow arg="tx-queue4-byte" typ="multi { counter: num
 }">The number of bytes transmitted via this port from queue 4.</ArgTableRow>
<ArgTableRow arg="tx-queue5-packet" typ="multi { counter: num
 }">The number of packets transmitted via this port from queue 5.</ArgTableRow>
<ArgTableRow arg="tx-queue5-byte" typ="multi { counter: num
 }">The number of bytes transmitted via this port from queue 5.</ArgTableRow>
<ArgTableRow arg="tx-queue6-packet" typ="multi { counter: num
 }">The number of packets transmitted via this port from queue 6.</ArgTableRow>
<ArgTableRow arg="tx-queue6-byte" typ="multi { counter: num
 }">The number of bytes transmitted via this port from queue 6.</ArgTableRow>
<ArgTableRow arg="tx-queue7-packet" typ="multi { counter: num
 }">The number of packets transmitted via this port from queue 7.</ArgTableRow>
<ArgTableRow arg="tx-queue7-byte" typ="multi { counter: num
 }">The number of bytes transmitted via this port from queue 7.</ArgTableRow>
<ArgTableRow arg="tx-drop-packet" typ="multi { counter: num
 }">Total transmitted packets dropped.</ArgTableRow>
<ArgTableRow arg="tx-drop-byte" typ="multi { counter: num
 }">Total transmitted bytes dropped.</ArgTableRow>
<ArgTableRow arg="tx-drop-queue0-packet" typ="multi { counter: num
 }">The number of packets dropped from queue 0.</ArgTableRow>
<ArgTableRow arg="tx-drop-queue0-byte" typ="multi { counter: num
 }">The number of bytes dropped from queue 0.</ArgTableRow>
<ArgTableRow arg="tx-drop-queue1-packet" typ="multi { counter: num
 }">The number of packets dropped from queue 1.</ArgTableRow>
<ArgTableRow arg="tx-drop-queue1-byte" typ="multi { counter: num
 }">The number of bytes dropped from queue 1.</ArgTableRow>
<ArgTableRow arg="tx-drop-queue2-packet" typ="multi { counter: num
 }">The number of packets dropped from queue 2.</ArgTableRow>
<ArgTableRow arg="tx-drop-queue2-byte" typ="multi { counter: num
 }">The number of bytes dropped from queue 2.</ArgTableRow>
<ArgTableRow arg="tx-drop-queue3-packet" typ="multi { counter: num
 }">The number of packets dropped from queue 3.</ArgTableRow>
<ArgTableRow arg="tx-drop-queue3-byte" typ="multi { counter: num
 }">The number of bytes dropped from queue 3.</ArgTableRow>
<ArgTableRow arg="tx-drop-queue4-packet" typ="multi { counter: num
 }">The number of packets dropped from queue 4.</ArgTableRow>
<ArgTableRow arg="tx-drop-queue4-byte" typ="multi { counter: num
 }">The number of bytes dropped from queue 4.</ArgTableRow>
<ArgTableRow arg="tx-drop-queue5-packet" typ="multi { counter: num
 }">The number of packets dropped from queue 5.</ArgTableRow>
<ArgTableRow arg="tx-drop-queue5-byte" typ="multi { counter: num
 }">The number of bytes dropped from queue 5.</ArgTableRow>
<ArgTableRow arg="tx-drop-queue6-packet" typ="multi { counter: num
 }">The number of packets dropped from queue 6.</ArgTableRow>
<ArgTableRow arg="tx-drop-queue6-byte" typ="multi { counter: num
 }">The number of bytes dropped from queue 6.</ArgTableRow>
<ArgTableRow arg="tx-drop-queue7-packet" typ="multi { counter: num
 }">The number of packets dropped from queue 7.</ArgTableRow>
<ArgTableRow arg="tx-drop-queue7-byte" typ="multi { counter: num
 }">The number of bytes dropped from queue 7.</ArgTableRow>
</ArgTable>
