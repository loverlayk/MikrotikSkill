# packet

> The packets that the last run of start captured, kept in memory for 10 minutes after the sniffer stops, or until the next start. time counts seconds from the start of the capture, shown with microseconds. See Packet...

-----------

## tool/sniffer/packet 
**Type:** Directory

The packets that the last run of [`start`](start) captured, kept in memory for 10 minutes after the sniffer stops, or until the next start. `time` counts seconds from the start of the capture, shown with microseconds. See [Packet sniffer](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer).

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="time" typ="num">Time offset of the packet relative to the start of the capture, in seconds with microsecond precision.</ArgTableRow>
<ArgTableRow arg="num" typ="num">Packet sequence number, starting from 0 for the first captured packet.</ArgTableRow>
<ArgTableRow arg="direction" typ="enum (rx | tx) { rx:0, tx:1 }">Direction of the packet relative to the router, `rx` received, `tx` sent.</ArgTableRow>
<ArgTableRow arg="src-mac" typ="macAddr">Source MAC address of the frame, shown only for interfaces that have a MAC address, for example Ethernet, WiFi, EoIP, VXLAN or VLAN.</ArgTableRow>
<ArgTableRow arg="dst-mac" typ="macAddr">Destination MAC address of the frame, shown only for interfaces that have a MAC address, for example Ethernet, WiFi, EoIP, VXLAN or VLAN.</ArgTableRow>
<ArgTableRow arg="vlan" typ="object { vlan: composite { id: num
, prio: [ num]
 }
 }">VLAN tag of the frame, displayed as `id:priority`.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">Interface on which the packet was captured.</ArgTableRow>
<ArgTableRow arg="src-address" typ="composite { address: alt { ip: ipAddr
, ipv6: ip6Addr
 }
, port: enum ()
 }">Source IP address and source port of the packet, displayed as `address:port`.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="composite { address: alt { ip: ipAddr
, ipv6: ip6Addr
 }
, port: enum ()
 }">Destination IP address and destination port of the packet, displayed as `address:port`.</ArgTableRow>
<ArgTableRow arg="protocol" typ="enum ()">MAC (L2) protocol of the frame, for example `ip`, `arp` or `ipv6`.</ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="enum (ip) { ip:0 }">IP protocol of the packet, for example `icmp`, `tcp` or `udp`.</ArgTableRow>
<ArgTableRow arg="size" typ="num">Total frame size in bytes, including the L2 header.</ArgTableRow>
<ArgTableRow arg="cpu" typ="num">CPU core on which the packet was processed.</ArgTableRow>
<ArgTableRow arg="ip-packet-size" typ="num">Size of the IP packet in bytes.</ArgTableRow>
<ArgTableRow arg="ip-header-size" typ="num">Size of the IP header in bytes.</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">DSCP (Differentiated Services Code Point) field of the IP header.</ArgTableRow>
<ArgTableRow arg="ecn" typ="num">ECN (Explicit Congestion Notification) field of the IP header.</ArgTableRow>
<ArgTableRow arg="identification" typ="num">Identification field of the IP header.</ArgTableRow>
<ArgTableRow arg="fragment-offset" typ="num">Fragment offset field of the IP header.</ArgTableRow>
<ArgTableRow arg="ttl" typ="num">Time to live field of the IP header.</ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="multi { array-id, flag: enum (fin | syn | rst | psh | ack | urg | ece | cwr) { fin:0, syn:1, rst:2, psh:3, ack:4, urg:5, ece:6, cwr:7 }
 }">TCP flags of the packet: `fin`, `syn`, `rst`, `psh`, `ack`, `urg`, `ece` or `cwr`.</ArgTableRow>
<ArgTableRow arg="data" typ="string">Content of the captured packet in hexadecimal format.</ArgTableRow>
</ArgTable>
