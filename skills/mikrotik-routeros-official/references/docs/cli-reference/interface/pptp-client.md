# pptp-client

> PPTP client interfaces connect to a remote PPTP server. The client entry is disabled by default; enable it to dial.

-----------

## interface/pptp-client 
**Type:** Directory

[PPTP](../../../virtual-private-networks/pptp) client interfaces connect to a remote PPTP server. The client entry is disabled by default; enable it to dial.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled. New client entries are disabled; set `disabled=no` to start the connection.</ArgTableRow>
<ArgTableRow arg="R" typ="running">Whether the interface is running, which means the tunnel is connected.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Interface name.</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">Maximum Transmission Unit: the largest packet the client sends over the PPTP tunnel. The tunnel comes up with the lower of the client and server values. Default: `1450`.</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">Maximum Receive Unit: the largest packet the client receives over the PPTP tunnel. Default: `1450`.</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">Maximum packet size that can be received on the link. If a packet is bigger than the tunnel MTU, it is split into multiple packets, allowing full-size IP or Ethernet packets to be sent over the tunnel. Default: `disabled`.</ArgTableRow>
<ArgTableRow arg="connect-to" typ="alt { address: ipAddr
, name: string
 }" mandatory="1">IPv4 address or DNS name of the PPTP server.</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">User name used for authentication. It must match an account configured on the server (`/ppp/secret` or RADIUS on a RouterOS server).</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password used for authentication. It is stored in the configuration.</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">PPP profile used when establishing the tunnel. Default: `default-encryption`.</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">Keepalive timeout in seconds. `disabled` turns keepalive off. Default: `60`.</ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="enum (no | yes | exclusively) { no:0, yes:1, exclusively:2 }">Whether to use DNS settings from the peer. Default: `no`.</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool">Whether to add a default route through the tunnel. Default: `no`.</ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num">Distance value applied to the auto-created default route when `add-default-route` is enabled.</ArgTableRow>
<ArgTableRow arg="dial-on-demand" typ="bool">Connects to the PPTP server only when outbound traffic is generated. If enabled, a route with a gateway address from 10.112.112.0/24 network is added while the connection is not established. Default: `no`.</ArgTableRow>
<ArgTableRow arg="allow" typ="ubit (pap, chap, mschap1, mschap2)">Allowed authentication methods. Default: `pap,chap,mschap1,mschap2`.</ArgTableRow>
</ArgTable>
