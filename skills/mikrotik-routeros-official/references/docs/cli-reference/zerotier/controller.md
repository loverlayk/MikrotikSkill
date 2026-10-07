# controller

> Zerotier configuration controller.

-----------

## zerotier/controller 
**Package:** zerotier
**Type:** Directory

Zerotier configuration controller.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">Whether the controller is inactive.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="disabled" typ="bool">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1">ZeroTier instance name.</ArgTableRow>
<ArgTableRow arg="name" typ="string" mandatory="1">Short name for this controller.</ArgTableRow>
<ArgTableRow arg="network" typ="string">16-digit network ID.</ArgTableRow>
<ArgTableRow arg="private" typ="bool">Enables access control.</ArgTableRow>
<ArgTableRow arg="broadcast" typ="bool">Allows receiving broadcast (FF:FF:FF:FF:FF:FF) packets.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Network MTU.</ArgTableRow>
<ArgTableRow arg="multicast-limit" typ="num">Maximum recipients for a multicast packet.</ArgTableRow>
<ArgTableRow arg="ip-range" typ="super { first: address (flags=4)
, [last] [ -address (flags=4)]
 }">IP range, for example, 172.16.16.1-172.16.16.254.</ArgTableRow>
<ArgTableRow arg="ip6-range" typ="super { first: address (flags=6)
, [last] [ -address (flags=6)]
 }">IPv6 range, for example, `fd00:feed:feed:beef::-fd00:feed:feed:beef:ffff:ffff:ffff:ffff`.</ArgTableRow>
<ArgTableRow arg="ip6-rfc4193" typ="bool">The rfc4193 mode gives every member a /128 on a /88 network.</ArgTableRow>
<ArgTableRow arg="ip6-6plane" typ="bool">Gives every member a /80 within a /40 network and uses NDP emulation to route all IPs under that /80 to its owner.</ArgTableRow>
<ArgTableRow arg="routes" typ="object { route: super { dst: address (flags=46/)
, [gw] [ @address (flags=46)]
 }
 }">Push routes in the following format: `Routes ::= Route[,Routes] Route ::= Dst[@Gw]`.</ArgTableRow>
</ArgTable>
