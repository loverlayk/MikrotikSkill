# raw

> RouterOS directory reference for /ipv6/firewall/raw.

-----------

## ipv6/firewall/raw 
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="chain" typ="enum" mandatory="1">Specifies to which chain the rule will be added. If the input does not match the name of an already defined chain, a new chain will be created.</ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | jump | return | log | passthrough | add-src-to-address-list | add-dst-to-address-list | drop | notrack) { accept:0, jump:1, return:2, log:3, passthrough:4, add-src-to-address-list:5, add-dst-to-address-list:6, drop:10, notrack:42 }">Action to take if a packet is matched by the rule: `accept` - accept the packet. A packet is not passed to the next firewall rule.  `add-dst-to-address-list` - add the destination address to the address list specified by the `address-list` parameter.  `add-src-to-address-list` - add the source address to the address list specified by the `address-list` parameter.  `drop` - drop the packet.  `jump` - jump to the user-defined chain specified by the value of the `jump-target` parameter.  `log` - add a message to the system log containing the following data: in-interface, out-interface, src-mac, protocol, src-ip:port->dst-ip:port, and length of the packet. After a packet is matched it is passed to the next rule in the list, similar to `passthrough`.  `notrack` - skip connection tracking for the packet.  `passthrough` - if a packet is matched by the rule, increase the counter and go to the next rule (useful for statistics).  `return` - passes control back to the chain from where the jump took place.</ArgTableRow>
<ArgTableRow arg="jump-target" typ="enum ()">Name of the target chain to jump to. Applicable only if `action=jump`.</ArgTableRow>
<ArgTableRow arg="tls-host" typ="super { !
, tls-host: string
 }">Matches HTTPS traffic based on TLS SNI hostname. Accepts GLOB syntax for wildcard matching. The matcher will not be able to match the hostname if the TLS handshake frame is fragmented into multiple TCP segments.</ArgTableRow>
<ArgTableRow arg="in-interface" typ="super { !
, interface: iface_enum
 }">Interface the packet has entered the router.</ArgTableRow>
<ArgTableRow arg="out-interface" typ="super { !
, interface: iface_enum
 }">Interface the packet is leaving the router.</ArgTableRow>
<ArgTableRow arg="in-interface-list" typ="super { !
, interface-list: enum
 }">Set of interfaces defined in interface list. Works the same as `in-interface`.</ArgTableRow>
<ArgTableRow arg="out-interface-list" typ="super { !
, interface-list: enum
 }">Set of interfaces defined in interface list. Works the same as `out-interface`.</ArgTableRow>
<ArgTableRow arg="in-bridge-port" typ="super { !
, interface: iface_enum
 }">Actual interface the packet has entered the router if the incoming interface is a bridge. Works only if `use-ip-firewall` is enabled in bridge settings.</ArgTableRow>
<ArgTableRow arg="out-bridge-port" typ="super { !
, interface: iface_enum
 }">Actual interface the packet leaves the router if the outgoing interface is a bridge. Works only if `use-ip-firewall` is enabled in bridge settings.</ArgTableRow>
<ArgTableRow arg="in-bridge-port-list" typ="super { !
, interface-list: enum
 }">Set of interfaces defined in interface list. Works the same as `in-bridge-port`.</ArgTableRow>
<ArgTableRow arg="out-bridge-port-list" typ="super { !
, interface-list: enum
 }">Set of interfaces defined in interface list. Works the same as `out-bridge-port`.</ArgTableRow>
<ArgTableRow arg="packet-mark" typ="super { !
, mark: enum
 }">Matches packets marked by the mangle facility with a particular packet mark. If `no-mark` is set, the rule will match any unmarked packet.</ArgTableRow>
<ArgTableRow arg="src-port" typ="super { !
, port: multi { range: range [ .. 65535]
 }
 }">List of source ports and ranges of source ports. Applicable only if the protocol is TCP or UDP.</ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, port: multi { range: range [ .. 65535]
 }
 }">List of destination port numbers or port number ranges.</ArgTableRow>
<ArgTableRow arg="port" typ="super { !
, port: multi { range: range [ .. 65535]
 }
 }">Matches if any (source or destination) port matches the specified list of ports or port ranges. Applicable only if `protocol` is TCP or UDP.</ArgTableRow>
<ArgTableRow arg="icmp-options" typ="super { !
, type: num [0 .. 255]
, [code] [ :range [ .. 255]]
 }">Matches ICMP type:code fields.</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="super { !
, address: macAddr
 }">Matches the source MAC address of the packet.</ArgTableRow>
<ArgTableRow arg="content" typ="super { !
, content: string
 }">Matches packets that contain the specified text.</ArgTableRow>
