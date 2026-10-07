# quick

> Shows the matching packets live, until you stop it with Q or for the time given in duration. The filter arguments are the filter- settings of /tool/sniffer without the filter- prefix, and vlan-id for filter-vlan....

-----------

## tool/sniffer/quick 
**Type:** Command

Shows the matching packets live, until you stop it with <kbd>Q</kbd> or for the time given in `duration`. The filter arguments are the `filter-*` settings of [`/tool/sniffer`](.) without the `filter-` prefix, and `vlan-id` for `filter-vlan`. Without filter arguments, the saved filters apply; with filter arguments, only the filters given apply, and the saved settings do not change. `quick` cannot run while the sniffer runs (`already running`). `proplist` selects the columns, for example `proplist=interface,time,dir,src-address,dst-address,protocol,size`. See [Packet sniffer](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="rows" typ="num">Maximum number of packets displayed in the output. Default: the `quick-rows` setting (20).</ArgTableRow>
<ArgTableRow arg="show-frame" typ="bool">Whether to show the raw frame content in the output. Default: the `quick-show-frame` setting (no).</ArgTableRow>
<ArgTableRow arg="interface" typ="object { interface: iface_enum
 }">Interface or list of interfaces to capture traffic on. A bridged packet shows once on the bridge and once on the bridge port when both are included.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">Filter: capture only frames with a matching MAC address or MAC address with mask.</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">Filter: capture only frames with a matching source MAC address or MAC address with mask.</ArgTableRow>
<ArgTableRow arg="dst-mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">Filter: capture only frames with a matching destination MAC address or MAC address with mask.</ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="object { mac-protocol-element: super { !
, protocol: alt { mac-protocol: enum ()
, protocol-number: num [ .. 65535]
 }
 }
 }">Filter: capture only frames with a matching MAC (L2) protocol.</ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="object { ip-protocol-element: super { !
, ip-protocol: enum ()
 }
 }">Filter: capture only packets with a matching IP protocol.</ArgTableRow>
<ArgTableRow arg="ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">Filter: capture only packets with a matching IP address or subnet.</ArgTableRow>
<ArgTableRow arg="src-ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">Filter: capture only packets with a matching source IP address or subnet.</ArgTableRow>
<ArgTableRow arg="dst-ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">Filter: capture only packets with a matching destination IP address or subnet.</ArgTableRow>
<ArgTableRow arg="ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">Filter: capture only packets with a matching IPv6 address or prefix.</ArgTableRow>
<ArgTableRow arg="src-ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">Filter: capture only packets with a matching source IPv6 address or prefix.</ArgTableRow>
<ArgTableRow arg="dst-ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">Filter: capture only packets with a matching destination IPv6 address or prefix.</ArgTableRow>
<ArgTableRow arg="port" typ="object { port-element: super { !
, port: enum ()
 }
 }">Filter: capture only packets with a matching source or destination port.</ArgTableRow>
<ArgTableRow arg="src-port" typ="object { port-element: super { !
, port: enum ()
 }
 }">Filter: capture only packets with a matching source port.</ArgTableRow>
<ArgTableRow arg="dst-port" typ="object { port-element: super { !
, port: enum ()
 }
 }">Filter: capture only packets with a matching destination port.</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="object { vlan-element: super { !
, vlan: num [ .. 4095]
 }
 }">Filter: capture only frames with a matching VLAN ID.</ArgTableRow>
<ArgTableRow arg="direction" typ="enum (any | tx | rx) { any:0, tx:1, rx:2 }">
Filter: directions to capture.
- `any` (default) - Received and sent packets.
- `rx` - Received packets. They are captured before the firewall, so packets that a firewall rule drops are still captured.
- `tx` - Sent packets, captured after the firewall.
</ArgTableRow>
<ArgTableRow arg="operator-between-entries" typ="enum (or | and) { or:0, and:1 }">
How the entries of one filter are combined.
- `or` (default) - A packet matches a filter when it matches any of the filter's entries.
- `and` - A packet matches a filter only when it matches all of the filter's entries.
</ArgTableRow>
<ArgTableRow arg="cpu" typ="object { cpu-element: super { !
, cpu: num
 }
 }">Filter: capture only packets processed by the given CPU core.</ArgTableRow>
