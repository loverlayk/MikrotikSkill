# wireguard

> WireGuard creates encrypted IP tunnels between peers identified by public keys.

-----------

## interface/wireguard 
**Type:** Directory

[WireGuard](../../../virtual-private-networks/wireguard) creates encrypted IP tunnels between peers identified by public keys.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="R" typ="running">Whether the interface is running.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the tunnel.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Layer3 maximum transmission unit.</ArgTableRow>
<ArgTableRow arg="listen-port" typ="num">Port for the WireGuard service to listen on for incoming sessions.</ArgTableRow>
<ArgTableRow arg="private-key" typ="string">A base64 private key. If not specified, it is automatically generated upon interface creation. Each network interface has a private key and a list of peers.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">Specifies which VRF the WireGuard UDP socket uses to determine how encrypted packets are sent or received.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="public-key" typ="string">A base64 public key calculated from the private key. Public keys are used by peers to authenticate each other.</ArgTableRow>
</ArgTable>
