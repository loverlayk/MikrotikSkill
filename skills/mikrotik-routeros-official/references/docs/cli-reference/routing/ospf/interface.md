# interface

> RouterOS directory reference for /routing/ospf/interface.

-----------

## routing/ospf/interface 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" unset="1"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=4i)" unset="1"></ArgTableRow>
<ArgTableRow arg="area" typ="enum"></ArgTableRow>
<ArgTableRow arg="instance-id" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (broadcast | nbma | ptp | ptp-unnumbered | ptmp | ptmp-broadcast | virtual-link)">
The OSPF network type on this interface. Note that if interface configuration does not exist, the default network type is 'ptp' on PtP interfaces and 'broadcast' on all other interfaces.
- `broadcast` - Network type suitable for Ethernet and other multicast capable link layers. Elects designated router.
- `nbma` - Non-Broadcast Multiple Access. Protocol packets are sent to each neighbor's unicast address. Requires manual configuration of neighbors. Elects designated router.
- `ptp` - Suitable for networks that consist only of two nodes. Does not elect a designated router.
- `ptmp` - Point-to-Multipoint. Easier to configure than NBMA because it requires no manual configuration of a neighbor. Does not elect a designated router. This is the most robust network type and as such suitable for wireless networks, if 'broadcast' mode does not work well enough for them
- `ptp-unnumbered` - Works the same as ptp, except that the remote neighbor does not have an associated IP address to a specific PTP interface. For example, in case IP unnumbered is used on Cisco devices.
- `virtual-link` - Interface for virtual link.
</ArgTableRow>
<ArgTableRow arg="auth" typ="enum (simple | md5 | sha1 | sha256 | sha384 | sha512)" unset="1"></ArgTableRow>
<ArgTableRow arg="auth-key" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="auth-id" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="cost" typ="num"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="passive" typ="switch"></ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="retransmit-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="transmit-delay" typ="time"></ArgTableRow>
<ArgTableRow arg="hello-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="dead-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="vlink-transit-area" typ="enum" unset="1">A non-backbone area the two routers have in common over which the virtual link will be established. Virtual links can not be established through stub areas.</ArgTableRow>
<ArgTableRow arg="vlink-neighbor-id" typ="ipAddr" unset="1">Specifies the **router-id** of the neighbor which should be connected over the virtual link.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="state" typ="enum (down | loopback | ptp | passive | waiting | standby | dr-other | bdr | dr)"></ArgTableRow>
<ArgTableRow arg="dr" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="bdr" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="vlink-remote-address" typ="address (flags=46)"></ArgTableRow>
</ArgTable>
