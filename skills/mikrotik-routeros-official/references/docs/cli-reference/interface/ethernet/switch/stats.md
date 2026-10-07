# stats

> RouterOS settings reference for /interface/ethernet/switch/stats.

-----------

## interface/ethernet/switch/stats 
**Conditions:** !smips
**Syscap:** musicswitch
**Type:** Settings Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="driver-rx-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="driver-rx-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="driver-tx-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="driver-tx-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-too-short" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-64" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-65-127" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-128-255" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-256-511" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-512-1023" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-1024-1518" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-1519-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-too-long" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-broadcast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-pause" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-multicast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-fcs-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-align-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-fragment" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-overflow" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-control" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-unknown-op" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-length-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-code-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-carrier-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-jabber" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-drop" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-ip-header-checksum-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-tcp-checksum-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-udp-checksum-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-too-short" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-64" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-65-127" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-128-255" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-256-511" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-512-1023" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-1024-1518" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-1519-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-too-long" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-broadcast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-pause" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-multicast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-underrun" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-excessive-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-multiple-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-single-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-excessive-deferred" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-deferred" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-late-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-total-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-pause-honored" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-jabber" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-fcs-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-control" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-fragment" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-carrier-sense-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-64" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-65-127" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-128-255" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-256-511" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-512-1023" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-1024-1518" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-1519-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom0-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom0-drop-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom1-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom1-drop-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="policy-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="custom-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="current-learned" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="not-learned" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-unicast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-unicast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-error-events" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-1024-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-1024-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-1024-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-codewords" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-corrected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-uncorrected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-symbol-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="fc-fec-rx-block" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="fc-fec-block-corrected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="fc-fec-block-uncorrected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue0-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue0-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue1-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue1-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue2-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue2-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue3-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue3-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue4-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue4-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue5-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue5-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue6-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue6-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue7-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue7-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue0-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue0-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue1-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue1-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue2-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue2-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue3-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue3-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue4-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue4-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue5-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue5-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue6-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue6-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue7-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue7-byte" typ="multi { counter: num
 }"></ArgTableRow>
</ArgTable>
