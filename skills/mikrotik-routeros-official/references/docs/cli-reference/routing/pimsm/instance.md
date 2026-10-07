# instance

> The instance menu defines the main PIM-SM settings. The instance is then used for all other PIM-related configurations like interface-template, static RP, and Bootstrap Router.

-----------

## routing/pimsm/instance 
**Conditions:** !smips
**Type:** Directory

The instance menu defines the main PIM-SM settings. The instance is then used for all other PIM-related configurations like interface-template, static RP, and Bootstrap Router.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="vrf" typ="enum">Name of the VRF for control connections.</ArgTableRow>
<ArgTableRow arg="name" typ="string">Name of the instance.</ArgTableRow>
<ArgTableRow arg="afi" typ="enum (ip | ipv6)">Specifies address family for PIM.</ArgTableRow>
<ArgTableRow arg="switch-to-spt" typ="bool">Whether to switch to Shortest Path Tree (SPT) if multicast data bandwidth threshold is reached. The router will not proceed from protocol phase one (register encapsulation) to native multicast traffic flow if this option is disabled. It is recommended to enable this option.</ArgTableRow>
<ArgTableRow arg="switch-to-spt-interval" typ="time">Time interval in which to account for multicast data bandwidth, used in conjunction with `switch-to-spt-bytes` to determine if the switching threshold is reached.</ArgTableRow>
<ArgTableRow arg="switch-to-spt-bytes" typ="num">Multicast data bandwidth threshold. Switching to Shortest Path Tree (SPT) happens if this threshold is reached in the specified time interval. If a value of 0 is configured, switching will happen immediately.</ArgTableRow>
<ArgTableRow arg="crp-advertise-contained" typ="bool">Currently not implemented.</ArgTableRow>
<ArgTableRow arg="bsm-forward-back" typ="bool">Currently not implemented.</ArgTableRow>
<ArgTableRow arg="rp-hash-mask-length" typ="num">The hash mask allows changing how many groups to map to one of the matching RPs.</ArgTableRow>
<ArgTableRow arg="rp-static-override" typ="bool">Changes the selection priority for static RP. When disabled, the bootstrap RP set has a higher priority. When enabled, static RP has a higher priority.</ArgTableRow>
<ArgTableRow arg="ssm-range" typ="address (flags=46/)">Currently not implemented.</ArgTableRow>
</ArgTable>
