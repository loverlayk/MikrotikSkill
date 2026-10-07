# settings

> This menu allows you to configure various IPv6-related kernel and system-wide network parameters. These settings control how the operating system handles IP traffic and network communications.

-----------

## ipv6/settings 
**Type:** Settings Directory

This menu allows you to configure various IPv6-related kernel and system-wide network parameters. These settings control how the operating system handles IP traffic and network communications.

:::note
Changing IPv6 settings does not dynamically remove an existing SLAAC configuration, a router reboot is required.

:::

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="disable-ipv6" typ="bool">Disable or enable IPv6 system-wide. When disabled, prevents link-local address generation.</ArgTableRow>
<ArgTableRow arg="forward" typ="bool">Enable or disable packet forwarding between interfaces.</ArgTableRow>
<ArgTableRow arg="multipath-hash-policy" typ="enum (l3 | l4 | l3-inner) { l3:0, l4:1, l3-inner:2 }">
Specify the IPv6 hash policy for [ECMP](../../user-guides/routing-and-networking-protocols/routing-decision.md#multipath-ecmp-routes) routing:
- l3 - Layer-3 hashing of source IP, destination IP, flow label, and IP protocol.
- l3-inner - Layer-3 hashing or inner layer-3 hashing if available.
- l4 - Layer-4 hashing of source IP, destination IP, IP protocol, source port, and destination port.
</ArgTableRow>
<ArgTableRow arg="accept-redirects" typ="bool">Accept or reject ICMP redirect messages. Enable on hosts and disable on routers.</ArgTableRow>
<ArgTableRow arg="accept-router-advertisements" typ="enum (no | yes-if-forwarding-disabled | yes) { no:0, yes-if-forwarding-disabled:1, yes:2 }">Control acceptance of router advertisement (RA) messages. When enabled, the router obtains addresses using [stateless address configuration](../../system-information-and-utilities/neighbor-discovery.md).</ArgTableRow>
<ArgTableRow arg="accept-router-advertisements-on" typ="enum">Specify which interfaces to listen for incoming router advertisements (RAs).</ArgTableRow>
<ArgTableRow arg="disable-link-local-address" typ="bool">Disable automatic link-local address generation for non-VPN interfaces. Use this when you need manually configured link-local addresses.</ArgTableRow>
<ArgTableRow arg="stale-neighbor-detect-interval" typ="num">Set the interval at which the system checks stale IPv6 neighbor entries and probes them to verify reachability.</ArgTableRow>
<ArgTableRow arg="stale-neighbor-timeout" typ="num">Timeout duration after which stale IPv6 neighbor entries are purged.</ArgTableRow>
<ArgTableRow arg="min-neighbor-entries" typ="num">Set the minimum number of IPv6 neighbor entries for which the device must allocate memory.</ArgTableRow>
<ArgTableRow arg="soft-max-neighbor-entries" typ="num">Set the expected maximum number of IPv6 neighbor entries the system should handle.</ArgTableRow>
<ArgTableRow arg="max-neighbor-entries" typ="num">
Set the maximum number of IPv6 neighbor entries. As of RouterOS version 7.1, the default value depends on installed RAM:
- 1024 for 64 MiB
- 2048 for 128 MiB
- 4096 for 256 MiB
- 8192 for 512 MiB
- 16384 for 1024 MiB or higher

Setting a value higher than the default increases the risk of out-of-memory conditions.
</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">Enable [Fast Path](../../firewall-and-quality-of-service/packet-flow-in-routeros#fast-path) for IPv6 traffic.</ArgTableRow>
</ArgTable>
Fasttrack and fastpath values are cumulative since the feature was last enabled or since the system restarted.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="ipv6-fast-path-active" typ="bool">Indicates whether the IPv6 fast path feature is currently active.</ArgTableRow>
<ArgTableRow arg="ipv6-fast-path-packets" typ="num">Total number of packets that have been processed through the IPv6 fast path.</ArgTableRow>
<ArgTableRow arg="ipv6-fast-path-bytes" typ="num">Total number of bytes that have been processed through the IPv6 fast path.</ArgTableRow>
<ArgTableRow arg="ipv6-fasttrack-active" typ="bool">Indicates whether the IPv6 fasttrack feature is currently active.</ArgTableRow>
<ArgTableRow arg="ipv6-fasttrack-packets" typ="num">Total number of packets that have been processed through IPv6 fasttrack.</ArgTableRow>
<ArgTableRow arg="ipv6-fasttrack-bytes" typ="num">Total number of bytes that have been processed through IPv6 fasttrack.</ArgTableRow>
</ArgTable>
