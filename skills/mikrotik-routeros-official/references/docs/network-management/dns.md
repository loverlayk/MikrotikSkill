# DNS

> The RouterOS DNS resolver: use the router as the DNS server for your network, check and troubleshoot it, add local names, send domains to other servers, use domain names in the firewall, block ads with adlists, use...

# DNS

RouterOS has a caching DNS resolver. The router uses it for its own lookups, and it can be the DNS server for the devices in your network: it asks upstream DNS servers, for example those of your ISP, and keeps their answers in its cache.

With the default configuration, this already works, and you do not need to change anything. The following sections cover the setup, how to check it, and extra tasks such as local names and ad blocking. The extras apply only to devices that use the router as their DNS server: devices that get other DNS servers from DHCP, for example 1.1.1.1, bypass the router's static entries and adlists.

## Use the router as the DNS server for your network

The default configuration already does this. To set it up yourself:

1. Allow the router to answer the devices in your network:

   ```ros
   /ip/dns/set allow-remote-requests=yes
   ```

2. Give the router's address to your DHCP clients as their DNS server: set `dns-server` in `/ip/dhcp-server/network`, for example to 192.168.88.1 (see [DHCP server](./dhcp/server)).

The router gets its upstream servers from other services, for example from the ISP through the DHCP client on the WAN port. They show up as `dynamic-servers` in `/ip/dns/print`. To use other upstream servers, set them in `servers`. The router tries them before the dynamic ones:

```ros
/ip/dns/set servers=1.1.1.1,9.9.9.9
```

With `allow-remote-requests=yes`, the router answers DNS queries on UDP and TCP port 53 on all its addresses. The default firewall drops these queries when they come from the internet. If you use your own firewall rules, drop them as well, so your router is not an open resolver that anyone on the internet can use:

```ros
/ip/firewall/filter/add chain=input in-interface-list=WAN protocol=udp dst-port=53 action=drop comment="drop DNS from WAN"
/ip/firewall/filter/add chain=input in-interface-list=WAN protocol=tcp dst-port=53 action=drop comment="drop DNS from WAN"
```

## Check and troubleshoot

To test a name on the router itself:

```ros
:put [:resolve mikrotik.com]
```

To test the router as the DNS server from a computer in your network, ask it directly, for example with `nslookup mikrotik.com 192.168.88.1`.

The answer of a DNS server has a status:

- `NOERROR`: the name exists. The answer can still contain no records, when the name has none of the requested type.
- `NXDOMAIN`: the name does not exist.
- `SERVFAIL`: the router could not get an answer, for example because no upstream server answered in time.

The router keeps answers in its cache for their time to live (TTL). To see the cached answers, or to empty the cache after a change:

```ros
/ip/dns/cache/print
/ip/dns/cache/flush
```

The router logs DNS errors, for example about the DoH server or an adlist import, in the `dns` topic:

```ros
/log/print where topics~"dns"
```

If devices get no answer at all, check `allow-remote-requests` and your firewall rules. If a name resolves to `0.0.0.0`, an adlist blocks it, on the router or on the upstream server.

## Local names

Static entries answer names from the router itself, for example for the devices in your network:

```ros
[admin@MikroTik] > /ip/dns/static/add name=nas.lan address=192.168.88.20
[admin@MikroTik] > /ip/dns/static/add name=printer.lan address=192.168.88.21
[admin@MikroTik] > /ip/dns/static/add name=example.lan address=192.168.88.30 match-subdomain=yes
[admin@MikroTik] > /ip/dns/static/print
Columns: NAME, TYPE, ADDRESS, TTL
# NAME         TYPE  ADDRESS        TTL
0 nas.lan      A     192.168.88.20  1d
1 printer.lan  A     192.168.88.21  1d
2 example.lan  A     192.168.88.30  1d
```

- An IPv6 address makes an AAAA entry.
- The router also answers reverse lookups (PTR) for these addresses.
- With `match-subdomain=yes`, an entry answers for the name and for every name below it, for example `www.example.lan`.

The DHCP server and IP neighbor discovery add static entries by themselves, flagged `D` (dynamic), when their `add-dns-entries` setting is on. See [DHCP server](./dhcp/server) and [`/ip/neighbor/discovery-settings`](../cli-reference/ip/neighbor/discovery-settings).

## Send a domain to another DNS server

A `FWD` entry sends the queries for a name to another DNS server instead of the normal upstream servers, for example the names of a company network to the company's DNS server:

```ros
/ip/dns/static/add name=corp.example.com type=FWD forward-to=10.0.0.53 match-subdomain=yes
```

`forward-to` takes an IP address, a DNS name or the name of a forwarder. Without `forward-to`, a `FWD` entry sends the queries to the normal upstream servers.

A forwarder is a named group of DNS and DoH servers for `FWD` entries. The router sends each query to the next server of the group in turn:

```ros
/ip/dns/forwarders/add name=branch dns-servers=10.1.0.53,10.1.1.53
/ip/dns/static/add name=branch.example.com type=FWD forward-to=branch match-subdomain=yes
```

