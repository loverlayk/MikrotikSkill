# dns

> Settings of the DNS resolver and cache. The router uses them for its own lookups and, with allow-remote-requests=yes, answers DNS queries from clients. A change in this menu takes effect at once; a query that arrives...

-----------

## ip/dns 
**Type:** Settings Directory

Settings of the DNS resolver and cache. The router uses them for its own lookups and, with `allow-remote-requests=yes`, answers DNS queries from clients. A change in this menu takes effect at once; a query that arrives at that moment can stay unanswered, and the client sends it again. The cache is kept. For an overview and examples, see [DNS](../../../network-management/dns).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="servers" typ="multi { servers: address (flags=46v)
 }">Upstream DNS servers, IPv4 or IPv6 addresses, optionally with `@<vrf>` to reach a server in another VRF. The router tries these servers before `dynamic-servers`, in the listed order. It waits `query-server-timeout` for an answer and then tries the next server. When a server answers, the router keeps using it for later queries.</ArgTableRow>
<ArgTableRow arg="use-doh-server" typ="string">URL of a DNS over HTTPS (DoH) server, for example `https://cloudflare-dns.com/dns-query`. When it is set, the router sends every query over one reused HTTPS connection (TCP port 443) to this server, and `servers` and `dynamic-servers` are used only to look up the host name of the DoH server (A and AAAA over UDP port 53); a static entry for the host name also works. The router does not fall back to plain DNS: when the DoH server does not answer, clients get SERVFAIL after `query-total-timeout`, and the log shows `dns,error DoH server connection error: ...`, for example `Connection refused` or `timeout connecting`. Static `FWD` entries keep using their own servers over plain DNS. Only one DoH server can be set. ARM64 and x86 devices, including CHR, use HTTP/2; other architectures use HTTP/1.1, so DoH services that require HTTP/2, such as Quad9, work only on ARM64 and x86. Default: empty.</ArgTableRow>
<ArgTableRow arg="verify-doh-cert" typ="bool">Whether the router verifies the certificate of the DoH server against `/certificate` and the built-in trust store. Default: no.</ArgTableRow>
<ArgTableRow arg="doh-max-server-connections" typ="num">Maximum number of HTTPS connections to the DoH server. Default: 5.</ArgTableRow>
<ArgTableRow arg="doh-max-concurrent-queries" typ="num">Maximum number of DoH queries in progress at the same time. Default: 50.</ArgTableRow>
<ArgTableRow arg="doh-timeout" typ="time">How long the router waits for an answer from the DoH server. Default: 5s.</ArgTableRow>
<ArgTableRow arg="allow-remote-requests" typ="bool">Whether the router answers DNS queries from other devices, on UDP and TCP port 53 of its addresses. With `no`, only the router itself uses the resolver. The default firewall drops connections from the WAN side; allow port 53 only from your own networks, so the router does not answer queries from the internet. Default: no.</ArgTableRow>
<ArgTableRow arg="max-udp-packet-size" typ="num">Maximum size of a DNS message over UDP, in bytes. Default: 4096.</ArgTableRow>
<ArgTableRow arg="query-server-timeout" typ="time">How long the router waits for an answer from one upstream server before it tries the next one. Default: 2s.</ArgTableRow>
<ArgTableRow arg="query-total-timeout" typ="time">How long the router tries to resolve a query in total. When no server answers in this time, the client gets a SERVFAIL answer. Set it in relation to `query-server-timeout` and the number of servers. Default: 10s.</ArgTableRow>
<ArgTableRow arg="max-concurrent-queries" typ="num">Largest number of queries that can wait for an upstream answer at the same time. While the limit is reached, the router drops new queries, also those it could answer from the cache, until a waiting query finishes. Default: 100.</ArgTableRow>
<ArgTableRow arg="max-concurrent-tcp-sessions" typ="num">Maximum number of TCP connections from clients at the same time. Default: 20.</ArgTableRow>
<ArgTableRow arg="cache-size" typ="num">Size of the DNS cache, in KiB. Adlist entries are kept in the cache too. Default: 2048.</ArgTableRow>
<ArgTableRow arg="cache-max-ttl" typ="time">Longest time the router keeps an upstream answer in the cache. A longer TTL from the upstream server is shortened to this value, and clients get the remaining time. Static entries keep their own `ttl`. Default: 1w.</ArgTableRow>
<ArgTableRow arg="address-list-extra-time" typ="time">Time added to the TTL of an answer before the router removes a dynamic address-list entry that a static entry with `address-list` created. Default: 0s.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">VRF in which the resolver answers clients when `allow-remote-requests=yes`. Clients in other VRFs get no answer; the router's own lookups keep working. Upstream servers without a VRF suffix are reached through the main routing table; to reach a server in another VRF, write it as `address@vrf` in `servers`, for example `servers=10.0.0.1@vrf1,1.1.1.1`. Default: main.</ArgTableRow>
<ArgTableRow arg="mdns-repeat-ifaces" typ="multi { iface_enum
 }">Interfaces between which the router repeats multicast DNS (mDNS). The router receives IPv4 mDNS packets (UDP port 5353 to 224.0.0.251) on each listed interface and sends them again from its own address on the other listed interfaces, so devices in different networks can discover each other. IPv6 mDNS (ff02::fb) is not repeated. The router handles the packets itself, so they pass the input chain of the firewall: input rules must not drop UDP port 5353 on these interfaces (the default firewall accepts it on `LAN` interfaces). Use interfaces that carry multicast, such as Ethernet, VLAN, bridge or EoIP interfaces; layer 3 tunnels such as WireGuard carry no multicast. Default: empty (no repeating).</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="dynamic-servers" typ="multi { dynamic-servers: address (flags=46v)
 }">DNS servers learned from other services, for example from the DHCP client with `use-peer-dns=yes`. The router tries them after `servers`.</ArgTableRow>
<ArgTableRow arg="cache-used" typ="num">Part of `cache-size` in use, in KiB.</ArgTableRow>
</ArgTable>
