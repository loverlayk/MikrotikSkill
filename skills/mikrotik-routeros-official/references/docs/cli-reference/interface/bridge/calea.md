# calea

> RouterOS directory reference for /interface/bridge/calea.

-----------

## interface/bridge/calea 
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="all" typ="switch"></ArgTableRow>
<ArgTableRow arg="static" typ="switch"></ArgTableRow>
<ArgTableRow arg="dynamic" typ="switch"></ArgTableRow>
<ArgTableRow arg="chain" typ="enum (input | forward | output) { input:1, forward:2, output:3 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (sniff | sniff-pc) { sniff:12, sniff-pc:13 }"></ArgTableRow>
<ArgTableRow arg="sniff-target" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="sniff-target-port" typ="num"></ArgTableRow>
<ArgTableRow arg="sniff-id" typ="num"></ArgTableRow>
<ArgTableRow arg="in-interface" typ="super { !
, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="in-bridge" typ="super { !
, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="out-interface" typ="super { !
, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="out-bridge" typ="super { !
, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="in-interface-list" typ="super { !
, interface-list: enum
 }"></ArgTableRow>
<ArgTableRow arg="out-interface-list" typ="super { !
, interface-list: enum
 }"></ArgTableRow>
<ArgTableRow arg="in-bridge-list" typ="super { !
, interface-list: enum
 }"></ArgTableRow>
<ArgTableRow arg="out-bridge-list" typ="super { !
, interface-list: enum
 }"></ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="super { !
, address: macAddr
, [mask] /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="dst-mac-address" typ="super { !
, address: macAddr
, [mask] /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="super { !
, protocol: alt { protocol-name: enum (length) { length:1 }
, protocol-number: num [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, address: ipAddr
, [netmask] /num [ .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, address: ipAddr
, [netmask] /num [ .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="src-address6" typ="super { !
, address: ip6Prefix
 }"></ArgTableRow>
<ArgTableRow arg="dst-address6" typ="super { !
, address: ip6Prefix
 }"></ArgTableRow>
<ArgTableRow arg="src-port" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="super { !
, protocol: enum ()
 }"></ArgTableRow>
<ArgTableRow arg="packet-mark" typ="super { !
, mark: enum
 }"></ArgTableRow>
<ArgTableRow arg="packet-type" typ="super { !
, type: enum (host | broadcast | multicast | other-host) { host:0, broadcast:1, multicast:2, other-host:3 }
 }"></ArgTableRow>
<ArgTableRow arg="limit" typ="super { count: num
, [time] [ /time]
, [burst] ,num
 }"></ArgTableRow>
<ArgTableRow arg="802.3-sap" typ="super { !
, sap: num [ .. 0xff]
 }"></ArgTableRow>
<ArgTableRow arg="802.3-type" typ="super { !
, type: num [ .. 0xffff]
 }"></ArgTableRow>
<ArgTableRow arg="arp-opcode" typ="super { !
, opcode: alt { common-opcode: enum (request | reply | request-reverse | reply-reverse | drarp-request | drarp-reply | drarp-error | inarp-request | inarp-reply | arp-nak) { request:1, reply:2, request-reverse:3, reply-reverse:4, drarp-request:5, drarp-reply:6, drarp-error:7, inarp-request:8, inarp-reply:9, arp-nak:10 }
, opcode-number: num [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="arp-hardware-type" typ="super { !
, type: num [ .. 0xffff]
 }"></ArgTableRow>
<ArgTableRow arg="arp-packet-type" typ="super { !
, type: num [ .. 0xffff]
 }"></ArgTableRow>
<ArgTableRow arg="arp-src-address" typ="super { !
, address: ipAddr
, [netmask] /num [ .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="arp-dst-address" typ="super { !
, address: ipAddr
, [netmask] /num [ .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="arp-src-mac-address" typ="super { !
, address: macAddr
, [mask] /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="arp-dst-mac-address" typ="super { !
, address: macAddr
, [mask] /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="arp-gratuitous" typ="super { gratuitous: bool
 }"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="super { !
, type: num [ .. 4095]
 }"></ArgTableRow>
<ArgTableRow arg="vlan-priority" typ="super { !
, type: num [ .. 7]
 }"></ArgTableRow>
<ArgTableRow arg="vlan-encap" typ="super { !
, protocol: alt { protocol-name: enum (length) { length:1 }
, protocol-number: num [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="stp-type" typ="super { !
, type: alt { type-name: enum (config | tcn) { config:0, tcn:0x80 }
, type-number: num [ .. 255]
 }
 }"></ArgTableRow>
<ArgTableRow arg="stp-flags" typ="super { !
, type: alt { type-name: enum (topology-change | topology-change-ack) { topology-change:1, topology-change-ack:0x80 }
, type-number: num [ .. 255]
 }
 }"></ArgTableRow>
<ArgTableRow arg="stp-root-priority" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-root-address" typ="super { !
, address: macAddr
, [mask] /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="stp-root-cost" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-sender-priority" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-sender-address" typ="super { !
, address: macAddr
, [mask] /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="stp-port" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-msg-age" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-max-age" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-hello-time" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-forward-delay" typ="super { !
, min: num [0 .. 65535]
, [max] -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="ingress-priority" typ="super { !
, priority: num [0 .. 63]
 }"></ArgTableRow>
<ArgTableRow arg="tls-host" typ="super { !
, tls-host: string
 }"></ArgTableRow>
<ArgTableRow arg="log" typ="bool"></ArgTableRow>
<ArgTableRow arg="log-prefix" typ="string"></ArgTableRow>
</ArgTable>
