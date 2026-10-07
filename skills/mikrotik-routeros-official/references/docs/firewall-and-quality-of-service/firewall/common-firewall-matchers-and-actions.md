# Common Firewall Matchers and Actions

> This page explains MikroTik RouterOS firewall statistics and commands, detailing how to view matching stats for IPv4/IPv6 rules, reset counters, and lists common matchers like MAC addresses, interfaces, IP ranges,...

# Common Firewall Matchers and Actions

## Stats

To view matching statistics by firewall rules, run the `/ip/firewall/filter/print stats` command or `/ipv6/firewall/filter/print stats` for IPv6 firewall.

| Property | Description |
| :-- | :-- |
| **bytes** (*integer*) | The total amount of bytes matched by the rule |
| **packets** (*integer*) | The total amount of packets matched by the rule |

```text
[admin@MikroTik] > ip firewall filter print stats
Flags: X - disabled, I - invalid, D - dynamic
 #    CHAIN                                                                                                                 ACTION                            BYTES         PACKETS
 0  D ;;; special dummy rule to show fasttrack counters
      forward                                                                                                               passthrough              50 507 925 242      50 048 246
 1    ;;; defconf: drop invalid
      forward                                                                                                               drop                            432 270           9 719
 2    ;;; defconf: drop invalid
      input                                                                                                                 drop                            125 943           2 434
 3    input                                                                                                                 accept                   20 090 211 549      20 009 864
 4    ;;; defconf: accept ICMP
      input                                                                                                                 accept                          634 926           7 648
 5    ;;; defconf: drop all not coming from LAN
      input                                                                                                                 drop                          4 288 079          83 428
  6    ;;; defconf: accept in ipsec policy
       forward                                                                                                               accept                                0               0
  7    ;;; defconf: accept out ipsec policy
       forward                                                                                                               accept                                0               0
  8    ;;; defconf: fasttrack
       forward                                                                                                               fasttrack-connection     28 505 528 775      31 504 682
  9    ;;; defconf: accept established,related, untracked
       forward                                                                                                               accept                   28 505 528 775      31 504 682
 10    ;;; defconf: drop all from WAN not DSTNATed
      forward                                                                                                               drop                                  0               0
```

Statistics parameters can be reset by the following commands:

| Command | Description |
| :-- | :-- |
| **reset-counters** (*id*) | Reset statistics counters for a specific firewall rule or a list of rules. |
| **reset-counters-all** | Reset statistics counters for all firewall rules in the table. |

## Other Useful Commands

By default print is equivalent to `print static` and shows only static rules.

To also print dynamic rules, use `print all`.

Or to print only dynamic rules use `print dynamic`.

## Matchers

Matchers are executed in a specific order.

### For IPv4

- Source MAC Address
- In/Out interfaces
- In/Out interface lists
- IP Range
- Address type
- Address list
- TTL
- DSCP
- Length
- TLS
- IPv4 Options
- Dst Port
- Src Port
- Any Port
- TCP Options
- TCP MSS
- ICMP Codes
- Ingress Priority
- Priority
- Packet Mark
- Realm (routing table)
- Hotspot
- Connection Mark
- Connection State
- Connection NAT State
- Connection Bytes
- Connection Limit
- Connection Rate
- Ipsec Policy
- Helper
- String (content)
- PSD
- Layer7
- Random
- Nth
- PCC
- Limit
- Dst Limit
- Log

### For IPv6

- Address type
- Address list
- Source MAC Address
- In/Out interfaces
- In/Out interface lists
- Hop Limit
- DSCP
- Length
- TLS
- IPv6 Header
- Dst Port
- Src Port
- Any Port
- TCP Options
- TCP MSS
- ICMPv6 Codes
- Ingress Priority
- Priority
- Packet Mark
- Connection Mark
- Connection State
- Connection NAT State
- Connection Bytes
- Connection Limit
- Connection Rate
- Ipsec Policy
- Helper
- Match String (content)
- Random
- Nth
- PCC
- Limit
- Dst Limit
- Log