The router does not skip a server of a forwarder that stops answering: the queries that reach it fail. Add only servers that work.

## Use domain names in firewall rules

With `address-list`, the router adds the addresses it answers for an entry to a firewall address list. With a `FWD` entry, these are the addresses in the upstream answer:

```ros
/ip/dns/static/add name=example.com type=FWD address-list=example-com match-subdomain=yes
```

After a device in your network looks up `example.com` through the router, the list holds the addresses of the answer:

```ros
[admin@MikroTik] > /ip/firewall/address-list/print where list=example-com
Flags: D - DYNAMIC
Columns: LIST, ADDRESS, CREATION-TIME
#   LIST         ADDRESS        CREATION-TIME
;;; created for example.com.
0 D example-com  198.51.100.10  2026-09-24 12:32:52
;;; created for example.com.
1 D example-com  198.51.100.11  2026-09-24 12:32:52
```

Use the list in firewall rules, or in mangle rules to route the traffic of a domain differently (see [Policy routing](../user-guides/routing-and-networking-protocols/policy-routing)). The router removes an entry when the TTL of the answer has passed, plus `address-list-extra-time` from `/ip/dns`. Only the queries of devices add entries. The router's own lookups, for example with `:resolve`, do not.

## Block ads with adlists

An adlist is a list of domain names, for example of ad and tracking servers, that the router blocks. It answers A queries for these names with `0.0.0.0` and AAAA queries with `::`, so the devices cannot reach them.

The router keeps adlists in the DNS cache, so raise `cache-size` before you add a list. A list of about 75 000 names needs about 6 MiB; the example leaves room for the normal cache as well:

```ros
[admin@MikroTik] > /ip/dns/set cache-size=16384
[admin@MikroTik] > /ip/dns/adlist/add url=https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts
[admin@MikroTik] > /ip/dns/adlist/print
0  url="https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"
   match-count=0 name-count=76524
```

`name-count` shows how many names the router imported, and `match-count` how many queries the list blocked.

When the cache is too small, the router stops the import and logs `adlist read: max cache size reached`. Raising `cache-size` afterwards does not complete the list. Remove the adlist and add it again.

An adlist can also be a file on the router, with one name per line, in hosts file format or as plain names:

```ros
/file/add name=adlist.txt contents="0.0.0.0 ads.example.net\ntracker.example.net\n"
/ip/dns/adlist/add file=adlist.txt
```

To stop blocking a name, add a `FWD` entry for it. The router then sends its queries to the upstream servers:

```ros
/ip/dns/static/add name=ads.example.net type=FWD
```

To stop all adlists for a while, for example for 10 minutes:

```ros
/ip/dns/adlist/pause duration=10m
```

