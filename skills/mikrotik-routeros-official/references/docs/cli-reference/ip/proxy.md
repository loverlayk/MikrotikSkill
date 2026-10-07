# proxy

> Settings of the web proxy. The proxy forwards the requests of its clients, HTTP, HTTPS (CONNECT) and FTP, and of connections redirected to it with destination NAT, and it caches HTTP responses. Changing any setting...

-----------

## ip/proxy 
**Type:** Settings Directory

Settings of the web proxy. The proxy forwards the requests of its clients, HTTP, HTTPS (`CONNECT`) and FTP, and of connections redirected to it with destination NAT, and it caches HTTP responses. Changing any setting in this menu clears the cache. For an overview and examples, see [Web Proxy](../../../network-management/proxy/web-proxy).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool">Whether the web proxy runs. Default: no.</ArgTableRow>
<ArgTableRow arg="src-address" typ="object { address: alt { address: ipAddr
, address6: ip6Addr
 }
 }">Source address of the connections the proxy opens to servers. It must be an address of the router; otherwise, and when it is not set, the router uses the source address chosen by routing. Default: `::` (not set).</ArgTableRow>
<ArgTableRow arg="port" typ="multi { port: num [1 .. 65535]
 }">TCP port the proxy listens on, or several ports as a comma-separated list, for example `8080,3128`. The proxy listens on all IPv4 and IPv6 addresses of the router, so protect the port with firewall rules. To tell the ports apart in rules, use `local-port` in the access, cache and direct lists. Default: 8080.</ArgTableRow>
<ArgTableRow arg="anonymous" typ="bool">
Whether the proxy tells the server about the client.
- `no` (default) - Add `Via: 1.1 <router address> (Mikrotik HttpProxy)`, `X-Forwarded-For: <client address>` and `X-Proxy-ID` to the requests sent to servers. When a request arrives with `Via` and `X-Forwarded-For` already set, for example from another proxy, the proxy adds its entries to them.
- `yes` - Send none of these headers.
</ArgTableRow>
<ArgTableRow arg="parent-proxy" typ="alt { host: ipAddr
, host6: ip6Addr
 }">IPv4 or IPv6 address of another proxy that receives the requests, HTTPS (`CONNECT`) requests included, except those that [`/ip/proxy/direct`](direct/) sends directly to the server. The parent proxy is used only when `parent-proxy-port` is not 0. When the parent proxy cannot be reached, the client gets an error page; the router does not fall back to a direct connection. Default: `::` (none).</ArgTableRow>
<ArgTableRow arg="parent-proxy-port" typ="num">TCP port of the parent proxy. With 0, no parent proxy is used, even when `parent-proxy` is set. Default: 0.</ArgTableRow>
<ArgTableRow arg="cache-administrator" typ="string">Name or email address shown on the error pages of the proxy as a `mailto:` link, the `$(admin)` variable of the error page template (see [`reset-html`](reset-html)). Default: webmaster.</ArgTableRow>
<ArgTableRow arg="max-cache-size" typ="alt { special: enum (none | unlimited) { none:0, unlimited:0xffffffff }
, value: num
 }">
Largest total size of the cache, in KiB.
- `unlimited` (default) - No limit. A RAM cache can then use most of the router's free memory, so set a limit on a router that runs other services.
- `none` - Do not cache.
- A number - Limit in KiB.
</ArgTableRow>
<ArgTableRow arg="max-cache-object-size" typ="num">Largest response the proxy stores in the cache, in KiB. Larger responses reach the client without being stored. Default: 2048KiB.</ArgTableRow>
<ArgTableRow arg="cache-on-disk" typ="bool">
Where the proxy keeps the cache.
- `no` (default) - In RAM.
- `yes` - On the storage of the router, in the store named by `cache-path`, which `/file` shows with the type `web-proxy store`.
</ArgTableRow>
<ArgTableRow arg="max-client-connections" typ="num">Largest number of client connections the proxy serves at the same time. Further requests wait until a connection is free. Default: 600.</ArgTableRow>
<ArgTableRow arg="max-server-connections" typ="num">Default: 600.</ArgTableRow>
<ArgTableRow arg="max-fresh-time" typ="time">Default: 3d.</ArgTableRow>
<ArgTableRow arg="serialize-connections" typ="bool">Default: no.</ArgTableRow>
<ArgTableRow arg="always-from-cache" typ="bool">Default: no.</ArgTableRow>
<ArgTableRow arg="cache-hit-dscp" typ="num">DSCP value, 0 to 63, the router sets on the packets of responses it serves from the cache. Use it to recognise cache hits in queues and firewall rules. Default: 4.</ArgTableRow>
<ArgTableRow arg="cache-path" typ="string">Name of the cache directory. With `cache-on-disk=yes`, the router creates it on its storage as a `web-proxy store`. A path, for example `usb1/web-proxy` on a disk, needs an existing directory; otherwise the router refuses it with `bad cache path`. It cannot be empty. Default: web-proxy.</ArgTableRow>
</ArgTable>
