# all

> All records in the DNS cache, including the PTR records the router creates for static entries and records the resolver keeps internally. For an overview, see DNS.

-----------

## ip/dns/cache/all 
**Type:** Directory

All records in the DNS cache, including the PTR records the router creates for static entries and records the resolver keeps internally. For an overview, see [DNS](../../../../network-management/dns).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="S" typ="static">The record comes from a static entry in [`/ip/dns/static`](../static), for example the PTR record made for a static `A` or `AAAA` entry.</ArgTableRow>
<ArgTableRow arg="N" typ="negative">A cached negative answer: the name or the record type does not exist.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Domain name of the record.</ArgTableRow>
<ArgTableRow arg="type" typ="enum (A | NS | MD | MF | CNAME | SOA | MB | MG | MR | NULL | WKS | PTR | HINFO | MINFO | MX | TXT | AAAA | SRV) { A:1, NS:2, MD:3, MF:4, CNAME:5, SOA:6, MB:7, MG:8, MR:9, NULL:10, WKS:11, PTR:12, HINFO:13, MINFO:14, MX:15, TXT:16, AAAA:28, SRV:33 }">Record type.</ArgTableRow>
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
 }">Data of the record, for example the address of an `A` record or the target name of a `PTR` record.</ArgTableRow>
<ArgTableRow arg="ttl" typ="time">Remaining time before the record expires from the cache.</ArgTableRow>
<ArgTableRow arg="responsible" typ="string">Email address of the zone administrator, from an `SOA` record.</ArgTableRow>
<ArgTableRow arg="serial" typ="num">Serial number of the zone, from an `SOA` record.</ArgTableRow>
<ArgTableRow arg="refresh" typ="num">Refresh interval of the zone, in seconds, from an `SOA` record.</ArgTableRow>
<ArgTableRow arg="retry" typ="num">Retry interval of the zone, in seconds, from an `SOA` record.</ArgTableRow>
<ArgTableRow arg="expire" typ="num">Expire time of the zone, in seconds, from an `SOA` record.</ArgTableRow>
<ArgTableRow arg="minimum" typ="num">Minimum TTL of the zone, in seconds, from an `SOA` record.</ArgTableRow>
</ArgTable>