[Video: Adlist setup](https://youtube.com/watch?v=RMJnjyAOfLI)

## DNS over HTTPS

With DNS over HTTPS (DoH), the router sends its upstream queries encrypted, over HTTPS, to one DoH server:

```ros
/ip/dns/set use-doh-server=https://cloudflare-dns.com/dns-query verify-doh-cert=yes
```

Keep `servers` or `dynamic-servers`, or add a static entry for the DoH server's host name: the router looks up that name through its normal DNS servers. With `verify-doh-cert=yes`, the router checks the server's certificate against the built-in trust store and the certificates in `/certificate` (see [Certificates](../authentication-authorization-accounting/certificates#built-in-trust-store-authorities)).

Some DoH services need HTTP/2, which only ARM64 and x86 devices, including CHR, support:

- Cloudflare, Control D, Google, NextDNS and OpenDNS work on all devices.
- Mullvad, Quad9 and UncensoredDNS work only on ARM64 and x86 devices.

While a DoH server is set, the router sends all upstream queries to it and does not fall back to the normal DNS servers. When the DoH server cannot be reached, devices get `SERVFAIL`. `FWD` entries keep using their own servers.

[Video: DoH setup](https://youtube.com/watch?v=w4erB0VzyIE)

## More record types and regular expressions

Static entries can also hold other record types:

- `CNAME` gives a name an alias. The router answers it together with the address of the target, which can come from a static entry or from upstream: `/ip/dns/static/add name=files.lan type=CNAME cname=nas.lan`.
- `NXDOMAIN` makes a name not exist, for all record types: `/ip/dns/static/add name=tracker.example.com type=NXDOMAIN`.
- `MX` names the mail server of a domain: `/ip/dns/static/add name=lan type=MX mx-exchange=mail.lan mx-preference=10`.
- `TXT` holds text: `/ip/dns/static/add name=lan type=TXT text="managed by RouterOS"`.

To match many names with one entry, use a regular expression instead of `name`:

```ros
/ip/dns/static/add regexp="^host[0-9]+\\.lan\$" address=192.168.88.40
```

The router matches the expression against the name in lower case, so write it in lower case. On the command line, a backslash is written as `\\` and `$` as `\$`: the entry above is stored as `^host[0-9]+\.lan$`.

Create only one entry for each name and record type. When several entries match the same name, for example an entry with `match-subdomain=yes` and an entry for a name below it, the order of the list does not decide which of them answers.

## mDNS repeater

Multicast DNS (mDNS) lets devices find each other in a local network, for example printers (AirPrint), media players (AirPlay, Chromecast) and smart home devices. mDNS stays in one network. The mDNS repeater passes it on between the interfaces you list, so devices in different networks or VLANs can find each other:

```ros
/ip/dns/set mdns-repeat-ifaces=bridge,vlan20
```

Use interfaces that carry multicast, such as Ethernet, VLAN, bridge or EoIP interfaces. Repeating adds multicast traffic to every listed network.

The router receives the mDNS packets itself, so they pass the input chain of the firewall. The default firewall accepts them on the interfaces in the `LAN` interface list. If your input rules drop UDP port 5353 on a listed interface, for example a VLAN that is not in `LAN`, add this rule before the rules that drop traffic:

```ros
/ip/firewall/filter/add chain=input protocol=udp dst-port=5353 action=accept comment="accept mDNS"
```

## Technical details

### How the router answers a query

What the router answers depends on the entries that exist for the name:

| Entries for the name | Answer |
| :-- | :-- |
| None | From the cache or the upstream servers. |
| Static entry, for example A | From the entry, for its record type. Other record types come from upstream; when upstream has none, the router answers `NOERROR` without records. |
| Name on an adlist | `0.0.0.0` for A and `::` for AAAA, also when a static A or AAAA entry exists. Other record types come from upstream. |
| `FWD` entry | From the `forward-to` server, or from the upstream servers. The adlists do not apply. |
| `FWD` and A entries | From the A entry. |
| `NXDOMAIN` entry | `NXDOMAIN` for all record types. |

Names are matched in lower case. The cache answers with the remaining TTL.

### Upstream servers

- The router tries the static `servers` first, in order, then the `dynamic-servers`, for example those of the DHCP client with `use-peer-dns=yes`.
- The router waits `query-server-timeout` for an answer before it tries the next server. When a server answers, the router keeps using it for later queries.
- When no server answers within `query-total-timeout`, the device gets `SERVFAIL`.
- When `max-concurrent-queries` queries are waiting for upstream answers, the router drops new queries, also those it could answer from the cache, until one of the waiting queries finishes.
- A change in `/ip/dns` takes effect at once. A query that arrives at that moment can stay unanswered, and the device sends it again. The cache is kept.

### Cache

- `cache-max-ttl` limits the TTL of upstream answers. Static entries use their own `ttl`, 1 day by default.
- Adlists count against `cache-size`: each name needs about 75 bytes.
- `/ip/dns/cache` lists the answers the router gives. `/ip/dns/cache/all` also lists the other records it holds, such as the PTR records for static entries. Regular expression entries have no PTR records.

### Adlists

- Each line holds one name, alone or after an address (`0.0.0.0`, `127.0.0.1` or `::1`) as in a hosts file. Lines and line ends starting with `#` are comments. Names must be in lower case, and wildcards such as `*.example.com` are not supported.
- Only the listed name is blocked, not the names below it. Blocked answers have a TTL of 2 seconds.
- Disabling an adlist does not free the cache memory its names use; they still count against `cache-size`. Only removing the list releases it.
- The router verifies the certificate of an HTTPS adlist URL (`ssl-verify=yes`). For a server with a self-signed certificate, import its CA certificate into `/certificate`, or set `ssl-verify=no`.
- The router checks all lists for changes every 4 hours; `/ip/dns/adlist/reload` checks them at once. The router stores the lists on its disk.
- A router can have up to 64 adlists.

### DNS over HTTPS

- The router keeps one HTTPS connection (TCP port 443) to the DoH server and sends all queries through it.
- On ARM64 and x86 devices, the router uses HTTP/2 when the server supports it. Other devices use HTTP/1.1.
- DoH errors are logged in the `dns` topic, for example `DoH server connection error: timeout connecting`.

### Forwarders

- The servers of a forwarder take turns, one query each, across `dns-servers` and `doh-servers`. A query that goes to a server that does not answer fails after `query-total-timeout`.
- For a forwarder, `verify-doh-cert` is on by default, unlike in `/ip/dns`.

### VRF

- The resolver answers devices in the VRF set in `vrf`, `main` by default. Devices in other VRFs get no answer.
- Upstream servers are reached through the main routing table. To reach a server in another VRF, write it as `address@vrf`, for example `servers=10.0.0.1@vrf1`.

### mDNS repeater

- The router repeats IPv4 mDNS (UDP port 5353 to 224.0.0.251), and sends the packets from its own address on the other interfaces. IPv6 mDNS (ff02::fb) is not repeated.
- Layer 3 tunnels such as WireGuard carry no multicast, so mDNS cannot be repeated over them.

For all properties, see [`/ip/dns`](../cli-reference/ip/dns/), [`/ip/dns/static`](../cli-reference/ip/dns/static), [`/ip/dns/adlist`](../cli-reference/ip/dns/adlist/) and [`/ip/dns/forwarders`](../cli-reference/ip/dns/forwarders) in the CLI reference.
