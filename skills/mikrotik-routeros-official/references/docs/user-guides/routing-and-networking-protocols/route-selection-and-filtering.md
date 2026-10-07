# Route Selection and Filtering

> Route filtering in MikroTik RouterOS uses script-like syntax to match prefixes and modify routing distances based on conditions, with properties categorized as readable or readable/writable for matchers and actions.

# Route Selection and Filtering

## Route Filtering

### Filter Syntax

Routing filter rules use script-like syntax. The following example matches prefixes from subnet 192.168.1.0/24 with a prefix length greater than 24 and increments the default distance by 1. If there is no match, it subtracts the default distance by one.

```ros
/routing/filter/rule
  add chain=myChain \
  rule="if (dst in 192.168.1.0/24 && dst-len>24) {set distance +1; accept} else {set distance -1; accept}"
```

A filter rule may consist of multiple matchers and actions:

```text
if ( [matchers] ) { [actions] } else { [actions] }
```

There are two types of properties:

- Only readable — properties whose values are read-only and cannot be rewritten. They can be used only by matchers.
- Readable/writable — properties whose values are readable and writable. They can be used by filter actions and by matchers.

For numeric properties only, readable properties can be matched by other readable properties or by constant values with boolean operators.

```text
[matchers]:
[prop readable] [bool operator] [prop readable]

[actions]:
[action] [prop writeable] [value]
```

You do not need a boolean operator if the matcher has only one possible operation.

Example without a boolean operator:

```text
if ( protocol connected ) { accept }
```

Example with boolean operator:

```text
if ( bgp-med < 30 ) { accept }
```

With readable flag properties, the matcher does not require a boolean operator or a value.

```text
if ( ospf-dn ) { reject }
```

:::info
The default action of the routing filter chain is `reject`.
:::

#### Only Readable Properties

