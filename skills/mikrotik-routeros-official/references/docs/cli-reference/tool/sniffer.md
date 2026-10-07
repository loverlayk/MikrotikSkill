# sniffer

> Settings of the packet sniffer: which packets it captures (the filter- settings), where it keeps them (memory and a file) and whether it streams them to a TZSP receiver. start and quick without filter arguments use...

-----------

## tool/sniffer 
**Type:** Settings Directory

Settings of the packet sniffer: which packets it captures (the `filter-*` settings), where it keeps them (memory and a file) and whether it streams them to a TZSP receiver. [`start`](start) and [`quick`](quick) without filter arguments use the saved filters. With filter arguments, they use only the filters given, for that run; the saved filters do not apply and do not change. See [Packet sniffer](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="only-headers" typ="bool">Store and save only the packet headers, not the payload. The packet list still shows the original packet size. Default: no.</ArgTableRow>
<ArgTableRow arg="memory-limit" typ="num">Memory for the captured packets, in KiB (10..4294967295). What does not fit is handled as `memory-scroll` says. Default: 100KiB.</ArgTableRow>
<ArgTableRow arg="memory-scroll" typ="bool">What happens when `memory-limit` is reached: `yes` replaces the oldest packets with new ones, so the memory holds the latest packets; `no` keeps the first packets and stores no more. Default: yes.</ArgTableRow>
<ArgTableRow arg="file-name" typ="file">File that the captured packets are written to while the sniffer runs, in pcapng format. Each start overwrites the file. A path on another disk, such as `usb1/capture.pcap`, writes the file there. Empty (default) keeps the packets only in memory; write them to a file later with [`save`](save).</ArgTableRow>
<ArgTableRow arg="file-limit" typ="num">Size limit of `file-name`, in KiB (10..4294967295). When the file reaches the limit, the sniffer stops writing to it but keeps running. Default: 1000KiB.</ArgTableRow>
<ArgTableRow arg="streaming-enabled" typ="bool">Send every captured packet to `streaming-server` as TZSP (version 1, Ethernet encapsulation, the whole frame) over UDP, for example to Wireshark. Default: no.</ArgTableRow>
<ArgTableRow arg="streaming-server" typ="composite { ip: ipAddr
, port: [ enum ()]
 }">Receiver of the TZSP stream: an address, or `address:port`. Without a port, 37008 is used. Default: 0.0.0.0:37008.</ArgTableRow>
<ArgTableRow arg="max-packet-size" typ="num">Maximum packet size, in bytes (2048..65536). Default: 2048.</ArgTableRow>
<ArgTableRow arg="filter-stream" typ="bool">With `yes`, the sniffer does not capture the packets it streams to `streaming-server`, and it does not capture ICMP packets to and from the `streaming-server` address either, also while streaming is off. Set `yes` when the interface towards the stream receiver is sniffed: with `no`, the stream packets are captured and streamed again, in a loop. Default: no.</ArgTableRow>
<ArgTableRow arg="filter-interface" typ="object { interface: iface_enum
 }">Interfaces to sniff. Empty (default) sniffs all interfaces; a packet to or from the router through a bridge then shows once on the bridge and once on the bridge port.</ArgTableRow>
<ArgTableRow arg="filter-mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">Up to 16 MAC addresses, or MAC addresses with a mask; a frame matches when its source or destination MAC address matches. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-src-mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">Up to 16 source MAC addresses, or MAC addresses with a mask. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-dst-mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">Up to 16 destination MAC addresses, or MAC addresses with a mask. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-mac-protocol" typ="object { mac-protocol-element: super { !
, protocol: alt { mac-protocol: enum ()
, protocol-number: num [ .. 65535]
 }
 }
 }">Up to 16 MAC (L2) protocols, by EtherType number (0..65535) or name: `802.2` (0x0004), `arp` (0x0806), `capsman` (0x88BB), `dot1x` (0x888E), `homeplug-av` (0x88E1), `ip` (0x0800), `ipv6` (0x86DD), `ipx` (0x8137), `lacp` (0x8809), `lldp` (0x88CC), `loop-protect` (0x9003), `macsec` (0x88E5), `mpls-multicast` (0x8848), `mpls-unicast` (0x8847), `mvrp` (0x88F5), `packing-compr`, `packing-simple`, `pppoe` (0x8864), `pppoe-discovery` (0x8863), `rarp` (0x8035), `romon` (0x88BF), `service-vlan` (0x88A8), `vlan` (0x8100). A VLAN-tagged frame matches the protocol inside the tag, not `vlan`; select VLANs with `filter-vlan`. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">Up to 16 IPv4 addresses or prefixes; a packet matches when its source or destination address matches. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-src-ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">Up to 16 source IPv4 addresses or prefixes. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-dst-ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">Up to 16 destination IPv4 addresses or prefixes. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">Up to 16 IPv6 prefixes; a packet matches when its source or destination address matches. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-src-ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">Up to 16 source IPv6 prefixes. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-dst-ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">Up to 16 destination IPv6 prefixes. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-ip-protocol" typ="object { ip-protocol-element: super { !
