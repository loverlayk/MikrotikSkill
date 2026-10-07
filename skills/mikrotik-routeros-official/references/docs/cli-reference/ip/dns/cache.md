# cache

> Answers the router can give from its cache: upstream answers and the static entries. For a complete list, including the PTR records made for static entries, see all. For an overview, see DNS.

-----------

## ip/dns/cache 
**Type:** Directory

Answers the router can give from its cache: upstream answers and the static entries. For a complete list, including the PTR records made for static entries, see [`all`](all). For an overview, see [DNS](../../../../network-management/dns).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="S" typ="static">The record comes from a static entry in [`/ip/dns/static`](../static). Static records show a TTL of 0s here.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (A | NS | CNAME | MX | TXT | AAAA | SRV) { A:1, NS:2, CNAME:5, MX:15, TXT:16, AAAA:28, SRV:33 }">Record type.</ArgTableRow>
<ArgTableRow arg="data" typ="alt { address: ipAddr
, name: string
, info: composite { rmail: string
, email: string
 }
, mx: composite { preference: num
, exchange: string
 }
, srv: composite { port: num
, target: string
 }
, soa-mname: string
, address6: ip6Addr
 }">Data of the record, for example the address of an `A` record.</ArgTableRow>
<ArgTableRow arg="name" typ="string">Domain name of the record.</ArgTableRow>
<ArgTableRow arg="ttl" typ="time">Remaining time before the record expires from the cache. It counts down, and it is never longer than `cache-max-ttl` in [`/ip/dns`](../).</ArgTableRow>
</ArgTable>
