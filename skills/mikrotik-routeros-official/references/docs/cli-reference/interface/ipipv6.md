# ipipv6

> IPIP (IP-in-IP) is a simple tunneling protocol defined in RFC 2003 that encapsulates IP packets within another IP header to transport traffic between two endpoints.

-----------

## interface/ipipv6 
**Type:** Directory

[IPIP](../../virtual-private-networks/ipip.md) (IP-in-IP) is a simple tunneling protocol defined in RFC 2003 that encapsulates IP packets within another IP header to transport traffic between two endpoints.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="R" typ="running">Whether the interface is running.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Interface name.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Layer3 maximum transmission unit.</ArgTableRow>
<ArgTableRow arg="local-address" typ="ip6Addr">IP address on the router used by the IPIP tunnel.</ArgTableRow>
<ArgTableRow arg="remote-address" typ="address (flags=6Dvi)" mandatory="1">IP address of the remote end of the IPIP tunnel.</ArgTableRow>
<ArgTableRow arg="keepalive" typ="super { keepalive-interval: time [1 .. ]
, [keepalive-retries] [ ,num [1 .. ]]
 }">
The keepalive parameter sets the time interval in which the tunnel running flag remains even if the remote end of the tunnel goes down. If the configured time and retries fail, the interface running flag is removed.  
Parameters are written in the following format: `KeepaliveInterval,KeepaliveRetries`  
 where KeepaliveInterval is the time interval and KeepaliveRetries is the number of retry attempts.  
By default keepalive is set to 10 seconds and 10 retries.
</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">DSCP value of the packet. Inherited means the DSCP value is inherited from the tunneled traffic.</ArgTableRow>
<ArgTableRow arg="clamp-tcp-mss" typ="bool">Controls whether to change the MSS size for received TCP SYN packets. When enabled, the router changes the MSS size for received TCP SYN packets if the current MSS size exceeds the tunnel interface MTU (taking into account the TCP/IP overhead). The received encapsulated packet still contains the original MSS, and only after decapsulation the MSS is changed.</ArgTableRow>
<ArgTableRow arg="dont-fragment" typ="bool">
Whether to include the DF bit in related packets.
- `no` - fragment if needed.
- `inherit` - use the DF flag of the original packet.
</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string" syscap="security">When a secret is specified, the router adds a dynamic IPsec peer to remote-address with a pre-shared key and policy (by default phase2 uses sha1/aes128cbc).</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="actual-mtu" typ="num">Actual maximum transmission unit of the tunnel.</ArgTableRow>
<ArgTableRow arg="current-remote-address" typ="ip6Addr">Current IP address of the remote end.</ArgTableRow>
</ArgTable>
