# inserts

> Counters of the objects the proxy writes to its cache. For an overview of caching, see Web Proxy.

-----------

## ip/proxy/inserts 
**Type:** Settings Directory

Counters of the objects the proxy writes to its cache. For an overview of caching, see [Web Proxy](../../../network-management/proxy/web-proxy).

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="successes" typ="num">Objects stored in the cache.</ArgTableRow>
<ArgTableRow arg="denied" typ="num">Responses not stored because a [`/ip/proxy/cache`](cache/) rule with `action=deny` matched the request.</ArgTableRow>
<ArgTableRow arg="too-large" typ="num"></ArgTableRow>
<ArgTableRow arg="no-memory" typ="num"></ArgTableRow>
<ArgTableRow arg="errors" typ="num"></ArgTableRow>
</ArgTable>