<ArgTableRow arg="size" typ="object { size-element: super { !
, size-range: range [0 .. 65535]
 }
 }">Filter: capture only packets with a matching size or size range in bytes.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum">Interface on which the packet was captured.</ArgTableRow>
<ArgTableRow arg="time" typ="num">Time offset of the packet relative to the start of the capture, in seconds with microsecond precision.</ArgTableRow>
<ArgTableRow arg="num" typ="num">Packet sequence number, starting from 0 for the first captured packet.</ArgTableRow>
<ArgTableRow arg="dir" typ="enum (<- | ->) { <-:0, ->:1 }">Direction of the packet, `<-` received, `->` sent.</ArgTableRow>
<ArgTableRow arg="src-mac" typ="macAddr">Source MAC address of the frame, shown only for interfaces that have a MAC address, for example Ethernet, WiFi, EoIP, VXLAN or VLAN.</ArgTableRow>
<ArgTableRow arg="dst-mac" typ="macAddr">Destination MAC address of the frame, shown only for interfaces that have a MAC address, for example Ethernet, WiFi, EoIP, VXLAN or VLAN.</ArgTableRow>
<ArgTableRow arg="vlan" typ="composite { id: num [ .. 4095]
, priority: num [ .. 7]
 }">VLAN tag of the frame, displayed as `id:priority`.</ArgTableRow>
<ArgTableRow arg="src-address" typ="composite { address: alt { ip: ipAddr
, ipv6: ip6Addr
, descr: string
 }
, port: enum ()
 }">Source IP address and source port of the packet, displayed as `address:port`.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="composite { address: alt { ip: ipAddr
, ipv6: ip6Addr
 }
, port: enum ()
 }">Destination IP address and destination port of the packet, displayed as `address:port`.</ArgTableRow>
<ArgTableRow arg="protocol" typ="composite { mac-protocol: enum ()
, ip-protocol: enum (ip) { ip:0 }
 }">MAC (L2) protocol of the frame and its IP protocol, for example `ip:icmp`.</ArgTableRow>
<ArgTableRow arg="size" typ="num">Total frame size in bytes, including the L2 header.</ArgTableRow>
<ArgTableRow arg="cpu" typ="num">CPU core on which the packet was processed.</ArgTableRow>
<ArgTableRow arg="fp" typ="bool">Whether the packet was processed in the fast path.</ArgTableRow>
<ArgTableRow arg="raw" typ="string">Raw frame content in hexadecimal format, shown when the `show-frame` parameter is enabled.</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">DSCP (Differentiated Services Code Point) field of the IP header.</ArgTableRow>
<ArgTableRow arg="ecn" typ="num">ECN (Explicit Congestion Notification) field of the IP header.</ArgTableRow>
<ArgTableRow arg="fragment-offset" typ="num">Fragment offset field of the IP header.</ArgTableRow>
<ArgTableRow arg="identification" typ="num">Identification field of the IP header.</ArgTableRow>
<ArgTableRow arg="ip-header-size" typ="num">Size of the IP header in bytes.</ArgTableRow>
<ArgTableRow arg="ip-packet-size" typ="num">Size of the IP packet in bytes.</ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="super { tcp-flags: multi { array-id, flag: enum (fin | syn | rst | psh | ack | urg | ece | cwr) { fin:0, syn:1, rst:2, psh:3, ack:4, urg:5, ece:6, cwr:7 }
 }
 }">TCP flags of the packet: `fin`, `syn`, `rst`, `psh`, `ack`, `urg`, `ece` or `cwr`.</ArgTableRow>
<ArgTableRow arg="ttl" typ="num">Time to live field of the IP header.</ArgTableRow>
</ArgTable>
