# snmp

> The /snmp menu turns the SNMP agent on and sets its general behavior: the engine ID that identifies the router to SNMPv3 clients, the address and VRF it answers on, and how traps are sent. The agent is off by...

-----------

## snmp 
**Type:** Settings Directory

The `/snmp` menu turns the SNMP agent on and sets its general behavior: the engine ID that identifies the router to SNMPv3 clients, the address and VRF it answers on, and how traps are sent. The agent is off by default. The communities that may actually read or write are defined in the `/snmp/community` menu. See the [SNMP guide](../../diagnostics-monitoring-and-troubleshooting/snmp) for configuration examples.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool">Whether the SNMP agent answers queries and sends traps. Default: no.</ArgTableRow>
<ArgTableRow arg="contact" typ="string">Administrative contact information, readable by any collector. Default: empty.</ArgTableRow>
<ArgTableRow arg="location" typ="string">Administrative location information, readable by any collector. Default: empty.</ArgTableRow>
<ArgTableRow arg="engine-id-suffix" typ="string">Tail of the agent's SNMP engine ID. The router builds the full engine ID from the prefix `80003a8c04` and the given value written as ASCII hex; for example the suffix `1234` produces the engine ID `80003a8c0431323334`. Leave the suffix empty to use the automatically generated engine ID, which is different on each router and stays the same across reboots. Default: empty.</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip: ipAddr
, ip6: ip6Addr
 }">Source address for SNMP messages. With a value set, the agent answers only requests addressed to that address, and an IPv4 value stops it answering IPv6 requests. Default: `::` - replies come from the address of the interface that received the request.</ArgTableRow>
<ArgTableRow arg="trap-target" typ="object { ip-addresses: alt { ipv6: ip6Addr
, ip: ipAddr
 }
 }">List of collector addresses that receive SNMP traps; traps go to UDP port 162 on each address. Default: empty.</ArgTableRow>
<ArgTableRow arg="trap-community" typ="enum">Community used to send traps. It must exist in the `/snmp/community` menu; its security level decides how the trap is protected. Default: `public`.</ArgTableRow>
<ArgTableRow arg="trap-version" typ="enum (1 | 2 | 3) { 1:0, 2:1, 3:3 }">
Version of the trap protocol.
- `1` (default) - SNMPv1 trap.
- `2` - SNMPv2c trap.
- `3` - SNMPv3 trap, using the authentication and encryption of the `trap-community`.
</ArgTableRow>
<ArgTableRow arg="trap-generators" typ="multi { array-id, generator: enum
 }">
Events that generate a trap; several values can be combined.
- `interfaces` - A `linkDown`/`linkUp` trap when an interface changes state; narrow this with `trap-interfaces`.
- `start-trap` - A trap when the SNMP service starts.
- `temp-exception` (default) - A trap when the CPU temperature reaches the `/system/health` threshold.
</ArgTableRow>
<ArgTableRow arg="trap-interfaces" typ="object { interface: iface_enum
 }">List of interfaces whose state changes generate `interfaces` traps; other interfaces stay quiet. Empty means any interface. Default: empty.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">VRF the SNMP agent runs in. Requests that arrive in other VRFs get no reply. Default: `main`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="engine-id" typ="string">Full SNMP engine ID of the agent: the prefix `80003a8c04` followed by the `engine-id-suffix` value written as ASCII hex, or the automatically generated ID when the suffix is empty. SNMPv3 clients address the agent by this value and include it in every request.</ArgTableRow>
</ArgTable>
