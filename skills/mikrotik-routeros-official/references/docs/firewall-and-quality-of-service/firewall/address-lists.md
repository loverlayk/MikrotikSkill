# Address lists

> Address lists group IP addresses, prefixes, ranges and DNS names under one name for firewall rules. Entries can be static, added by rules with a timeout, or resolved from names.

# Address lists

An address list is a named set of IP addresses, prefixes and, for IPv4, address ranges. Filter, NAT, mangle and raw rules match it with `src-address-list` and `dst-address-list`, and `!` in front of the name matches every address that is not in the list. One rule then covers many addresses, and you change who it applies to by changing the list, not the rule.

Entries come from three sources: you add them, firewall rules add them with the `add-src-to-address-list` and `add-dst-to-address-list` actions, and the router resolves DNS names you put in a list. IPv4 lists are in `/ip/firewall/address-list` and IPv6 lists in `/ipv6/firewall/address-list`. The two are separate, even when a list has the same name in both.

## Block traffic from a list of addresses

Drop everything that comes from the WAN from the addresses in the list `blocked`. `WAN` is the interface list of the default configuration that holds the internet port:

```ros
/ip/firewall/address-list/add list=blocked address=203.0.113.0/24 \
    comment="Abuse reports"
/ip/firewall/address-list/add list=blocked address=198.51.100.7
/ip/firewall/raw/add chain=prerouting action=drop \
    in-interface-list=WAN src-address-list=blocked \
    comment="Drop traffic from blocked addresses"
```

```ros
[admin@MikroTik] > /ip/firewall/address-list/print where list=blocked
Columns: LIST, ADDRESS, CREATION-TIME
# LIST     ADDRESS         CREATION-TIME
;;; Abuse reports
0 blocked  203.0.113.0/24  2026-10-01 08:50:12
1 blocked  198.51.100.7    2026-10-01 08:50:12
```

Rules in `/ip/firewall/raw` run before [connection tracking](../connection-tracking), so this rule drops every packet from these addresses that arrives on the WAN: new connections to the router and to forwarded services, and also the replies to connections that hosts in your LAN open to them. To block more addresses later, add them to the list.

To add many entries at once, paste several `add` lines into the terminal, or put them in an `.rsc` file and import it with `/import`. `203.0.113.77/24` and `203.0.113.0/24` are the same entry, so the second `add` fails with `failure: already have such entry`, and an import stops there.

IPv6 addresses go into the IPv6 list, with the same drop rule in `/ipv6/firewall/raw`:

```ros
/ipv6/firewall/address-list/add list=blocked address=2001:db8:bad::/48
/ipv6/firewall/raw/add chain=prerouting action=drop \
    in-interface-list=WAN src-address-list=blocked \
    comment="Drop traffic from blocked addresses"
```

An IPv6 host can change its address inside its /64. For IPv6, list whole prefixes, a /64 or larger, rather than single addresses.

## Allow access from a dynamic address by name

A remote office or a home connection often has an address that changes. Put its DNS name in a list, for example the DDNS name of the office router, and allow SSH and WinBox from it (SSH is TCP port 22, WinBox TCP port 8291):

