# route

> RouterOS directory reference for /ipv6/route.

-----------

## ipv6/route 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="A" typ="active">active</ArgTableRow>
<ArgTableRow arg="c" typ="connect">connect</ArgTableRow>
<ArgTableRow arg="s" typ="static">static</ArgTableRow>
<ArgTableRow arg="r" typ="rip">rip</ArgTableRow>
<ArgTableRow arg="b" typ="bgp">bgp</ArgTableRow>
<ArgTableRow arg="o" typ="ospf">ospf</ArgTableRow>
<ArgTableRow arg="i" typ="is-is">is-is</ArgTableRow>
<ArgTableRow arg="d" typ="dhcp">dhcp</ArgTableRow>
<ArgTableRow arg="v" typ="vpn">vpn</ArgTableRow>
<ArgTableRow arg="m" typ="modem">modem</ArgTableRow>
<ArgTableRow arg="g" typ="slaac">slaac</ArgTableRow>
<ArgTableRow arg="y" typ="bgp-mpls-vpn">bgp-mpls-vpn</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">hw-offloaded</ArgTableRow>
<ArgTableRow arg="+" typ="ecmp">ecmp</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="dst-address" typ="address (flags=6/)"></ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum"></ArgTableRow>
<ArgTableRow arg="pref-src" typ="address (flags=6)" unset="1"></ArgTableRow>
<ArgTableRow arg="gateway" typ="address (flags=6ivSL)" unset="1"></ArgTableRow>
<ArgTableRow arg="blackhole" typ="switch"></ArgTableRow>
<ArgTableRow arg="check-gateway" typ="enum (none | arp | ping | bfd)" unset="1"></ArgTableRow>
<ArgTableRow arg="distance" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="scope" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="target-scope" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="vrf-interface" typ="iface_enum" unset="1"></ArgTableRow>
<ArgTableRow arg="suppress-hw-offload" typ="bool" syscap="crs_prestera"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="immediate-gw" typ="multi { gw: address (flags=6i)
 }"></ArgTableRow>
</ArgTable>
