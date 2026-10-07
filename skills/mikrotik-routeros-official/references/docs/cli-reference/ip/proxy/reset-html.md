# reset-html

> Writes the default template of the proxy's error page to the file webproxy/error.html on the router and replaces a changed copy. The proxy builds its error pages, for example the page for a request denied by...

-----------

## ip/proxy/reset-html 
**Type:** Command

Writes the default template of the proxy's error page to the file `webproxy/error.html` on the router and replaces a changed copy. The proxy builds its error pages, for example the page for a request denied by [`/ip/proxy/access`](access/), from this file, so you can edit it; the proxy uses the changed file at once. Without the file, the proxy uses the same page built in. The template uses the variables `$(status)`, `$(url)`, `$(error)`, `$(admin)` (the `cache-administrator` setting) and `$(signature)`, and the block `$(if error)` ... `$(endif)`. For an overview, see [Web Proxy](../../../network-management/proxy/web-proxy).
