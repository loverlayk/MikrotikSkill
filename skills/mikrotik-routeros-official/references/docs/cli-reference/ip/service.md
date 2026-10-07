# service

> The management and service listeners of the router: WinBox, SSH, Telnet, FTP, the web server (www for HTTP, www-ssl for HTTPS), the API (api, api-ssl) and the reverse proxy. Each entry sets the port, the addresses...

-----------

## ip/service 
**Type:** Directory

The management and service listeners of the router: WinBox, SSH, Telnet, FTP, the web server (`www` for HTTP, `www-ssl` for HTTPS), the API (`api`, `api-ssl`) and the reverse proxy. Each entry sets the port, the addresses and VRF a service accepts clients from, and the certificate of the TLS services. You cannot add services, only change and disable the existing ones. The list also shows dynamic entries: ports other features and containers listen on, and established connections to the services. For the web server parts (WebFig, REST API, graphs), see [`/ip/service/webserver`](webserver). For an overview and the list of ports RouterOS uses, see [Services](../../../system-information-and-utilities/services).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">Dynamic entry created by RouterOS: a port that another feature or a container listens on (for example `btest`, `discover`, `resolver`, `dhcp`, `upnp`), or, together with the `c` flag, an established connection to a service.</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">The service is disabled and does not listen on its port.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The service cannot run with its settings, for example because another service already uses the port. The reason is shown as a comment, such as `cannot bind to port 80: Address in use (12)`.</ArgTableRow>
<ArgTableRow arg="c" typ="connection">The entry is an established connection to a service. `local` and `remote` show the addresses of the connection.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="port" typ="num">TCP port the service listens on, `1..65535`. When another service already listens on the port, the entry becomes invalid (`I`). The default depends on the service: `ftp` 21, `ssh` 22, `telnet` 23, `www` 80, `www-ssl` 443, `winbox` 8291, `api` 8728, `api-ssl` 8729, `reverse-proxy` 443.</ArgTableRow>
<ArgTableRow arg="address" typ="object { address: alt { address: ipPrefix
, address: ip6Prefix
 }
 }" deprecated="1">Deprecated name of `available-from`. A value set with `address` is written to `available-from`.</ArgTableRow>
<ArgTableRow arg="available-from" typ="object { address: alt { address: ipPrefix
, address: ip6Prefix
 }
 }">IPv4 and IPv6 prefixes of the clients allowed to use the service. A client from another address can still open the TCP connection, and the router then closes it without serving the client, so the port stays visible. To hide a service from untrusted networks, drop the traffic in the firewall input chain as well. Empty means any address. Default: empty.</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none) { none:0 }">Certificate the service presents to TLS clients. Applies to `www-ssl`, `api-ssl` and `reverse-proxy`. With `none`, `www-ssl` and `api-ssl` accept only anonymous Diffie-Hellman ciphers: the connection is encrypted, but the router does not prove its identity, and browsers and tools such as cURL cannot connect. Set a certificate for HTTPS. For `reverse-proxy`, the certificate is used by the rules that have none of their own (see [`/ip/reverse-proxy`](../reverse-proxy)). Default: none.</ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2) { any:0, only-1.2:2 }">
TLS versions the service accepts. Applies to the TLS services.
- `any` (default) - TLS 1.0, 1.1 and 1.2.
- `only-1.2` - Only TLS 1.2.
</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">VRF the service listens in. Default: main.</ArgTableRow>
<ArgTableRow arg="max-sessions" typ="num">Maximum number of simultaneous sessions of the service, `1..1000`. Default: 20.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="container" typ="enum () { :0 }">Name of the container that listens on the port, for dynamic entries created by containers.</ArgTableRow>
<ArgTableRow arg="netns" typ="num">Network namespace number of the container that listens on the port, for dynamic entries created by containers.</ArgTableRow>
<ArgTableRow arg="name" typ="string">Name of the service. For dynamic entries, the feature or program that listens on the port or holds the connection.</ArgTableRow>
<ArgTableRow arg="proto" typ="enum ()">Transport protocol of the port: `tcp` or `udp`.</ArgTableRow>
<ArgTableRow arg="local" typ="ip6Addr">Router address of an established connection (entries with the `c` flag).</ArgTableRow>
<ArgTableRow arg="remote" typ="composite { ip: ip6Addr
, port: num
 }">Client address and port of an established connection (entries with the `c` flag).</ArgTableRow>
</ArgTable>
