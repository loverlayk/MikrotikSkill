# gre

> Generic Routing Encapsulation (GRE) is a tunneling protocol originally developed by Cisco to encapsulate a wide variety of network layer protocols over an IP network.

-----------

## interface/gre 
**Type:** Directory

[Generic Routing Encapsulation (GRE)](../../virtual-private-networks/gre.md) is a tunneling protocol originally developed by Cisco to encapsulate a wide variety of network layer protocols over an IP network.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="R" typ="running">Whether the interface is running.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the tunnel.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Layer3 maximum transmission unit of the tunnel. Default: `auto` — the router subtracts the 24-byte GRE/IP overhead from the outgoing interface MTU (actual-mtu is 1476 on a 1500-byte interface).</ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr">IP address used for the local tunnel end. If set to 0.0.0.0, the IP address of the outgoing interface is used.</ArgTableRow>
<ArgTableRow arg="remote-address" typ="address (flags=4Dv)" mandatory="1">IP address of the remote tunnel end.</ArgTableRow>
<ArgTableRow arg="keepalive" typ="super { keepalive-interval: time [1 .. ]
, [keepalive-retries] [ ,num [1 .. ]]
 }">
The keepalive parameter sets how often the router checks the remote end of the tunnel: the router sends GRE echo probes to the remote end every `KeepaliveInterval` seconds, repeated up to `KeepaliveRetries` times. The minimum interval is 1 second and a 0-second setting is rejected; unsetting `keepalive` turns it off, but on current RouterOS that does not change the running-flag behavior. By default keepalive is set to 10 seconds and 10 retries. On current RouterOS the tunnel keeps the running flag while it is enabled, even when the remote end stops answering; the tunneled traffic is then dropped until the remote end responds again.  
Parameters are written in the following format: `KeepaliveInterval,KeepaliveRetries`  
 where KeepaliveInterval is the time interval and KeepaliveRetries is the number of retry attempts.
</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">DSCP value of the packet. Inherited means the DSCP value is inherited from the tunneled traffic.</ArgTableRow>
<ArgTableRow arg="clamp-tcp-mss" typ="bool">Controls whether to change the MSS size for received TCP SYN packets. When enabled, the router changes the MSS size for received TCP SYN packets if the current MSS size exceeds the tunnel interface MTU (taking into account the TCP/IP overhead). The received encapsulated packet still contains the original MSS, and only after decapsulation the MSS is changed.</ArgTableRow>
<ArgTableRow arg="dont-fragment" typ="bool">
Whether to include the DF bit in related packets. Default: `no` — `yes` is rejected on RouterOS 7, only `no` and `inherit` are valid.
- `no` - fragment if needed.
- `inherit` - use the DF flag of the original packet.
</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string" syscap="security">When a secret is specified, the router adds a dynamic IPsec peer to remote-address with a pre-shared key and policy (by default phase2 uses sha1/aes128cbc).</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">Whether to allow FastPath processing. Must be disabled if IPsec tunneling is used.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="actual-mtu" typ="num">Actual maximum transmission unit of the tunnel.</ArgTableRow>
<ArgTableRow arg="current-remote-address" typ="ipAddr">Current IP address of the remote end.</ArgTableRow>
</ArgTable>
