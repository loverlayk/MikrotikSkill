# Common Firewall Matchers and Actions

> Commands and rules that are common to the firewall filter, NAT, mangle and RAW tables of RouterOS: view and reset the rule counters, show or hide dynamic rules, and the order in which the matchers of a rule are checked.

# Common Firewall Matchers and Actions

The firewall tables [filter](./filter), [NAT](./nat), [mangle](./mangle) and [RAW](./raw) have several things in common. Each rule counts the packets that it matches. The same commands show and reset these counters. The router checks the matchers of a rule in a fixed order.

The examples on this page use the IPv4 filter table. The counter commands are the same in the other tables and in the IPv6 firewall, for example `/ip/firewall/nat/print stats` or `/ipv6/firewall/filter/print stats`.

## View the rule counters

Each firewall rule counts the packets and the bytes that it has matched. To see the counters, use `print stats`. This command shows the static rules of the `forward` chain:

```ros
/ip/firewall/filter/print stats static where chain=forward
```

```text
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN    ACTION                BYTES  PACKETS
;;; defconf: accept in ipsec policy
0 forward  accept                    0        0
;;; defconf: accept out ipsec policy
1 forward  accept                    0        0
;;; defconf: fasttrack
2 forward  fasttrack-connection  2 457       15
;;; defconf: accept established,related, untracked
3 forward  accept                2 457       15
;;; defconf: drop invalid
4 forward  drop                      0        0
;;; defconf: drop all from WAN not DSTNATed
5 forward  drop                    112        2
```

`PACKETS` is the number of packets that the rule has matched, and `BYTES` is their total size. The line above each rule is its comment.

To see the counters of particular rules, select them by their comment. This command shows the rules whose comment contains "drop invalid":

```ros
/ip/firewall/filter/print stats where comment~"drop invalid"
```

Use the counters to check that a new rule works: send traffic that the rule has to match, and look at its counters. If they do not grow, the rule does not match the traffic, or the packets do not reach the rule: an earlier rule of the chain has accepted or dropped them, or [FastTrack](../connection-tracking#fasttrack) handles the connection. In the default configuration, established connections are FastTracked and accepted at the start of the `forward` chain, so the rules after that do not see most of their packets.

## Reset the counters

To set the counters of one rule or of several rules back to zero, use `reset-counters` with the rules that `find` selects. This command resets the rules whose comment contains "WAN":

```ros
/ip/firewall/filter/reset-counters [find comment~"WAN"]
```

To reset the counters of all rules of the table, use `reset-counters-all`:

```ros
/ip/firewall/filter/reset-counters-all
```

Both commands work on one table: `/ip/firewall/filter/reset-counters-all` does not change the counters of the NAT, mangle and RAW rules. Each table has its own commands, for example for the NAT table:

```ros
/ip/firewall/nat/reset-counters-all
```

## Show or hide dynamic rules

A table can contain dynamic rules, marked with the `D` flag. These are rules that the router adds itself. An example is the rule with the comment "special dummy rule to show fasttrack counters": it processes no packets, and its counters show the traffic that FastTrack handles. You cannot change or remove that rule.

In the IPv4 tables, `print` lists the static and the dynamic rules, and `print all` does the same. To list only one kind, add `static` or `dynamic`:

```ros
/ip/firewall/filter/print dynamic
```

```text
Flags: D - DYNAMIC
0 D ;;; special dummy rule to show fasttrack counters
    chain=forward action=passthrough
```

`/ip/firewall/filter/print static` lists only the rules of the configuration. The rule numbers in the output belong to the list that the command printed, so they differ between `print` and `print static`. In the IPv6 firewall, only the NAT table has the `static` and `dynamic` switches. The IPv6 filter, mangle and RAW tables do not have these switches.

## Order of the matchers

A rule matches a packet only when all its matchers match. The router checks the matchers of a rule in a fixed order, which does not depend on the order in which you write them.

The order matters for the matchers that keep a count or a state of their own, such as `nth`, `limit` and `dst-limit`: they see only the packets that have passed all matchers before them. For example, in a rule with `protocol=icmp` and `limit`, only ICMP packets use up the limit: the `protocol` matcher is not in the lists, and the router checks it before `limit`. In a rule with `nth` and `limit`, the limit counts only the packets that `nth` has selected. A packet over the limit does not match the rule, and the next rule of the chain processes it. `log` comes last: the rule writes a log entry only for a packet that all its matchers have matched.

### For IPv4

1. Source MAC address
2. In and out interfaces
3. In and out interface lists
4. IP range
5. Address type
6. Address list
7. TTL
8. DSCP
9. Length
10. TLS
11. IPv4 options
12. Destination port
13. Source port
14. Any port
15. TCP options
16. TCP MSS
17. ICMP codes
18. Ingress priority
19. Priority
20. Packet mark
21. Realm (routing table)
22. HotSpot
23. Connection mark
24. Connection state
25. Connection NAT state
26. Connection bytes
27. Connection limit
28. Connection rate
29. IPsec policy
30. Helper
31. String (content)
32. PSD
33. Layer7
34. Random
35. Nth
36. PCC
37. Limit
38. Destination limit
39. Log

### For IPv6

1. Address type
2. Address list
3. Source MAC address
4. In and out interfaces
5. In and out interface lists
6. Hop limit
7. DSCP
8. Length
9. TLS
10. IPv6 header
11. Destination port
12. Source port
13. Any port
14. TCP options
15. TCP MSS
16. ICMPv6 codes
17. Ingress priority
18. Priority
19. Packet mark
20. Connection mark
21. Connection state
22. Connection NAT state
23. Connection bytes
24. Connection limit
25. Connection rate
26. IPsec policy
27. Helper
28. String (content)
29. Random
30. Nth
31. PCC
32. Limit
33. Destination limit
34. Log

The properties of the matchers are described in the CLI reference of each table, for example [`/ip/firewall/filter`](../../cli-reference/ip/firewall/filter) and [`/ipv6/firewall/filter`](../../cli-reference/ipv6/firewall/filter).
