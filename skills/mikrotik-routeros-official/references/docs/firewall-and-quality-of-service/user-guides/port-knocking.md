# Port knocking

> Port knocking keeps the management ports of a RouterOS router closed until a client connects to a secret sequence of ports; the firewall then adds the client to a trusted address list. Covers the knock rules in the...

# Port knocking

Every public IP address is scanned constantly, by bots and by services such as Shodan, and anyone can use the results to try brute-force attacks or known exploits against the open ports. Port knocking keeps the ports closed instead: the router only watches for connection attempts to a secret sequence of ports. A client that knocks on the right ports in the right order is added to the `secured` address list, and the firewall accepts its connections.

A typical use is a router at a remote site that you manage from changing addresses, where a fixed list of allowed source addresses does not work.

Port knocking is an extra layer, not a replacement for real authentication. Knocks are plain packets, and anyone who can observe the traffic between you and the router can repeat them. You should reach management services through a VPN such as [WireGuard](../../virtual-private-networks/wireguard) where you can; see [Securing your router](../../getting-started/securing-your-router) for the other measures.

## Open access with a knock sequence

The example assumes the default configuration: the internet-facing interfaces are in the `WAN` interface list, and the input chain ends with the rule `defconf: drop all not coming from LAN`. The knock rules must come before that rule, otherwise knocks from the WAN side never reach them; `place-before` puts each rule there:

```ros
/ip/firewall/filter
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=888 in-interface-list=WAN \
    address-list=888 address-list-timeout=30s \
    comment="Port knocking: first knock" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=555 in-interface-list=WAN \
    src-address-list=888 address-list=555 address-list-timeout=30s \
    comment="Port knocking: second knock" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=222 in-interface-list=WAN \
    src-address-list=555 address-list=secured address-list-timeout=30m \
    comment="Port knocking: last knock" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=accept \
    in-interface-list=WAN src-address-list=secured \
    comment="Port knocking: accept knocked clients" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

How the rules work:

- The first knock, a connection attempt to TCP port 888, adds the source address to the `888` list for 30 seconds.
- The second knock, to port 555, counts only from an address on the `888` list, and adds it to the `555` list. You can chain as many knocks as you like in the same way: each rule requires the list of the previous knock.
- The last knock, to port 222, moves the address to the `secured` list for 30 minutes.
- The `accept` rule accepts all input from addresses on the `secured` list. To open only the management ports, add `protocol=tcp dst-port=22,8291` to it.
- Knocks in the wrong order do not grant access: a knock counts only when the address is already on the list of the previous knock.
- A session opened while the address is on the `secured` list stays open after the entry expires, because the default configuration accepts established connections earlier in the chain. New connections need a new knock sequence.

## Knock from a client

A dedicated port-knocking client works, but a shell one-liner with `nmap` does the job. Each `nmap` run sends a connection attempt to one port; the whole sequence takes a few seconds:

```bash
for x in 888 555 222; do nmap -p $x -Pn 203.0.113.1; done
```

Replace `203.0.113.1` with the public address of your router. The ports show as closed or filtered in the `nmap` output, depending on your firewall; that is expected, because nothing listens on them. After the last knock, connect to the router as usual within 30 minutes.

## Add a blacklist

A port scan that happens to hit the knock ports in the right order opens the router, and with only a few knocks that is not unlikely. A blacklist stops scanners before they get that far. The following rules are added disabled, so that you cannot lock yourself out while you add them:

```ros
/ip/firewall/filter
add chain=input action=drop \
    in-interface-list=WAN src-address-list=blacklist \
    comment="Port knocking: drop blacklisted" disabled=yes \
    place-before=([find chain=input]->0)
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=666 in-interface-list=WAN \
    address-list=blacklist address-list-timeout=1000m \
    comment="Port knocking: bad port" disabled=yes \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=21,22,23,8291,10000-60000 \
    in-interface-list=WAN src-address-list=!secured \
    address-list=blacklist address-list-timeout=1m \
    comment="Port knocking: slow down scans" disabled=yes \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

- The drop rule goes before the first rule of the input chain (`place-before=([find chain=input]->0)`), so a blacklisted address cannot knock or connect at all. Refer to rules with `find` in pasted commands: a plain number such as `place-before=0` works only after a `print` in the same session, and otherwise fails with `item referred by 'place-before' does not exist`.
- A bad port is one that a trusted user never uses. Any connection attempt to it puts the source on the blacklist for 1000 minutes.
- The second rule slows port scans down until they are pointless, without locking out a real user for long: a connection attempt to one of the listed ports puts the source on the blacklist for one minute. The list can hold every port apart from the knock ports. It skips addresses on the `secured` list, so after a successful knock you can use these ports.

:::warning
You can block yourself. When the rules are enabled, connecting to SSH or WinBox before you knock puts your own address on the blacklist for a minute, and your knocks are dropped during that time. A client that was blocked keeps retrying its connection for a while, and each retry can renew the entry: wait a minute after a blocked attempt before you knock again. Enable the rules only when you have another way to reach the router, or in [Safe Mode](../../getting-started/configuration-management/#safe-mode).
:::

When you are ready, enable the rules:

```ros
/ip/firewall/filter/enable [find comment~"^Port knocking"]
```

## Use a passphrase for each knock

You can go further and require a passphrase with a knock. A layer 7 protocol entry matches the passphrase in the packet payload, and a UDP knock rule requires it. Use the UDP rule instead of the first TCP knock:

```ros
/ip/firewall/layer7-protocol/add name=pass regexp="^passphrase\$"
/ip/firewall/filter/add chain=input action=add-src-to-address-list \
    protocol=udp dst-port=888 in-interface-list=WAN \
    layer7-protocol=pass address-list=888 address-list-timeout=30s \
    comment="Port knocking: first knock with passphrase" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
/ip/firewall/filter/remove [find comment="Port knocking: first knock"]
```

The `$` in the regular expression must be escaped as `\$`, otherwise RouterOS reads it as the start of a variable name; the stored expression is `^passphrase$`. The expression matches only the exact payload: a wrong passphrase or a trailing newline does not count. Send the passphrase without a newline, with `printf` or `echo -n`, then knock on the other ports:

```bash
printf 'passphrase' | nc -u -w1 203.0.113.1 888
for x in 555 222; do nmap -p $x -Pn 203.0.113.1; done
```

:::warning
Layer 7 rules are very resource-intensive. Do not use them unless you know what you are doing.
:::

## Check the lists

See which addresses are in the middle of a knock sequence, which are trusted and which are blocked, with the time left for each entry:

```ros
/ip/firewall/address-list/print \
    where list~"^(888|555|secured|blacklist)\$"
```

To unblock an address, remove it from the blacklist:

```ros
/ip/firewall/address-list/remove \
    [find list=blacklist address=203.0.113.10]
```

## IPv6

These rules apply to IPv4. When the router is reachable over IPv6, add the TCP knock rules to `/ipv6/firewall/filter` in the same way, before the rule that drops IPv6 input from outside the LAN.

## Related topics

- [SSH brute-force protection](bruteforce-prevention) limits repeated SSH connections from one address and uses the same `secured` list to exempt clients that knocked correctly.
- [DDoS protection](ddos-protection) detects floods of new connections towards hosts behind the router.

For all rule properties, see [`/ip/firewall/filter`](../../cli-reference/ip/firewall/filter/), [`/ip/firewall/address-list`](../../cli-reference/ip/firewall/address-list) and [`/ip/firewall/layer7-protocol`](../../cli-reference/ip/firewall/layer7-protocol) in the CLI reference.
