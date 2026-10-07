# forwarders

> Named groups of upstream servers for static FWD entries: set forward-to of an entry in /ip/dns/static to the forwarder name. Every query takes the next server in turn across dns-servers and doh-servers (round robin)....

-----------

## ip/dns/forwarders 
**Type:** Directory

Named groups of upstream servers for static `FWD` entries: set `forward-to` of an entry in [`/ip/dns/static`](static) to the forwarder name. Every query takes the next server in turn across `dns-servers` and `doh-servers` (round robin). A server that does not answer is not skipped: the queries it gets fail with SERVFAIL after `query-total-timeout`, so list only servers that work. For examples, see [DNS](../../../network-management/dns).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The forwarder is disabled.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the forwarder, used as `forward-to` in static `FWD` entries.</ArgTableRow>
<ArgTableRow arg="dns-servers" typ="multi { address (flags=46D)
 }">DNS servers of the forwarder, as IP addresses or DNS names, for example `dns-servers=1.1.1.1,8.8.8.8`.</ArgTableRow>
<ArgTableRow arg="doh-servers" typ="multi { string
 }">DoH server URLs of the forwarder, for example `doh-servers=https://dns.google/dns-query`. The router looks up their host names through `servers` in `/ip/dns`.</ArgTableRow>
<ArgTableRow arg="verify-doh-cert" typ="bool">Whether the router verifies the certificates of the DoH servers against `/certificate` and the built-in trust store. A server with an untrusted certificate fails with `SSL: ssl: no trusted CA certificate found (6)` in the log. This default differs from `verify-doh-cert` in `/ip/dns`. Default: yes.</ArgTableRow>
</ArgTable>