, ip-protocol: enum ()
 }
 }">Up to 16 IP or IPv6 protocols, by number or name: `dccp`, `ddp`, `egp`, `encap`, `etherip`, `ggp`, `gre`, `hmp`, `icmp`, `icmpv6`, `idpr-cmtp`, `igmp`, `ipencap`, `ipip`, `ipsec-ah`, `ipsec-esp`, `ipv6-encap`, `ipv6-frag`, `ipv6-nonxt`, `ipv6-opts`, `ipv6-route`, `iso-tp4`, `l2tp`, `ospf`, `pim`, `pup`, `rdp`, `rspf`, `rsvp`, `sctp`, `st`, `tcp`, `udp`, `udp-lite`, `vmtp`, `vrrp`, `xns-idp`, `xtp`. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-port" typ="object { port-element: super { !
, port: enum ()
 }
 }">Up to 16 ports, by number or by name such as `ssh`, `dns`, `bootps` (67) or `bootpc` (68); a packet matches when its source or destination port matches. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-src-port" typ="object { port-element: super { !
, port: enum ()
 }
 }">Up to 16 source ports, by number or name. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-dst-port" typ="object { port-element: super { !
, port: enum ()
 }
 }">Up to 16 destination ports, by number or name. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-vlan" typ="object { cpu-element: super { !
, vlan: num [ .. 4095]
 }
 }">Up to 16 VLAN IDs (0..4095). It matches tagged frames on the interface that carries them, such as the trunk port; the IP and MAC filters match the packet inside the tag. On the VLAN interface itself, packets are untagged and do not match. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-cpu" typ="object { cpu-element: super { !
, cpu: num
 }
 }">CPU cores that processed the packet. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-size" typ="object { size-element: super { !
, size-range: range [0 .. 65535]
 }
 }">Packet sizes or size ranges in bytes (0..65535), for example `1000-1500`. Prefix an entry with `!` to negate it. Empty (default) means no filter.</ArgTableRow>
<ArgTableRow arg="filter-direction" typ="enum (any | tx | rx) { any:0, tx:1, rx:2 }">
Directions to capture.
- `any` (default) - Received and sent packets.
- `rx` - Received packets. They are captured before the firewall, so packets that a firewall rule drops are still captured.
- `tx` - Sent packets, captured after the firewall.
</ArgTableRow>
<ArgTableRow arg="filter-operator-between-entries" typ="enum (or | and) { or:0, and:1 }">
How the entries of one filter are combined. Different filters always combine: a packet has to match every filter that is set.
- `or` (default) - A packet matches a filter when it matches any of the filter's entries.
- `and` - A packet matches a filter only when it matches all of the filter's entries, for example both addresses of `filter-ip-address=192.168.88.10/32,192.168.88.1/32`.
</ArgTableRow>
<ArgTableRow arg="quick-rows" typ="num">Number of packets that [`quick`](quick) shows when its `rows` argument is not given. Default: 20.</ArgTableRow>
<ArgTableRow arg="quick-show-frame" typ="bool">Whether [`quick`](quick) shows the frame content when its `show-frame` argument is not given. Default: no.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="running" typ="bool">`yes` while the sniffer is running.</ArgTableRow>
</ArgTable>