```ros
/ip/firewall/address-list/add list=trusted address=office.example.com \
    comment="Office router"
/ip/firewall/filter/add chain=input action=accept protocol=tcp \
    dst-port=22,8291 src-address-list=trusted \
    comment="Allow SSH and WinBox from trusted addresses" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

The rule goes before the default `drop all not coming from LAN` rule. A plain `add` puts it after the drop rule, where it never matches.

The router resolves the name and adds the address as a dynamic entry, with the name as its comment:

```ros
[admin@MikroTik] > /ip/firewall/address-list/print where list=trusted
Flags: D - DYNAMIC
Columns: LIST, ADDRESS, CREATION-TIME
#   LIST     ADDRESS             CREATION-TIME
;;; Office router
4   trusted  office.example.com  2026-10-01 08:52:00
;;; office.example.com
5 D trusted  198.51.100.20       2026-10-01 08:52:00
```

When the DNS record expires, the router resolves the name again and replaces an address that has changed, so the rule follows the office's address.

:::warning
The rule opens SSH and WinBox to every host that has the address the name resolves to. Use a name that only you control. Access depends on the answers of the router's DNS servers, so use DNS servers you trust, and keep another way in, such as a VPN. If `/ip/service` limits WinBox or SSH with `available-from`, the address must be allowed there as well (see [Limit who can use a service](../../system-information-and-utilities/services#limit-who-can-use-a-service)).
:::

## Block hosts that probe a closed port

A host that tries to reach Telnet on your WAN address is usually scanning for weak devices. List such hosts for a day and drop all their traffic, including traffic to services you forward to the LAN:

```ros
/ip/firewall/raw/add chain=prerouting action=add-src-to-address-list \
    in-interface-list=WAN protocol=tcp dst-port=23 \
    src-address-list=!trusted \
    address-list=port-scanners address-list-timeout=1d \
    comment="List hosts that probe the Telnet port"
/ip/firewall/raw/add chain=prerouting action=drop \
    in-interface-list=WAN src-address-list=port-scanners \
    comment="Drop listed hosts"
```

The first rule adds the source address to `port-scanners` and passes the packet on to the next rule. From then on, the second rule drops every packet from that host, until the timeout ends. Each new probe resets the timeout to a full day.

One packet is enough to list its source address, and the source address of a packet can be forged. Keep the addresses you rely on, such as your DNS servers, VPN peers and the office, in the `trusted` list from the previous section: `src-address-list=!trusted` makes the first rule skip them.

```ros
[admin@MikroTik] > /ip/firewall/address-list/print where list=port-scanners
Flags: D - DYNAMIC
Columns: LIST, ADDRESS, CREATION-TIME, TIMEOUT
#   LIST           ADDRESS        CREATION-TIME        TIMEOUT
2 D port-scanners  198.51.100.23  2026-10-01 08:50:30  23h59m55s
```

Entries with a timeout are dynamic (`D`): they are not saved in the configuration, and a reboot clears them. Scanners come back, so the list fills again. `address-list-timeout=none-static` keeps the entries over reboots, but the list then grows with every scanner until you remove entries, and every new entry changes the saved configuration.

For rules that list a host only after several attempts, see [SSH brute-force protection](../user-guides/bruteforce-prevention) and [Port knocking](../user-guides/port-knocking), which opens a port only after a secret sequence of connection attempts.

## View, remove and export entries

Show a list, or only count its entries:

```ros
/ip/firewall/address-list/print where list=port-scanners
/ip/firewall/address-list/print count-only where list=port-scanners
```

Remove one entry:

```ros
/ip/firewall/address-list
remove [find list=port-scanners address=198.51.100.23]
```

To copy a list to another router, export it to a file. Write `file=` before `where`, because `where` takes the rest of the command line as its condition. With `file=` after it, the export prints to the terminal and writes no file.

```ros
/ip/firewall/address-list/export file=blocked where list=blocked
```

The file `blocked.rsc` holds the static entries of the list. Dynamic entries are not exported.

```ros
/ip firewall address-list
add address=203.0.113.0/24 comment="Abuse reports" disabled=no dynamic=no \
    list=blocked
