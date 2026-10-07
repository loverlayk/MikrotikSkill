# mangle

> RouterOS directory reference for /ip/firewall/mangle.

-----------

## ip/firewall/mangle 
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="all" typ="switch"></ArgTableRow>
<ArgTableRow arg="static" typ="switch"></ArgTableRow>
<ArgTableRow arg="dynamic" typ="switch"></ArgTableRow>
<ArgTableRow arg="chain" typ="enum" mandatory="1">Specifies to which chain the rule will be added. If the input does not match the name of an already defined chain, a new chain will be created.</ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | jump | return | log | passthrough | add-src-to-address-list | add-dst-to-address-list | sniff-tzsp | sniff-pc | drop | mark-packet | mark-connection | change-mss | change-dscp | strip-ipv4-options | change-ttl | mark-routing | set-priority | clear-df | fasttrack-connection | route) { accept:0, jump:1, return:2, log:3, passthrough:4, add-src-to-address-list:5, add-dst-to-address-list:6, sniff-tzsp:7, sniff-pc:8, drop:10, mark-packet:30, mark-connection:31, change-mss:32, change-dscp:33, strip-ipv4-options:34, change-ttl:35, mark-routing:36, set-priority:37, clear-df:39, fasttrack-connection:40, route:41 }">
Action to take if a packet is matched by the rule:
- `accept` - accept the packet. A packet is not passed to the next firewall rule.
- `add-dst-to-address-list` - add the destination address to the address list specified by the `address-list` parameter.
- `add-src-to-address-list` - add the source address to the address list specified by the `address-list` parameter.
- `jump` - jump to the user-defined chain specified by the value of the `jump-target` parameter.
- `log` - add a message to the system log containing the following data: in-interface, out-interface, src-mac, protocol, src-ip:port-&gt;dst-ip:port, and length of the packet. After a packet is matched it is passed to the next rule in the list, similar to `passthrough`.
- `passthrough` - if a packet is matched by the rule, increase the counter and go to the next rule (useful for statistics).
- `return` - passes control back to the chain from where the jump took place.
- `sniff-tzsp` - send a packet to a remote TZSP compatible system (such as Wireshark). Set remote target with `sniff-target` and `sniff-target-port` parameters (Wireshark recommends port 37008). After a packet is matched it is passed to the next rule in the list, similar to `passthrough`.
- `sniff-pc` - send a packet to a remote RouterOS CALEA server. After a packet is matched it is passed to the next rule in the list, similar to `passthrough`.
- `drop` - silently drop the packet.
- `mark-packet` - mark the packet with the specified `new-packet-mark`.
- `mark-connection` - mark the connection with the specified `new-connection-mark`.
- `change-mss` - change the Maximum Segment Size field value of the packet to a value specified by the `new-mss` parameter.
- `change-dscp` - change the Differentiated Services Code Point (DSCP) field value specified by the `new-dscp` parameter.
- `change-ttl` - change the Time to Live field value of the packet to a value specified by the `new-ttl` parameter.
- `mark-routing` - place a mark specified by the `new-routing-mark` parameter on a packet. This kind of mark is used for policy routing purposes only. Do not apply any other routing marks besides `main` for packets processed by FastTrack, since FastTrack can only work in the main routing table.
- `set-priority` - set the priority of the packet.
- `clear-df` - clear the Don't Fragment flag.
- `fasttrack-connection` - mark the connection for FastTrack. After a packet is matched it is passed to the next rule in the list, similar to `passthrough`.
- `route` - forces packets to a gateway IP specified by 'route-dst' parameter, by ignoring normal routing decisions (prerouting chain only).
- `strip-ipv4-options` - strip IPv4 option fields from IP header. The action does not actually remove IPv4 options but rather replaces all option octets with NOP. Further matcher with `ipv4-options=any` will still match the packet.
</ArgTableRow>
<ArgTableRow arg="jump-target" typ="enum ()">Name of the target chain to jump to. Applicable only if `action=jump`.</ArgTableRow>
<ArgTableRow arg="new-packet-mark" typ="enum ()">Sets the new packet mark value.</ArgTableRow>
<ArgTableRow arg="new-connection-mark" typ="enum ()">Sets the new connection mark value.</ArgTableRow>
<ArgTableRow arg="new-routing-mark" typ="enum ()">Sets a new `routing-mark` value. In RouterOS v7 routing mark must be created beforehand as a new [Routing table](../../../../user-guides/routing-and-networking-protocols/policy-routing.md)</ArgTableRow>
<ArgTableRow arg="new-mss" typ="alt { mss-action: enum (clamp-to-pmtu) { clamp-to-pmtu:65535 }
, mss-value: num [40 .. 65534]
 }">Sets a new MSS for a packet. **Important:** Clamp-to-pmtu feature sets the DF bit in the IP header to dynamically discover the PMTU of a path. The host sends all datagrams on that path with the DF bit set until it receives ICMP Destination Unreachable messages with a code meaning "fragmentation needed and DF set". Upon receipt of such a message, the source host reduces its assumed PMTU for the path.</ArgTableRow>
