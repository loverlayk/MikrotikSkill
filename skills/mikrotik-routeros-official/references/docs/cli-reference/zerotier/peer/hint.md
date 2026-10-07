# hint

> RouterOS directory reference for /zerotier/peer/hint.

-----------

## zerotier/peer/hint 
**Package:** zerotier
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum" mandatory="1">ZeroTier instance name.</ArgTableRow>
<ArgTableRow arg="identity" typ="string" mandatory="1">ZeroTier identity of the peer.</ArgTableRow>
<ArgTableRow arg="addresses" typ="multi { array-id, array-id, address: composite { addr: address (flags=46)
, port: num [1 .. 65535]
 }
 }" mandatory="1">List of IP addresses and ports for the peer.</ArgTableRow>
</ArgTable>
