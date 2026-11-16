# server

> Global settings for the PPTP server. The server listens on TCP port 1723 when enabled.

-----------

## interface/pptp-server/server 
**Type:** Settings Directory

Global settings for the [PPTP](../../../virtual-private-networks/pptp) server. The server listens on TCP port 1723 when enabled.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool">Defines whether the PPTP server is enabled. Default: `no`.</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">Maximum Transmission Unit: the largest packet the server sends over a PPTP tunnel. The tunnel comes up with the lower of the client and server values. Default: `1450`.</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">Maximum Receive Unit: the largest packet the server receives over a PPTP tunnel. Default: `1450`.</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">Maximum packet size that can be received on the link. If a packet is bigger than the tunnel MTU, it is split into multiple packets, allowing full-size IP or Ethernet packets to be sent over the tunnel. Default: `disabled`.</ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)">Authentication methods that the server accepts. Default: `mschap1,mschap2`.</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">If the server receives no packet during the keepalive period, it sends keepalive packets once per second, up to five times, and disconnects the client if none is answered. Default: `30`.</ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum">PPP profile used when establishing the tunnel unless the secret specifies another one. Default: `default-encryption`.</ArgTableRow>
</ArgTable>
