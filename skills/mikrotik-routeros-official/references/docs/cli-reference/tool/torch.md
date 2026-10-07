# torch

> Shows the traffic that passes one interface right now, grouped into flows by addresses, protocol, ports and DSCP, with the rate of each flow in both directions. Torch sees packets before the firewall, and turns IP...

-----------

## tool/torch 
**Type:** Command

Shows the traffic that passes one interface right now, grouped into flows by addresses, protocol, ports and DSCP, with the rate of each flow in both directions. Torch sees packets before the firewall, and turns IP fast path off while it runs. It runs until stopped with Ctrl-C or until `duration` ends. For examples and how to read the output, see [Torch](../../diagnostics-monitoring-and-troubleshooting/torch).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum">Interface to watch. The name can be given without `interface=`, for example `/tool/torch bridge`.</ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, src-address: ipPrefix
 }">Show only flows whose `src-address` is in this IPv4 prefix. `src-address` of a flow is the address on the far side of the interface, whose traffic the interface receives. Default: any.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, dst-address: ipPrefix
 }">Show only flows whose `dst-address`, the other end of the flow, is in this IPv4 prefix. Default: any.</ArgTableRow>
<ArgTableRow arg="src-address6" typ="super { !
, src-address6: ip6Prefix
 }">IPv6 prefix for `src-address`, the far side of the interface. Default: any.</ArgTableRow>
<ArgTableRow arg="dst-address6" typ="super { !
, dst-address6: ip6Prefix
 }">IPv6 prefix for `dst-address`, the other end of the flow. Default: any.</ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="enum (any) { any:3 }">Show only flows of this MAC protocol, for example `ip`. Default: any.</ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="enum (any) { any:256 }">Show only flows of this IP protocol, for example `tcp`. Default: any.</ArgTableRow>
<ArgTableRow arg="port" typ="enum (any) { any:0 }">Show only flows with this port as `src-port` or `dst-port`, one port or `any`. The filter applies to flows that have ports: flows without ports, such as ICMP, still appear. Default: any.</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="alt { number: num [ .. 4095]
, enum: enum (any) { any:0xffff }
 }">Show only frames with this VLAN ID, `0..4095`, or `any`. Tagged frames on the parent interface get a `VLAN-ID` column also without this filter. Default: any.</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">Show only flows with this DSCP value, `0..63`, for example `46` for Expedited Forwarding. Default: any.</ArgTableRow>
<ArgTableRow arg="cpu" typ="num">With `any`, adds a `CPU` column: one row for each CPU that handled packets of a flow.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="cpu" typ="num">CPU that handled the packets of the row. Shown with `cpu=any`.</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num">VLAN ID of the flow. Shown for tagged frames on the parent interface; on the VLAN interface itself the frames are untagged and the column does not appear.</ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="enum ()">MAC protocol of the flow, for example `ip`.</ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="enum ()">IP protocol of the flow, for example `tcp`, `udp` or `icmp`.</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">DSCP value of the flow.</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }">Address on the far side of the interface: the side whose traffic the interface receives, also when the router started the conversation.</ArgTableRow>
<ArgTableRow arg="src-port" typ="enum ()">Port on the `src-address` side, for TCP and UDP flows, shown with its service name.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }">The other end of the flow.</ArgTableRow>
<ArgTableRow arg="dst-port" typ="enum ()">Port on the `dst-address` side, for TCP and UDP flows, shown with its service name, such as `2000 (btserv)`.</ArgTableRow>
<ArgTableRow arg="tx" typ="num">Rate of the traffic the interface sends towards `src-address`, in bits per second.</ArgTableRow>
<ArgTableRow arg="rx" typ="num">Rate of the traffic the interface receives from `src-address`, in bits per second.</ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num">Packets per second the interface sends towards `src-address`.</ArgTableRow>
<ArgTableRow arg="rx-packets" typ="num">Packets per second the interface receives from `src-address`.</ArgTableRow>
</ArgTable>
