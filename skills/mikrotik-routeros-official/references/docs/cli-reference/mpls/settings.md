# settings

> RouterOS settings reference for /mpls/settings.

-----------

## mpls/settings 
**Conditions:** !smips
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="dynamic-label-range" typ="range">Range of Label numbers used for dynamic allocation. The first 16 labels are reserved for special purposes (as defined in RFC). If you intend to configure labels statically then adjust the dynamic default range not to include numbers that will be used in a static configuration.</ArgTableRow>
<ArgTableRow arg="propagate-ttl" typ="enum (yes | no)">Whether to copy TTL values from IP header to MPLS header. If this option is set to **no** then hops inside the MPLS cloud will be invisible to traceroutes.</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="enum (yes | no)">Enable/disable MPLS fast-path support.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mpls-fast-path-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="mpls-fast-path-bytes" typ="num"></ArgTableRow>
</ArgTable>
