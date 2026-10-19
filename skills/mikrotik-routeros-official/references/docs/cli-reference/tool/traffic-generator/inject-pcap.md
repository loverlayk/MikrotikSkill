# inject-pcap

> RouterOS command reference for /tool/traffic-generator/inject-pcap.

-----------

## tool/traffic-generator/inject-pcap 
**Type:** Command
Replays packets from a PCAP or PCAPNG file on an interface. PCAPNG is the format the [sniffer tool](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer) saves captures in.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum">Interface the captured packets are replayed on.</ArgTableRow>
<ArgTableRow arg="pcap-file" typ="file">Name of a PCAP or PCAPNG file stored on the router.</ArgTableRow>
<ArgTableRow arg="speed-multiplier" typ="num">Replay speed multiplier relative to the capture rate (1 replays in real time).</ArgTableRow>
<ArgTableRow arg="loop" typ="bool">Whether the capture is replayed in a loop.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="iteration" typ="num">Current replay iteration number (in loop mode).</ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num">Packets replayed so far.</ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num">Bytes replayed so far.</ArgTableRow>
</ArgTable>
