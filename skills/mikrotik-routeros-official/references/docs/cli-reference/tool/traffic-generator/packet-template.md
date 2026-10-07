# packet-template

> RouterOS directory reference for /tool/traffic-generator/packet-template.

-----------

## tool/traffic-generator/packet-template 
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="header-stack" typ="multi { header: enum (mac | vlan | ip | udp | raw | ipv6 | tcp) { mac:1, vlan:2, ip:3, udp:4, raw:5, ipv6:6, tcp:7 }
 }"></ArgTableRow>
<ArgTableRow arg="port" typ="enum"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="mac-src" typ="multi { array-id, array-id, mac-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }"></ArgTableRow>
<ArgTableRow arg="mac-dst" typ="multi { array-id, array-id, mac-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }"></ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="multi { protocol: alt { protocol-name: enum ()
, protocol-number: num [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="vlan-priority" typ="multi { priority: num [ .. 7]
 }"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="multi { id: num [ .. 4095]
 }"></ArgTableRow>
<ArgTableRow arg="vlan-protocol" typ="multi { protocol: alt { protocol-name: enum ()
, protocol-number: num [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="ip-dscp" typ="multi { dscp: num [ .. 255]
 }"></ArgTableRow>
<ArgTableRow arg="ip-id" typ="multi { id: num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="ip-frag-off" typ="multi { frag-off: num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="ip-ttl" typ="multi { ttl: num [ .. 255]
 }"></ArgTableRow>
<ArgTableRow arg="ip-src" typ="multi { array-id, array-id, ip-range: ipRange
 }"></ArgTableRow>
<ArgTableRow arg="ip-dst" typ="multi { array-id, array-id, ip-range: ipRange
 }"></ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="multi { protocol-name: enum ()
 }"></ArgTableRow>
<ArgTableRow arg="ip-gateway" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="udp-src-port" typ="multi { array-id, array-id, port-range: range [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="udp-dst-port" typ="multi { array-id, array-id, port-range: range [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="udp-checksum" typ="multi { array-id, checksum: num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="raw-header" typ="multi { raw-header: string
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-src" typ="multi { array-id, array-id, ipv6-mask: ip6Prefix
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-dst" typ="multi { array-id, array-id, ipv6-mask: ip6Prefix
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-next-header" typ="multi { protocol: enum ()
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-gateway" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="ipv6-traffic-class" typ="multi { traffic-class: num [ .. 255]
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-flow-label" typ="multi { flow-label: num [ .. 0xfffff]
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-hop-limit" typ="multi { hop-limit: num [ .. 255]
 }"></ArgTableRow>
<ArgTableRow arg="tcp-src-port" typ="multi { array-id, array-id, port-range: range [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="tcp-dst-port" typ="multi { array-id, array-id, port-range: range [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="tcp-syn" typ="multi { array-id, array-id, syn-range: range
 }"></ArgTableRow>
<ArgTableRow arg="tcp-ack" typ="multi { array-id, array-id, ack-range: range
 }"></ArgTableRow>
<ArgTableRow arg="tcp-data-offset" typ="multi { data-offset: num [ .. 15]
 }"></ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="multi { flags: ubit (fin, syn, rst, psh, ack, urg, ece, cwr, ns, res0, res1, res2)
 }"></ArgTableRow>
<ArgTableRow arg="tcp-window-size" typ="multi { window-size: num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="tcp-urgent-pointer" typ="multi { urgent-pointer: num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="data" typ="enum (uninitialized | random | specific-byte | incrementing) { uninitialized:0, random:1, specific-byte:2, incrementing:3 }"></ArgTableRow>
<ArgTableRow arg="data-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="random-byte-offsets-and-masks" typ="multi { array-id, array-id, offset-and-mask: composite { offset: num [ .. 256]
, mask: num [ .. 255]
 }
 }"></ArgTableRow>
<ArgTableRow arg="random-ranges" typ="object { random-range: super { offset: num [ .. 256]
, [width] :enum (8 | 16 | 32) { 8:8, 16:16, 32:32 }
, [range] :range
 }
 }"></ArgTableRow>
<ArgTableRow arg="special-footer" typ="bool"></ArgTableRow>
<ArgTableRow arg="compute-checksum-from-offset" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="assumed-port" typ="enum (none) { none:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="assumed-interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="assumed-mac-src" typ="multi { mac: macAddr
 }"></ArgTableRow>
<ArgTableRow arg="assumed-mac-dst" typ="multi { mac: macAddr
 }"></ArgTableRow>
<ArgTableRow arg="assumed-mac-protocol" typ="multi { protocol: alt { protocol-name: enum ()
, protocol-number: num
 }
 }"></ArgTableRow>
<ArgTableRow arg="assumed-vlan-priority" typ="multi { priority: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-vlan-id" typ="multi { priority: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-vlan-protocol" typ="multi { protocol: alt { protocol-name: enum ()
, protocol-number: num
 }
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ip-dscp" typ="multi { dscp: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ip-id" typ="multi { id: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ip-frag-off" typ="multi { frag-off: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ip-ttl" typ="multi { ttl: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ip-src" typ="multi { assumed-ip-src: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ip-dst" typ="multi { assumed-ip-dst: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ip-protocol" typ="multi { ip-protocol: enum ()
 }"></ArgTableRow>
<ArgTableRow arg="assumed-udp-src-port" typ="multi { port: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-udp-dst-port" typ="multi { port: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-udp-checksum" typ="multi { checksum: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-raw-header" typ="multi { assumed-raw-header: string
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ipv6-src" typ="multi { ip: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ipv6-dst" typ="multi { ip: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ipv6-next-header" typ="multi { ip-protocol: enum ()
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ipv6-traffic-class" typ="multi { traffic-class: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ipv6-flow-label" typ="multi { flow-label: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-ipv6-hop-limit" typ="multi { hop-limit: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-tcp-src-port" typ="multi { port: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-tcp-dst-port" typ="multi { port: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-tcp-syn" typ="multi { syn: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-tcp-ack" typ="multi { ack: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-tcp-data-offset" typ="multi { data-offset: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-tcp-flags" typ="multi { flags: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-tcp-window-size" typ="multi { window-size: num
 }"></ArgTableRow>
<ArgTableRow arg="assumed-tcp-urgent-pointer" typ="multi { urgent-pointer: num
 }"></ArgTableRow>
</ArgTable>
