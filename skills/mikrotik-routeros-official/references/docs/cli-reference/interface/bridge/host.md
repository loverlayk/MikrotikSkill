# host

> RouterOS directory reference for /interface/bridge/host.

-----------

## interface/bridge/host 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The static host entry is disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The host entry is invalid, for example a static host whose interface has been removed.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">The host was learned dynamically.</ArgTableRow>
<ArgTableRow arg="L" typ="local">The host entry belongs to the bridge itself, which displays all local interfaces.</ArgTableRow>
<ArgTableRow arg="E" typ="external">The host entry was learned from an external table, such as a switch chip forwarding database, a VXLAN tunnel or the Wireless registration table. Static host entries never display this flag, whether or not they have a `vid`.</ArgTableRow>
<ArgTableRow arg="A" typ="aged">The host entry has locally expired on an MLAG dual bond, but was not removed, because such hosts are only removed when aged on both peers.</ArgTableRow>
<ArgTableRow arg="a" typ="aged-peer">The host entry has expired on the MLAG peer's dual bond.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr" mandatory="1">The MAC address of the static host entry.</ArgTableRow>
<ArgTableRow arg="vid" typ="num">VLAN ID associated with the static host entry. The entry applies only to the given VLAN. It only has an effect when `vlan-filtering` is enabled on the bridge.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">The interface through which traffic for this MAC address is forwarded.</ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" mandatory="1">The bridge interface to which the host entry belongs.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="on-interface" typ="iface_enum">The bridge port on which the host was learned.</ArgTableRow>
<ArgTableRow arg="remote-ip" typ="alt { ipv4: ipAddr
, ipv6: ip6Addr
 }">The IP address of the remote tunnel endpoint for a host learned over VXLAN.</ArgTableRow>
<ArgTableRow arg="dhcpv4-ip" typ="ipAddr">The IPv4 address bound to this MAC address in the DHCP snooping binding table.</ArgTableRow>
<ArgTableRow arg="dhcpv4-server-id" typ="ipAddr">The DHCP server that issued the lease for this host.</ArgTableRow>
<ArgTableRow arg="dhcpv4-status" typ="enum (bound | requesting | searching | renewing | rebinding | expired | relay-agent)">The state of the DHCP snooping binding for this host.</ArgTableRow>
<ArgTableRow arg="dhcpv4-expires-after" typ="time">Remaining lifetime of the DHCP snooping binding for this host.</ArgTableRow>
</ArgTable>
