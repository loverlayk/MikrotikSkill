# server

> RouterOS directory reference for /interface/pppoe-server/server.

-----------

## interface/pppoe-server/server 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">Whether the server configuration is invalid.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="service-name" typ="string">The PPPoE service name. Server accepts clients that send a PADI message with service-names that match this setting, or if the service-name field in the PADI message is not set.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum { <l2tp>:0xfffffffe }" mandatory="1">Interface that the clients are connected to.</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">Maximum Transmission Unit. The optimal value is the MTU of the interface the tunnel is working over reduced by 20 (so, for 1500-byte Ethernet link, set the MTU to 1480 to avoid fragmentation of packets).</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">Maximum Receive Unit. The optimal value is the MTU of the interface the tunnel is working over reduced by 20 (so, for 1500-byte Ethernet link, set the MTU to 1480 to avoid fragmentation of packets).</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">Maximum packet size that can be received on the link. If a packet is bigger than tunnel MTU, it is split into multiple packets, allowing full-size IP or Ethernet packets to be sent over the tunnel.</ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)">Authentication methods that the server accepts.</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">Defines the time period (in seconds) after which the router starts sending keepalive packets every second. If no traffic and no keepalive responses arrive for twice the `keepalive-timeout`, the non-responding client is disconnected. Set to `disabled` to turn off echo packets.</ArgTableRow>
<ArgTableRow arg="one-session-per-host" typ="bool">Allow only one session per host (determined by MAC address). If a host tries to establish a new session, the old one is closed.</ArgTableRow>
<ArgTableRow arg="max-sessions" typ="num">Maximum number of clients that the AC can serve. `0` means no limitation.</ArgTableRow>
<ArgTableRow arg="pado-delay" typ="num">Delay in milliseconds before sending PADO response.</ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum">Specifies which PPP profile configuration is used when establishing the tunnel.</ArgTableRow>
<ArgTableRow arg="accept-empty-service" typ="bool">Accept PADI with empty service name if no matching PPPoE service is available.</ArgTableRow>
<ArgTableRow arg="pppoe-over-vlan-range" typ="multi { vlan-range: range [1 .. 4094]
 }">
This setting allows a PPPoE server to operate over 802.1Q VLANs. Supports a range of VLAN IDs and individual VLANs specified with comma-separated values, for example: `100-115,120,122,128-130`.  

When you specify the VLAN IDs, the PPPoE server will accept 802.1Q tagged packets from clients, and it will reply using the same VLAN. You then have an option to accept or drop untagged PPPoE clients on the same interface using the `accept-untagged` property.  
You can configure the PPPoE server with `pppoe-over-vlan-range` setting even on VLAN interface enabling the QinQ setups as well. But keep in mind that the inner VLAN tag should be 802.1Q.
</ArgTableRow>
<ArgTableRow arg="accept-untagged" typ="bool">Whether to accept untagged (non-VLAN) PPPoE packets on the interface when `pppoe-over-vlan-range` is specified.</ArgTableRow>
</ArgTable>
