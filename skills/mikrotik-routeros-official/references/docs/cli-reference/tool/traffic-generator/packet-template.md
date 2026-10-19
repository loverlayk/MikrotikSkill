# packet-template

> RouterOS directory reference for /tool/traffic-generator/packet-template.

-----------

## tool/traffic-generator/packet-template 
**Type:** Directory
Builds the packet content of a stream from header parameters: MAC, VLAN, IPv4/IPv6, UDP and TCP fields, plus the payload. Many header values are assumed when they can be derived; assumed values are read-only and are re-derived when the template is edited. See the [Traffic Generator](../../../diagnostics-monitoring-and-troubleshooting/traffic-generator) guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Descriptive name of the packet template.</ArgTableRow>
<ArgTableRow arg="header-stack" typ="multi { header: enum (mac | vlan | ip | udp | raw | ipv6 | tcp) { mac:1, vlan:2, ip:3, udp:4, raw:5, ipv6:6, tcp:7 }
 }">Sequence of headers in the generated packet: mac (Ethernet, 14 bytes), vlan (802.1Q tag, 4 bytes), ip (IPv4, 20 bytes), udp (UDP, 8 bytes), raw (arbitrary bytes as a hex string), ipv6 (IPv6, 40 bytes), tcp (TCP). Most header types may appear several times; there can be at most two IP headers and one UDP header per packet. Sequence limitations follow protocol rules (for example a VLAN header can follow only a mac header or another VLAN header).</ArgTableRow>
<ArgTableRow arg="port" typ="enum">Name of the port (from the port menu) the packets are sent out through. Mutually exclusive with interface; the port can also be set in the stream.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">Interface the packets are sent out through. Mutually exclusive with port; convenient for quick tests since a port entry is then created dynamically.</ArgTableRow>
<ArgTableRow arg="mac-src" typ="multi { array-id, array-id, mac-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }">Source MAC address(es), with optional masks, of the Ethernet header.</ArgTableRow>
<ArgTableRow arg="mac-dst" typ="multi { array-id, array-id, mac-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }">Destination MAC address(es), with optional masks, of the Ethernet header.</ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="multi { protocol: alt { protocol-name: enum ()
, protocol-number: num [ .. 65535]
 }
 }">EtherType of the Ethernet frame, by name or by protocol number (0-65535).</ArgTableRow>
<ArgTableRow arg="vlan-priority" typ="multi { priority: num [ .. 7]
 }">VLAN priority (0-7) of the 802.1Q tag.</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="multi { id: num [ .. 4095]
 }">VLAN ID (0-4095) of the 802.1Q tag.</ArgTableRow>
<ArgTableRow arg="vlan-protocol" typ="multi { protocol: alt { protocol-name: enum ()
, protocol-number: num [ .. 65535]
 }
 }">VLAN protocol, by name or by EtherType number (0-65535).</ArgTableRow>
<ArgTableRow arg="ip-dscp" typ="multi { dscp: num [ .. 255]
 }">DS Field value(s) (0-255) of the IPv4 header (DS Field holds the DSCP and ECN values).</ArgTableRow>
<ArgTableRow arg="ip-id" typ="multi { id: num [ .. 65535]
 }">IPv4 identification value(s) (0-65535).</ArgTableRow>
<ArgTableRow arg="ip-frag-off" typ="multi { frag-off: num [ .. 65535]
 }">IPv4 fragmentation offset(s) (0-65535).</ArgTableRow>
<ArgTableRow arg="ip-ttl" typ="multi { ttl: num [ .. 255]
 }">IPv4 time-to-live value(s) (0-255).</ArgTableRow>
<ArgTableRow arg="ip-src" typ="multi { array-id, array-id, ip-range: ipRange
 }">Source IPv4 address(es), with optional masks, of the IPv4 header.</ArgTableRow>
<ArgTableRow arg="ip-dst" typ="multi { array-id, array-id, ip-range: ipRange
 }">Destination IPv4 address(es), with optional masks, of the IPv4 header.</ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="multi { protocol-name: enum ()
 }">IPv4 protocol, for example tcp, udp or icmp.</ArgTableRow>
<ArgTableRow arg="ip-gateway" typ="ipAddr">Next-hop IPv4 address. When the sender and the receiver are the same device the next hop cannot be derived from ip-dst; when ip-gateway is set, the destination MAC is assumed from the resolved gateway.</ArgTableRow>
<ArgTableRow arg="udp-src-port" typ="multi { array-id, array-id, port-range: range [ .. 65535]
 }">UDP source port(s) or port range(s) (0-65535).</ArgTableRow>
<ArgTableRow arg="udp-dst-port" typ="multi { array-id, array-id, port-range: range [ .. 65535]
 }">UDP destination port(s) or port range(s) (0-65535).</ArgTableRow>
<ArgTableRow arg="udp-checksum" typ="multi { array-id, checksum: num [ .. 65535]
 }">UDP checksum value(s) (0-65535).</ArgTableRow>
