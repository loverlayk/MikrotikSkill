# Layer7

> Layer7 protocol inspection matches regular expressions against the payload of IPv4 ICMP, TCP and UDP streams. The page covers the inspection window, direction requirements, regular expression syntax, examples for RDP...

# Layer7

Layer7-protocol matches a regular expression against the payload of an IPv4 ICMP, TCP or UDP stream. Use it when the port does not identify the protocol reliably, for example when an application runs on non-standard ports, and the payload contains a recognizable signature. The examples use RDP and Telnet because both payloads contain distinctive strings.

:::warning
The L7 matcher is resource-intensive. Use it only for specific traffic. Do not use it for generic web blocking: HTTPS and QUIC encrypt the HTTP request and response, so the matcher cannot see the web traffic, and inspecting all web traffic increases CPU and memory use. Use other features to block web pages by URL.
:::

## Configuration

Define a pattern in the `layer7-protocol` menu, then reference it from a firewall rule. The matcher is available in the IPv4 firewall; it is not available in `/ipv6/firewall` or `/ip/firewall/raw`.

```ros
/ip/firewall/layer7-protocol
add name=rdp regexp="rdpdr.*cliprdr.*rdpsnd"

/ip/firewall/filter
add chain=forward action=drop protocol=tcp layer7-protocol=rdp \
    log=yes log-prefix=rdp
```

Add regular firewall rules before the L7 rule to accept traffic that is already known by address or port. Those packets are not passed to the matcher:

```ros
/ip/firewall/filter
add chain=forward action=accept protocol=tcp dst-port=80
add chain=forward action=accept protocol=tcp dst-port=443
add chain=forward action=drop protocol=tcp layer7-protocol=rdp
```

The accepted ports are unrelated web traffic. Do not accept the traffic you want the L7 rule to match before the rule, because the accept rule bypasses the matcher.

The pattern matches a payload that contains the three RDP channel names in this order. `.*` matches any characters between them; escape a literal dot as `\\.` in a command (stored as `\.`), because an unescaped `.` matches any character. The example does not restrict the port, so the matcher sees both directions.

Check the rule counters with `/ip/firewall/filter/print stats`, or the log entries with the `rdp` prefix. The counter increases only when the pattern matches.

An L7 drop rule acts after the pattern is found. Packets sent before the match, including the packet that carries the signature, can already be forwarded, so the first exchange can complete. Use L7 to classify traffic or to stop a session after the signature appears, not as a guarantee that no data is exchanged.

## Match traffic to the router

A rule in the `forward` chain can see both directions of a connection when it has no address or port conditions. A rule in the `input` chain sees only packets addressed to the router, so use the same `layer7-protocol` in an `output` rule as well. Without the second rule, the matcher does not receive the packets in the other direction and a pattern from that direction does not match.

The following example matches the Telnet negotiation that the router sends when a client connects to its Telnet service:

```ros
/ip/firewall/layer7-protocol
add name=telnet regexp="^\\xff[\\xfb-\\xfe].\\xff[\\xfb-\\xfe].\\xff[\\xfb-\\xfe]"

/ip/firewall/filter
add chain=input action=accept protocol=tcp dst-port=23 \
    layer7-protocol=telnet
add chain=output action=accept protocol=tcp src-port=23 \
    layer7-protocol=telnet
```

The pattern matches the first eight bytes of the Telnet negotiation: `\xff`, a command byte in the range `\xfb` to `\xfe`, and an option byte, then the same pair once more, then `\xff` and a command byte. The input rule matches the client-to-server port (`dst-port=23`); the output rule matches the server-to-client port (`src-port=23`). Both rules need the same `layer7-protocol`; use the action you need in each chain. To block matching connections, use `action=drop` in both.

Write hex escapes with a double backslash in a script or command (`\\xff`); the router stores the pattern as `\xff`.

## Troubleshooting

### The rule does not match

Check these points in order:

- **Encrypted traffic.** HTTPS and QUIC encrypt the application data, so the matcher cannot see the HTTP request or response.
- **Inspection window.** The matcher examines at most the first 10 packets that carry data or the first 2 KB of application payload, whichever comes first. TCP ACK-only packets are not counted, and the 2 KB includes application headers such as HTTP; IP and TCP headers are not counted. A pattern that appears later in the stream is not found. For example, a large HTTP response can place a signature beyond 2 KB.
- **Direction.** A rule with address or port conditions sees only the packets that match them. If the pattern can appear in the response, do not restrict the rule to the request direction. Use a rule that matches both directions, or add a rule with the reversed conditions. In the `input` chain, add the same matcher to an `output` rule. For other chains, make sure a rule sees both directions.
- **Case.** Matching is case-insensitive. A pattern cannot distinguish uppercase from lowercase.
- **Regular expression syntax.** Hex escapes such as `\x2f` work, and character ranges such as `[0-9]` work. POSIX character classes such as `[[:digit:]]` do not match, and octal escapes such as `\057` do not work. RouterOS rejects a regexp that it cannot compile when you add the definition, with an error such as `bad regexp: unmatched ()`.
- **Rule order.** Rules are evaluated in order. Once an L7 rule matches a connection, later L7 rules do not inspect it, so put the most specific rule first. Add regular accept rules before L7 rules to reduce the traffic the matcher sees.
- **Menu.** L7 is available only in the IPv4 firewall, not in `/ipv6/firewall` or `/ip/firewall/raw`.

### CPU and memory use

Each connection is inspected separately until the pattern matches or the window ends. Many connections, or broad patterns, increase CPU and memory use. Keep the number of L7 rules small, put regular matchers before them, and do not use L7 for generic web traffic. No fixed memory or CPU figure applies: the cost depends on the number of connections the rule inspects and on the pattern.

## Technical details

The matcher collects data from a connection and searches for the regular expression in it. It stops at 10 data packets or 2 KB of application payload, whichever is reached first. The 2 KB includes application headers such as HTTP; IP and TCP headers are not counted. If the pattern is not found, the matcher stops inspecting the connection, frees its state and leaves the protocol unknown. If the pattern is found, the firewall rule matches, and later L7 rules do not inspect the connection.

Matching is case-insensitive: both the pattern and the payload are compared without regard to case.

The `regexp` value uses a regular expression syntax with these behaviors: hex escapes (`\xNN`) and character ranges (`[0-9]`) are supported; POSIX character classes (`[[:digit:]]`) and octal escapes are not. Write a backslash as `\\` in a script or command so that the stored value contains `\xNN`.

Patterns for common protocols are collected in the [l7-filter project](https://l7-filter.sourceforge.net/Pattern-HOWTO), but check each pattern on your traffic: the project's syntax and the RouterOS regexp engine may differ.

All properties of the `/ip/firewall/layer7-protocol` menu are described in the [`/ip/firewall/layer7-protocol`](../../cli-reference/ip/firewall/layer7-protocol/) CLI reference.
