# filter-wizard

> RouterOS command reference for /routing/filter/filter-wizard.

-----------

## routing/filter/filter-wizard 
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="chain" typ="enum"></ArgTableRow>
<ArgTableRow arg="dst" typ="super { !
, dst: alt { dst-list: enum
, dst: address (flags=46/+)
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="dst-len" typ="super { !
, dst-len: range [ .. 128]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="gateway" typ="super { !
, dst: alt { dst-list: enum
, dst: address (flags=46/+)
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="match-chain" typ="super { !
, chain: enum
 }" unset="1">returns true if provided chain did not reject</ArgTableRow>
<ArgTableRow arg="routing-table" typ="super { !
, table: enum
 }" unset="1">name of the routing table the route was imported from</ArgTableRow>
<ArgTableRow arg="afi" typ="super { !
, afi: ubit (ip, ipv6, l2vpn, vpnv4, vpnv6, l2vpn-cisco)
 }" unset="1">address family of the route</ArgTableRow>
<ArgTableRow arg="protocol" typ="super { !
, protocol: ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, slaac, bgp-mpls-vpn)
 }" unset="1">protocol type from which the route was imported</ArgTableRow>
<ArgTableRow arg="bgp-atomic-aggregate" typ="bool"></ArgTableRow>
<ArgTableRow arg="bgp-local-origin" typ="bool">returns true if prefix is locally originated, e.g BGP network</ArgTableRow>
<ArgTableRow arg="suppress-hw-offload" typ="bool" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="use-te-nexthop" typ="bool"></ArgTableRow>
<ArgTableRow arg="blackhole" typ="bool">matches blackhole routes</ArgTableRow>
<ArgTableRow arg="ospf-type" typ="super { !
, ospf-type: enum (intra | inter | ext1 | ext2 | nssa1 | nssa2) { intra:0, inter:1, ext1:2, ext2:3, nssa1:7, nssa2:8 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="rpki" typ="super { !
, rpki-type: enum (unknown | valid | invalid)
 }" unset="1">RPKI validation status of the prefix</ArgTableRow>
<ArgTableRow arg="bgp-origin" typ="super { !
, bgp-origin: ubit (igp, egp, incomplete)
 }" unset="1">matches BGP Origin attribute</ArgTableRow>
<ArgTableRow arg="bgp-as-path" typ="string">regexp that matches BGP AS-Path attribute, see documentation for more details</ArgTableRow>
<ArgTableRow arg="bgp-communities-match" typ="super { !
, match: enum (any | any-list | equal | equal-list | includes | includes-list | subset | subset-list)
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-communities" typ="object" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-communities-list-name" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-ext-communities-match" typ="super { !
, match: enum (any | any-list | equal | equal-list | includes | includes-list | subset | subset-list)
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-ext-communities" typ="object" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-ext-communities-list-name" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-large-communities-match" typ="super { !
, match: enum (any | any-list | equal | equal-list | includes | includes-list | subset | subset-list)
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-large-communities" typ="object" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-large-communities-list-name" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="distance" typ="super { !
, value: alt { num-list: enum
, range: range [ .. 255]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="scope" typ="super { !
, value: alt { num-list: enum
, range: range [ .. 255]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="scope-target" typ="super { !
, value: alt { num-list: enum
, range: range [ .. 255]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-weight" typ="super { !
, value: alt { num-list: enum
, range: range [ .. 65535]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-local-pref" typ="super { !
, value: alt { num-list: enum
, range: range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-med" typ="super { !
, value: alt { num-list: enum
, range: range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-out-med" typ="super { !
, value: alt { num-list: enum
, range: range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-as-path-length" typ="super { !
, value: alt { num-list: enum
, range: range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="ospf-metric" typ="super { !
, value: alt { num-list: enum
, range: range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="set-distance" typ="alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag)
, val: num [1 .. 255]
, value: composite { inc: [ enum ( | add | sub)]
, val: num [1 .. 255]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="set-scope" typ="alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag)
, val: num [1 .. 255]
, value: composite { inc: enum ( | add | sub)
, val: num [1 .. 255]
 }
 }"></ArgTableRow>
<ArgTableRow arg="set-scope-target" typ="alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag)
, val: num [1 .. 255]
, value: composite { inc: enum ( | add | sub)
, val: num [1 .. 255]
 }
 }"></ArgTableRow>
<ArgTableRow arg="set-bgp-weight" typ="alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag)
, val: num [ .. 65535]
, value: composite { inc: enum ( | add | sub)
, val: num [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="set-bgp-local-pref" typ="alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag)
, val: num
, value: composite { inc: enum ( | add | sub)
, val: num
 }
 }">set a value of the BGP Local-Pref attribute</ArgTableRow>
<ArgTableRow arg="set-bgp-med" typ="alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag)
, val: num
, value: composite { inc: enum ( | add | sub)
, val: num
 }
 }"></ArgTableRow>
<ArgTableRow arg="set-bgp-out-med" typ="alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag)
, val: num
, value: composite { inc: enum ( | add | sub)
, val: num
 }
 }"></ArgTableRow>
<ArgTableRow arg="set-suppress-hw-offload" typ="bool" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="set-use-te-nexthop" typ="bool"></ArgTableRow>
<ArgTableRow arg="set-blackhole" typ="bool"></ArgTableRow>
<ArgTableRow arg="set-gw-check" typ="enum (none | arp | ping | bfd)">set gateway check</ArgTableRow>
<ArgTableRow arg="set-gateway" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="set-comment" typ="string"></ArgTableRow>
<ArgTableRow arg="set-bgp-communities" typ="object">set a value of the BGP Communities attribute</ArgTableRow>
<ArgTableRow arg="set-bgp-communities-list" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="set-bgp-ext-communities" typ="object"></ArgTableRow>
<ArgTableRow arg="set-bgp-large-communities" typ="object"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | reject | jump | return)" unset="1"></ArgTableRow>
<ArgTableRow arg="jump-target-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="rpki-verify" typ="enum" unset="1">Enable RPKI verification in the current chain from specified RPKI group</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="result" typ="string"></ArgTableRow>
</ArgTable>