<ArgTableRow arg="raw-header" typ="multi { raw-header: string
 }">Raw header bytes as a hexadecimal string.</ArgTableRow>
<ArgTableRow arg="ipv6-src" typ="multi { array-id, array-id, ipv6-mask: ip6Prefix
 }">Source IPv6 address(es), with optional masks, of the IPv6 header.</ArgTableRow>
<ArgTableRow arg="ipv6-dst" typ="multi { array-id, array-id, ipv6-mask: ip6Prefix
 }">Destination IPv6 address(es), with optional masks, of the IPv6 header.</ArgTableRow>
<ArgTableRow arg="ipv6-next-header" typ="multi { protocol: enum ()
 }">IPv6 Next Header protocol.</ArgTableRow>
<ArgTableRow arg="ipv6-gateway" typ="ip6Addr">Next-hop IPv6 address; the destination MAC is assumed from the resolved gateway.</ArgTableRow>
<ArgTableRow arg="ipv6-traffic-class" typ="multi { traffic-class: num [ .. 255]
 }">IPv6 traffic class value(s) (0-255).</ArgTableRow>
<ArgTableRow arg="ipv6-flow-label" typ="multi { flow-label: num [ .. 0xfffff]
 }">IPv6 flow label value(s) (0-1048575).</ArgTableRow>
<ArgTableRow arg="ipv6-hop-limit" typ="multi { hop-limit: num [ .. 255]
 }">IPv6 hop limit value(s) (0-255).</ArgTableRow>
<ArgTableRow arg="tcp-src-port" typ="multi { array-id, array-id, port-range: range [ .. 65535]
 }">TCP source port(s) or port range(s) (0-65535).</ArgTableRow>
<ArgTableRow arg="tcp-dst-port" typ="multi { array-id, array-id, port-range: range [ .. 65535]
 }">TCP destination port(s) or port range(s) (0-65535).</ArgTableRow>
<ArgTableRow arg="tcp-syn" typ="multi { array-id, array-id, syn-range: range
 }">TCP sequence number value(s), can be a range.</ArgTableRow>
<ArgTableRow arg="tcp-ack" typ="multi { array-id, array-id, ack-range: range
 }">TCP acknowledgement number value(s), can be a range.</ArgTableRow>
<ArgTableRow arg="tcp-data-offset" typ="multi { data-offset: num [ .. 15]
 }">TCP data offset (0-15, in 32-bit words).</ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="multi { flags: ubit (fin, syn, rst, psh, ack, urg, ece, cwr, ns, res0, res1, res2)
 }">TCP flag bits to set: fin, syn, rst, psh, ack, urg, ece, cwr, ns, res0, res1, res2.</ArgTableRow>
<ArgTableRow arg="tcp-window-size" typ="multi { window-size: num [ .. 65535]
 }">TCP window size value(s) (0-65535).</ArgTableRow>
<ArgTableRow arg="tcp-urgent-pointer" typ="multi { urgent-pointer: num [ .. 65535]
 }">TCP urgent pointer value(s) (0-65535).</ArgTableRow>
<ArgTableRow arg="data" typ="enum (uninitialized | random | specific-byte | incrementing) { uninitialized:0, random:1, specific-byte:2, incrementing:3 }">How the packet payload (after the header) is filled: uninitialized (not zeroed; fastest), specific-byte (with data-byte), incrementing (bytes 00 01 02 ...), random (random bytes; slowest).</ArgTableRow>
<ArgTableRow arg="data-byte" typ="num">Byte used to fill the payload when data=specific-byte.</ArgTableRow>
<ArgTableRow arg="random-byte-offsets-and-masks" typ="multi { array-id, array-id, offset-and-mask: composite { offset: num [ .. 256]
, mask: num [ .. 255]
 }
 }">Byte offsets in the packet, each with a bit mask, that are filled with random values.</ArgTableRow>
<ArgTableRow arg="random-ranges" typ="object { random-range: super { offset: num [ .. 256]
, [width] :enum (8 | 16 | 32) { 8:8, 16:16, 32:32 }
, [range] :range
 }
 }">Fields at given byte offsets that are filled with random values: `width` sets the field size (8, 16 or 32 bits) and `range` the range of the values.</ArgTableRow>
<ArgTableRow arg="special-footer" typ="bool">Whether a special footer is appended to the generated packets.</ArgTableRow>
<ArgTableRow arg="compute-checksum-from-offset" typ="num">Byte offset from which the 2-byte checksum is calculated; for example 14 skips the Ethernet header. no-checksum disables the checksum.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="assumed-port" typ="enum (none) { none:0xffffffff }">Assumed port the packets are sent out through, derived when only an interface is set.</ArgTableRow>
<ArgTableRow arg="assumed-interface" typ="iface_enum">Assumed interface the packets are sent out through.</ArgTableRow>
<ArgTableRow arg="assumed-mac-src" typ="multi { mac: macAddr
 }">Assumed source MAC address (the MAC address of the interface).</ArgTableRow>
