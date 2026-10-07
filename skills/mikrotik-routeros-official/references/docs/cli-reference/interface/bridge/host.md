# host

> RouterOS directory reference for /interface/bridge/host.

-----------

## interface/bridge/host 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="L" typ="local">local</ArgTableRow>
<ArgTableRow arg="E" typ="external">external</ArgTableRow>
<ArgTableRow arg="A" typ="aged">aged</ArgTableRow>
<ArgTableRow arg="a" typ="aged-peer">aged-peer</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vid" typ="num"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="on-interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="remote-ip" typ="alt { ipv4: ipAddr
, ipv6: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="dhcpv4-ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="dhcpv4-server-id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="dhcpv4-status" typ="enum (bound | requesting | searching | renewing | rebinding | expired | relay-agent)"></ArgTableRow>
<ArgTableRow arg="dhcpv4-expires-after" typ="time"></ArgTableRow>
</ArgTable>
