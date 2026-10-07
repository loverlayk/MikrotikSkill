# walled-garden

> RouterOS directory reference for /ip/hotspot/walled-garden.

-----------

## ip/hotspot/walled-garden 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="server" typ="super { !
, server: enum
 }"></ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, range: ipRange
 }"></ArgTableRow>
<ArgTableRow arg="method" typ="super { !
, method: enum (GET | HEAD | POST | PUT | CONNECT | OPTIONS | DELETE | TRACE)
 }"></ArgTableRow>
<ArgTableRow arg="dst-host" typ="super { !
, host: string
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, ports: multi { ports: range [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="path" typ="super { !
, path: string
 }"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (allow | deny)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="dst-address" typ="super { !
, range: ipRange
 }"></ArgTableRow>
<ArgTableRow arg="hits" typ="num"></ArgTableRow>
</ArgTable>
