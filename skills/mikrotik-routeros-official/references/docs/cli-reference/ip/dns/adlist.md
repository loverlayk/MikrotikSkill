# adlist

> Ad-blocking lists. The router answers A and AAAA queries for the names in these lists with 0.0.0.0 and :: (TTL 2 s) instead of asking upstream; other query types, such as MX or HTTPS, go upstream. Only the exact name...

-----------

## ip/dns/adlist 
**Type:** Directory

Ad-blocking lists. The router answers A and AAAA queries for the names in these lists with `0.0.0.0` and `::` (TTL 2 s) instead of asking upstream; other query types, such as MX or HTTPS, go upstream. Only the exact name is blocked, not its subdomains. The names are kept in the DNS cache memory and count against `cache-size` in [`/ip/dns`](../): each name takes about 75 bytes, so 76 500 names use about 5.6 MiB. When the cache is too small, the import stops with the log messages `adlist read: max cache size reached` and `could not add name, stopping import`, and `name-count` shows how many names were imported; raising `cache-size` afterwards does not complete the list, so remove the adlist and add it again. Disabling an adlist does not free the cache memory its names use: they still count against `cache-size` until the list is removed. The router re-checks the lists every 4 hours. Up to 64 adlists can be added. A static `FWD` entry exempts a name from all adlists; a static A entry alone does not. For examples, see [DNS](../../../../network-management/dns).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The adlist is disabled and blocks nothing.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file" typ="file">
File on the router with the names to block, as `/file/print` shows it. One name per line, in lower case, in one of these formats:
- `0.0.0.0 name`, `127.0.0.1 name` or `::1 name` - Hosts file format.
- `name` - Just the name.

Lines starting with `#` and comments after a name are ignored. Wildcards such as `*.example.com` and several names on one line are not supported.
</ArgTableRow>
<ArgTableRow arg="url" typ="string">URL of a list in the same format as `file`, for example a public hosts file. The router downloads it and keeps a copy on its storage (not shown in `/file`).</ArgTableRow>
<ArgTableRow arg="ssl-verify" typ="bool">Whether the router verifies the certificate of the `url` server against the built-in trust store and the certificates in `/certificate`. When the check fails, the router does not import the list and logs `http client error: SSL: ...` in the `dns` topic. For a server with a self-signed certificate, import its CA certificate or set `ssl-verify=no`. Default: yes.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="match-count" typ="num">Number of queries answered from this list.</ArgTableRow>
<ArgTableRow arg="name-count" typ="num">Number of names imported from this list.</ArgTableRow>
</ArgTable>
