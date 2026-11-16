# walled-garden

> The /ip/hotspot/walled-garden menu lists the HTTP requests that devices can make before login. The rules of /ip/hotspot/walled-garden/ip are shown here as dynamic entries. See the HotSpot guide.

-----------

## ip/hotspot/walled-garden 
**Type:** Directory

The `/ip/hotspot/walled-garden` menu lists the HTTP requests that devices can make before login. The rules of `/ip/hotspot/walled-garden/ip` are shown here as dynamic entries. See the [HotSpot](../../../../authentication-authorization-accounting/hotspot-captive-portal) guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The rule is disabled.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">The rule is dynamic.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="server" typ="super { !
, server: enum
 }">HotSpot server to which the rule applies.</ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, range: ipRange
 }">IP address of the client.</ArgTableRow>
<ArgTableRow arg="method" typ="super { !
, method: enum (GET | HEAD | POST | PUT | CONNECT | OPTIONS | DELETE | TRACE)
 }">HTTP method of the request.</ArgTableRow>
<ArgTableRow arg="dst-host" typ="super { !
, host: string
 }">Host name of the web server. It must match the whole name. `*` stands for any number of characters, `?` for one character. A value that starts with `:` is a regular expression.</ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, ports: multi { ports: range [ .. 65535]
 }
 }">TCP port of the request.</ArgTableRow>
<ArgTableRow arg="path" typ="super { !
, path: string
 }">Path of the request, the part after the host name. It is matched in the same way as `dst-host`.</ArgTableRow>
<ArgTableRow arg="action" typ="enum (allow | deny)">`allow` - the request passes without login. `deny` - the request needs a login.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="dst-address" typ="super { !
, range: ipRange
 }">IP address of the web server.</ArgTableRow>
<ArgTableRow arg="hits" typ="num">Number of requests that matched the rule.</ArgTableRow>
</ArgTable>
