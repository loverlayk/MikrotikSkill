# vteps

> View and configure remote VXLAN tunnel endpoints (VTEPs). Static entries provide head-end replication for broadcast, unknown-unicast, and multicast traffic and can carry a comment; dynamic entries can be supplied by...

-----------

## interface/vxlan/vteps 
**Type:** Directory

View and configure remote VXLAN tunnel endpoints (VTEPs). Static entries provide head-end replication for broadcast, unknown-unicast, and multicast traffic and can carry a `comment`; dynamic entries can be supplied by EVPN. See the [VXLAN guide](../../../bridging-and-switching/vxlan) for forwarding and configuration examples.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">Whether the VTEP entry is dynamic rather than statically configured.</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">Whether the VTEP entry is disabled.</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">Whether the VTEP entry is hardware-offloaded on a supported device.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Name of the VXLAN interface to which this remote VTEP entry belongs.</ArgTableRow>
<ArgTableRow arg="remote-ip" typ="alt { address: ipAddr
, ipv6-address: ip6Addr
 }" mandatory="1">IPv4 or IPv6 address of the remote VTEP used for broadcast, unknown-unicast, and multicast (BUM) flooding. Without a multicast underlay, the router replicates BUM traffic to every static VTEP. Static entries do not restrict received packets and are not access-control rules. The address family must match the VXLAN interface `vteps-ip-version`; opposite-family entries are ignored.</ArgTableRow>
</ArgTable>