<ArgTableRow arg="new-dscp" typ="enum (from-priority-to-high-3-bits | from-priority) { from-priority-to-high-3-bits:254, from-priority:255 }">Sets the new DSCP value.</ArgTableRow>
<ArgTableRow arg="new-priority" typ="alt { new-priority: enum (from-dscp | from-ingress | from-dscp-high-3-bits) { from-dscp:65536, from-ingress:65537, from-dscp-high-3-bits:65538 }
, new-priority: num [0 .. 63]
 }">Sets a new priority for a packet. This can be the VLAN, WMM, DSCP or MPLS EXP priority [Read more](../../../../bridging-and-switching/user-guides/wmm-and-vlan-priority.md). This property can also be used to set an internal priority.</ArgTableRow>
<ArgTableRow arg="new-ttl" typ="super { mode: enum (set | increment | decrement) { set:0, increment:1, decrement:2 }
, [value] :num [0 .. 255]
 }">Sets the new TTL value.</ArgTableRow>
<ArgTableRow arg="passthrough" typ="bool">Whether to let the packet pass through to the next rule.</ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="super { !,
, flags: multi { array-id, array-id, flag: super { !
, flag: enum (fin | syn | rst | psh | ack | urg | ece | cwr) { fin:0, syn:1, rst:2, psh:3, ack:4, urg:5, ece:6, cwr:7 }
 }
 }
 }">
Matches the specified TCP flags:
- `ack` - acknowledging data.
- `cwr` - congestion window reduced.
- `ece` - ECN-echo flag (explicit congestion notification).
- `fin` - close connection.
- `psh` - push function.
- `rst` - reset connection.
- `syn` - new connection.
- `urg` - urgent data.
</ArgTableRow>
<ArgTableRow arg="p2p" typ="super { !
, p2p: enum (fasttrack | gnutella | direct-connect | edonkey | bit-torrent | blubster | soulseek | winmx | warez | all-p2p) { fasttrack:0x01, gnutella:0x02, direct-connect:0x03, edonkey:0x04, bit-torrent:0x05, blubster:0x06, soulseek:0x07, winmx:0x08, warez:0x09, all-p2p:0xFF }
 }">Matches some unencrypted P2P protocols. Deprecated since mostly everything is encrypted and requires deep packet inspection to identify. IPv4 only.</ArgTableRow>
<ArgTableRow arg="connection-state" typ="super { !
, state: ubit (invalid, established, related, new, untracked)
 }">
Interprets the connection tracking analytics data for a particular packet:
 - `established` - a packet that belongs to an existing connection.
 - `invalid` - a packet that does not have a determined state in connection tracking (usually severe out-of-order packets, packets with wrong sequence/ack number, or in case of resource over usage on the router). An invalid packet will not participate in NAT (as only connection-state=new packets do), and will still contain the original source IP address when routed. You should drop all `connection-state=invalid` packets in the firewall filter forward and input chains.
 - `new` - the packet has started a new connection or is otherwise associated with a connection that has not seen packets in both directions.
 - `related` - a packet that is related to, but not part of an existing connection, such as ICMP errors or a packet that begins an FTP data connection.
 - `untracked` - a packet that was set to bypass connection tracking in firewall RAW tables.
</ArgTableRow>
<ArgTableRow arg="connection-nat-state" typ="super { !
, state: ubit (srcnat, dstnat)
 }">
