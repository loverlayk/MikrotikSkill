# monitor-peers

> Continuously prints the client's view of its time sources, updating in place. Includes the local reference clock (127.127.1.0) when use-local-clock is enabled. See the NTP guide.

-----------

## system/ntp/monitor-peers 
**Type:** Command

Continuously prints the client's view of its time sources, updating in place. Includes the local reference clock (127.127.1.0) when `use-local-clock` is enabled. See the [NTP](../../../system-information-and-utilities/ntp) guide.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="string">Association type, for example `ucast-client` for a unicast server.</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)">Peer address from the server list, or 127.127.1.0 for the local reference clock.</ArgTableRow>
<ArgTableRow arg="refid" typ="string">Reference ID: the time source of the peer (typically the address of the peer's own upstream source). Empty while the peer is unsynchronized.</ArgTableRow>
<ArgTableRow arg="stratum" typ="num">Stratum announced by the peer. 16 means unsynchronized.</ArgTableRow>
<ArgTableRow arg="hpoll" typ="num">Current poll interval to this peer, as the power of 2 in seconds (6 = 64 s).</ArgTableRow>
<ArgTableRow arg="ppoll" typ="num">Poll interval the peer asks for, as the power of 2 in seconds.</ArgTableRow>
<ArgTableRow arg="root-delay" typ="num">Total round-trip delay from the peer to the root (stratum 1) time source.</ArgTableRow>
<ArgTableRow arg="root-disp" typ="num">Maximum error of the peer relative to the root time source.</ArgTableRow>
<ArgTableRow arg="offset" typ="num">Estimated clock offset of the peer relative to the local clock.</ArgTableRow>
<ArgTableRow arg="delay" typ="num">Round-trip delay to the peer.</ArgTableRow>
<ArgTableRow arg="disp" typ="num">Dispersion of the peer: the accumulated measurement error of its time.</ArgTableRow>
<ArgTableRow arg="jitter" typ="num">Variation of the offset between consecutive samples.</ArgTableRow>
</ArgTable>
