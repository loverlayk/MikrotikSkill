# access

> Rules that allow, deny, redirect or change the requests of proxy clients, HTTP and HTTPS (CONNECT) requests alike. The proxy checks the rules from top to bottom, and the first matching rule decides. A request that...

-----------

## ip/proxy/access 
**Type:** Directory

Rules that allow, deny, redirect or change the requests of proxy clients, HTTP and HTTPS (`CONNECT`) requests alike. The proxy checks the rules from top to bottom, and the first matching rule decides. A request that matches no rule is allowed. A rule without matchers matches every request. Prefix a matcher value with `!` to negate it, for example `src-address=!192.168.88.0/24`. For examples, see [Web Proxy](../../../../network-management/proxy/web-proxy).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled. The rule is not used. New rules are created enabled.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="src-address" typ="super { !
, range: alt { ip4: ipRange
, ip6: ip6Prefix
 }
 }">Address of the client: an IPv4 address, range or prefix, or an IPv6 prefix.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, range: alt { ip4: ipRange
, ip6: ip6Prefix
 }
 }">Address of the server the proxy connects to, which is the resolved address of the host name in the request. Same format as `src-address`.</ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, ports: multi { ports: range [ .. 65535]
 }
 }">Port of the server, for HTTPS requests the port of the `CONNECT` tunnel. A port, a range or a comma-separated list, for example `dst-port=!443`.</ArgTableRow>
<ArgTableRow arg="local-port" typ="super { !
, port: num [0 .. 65535]
 }">Port of the proxy the request arrived on. Use it when `port` in [`/ip/proxy`](../) lists several ports.</ArgTableRow>
<ArgTableRow arg="dst-host" typ="super { !
, host: string
 }">
Host name of the request, for HTTPS requests the host of the `CONNECT` tunnel. The value must match the whole name and is not case-sensitive, so `example.com` does not match `www.example.com`.
- Wildcards: `*` matches any characters and `?` one character, for example `*.example.com`.
- A value that starts with `:` is a regular expression, which can match any part of the name: `:mail` matches `mail.example.com`. Anchor it with `^` and `$`, for example `:^www`.
</ArgTableRow>
<ArgTableRow arg="path" typ="super { !
, path: string
 }">
Path of the requested URL, including the query string, for example `/music/a.mp3?x=1`. Wildcards and regular expressions work as in `dst-host`.
- Wildcards must match the whole path including the query string, so `*.mp3` matches `/music/a.mp3` but not `/music/a.mp3?x=1`.
- The path always starts with `/`, so the router refuses a value such as `music/*`, which could never match.
- HTTPS requests have no path, so a rule with `path` never matches them.
</ArgTableRow>
<ArgTableRow arg="method" typ="super { !
, method: enum (GET | HEAD | POST | PUT | CONNECT | OPTIONS | DELETE | TRACE)
 }">HTTP method of the request: `GET`, `HEAD`, `POST`, `PUT`, `CONNECT`, `OPTIONS`, `DELETE` or `TRACE`. Clients of the proxy request HTTPS pages with `CONNECT`. The methods are defined in [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110#name-methods).</ArgTableRow>
<ArgTableRow arg="action" typ="enum (allow | deny | redirect | url-append)">
What the proxy does with a matching request.
- `allow` (default) - Pass the request on.
- `deny` - Answer with an HTTP 403 error page.
- `redirect` - Answer with HTTP 307 and the URL in `action-data` as the new location.
- `url-append` - Add the text in `action-data` to the end of the requested URL, after the path and query string, and pass the request on.
</ArgTableRow>
<ArgTableRow arg="action-data" typ="string">redirect URL/append URL. With `action=redirect`, the URL the client is sent to, for example `http://intranet.example.com/blocked.html`. With `action=url-append`, the text added to the end of the requested URL, as it is, without a separator.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="hits" typ="num">Number of requests the rule matched. Reset it with [`reset-counters`](reset-counters) or [`reset-counters-all`](reset-counters-all).</ArgTableRow>
</ArgTable>
