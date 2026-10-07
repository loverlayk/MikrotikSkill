# start

> Starts the sniffer with the settings in /tool/sniffer. The filter arguments are the filter- settings without the filter- prefix (interface, ip-address, port, ip-protocol), and vlan-id for filter-vlan. With filter...

-----------

## tool/sniffer/start 
**Type:** Command

Starts the sniffer with the settings in [`/tool/sniffer`](.). The filter arguments are the `filter-*` settings without the `filter-` prefix (`interface`, `ip-address`, `port`, `ip-protocol`), and `vlan-id` for `filter-vlan`. With filter arguments, the run uses only the filters given; the saved filters do not apply and do not change. While the sniffer runs, the router turns off IPv4 fast path, and with it FastTrack. The captured packets stay in memory after [`stop`](stop), for [`packet`](packet), [`protocol`](protocol), [`host`](host) and [`connection`](connection), for 10 minutes or until the next start. See [Packet sniffer](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="object { interface: iface_enum
 }">Interfaces to sniff in this run.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">Up to 16 MAC addresses, or MAC addresses with a mask; a frame matches when its source or destination MAC address matches. Prefix an entry with `!` to negate it.</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">Up to 16 source MAC addresses, or MAC addresses with a mask. Prefix an entry with `!` to negate it.</ArgTableRow>
<ArgTableRow arg="dst-mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">Up to 16 destination MAC addresses, or MAC addresses with a mask. Prefix an entry with `!` to negate it.</ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="object { mac-protocol-element: super { !
, protocol: alt { mac-protocol: enum ()
, protocol-number: num [ .. 65535]
 }
 }
 }">Up to 16 MAC (L2) protocols, by name or number (0..65535), for example `ip`, `arp`, `ipv6` or `802.2`. Prefix an entry with `!` to negate it.</ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="object { ip-protocol-element: super { !
, ip-protocol: enum ()
 }
 }">Up to 16 IP or IPv6 protocols, by name or number, for example `icmp`, `tcp` or `udp`. Prefix an entry with `!` to negate it.</ArgTableRow>
<ArgTableRow arg="ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">Up to 16 IPv4 addresses or prefixes; a packet matches when its source or destination address matches. Prefix an entry with `!` to negate it.</ArgTableRow>
<ArgTableRow arg="src-ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">Up to 16 source IPv4 addresses or prefixes. Prefix an entry with `!` to negate it.</ArgTableRow>
<ArgTableRow arg="dst-ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">Up to 16 destination IPv4 addresses or prefixes. Prefix an entry with `!` to negate it.</ArgTableRow>
<ArgTableRow arg="ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">Up to 16 IPv6 prefixes; a packet matches when its source or destination address matches. Prefix an entry with `!` to negate it.</ArgTableRow>
<ArgTableRow arg="src-ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">Up to 16 source IPv6 prefixes. Prefix an entry with `!` to negate it.</ArgTableRow>
<ArgTableRow arg="dst-ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">Up to 16 destination IPv6 prefixes. Prefix an entry with `!` to negate it.</ArgTableRow>
<ArgTableRow arg="port" typ="object { port-element: super { !
, port: enum ()
 }
 }">Up to 16 ports, by number or by name such as `ssh` or `telnet`; a packet matches when its source or destination port matches. Prefix an entry with `!` to negate it.</ArgTableRow>
<ArgTableRow arg="src-port" typ="object { port-element: super { !
, port: enum ()
 }
 }">Up to 16 source ports, by number or name. Prefix an entry with `!` to negate it.</ArgTableRow>
<ArgTableRow arg="dst-port" typ="object { port-element: super { !
, port: enum ()
 }
 }">Up to 16 destination ports, by number or name. Prefix an entry with `!` to negate it.</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="object { vlan-element: super { !
, vlan: num [ .. 4095]
 }
 }">Up to 16 VLAN IDs (0..4095). Prefix an entry with `!` to negate it.</ArgTableRow>
<ArgTableRow arg="direction" typ="enum (any | tx | rx) { any:0, tx:1, rx:2 }">
Directions to capture in this run.
- `any` (default) - Received and sent packets.
- `rx` - Received packets. They are captured before the firewall, so packets that a firewall rule drops are still captured.
- `tx` - Sent packets, captured after the firewall.
</ArgTableRow>
<ArgTableRow arg="operator-between-entries" typ="enum (or | and) { or:0, and:1 }">
How the entries of one filter are combined in this run.
- `or` (default) - A packet matches a filter when it matches any of the filter's entries.
- `and` - A packet matches a filter only when it matches all of the filter's entries.
</ArgTableRow>
<ArgTableRow arg="cpu" typ="object { cpu-element: super { !
, cpu: num
 }
 }">CPU cores that processed the packet. Prefix an entry with `!` to negate it.</ArgTableRow>
<ArgTableRow arg="size" typ="object { size-element: super { !
, size-range: range [0 .. 65535]
 }
 }">Packet sizes or size ranges in bytes (0..65535), for example `1000-1500`. Prefix an entry with `!` to negate it.</ArgTableRow>
</ArgTable>
