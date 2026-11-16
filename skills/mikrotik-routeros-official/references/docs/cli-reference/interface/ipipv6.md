# ipipv6

> IPIP (IP-in-IP) carries IPv4 packets inside an outer IPv6 header. The outer header uses next header 4 (IPIP), and the inner packet is still IPv4.

-----------

## interface/ipipv6 
**Type:** Directory

[IPIP](../../virtual-private-networks/ipip.md) (IP-in-IP) carries IPv4 packets inside an outer IPv6 header. The outer header uses next header 4 (IPIP), and the inner packet is still IPv4.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="R" typ="running">Whether the interface is running.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Interface name.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Layer 3 maximum transmission unit of the tunnel. Default: `auto`, which sets `actual-mtu` to the MTU of the underlying interface minus 40 bytes for the outer IPv6 header. A fixed value overrides this calculation.</ArgTableRow>
<ArgTableRow arg="local-address" typ="ip6Addr">IPv6 address on the router used by the tunnel. The remote router must reach this address as its `remote-address`.</ArgTableRow>
<ArgTableRow arg="remote-address" typ="address (flags=6Dvi)" mandatory="1">IPv6 address of the remote end of the tunnel. The router must have a route to this address that does not use the tunnel itself.</ArgTableRow>
<ArgTableRow arg="keepalive" typ="super { keepalive-interval: time [1 .. ]
, [keepalive-retries] [ ,num [1 .. ]]
 }">
Sends keepalive probes to the remote endpoint and keeps the running flag only while the peer answers. The interface running flag is removed after `KeepaliveRetries` consecutive unanswered probes.
Parameters are written in the following format: `KeepaliveInterval,KeepaliveRetries`
where KeepaliveInterval is the time interval between probes and KeepaliveRetries is the number of retry attempts.
Default: `10s,10`. The interval must be at least 1 second and the retry count at least 1. The remote end must answer RouterOS keepalive probes; peers such as a Linux `ipip` tunnel do not, so unset the property for them. Unsetting keepalive disables dead-peer detection: the running flag stays set when the peer stops answering.
</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">DSCP value set in the outer header of tunnel packets. Default: `inherit`, which copies the DSCP value from the tunneled packet. A number marks the outer packets with that value instead.</ArgTableRow>
<ArgTableRow arg="clamp-tcp-mss" typ="bool">Controls whether to change the MSS size for received TCP SYN packets. When enabled, the router changes the MSS size for received TCP SYN packets if the current MSS size exceeds the tunnel interface MTU (taking into account the TCP/IP overhead). The received encapsulated packet still contains the original MSS, and only after decapsulation the MSS is changed. Default: `yes`.</ArgTableRow>
<ArgTableRow arg="dont-fragment" typ="bool">
Whether to set the DF bit in the outer header.
- `no` - clear the DF bit, so the outer packet can be fragmented. Default.
- `inherit` - use the DF flag of the tunneled packet.
</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string" syscap="security">When a secret is specified, the router adds a dynamic IPsec peer to remote-address with a pre-shared key and a transport-mode policy for the tunnel packets, using the default IPsec proposal. Keepalive packets are protected too. Both ends need the same secret. This menu has no `allow-fast-path` property, so no FastPath step is needed.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="actual-mtu" typ="num">Actual maximum transmission unit of the tunnel: the largest inner packet the tunnel accepts. With `mtu=auto` it follows the MTU of the underlying interface minus the outer header size, and becomes smaller when IPsec is enabled.</ArgTableRow>
<ArgTableRow arg="current-remote-address" typ="ip6Addr">Current IPv6 address of the remote end.</ArgTableRow>
</ArgTable>
