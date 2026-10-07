# peer

> ZeroTier's peer is an informative section with a list of nodes that your node knows about. Nodes can not talk to each other unless they are joined and authorized on the same network.

-----------

## zerotier/peer 
**Package:** zerotier
**Type:** Directory

ZeroTier's peer is an informative section with a list of nodes that your node knows about. Nodes can not talk to each other unless they are joined and authorized on the same network.

```ros
[admin@Home] > `/zerotier/peer/print` 
Columns: INSTANCE, ZT-ADDRESS, LATENCY, ROLE, PATH
# INSTANCE  ZT-ADDRESS  LATENCY  ROLE    PATH
0 zt1       61d294b9cb  186ms    PLANET  active,preferred,50.7.73.34/9993,recvd:4s526ms                  
1 zt1       62f865ae71  270ms    PLANET  active,preferred,50.7.252.138/9993,recvd:4s440ms,sent:9s766ms   
2 zt1       778cde7190  132ms    PLANET  active,preferred,103.195.103.66/9993,recvd:4s579ms,sent:9s766ms 
3 zt1       992fcf1db7  34ms     PLANET  active,preferred,195.181.173.159/9993,recvd:4s675ms,sent:4s712ms
4 zt1       159924d630  130ms    LEAF    active,preferred,34.121.192.xx/21002,recvd:3s990ms,sent:3s990ms
```

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="B" typ="bonded">Whether the peer is bonded.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum">ZeroTier instance name.</ArgTableRow>
<ArgTableRow arg="zt-address" typ="string">ZeroTier address of the peer.</ArgTableRow>
<ArgTableRow arg="bonded" typ="bool">Whether the peer is bonded.</ArgTableRow>
<ArgTableRow arg="latency" typ="time">Latency to the peer.</ArgTableRow>
<ArgTableRow arg="role" typ="string">Role of the peer (PLANET, MOON, or LEAF).</ArgTableRow>
<ArgTableRow arg="path" typ="multi { array-id, path: string
 }">Active path to the peer.</ArgTableRow>
</ArgTable>