add address=198.51.100.7 disabled=no dynamic=no list=blocked
```

Copy the file to the other router, with **Files** in WinBox (see [Manage files in WinBox](../../system-information-and-utilities/files#manage-files-in-winbox)) or with `scp`, and import it:

```ros
/import blocked.rsc
```

The file holds only the entries: add the drop rule on the other router as well. The import stops at the first address that is already in the list, with `failure: already have such entry`. To update the list on the other router later, remove its entries first (the list holds no DNS names) and import the new file:

```ros
/ip/firewall/address-list/remove [find list=blocked]
/import blocked.rsc
```

To empty a list that holds a DNS name, remove it in two steps:

```ros
/ip/firewall/address-list/remove [find list=trusted !dynamic]
/ip/firewall/address-list/remove [find list=trusted]
```

The first command removes the static entries; removing the name also removes the addresses it resolved to. The second removes the dynamic entries that rules added. A single `remove [find list=trusted]` also selects the name's addresses, and it stops with `no such item` after the name is gone.

## How entries behave

### Static and dynamic entries

| How the entry is created | Flag | Saved in the configuration and export | After a reboot |
| :-- | :-- | :-- | :-- |
| `add` without `timeout` | | Yes | Kept |
| A rule with `address-list-timeout=none-static` | | Yes | Kept |
| `add` with `timeout` or `dynamic=yes` | `D` | No | Gone |
| A rule with a time or `address-list-timeout=none-dynamic` | `D` | No | Gone |
| An address resolved from a DNS name | `D` | No, the name entry is | The name entry is kept |

Static entries keep their `creation-time` after a reboot. The entries that DNS and the DHCP server add are dynamic too.

### Timeouts

The longest timeout is `35w3d13h13m56s`. A longer one fails with `value of timeout is out of range (00:00:00 .. 35w3d13:13:56)`.

When a rule matches an address that is already in the list, it resets the entry's timeout. When the address is already a static entry in that list, the entry stays static and gets no timeout.

### Addresses, prefixes and ranges

- An address with a prefix length is stored as its network: `203.0.113.77/24` becomes `203.0.113.0/24`.
- An IPv4 range that is exactly one prefix is stored as that prefix: `198.51.100.0-198.51.100.255` becomes `198.51.100.0/24`. Other ranges stay ranges, for example `198.51.100.10-198.51.100.20`.
- An entry that is already in the list is refused with `failure: already have such entry`. Overlapping entries are accepted, for example a /24 and an address inside it.
- IPv6 lists take addresses and prefixes, but no ranges: `failure: 2001:db8::1-2001:db8::5 is not a valid dns name`. An IPv6 address without a prefix length is stored as a /128.

:::note
Anything that is not a valid address is stored as a DNS name, without an error. A range written in short form, such as `203.0.113.1-254`, becomes a name that never resolves, and the entry matches nothing. Write ranges in full: `203.0.113.1-203.0.113.254`.
:::

### Domain names

- The router resolves the name with its own DNS settings (`/ip/dns`) and adds one dynamic entry for each address in the answer, with the name as the comment. IPv4 lists get the A records, IPv6 lists the AAAA records.
- The dynamic entries show no timeout. When the DNS record expires, the router resolves the name again: addresses that changed are replaced, the others stay.
- The list holds whatever the router's DNS server answers. A filtering DNS server that answers `0.0.0.0` for a name puts `0.0.0.0` in the list. A device that asks another DNS server can get other addresses for the same name.
- Names served by CDNs or by round-robin DNS can return different addresses on each query, so a list built from the name can miss addresses that devices use. When the devices use the router as their DNS server, a static DNS `FWD` entry with `address-list` adds exactly the addresses the router answers them (see [Use domain names in firewall rules](../../network-management/dns#use-domain-names-in-firewall-rules)).
- An entry that holds a name shows the name in `ADDRESS`. When the name resolves, dynamic entries with the name as their comment follow it. A name entry without them does not resolve, which is how a short range that became a name shows up.
- Removing the name entry removes the addresses it resolved to.

## Other features that add entries

- DNS: a static DNS entry with `address-list` adds the addresses the router answers for the name, see [Use domain names in firewall rules](../../network-management/dns#use-domain-names-in-firewall-rules).
- DHCP server: `address-lists` on the server or on a lease adds the address of a bound lease, see [`/ip/dhcp-server`](../../cli-reference/ip/dhcp-server/) and [`/ip/dhcp-server/lease`](../../cli-reference/ip/dhcp-server/lease/).
- PPP: `address-list` in a PPP profile adds the address the server assigns or the client receives, see [User profiles](../../authentication-authorization-accounting/ppp-aaa#user-profiles).

For all parameters, see the CLI reference for [`/ip/firewall/address-list`](../../cli-reference/ip/firewall/address-list) and [`/ipv6/firewall/address-list`](../../cli-reference/ipv6/firewall/address-list).
