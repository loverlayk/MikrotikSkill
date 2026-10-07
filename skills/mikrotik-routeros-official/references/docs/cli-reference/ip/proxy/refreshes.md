# refreshes

> Counters of the cached objects the proxy revalidated with the server before it answered the client. To revalidate an object, the proxy sends a conditional request with If-Modified-Since or If-None-Match. Each counter...

-----------

## ip/proxy/refreshes 
**Type:** Settings Directory

Counters of the cached objects the proxy revalidated with the server before it answered the client. To revalidate an object, the proxy sends a conditional request with `If-Modified-Since` or `If-None-Match`. Each counter counts one reason. For an overview of caching, see [Web Proxy](../../../network-management/proxy/web-proxy).

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="url-requests" typ="num">Objects whose URL has a query string. The proxy revalidates them on every request.</ArgTableRow>
<ArgTableRow arg="request-max-age" typ="num"></ArgTableRow>
<ArgTableRow arg="expired" typ="num"></ArgTableRow>
<ArgTableRow arg="response-max-age" typ="num"></ArgTableRow>
<ArgTableRow arg="config-max-fresh" typ="num"></ArgTableRow>
<ArgTableRow arg="heuristic" typ="num"></ArgTableRow>
<ArgTableRow arg="other" typ="num">Other reasons, for example an object that has an `ETag` header but no `Last-Modified` header.</ArgTableRow>
</ArgTable>
