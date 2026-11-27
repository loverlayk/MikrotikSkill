# controller

> Networks that the router's own ZeroTier controller hosts. For a configuration example, see Self-hosted ZeroTier controller on a hAP ax³.

-----------

## zerotier/controller 
**Package:** zerotier
**Type:** Directory

Networks that the router's own ZeroTier controller hosts. For a configuration example, see [Self-hosted ZeroTier controller on a hAP ax³](../../../virtual-private-networks/zerotier-controller).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">Whether the controller is inactive.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="disabled" typ="bool">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1">ZeroTier instance name.</ArgTableRow>
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the network. Members see it as `network-name` in `/zerotier/interface`.</ArgTableRow>
<ArgTableRow arg="network" typ="string">16-digit network ID. Without it, the router creates the ID when it adds the network; the first ten digits are the ZeroTier address of the instance.</ArgTableRow>
<ArgTableRow arg="private" typ="bool">Access control of the network. With `yes`, a device joins only after its entry in `/zerotier/controller/member` has `authorized=yes`. With `no`, every device that knows the network ID is authorized when it joins.</ArgTableRow>
<ArgTableRow arg="broadcast" typ="bool">Allows receiving broadcast (FF:FF:FF:FF:FF:FF) packets.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Network MTU.</ArgTableRow>
<ArgTableRow arg="multicast-limit" typ="num">Maximum recipients for a multicast packet.</ArgTableRow>
<ArgTableRow arg="ip-range" typ="super { first: address (flags=4)
, [last] [ -address (flags=4)]
 }">Range of addresses for members that have no `ip-address`, for example, 172.16.16.1-172.16.16.254.</ArgTableRow>
<ArgTableRow arg="ip6-range" typ="super { first: address (flags=6)
, [last] [ -address (flags=6)]
 }">IPv6 range, for example, `fd00:feed:feed:beef::-fd00:feed:feed:beef:ffff:ffff:ffff:ffff`.</ArgTableRow>
<ArgTableRow arg="ip6-rfc4193" typ="bool">The rfc4193 mode gives every member a /128 on a /88 network.</ArgTableRow>
<ArgTableRow arg="ip6-6plane" typ="bool">Gives every member a /80 within a /40 network and uses NDP emulation to route all IPs under that /80 to its owner.</ArgTableRow>
<ArgTableRow arg="routes" typ="object { route: super { dst: address (flags=46/)
, [gw] [ @address (flags=46)]
 }
 }">Routes that the members get, in the format `Routes ::= Route[,Routes] Route ::= Dst[@Gw]`. A member gets an address from `ip-range` only when `routes` has a subnet that contains it; for example, `ip-range=172.27.27.10-172.27.27.20` with `routes=172.27.27.0/24`.</ArgTableRow>
</ArgTable>