Matches connections that are source-natted, destination-natted, or both. The `connection-state=related` connections' connection-nat-state is determined by the direction of the first packet, and if connection tracking needs to use dst-nat to deliver this connection to the same hosts as the main connection, it will be in connection-nat-state=dstnat even if there are no dst-nat rules at all.
`ein-snat` and `ein-dnat` are source and destination nated connections when endpoint-independent NAT is used.
</ArgTableRow>
<ArgTableRow arg="sniff-target" typ="ipAddr">IP address to send the sniffed packet to.</ArgTableRow>
<ArgTableRow arg="sniff-target-port" typ="num">Port to send the sniffed packet to.</ArgTableRow>
<ArgTableRow arg="sniff-id" typ="num">ID of the sniffing session.</ArgTableRow>
<ArgTableRow arg="route-dst" typ="ipAddr">Specifies the route destination for the `route` action.</ArgTableRow>
<ArgTableRow arg="tls-host" typ="super { !
, tls-host: string
 }">Matches HTTPS traffic based on TLS SNI hostname. Accepts GLOB syntax for wildcard matching. The matcher will not be able to match the hostname if the TLS handshake frame is fragmented into multiple TCP segments.</ArgTableRow>
<ArgTableRow arg="connection-limit" typ="super { !
, limit: num
, [netmask] ,num
 }">Matches connections per address or address block after a given value is reached. You should use this together with `connection-state=new` and/or with `tcp-flags=syn` because the matcher is very resource-intensive.</ArgTableRow>
<ArgTableRow arg="layer7-protocol" typ="super { !
, protocol: enum
 }">Layer7 filter name defined in the layer7 protocol menu.</ArgTableRow>
<ArgTableRow arg="realm" typ="super { !
, realm: num
 }">Matches the routing realm. IPv4 only.</ArgTableRow>
<ArgTableRow arg="protocol" typ="super { !
, protocol: enum ()
 }">Matches the particular IP protocol specified by protocol name or number.</ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, range: ipRange
 }">Matches packets whose source is equal to the specified IP or falls into the specified IP range.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, range: ipRange
 }">Matches packets whose destination is equal to the specified IP or falls into the specified IP range.</ArgTableRow>
<ArgTableRow arg="fragment" typ="super { fragment: bool
 }">Matches fragmented packets. The first (starting) fragment does not count. If connection tracking is enabled there will be no fragments as the system automatically assembles every packet. IPv4 only.</ArgTableRow>
<ArgTableRow arg="psd" typ="super { weight-threshold: num
, [delay-threshold] ,time
, [low-port-weight] ,num
, [high-port-weight] ,num
 }">
Attempts to detect TCP and UDP scans. Parameters are in the following format: `WeightThreshold, DelayThreshold, LowPortWeight, HighPortWeight`.
- `WeightThreshold` - total weight of the latest TCP/UDP packets with different destination ports coming from the same host to be treated as port scan sequence.
- `DelayThreshold` - delay for the packets with different destination ports coming from the same host to be treated as possible port scan subsequence.
- `LowPortWeight` - the weight of the packets with privileged destination port (&lt;1024).
- `HighPortWeight` - the weight of the packets with a non-privileged destination port. IPv4 only.
</ArgTableRow>
<ArgTableRow arg="ipv4-options" typ="super { options: enum (strict-source-routing | loose-source-routing | no-source-routing | record-route | no-record-route | timestamp | no-timestamp | router-alert | no-router-alert | any | none) { strict-source-routing:0x1, loose-source-routing:0x2, no-source-routing:0x4, record-route:0x8, no-record-route:0x10, timestamp:0x20, no-timestamp:0x40, router-alert:0x80, no-router-alert:0x100, any:0x200, none:0x400 }
 }">
Matches IPv4 header options.
- `any` - matches packets with at least one of the IPv4 options.
- `loose-source-routing` - matches packets with a loose source routing option.
- `no-record-route` - matches packets with no record route option.
- `no-router-alert` - matches packets with no router alert option.
- `no-source-routing` - matches packets with no source routing option.
- `no-timestamp` - matches packets with no timestamp option.
- `record-route` - matches packets with record route option.
- `router-alert` - matches packets with router alert option.
- `strict-source-routing` - matches packets with a strict source routing option.
- `timestamp` - matches packets with a timestamp. IPv4 only.
</ArgTableRow>
<ArgTableRow arg="src-address-type" typ="super { !
, type: ubit (unicast, local, broadcast, multicast, blackhole)
 }">
