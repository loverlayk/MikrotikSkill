# flood-ping

> Sends a series of ICMP echo requests to one host and shows only the totals. Not available on SMIPS devices. Needs the traffic-gen device-mode feature; without it the command fails with failure: not allowed by...

-----------

## tool/flood-ping 
**Conditions:** !smips
**Type:** Command

Sends a series of ICMP echo requests to one host and shows only the totals. Not available on SMIPS devices. Needs the `traffic-gen` device-mode feature; without it the command fails with `failure: not allowed by device-mode`. For examples, see [Flood Ping](../../diagnostics-monitoring-and-troubleshooting/flood-ping).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">IPv4 or IPv6 address of the host to ping.</ArgTableRow>
<ArgTableRow arg="count" typ="num">Number of requests to send, `0..1000`.</ArgTableRow>
<ArgTableRow arg="size" typ="num">Size of each request, `10..1500`.</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">How long to wait for each reply, `00:00:00.010..00:00:05` (10 ms to 5 s).</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="sent" typ="num">Number of requests sent.</ArgTableRow>
<ArgTableRow arg="received" typ="num">Number of replies received. The difference from `sent` is the packet loss.</ArgTableRow>
<ArgTableRow arg="min-rtt" typ="time">Shortest round-trip time of the run.</ArgTableRow>
<ArgTableRow arg="avg-rtt" typ="time">Average round-trip time of the run.</ArgTableRow>
<ArgTableRow arg="max-rtt" typ="time">Longest round-trip time of the run.</ArgTableRow>
</ArgTable>
