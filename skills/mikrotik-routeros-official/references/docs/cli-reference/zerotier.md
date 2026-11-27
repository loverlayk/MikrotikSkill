# zerotier

> The ZeroTier network hypervisor is a self-contained network virtualization engine that implements an Ethernet virtualization layer on top of a peer-to-peer network. To host your own network, see Self-hosted ZeroTier...

-----------

## zerotier 
**Package:** zerotier
**Type:** Directory

The [ZeroTier](../../virtual-private-networks/zerotier.md) network hypervisor is a self-contained network virtualization engine that implements an Ethernet virtualization layer on top of a peer-to-peer network. To host your own network, see [Self-hosted ZeroTier controller on a hAP ax³](../../virtual-private-networks/zerotier-controller).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="R" typ="online">Whether the instance is online.</ArgTableRow>
<ArgTableRow arg="F" typ="tcp-fallback">Whether TCP fallback is active.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Instance name.</ArgTableRow>
<ArgTableRow arg="disabled" typ="bool">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="port" typ="num">Port number the instance listens to.</ArgTableRow>
<ArgTableRow arg="identity" typ="string">Identity of the instance: its ZeroTier address (the first ten characters), the public key and the secret key. `/export` leaves it out and `/export show-sensitive` includes it. `identity.public` shows the identity without the secret key.</ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, interface: iface_enum
 }">List of interfaces used to discover ZeroTier peers with ARP and IP type connections.</ArgTableRow>
<ArgTableRow arg="route-distance" typ="num">Route distance for routes obtained from planet/moon servers.</ArgTableRow>
<ArgTableRow arg="backup-priorities" typ="multi { array-id, array-id, backup-priority: composite { interface: iface_enum
, priority: num
 }
 }">Backup interface priorities for failover.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="identity.public" typ="string">Public identity of the instance.</ArgTableRow>
<ArgTableRow arg="state" typ="string">Current state of the instance.</ArgTableRow>
<ArgTableRow arg="moons" typ="multi { array-id, moon: string
 }">List of moons the instance is connected to.</ArgTableRow>
</ArgTable>