Matches the source address type:
- `unicast` - an IP address used for point-to-point transmission.
- `local` - the address is assigned to one of the router's interfaces.
- `broadcast` - a packet is sent to all devices in the subnet.
- `multicast` - a packet is forwarded to a defined group of devices.
</ArgTableRow>
<ArgTableRow arg="dst-address-type" typ="super { !
, type: ubit (unicast, local, broadcast, multicast, blackhole)
 }">
Matches the destination address type:
- `unicast` - an IP address used for point-to-point transmission.
- `local` - the destination address is assigned to one of the router's interfaces.
- `broadcast` - a packet is sent to all devices in a subnet.
- `multicast` - a packet is forwarded to a defined group of devices.
</ArgTableRow>
<ArgTableRow arg="src-address-list" typ="super { !
, address-list: enum
 }">Matches the source address of a packet against a user-defined address list. Supports only one list.</ArgTableRow>
<ArgTableRow arg="dst-address-list" typ="super { !
, address-list: enum
 }">Matches the destination address of a packet against a user-defined address list. Supports only one list.</ArgTableRow>
<ArgTableRow arg="hotspot" typ="multi { array-id, array-id, flag: super { !
, flag: enum (from-client | auth | local-dst | to-client | http) { from-client:0, auth:1, local-dst:2, to-client:3, http:4 }
 }
 }">
Matches packets received from HotSpot clients against various HotSpot matchers.
- `auth` - matches authenticated HotSpot client packets.
- `from-client` - matches packets coming from the HotSpot client.
- `http` - matches HTTP requests sent to the HotSpot server.
- `local-dst` - matches packets destined to the HotSpot server.
- `to-client` - matches packets sent to the HotSpot client. IPv4 only.
</ArgTableRow>
<ArgTableRow arg="address-list" typ="enum ()">Name of the address list to be used. Applicable if the action is `add-dst-to-address-list` or `add-src-to-address-list`.</ArgTableRow>
<ArgTableRow arg="address-list-timeout" typ="alt { address-list-timeout: enum (none-dynamic | none-static) { none-dynamic:0, none-static:0xffffffff }
, address-list-timeout: time [ .. 21474836]
 }">
How long the address stays in `address-list` after the `add-src-to-address-list` or `add-dst-to-address-list` action adds it. With a time, the rule adds a dynamic entry (`D`) that the router removes when the time ends; each new match of the rule resets the time to its full value. The maximum is `35w3d13h13m56s`. An address that is already a static entry in the list stays static.
- `none-dynamic` (`0s`) - Add a dynamic entry without a timeout. It is not saved in the configuration and a reboot clears it.
- `none-static` - Add a static entry. It is saved in the configuration and in exports, and stays after a reboot until you remove it.
</ArgTableRow>
<ArgTableRow arg="ttl" typ="super { mode: enum (equal | not-equal | less-than | greater-than) { equal:0, not-equal:1, less-than:2, greater-than:3 }
, [value] :num [0 .. 255]
 }">Matches the packet TTL value. IPv4 only.</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="super { !
, mark: enum
 }">Matches packets marked by the mangle facility with a particular connection mark. If `no-mark` is set, the rule will match any unmarked connection.</ArgTableRow>
<ArgTableRow arg="connection-type" typ="super { !
, type: enum (ftp | pptp | h323 | sip | irc | quake3 | tftp) { ftp:0, pptp:1, h323:2, sip:3, irc:4, quake3:5, tftp:6 }
 }">Matches packets from related connections based on information from their connection tracking helpers. A relevant connection helper must be enabled under `/ip/firewall/service-port`.</ArgTableRow>
<ArgTableRow arg="connection-bytes" typ="super { from: num
, [to] -num
 }">Matches packets only if a given amount of bytes has been transferred through the particular connection. 0 means infinity, for example `connection-bytes=2000000-0` means that the rule matches if more than 2MB has been transferred through the relevant connection.</ArgTableRow>
<ArgTableRow arg="connection-rate" typ="super { !
, from: num
, [to] -num
 }">Allows capturing traffic based on the present speed of the connection.</ArgTableRow>
<ArgTableRow arg="routing-mark" typ="super { !
, mark: enum ()
 }">Matches packets marked by the mangle facility with a particular routing mark.</ArgTableRow>
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
</ArgTable>
