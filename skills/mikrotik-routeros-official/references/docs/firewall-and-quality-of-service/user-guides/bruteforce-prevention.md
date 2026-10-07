# SSH brute-force protection

> Protect an internet-facing SSH service on RouterOS with firewall rules that count new connections per source address and block a source that opens too many in a short time. Covers what to do before exposing SSH,...

# SSH brute-force protection

Every public IP address receives a steady stream of automated login attempts. RouterOS delays its answer to each failed login, which slows guessing down, but it does not block the source address. If SSH on your router is reachable from the internet, a bot can keep guessing passwords for as long as it likes.

The firewall rules on this page count the new SSH connections from each source address and block a source that opens too many in a short time. With the [default configuration](../../getting-started/configuration-management/default-configurations), the firewall drops all management access from the WAN side, and you do not need these rules.

## Reduce the exposure first

Rate limiting only slows an attacker down. The following measures remove the risk instead; consider them before you open SSH to the internet:

- Reach the router through a VPN, for example [WireGuard](../../virtual-private-networks/wireguard), and keep SSH closed on the WAN side.
- Allow SSH only from the addresses you manage the router from, as described in [Securing your router](../../getting-started/securing-your-router#opening-management-access-from-wan-advanced).
- Log in with [SSH keys](../../management-tools/ssh#log-in-with-a-public-key) and turn off password logins with `/ip/ssh/set password-authentication=no`. Password guessing then has nothing to find. With the default setting, `yes-if-no-key`, only users without a key can log in with a password.
- Hide the port behind [port knocking](port-knocking), so that SSH opens only for a client that knows the knock sequence.

Use the rules on this page when SSH must stay reachable from the internet, or as an extra layer on top of these measures.

## Block sources that open repeated SSH connections

The rules move a source address through three address lists, one stage per new SSH connection, and put it on a blacklist at the fourth connection:

| Connection from the source | Condition | Result |
|---|---|---|
| First | None | Added to `connection1` for 5 minutes |
| Second | Within 5 minutes of the previous connection | Added to `connection2` for 15 minutes |
| Third | Within 15 minutes of the previous connection | Added to `connection3` for 1 hour |
| Fourth | Within 1 hour of the previous connection | Added to `bruteforce_blacklist` for 1 day, connection dropped |

The example assumes the default configuration: the internet-facing interfaces are in the `WAN` interface list, and the input chain ends with the rule `defconf: drop all not coming from LAN`. The rules must come before that rule, otherwise connections from the WAN side never reach them; `place-before` puts each rule there:

```ros
/ip/firewall/filter
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=22 connection-state=new \
    in-interface-list=WAN src-address-list=connection3 \
    address-list=bruteforce_blacklist address-list-timeout=1d \
    comment="SSH brute force: blacklist" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=22 connection-state=new \
    in-interface-list=WAN src-address-list=connection2 \
    address-list=connection3 address-list-timeout=1h \
    comment="SSH brute force: third connection" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=22 connection-state=new \
    in-interface-list=WAN src-address-list=connection1 \
    address-list=connection2 address-list-timeout=15m \
    comment="SSH brute force: second connection" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=add-src-to-address-list \
    protocol=tcp dst-port=22 connection-state=new \
    in-interface-list=WAN \
    address-list=connection1 address-list-timeout=5m \
    comment="SSH brute force: first connection" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=accept \
    protocol=tcp dst-port=22 in-interface-list=WAN \
    src-address-list=!bruteforce_blacklist \
    comment="SSH brute force: accept" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=drop \
    protocol=tcp dst-port=22 in-interface-list=WAN \
    comment="SSH brute force: drop blacklisted" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

How the rules work:

- The first four rules only add the source to a list; `add-src-to-address-list` does not stop the packet, so it continues to the next rule. The rules are in reverse order, so each connection moves the source one stage further.
- The `accept` rule lets the connection through unless the source is on the blacklist, and the last rule drops it. Without the last rule, a blacklisted connection continues down the chain, and on a firewall that does not drop it later, the blacklist blocks nothing.
- The rules count new connections (`connection-state=new`). A session that is already open stays open, because the default configuration accepts established connections earlier in the chain.
- `in-interface-list=WAN` keeps the rules away from connections from your LAN.
- If SSH listens on a different port, change `dst-port` in every rule.
- If a command fails with `no such item`, the router has no rule with the `defconf: drop all not coming from LAN` comment. On a router without the default firewall, leave out `place-before`, or place the rules before your own drop rule.

:::warning
You can block yourself. The rules count connections, not failed logins: successful logins count too, and a successful login does not remove the source from the lists. An SSH session, a file copy with `scp` and a second session can be enough when a script or backup tool adds one more connection, and that address is then blocked for a day. Exempt the addresses you manage the router from, as described in the next section.
:::

### Exempt trusted addresses

Accept SSH from trusted addresses before the counting rules. The list name `secured` is the one the [port knocking](port-knocking) example uses for clients that knocked correctly, so its accept rule already exempts those clients when it comes before these rules. Add fixed addresses to the same list:

```ros
/ip/firewall/address-list/add list=secured address=198.51.100.7 \
    comment="Office"
/ip/firewall/filter/add chain=input action=accept \
    protocol=tcp dst-port=22 src-address-list=secured \
    comment="SSH brute force: trusted" \
    place-before=[find comment="SSH brute force: blacklist"]
```

### IPv6

These rules apply to IPv4. When SSH is reachable over IPv6, add the same rules to `/ipv6/firewall/filter`, before the rule that drops IPv6 input from outside the LAN.

## Check and unblock

List the sources the rules are tracking, with the time left for each entry, and see how many packets reached each rule:

```ros
/ip/firewall/address-list/print where list~"^connection|^bruteforce"
/ip/firewall/filter/print stats where comment~"SSH brute force"
```

Failed logins appear in the log as `login failure for user <name> from <address> via ssh`:

```ros
/log/print where message~"login failure"
```

A blocked address stays blocked until it has not tried to connect for a day: new connection attempts from a blacklisted source renew its entry. To unblock an address, remove its entries from all four lists, for example from the console or from another address:

```ros
/ip/firewall/address-list/remove \
    [find list~"^connection|^bruteforce" address=203.0.113.10]
```

## How many guesses the rules allow

The RouterOS SSH server accepts up to nine password attempts on one connection before it closes the connection. With the timeouts of the example:

- A source that connects quickly gets three connections, up to 27 password guesses, before it is blocked for a day.
- A source that waits more than 5 minutes between connections never leaves the first stage and is never blocked: up to 9 guesses every 5 minutes, about 2,600 guesses per day.

The growing timeouts are what makes the rules effective. If all three lists used a 1-minute timeout, a source could open three connections every minute without being blocked, up to 27 guesses per minute. To slow down a patient attacker further, raise the timeout of `connection1`: with 30 minutes, the limit falls to 9 guesses every 30 minutes. A longer first stage also makes it easier to block yourself.

Even with these rules, a weak password can be guessed over time. Keys or long, unique passwords remain the real protection.

## Related topics

- [DDoS protection](ddos-protection) uses the same address-list technique with `dst-limit` to detect floods of new connections towards hosts behind the router.
- [Port knocking](port-knocking) keeps SSH closed until a client sends the right sequence of connection attempts.
- The [connection rate](connection-rate) matcher measures the throughput of a single connection; it does not count connections.

For all rule properties, see [`/ip/firewall/filter`](../../cli-reference/ip/firewall/filter/) and [`/ip/firewall/address-list`](../../cli-reference/ip/firewall/address-list) in the CLI reference.