<ArgTableRow arg="ingress-priority" typ="super { !
, ingress-priority: num [0 .. 63]
 }">Matches the priority of an ingress packet. Priority may be derived from VLAN, WMM, DSCP, or MPLS EXP bit.</ArgTableRow>
<ArgTableRow arg="priority" typ="super { !
, priority: num [0 .. 63]
 }">Matches the packet's priority after a new priority has been set. Priority may be derived from VLAN, WMM, DSCP, MPLS EXP bit, or from the priority set by using the set-priority action.</ArgTableRow>
<ArgTableRow arg="dscp" typ="super { !
, dscp: num [0 .. 63]
 }">Matches the DSCP IP header field.</ArgTableRow>
<ArgTableRow arg="tos" typ="super { !
, tos: num [0 .. 255]
, [mask] [ /num [0 .. 255]]
 }"></ArgTableRow>
<ArgTableRow arg="limit" typ="super { !
, count: num [1 .. 32000000000]
, [time] [ /time [1 .. ]]
, [burst] ,num [ .. 2000000000]
, [mode] [ :enum (packet | bit) { packet:0, bit:1 }]
 }">
Matches packets up to a limited rate (packet rate or bit rate). A rule with this matcher will match until this limit is reached. Parameters are written in the following format: `rate[/time],burst:mode`.
- `rate` - packet or bit count per time interval to match.
- `time` - specifies the time interval in which the packet or bit rate cannot be exceeded (optional, 1s will be used if not specified).
- `burst` - initial number of packets or bits to match: this number gets recharged every 10ms so burst should be at least 1/100 of a rate per second.
-  `mode` - packet or bit mode.
</ArgTableRow>
<ArgTableRow arg="dst-limit" typ="super { count: num
, [time] [ /time]
, [burst] ,num
, [mode] ,enum (dst-address | dst-address-and-port | src-address | src-and-dst-addresses | addresses-and-dst-port) { dst-address:1, dst-address-and-port:3, src-address:4, src-and-dst-addresses:5, addresses-and-dst-port:7 }
, [expire] [ /time]
 }">
Matches packets until a given rate is exceeded. Rate is defined as packets per time interval. As opposed to the `limit` matcher, every flow has its own limit. Flow is defined by a mode parameter. Parameters are written in the following format: `rate[/time],burst,mode[/expire]`.
- `rate` - packet count per time interval per-flow to match.
- `time` - specifies the time interval in which the packet count rate per flow cannot be exceeded (optional, 1s will be used if not specified).
- `burst` - initial number of packets per flow to match: this number gets recharged by one every time/rate, up to this number.
- `mode` - specifies what unique fields define flow (src-address, dst-address, src-and-dst-address, dst-address-and-port, addresses-and-dst-port).
- `expire` - specifies interval after which flow with no packets will be allowed to be deleted (optional).
</ArgTableRow>
<ArgTableRow arg="time" typ="super { !
, start: time [0 .. 86400]
, [end] -time [0 .. 86400]
, [day] ,ubit (sun, mon, tue, wed, thu, fri, sat)
 }">Creates a filter based on the packets' arrival time and date or, for locally generated packets, departure time and date. The matcher takes into account the time and timezone configured on the router.</ArgTableRow>
<ArgTableRow arg="random" typ="super { percent: num [1 .. 99]
 }">Matches packets randomly with a given probability.</ArgTableRow>
<ArgTableRow arg="nth" typ="super { !
, every: num [1 .. ]
, [packet] [ ,num [1 .. ]]
 }">Matches every nth packet: `nth=2,1` will match every first packet of 2, hence, 50% of all the traffic matched by the rule.</ArgTableRow>
<ArgTableRow arg="tcp-mss" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }">Matches the TCP MSS value of an IP packet.</ArgTableRow>
<ArgTableRow arg="per-connection-classifier" typ="super { !
, values-to-hash: enum (src-address | dst-address | both-addresses | src-port | src-address-and-port | dst-port | dst-address-and-port | both-ports | both-addresses-and-ports) { src-address:1, dst-address:2, both-addresses:3, src-port:4, src-address-and-port:5, dst-port:8, dst-address-and-port:10, both-ports:12, both-addresses-and-ports:15 }
, [denominator] :num [1 .. ]
, [remainder] /num [0 .. ]
 }">PCC matcher allows dividing traffic into equal streams with the ability to keep packets with a specific set of options in one particular stream.</ArgTableRow>
<ArgTableRow arg="packet-size" typ="super { !
, min: num [ .. 65535]
, [max] -num [ .. 65535]
 }">Matches packets of specified size or size range in bytes.</ArgTableRow>
