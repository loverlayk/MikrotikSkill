# neighbor

> List of all discovered nodes by the IPv6 Neighbor Discovery protocol, or nodes added manually by configuration.

-----------

## ipv6/neighbor 
**Type:** Directory

List of all discovered nodes by the IPv6 [Neighbor Discovery](https://tools.ietf.org/html/rfc4861) protocol, or nodes added manually by configuration.

The default maximum number of neighbor entries depends on installed RAM. Adjust it with `/ipv6/settings/set max-neighbor-entries=x`. See [IPv6 Settings](./settings.md) for details.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="R" typ="router">router</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="ip6Addr">IPv6 address of the neighbor.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">Interface name to which this neighbor is attached.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the device to add.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string">
Status of the cached entry:
- **noarp** - the neighbor entry is valid. RouterOS does not validate this entry, but it can be removed when its lifetime expires.
- **incomplete** - address resolution is in progress and the neighbor's link-layer address is not yet determined.
- **reachable** - the neighbor was reachable recently (within tens of seconds).
- **stale** - the neighbor is no longer known to be reachable. Will continue sending traffic to the neighbor before attempting reachability verification.
- **delay** - the neighbor is no longer known to be reachable, and traffic has recently been sent to the neighbor. RouterOS delays probes briefly to allow the upper-layer protocol to confirm reachability.
- **probe** - the neighbor is no longer known to be reachable and unicast Neighbor Solicitation probes are being sent to verify reachability.
- **failed** - RouterOS could not resolve the neighbor's MAC address using the Neighbor Discovery protocol.
</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">Indicates the VRF associated with this neighbor entry.</ArgTableRow>
</ArgTable>
