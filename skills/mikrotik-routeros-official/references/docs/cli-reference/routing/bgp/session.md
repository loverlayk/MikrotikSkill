# session

> List of BGP already established, not yet connected or disconnected sessions.

-----------

## routing/bgp/session 
**Conditions:** !smips
**Type:** Directory

List of BGP already established, not yet connected or disconnected sessions.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="E" typ="established">established</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="remote.address" typ="address (flags=46iv+:)"></ArgTableRow>
<ArgTableRow arg="remote.port" typ="num"></ArgTableRow>
<ArgTableRow arg="remote.as" typ="super { as: as
, [sub-as] [ /as]
 }"></ArgTableRow>
<ArgTableRow arg="remote.id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="remote.refused-cap-opt" typ="bool"></ArgTableRow>
<ArgTableRow arg="remote.capabilities" typ="ubit (mp, rr, orf, enhe, em, sec, ml, role, gr, as4, dyn, ms, ap, err, llgr, fqdn)">Remote peer's advertised/supported capabilities.</ArgTableRow>
<ArgTableRow arg="remote.afi" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)">Remote peer's advertised/supported address families.</ArgTableRow>
<ArgTableRow arg="remote.hold-time" typ="alt { special: enum (infinity) { infinity:0 }
, number: time [3 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="remote.messages" typ="num">Number of BGP messages received from remote peer.</ArgTableRow>
<ArgTableRow arg="remote.bytes" typ="num">Total number of bytes received from remote peer.</ArgTableRow>
<ArgTableRow arg="remote.gr-restart" typ="bool"></ArgTableRow>
<ArgTableRow arg="remote.gr-time" typ="num"></ArgTableRow>
<ArgTableRow arg="remote.gr-afi" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6)"></ArgTableRow>
<ArgTableRow arg="remote.gr-afi-fwp" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6)"></ArgTableRow>
<ArgTableRow arg="remote.eor" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)">List of address families that received end-of-rib from remote peer.</ArgTableRow>
<ArgTableRow arg="remote.role" typ="enum (provider | route-server | route-server-client | customer | peer)">Role received from the remote peer. See [Route Leak Prevention](../../../../user-guides/routing-and-networking-protocols/unicast/bgp/route-leak-prevention.md).</ArgTableRow>
<ArgTableRow arg="local.role" typ="enum (ibgp | ibgp-rr | ebgp | ebgp-provider | ebgp-rs | ebgp-rs-client | ebgp-customer | ebgp-peer)">Locally configured role. See [Route Leak Prevention](../../../../user-guides/routing-and-networking-protocols/unicast/bgp/route-leak-prevention.md).</ArgTableRow>
<ArgTableRow arg="local.address" typ="address (flags=46iv:)"></ArgTableRow>
<ArgTableRow arg="local.port" typ="num"></ArgTableRow>
<ArgTableRow arg="local.as" typ="super { as: as
, [sub-as] [ /as]
 }"></ArgTableRow>
<ArgTableRow arg="local.id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="local.cluster-id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="local.capabilities" typ="ubit (mp, rr, enhe, role, gr, as4, ap)"></ArgTableRow>
<ArgTableRow arg="local.afi" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)"></ArgTableRow>
<ArgTableRow arg="local.messages" typ="num"></ArgTableRow>
<ArgTableRow arg="local.bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="local.eor" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4)"></ArgTableRow>
<ArgTableRow arg="output.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf | input)"></ArgTableRow>
<ArgTableRow arg="output.procid" typ="num"></ArgTableRow>
<ArgTableRow arg="output.filter-select" typ="enum"></ArgTableRow>
<ArgTableRow arg="output.filter-chain" typ="enum"></ArgTableRow>
<ArgTableRow arg="output.network" typ="enum"></ArgTableRow>
<ArgTableRow arg="output.add-path" typ="ubit (ip, ipv6)"></ArgTableRow>
<ArgTableRow arg="output.remove-private-as" typ="bool"></ArgTableRow>
<ArgTableRow arg="output.default-originate" typ="enum (never | if-installed | always)"></ArgTableRow>
<ArgTableRow arg="output.default-prepend" typ="num"></ArgTableRow>
<ArgTableRow arg="output.no-client-to-client-reflection" typ="bool"></ArgTableRow>
<ArgTableRow arg="output.no-early-cut" typ="bool"></ArgTableRow>
<ArgTableRow arg="output.keep-sent-attributes" typ="bool"></ArgTableRow>
<ArgTableRow arg="output.last-notification" typ="string">Content of last sent notification message.</ArgTableRow>
<ArgTableRow arg="input.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf)"></ArgTableRow>
<ArgTableRow arg="input.procid" typ="num">Shows which routing process the session is tied to.</ArgTableRow>
<ArgTableRow arg="input.filter" typ="enum"></ArgTableRow>
<ArgTableRow arg="input.allow-as" typ="num"></ArgTableRow>
<ArgTableRow arg="input.as-override" typ="bool"></ArgTableRow>
<ArgTableRow arg="input.ignore-as-path-len" typ="bool"></ArgTableRow>
<ArgTableRow arg="input.limit-process-routes" typ="num"></ArgTableRow>
<ArgTableRow arg="input.add-path" typ="ubit (ip, ipv6)"></ArgTableRow>
<ArgTableRow arg="input.last-notification" typ="string">Content of last received notification message.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="ibgp" typ="switch">Indicates if the session is iBGP.</ArgTableRow>
<ArgTableRow arg="ebgp" typ="switch">Indicates if the session is eBGP.</ArgTableRow>
<ArgTableRow arg="limit-exceeded" typ="switch">Indicates if received prefix count exceeds configured prefix limit by `input.limit-process-routes-ipv4` and/or `input.limit-process-routes-ipv6`.</ArgTableRow>
<ArgTableRow arg="stopped" typ="switch">Indicates whether session is administratively stopped.</ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum"></ArgTableRow>
<ArgTableRow arg="nexthop-choice" typ="enum (default | force-self | propagate)"></ArgTableRow>
<ArgTableRow arg="cisco-vpls-nlri-len-fmt" typ="enum (auto-bits | auto-bytes | bits | bytes)"></ArgTableRow>
<ArgTableRow arg="multihop" typ="bool"></ArgTableRow>
<ArgTableRow arg="hold-time" typ="alt { special: enum (infinity) { infinity:0 }
, number: time [3 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="keepalive-time" typ="time"></ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time">Uptime of established session.</ArgTableRow>
<ArgTableRow arg="last-started" typ="date"></ArgTableRow>
<ArgTableRow arg="last-stopped" typ="date"></ArgTableRow>
<ArgTableRow arg="save-to" typ="string"></ArgTableRow>
<ArgTableRow arg="prefix-count" typ="num"></ArgTableRow>
<ArgTableRow arg="keepalive-timer" typ="time"></ArgTableRow>
<ArgTableRow arg="restart-timer" typ="time"></ArgTableRow>
</ArgTable>