<ArgTableRow arg="log" typ="bool">Add a message to the system log containing the following data: in-interface, out-interface, src-mac, protocol, src-ip:port-&gt;dst-ip:port, and length of the packet. Allows logging of packets even if the action is not `log`, useful for debugging the firewall.</ArgTableRow>
<ArgTableRow arg="log-prefix" typ="string">Adds the specified text at the beginning of every log message. Applicable if `action=log` or `log=yes` is configured.</ArgTableRow>
<ArgTableRow arg="ipsec-policy" typ="super { direction: enum (in | out) { in:0, out:1 }
, [policy] ,enum (none | ipsec) { none:0, ipsec:1 }
 }">
Matches the policy used by IPsec. Value is written in the following format: `direction, policy`.
- `in` - valid in the PREROUTING, INPUT, and FORWARD chains.
- `out` - valid in the POSTROUTING, OUTPUT, and FORWARD chains.
- `ipsec` - matches if the packet is subject to IPsec processing.
- `none` - matches packets that are not subject to IPsec processing.
</ArgTableRow>
<ArgTableRow arg="protocol" typ="super { !
, protocol: enum (icmpv6) { icmpv6:58 }
 }">Matches the particular IP protocol specified by protocol name or number.</ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, address: ip6Prefix
 }">Matches packets whose source is equal to the specified IP or falls into the specified IP range.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, address: ip6Prefix
 }">Matches packets whose destination is equal to the specified IP or falls into the specified IP range.</ArgTableRow>
<ArgTableRow arg="src-address-list" typ="super { !
, address-list: enum
 }">Matches the source address of a packet against a user-defined address list. Supports only one list.</ArgTableRow>
<ArgTableRow arg="dst-address-list" typ="super { !
, address-list: enum
 }">Matches the destination address of a packet against a user-defined address list. Supports only one list.</ArgTableRow>
<ArgTableRow arg="address-list" typ="enum ()">Name of the address list to be used. Applicable if the action is `add-dst-to-address-list` or `add-src-to-address-list`.</ArgTableRow>
<ArgTableRow arg="address-list-timeout" typ="alt { address-list-timeout: enum (none-dynamic | none-static) { none-dynamic:0, none-static:0xffffffff }
, address-list-timeout: time [ .. 21474836]
 }">
How long the address stays in `address-list` after the `add-src-to-address-list` or `add-dst-to-address-list` action adds it. With a time, the rule adds a dynamic entry (`D`) that the router removes when the time ends; each new match of the rule resets the time to its full value. The maximum is `35w3d13h13m56s`. An address that is already a static entry in the list stays static.
- `none-dynamic` (`0s`) - Add a dynamic entry without a timeout. It is not saved in the configuration and a reboot clears it.
- `none-static` - Add a static entry. It is saved in the configuration and in exports, and stays after a reboot until you remove it.
</ArgTableRow>
<ArgTableRow arg="src-address-type" typ="super { !
, type: ubit (unicast, local, anycast, multicast, unreachable)
 }">Matches the source address type: `unicast` - an IP address used for point-to-point transmission.  `local` - the address is assigned to one of the router's interfaces.  `anycast` - a packet sent to the nearest node in a group.  `multicast` - a packet is forwarded to a defined group of devices.  `unreachable` - the address is unreachable.</ArgTableRow>
<ArgTableRow arg="dst-address-type" typ="super { !
, type: ubit (unicast, local, anycast, multicast, unreachable)
 }">Matches the destination address type: `unicast` - an IP address used for point-to-point transmission.  `local` - the destination address is assigned to one of the router's interfaces.  `anycast` - a packet sent to the nearest node in a group.  `multicast` - a packet is forwarded to a defined group of devices.  `unreachable` - the address is unreachable.</ArgTableRow>
<ArgTableRow arg="headers" typ="super { !
, type: ubit (hop, dst, route, frag, ah, esp, none, proto)
, [mode] [ :enum (exact | contains) { exact:0, contains:1 }]
 }">Matches IPv6 next-header. Two types of header matching are possible controlled by the `mode` parameter: `contains` - soft matching, matches at least selected headers.  `exact` - matches the exact set of selected headers.</ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="super { !,
, flags: multi { array-id, array-id, flag: super { !
, flag: enum (fin | syn | rst | psh | ack | urg | ece | cwr) { fin:0, syn:1, rst:2, psh:3, ack:4, urg:5, ece:6, cwr:7 }
 }
 }
 }">Matches the specified TCP flags: `ack` - acknowledging data.  `cwr` - congestion window reduced.  `ece` - ECN-echo flag (explicit congestion notification).  `fin` - close connection.  `psh` - push function.  `rst` - reset connection.  `syn` - new connection.  `urg` - urgent data.</ArgTableRow>
<ArgTableRow arg="hop-limit" typ="super { mode: enum (equal | not-equal | less-than | greater-than) { equal:0, not-equal:1, less-than:2, greater-than:3 }
, [value] :num [0 .. 255]
 }">Matches the hop limit field in the IPv6 header.</ArgTableRow>
</ArgTable>
