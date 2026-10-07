# cache-contents

> Objects in the cache of the web proxy. Remove an entry to make the proxy fetch the object from the server on the next request. To empty the whole cache, use clear-cache. For an overview of caching, see Web Proxy.

-----------

## ip/proxy/cache-contents 
**Type:** Directory

Objects in the cache of the web proxy. Remove an entry to make the proxy fetch the object from the server on the next request. To empty the whole cache, use [`clear-cache`](clear-cache). For an overview of caching, see [Web Proxy](../../../network-management/proxy/web-proxy).

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="uri" typ="string">URL of the object.</ArgTableRow>
<ArgTableRow arg="file-size" typ="num">Size of the object, in KiB.</ArgTableRow>
<ArgTableRow arg="last-modified" typ="date">Date the proxy stored the object. It is not the `Last-Modified` header of the response.</ArgTableRow>
<ArgTableRow arg="last-modified-time" typ="date">Time the proxy stored the object.</ArgTableRow>
<ArgTableRow arg="last-accessed" typ="date"></ArgTableRow>
<ArgTableRow arg="last-accessed-time" typ="date"></ArgTableRow>
</ArgTable>
