# settings

> This menu allows you to configure various IPv4 and IPv6-related kernel and system-wide network parameters. These settings control how the operating system handles IP traffic and network communications.

-----------

## ip/settings 
**Type:** Settings Directory

This menu allows you to configure various IPv4 and IPv6-related kernel and system-wide network parameters. These settings control how the operating system handles IP traffic and network communications.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ip-forward" typ="bool">Enable or disable packet forwarding between interfaces. Resets all configuration parameters to defaults according to [RFC 1812](https://tools.ietf.org/html/rfc1812) for routers.</ArgTableRow>
<ArgTableRow arg="send-redirects" typ="bool">Send ICMP redirects. Enable this on routers.</ArgTableRow>
<ArgTableRow arg="accept-source-route" typ="bool">Accept packets with the SRR option. Accepting source-routed (SSRR/LSRR) packets is a well-known spoofing/security risk and should be kept disabled unless required by the setup.</ArgTableRow>
<ArgTableRow arg="accept-redirects" typ="bool">Accept ICMP redirect messages. Enable on hosts and disable on routers.</ArgTableRow>
<ArgTableRow arg="secure-redirects" typ="bool">Accept ICMP redirect messages only for gateways listed in the default gateway list.</ArgTableRow>
<ArgTableRow arg="rp-filter" typ="enum (no | strict | loose) { no:0, strict:1, loose:2 }">
Enable or disable source validation.
- `no` - Do not validate source addresses.
- `strict` - Strict mode as defined in [RFC 3704](https://tools.ietf.org/html/rfc3704) Strict Reverse Path. Each incoming packet is tested against the FIB and if the interface is not the best reverse path, the packet check will fail. By default, failed packets are discarded.
- `loose` - Loose mode as defined in [RFC 3704](https://tools.ietf.org/html/rfc3704) Loose Reverse Path. Each incoming packet's source address is tested against the FIB and if the source address is not reachable through any interface, the packet check will fail.

[RFC 3704](https://tools.ietf.org/html/rfc3704) recommends enabling `strict` mode to prevent IP spoofing from DDoS attacks.

If you use asymmetric routing, complex routing, or VRRP, then `strict` mode will cause problems, enable `loose` mode instead.
</ArgTableRow>
<ArgTableRow arg="ipv4-multipath-hash-policy" typ="enum (l3 | l4 | l3-inner) { l3:0, l4:1, l3-inner:2 }">
IPv4 hash policy used for [ECMP](../../user-guides/routing-and-networking-protocols/routing-decision.md#multipath-ecmp-routes) routing.

- l3 - Layer-3 hashing of source and destination IP addresses.
- l3-inner - Layer-3 hashing, or inner layer-3 hashing if available.
- l4 - Layer-4 hashing of source and destination IP addresses, IP protocol, source port, and destination port.
</ArgTableRow>
<ArgTableRow arg="tcp-syncookies" typ="bool">Send syncookies when the SYN backlog queue of a socket overflows. This helps prevent SYN flood attacks. However, syncookies violate the TCP protocol and prevent the use of TCP extensions, which can degrade some services (for example, SMTP relaying). This degradation may be visible to your clients and relays contacting you.</ArgTableRow>
<ArgTableRow arg="tcp-timestamps" typ="enum (disabled | random-offset | enabled) { disabled:0, random-offset:1, enabled:2 }">Enable or disable TCP timestamps, or add a random offset to TCP timestamps (default behavior). Disabling timestamps can help reduce performance drop spikes.</ArgTableRow>
<ArgTableRow arg="max-neighbor-entries" typ="num">
Sets Linux `gc_thresh3`. A maximum number of allowed neighbors in the ARP table. Default value depends on the installed amount of RAM. It is possible to set a higher value than the default, but it increases the risk of out-of-memory condition.
The default values for certain RAM sizes:

- 2048 for 64 MiB,
- 4096 for 128 MiB,
- 8192 for 256 MiB,
- 16384 for 512 MiB or higher.

The ARP cache stores ARP entries, and if some of these entries are incomplete, they can stay in the cache for an indefinite period of time. This will only happen if the number of entries in the cache is less than one-fourth of the maximum number allowed. The reason for this is to prevent the unnecessary running of the garbage-collector when the ARP table is not close to being full.
</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="time">Sets Linux `base_reachable_time` (`base_reachable_time_ms`) on all interfaces that use ARP. The initial validity of the ARP entry is picked from the interval [`timeout/2 - 3*timeout/2`] (default from 15s to 45s) after the neighbor was found. Can use postfix ms, s, m, h, d for milliseconds, seconds, minutes, hours, or days. If no postfix is set then seconds (s) are used. The parameter means how long a valid ARP record will be considered complete if no one communicates with the specific MAC/IP during this time. The parameter does not represent a time when an ARP entry is removed from the ARP cache (see `max-neighbor-entries` setting).</ArgTableRow>
<ArgTableRow arg="icmp-rate-limit" typ="num">Limit the maximum rates for sending ICMP packets whose type matches icmp-rate-mask to specific targets. Value of `0` disables any limiting, other values indicate the minimum space between responses in milliseconds.</ArgTableRow>
<ArgTableRow arg="icmp-rate-mask" typ="num">Mask of ICMP types for which rates are limited. For more information, see the [Linux man pages](http://man7.org/linux/man-pages/man7/icmp.7.html).</ArgTableRow>
<ArgTableRow arg="icmp-errors-use-inbound-interface-address" typ="bool">When enabled, send ICMP error message replies with a source address equal to the primary address of the receiving interface that caused the error. Use this for complex network debugging.</ArgTableRow>
<ArgTableRow arg="ipv4-high-fragment-thresh" typ="num">
Sets the upper bound of memory (in bytes) the kernel may consume for all fragment reassembly queues combined (every interface and every flow). When the total memory used by the cache reaches this limit the kernel starts dropping newly arriving fragments, causing packets to be discarded. Raising the limit reduces the chance of drops under heavy fragmentation (e.g. high-throughput links with VPNs, or MTU-limited paths), but it also raises the maximum amount of RAM that can be used.

The default value depends on the installed amount of RAM:

- 512 KiB for 64 MiB of RAM,
- 1024 KiB for 128 MiB of RAM,
- 2048 KiB for 256 MiB of RAM,
- 4096 KiB for 512MiB of RAM,
- 16 MiB for 1 GiB of RAM,
- 32 MiB for 2 GiB of RAM or higher.
</ArgTableRow>
<ArgTableRow arg="ipv4-fragment-time" typ="num">Time in seconds to keep an IPv4 fragment in memory.</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">Allows [Fast Path](../../firewall-and-quality-of-service/packet-flow-in-routeros#fast-path)</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="ipv4-fast-path-active" typ="bool">Indicates whether fast-path is active.</ArgTableRow>
<ArgTableRow arg="ipv4-fast-path-packets" typ="num">Amount of fast-pathed packets.</ArgTableRow>
<ArgTableRow arg="ipv4-fast-path-bytes" typ="num">Amount of fast-pathed bytes.</ArgTableRow>
<ArgTableRow arg="ipv4-fasttrack-active" typ="bool">Indicates whether fasttrack is active.</ArgTableRow>
<ArgTableRow arg="ipv4-fasttrack-packets" typ="num">Amount of fasttracked packets.</ArgTableRow>
<ArgTableRow arg="ipv4-fasttrack-bytes" typ="num">Amount of fasttracked bytes.</ArgTableRow>
</ArgTable>