<ArgTableRow arg="assumed-mac-dst" typ="multi { mac: macAddr
 }">Assumed destination MAC address, derived from ip-dst or from resolving ip-gateway.</ArgTableRow>
<ArgTableRow arg="assumed-mac-protocol" typ="multi { protocol: alt { protocol-name: enum ()
, protocol-number: num
 }
 }">Assumed EtherType, derived from the header stack (for example ip).</ArgTableRow>
<ArgTableRow arg="assumed-vlan-priority" typ="multi { priority: num
 }">Assumed VLAN priority of the 802.1Q tag.</ArgTableRow>
<ArgTableRow arg="assumed-vlan-id" typ="multi { priority: num
 }">Assumed VLAN ID of the 802.1Q tag.</ArgTableRow>
<ArgTableRow arg="assumed-vlan-protocol" typ="multi { protocol: alt { protocol-name: enum ()
, protocol-number: num
 }
 }">Assumed VLAN protocol of the 802.1Q tag.</ArgTableRow>
<ArgTableRow arg="assumed-ip-dscp" typ="multi { dscp: num
 }">Assumed IPv4 DS Field value.</ArgTableRow>
<ArgTableRow arg="assumed-ip-id" typ="multi { id: num
 }">Assumed IPv4 identification value.</ArgTableRow>
<ArgTableRow arg="assumed-ip-frag-off" typ="multi { frag-off: num
 }">Assumed IPv4 fragmentation offset.</ArgTableRow>
<ArgTableRow arg="assumed-ip-ttl" typ="multi { ttl: num
 }">Assumed IPv4 time-to-live value (for example 64).</ArgTableRow>
<ArgTableRow arg="assumed-ip-src" typ="multi { assumed-ip-src: ipAddr
 }">Assumed source IPv4 address (an address of the interface).</ArgTableRow>
<ArgTableRow arg="assumed-ip-dst" typ="multi { assumed-ip-dst: ipAddr
 }">Assumed destination IPv4 address.</ArgTableRow>
<ArgTableRow arg="assumed-ip-protocol" typ="multi { ip-protocol: enum ()
 }">Assumed IPv4 protocol, derived from the header stack (for example udp).</ArgTableRow>
<ArgTableRow arg="assumed-udp-src-port" typ="multi { port: num
 }">Assumed UDP source port.</ArgTableRow>
<ArgTableRow arg="assumed-udp-dst-port" typ="multi { port: num
 }">Assumed UDP destination port.</ArgTableRow>
<ArgTableRow arg="assumed-udp-checksum" typ="multi { checksum: num
 }">Assumed UDP checksum value.</ArgTableRow>
<ArgTableRow arg="assumed-raw-header" typ="multi { assumed-raw-header: string
 }">Assumed raw header bytes, as a hexadecimal string.</ArgTableRow>
<ArgTableRow arg="assumed-ipv6-src" typ="multi { ip: ip6Addr
 }">Assumed source IPv6 address (an address of the interface).</ArgTableRow>
<ArgTableRow arg="assumed-ipv6-dst" typ="multi { ip: ip6Addr
 }">Assumed destination IPv6 address.</ArgTableRow>
<ArgTableRow arg="assumed-ipv6-next-header" typ="multi { ip-protocol: enum ()
 }">Assumed IPv6 Next Header protocol.</ArgTableRow>
<ArgTableRow arg="assumed-ipv6-traffic-class" typ="multi { traffic-class: num
 }">Assumed IPv6 traffic class value.</ArgTableRow>
<ArgTableRow arg="assumed-ipv6-flow-label" typ="multi { flow-label: num
 }">Assumed IPv6 flow label value.</ArgTableRow>
<ArgTableRow arg="assumed-ipv6-hop-limit" typ="multi { hop-limit: num
 }">Assumed IPv6 hop limit value.</ArgTableRow>
<ArgTableRow arg="assumed-tcp-src-port" typ="multi { port: num
 }">Assumed TCP source port.</ArgTableRow>
<ArgTableRow arg="assumed-tcp-dst-port" typ="multi { port: num
 }">Assumed TCP destination port.</ArgTableRow>
<ArgTableRow arg="assumed-tcp-syn" typ="multi { syn: num
 }">Assumed TCP sequence number.</ArgTableRow>
<ArgTableRow arg="assumed-tcp-ack" typ="multi { ack: num
 }">Assumed TCP acknowledgement number.</ArgTableRow>
<ArgTableRow arg="assumed-tcp-data-offset" typ="multi { data-offset: num
 }">Assumed TCP data offset.</ArgTableRow>
<ArgTableRow arg="assumed-tcp-flags" typ="multi { flags: num
 }">Assumed TCP flags.</ArgTableRow>
<ArgTableRow arg="assumed-tcp-window-size" typ="multi { window-size: num
 }">Assumed TCP window size.</ArgTableRow>
<ArgTableRow arg="assumed-tcp-urgent-pointer" typ="multi { urgent-pointer: num
 }">Assumed TCP urgent pointer value.</ArgTableRow>
</ArgTable>
