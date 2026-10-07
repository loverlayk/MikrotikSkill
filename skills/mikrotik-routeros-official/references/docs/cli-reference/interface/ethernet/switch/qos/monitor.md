# monitor

> Monitors hardware QoS resources.

-----------

## interface/ethernet/switch/qos/monitor 
**Syscap:** rbswitch and crs_prestera
**Type:** Command

Monitors hardware QoS resources.

```ros
[admin@crs312] /interface/ethernet/switch/qos> monitor once
           total-packet-cap: 11 480   
           total-packet-use: 0        
             total-byte-cap: 2648.0KiB
             total-byte-use: 0        
       multicast-packet-cap: 1 148    
       multicast-packet-use: 0        
         multicast-byte-cap: 264.8KiB 
         multicast-byte-use: 0        
  mirror-ingress-packet-cap: 1 148    
  mirror-ingress-packet-use: 0        
    mirror-ingress-byte-cap: 264.8KiB 
    mirror-ingress-byte-use: 0        
   mirror-egress-packet-cap: 1 148    
   mirror-egress-packet-use: 0        
     mirror-egress-byte-cap: 264.8KiB 
     mirror-egress-byte-use: 0        
      lossy-pool-packet-cap: 2 301    
      lossy-pool-packet-use: 0        
   lossless-pool-packet-cap: 2 301    
   lossless-pool-packet-use: 0        
        lossy-pool-byte-cap: 530.0KiB 
        lossy-pool-byte-use: 0        
     lossless-pool-byte-cap: 530.0KiB 
     lossless-pool-byte-use: 0 
```

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="total-packet-cap" typ="num" syscap="!prestera-cpss">Total packet capacity. The maximum number of hardware packet descriptors that the device can store in all queues.</ArgTableRow>
<ArgTableRow arg="total-packet-use" typ="num" syscap="!prestera-cpss">Total packet usage. The current number of packet descriptors residing in the hardware memory.</ArgTableRow>
<ArgTableRow arg="total-byte-cap" typ="num">Total tx memory capacity.</ArgTableRow>
<ArgTableRow arg="total-byte-use" typ="num">Total tx memory usage. The current number of bytes occupied by the packets in all tx queues.</ArgTableRow>
<ArgTableRow arg="multicast-packet-cap" typ="num" syscap="!prestera-cpss">Multicast packet capacity. The maximum number of hardware packet descriptors that can be used by multicast/broadcast traffic. Depends on the `multicast-buffers` setting.</ArgTableRow>
<ArgTableRow arg="multicast-packet-use" typ="num" syscap="!prestera-cpss">Multicast packet usage. The hardware makes a copy of the packet descriptor for each multicast destination.</ArgTableRow>
<ArgTableRow arg="multicast-byte-cap" typ="num" syscap="!prestera-ac3">Multicast byte capacity.</ArgTableRow>
<ArgTableRow arg="multicast-byte-use" typ="num" syscap="prestera-bc2">Multicast byte usage.</ArgTableRow>
<ArgTableRow arg="mirror-ingress-packet-cap" typ="num" syscap="!prestera-cpss">Ingress mirror packet capacity. The maximum number of hardware packet descriptors that can be used by ingress mirrored traffic. Depends on the `mirror-buffers` setting.</ArgTableRow>
<ArgTableRow arg="mirror-ingress-packet-use" typ="num" syscap="!prestera-cpss">Ingress mirror packet usage.</ArgTableRow>
<ArgTableRow arg="mirror-ingress-byte-cap" typ="num" syscap="prestera-bc2">Ingress mirror byte capacity. Depends on the `mirror-buffers` setting.</ArgTableRow>
<ArgTableRow arg="mirror-ingress-byte-use" typ="num" syscap="prestera-bc2">Ingress mirror byte usage.</ArgTableRow>
<ArgTableRow arg="mirror-egress-packet-cap" typ="num" syscap="!prestera-cpss">Egress mirror packet capacity. The maximum number of hardware packet descriptors that can be used by egress mirrored traffic. Depends on the `mirror-buffers` setting.</ArgTableRow>
<ArgTableRow arg="mirror-egress-packet-use" typ="num" syscap="!prestera-cpss">Egress mirror packet usage.</ArgTableRow>
<ArgTableRow arg="mirror-egress-byte-cap" typ="num" syscap="prestera-bc2">Egress mirror byte capacity. Depends on the `mirror-buffers` setting.</ArgTableRow>
<ArgTableRow arg="mirror-egress-byte-use" typ="num" syscap="prestera-bc2">Egress mirror byte usage.</ArgTableRow>
<ArgTableRow arg="shared-packet-cap" typ="num" syscap="prestera-ac3">Shared packet capacity. The maximum number of hardware packet descriptors that can be shared between ports and tx queues. Depends on the `shared-buffers` setting.</ArgTableRow>
<ArgTableRow arg="shared-packet-use" typ="num" syscap="prestera-ac3">Shared packet usage. The current number of shared packet descriptors used by all tx queues.</ArgTableRow>
<ArgTableRow arg="shared-byte-cap" typ="num" syscap="prestera-ac3">Shared tx memory capacity. Depends on the `shared-buffers` setting.</ArgTableRow>
<ArgTableRow arg="shared-byte-use" typ="num" syscap="prestera-ac3">Shared tx memory usage. The current number of shared buffers occupied by the packets in all tx queues.</ArgTableRow>
<ArgTableRow arg="lossy-pool-packet-cap" typ="num" syscap="prestera-bc2">Shared packet capacity of the lossy pool.</ArgTableRow>
<ArgTableRow arg="lossy-pool-packet-use" typ="num" syscap="prestera-bc2">Shared packet usage of the lossy pool.</ArgTableRow>
<ArgTableRow arg="lossless-pool-packet-cap" typ="num" syscap="!prestera-ac3">Shared packet capacity of the lossless pool.</ArgTableRow>
<ArgTableRow arg="lossless-pool-packet-use" typ="num" syscap="!prestera-ac3">Shared packet usage of the lossless pool.</ArgTableRow>
<ArgTableRow arg="lossy-pool-byte-cap" typ="num" syscap="!prestera-ac3">Lossy pool byte capacity.</ArgTableRow>
<ArgTableRow arg="lossy-pool-byte-use" typ="num" syscap="!prestera-ac3">Lossy pool byte usage.</ArgTableRow>
<ArgTableRow arg="lossless-pool-byte-cap" typ="num" syscap="!prestera-ac3">Lossless pool byte capacity.</ArgTableRow>
<ArgTableRow arg="lossless-pool-byte-use" typ="num" syscap="!prestera-ac3">Lossless pool byte usage.</ArgTableRow>
<ArgTableRow arg="wred-packet-cap" typ="num" syscap="prestera-bc2">The maximum packet count that a queue can use above the shared cap to trigger a random tail drop (`queueX-shared-packet-cap` in `/in/eth/sw/qos/port/print` usage) . For example, if `queue1-shared-packet-cap=3072` and `wred-packet-cap=512`, WRED triggers when `queue1-packet-use` exceeds 3072, reaching 100% drop rate at 3072+512=3584 packets.</ArgTableRow>
<ArgTableRow arg="wred-byte-cap" typ="num" syscap="prestera-bc2">The maximum byte count that a queue can use above the shared cap to trigger a random tail drop (`queueX-shared-byte-cap`). For example, if `queue1-shared-byte-cap=768KiB` and `wred-byte-cap=128KiB`, WRED triggers when `queue1-packet-use` exceeds 768KiB, reaching 100% drop rate at 768+128=896KiB.</ArgTableRow>
</ArgTable>
