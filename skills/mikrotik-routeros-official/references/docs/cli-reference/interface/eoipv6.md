# eoipv6

> Ethernet over IP (EoIP) Tunneling is a MikroTik RouterOS protocol designed to create an Ethernet tunnel between two routers over an IP network.

-----------

## interface/eoipv6 
**Type:** Directory

[Ethernet over IP (EoIP)](../../virtual-private-networks/eoip.md) Tunneling is a MikroTik RouterOS protocol designed to create an Ethernet tunnel between two routers over an IP network.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the tunnel.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Layer3 maximum transmission unit.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">Media Access Control number of an interface. The address numeration authority IANA allows the use of MAC addresses in the range from 00:00:5E:80:00:00 - 00:00:5E:FF:FF:FF freely.</ArgTableRow>
<ArgTableRow arg="local-address" typ="ip6Addr">Source address of the tunnel packets, local to the router.</ArgTableRow>
<ArgTableRow arg="remote-address" typ="address (flags=6Dvi)" mandatory="1">IPV6 address of the remote end of the EoIP tunnel.</ArgTableRow>
<ArgTableRow arg="tunnel-id" typ="num" mandatory="1">Unique tunnel identifier, which must match the other side of the tunnel.</ArgTableRow>
<ArgTableRow arg="keepalive" typ="super { keepalive-interval: time [1 .. ]
, [keepalive-retries] [ ,num [1 .. ]]
 }">
The keepalive parameter sets the time interval in which the tunnel running flag remains even if the remote end of the tunnel goes down. If the configured time and retries fail, the interface running flag is removed.  
Parameters are written in the following format: `KeepaliveInterval,KeepaliveRetries`  
 where KeepaliveInterval is the time interval and KeepaliveRetries is the number of retry attempts.  
By default keepalive is set to 10 seconds and 10 retries.
</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">DSCP value of the packet. Inherited means the DSCP value is inherited from the packet to be encapsulated.</ArgTableRow>
<ArgTableRow arg="clamp-tcp-mss" typ="bool">Controls whether to change MSS size for received TCP SYN packets. When enabled, the router changes the MSS size for received TCP SYN packets if the current MSS size exceeds the tunnel interface MTU (taking into account the TCP/IP overhead). The received encapsulated packet still contains the original MSS, and only after decapsulation the MSS is changed.</ArgTableRow>
<ArgTableRow arg="dont-fragment" typ="bool">
Whether to include the DF bit in related packets.
- `no` - fragment if needed.
- `inherit` - use the DF flag of the original packet.
</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string" syscap="security">When a secret is specified, the router adds a dynamic IPsec peer to remote-address with a pre-shared key and policy (by default phase2 uses sha1/aes128cbc).</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }">[Address Resolution Protocol](../../getting-started/networking-fundamentals/index.md#arp-and-tying-it-all-together) mode.</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }">Time interval in which ARP entries time out.</ArgTableRow>
<ArgTableRow arg="arp-accept" typ="bool">Whether to accept gratuitous ARP replies.</ArgTableRow>
<ArgTableRow arg="loop-protect" typ="enum (default | off | on) { default:0, off:1, on:2 }">Enables or disables loop protect on the selected interface. `default` works as turned off.</ArgTableRow>
<ArgTableRow arg="loop-protect-send-interval" typ="time">Sets how often loop protect packets are sent on the selected interface.</ArgTableRow>
<ArgTableRow arg="loop-protect-disable-time" typ="time">Sets how long the selected interface is disabled when a loop is detected.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="actual-mtu" typ="num">Actual maximum transmission unit of the tunnel.</ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num">[Layer2 maximum transmission unit](../../hardware/mtu-in-routeros.md). Not configurable for EoIP.</ArgTableRow>
<ArgTableRow arg="current-remote-address" typ="ip6Addr">Current IPv6 address of the remote end.</ArgTableRow>
<ArgTableRow arg="loop-protect-status" typ="enum (off | on | disabled) { off:1, on:2, disabled:3 }">
Loop protection status:
- `on` - loop protect is enabled and the interface is sending and listening for loop protect packets
- `off` - loop protect is disabled
- `disabled` - loop protect is enabled, the interface has received a loop protect packet and disabled itself to prevent a loop.
</ArgTableRow>
</ArgTable>
