# interface

> RouterOS directory reference for /zerotier/interface.

-----------

## zerotier/interface 
**Package:** zerotier
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">Whether the interface was created dynamically.</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="R" typ="running">Whether the interface is running.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Short name for the interface.</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }">ARP timeout value.</ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool">Forces the interface into running state.</ArgTableRow>
<ArgTableRow arg="network" typ="string" mandatory="1">16-digit network ID.</ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1">ZeroTier instance name.</ArgTableRow>
<ArgTableRow arg="allow-managed" typ="bool">ZeroTier managed IP addresses and routes are assigned.</ArgTableRow>
<ArgTableRow arg="allow-global" typ="bool">ZeroTier IP addresses and routes can overlap public IP space.</ArgTableRow>
<ArgTableRow arg="allow-default" typ="bool">The network can override the system default route (force VPN mode).</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the ZeroTier interface.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Maximum transmission unit of the interface.</ArgTableRow>
<ArgTableRow arg="bridge" typ="bool">Whether the interface acts as a bridge.</ArgTableRow>
<ArgTableRow arg="dhcp" typ="bool">Whether DHCP is enabled on the interface.</ArgTableRow>
<ArgTableRow arg="network-name" typ="string">Human-readable network name from the controller.</ArgTableRow>
<ArgTableRow arg="status" typ="string">Current status of the interface on the network.</ArgTableRow>
<ArgTableRow arg="type" typ="string">Type of the network interface.</ArgTableRow>
</ArgTable>