| Property | Type | Description |
| :-- | :-- | :-- |
| ***Numeric properties*** |  |  |
| `dst-len` |  | Destination prefix length |
| `bgp-path-len` |  | The current length of the BGP AS-PATH |
| `bgp-input-local-as` |  | AS number of the local peer to which the prefix was sent |
| `bgp-input-remote-as` |  | AS number of the remote peer from which the prefix was received |
| `bgp-output-local-as` |  | AS number of the peer that will advertise the prefix |
| `bgp-output-remote-as` |  | AS number of the peer to which the prefix will be advertised |
| `ospf-metric` |  | Current OSPF metric |
| `ospf-tag` |  | Current OSPF tag |
| `rip-metric` |  | Current RIP metric |
| `rip-tag` |  | Current RIP tag |
| ***Flag properties*** |  |  |
| `active` |  | indicates whether the route is active |
| `bgp-atomic-aggregate` |  |  |
| `bgp-communities-empty` |  | indicates if the BGP Communities attribute is empty |
| `bgp-ext-communities-empty` |  | indicates if the BGP Extended Communities attribute is empty |
| `bgp-large-communities-empty` |  | indicates if the BGP Large Communities attribute is empty |
| `bgp-network` |  | Indicates if the prefix is originated from BGP networks |
| `ospf-dn` |  | Indicates if the OSPF route has the DN bit set. |
| ***Prefix properties*** |  |  |
| `dst` |  | Destination |
| `ospf-fwd` |  | Current OSPF forwarding address |
| `bgp-input-local-addr` |  | The IP address of the local peer to which the prefix was sent |
| `bgp-input-remote-addr` |  | The IP address of the remote peer from which the prefix was received |
| `bgp-output-local-addr` |  | The IP address of the peer that will advertise the prefix |
| `bgp-output-remote-addr` |  | The IP address of the peer to which the prefix will be advertised |
| Other Properties |  |  |
| `afi` | `ipv4 \| ipv6 \| l2vpn \| l2vpn-cisco \| vpnv4 \| vpnv6` | The address family of the route. |
| `bgp-as-path` | `numeric_regexp` | AS path [regexp matching](#as-path-regexp-matching) |
| `bgp-as-path-slow-legacy` | `string_regexp` | **Deprecated**. Extremely slow old-style AS path matching. This parameter should be used only as a temporary matcher while migrating from an old ROS v6 config. [Read more>>](#as-path-regexp-matching) |
| `chain` | `chain_name` |  |
| `origin` | `string` | Match route's origin instance, for example, it can match routes imported from a specific OSPF instance: `if (origin <instance_name>) {}` |
| `ospf-type` | `ext1 \| ext2 \| inter \| intra \| nssa1 \| nssa2` | Type of the OSPF route: ext1 - external (Type 5 LSA) with type1 metricext2 - external (Type 5 LSA) with type2 metricinter - inter-area-route (Type 3 LSA)intra - intra-area-route (Type 1/2 LSA)nssa1 - Type 7 LSA with type1 metricnssa2 - Type 7 LSA with type2 metric |
| `protocol` | `bgp \| connected \| dhcp \| fantasy \| modem \| ospf \| rip \| static \| slaac \| vpn` | Protocol type from which the route was imported. |
| `rpki` | `invalid \| unknown \| valid \| unverified` | [RPKI](./unicast/rpki.md) validation status of the prefix |
| `rtab` | `routing_table_name` | Name of the routing table the route was imported from |
| `vrf` | `vrf_name` | Name of the VRF the route was imported from |

#### Writeable Properties

| Property | Type | Description |
| :-- | :-- | :-- |
| ***Numeric properties*** |  |  |
| `distance` |  | route distance |
| `scope` |  |  |
| `scope-target` |  | target scope |
| `bgp-weight` |  | BGP WEIGHT attribute |
| `bgp-med` |  | BGP MED attribute is local to the router. It is also used in the output of iBGP peers. |
| `bgp-out-med` |  | BGP MED attribute to be sent to a remote peer. Should be used in the output chain of eBGP peers. |
| `bgp-local-pref` |  | BGP LOCALPREF attribute |
| `bgp-igp-metric` |  | BGP IGP METRIC |
| `bgp-path-peer-prepend` |  | Prepend last received remote peer's ASN. If the prefix is originated from the router, then this parameter will not do anything on the router's output, because ASN does not exist yet.    If used as a matcher in BGP input, it is possible to filter prefixes exceeding a certain number of prepends. For example, if a remote peer prepends its ASN 5 times, but we want to allow max 4 times prepended ASN, then we can use: `if (bgp-path-peer-prepend > 4) {reject}`    This parameter also overrides any prepends received from the remote peer, for example, if the remote peer prepended its AS 3 times, we can remove this prepend by setting `bgp-path-peer-prepend 1` in BGP input |
| `bgp-path-prepend` |  | Prepend router's ASN, should be used in BGP output. |
| `ospf-ext-metric` |  | OSPF External route metric |
| `ospf-ext-tag` |  | OSPF external route tag |
| `rip-ext-metric` |  | RIP External route metric |
| `rip-ext-tag` |  | RIP External route tag |
| ***Flag properties*** |  |  |
| `ospf-ext-dn` |  | DN bit for external OSPF routes |
| `blackhole` |  | Blackhole route |
| `suppress-hw-offload` |  | Whether to [suppress L3 HW offloading](../../bridging-and-switching/l3-hardware-offloading.md#suppressing-hw-offload) |
| `use-te-nexthop` |  |  |
| ***Other properties*** |  |  |
| `gw` | `ipv4/6 address` | IPv4/IPv6 address or interface name. In the case of BGP output, a gateway can be adjusted in the following setups: is a BGP reflectornexthop-choice is set to propagateis not eBGP and nexthop-choice=force-self is not set. |
| `gw-ll` | `ipv6 address` | ipv6 link local nexthop attribute. In the case of BGP output, a gateway can be adjusted in the following setups: is a BGP reflectornexthop-choice is set to propagateis not eBGP and `nexthop-choice=force-self` is not set. |
| `gw-interface` | `interface_name` | The interface part of the gateway. Should be used if it is required to attach a specific interface for next-hop, like (`1.2.3.4%ether1`) |
| `gw-check` | `none \| arp \| icmp \| bfd \| bfd-mh` |  |
| `pref-src` | `ipv4/6 address` |  |
| `bgp-origin` | `igp \| egp \| incomplete` |  |
| `ospf-ext-fwd` | `ipv4/6 address` | Forwarding address of External OSPF route |
| `ospf-ext-type` | `type1 \| type2` | OSPF External route type |
| `comment` | `string` |  |
| `bgp-communities` | `inline_community_set \| community_list_name` | BGP Communities attribute is defined in [RFC 1997](https://tools.ietf.org/html/rfc1997). Each community is 32-bit in size. |
| `bgp-ext-communities` | `inline_ext_community_set \| ext_community_list_name` | BGP Extended Communities attribute is defined in [RFC 4360](https://tools.ietf.org/html/rfc4360). RouterOS parses `site-of-origin` (prefixed with `soo:`) and `route-target` (prefixed with `rt:`) extended communities. For example, `set bgp-ext-communities rt:1111:2.3.4.5;` It is possible to set/match RAW extended community value in 64-bit hex, for example, `set bgp-ext-communities 0x.........;` |
| `bgp-large-communities` | `inline_large_community_set \| large_community_list_name` | BGP Large Communities attribute is defined in [RFC 8092](https://datatracker.ietf.org/doc/html/rfc8092). Suitable for use with all ASNs including 32-bit ASNs. Each community is 12-bytes in length and consists of 3 parts: `global_admin:local_part_1:local_part_2`. |

#### Commands

| Command | Params | Description |
| :-- | :-- | :-- |
| `accept` |  | accept matched prefix and stop processing the chain. |
| `reject` |  | reject matched prefix and stop processing the chain, the prefix will be stored in the memory as "filtered" and will not be a candidate to be selected as the best path. |
| `return` |  | return to the parent chain |
| `jump` | `jump chain_name` | jump to a specified chain |
| `unset` | `unset prop_name` | used to unset the value of the following properties: `pref-src, bgp-med, bgp-out-med, bgp-local-pref` |
| `append` |  | append at the end of the list or string. Following property values can be appended: `bgp-communities, bgp-ext-communities, bgp-large-communities, comment` |
| `filter` |  | Inverse of the delete action (Delete everything except the specified values). Values of the following properties can be filtered: `bgp-communities, bgp-ext-communities, bgp-large-communities` |
| `delete` |  | Delete the value of the specified property. Values of the following properties can be deleted: `bgp-communities, bgp-ext-communities, bgp-large-communities` |
| `set` | `prop_writeable value` | The command is used to set a new value to writeable properties. Value can be set from other readable properties of matching types. For numeric properties, it is possible to prefix the value with +/- which will increment or decrement the current property value by a given amount. For example, `set bgp-local-pref +1` will increment the current LOCAL\_PREF by one, or extract the value from another readable num property, `set distance +ospf-ext-metric` |
| `rpki-verify` | `rpki_group_name` | Enable [RPKI](./unicast/rpki.md) verification in the current chain from the specified RPKI group. |

#### Operators

##### Matcher Operators

| Operator | Description | Example |
| :-- | :-- | :-- |
| `&&` | Logical AND operator | `if (dst in 192.168.0.0/16 && dst-len in 16-32) {reject;}` |
| `\|\|` | Logical OR operator | `if (dst in 192.168.0.0/16 \|\| dst-len in 16-32) {reject;}` |
| `not` | Logical NOT operator | `if (not bgp-network) {reject; }` |

##### Num Prop Operators

| Operator | Description |
| :-- | :-- |
| `in` | returns true if the value is in the provided numeric range. Numeric range can be written in the following formats: `{int..int}`, `{int-int}` |
| `==` | returns true if numeric values are equal |
| `!=` | returns true if numeric values are not equal |
| `>` | returns true if the left numeric value is greater than the right numeric value |
| `<` | returns true if the left numeric value is less than the right numeric value |
| `>=` | returns true if the left numeric value is greater than or equal to the right numeric value |
| `<=` | returns true if the left numeric value is less than or equal to the right numeric value |

##### Prefix Operators

| Operator | Description |
| :-- | :-- |
| `in` | Returns true if the prefix is the subnet of the provided network. If an operator is used to match prefixes from the address list (e.g `dst in list_name`), then it will match only the exact prefix. |
| `!=` | Returns true if the prefix is not equal to the provided value |
| `==` | Returns true if the prefix is equal to the provided value |

:::info
Address lists by design are matching host addresses which means that it will match also  /32 prefix that belongs to any range from the address list. The workaround to exclude /32  prefixes from being advertised is to use dst-len `if (dst in list_name && dst-len < 32) {}`
:::

##### BGP Community Operators

| Operator | Description | Example |
| :-- | :-- | :-- |
| `equal` | returns true if the provided communities are equal to the route's property value |  |
| `equal-list` | returns true if communities from the provided `community-list` are equal to the route's property value |  |
| `any` | returns true if the route's property value contains at least one of the provided communities |  |
| `any-list` | returns true if the route's property value contains at least one community from the provided list |  |
| `includes` | returns true if the route's property value includes specified communities |  |
| `includes-list` | returns true if the route's property value includes all communities from the specified `communities-list` |  |
| `subset` | returns true if the route's community subset matches communities from the list | `1:1,3:3` will match `1:1,2:2,3:3` |
| `subset-list` | the same as `subset`, but matches communities from the community list. |  |
| `any-regexp` | the same as `any`, but matched by regexp |  |
| `subset-regexp` | the same as `subset`, but matched by regexp |  |

##### String Operators

| Operator | Description |
| :-- | :-- |
| `find` | Check if the provided substring is part of the property value |
| `regexp` | Match the string regexp of the property value |

### Deleting BGP Communities

Routing filters allow clearing BGP communities by using the `delete` command. The `delete` command accepts several parameters based on the type of community:

- **communities**:
  - `wk` - Will match and remove well-known communities.
  - `other` - Will match and remove other communities that are not well known.
  - `regexp` - regexp pattern to match communities that should be deleted.
  - `<community-list name>` - Deletes communities from specified `community-list`.
- **ext-communities**:
  - `rt` - Will match and remove **RouteTarget**.
  - `soo` - Will match and remove **Site-of-Origin**.
  - `other` - Will match and remove other ext communities that are not **RT** or **SOO**.
  - `regexp` - regexp pattern to match ext communities that should be deleted.
  - `<community-ext-list name>` - Deletes communities from specified `community-ext-list`.
- **large-communities**:
  - `all` - Removes everything.
  - `regexp` - regexp pattern to match large communities that should be deleted.
  - `<community-large-list name>` - Deletes large communities from specified `community-large-list`.

It is possible to specify multiple community types, for example delete all SOOs, other types of ext communities and specific RTs from the community-ext list:

```ros
/routing/filter/community-ext-list
add list=myRTList communities="rt:1.1.1.1:222"
/routing/filter/rule
add chain=myChain rule="delete bgp-ext-communities soo,other,myRTList;"
```

### AS-PATH Regexp Matching

An AS path is the sequence of autonomous system numbers (ASNs). For example, the AS path `123 456 789` means the route originated from AS 789 and traversed AS 456 before reaching the destination. To apply routing policies, match specific AS numbers or sets of AS numbers in the AS path by using a regular expression (regexp).

There are two common ways to work with AS path data:

- Convert the whole AS path to a string and let regexp operate on the string (ROS v6 or Cisco style).
- Let regexp operate on each AS path entry as a number (ROS v7, Juniper style).

The first method matches per character. The second method matches per AS number. The second method is faster and uses fewer resources than the string matching approach.

This change requires administrators to use new regexp strategies. Old regexp patterns from RouterOS v6 cannot be copied and pasted directly because they can cause syntax errors or unexpected results.

Take this basic AS path filter rule:

```ros
/routing/filter/rule
add chain=myChain rule="if (bgp-as-path .1234.) {accept}"
```

This regexp pattern matches ASN 1234 anywhere in the middle of the AS path. With old style string matching method, the same pattern matches any AS path that contains an ASN with at least six characters and the substring `1234`. An equivalent old style pattern is `._1234_.`.

For example, the old string style pattern `1234[5-9]` matches 12345 through 12349 anywhere in the string. That yields matches such as `12345 3434` and `11 9123467 22`. With new style matcher, the same pattern matches an AS path containing the exact ASN 1234 followed by an ASN from 5 to 9, such as `1234 7 111` or `111 1234 5 222`. It does not match `12345 3434`.

:::danger
Copying regexp patterns between implementations can produce unexpected or dangerous results.

Do not copy Regex patterns directly from ROS v6 or Cisco configurations, they are not directly compatible. It can lead to unexpected or even dangerous configurations in some scenarios.
:::

:::info
The AS-Path parameter must exist for the regexp matcher to be applied. This means that it is not possible to match a non-existent (empty) AS-Path with a regular expression, aka `^$`. `bgp-path-len` should be used instead.
:::

#### Regex Testing Tool

RouterOS has a built-in regexp checking tool to help administrators validate regexps. This tool also supports num-list values so you can test a regexp against any AS path before applying it to routing filters.

```ros
/routing/filter/num-list/add list=test range=100-1500

/routing/filter/test-as-path-regexp regexp="[[:test:]]5678\$" as-path="1234,5678"
```

#### Supported Operators

| Operator | Description | Example | Example Explained | Example Matches |
| :-- | :-- | :-- | :-- | :-- |
| `^` | Represents the beginning of the path | `^1234` | will match an AS-path starting with ASN 1234 |  |
| `$` | Represents the end of the path | `1234$` | will match the AS-path of origin ASN 1234 |  |
| `*` | Zero or more occurrences of the listed ASN | `^1234*$` | will match a Null as-path or an as-path where ASN 1234 may or may not appear multiple times | **Match:**  1234  1234 1234 1234  Null path  **No Match:**  1234 5678 |
| `+` | One or more occurrences of the listed ASN | `1234+` | will match an AS-path where ASN 1234 appears at least once | **Match:**  1234  3 1234 6  **No match:**  12345 678 |
| `?` | Zero or one occurrence of the listed ASN | `^1234? 5678` | will match an AS-path that may or may not start with ASN 1234 appearing once. | **Match**:  5678  1234 5678  **No match:**  1234 1234 5678  12345 5678 |
| `.` | One occurrence of any ASN | `^.$` | will match any AS-path with the length of one. | **Match:**  12345  45678  **No match:**  1234 5678 |
|  `\|`  | Match one of two ASNs on each side | `^(1234\|5678)` | will match an AS-path starting with ASN 1234 or 5678 | **Match**:  1234  5678  1234 5678  **No Match:**  91011 |
| `[ ]`  `[^ ]` | Represents the set of AS numbers where one AS number from the list must match.  Use ^ after opening the bracket to negate the set.  It is also possible to reference the pre-defined num-lists from [num-list](#community-and-num-lists) with [[:numset\_name:]] | `^[1234 5678 1-100]` | will match the AS-path that starts with 1234 or 5678 or from the range of 1 to 100 | **Match:**  1234  99  5678  **No Match:**  101 |
| `()` | Group of regexp terms to match | `^(1234$\|5678)` | will match an AS-path that starts and ends with 1234 or an AS-path that starts with 5678 | **Match:**  1234  5678 9999  **No Match:**  1234 5678 |

:::warning
Repetition ranges {} are not supported.
:::

### Community and Num Lists

A list of commonly used numbers can be configured from the `/routing/filter/num-list` menu. These lists of numbers can be used in the filter rules to simplify the filter setup process.

In a similar manner, you are allowed to also define community, extended community, and large community lists. Community sets can be used for matching, appending, and setting.

For example, match communities from the list and clear the attribute:

```ros
/routing/filter/community-list
add communities=111:222 list=myCommunityList

/routing/filter/rule
add chain=myChain rule="if (bgp-communities equal-list myCommunityList) {delete bgp-communities wk,other; accept;}"
```

## Route Selection

Route selection rules control how output routes are selected from available candidate routes. By default, if no selection rules are set, output selects the best route.

The following routing table shows two candidate routes and one best route. By default, when BGP selects a route to send out, it chooses the active route.

```text
[admin@4] /routing/route> print where dst-address=1.0.0.0/24
Flags: A - ACTIVE; b, y - COPY
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
   DST-ADDRESS  GATEWAY         AFI  DISTANCE  SCOPE  TARGET-SCOPE  IMMEDIATE-GW
 b 1.0.0.0/24   10.155.101.217  ip4        19     40            30  10.155.109.254%ether1
Ab 1.0.0.0/24   10.155.101.232  ip4        20     40            30  10.155.109.254%ether1
 b 1.0.0.0/24   10.155.101.231  ip4        20     40            30  10.155.109.254%ether1
```

If you need a preference for routes that are not active, use selection rules.

Selection rules in RouterOS are configured from the `/routing/filter/select-rule` menu.

Select rules can also call routing filters so routes are selected by filter rules. For example, to mimic the default output selection, use this rule set:

```ros
/routing/filter/rule
add chain=get_active rule="if (active) {accept}"

/routing/filter/select-rule
add chain=my_select_chain do-where=get_active
```

Select rules can be also used to limit how many additional paths to pick for BGP Add-path, for example max 3 paths:

```ros
/routing/filter/select-rule add chain=select-for-addpath do-take=3
```

## Routing Filter Wizard

Because writing filter rules in script-like syntax is more complex, routing filter wizard that generates filter rules with ROSv6-like syntax was introduced.

Quick demonstration:

```routeros
[admin@CCR2004_2XS_111] /routing/filter> filter-wizard <tab>
action        dst                   ospf-type         scope-target      set-gw-check                use-te-nexthop
afi           dst-len               protocol          set-bgp-...       set-scope
bgp-...       gateway               routing-table     set-blackhole     set-scope-target
blackhole     jump-target-chain     rpki              set-comment       set-suppress-hw-offload
chain         match-chain           rpki-verify       set-distance      set-use-te-nexthop
distance      ospf-metric           scope             set-gateway       suppress-hw-offload

[admin@CCR2004_2XS_111] /routing/filter> filter-wizard action=accept chain=vpn-in afi=vpnv4 set-bgp-ext-communities=rt:2:2
  result: Filter rule 'if (afi vpnv4) { set bgp-ext-communities rt:2:2; accept; }' added

[admin@CCR2004_2XS_111] /routing/filter> /routing/filter/rule/print
Flags: X - disabled, I - inactive
 0   ;;; added by filter-wizard
     chain=vpn-in rule="if (afi vpnv4) { set bgp-ext-communities rt:2:2; accept; }"
```

The filter wizard adds rules at the end of the list and gives them the comment `added by filter-wizard`.

Errors returned when you try to add a filter with unacceptable values are printed in the CLI and logged in the system log with the `route,error` topic.

```routeros
[admin@CCR2004_2XS_111] /routing/filter> filter-wizard action=accept chain=vpn-in afi=vpnv4 match-chain=vpn-in
  result: Error adding 'if (chain vpn-in && afi vpnv4) { accept; }'match with 'vpn-in' creates chain loop (6)

[admin@CCR2004_2XS_111] /routing/filter> /log/print
 2025-05-19 13:05:15 route,error Error adding 'if (chain vpn-in && afi vpnv4) { accept; }'match with 'vpn-in' creates chain loop (6)

```
