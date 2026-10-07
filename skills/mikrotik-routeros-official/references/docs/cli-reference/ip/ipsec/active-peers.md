# active-peers

> This menu provides various statistics about remote peers that currently have established a phase 1 connection.

-----------

## ip/ipsec/active-peers 
**Type:** Directory

This menu provides various statistics about remote peers that currently have established a phase 1 connection.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="responder">Whether the peer is a responder.</ArgTableRow>
<ArgTableRow arg="N" typ="natt-peer">Whether NAT traversal is used for the peer.</ArgTableRow>
<ArgTableRow arg="P" typ="ppk">Whether post-quantum preshared key is used.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="id" typ="string">Peer identifier.</ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">Local IP address.</ArgTableRow>
<ArgTableRow arg="port" typ="num">Remote port.</ArgTableRow>
<ArgTableRow arg="remote-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">Remote IP address.</ArgTableRow>
<ArgTableRow arg="state" typ="enum (spawning | starting | message-1-received | message-1-sent | message-2-received | message-2-sent | message-3-received | message-3-sent | message-4-received | established | expired | no-phase1 | eap | crypto | qkd) { spawning:0, starting:1, message-1-received:2, message-1-sent:3, message-2-received:4, message-2-sent:5, message-3-received:6, message-3-sent:7, message-4-received:8, established:9, expired:10, no-phase1:11 }">Current IKE phase 1 state.</ArgTableRow>
<ArgTableRow arg="side" typ="enum (initiator | responder)">Whether the peer acts as a responder.</ArgTableRow>
<ArgTableRow arg="dynamic-address" typ="alt { ip: ipAddr
 }">Dynamically assigned address.</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">Connection uptime.</ArgTableRow>
<ArgTableRow arg="last-seen" typ="time">Time since the last received packet.</ArgTableRow>
<ArgTableRow arg="ph2-total" typ="num">Total number of phase 2 exchanges.</ArgTableRow>
<ArgTableRow arg="spii" typ="string">Initiator SPI value.</ArgTableRow>
<ArgTableRow arg="spir" typ="string">Responder SPI value.</ArgTableRow>
<ArgTableRow arg="rx-packets" typ="num">Number of received packets.</ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num">Number of received bytes.</ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num">Number of transmitted packets.</ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num">Number of transmitted bytes.</ArgTableRow>
</ArgTable>
