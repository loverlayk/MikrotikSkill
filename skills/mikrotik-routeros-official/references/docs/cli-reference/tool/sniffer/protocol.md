# protocol

> Packets and bytes of the last capture per MAC protocol, IP protocol and port, with each row's share of all captured bytes. A packet counts in every row it belongs to: for a TCP packet, the ip row, the ip/tcp row and...

-----------

## tool/sniffer/protocol 
**Type:** Directory

Packets and bytes of the last capture per MAC protocol, IP protocol and port, with each row's share of all captured bytes. A packet counts in every row it belongs to: for a TCP packet, the `ip` row, the `ip`/`tcp` row and a row for each of its ports. See [Packet sniffer](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer).

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="protocol" typ="enum ()">MAC (L2) protocol, for example `ip`, `arp`, `ipv6` or `802.2`.</ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="enum (ip) { ip:0 }">IP protocol, for example `icmp`, `tcp` or `udp`. Empty on the row that counts a whole MAC protocol.</ArgTableRow>
<ArgTableRow arg="port" typ="enum ()">Port, with its service name where known, for example `80 (http)`. Empty on the rows that count a whole protocol.</ArgTableRow>
<ArgTableRow arg="packets" typ="num">Number of captured packets in this row.</ArgTableRow>
<ArgTableRow arg="bytes" typ="num">Number of captured bytes in this row.</ArgTableRow>
<ArgTableRow arg="share" typ="num">Share of this row's bytes in all captured bytes, in percent.</ArgTableRow>
</ArgTable>
